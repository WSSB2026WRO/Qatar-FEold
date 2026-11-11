# System Reliability and Failure Mode Analysis

## 1. Rating method

Use a 1–10 scale for severity (S), occurrence (O), and detectability (D). The risk priority number is:

\[
RPN=S\times O\times D
\]

No numeric S/O/D ratings are assigned in this baseline register because physical occurrence and detectability evidence has not been recorded. Apply the scale during a documented risk review; RPN is a prioritization aid and does not replace severity-based safety controls.

## 2. Failure mode and effects analysis

| Subsystem | Failure mode | Effect | Detection | Recommended mitigation |
|---|---|---|---|---|
| Drive | Wheel slip | Distance and turn error | Encoder/gyro disagreement | Tune acceleration and verify traction |
| Drive | Motor stall | Vehicle stops or deviates | Not implemented as a dedicated source-level stall detector; verify with an encoder-progress test | Add a bounded progress timeout and safe-stop response after validating thresholds on hardware |
| Steering | Linkage backlash | Heading oscillation | Angle repeatability test | Reduce clearance and inspect joints |
| Steering | Mechanical binding | High load or incomplete turn | Existing manoeuvre timeout plus physical full-travel inspection | Verify clearance and actuator load across the complete steering range |
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


