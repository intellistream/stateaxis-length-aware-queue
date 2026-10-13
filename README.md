# stateaxis-length-aware-queue

Extension ID: `org.vllm-hust.stateaxis-length-aware-queue`

This active experimental MOD is the independently reviewable authority contract
for StateAxis bounded cold-prefill length classes and queue aging. Shuhao Zhang
(Tony) is directly responsible; no advisor is declared.

The reviewed mechanism admits only cold prefill requests without state. It
classifies prompts at 128 and 512 tokens, applies a 250ms anti-starvation aging
bound, caps the candidate snapshot at 64 requests and 1,048,576 tokens, and
reorders the complete selected plan and its traces atomically. Stateful,
decode, ambiguous-identity and clock-regression cases fail closed to control.

## Activation

Activation is default-off and must go through vLLM-HUST Extension Manager/ECPA:

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-length-aware-queue
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension plan org.vllm-hust.stateaxis-length-aware-queue
```

StateAxis rejects direct `STATE_ENGINE_ISSUE19_TELEMETRY` and
`STATE_ENGINE_ISSUE19_AUTHORITY` activation. The Host validates this MOD's
version and research-manifest SHA-256, binds the identity into assembly/state
graph, and exposes lifetime decision, authority, fallback, reorder and aged
promotion counters.

Rollback is to disable or forget the extension. The unchanged control scheduler
then remains authoritative and all MOD identity/effect counters stay absent or
zero.

## Evidence boundary

Historical Qwen2.5-14B varied-length real-NPU evidence contains three fresh
process runs per arm. Exactness and lifecycle passed, candidate authority
applied 51 times per run, and fallback remained zero. Mean throughput was
4.542923 requests/s control versus 4.511304 candidate (`-0.6960%`). The three
paired deltas have a 95% Student-t interval of `[-2.0359%, +0.6478%]`, so the
experiment resolves no benefit and retains a negative point estimate. Peak HBM
was effectively unchanged. Therefore no speedup is claimed and the mechanism
remains opt-in.

The active ECPA revision adds matched process/runtime evidence but no fresh
accelerator performance run. Raw historical bytes and the derived statistical
record are now local to this repository. See [EVIDENCE.md](EVIDENCE.md).

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
