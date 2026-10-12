# Contributing

Keep changes small and preserve the documented strict subset. Add a meaningful regression for behavior changes. Run `python -m unittest -v`, `python -m compileall -q .`, build a wheel, and verify its installed example and malformed-input failure outside the source tree. Do not broaden unsupported syntax silently.
