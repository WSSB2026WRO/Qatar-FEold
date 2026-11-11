# Reliability and Failure-Mode Notes

## 1. How we rate risks

For a formal review, we can rate severity (S), occurrence (O), and detectability (D) from 1 to 10. The risk priority number is:

[
RPN=S\times O\times D
]

We have not assigned numerical ratings in this register because we do not yet have recorded physical evidence for occurrence and detectability. The scale should be applied during a documented team review. An RPN helps us sort risks, but it does not replace safety controls for a serious hazard.

## 2. Failure modes we have identified

| Subsystem | Possible failure | Possible effect | How we can check it | Possible control |
|---|---|---|---|---|
| Drive | Wheel slip | Distance and turning error | Compare encoder and gyro behaviour | Adjust acceleration and check grip |
| Drive | Motor stall | Robot stops or leaves its path | No dedicated stall detector is implemented in the source; check encoder progress on the hardware | Add a progress timeout and safe stop after setting and testing its limits |
| Steering | Linkage backlash | Unsteady heading | Repeat wheel-angle measurements | Reduce clearance and inspect joints |
| Steering | Mechanical binding | High load or incomplete turn | Existing manoeuvre timeout and full-travel inspection | Check clearance and actuator load through the full range |
| Gyro | Bias drift | Heading error | Stationary drift check | Calibrate again and limit corrections |
| Ultrasonic | Multiple or false echo | Incorrect wall position | Check plausibility and continuity | Align sensors and filter readings |
| Pixy2 | Wrong colour classification | Wrong side of pillar | Check signature and repeated detections | Recheck signatures and lighting |
| Pixy2 | I²C communication loss | Missing obstacle information | Count consecutive communication errors | Stop safely and inspect the cable |
| Printed parts | Layer separation | Linkage or sensor mount failure | Visual inspection | Review print direction and settings |
| Battery | Voltage drop | Lower speed or controller reset | Observe battery voltage | Check battery condition under load |
| Parking | Position estimate error | Robot stops in the wrong position | Compare boundary and encoder information | Recheck parking geometry |

## 3. Risks that need attention first

We should give special attention to uncontrolled movement, steering lock, loss of obstacle detection, and broken mechanical connections. Testing should start with simple low-speed checks and move on to full mission trials only when the earlier checks are satisfactory.

## 4. Maintenance checks

### Before each run
- Check the wheels and tyre surfaces.
- Check steering movement and fasteners.
- Look for damage on printed parts.
- Check sensor mounts and cables.
- Check the battery.
- Confirm which software version is loaded.

### After each test session
- Look for cracks and loose joints.
- Save the run logs.
- Write down unusual behaviour and any changes made.
- Review motor and sensor behaviour.
- Update the maintenance notes.