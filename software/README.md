# Software Architecture

Two independent programs are maintained for the two WRO Future Engineers formats. Each program has a separate mission sequence and hardware-specific control logic.

## Challenge software

| Challenge | Source | Version | Main sensing |
|---|---|---|---|
| Open Challenge | [open_challenge.py](open_challenge/open_challenge.py) | OPEN-COMP-2 | Gyro and dual ultrasonic |
| Obstacle Challenge | [obstacle_challenge.py](obstacle_challenge/obstacle_challenge.py) | OBST-1 | Gyro, dual ultrasonic, Pixy2 |

## Runtime platform

- LEGO EV3
- Pybricks MicroPython
- EV3 motor and sensor interfaces
- Pixy2 I²C interface for Obstacle Challenge

## Shared software functions

- Motor and sensor initialization
- Gyro drift measurement and calibration
- Ultrasonic range acquisition
- Steering actuator control
- Encoder-based distance estimation
- Heading feedback
- Event and CSV logging
- Runtime fault and timeout handling

## Challenge-specific functions

### Open Challenge
- Dual-wall corridor centering
- Opening confirmation
- Route direction selection
- Twelve-corner route tracking
- Final approach to the start section

### Obstacle Challenge
- Pixy2 block acquisition
- Red/green signature classification
- Pillar range and lateral-position estimation
- Passing-side selection
- Obstacle clearance tracking
- Parking manoeuvre

## Development and regression

Keep the two challenge programs independent. Preserve reference versions and isolate experimental changes. Every change to sensor processing, steering, navigation, or mission logic should be followed by syntax verification and the relevant hardware regression tests.
