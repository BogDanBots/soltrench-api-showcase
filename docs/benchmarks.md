# Benchmark methodology

The public version should report a measurement only when the evidence records:

| Field | Required detail |
|---|---|
| Operation | The exact operation measured, such as a build, validation or observed API response. |
| Environment | Local, devnet or other environment; relevant machine/runtime conditions. |
| Sample | Request count, warm-up policy and whether failures were included. |
| Timing | Definition of start/end timestamps and percentile or summary used. |
| Dependencies | Provider/data mode and whether the measurement includes network time. |
| Limitations | What the result does not prove. |

No generic “low latency” or “production performance” claim should be published without this context. The approximately 200 ms class observation mentioned in planning is not included here as a result until its exact evidence and measurement boundary are verified.
