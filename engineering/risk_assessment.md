# Engineering Risk Assessment

This is the project's qualitative design-level risk register. The entries identify failure modes, effects, detection mechanisms, and associated engineering controls; no numeric risk scores are assigned.

| ID | Hazard / failure mode | Potential effect | Detection | Mitigation |
|---|---|---|---|---|
| R-01 | Gyro drift or incorrect sign | Heading error and missed turns | Stationary drift and rotation test | Recalibration, sign verification, plausibility checks |
| R-02 | Ultrasonic false echo | Incorrect lane estimate | Compare dual sensors and log outliers | Median filter, geometry rejection, close-wall guard |
| R-03 | Camera misclassification | Wrong pillar passing side | Signature test and video review | Lighting control, confirmation frames, threshold calibration |
| R-04 | Camera I²C communication loss | Missing obstacle observations | Consecutive error counter | Controlled stop or safe degraded state |
| R-05 | Drive wheel slip | Odometry and stopping error | Encoder-to-distance comparison | Reduce acceleration, improve traction, calibrate scale |
| R-06 | Steering linkage backlash | Inconsistent cornering | Bidirectional angle test | Reduce play, inspect joints, calibrate actuator map |
| R-07 | Printed-part fracture | Loss of steering or sensor mount | Visual inspection and fit test | Fillets, suitable orientation, material and load testing |
| R-08 | Cable interference | Sensor disconnect or mechanical jam | Full-travel inspection | Cable routing and strain relief |
| R-09 | Parking estimate error | Incorrect final pose | Repeated parking measurements | Improve boundary detection and final alignment |
| R-10 | Battery voltage variation | Speed and response variation | Log battery state | Controlled charging and repeatable test conditions |

For the expanded failure-mode register, scoring method, and maintenance schedule, see [System Reliability and Failure Mode Analysis](reliability/risk_assessment.md).

The table is a qualitative engineering risk record. Its mitigations describe the controls associated with each identified failure mode.
