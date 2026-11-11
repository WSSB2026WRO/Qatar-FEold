# Software — Team 6038

We have made two mission programs for our LEGO MINDSTORMS EV3 robot. Each mission is represented in two programming formats:

1. **Python / Pybricks MicroPython** — programs written as text-based source code.
2. **LEGO MINDSTORMS EV3 blocks** — native graphical EV3 project files.

This lets us compare both approaches on the same robot instead of guessing which one will work better for each mission.

## Folder map

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

## Engineering drawings

We explain the programs together with the hardware and control design. See the [eight-sheet drawing set](../docs/drawings/README.md), including the [system architecture](../docs/drawings/SYS-001_autonomous_vehicle_architecture.svg), [Obstacle Challenge state machine](../docs/drawings/OBS-001_obstacle_state_machine.svg), [EV3 wiring](../docs/drawings/ELE-001_ev3_wiring.svg), and [Pixy2 camera geometry](../docs/drawings/CAM-001_pixy2_camera_geometry.svg).

## Program files

| Mission | Python / Pybricks MicroPython | Native EV3 block project |
|---|---|---|
| Open Challenge | [`open_challenge.py`](open_challenge/open_challenge.py) | [`OpenChallenge.ev3`](ev3_blocks/open_challenge/OpenChallenge.ev3) |
| Obstacle Challenge | [`obstacle_challenge.py`](obstacle_challenge/obstacle_challenge.py) | [`ObstacleChallenge.ev3`](ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) |

Each challenge folder has its own README. The EV3 project folders also explain the native project archive and list the modules stored in it.

## Why we kept both programming approaches

We wanted to compare a text-based program with a visual block program on the same EV3 robot. We look at:
- How long it takes to create and change a program.
- Build, compilation, or project-preparation time.
- Time from pressing start to the first program action.
- Time for sensing, deciding, and moving.
- Mission time and repeatability.
- How easy the program is to debug, read, and maintain.

## Looking at timings smaller than one second

We are especially interested in how quickly each program starts and responds. We therefore pay attention to timings in milliseconds and fractions of a second.

We keep these measurements separate:

- **Build / compilation / project preparation:** time the software environment needs to prepare the program.
- **Startup latency:** time from the start command to the first confirmed program action.
- **Control-cycle duration:** time for an equivalent sensor, decision, and motor-command cycle.
- **Mission execution time:** time to complete the same defined mission.

Uploading Python code or preparing bytecode is not automatically the same as compiling a native EV3 graphical project. A fair comparison needs clear and equivalent timing boundaries.

We have documented the method and included both implementations, but we do not yet have a paired timing dataset. We therefore do not claim that either approach is faster.

## More detailed comparison

See [Dual-Implementation Technical Comparison](implementation_comparison.md) for the programming models, workflow, timing method, debugging, and evidence limits.

## What the Python programs do

The Python mission programs initialize the EV3 devices, read the sensors, use heading feedback, control the drive and steering motors, manage mission states, and record run information. The separate challenge READMEs explain the mission-specific behaviour.

## Hardware connection note

For the Obstacle Challenge, the Pixy2 camera and its integrated illumination connect through EV3 sensor port S4 using I²C. The light is part of the camera assembly, not a separate device on motor port D. Motor port D is unused by the challenge programs.

## Automated checks

Our automated checks confirm that the Python files can be compiled and that the analytical and documentation tests pass. They do not replace running the native EV3 block projects on the physical robot.