# Open Challenge — Algorithm Notes

## Program states

| State or phase | What happens | When it moves on |
|---|---|---|
| Initialization | Set up devices and encoder references | All device setup steps succeed |
| Ready | Wait for the operator | CENTER button is pressed |
| Gyro calibration | Estimate drift while stationary | Calibration is accepted |
| Navigation | Stay near the corridor centre and keep heading | An opening is confirmed |
| Corner | Turn toward the next absolute heading | Heading tolerance or timeout |
| Post-turn lockout | Avoid detecting the same opening twice | Lock distance has been travelled |
| Return approach | Estimate the remaining distance to the start | Final distance is reached |
| Finalization | Stop and save the data | Log file is written |

## How the navigation readings are used

1. Read the left and right ultrasonic sensors.
2. Add the readings to short histories.
3. Use median filtering to reduce single-reading spikes.
4. Reject readings when the robot's heading makes the wall geometry unreliable.
5. Calculate lateral error from the difference between the two wall distances.
6. Apply a deadband and combine lateral and heading corrections.
7. Limit the steering command and apply the close-wall override.
8. Send commands to both drive motors and record the data.

## How we detect a corner

The program accepts an opening only after the threshold has been exceeded for several readings in a row. It then uses a lockout distance after the turn so the previous opening is not detected again. The direction is estimated from the first opening and kept for the rest of the route.

## Main groups of settings

The Open Challenge source groups its settings around wheel and encoder geometry, gyro drift and heading direction, ultrasonic visibility limits, lateral and heading gains, corner steering and stopping, and the final return-distance calculation.

These values describe the current program configuration. We have not added a physical tuning log or before-and-after test results to the repository.

## Evidence

These notes explain the algorithm in our Python program. They do not report completed tuning sessions or measured performance on the track.