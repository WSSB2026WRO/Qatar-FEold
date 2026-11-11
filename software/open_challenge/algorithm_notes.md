# Open Challenge — Algorithm Notes

## State model

| State / phase | Purpose | Exit condition |
|---|---|---|
| Initialization | Configure devices and encoder references | All constructors succeed |
| Ready | Wait for operator start | CENTER button |
| Gyro calibration | Estimate stationary drift | Calibration accepted |
| Navigation | Centre in corridor and maintain heading | Opening confirmation |
| Corner | Rotate to next absolute heading | Heading tolerance or timeout |
| Post-turn lockout | Prevent duplicate opening detection | Lock distance travelled |
| Return approach | Estimate remaining distance to start | Final distance reached |
| Finalization | Stop and save data | Log write completes |

## Navigation signal path

1. Read left and right ultrasonic sensors.
2. Add readings to short histories.
3. Use median filtering to reduce isolated spikes.
4. Reject readings when heading makes wall geometry unreliable.
5. Compute lateral error from the difference between left and right ranges.
6. Apply a deadband and combine lateral and heading corrections.
7. Clamp the steering command and apply the close-wall override.
8. Command both drive motors and record telemetry.

## Corner detection logic

An opening is accepted only after the threshold is exceeded for consecutive samples. A lockout distance after each turn prevents the previous opening from being detected again. The route direction is inferred from the first opening and then retained.

## Parameter groups

The Open Challenge source groups its main configuration around wheel and encoder geometry, gyro drift and heading direction, ultrasonic visibility thresholds, lateral and heading gains, corner steering and stopping logic, and the final return-distance estimate. These parameters define the configured control behaviour; no physical tuning log or before-and-after performance dataset is included in this repository snapshot.

## Evidence scope

These notes describe the algorithm represented by the Python source. They are not a record of completed physical tuning sessions or measured track performance.
