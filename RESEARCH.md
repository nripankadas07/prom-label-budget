# Qualitative research — 12 October 2026

Observed 2026-10-12 06:35:23 UTC. Search queries: `prometheus cardinality sort:stars-desc`.

GitHub search requested star ordering through query qualifiers. Direct repository-search REST fetch was unsupported; connector results were noisy and some irrelevant matches were rejected. Established adjacent tools were added explicitly, with current repository metadata, README and three recent open issue/PR records inspected. Ranking is the highest-star relevant comparable among these found sources, not an exhaustive global ranking. Code inspected for one relevant comparable in each area; complete competitor installations and full feature inventories were not tested.

| Repository | Stars | Last pushed UTC | API license |
| --- | ---: | --- | --- |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 66487 | 2026-10-11T20:22:28Z | Apache-2.0 |
| [VictoriaMetrics/VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) | 17843 | 2026-10-11T03:19:55Z | Apache-2.0 |
| [thought-machine/prometheus-cardinality-exporter](https://github.com/thought-machine/prometheus-cardinality-exporter) | 50 | 2026-09-07T22:33:45Z | Apache-2.0 |

Highest-star relevant/adjacent source found in this inspected set: prometheus/prometheus.

Prometheus provides a full monitoring/querying system; VictoriaMetrics provides time-series storage and analytics; the cardinality exporter queries Prometheus TSDB status and offers service discovery. This candidate is an offline projection over captured normalized series labels. It does not scrape or predict memory, and merging identities does not prove correct aggregation of metric values. Current exporter instructions use GHCR rather than Docker Hub.

Installability, examples and support were assessed from current README/issue evidence. No measured time-to-result, reliability ranking, comparative speed or superiority claim is made. Our offline installed example passes; that establishes our behavior only. Specific demand remains inferred, as stated in README. All implementation code is original; no third-party source or prose was imported.

## Current evidence links

- prometheus/prometheus: [README](https://github.com/prometheus/prometheus/blob/main/README.md), observed blob `0465897e5cc16963a84fa6ba56b64b5dfa764009`.
  - [PR](https://github.com/prometheus/prometheus/pull/19998) — web/api: add experimental native metric metadata endpoint
  - [PR](https://github.com/prometheus/prometheus/pull/19997) — promtool: support stdin consistently for check config and rule unit tests
  - [PR](https://github.com/prometheus/prometheus/pull/19996) — storage/remote: use synctest for remote read gate wait tests
- VictoriaMetrics/VictoriaMetrics: [README](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/README.md), observed blob `518fdea1989291a3f4bf6e6bab414feb8a1479eb`.
  - [PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11744) — lib/promscrape/discovery/ec2: add all_enis option for creating a target per network interface
  - [PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11743) — Add -storageNodeLabelIndex flag
  - [PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11742) — dashboards: fix cluster resource filters
- thought-machine/prometheus-cardinality-exporter: [README](https://github.com/thought-machine/prometheus-cardinality-exporter/blob/master/README.md), observed blob `9b6e89caca205c2a5d18e724cc150b7df53c9f73`.
  - [PR](https://github.com/thought-machine/prometheus-cardinality-exporter/pull/146) — Bump golang from 1.26.4-alpine3.23 to 1.27.1-alpine3.23
  - [PR](https://github.com/thought-machine/prometheus-cardinality-exporter/pull/144) — Bump github.com/stretchr/testify from 1.11.1 to 1.12.0
  - [PR](https://github.com/thought-machine/prometheus-cardinality-exporter/pull/143) — Bump github.com/sirupsen/logrus from 1.9.4 to 1.10.0
