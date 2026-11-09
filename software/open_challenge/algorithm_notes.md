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

## Parameter tuning sequence

1. Wheel diameter and encoder distance scale.
2. Gyro drift and heading sign.
3. Ultrasonic sensor alignment and visibility thresholds.
4. Lateral gain and heading gain.
5. Corner steering command and stopping logic.
6. Start-return estimate and final slow approach.

Tune at low speed and preserve a baseline log before changing values.
