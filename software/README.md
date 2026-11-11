# Software Architecture

Team **6038** maintains two independent mission programs and two programming implementations for the LEGO EV3 robot. Python/Pybricks MicroPython and graphical LEGO EV3 block programming are both represented for the Open and Obstacle Challenges.

## Challenge implementations

| Challenge | Python source | LEGO EV3 block project | Main sensing |
|---|---|---|---|
| Open Challenge | [open_challenge.py](open_challenge/open_challenge.py) | `OpenChallenge.ev3` (native LEGO EV3 block project supplied with this delivery) | Gyro and dual ultrasonic |
| Obstacle Challenge | [obstacle_challenge.py](obstacle_challenge/obstacle_challenge.py) | `ObstacleChallenge.ev3` (native LEGO EV3 block project supplied with this delivery) | Gyro, dual ultrasonic, Pixy2 |

## Comparative engineering objective

The two implementations are maintained to compare:
- program construction and modification;
- build, compilation or project-preparation duration;
- startup latency;
- sensing/decision/actuation cycle time;
- mission execution time and repeatability;
- debugging, maintainability and reliability.

Team 6038 places particular emphasis on timing comparisons at fractions-of-a-second scale. Sub-second values are best represented in milliseconds or at a clearly stated decimal precision. Python upload or bytecode preparation is distinguished from native compilation, so that unlike stages are not compared as if they were identical.

The repository includes the comparison methodology, but no paired timing dataset is currently recorded. Accordingly, no measured performance advantage is attributed to either implementation.

See [Dual-Implementation Technical Comparison](implementation_comparison.md) for the full technical comparison.

## Python runtime platform

- LEGO EV3
- Pybricks MicroPython
- EV3 motor and sensor interfaces
- Pixy2 I²C interface for the Python Obstacle Challenge

## Shared software functions in the Python programs

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

## Automated Python repository tests

The repository includes unit tests for the analytical reference model and integrity checks for Markdown links, text encoding, and SVG XML structure. Run all tests from the repository root with `python -m unittest discover -s tests -v`.

## Software architecture

The two challenge programs remain independent because their mission logic and sensing requirements differ. The Python and block-program versions provide alternative implementations of these mission behaviours for comparative evaluation.
