# Issue #19 varied-length r1

- Version: `issue19-varied-length-20260812-r1`; official image; NPU7.
- This is independent evidence; r4 files were not modified.
- Oracle double-run exact: `True`; rows short/medium/long = 14/225/897 tokens; outputs 576/1084/16.

## Acceptance
- Six completed runs: `True`; exact: `True`; identity mismatch zero: `True`; fallback zero: `True`.

## Runs
- control r1: exact=True, authority=0, decisions=199, fallback=0, rebuild=0, stale_pop=0, HBM max=55224619008, throughput=4.514 req/s.
  - short: wait p50/p95/max=122.0/667.0/874 ms; TTFT p50/p95/max=85.868223/695.6548143999999/911.268176 ms.
  - medium: wait p50/p95/max=180.0/762.6499999999996/907 ms; TTFT p50/p95/max=108.92048/892.3213169499999/971.50607 ms.
  - long: wait p50/p95/max=304.0/906.0/1085 ms; TTFT p50/p95/max=176.5009055/1119.6546815/1203.879512 ms.
- control r2: exact=True, authority=0, decisions=195, fallback=0, rebuild=0, stale_pop=0, HBM max=55224504320, throughput=4.557 req/s.
  - short: wait p50/p95/max=105.5/741.7000000000002/939 ms; TTFT p50/p95/max=85.768037/666.2996245999997/978.048495 ms.
  - medium: wait p50/p95/max=188.0/942.2999999999998/1151 ms; TTFT p50/p95/max=108.8415005/1058.7868453499998/1215.495947 ms.
  - long: wait p50/p95/max=188.0/816.0/1028 ms; TTFT p50/p95/max=176.0686295/995.9323032499999/1156.461785 ms.
- control r3: exact=True, authority=0, decisions=197, fallback=0, rebuild=0, stale_pop=0, HBM max=55224442880, throughput=4.558 req/s.
  - short: wait p50/p95/max=198.0/712.7999999999998/978 ms; TTFT p50/p95/max=85.702437/798.0675909999998/1016.333095 ms.
  - medium: wait p50/p95/max=145.0/776.8999999999996/1012 ms; TTFT p50/p95/max=108.680702/564.3871845999992/1070.392511 ms.
  - long: wait p50/p95/max=288.0/863.0/1068 ms; TTFT p50/p95/max=176.25799949999998/1036.2118142499999/1195.055068 ms.
- candidate r1: exact=True, authority=51, decisions=198, fallback=0, rebuild=0, stale_pop=0, HBM max=55224774656, throughput=4.510 req/s.
  - short: wait p50/p95/max=213.0/578.3999999999999/765 ms; TTFT p50/p95/max=86.168289/633.8508557999999/801.775207 ms.
  - medium: wait p50/p95/max=281.0/798.0/909 ms; TTFT p50/p95/max=109.01838599999999/922.6421578999999/971.671336 ms.
  - long: wait p50/p95/max=281.0/908.0/1087 ms; TTFT p50/p95/max=176.59934700000002/1118.63766125/1206.451091 ms.
- candidate r2: exact=True, authority=51, decisions=199, fallback=0, rebuild=0, stale_pop=0, HBM max=55224500224, throughput=4.514 req/s.
  - short: wait p50/p95/max=271.0/782.8999999999995/880 ms; TTFT p50/p95/max=85.977035/846.7627461999999/921.812811 ms.
  - medium: wait p50/p95/max=271.0/818.0499999999998/913 ms; TTFT p50/p95/max=109.016097/901.8663086999999/976.858407 ms.
  - long: wait p50/p95/max=326.5/913.0/1093 ms; TTFT p50/p95/max=176.589881/1128.7726440000001/1215.4899 ms.
- candidate r3: exact=True, authority=51, decisions=200, fallback=0, rebuild=0, stale_pop=0, HBM max=55224680448, throughput=4.510 req/s.
  - short: wait p50/p95/max=233.0/954.0/1167 ms; TTFT p50/p95/max=86.050451/1034.4837883999999/1202.625242 ms.
  - medium: wait p50/p95/max=172.5/898.0/987 ms; TTFT p50/p95/max=109.3327705/972.4862959499999/1048.326299 ms.
  - long: wait p50/p95/max=233.0/885.6999999999998/1044 ms; TTFT p50/p95/max=176.633281/970.33529875/1171.198456 ms.

## Interpretation
- Candidate authority was exercised and correctness/lifecycle gates passed. This report deliberately makes no speedup claim; the frozen runtime exposes no isolated selector timer and the cold-process runs include startup/runtime effects.
- The identity note records that varied HTTP oracles are new and double-run exact, while the standalone startup full-oracle remains the previously verified fixture; this is not presented as a new full-model embedding/layer oracle.
