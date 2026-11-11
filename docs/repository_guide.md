# Repository Guide

This page is here to help us and anyone reviewing the project find the right files. It also explains how to run the automated checks and how we label the evidence.

## Folder structure

```text
Qatar-FE/
├── .github/workflows/            GitHub Actions validation
├── docs/                         Portfolio, verification, release, and repository notes
├── engineering/
│   ├── design_basis/             Reference vehicle assumptions
│   ├── diagrams/                 SVG engineering drawings
│   ├── electronics/              Electrical integration
│   ├── mechanical_design/        Chassis, steering, and 3D printing
│   ├── perception/               Pixy2 geometry and calibration
│   ├── reliability/              Failure modes and maintenance
│   ├── simulation/               Analytical model and parameter sweep
│   └── software/                 Control-system design
├── hardware/
│   └── custom_3d_printed_parts/  Part records and mesh inspection
├── Mobility Management/          Drive, steering, and navigation
├── Obstacle Management/          Camera-based obstacle notes
├── Power and Sense Management/   EV3 power, sensors, and interfaces
├── schemes/                      Drawing list and revision notes
├── software/
│   ├── open_challenge/            Open Challenge source and notes
│   └── obstacle_challenge/        Obstacle Challenge source and notes
├── src/                           Source-code index
├── tests/                         Analytical and documentation tests
├── t-photos/                      Team photographs
├── v-photos/                      Vehicle photographs
├── validation/                    Test framework and report template
└── video/                         Video index; no videos committed
```

## Running the automated checks

Open a terminal in the repository's root folder and run:

```bash
python -m py_compile software/open_challenge/open_challenge.py
python -m py_compile software/obstacle_challenge/obstacle_challenge.py
python -m unittest discover -s tests -v
python engineering/simulation/parameter_sweep.py
```

GitHub Actions runs these checks as well. They check Python syntax and analytical calculations. They do not measure how the physical robot performs.

## Evidence labels

We use these labels in the project notes:

- **Source-derived:** written directly in one of the supplied source files.
- **Configured:** a value set in the program.
- **Assumed:** an input selected for a design study.
- **Calculated:** worked out from stated inputs and equations.
- **Measured:** obtained from a documented physical measurement.
- **Simulated:** produced by a computational model.
- **Validated:** supported by repeatable tests and stated acceptance criteria.

## Keeping track of changes

When we make an important change, we record why it was made, which part of the robot is affected, the source version, parameter changes, test evidence, and a way to return to the previous version.