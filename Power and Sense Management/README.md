# Power and Sense Management

## System overview

This section defines the EV3 power, actuator, sensor, and communication architecture used by the two challenge programs.

## Device and port allocation

| EV3 port | Device | Open Challenge | Obstacle Challenge |
|---|---|---|---|
| A | Medium motor | Drive | Drive |
| B | Medium motor | Drive | Drive |
| C | Medium motor | Steering | Steering |
| D | No device assigned | Unused | Unused |
| S1 | Gyro sensor | Heading | Heading |
| S2 | Ultrasonic sensor | Left range | Left range |
| S3 | Ultrasonic sensor | Right range | Right range |
| S4 | Pixy2 camera with integrated illumination | Not used | I²C vision and camera illumination |

## Power management

- Use the EV3-approved battery system and inspect contacts before operation.
- Keep motor and sensor wiring secured and clear of moving linkages.
- Check battery condition when comparing runs.
- Do not connect an external load to an EV3 motor output without verifying electrical compatibility.
- Stop operation if the controller resets or sensor communication becomes unstable.

## Sensor management

### Gyro
Both programs perform stationary drift measurement and calibration. The vehicle must remain motionless during this process.

### Ultrasonic sensors
S2 and S3 provide left and right wall-distance observations. Sensor alignment and mounting geometry affect lateral-position estimates.

### Pixy2
The Obstacle Challenge program communicates with Pixy2 over I²C at configured address 0x54. Signature 1 is mapped to red and signature 2 to green.

## Electrical integration record

The Pixy2 camera and its illumination are one camera assembly connected through sensor port S4. The illumination is integrated with the Pixy2 and is not a separate device on EV3 motor port D. Port D is unused by both challenge programs. Component-specific electrical ratings are governed by the manufacturer's datasheets; the EV3 program sources do not encode battery chemistry, current limits, or fuse ratings.

## Commissioning and fault context

The commissioning architecture covers battery and connector condition, motor polarity, steering reference, stationary gyro calibration, ultrasonic ranging, Pixy2 I²C communication, and signature mapping. The documented fault response terminates autonomous operation when sensor data become invalid, camera communication repeatedly fails, or the controller resets.

## Fault response

If sensor data become invalid, camera communication fails repeatedly, or the controller resets, terminate the autonomous run and inspect the power and signal connections before restarting.
