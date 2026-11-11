# Repository Guide and Engineering Record

## Directory structure

```text
Qatar-FE/
├── .github/workflows/           Automated Python validation
├── docs/                        Project and release documentation
├── engineering/
│   ├── design_basis/             Reference design assumptions
│   ├── mechanical_design/        Chassis, mass properties, steering
│   ├── electronics/              Electrical integration
│   ├── software/                 Control architecture
│   ├── perception/               Camera geometry and calibration
│   ├── reliability/               Risk and failure analysis
│   ├── simulation/                Analytical models and parameter sweeps
│   └── diagrams/                  Original engineering diagrams
├── hardware/                     Hardware and custom-part documentation
├── software/
│   ├── open_challenge/            Open Challenge source and notes
│   └── obstacle_challenge/        Obstacle Challenge source and notes
├── tests/                         Analytical and documentation integrity tests
└── validation/                    Test plans and evidence requirements
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


