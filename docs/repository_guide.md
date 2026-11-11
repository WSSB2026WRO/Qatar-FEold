# Repository Guide and Engineering Record

## Directory structure

```text
Qatar-FE/
├── .github/workflows/            GitHub Actions validation
├── docs/                         Portfolio, verification, release and repository records
├── engineering/
│   ├── design_basis/             Reference vehicle assumptions
│   ├── diagrams/                 SVG engineering diagrams
│   ├── electronics/              Electrical integration
│   ├── mechanical_design/        Chassis, steering and additive manufacturing
│   ├── perception/               Pixy2 geometry and calibration
│   ├── reliability/              FMEA and maintenance
│   ├── simulation/               Analytical model and parameter sweep
│   └── software/                 Control-system design
├── hardware/
│   └── custom_3d_printed_parts/  Part records and mesh inspection notes
├── Mobility Management/          Propulsion, steering and navigation records
├── Obstacle Management/           Vision-based obstacle records
├── Power and Sense Management/    EV3 power, sensors and interfaces
├── schemes/                       Drawing register and release conventions
├── software/
│   ├── open_challenge/            Open Challenge source and documentation
│   └── obstacle_challenge/        Obstacle Challenge source and documentation
├── src/                           Source-code index
├── tests/                         Analytical and documentation integrity tests
├── t-photos/                      Team photographs
├── v-photos/                      Vehicle photographs
├── validation/                    Verification framework and test-record format
└── video/                         Demonstration-video index (no videos committed)
```

## Automated checks

Run the repository checks from the root directory:

```bash
python -m py_compile software/open_challenge/open_challenge.py
python -m py_compile software/obstacle_challenge/obstacle_challenge.py
python -m unittest discover -s tests -v
python engineering/simulation/parameter_sweep.py
```

The same checks are run by GitHub Actions. They validate source syntax and analytical calculations, not physical robot performance.

## Evidence classification

Use the following labels consistently:
- **Source-derived:** explicitly present in a supplied source file.
- **Configured:** a parameter set in software.
- **Assumed:** an input selected for a conceptual design case.
- **Calculated:** a value derived from stated assumptions and equations.
- **Measured:** obtained from a documented physical measurement.
- **Simulated:** produced by an explicit computational model.
- **Validated:** supported by repeatable tests and stated acceptance criteria.

## Revision control

Every significant change should include:
- purpose of the change;
- affected subsystem;
- source version;
- parameter changes;
- test evidence;
- rollback path.


