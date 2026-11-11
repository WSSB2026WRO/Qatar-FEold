# Comparing Our Two EV3 Programming Approaches

## Drawings that help explain the programs

We use the [system architecture](../docs/drawings/SYS-001_autonomous_vehicle_architecture.svg), [Obstacle Challenge state machine](../docs/drawings/OBS-001_obstacle_state_machine.svg), [EV3 wiring](../docs/drawings/ELE-001_ev3_wiring.svg), and [drawing index](../docs/drawings/README.md) to explain the hardware and software around the programs.

## Our team

**WRO Future Engineers team number: 6038**

We made two versions of our LEGO MINDSTORMS EV3 programs: one in Python using Pybricks MicroPython, and one using the graphical LEGO EV3 blocks. Both versions are for the same robot, which gives us a way to compare the approaches.

## Program files

The native block projects are stored in the repository by challenge:

| Challenge | EV3 block project | Python program |
|---|---|---|
| Obstacle Challenge | [ObstacleChallenge.ev3](ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) | [obstacle_challenge.py](obstacle_challenge/obstacle_challenge.py) |
| Open Challenge | [OpenChallenge.ev3](ev3_blocks/open_challenge/OpenChallenge.ev3) | [open_challenge.py](open_challenge/open_challenge.py) |

The EV3 files are native LEGO MINDSTORMS project archives. They contain the graphical programs and related project resources. They are not screenshots or text descriptions of the blocks. Each project folder has a README with more information.

## Why we made two versions

We wanted to compare writing code with arranging visual blocks, using the same robot rather than assuming one method would be better.

We are interested in:
- Time needed to create and change the program.
- Build, compilation, or project preparation time.
- Time between pressing start and the first motor or sensor action.
- Control-loop execution and response time.
- Consistency of sensor readings and decisions.
- Steering and drive response.
- Mission completion time over repeated runs.
- How easy each version is to debug and maintain.

## Technical comparison

| Topic | Python / Pybricks MicroPython | LEGO EV3 blocks |
|---|---|---|
| How we program | Text code with functions, variables, and control flow | Visual blocks connected into sequences and control structures |
| Writing algorithms | Flexible for calculations, state machines, filters, and reusable functions | Direct for sequences, loops, conditions, motor and sensor operations |
| Editing | Useful for structured changes, refactoring, and version control | Easy to see the program flow; large projects can take up a lot of screen space |
| Debugging | Text logs, variables, conditions, and source inspection | Inspecting the block sequence and using EV3 environment debugging tools |
| Build or preparation | Depends on Pybricks upload and MicroPython execution; source execution is not the same as a conventional native build | The EV3 software prepares the graphical project for execution |
| Runtime | Depends on interpreter overhead, algorithm design, sensor I/O, and loop structure | Depends on EV3 runtime, block design, sensor I/O, and loop structure |
| Timing analysis | We can add timestamps and log elapsed time in the code | We can time equivalent stages, depending on the EV3 environment's timing resolution |
| Maintenance | Good for modular code and shared parameters | Good for explaining simpler sequences visually; complex logic may need many blocks |
| Useful situations | More complex perception, geometry, calculations, and state machines | Clear visual sequences and quick inspection of program flow |

We do not assume that one version is faster just because of the programming language. We need to compare them on the same robot with the same mission conditions.

## Why we pay attention to sub-second timing

One thing we want to understand is how quickly each program gets ready and responds. We therefore pay attention to timings in milliseconds and fractions of a second.

We keep four different timing measurements:

1. **Build or preparation time:** how long the software environment takes to prepare the program. For Python, we must say whether we are measuring upload, bytecode preparation, or deployment. We should not call it native compilation if that is not what happens.
2. **Startup latency:** time from the start command to the first confirmed program action.
3. **Control-cycle duration:** time for the same sensor, decision, and motor-command cycle.
4. **Mission time:** time to finish the same defined course or task.

For a fair comparison, we need to use the same timing start and end points and repeat the measurements. Sub-second results should be written in milliseconds or with a clear decimal precision.

## What evidence we have so far

We have included both EV3 block projects and both Python programs. We have not yet added paired timing measurements or a controlled side-by-side test log. We therefore do not claim a numerical advantage for either version.

Our interest in measuring build and response times below one second is part of the project plan. Choosing a winner must wait until we have comparable measurements.

## Keeping the hardware the same

The comparison is about the programming methods, not different hardware. We should keep the motor assignments, sensors, battery condition, course, and control settings the same when comparing the programs.

For the Obstacle Challenge, the Pixy2 camera and its integrated illumination connect through EV3 sensor port S4. Motor port D has no assigned device.

## What we want to learn

Keeping both versions gives us a way to compare how we build, understand, and debug the programs, as well as how the robot responds. We can use those results to decide which approach is more suitable for each mission.