# Software Architecture — Team 6038

Team **6038** developed two mission programs for the LEGO MINDSTORMS EV3 robot and implemented each mission using two programming approaches:

1. **Python / Pybricks MicroPython** — text-based source programs.
2. **LEGO MINDSTORMS EV3 blocks** — native graphical EV3 project files.

This structure allows the team to compare the two approaches on the same robot platform and evaluate which is better suited to the competition missions.

## Software directory map

```text
software/
├── README.md
├── implementation_comparison.md
├── open_challenge/
│   ├── README.md
│   ├── algorithm_notes.md
│   └── open_challenge.py
├── obstacle_challenge/
│   ├── README.md
│   ├── algorithm_notes.md
│   └── obstacle_challenge.py
└── ev3_blocks/
    ├── open_challenge/
    │   ├── README.md
    │   └── OpenChallenge.ev3
    └── obstacle_challenge/
        ├── README.md
        └── ObstacleChallenge.ev3
```

## Mission implementation files

| Mission | Python / Pybricks MicroPython | Native EV3 block project |
|---|---|---|
| Open Challenge | [`open_challenge.py`](open_challenge/open_challenge.py) | [`OpenChallenge.ev3`](ev3_blocks/open_challenge/OpenChallenge.ev3) |
| Obstacle Challenge | [`obstacle_challenge.py`](obstacle_challenge/obstacle_challenge.py) | [`ObstacleChallenge.ev3`](ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) |

Each challenge folder contains its own README describing the corresponding implementation. The EV3 project folders also document the native project archive and the modules stored inside it.

## Why two programming approaches?

The team implemented both approaches to make a practical, evidence-based comparison rather than assuming that one programming language or environment is automatically superior.

The comparison includes:

- program construction and modification;
- build, compilation or project-preparation duration;
- startup latency from the start command to the first program action;
- sensing, decision and actuation cycle duration;
- mission execution time and repeatability;
- debugging, readability and maintainability.

## Sub-second timing: a Team 6038 strength

A distinctive strength of Team 6038 is its focus on comparing program preparation and robot response times at **fractions-of-a-second scale**. Sub-second measurements are best recorded in milliseconds or at a stated decimal precision.

The timing quantities are kept distinct:

- **Build / compilation / project preparation:** time required by the relevant software environment to prepare the program for execution.
- **Startup latency:** time from the start command to the first confirmed program action.
- **Control-cycle duration:** time for an equivalent sensing, decision and actuation cycle.
- **Mission execution time:** time to complete the same defined mission.

Python upload or bytecode preparation is not automatically equivalent to native compilation by the EV3 graphical environment. A fair comparison therefore uses clearly defined and equivalent timing boundaries.

The repository documents the comparison method and contains both implementations. It does not currently include a paired sub-second timing dataset, so no numerical speed advantage is claimed for either approach.

## Technical comparison

See [Dual-Implementation Technical Comparison](implementation_comparison.md) for the detailed comparison of programming models, workflow, runtime, debugging, timing methodology and evidence scope.

## Python software functions

The Python mission programs include EV3 device initialization, sensor acquisition, heading feedback, steering and drive control, mission-state logic, and run logging. Mission-specific details are documented in each Python challenge README.

## Hardware interface context

For the Obstacle Challenge, the Pixy2 camera assembly with its integrated illumination is connected through EV3 sensor port S4 using I²C. The illumination is part of the camera assembly, not a separate device on motor port D. Motor port D is unused by the challenge programs.

## Automated software checks

The repository's automated Python checks validate source parsing and analytical/documentation integrity. These checks are not a substitute for executing the native EV3 block projects on the physical robot.
