# prom-label-budget

Public alpha prepared on 12 October 2026. **Remote verification pending; not yet a verified launch.**
Original Python implementation, MIT, zero runtime dependencies. AI-assisted development.

Observability engineer reviewing exported series labels before relabeling. Estimate observed series collisions when dropping a dimension without sending production labels to a service.

Deduplicate normalized series, count metric and label cardinality and simulate a drop-label projection, with collision-group counts.

## Install and first useful result

Python 3.10+ (only Linux Python 3.12.14 tested in this preparation). Build requires setuptools 61+ and wheel already available; install into a fresh venv uses only the generated wheel. Run source tests with your build interpreter:

```sh
python -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse .
python -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps wheelhouse/*.whl
.venv/bin/prom-label-budget example.json
python -m unittest -v
```

The included synthetic input documents the exact normalized JSON schema.
Output is deterministic JSON; malformed inputs exit 2. Inputs are limited to 1 MiB.
No network connections, credential reads or writes to input files occur.
Hostnames, identifiers, paths and selected SSH values may be disclosed in output.
Review exported inputs and outputs before sharing. Use synthetic examples for reports.

## Scope and limits

No scraping, PromQL, TSDB memory prediction, storage savings or semantic value aggregation.

Specific demand: Inferred from Prometheus high-cardinality guidance and maintained cardinality tooling; no verified user request.
Discovery: Prometheus relabeling/cardinality examples.
Portfolio distinction: Works on metric-series identity; existing tabular and trace tools do not simulate series projections.
See RESEARCH.md and the bundled research record for alternatives and incomplete research coverage.
No competitor absence, performance superiority or customer-adoption claim.

## Acceptance criteria

- Duplicate series do not inflate counts.
- Metric names remain distinct after projection.
- Validate schemas and reject dropping __name__.

## Support and contribution

Report a reproducible synthetic input, expected result, actual output and Python version.
Keep changes bounded and run the unit suite and clean installed example.
Do not submit private host configuration, production metric labels or credentials.
Security reports should omit secrets; this offline diagnostic is not a security boundary.
The source distribution is the supported install path; no registry release is claimed.
