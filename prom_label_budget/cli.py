import argparse, json, pathlib, sys
from .core import run

def main():
    parser=argparse.ArgumentParser(description="Offline normalized-input explainer; see README limits")
    parser.add_argument("input",type=pathlib.Path)
    args=parser.parse_args()
    try:
        with args.input.open("rb") as f:
            raw=f.read(1048577)
        if len(raw)>1048576:
            raise ValueError("input exceeds 1 MiB")
        data=json.loads(raw.decode("utf-8"))
        if not isinstance(data,dict):
            raise ValueError("top-level JSON object required")
        print(json.dumps(run(data),sort_keys=True,ensure_ascii=True,allow_nan=False))
    except (OSError,UnicodeError,ValueError,TypeError,KeyError) as exc:
        print("input error: "+str(exc),file=sys.stderr)
        return 2
    return 0
