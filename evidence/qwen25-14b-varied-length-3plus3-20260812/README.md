# Qwen2.5-14B varied-length matched real-NPU result

Evidence label: `historical_matched_real_npu_workload_scoped_negative`

This directory makes the frozen Issue #19 result self-contained in the
canonical MOD repository. The four source files are byte-identical copies of
the StateAxis evidence named in the release audit. `RESULT.json` adds only a
transparent statistical summary derived from `raw.json`.

## Result

The campaign contains three fresh processes per arm on Ascend NPU7. Each run
contains 51 cold-prefill requests drawn from fixed 14-, 225- and 897-token
classes. All six runs are exact. Candidate authority applied to all 51 requests
in every candidate run, with zero fallback and zero identity mismatch.

| Arm | Run 1 req/s | Run 2 req/s | Run 3 req/s | Mean req/s | Mean peak HBM MiB |
|---|---:|---:|---:|---:|---:|
| Control | 4.513647 | 4.557087 | 4.558035 | 4.542923 | 52666.208 |
| Candidate | 4.510302 | 4.514057 | 4.509552 | 4.511304 | 52666.332 |

The candidate mean throughput point estimate is `-0.6960%`. Per-pair deltas
are `-0.0741%`, `-0.9442%` and `-1.0637%`; their mean is `-0.6940%` with a
two-sided 95% Student-t interval of `[-2.0359%, +0.6478%]`. With only three
pairs the interval crosses zero. The correct conclusion is therefore “no
resolved improvement; negative point estimate,” not a general regression or
speedup claim.

## Boundary

This result applies to the frozen r1 binary and this varied-length workload.
The active ECPA revision has matching software activation evidence but has not
been rerun on NPU. The original closure explicitly says not to repeat the same
workload; future work must use a materially different queue composition and a
new artifact identity, such as sustained head-of-line blocking with a much
higher long-request fraction and explicit starvation-tail gates.
