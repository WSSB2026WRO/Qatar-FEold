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

## Automated repository tests

The repository includes unit tests for the analytical reference model and integrity checks for Markdown links, text encoding, and SVG XML structure. Run all tests from the repository root with `python -m unittest discover -s tests -v`.

## Development and regression

Keep the two challenge programs independent. Preserve reference versions and isolate experimental changes. The documented software verification framework separates source-level checks from hardware regression evidence.
