# Benchmark evidence

This showcase publishes one retained, narrowly scoped measurement rather than
a generic latency claim. The evidence comes from the Pump.fun unsigned-build
benchmark release `b90c5cd3c5bdc124cb830bd7e17260c1a3e03400` (23 July 2026).

The retained benchmark page reports 400/400 unsigned builds across eight equal
cohorts of 50 requests, with 16/16 warmups passed and zero signing attempts or
broadcasts.

## Fast-mode distribution

The following distribution is for 200 measured fast-mode requests:

| Operation | p50 | p95 | p99 |
| --- | ---: | ---: | ---: |
| Server build — unsigned transaction construction | 0.377 ms | 0.529 ms | 1.405 ms |
| Same-host HTTP — request start to complete JSON response | 4.502 ms | 64.595 ms | 304.872 ms |

## Measurement boundary

- The server-build clock covers API-owned unsigned transaction construction.
- The same-host HTTP clock covers benchmark-client request start through the
  complete unsigned JSON response received through the Virginia edge path.
- Warmups are excluded. Percentiles use the `nearest_rank_v1` method:
  ascending sort, one-indexed rank `max(1, ceil(percentile × n))`, rounded to
  three decimal places.
- The measurement excludes wallet signing, simulation, submission,
  confirmation, trade-event observation, customer network distance and RPC
  choice.
- These are exact-release Pump.fun beta measurements, not an SLA, fastest-run
  claim or forecast of customer end-to-end latency. PumpSwap is outside this
  result.

## Evidence requirements

Any future measurement should retain the same context:

| Field | Required detail |
| --- | --- |
| Operation | The exact operation measured, such as a build, validation or observed API response. |
| Environment | Local, devnet or another environment, including relevant machine and runtime conditions. |
| Sample | Request count, warm-up policy and whether failures were included. |
| Timing | Start and end timestamp definitions plus the percentile or summary used. |
| Dependencies | Provider or data mode and whether network time is included. |
| Limitations | What the measurement does not prove. |

Without that context, the repository makes no generic latency or production
performance claim.
