# System Reliability and Failure Mode Analysis

## 1. Rating method

Use a 1–10 scale for severity (S), occurrence (O), and detectability (D). The risk priority number is:

[
RPN=S\times O\times D
]

The ratings below are preliminary design-review estimates, not field-derived failure statistics. They must be updated from actual test and maintenance records.

## 2. Preliminary FMEA

| Subsystem | Failure mode | Effect | Detection | Recommended mitigation |
|---|---|---|---|---|
| Drive | Wheel slip | Distance and turn error | Encoder/gyro disagreement | Tune acceleration and verify traction |
| Drive | Motor stall | Vehicle stops or deviates | Encoder progress timeout | Stop and inspect drivetrain |
| Steering | Linkage backlash | Heading oscillation | Angle repeatability test | Reduce clearance and inspect joints |
| Steering | Mechanical binding | High load or incomplete turn | Current/load proxy and encoder timeout | Full-sweep clearance test |
| Gyro | Bias drift | Heading error | Stationary drift test | Recalibration and bounded correction |
| Ultrasonic | Multipath echo | False wall position | Plausibility and continuity checks | Sensor alignment and filtering |
| Pixy2 | Misclassification | Wrong passing side | Signature confidence and temporal confirmation | Re-train signatures and verify lighting |
| Pixy2 | I²C communication loss | Missing obstacle data | Consecutive error counter | Safe stop and cable inspection |
| Printed parts | Layer separation | Linkage failure | Visual inspection | Correct orientation and print parameters |
| Battery | Voltage sag | Reduced speed or reset | Voltage logging | Battery health and load test |
| Parking | Position estimate error | Misaligned final pose | Boundary and encoder cross-check | Recalibrate lot geometry |

## 3. Safety priorities

Highest priority should be assigned to failures that can cause uncontrolled motion, steering lock, loss of obstacle detection, or mechanical separation. Testing should begin at low speed and progress only after the previous stage is repeatable.

## 4. Maintenance schedule

### Before each run
- inspect wheels and tire surfaces;
- verify steering travel and fasteners;
- inspect printed components;
- verify sensor mounting and cables;
- confirm battery state;
- verify correct software version.

### After each test session
- inspect for cracks and loosened joints;
- archive logs;
- record anomalies;
- review motor and sensor behaviour;
- update the maintenance record.

## 5. Change control

Any change to steering geometry, sensor mounting, drive ratio, camera position, or controller gains should trigger a targeted regression test. Preserve the previous working configuration and record the reason for the change.
