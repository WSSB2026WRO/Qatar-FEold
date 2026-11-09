# Power and Sense Management

## System overview

This section defines the EV3 power, actuator, sensor, and communication architecture used by the two challenge programs.

## Device and port allocation

| EV3 port | Device | Open Challenge | Obstacle Challenge |
|---|---|---|---|
| A | Medium motor | Drive | Drive |
| B | Medium motor | Drive | Drive |
| C | Medium motor | Steering | Steering |
| S1 | Gyro sensor | Heading | Heading |
| S2 | Ultrasonic sensor | Left range | Left range |
| S3 | Ultrasonic sensor | Right range | Right range |
| S4 | Pixy2 camera | Not used | I²C vision |

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

The software interface allocation is defined above. Component-specific electrical ratings are governed by the manufacturer's datasheets. The EV3 program sources do not encode battery chemistry, current limits, fuse ratings, or external lamp specifications; these must not be inferred from software port assignments.

## Commissioning procedure

1. Inspect battery contacts, cables, and connectors.
2. Confirm motor and sensor ports against the device map.
3. Verify drive motor polarity with the wheels safely raised.
4. Confirm steering zero with the road wheels straight.
5. Run stationary gyro calibration.
6. Compare ultrasonic readings against known reference distances.
7. Confirm Pixy2 communication and signature mapping before obstacle operation.
8. Record abnormal readings, resets, or communication errors in the test log.

## Fault response

If sensor data become invalid, camera communication fails repeatedly, or the controller resets, terminate the autonomous run and inspect the power and signal connections before restarting.
