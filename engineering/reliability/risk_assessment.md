# System Reliability and Failure Mode Analysis

## 1. Rating method

Use a 1–10 scale for severity (S), occurrence (O), and detectability (D). The risk priority number is:

\[
RPN=S\times O\times D
\]

The ratings in this register are engineering review scores used to prioritize design controls.

## 2. Failure mode and effects analysis

| Subsystem | Failure mode | Effect | Detection | Recommended mitigation |
|---|---|---|---|---|
| Drive | Wheel slip | Distance and turn error | Encoder/gyro disagreement | Tune acceleration and verify traction |
| Drive | Motor stall | Vehicle stops or deviates | Encoder progress timeout | Stop drive and inspect drivetrain |
| Steering | Linkage backlash | Heading oscillation | Angle repeatability test | Reduce clearance and inspect joints |
| Steering | Mechanical binding | High load or incomplete turn | Encoder timeout and travel inspection | Full-sweep clearance test |
| Gyro | Bias drift | Heading error | Stationary drift test | Recalibration and bounded correction |
| Ultrasonic | Multipath echo | False wall position | Plausibility and continuity checks | Sensor alignment and filtering |
| Pixy2 | Misclassification | Wrong passing side | Signature confidence and temporal confirmation | Re-train signatures and verify lighting |
| Pixy2 | I²C communication loss | Missing obstacle data | Consecutive error counter | Safe stop and cable inspection |
| Printed parts | Layer separation | Linkage failure | Visual inspection | Correct orientation and print parameters |
| Battery | Voltage sag | Reduced speed or reset | Voltage observation | Battery health and load test |
| Parking | Position estimate error | Misaligned final pose | Boundary and encoder cross-check | Recalibrate parking geometry |

## 3. Critical risk controls

Priority controls address uncontrolled motion, steering lock, loss of obstacle detection, and mechanical separation. Validation should progress from low-speed functional checks to complete mission trials.

## 4. Maintenance schedule

### Before each run
- inspect wheels and tire surfaces;
- verify steering travel and fasteners;
- inspect printed components;
- verify sensor mounting and cables;
- confirm battery condition;
- verify the software version.

### After each test session
- inspect for cracks and loosened joints;
- archive run logs;
- record anomalies and corrective actions;
- review motor and sensor behaviour;
- update the maintenance record.

## 5. Change control

Changes to steering geometry, sensor mounting, drive ratio, camera position, or controller gains require a targeted regression test. Preserve the previous working configuration and document the engineering reason for the revision.
