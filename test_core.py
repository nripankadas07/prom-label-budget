import json, os, pathlib, subprocess, sys, tempfile, unittest
from prom_label_budget.core import run

CASES = [({'series': []}, {'unique_series': 0, 'projected_series': 0}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}, {'__name__': 'm', 'user': 'a', 'code': '200'}]}, {'duplicates': 1, 'unique_series': 1}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}, {'__name__': 'm', 'user': 'b', 'code': '200'}], 'drop': ['user']}, {'projected_series': 1, 'lost_identity_count': 1, 'collision_group_sizes': [2]}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}, {'__name__': 'n', 'user': 'b', 'code': '200'}], 'drop': ['user']}, {'projected_series': 2}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}, {'__name__': 'm', 'user': 'b', 'code': '500'}], 'drop': ['user']}, {'projected_series': 2}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}], 'drop': ['unused']}, {'projected_series': 1}), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}], 'drop': ['__name__']}, 'error'), ({'series': [{}]}, 'error'), ({'series': [{'__name__': 'm', 'bad-label': 'a'}]}, 'error'), ({'series': [{'__name__': 'm', 'label': 2}]}, 'error'), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}], 'drop': ['user', 'user']}, 'error'), ({'series': [{'__name__': 'm', 'user': 'a', 'code': '200'}], 'drop': ['bad-label']}, 'error')]

class ContractTests(unittest.TestCase):
    def test_cli_demo(self):
        r=subprocess.run([sys.executable,"-c","from prom_label_budget.cli import main; raise SystemExit(main())","example.json"],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIsInstance(json.loads(r.stdout),dict)

    def test_cli_malformed(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)/"bad.json";path.write_text("[broken")
            r=subprocess.run([sys.executable,"-c","from prom_label_budget.cli import main; raise SystemExit(main())",str(path)],text=True,capture_output=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(r.stdout,"")
            self.assertIn("input error",r.stderr)

def make_case(data,expected):
    def test(self):
        before=json.dumps(data,sort_keys=True)
        if expected=="error":
            with self.assertRaises(ValueError): run(data)
        else:
            result=run(data)
            if expected=="opaque":
                self.assertEqual(set(result["paths"]),{"d","d/new","other"})
                self.assertEqual(result["whiteouts"][0]["removed"],["d/a"])
            elif expected=="order":
                self.assertEqual([r["start"] for r in result["requests"]],[50,0])
                self.assertEqual(result["coverage"],[[0,9],[50,59]])
            else:
                for key,value in expected.items(): self.assertEqual(result[key],value)
        self.assertEqual(json.dumps(data,sort_keys=True),before,"input mutated")
    return test
for i,(data,expected) in enumerate(CASES):
    setattr(ContractTests,"test_contract_%02d"%i,make_case(data,expected))

if __name__=="__main__": unittest.main()
