# Team 6038 — Dual EV3 Software Implementations

## Engineering drawing references

The implementation comparison is supported by the [system architecture](../docs/drawings/SYS-001_autonomous_vehicle_architecture.svg), [Obstacle Challenge state machine](../docs/drawings/OBS-001_obstacle_state_machine.svg), [EV3 wiring](../docs/drawings/ELE-001_ev3_wiring.svg) and the [complete drawing register](../docs/drawings/README.md).

## Team identity

**WRO Future Engineers team number: 6038**

We developed two ways to program our LEGO MINDSTORMS EV3 robot: Python with Pybricks MicroPython and the graphical LEGO EV3 block environment. Both versions control the same robot platform, which lets us compare the two approaches directly.

## Mission program archive

The native block projects are stored directly in the repository and organized by challenge:

| Challenge | LEGO EV3 block project | Python implementation |
|---|---|---|
| Obstacle Challenge | [ObstacleChallenge.ev3](ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) | [obstacle_challenge.py](obstacle_challenge/obstacle_challenge.py) |
| Open Challenge | [OpenChallenge.ev3](ev3_blocks/open_challenge/OpenChallenge.ev3) | [open_challenge.py](open_challenge/open_challenge.py) |

The EV3 files are native LEGO MINDSTORMS project containers. They preserve the graphical program and its project assets; they are not screenshots or a textual reconstruction of the blocks. Each native project has a folder-level README describing its contents.

## Why two implementations were developed

We chose to build both Python and EV3 block versions so that we could compare a text-based workflow with a visual one. Our aim is to find out which approach works better for our robot and the competition missions.

The comparison considers:
- program construction and modification time;
- build, compilation or project-generation time;
- time from starting the program to the first effective motor/sensor action;
- control-loop execution and response latency;
- sensor acquisition and decision consistency;
- steering and drive command responsiveness;
- mission completion time and repeatability;
- debugging clarity, maintainability and reliability.

## Python and EV3 blocks — technical comparison

| Comparison dimension | Python / Pybricks MicroPython | LEGO EV3 block programming |
|---|---|---|
| Programming model | Textual, procedural code with explicit functions, variables and control flow | Visual blocks connected into a graphical sequence and control structure |
| Algorithm expression | Flexible for custom calculations, state machines, filtering and reusable functions | Direct and accessible for sequences, loops, conditions, motor and sensor operations |
| Editing workflow | Efficient for structured edits, refactoring and version control | Visual and intuitive for inspecting program flow; large programs can become visually extensive |
| Debugging | Text logs, variables, explicit conditions and source-level inspection | Visual inspection of block sequence and EV3 environment debugging facilities |
| Build / compilation | Depends on the Pybricks upload and MicroPython execution workflow; Python source execution is not directly equivalent to a conventional native-code build | The EV3 development environment processes the graphical project into a runnable EV3 program |
| Runtime performance | Depends on interpreter overhead, algorithm design, sensor I/O and control-loop structure | Depends on the EV3 runtime, block implementation, sensor I/O and control-loop structure |
| Precision of timing analysis | Easy to instrument code with high-resolution timestamps and log elapsed time | Timing can be measured around equivalent program stages, subject to the EV3 environment's timing resolution |
| Maintainability | Strong for modular, parameterized and code-reviewed systems | Strong for visual communication of simpler sequences; complex logic may occupy many blocks |
| Best comparative use | Complex perception, geometry, custom calculations and explicit state-machine logic | Clear visual mission sequences and rapid inspection of the control flow |

We do not assume that either version is faster just because of the programming language. We will base that decision on tests carried out with the same robot setup and mission conditions.

## Compilation and timing performance as a team strength

A central strength of Team 6038 is its emphasis on comparing execution technologies quantitatively rather than selecting a programming method by preference. In particular, the team treats **build/compilation time and startup delay—measured in fractions of a second—as important performance indicators**.

For a meaningful comparison, these are kept as separate timing quantities:

1. **Build or compilation duration:** elapsed time required by the relevant programming environment to prepare the program for execution. For the Python workflow, the measured stage must be named precisely (for example, upload, bytecode preparation or deployment); it should not be mislabeled as a native compilation if no such compilation occurs.
2. **Program startup latency:** time from the start command to the first confirmed program action.
3. **Control-cycle duration:** elapsed time for an equivalent sensing, decision and actuation cycle.
4. **Mission execution time:** elapsed time to complete the same defined course or mission.

Sub-second results should be recorded in milliseconds or to a stated decimal precision, with the same timing boundaries and repeated-run method for both implementations.

## Comparative measurement record

We have included both EV3 block projects and both Python programs, but we have not yet added a set of paired timing measurements or a controlled side-by-side test log. For that reason, we do not claim a numerical advantage for either version. The team's focus on sub-second build and response measurement is documented as a deliberate engineering strength; quantitative winner selection is kept distinct from the existence of both implementations.

## Hardware equivalence

The comparison concerns software approaches for the team's LEGO EV3 robot. Hardware configuration, motor assignments, sensor assignments, battery condition, mission geometry and control parameters are treated as comparison conditions rather than software advantages. The Pixy2 camera assembly, including its integrated illumination, is connected through EV3 sensor port S4 for the Obstacle Challenge. Motor port D has no device assigned.

## Engineering conclusion

Keeping both versions gives us a practical way to compare the programming process and the robot's performance. We plan to use the results, including timings measured in milliseconds, to choose the approach that best meets each mission's requirements.
