# Power and Sense Management

## System overview

This section documents the EV3 power, actuator, sensor, and communication interfaces used by the supplied challenge programs. Electrical ratings not present in the source files must be taken from the component datasheets and verified on the actual assembly.

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

## Power management principles

1. Use a battery pack approved for the EV3 system.
2. Inspect battery contacts and cable condition before each run.
3. Record battery condition when comparing run performance.
4. Avoid adding external loads to motor ports without verifying electrical compatibility.
5. Keep power and sensor cables away from moving steering and drive components.
6. Stop testing if the controller resets or sensor communication becomes unstable.

## Sensor management

### Gyro
The programs measure gyro drift while the vehicle is stationary. The vehicle must remain still during calibration.

### Ultrasonic sensors
The two sensors provide left and right wall-distance observations. Their alignment and mounting positions influence corridor-position estimates.

### Pixy2
The Obstacle Challenge program communicates with Pixy2 over I²C. The configured address is 0x54. Signature 1 is mapped to red and signature 2 to green.

## Commissioning checklist

- [ ] Confirm the EV3 battery and connector condition.
- [ ] Confirm motor and sensor ports against the software configuration.
- [ ] Check cable retention and strain relief.
- [ ] Verify gyro calibration with the vehicle stationary.
- [ ] Compare ultrasonic readings against known distances.
- [ ] Confirm Pixy2 I²C communication before obstacle testing.
- [ ] Record any resets, communication errors, or intermittent readings.

## Electrical data register

| Item | Required record | Status |
|---|---|---|
| EV3 battery | Type, rated voltage, measured voltage | To be recorded |
| Drive motors | Exact model and datasheet | To be recorded |
| Steering motor | Exact model and datasheet | To be recorded |
| External loads | Voltage/current requirements | Verify before connection |
| Pixy2 | Firmware, mode, address | Configured in software; verify on device |
| Wiring | Port map and photographs | To be added |

## Fault response

If sensor data become invalid, camera communication fails repeatedly, or the controller resets, terminate the autonomous run and inspect the power and signal connections before restarting.
