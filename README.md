# stateaxis-length-aware-queue

Extension ID: `org.vllm-hust.stateaxis-length-aware-queue`

Length-aware prefill tiers with queue aging and anti-starvation.

This repository is the independent MOD boundary for StateAxis issues [#19](https://github.com/Qixin-Gaoke/stateaxis/issues/19).
It is deliberately `import_only`, default-off, and cannot be enabled. The split does
not inherit correctness, device, performance, or publication qualification from the
aggregate StateAxis repository.

## Evidence boundary

Status: **neutral**.

Exactness and lifecycle gates passed without a significant end-to-end benefit.

The copied evidence and its SHA-256 are recorded in `PROVENANCE.json`. Negative,
failed, and inconclusive results are retained. Microbenchmarks and component results
must not be restated as online end-to-end gains.

## Install and inspect

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-length-aware-queue
vllm-hust-ext extension check org.vllm-hust.stateaxis-length-aware-queue
```

Discovery does not enable the MOD. A future active revision must extract an
independently reviewable implementation, declare exclusive resources where needed,
and pass exactness, lifecycle, release, failure-recovery, and matched real-online
gates.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
