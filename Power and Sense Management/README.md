# Power and Sense Management

## How we connected the EV3 system

This page describes the power, motors, sensors, and communication used by our two challenge programs. We have listed the port assignments so it is easier to check the wiring against the code.

## EV3 port allocation

| EV3 port | Device | Open Challenge | Obstacle Challenge |
|---|---|---|---|
| A | Medium motor | Drive | Drive |
| B | Medium motor | Drive | Drive |
| C | Medium motor | Steering | Steering |
| D | No device assigned | Unused | Unused |
| S1 | Gyro sensor | Heading | Heading |
| S2 | Ultrasonic sensor | Left distance | Left distance |
| S3 | Ultrasonic sensor | Right distance | Right distance |
| S4 | Pixy2 camera with integrated illumination | Not used | Camera and illumination over I²C |

## Power checks

Before a run, we should:
- Use the EV3-approved battery system and check that the contacts are clean and secure.
- Keep motor and sensor cables away from moving parts.
- Check the battery condition when comparing runs.
- Check electrical compatibility before connecting anything to an EV3 motor output.
- Stop the run if the EV3 resets or sensor communication becomes unstable.

## Sensors

### Gyro
Both programs measure stationary drift and calibrate the gyro during startup. The vehicle must not move while this is happening.

### Ultrasonic sensors
S2 and S3 measure the distances to the left and right walls. Their alignment and mounting position affect the distance readings and the centre estimate.

### Pixy2
The Obstacle Challenge program communicates with the Pixy2 over I²C at address 0x54. Signature 1 is used for red and signature 2 for green.

## Camera and electrical integration

The Pixy2 and its illumination are one camera assembly connected to sensor port S4. The illumination is built into the Pixy2; it is not a separate device connected to motor port D. Port D is not used by either challenge program.

The program files do not contain all electrical ratings for the hardware. For battery chemistry, current limits, and fuse ratings, we need to use the component manufacturer's datasheets rather than guess values.

## Setup and fault checks

When we prepare the robot, we check the battery and connectors, motor directions, steering reference, gyro calibration, ultrasonic readings, Pixy2 communication, and camera signature mapping.

If sensor readings become invalid, camera communication keeps failing, or the controller resets, we should stop the autonomous run. We then inspect the power and signal connections before trying again.