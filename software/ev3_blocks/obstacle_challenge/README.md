# EV3 Blocks — Obstacle Challenge

**WRO Future Engineers team:** 6038  
**Programming format:** Native LEGO MINDSTORMS EV3 blocks  
**Mission:** Obstacle Challenge

## Project file

- [ObstacleChallenge.ev3](ObstacleChallenge.ev3) — the native EV3 project archive with the graphical program and its project resources.

The archive contains the main Obstacle Challenge program and these named EV3 program modules:

| Module in the EV3 project | Role indicated by its name |
|---|---|
| `HEADING.ev3p` | Heading |
| `DISTANCE.ev3p` | Distance |
| `CENTERING.ev3p` | Corridor centering |
| `RACE_STEP.ev3p` | Race step |
| `WALL_FOLLOW.ev3p` | Wall following |
| `MANEUVER.ev3p` | Manoeuvre |
| `STRAIGHT.ev3p` | Straight driving |
| `CORNER.ev3p` | Corner navigation |

These names come from the native project archive. They tell us which modules are stored in the project, but we do not add block-level details that are not shown in the archive.

## How this fits our two-program approach

This is the EV3 block version that sits alongside our Python Obstacle Challenge program:

- Python: [`software/obstacle_challenge/obstacle_challenge.py`](../../obstacle_challenge/obstacle_challenge.py)
- EV3 blocks: `software/ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3`

We kept both versions so we can compare text programming and visual programming on the same LEGO EV3 robot.

## Hardware note

The Python Obstacle Challenge documentation lists the Pixy2 camera assembly, including its integrated illumination, on EV3 sensor port S4 over I²C. The light is part of the camera assembly; it is not a separate lamp on motor port D. Port D has no assigned device.

This page describes the native EV3 block archive. We do not assume that every Python library, camera interface, or source-code feature has an identical block implementation unless the graphical project shows it.

## What we want to compare

We compare program preparation, startup delay, control-cycle time, mission time, repeatability, debugging, and maintenance. We are especially interested in sub-second timing, recorded in milliseconds or at a stated decimal precision.

Uploading Python source or preparing bytecode is a different step from the EV3 graphical environment preparing its project. We need to measure each workflow according to what it actually does.

We do not have paired timing results in this folder. Having both projects available does not by itself show that one is faster.

## Project format

`ObstacleChallenge.ev3` is kept in its native LEGO MINDSTORMS EV3 format. The archive contains the graphical program and its project resources for opening in compatible EV3 software.