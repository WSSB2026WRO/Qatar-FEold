# LEGO MINDSTORMS EV3 Blocks — Obstacle Challenge

**WRO Future Engineers team:** 6038  
**Implementation:** Native LEGO MINDSTORMS EV3 graphical programming  
**Mission:** Obstacle Challenge

## Project file

- [ObstacleChallenge.ev3](ObstacleChallenge.ev3) — native EV3 project archive containing the graphical program and its project resources.

The project archive includes the main Obstacle Challenge program and the following named EV3 program modules:

| EV3 program module | Documented role in the project |
|---|---|
| `HEADING.ev3p` | Heading-related program component |
| `DISTANCE.ev3p` | Distance-related program component |
| `CENTERING.ev3p` | Corridor-centering program component |
| `RACE_STEP.ev3p` | Race-step program component |
| `WALL_FOLLOW.ev3p` | Wall-following program component |
| `MANEUVER.ev3p` | Manoeuvre program component |
| `STRAIGHT.ev3p` | Straight-driving program component |
| `CORNER.ev3p` | Corner-navigation program component |

The module names above are taken from the native project archive. They identify the components stored in the project; this README does not infer undocumented block-level details.

## Purpose in Team 6038's dual-implementation project

This is the graphical-block counterpart to the Python Obstacle Challenge program:

- Python: [`software/obstacle_challenge/obstacle_challenge.py`](../../obstacle_challenge/obstacle_challenge.py)
- EV3 blocks: `software/ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3`

Team 6038 developed both versions to compare two programming approaches on the same LEGO EV3 robot and to select the approach best suited to the mission.

## Hardware context

The Python Obstacle Challenge documentation identifies the Pixy2 camera assembly, including its integrated illumination, on EV3 sensor port S4 using I²C. The illumination is integrated into the camera assembly; it is not a separate lamp connected to motor port D. Port D has no device assigned.

This README describes the native EV3 block project archive. It does not assume that every Python-specific library, camera interface, or source-code feature has an identical block-program implementation unless that equivalence is established by the graphical project itself.

## Comparative performance focus

The comparison covers program preparation/build time, startup latency, control-cycle timing, mission execution time, repeatability, debugging and maintainability. Particular attention is given to sub-second timing: measurements are expressed in milliseconds or with a clearly stated decimal precision.

For technical accuracy, Python source upload or bytecode preparation is distinguished from compilation performed by the EV3 graphical environment. These are compared only when the measured timing boundaries are clearly defined.

No paired timing results are included in this folder. The presence of both projects establishes the dual-implementation approach; it does not by itself establish that one implementation is faster.

## Opening the project

Open `ObstacleChallenge.ev3` with compatible LEGO MINDSTORMS EV3 software. The file is retained in its native project format so the graphical program and associated assets remain available for inspection.
