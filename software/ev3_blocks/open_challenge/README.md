# LEGO MINDSTORMS EV3 Blocks — Open Challenge

**WRO Future Engineers team:** 6038  
**Implementation:** Native LEGO MINDSTORMS EV3 graphical programming  
**Mission:** Open Challenge

## Project file

- [OpenChallenge.ev3](OpenChallenge.ev3) — native EV3 project archive containing the graphical program and its project resources.

The project archive includes the main Open Challenge program and the following named EV3 program modules:

| EV3 program module | Documented role in the project |
|---|---|
| `HEADING.ev3p` | Heading-related program component |
| `DISTANCE.ev3p` | Distance-related program component |
| `CENTERING.ev3p` | Corridor-centering program component |
| `DRIVE_DD.ev3p` | Drive / differential-drive program component |
| `CORNER.ev3p` | Corner-navigation program component |

The module names above are taken from the native project archive. They identify the components stored in the project; this README does not infer undocumented block-level details.

## Purpose in Team 6038's dual-implementation project

This is the graphical-block counterpart to the Python Open Challenge program:

- Python: [`software/open_challenge/open_challenge.py`](../../open_challenge/open_challenge.py)
- EV3 blocks: `software/ev3_blocks/open_challenge/OpenChallenge.ev3`

Team 6038 developed both versions to compare two programming approaches on the same LEGO EV3 robot and to select the approach best suited to the mission.

## Comparative performance focus

The comparison covers program preparation/build time, startup latency, control-cycle timing, mission execution time, repeatability, debugging and maintainability. Particular attention is given to sub-second timing: measurements are expressed in milliseconds or with a clearly stated decimal precision.

For technical accuracy, Python source upload or bytecode preparation is distinguished from compilation performed by the EV3 graphical environment. These are compared only when the measured timing boundaries are clearly defined.

No paired timing results are included in this folder. The presence of both projects establishes the dual-implementation approach; it does not by itself establish that one implementation is faster.

## Opening the project

Open `OpenChallenge.ev3` with compatible LEGO MINDSTORMS EV3 software. The file is retained in its native project format so the graphical program and associated assets remain available for inspection.
