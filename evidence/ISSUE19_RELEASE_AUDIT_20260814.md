# Issue #19 release audit

> **Document role: point-in-time report, not current repository status or a task
> assignment.** Current classification and priorities live only in
> [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

Issue #19 is closed as a default-off, no-significant-difference experiment.
The frozen `issue19-varied-length-20260812-r1` NPU7 evidence contains three
fresh-process runs per arm. All six runs are exact, candidate authority applies
51 times per run, and identity-set, lifecycle, and fallback counts are zero.
Control/candidate mean throughput is 4.543/4.511 request/s (candidate about
-0.70%); peak HBM is effectively unchanged.

The original NPU artifact is not relabeled as the release source. This PR
publishes those immutable raw bytes and reconstructs the previously uncommitted
production hook on current main. The reconstruction additionally makes Issue
#19 telemetry/authority independent of Issue #4 and atomically reorders both
request IDs and their selection traces. Offline regressions prove default-off
plan identity, legal cold-prefill reorder, trace alignment, and fail-closed
stateful/decode scope. Per the frozen closure instruction, the 3+3 workload was
not rerun; therefore the historical performance numbers apply only to the
recorded r1 artifact, while the current source is supported by offline semantic
equivalence tests.

Canonical evidence:

- `benchmarks/issue19_scheduler_cpu/native_serving_gate_20260812/varied_length_r1_raw.json`
  SHA-256 `1b185eb6c87bb97608414e9056718f8fdc9c9ea9072b8c8339dc1ea4e3a23a4b`
- `benchmarks/issue19_scheduler_cpu/native_serving_gate_20260812/varied_length_r1_status.json`
  SHA-256 `8fe002e01a1eba87f203f96167b514070fbbe39bda6d6e75cbda309e91cc088b`
- `benchmarks/issue19_scheduler_cpu/native_serving_gate_20260812/varied_length_r1_identity.json`
  SHA-256 `dc128f94b25ae6f70660d1182f9039940782f3fdaeea6ae41a3f6cafe6072c94`
- `benchmarks/issue19_scheduler_cpu/native_serving_gate_20260812/varied_length_r1_summary.md`
  SHA-256 `d38bd1f4bbeb836e074de44e7fcea898577f3c0a912f76d4a3491ce19c8e8b91`

Decision: do not enable by default and do not repeat the same workload. A
future revisit requires a materially different queue composition and a new
artifact identity.
