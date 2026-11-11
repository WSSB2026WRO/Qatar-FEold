# Analytical Simulation and Parameter Studies

## What is in this folder

We use these scripts and notes to repeat calculations for the Qatar FE reference vehicle. The model looks at load transfer, a simplified traction limit, geometric stability, and how changing the inputs affects the results.

These are analytical studies. They are not physical tests of our robot.

## Inputs for the reference case

- Vehicle mass: 0.85 kg
- Wheelbase: 0.100 m
- Track width: 0.100 m
- Centre-of-gravity height: 0.045 m
- Wheel radius: 0.028 m
- Friction coefficient: 0.65
- Gravity: 9.81 m/s²

The full assumptions and equations are in [Reference Vehicle Design Case](../design_basis/reference_vehicle_design_case.md).

## Running the parameter sweep

From this folder, run:

```bash
python parameter_sweep.py
```

The script creates `reference_design_sweep.csv`. It includes longitudinal and lateral load-transfer estimates for a range of inputs, plus theoretical ground-speed estimates at 250 and 300 deg/s. The speed calculation uses a 28 mm wheel radius, a 1:1 motor-to-wheel ratio, and assumes there is no wheel slip.

## Running the automated tests

We have standard-library unit tests for the reference calculation in `tests/test_reference_model.py`. From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

The tests check the baseline values, the zero-acceleration case, the linear relationship between acceleration and load transfer, and whether the outputs are finite and non-negative. They check the analytical model only; they do not test the physical robot.

## Limits of the model

The current model uses rigid-body equilibrium and a Coulomb friction limit. It does not include tyre load sensitivity, suspension movement, transient pitch and roll, motor torque-speed curves, battery voltage drop, wheel-slip behaviour, steering motor dynamics, or sensor delay.

We use the model to compare ideas and understand how the input values affect the calculations. We should not use it as a replacement for measurements on the robot.