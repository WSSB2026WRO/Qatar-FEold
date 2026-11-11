# Software Architecture — Team 6038

Team **6038** developed two mission programs for the LEGO MINDSTORMS EV3 robot and implemented each mission using two programming approaches:

1. **Python / Pybricks MicroPython** — text-based source programs.
2. **LEGO MINDSTORMS EV3 blocks** — native graphical EV3 project files.

This setup lets us compare both approaches on the same robot and decide which one suits each competition mission.

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

## Engineering diagrams

The mission software is documented alongside its hardware and control context. See the [complete eight-sheet engineering drawing set](../docs/drawings/README.md), including the [system architecture](../docs/drawings/SYS-001_autonomous_vehicle_architecture.svg), [Obstacle Challenge state machine](../docs/drawings/OBS-001_obstacle_state_machine.svg), [EV3 wiring](../docs/drawings/ELE-001_ev3_wiring.svg) and [Pixy2 camera geometry](../docs/drawings/CAM-001_pixy2_camera_geometry.svg).

## Mission implementation files

| Mission | Python / Pybricks MicroPython | Native EV3 block project |
|---|---|---|
| Open Challenge | [`open_challenge.py`](open_challenge/open_challenge.py) | [`OpenChallenge.ev3`](ev3_blocks/open_challenge/OpenChallenge.ev3) |
| Obstacle Challenge | [`obstacle_challenge.py`](obstacle_challenge/obstacle_challenge.py) | [`ObstacleChallenge.ev3`](ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) |

Each challenge folder contains its own README describing the corresponding implementation. The EV3 project folders also document the native project archive and the modules stored inside it.

## Why two programming approaches?

We implemented both approaches so we could compare them on the same robot instead of assuming that one programming environment would perform better.

The comparison includes:

- program construction and modification;
- build, compilation or project-preparation duration;
- startup latency from the start command to the first program action;
- sensing, decision and actuation cycle duration;
- mission execution time and repeatability;
- debugging, readability and maintainability.

## Sub-second timing: a Team 6038 strength

One area we wanted to examine closely was how long each program takes to start and respond. We therefore focus on timings measured in milliseconds or fractions of a second. Sub-second measurements are best recorded in milliseconds or at a stated decimal precision.

The timing quantities are kept distinct:

- **Build / compilation / project preparation:** time required by the relevant software environment to prepare the program for execution.
- **Startup latency:** time from the start command to the first confirmed program action.
- **Control-cycle duration:** time for an equivalent sensing, decision and actuation cycle.
- **Mission execution time:** time to complete the same defined mission.

Python upload or bytecode preparation is not automatically equivalent to native compilation by the EV3 graphical environment. A fair comparison therefore uses clearly defined and equivalent timing boundaries.

We have documented the comparison method and included both implementations here. It does not currently include a paired sub-second timing dataset, so no numerical speed advantage is claimed for either approach.

## Technical comparison

See [Dual-Implementation Technical Comparison](implementation_comparison.md) for the detailed comparison of programming models, workflow, runtime, debugging, timing methodology and evidence scope.

## Python software functions

The Python mission programs include EV3 device initialization, sensor acquisition, heading feedback, steering and drive control, mission-state logic, and run logging. Mission-specific details are documented in each Python challenge README.

## Hardware interface context

For the Obstacle Challenge, the Pixy2 camera assembly with its integrated illumination is connected through EV3 sensor port S4 using I²C. The illumination is part of the camera assembly, not a separate device on motor port D. Motor port D is unused by the challenge programs.

## Automated software checks

Our automated Python checks verify that the source files can be parsed and that the analytical and documentation checks pass. These checks are not a substitute for executing the native EV3 block projects on the physical robot.
