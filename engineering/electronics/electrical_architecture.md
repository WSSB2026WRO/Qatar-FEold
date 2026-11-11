# Electrical Architecture and Integration Specification

## 1. Scope

This specification documents the functional electrical architecture implied by the software device map and defines a professional integration framework. It does not assign unverified voltage, current, or connector ratings to individual components.

## 2. Functional blocks

| Block | Interface | Function |
|---|---|---|
| EV3 controller | Motor and sensor ports | Executes control program |
| Drive actuator A | EV3 motor port A | Propulsion |
| Drive actuator B | EV3 motor port B | Propulsion |
| Steering actuator C | EV3 motor port C | Steering |
| No device assigned | EV3 motor port D | Unused by both challenge programs |
| Gyro S1 | EV3 sensor port S1 | Heading feedback |
| Ultrasonic S2 | EV3 sensor port S2 | Left-side ranging |
| Ultrasonic S3 | EV3 sensor port S3 | Right-side ranging |
| Pixy2 camera with integrated illumination | I²C on EV3 sensor port S4 | Colour-signature perception and camera illumination in Obstacle Challenge |

## 3. Power integrity

The controller supply must remain within the manufacturer's operating limits during simultaneous drive and steering loads. A power-integrity review should record:
- battery type and manufacturer;
- nominal and measured voltage;
- connector and cable ratings;
- peak current under representative load;
- controller brownout or reset events;
- battery temperature after repeated runs.

The Pixy2 illumination is integrated with the camera assembly on S4; it is not a separate auxiliary lamp connected to motor port D.

## 4. Signal integrity

- Keep sensor cables away from moving linkages.
- Avoid tight bends and repeated flexing at connector exits.
- Secure the Pixy2 cable to prevent I²C connector movement.
- Confirm I²C address and output mode before running vision control.
- Verify that all sensor ports are initialized before autonomous movement.

## 5. Protection and failure handling

| Fault | Detection | Recommended response |
|---|---|---|
| Gyro drift | Startup drift measurement | Recalibrate or inhibit start |
| Ultrasonic invalid echo | Range plausibility checks | Reject sample and use bounded fallback |
| Pixy2 I²C fault | Consecutive communication error counter | Stop or enter defined safe state |
| Motor stall | Encoder progress timeout | Stop drive and report fault |
| Low battery | Voltage observation | Abort run below validated threshold |
| Loose sensor cable | Missing or implausible data | Stop autonomous operation |


