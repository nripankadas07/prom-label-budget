# Security

Offline diagnostic with strict documented input limits. No network, subprocess or filesystem lookup occurs in the core engine. The CLI reads only the explicit JSON path. It does not execute SSH directives or extract container files. Do not include secrets in reports; use synthetic reproductions and omit private hostnames, paths and label values. This is not a production security boundary.
