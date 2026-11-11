# EV3 Blocks — Open Challenge

**WRO Future Engineers team:** 6038  
**Programming format:** Native LEGO MINDSTORMS EV3 blocks  
**Mission:** Open Challenge

## Project file

- [OpenChallenge.ev3](OpenChallenge.ev3) — the native EV3 project archive with the graphical program and its project resources.

The archive contains the main Open Challenge program and these named EV3 program modules:

| Module in the EV3 project | Role indicated by its name |
|---|---|
| `HEADING.ev3p` | Heading |
| `DISTANCE.ev3p` | Distance |
| `CENTERING.ev3p` | Corridor centering |
| `DRIVE_DD.ev3p` | Drive / differential drive |
| `CORNER.ev3p` | Corner navigation |

These names come from the native project archive. They tell us which modules are included, but we do not add block-level details that are not shown in the archive.

## How this fits our two-program approach

This is the EV3 block version that sits alongside our Python Open Challenge program:

- Python: [`software/open_challenge/open_challenge.py`](../../open_challenge/open_challenge.py)
- EV3 blocks: `software/ev3_blocks/open_challenge/OpenChallenge.ev3`

We kept both versions so we can compare text programming and visual programming on the same LEGO EV3 robot.

## What we want to compare

We compare program preparation, startup delay, control-cycle time, mission time, repeatability, debugging, and maintenance. We are especially interested in sub-second timing, recorded in milliseconds or at a stated decimal precision.

Uploading Python source or preparing bytecode is a different step from the EV3 graphical environment preparing its project. We need to measure each workflow according to what it actually does.

We do not have paired timing results in this folder. Having both projects available does not by itself show that one is faster.

## Project format

`OpenChallenge.ev3` is kept in its native LEGO MINDSTORMS EV3 format. The archive contains the graphical program and its project resources for opening in compatible EV3 software.