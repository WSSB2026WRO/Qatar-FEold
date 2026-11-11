# Analytical Simulation and Parameter Studies

## Scope

This directory contains reproducible analytical studies for the Qatar FE reference vehicle design case. The models evaluate vehicle load transfer, traction limits, geometric stability, and the sensitivity of key parameters.

## Reference inputs

- Vehicle mass: 0.85 kg
- Wheelbase: 0.100 m
- Track width: 0.100 m
- Centre-of-gravity height: 0.045 m
- Wheel radius: 0.028 m
- Friction coefficient: 0.65
- Gravity: 9.81 m/s²

The complete design basis and governing equations are documented in [Reference Vehicle Design Case](../design_basis/reference_vehicle_design_case.md).

## Reproduction

```bash
python parameter_sweep.py
```

The script writes `reference_design_sweep.csv` with longitudinal and lateral load-transfer estimates over a parameter grid, plus theoretical ground-speed estimates at 250 and 300 deg/s. The speed estimates use the 28 mm reference wheel radius, a 1:1 motor-to-wheel ratio, and a no-slip assumption.

## Automated unit tests

The repository includes standard-library unit tests for the reference calculation in `tests/test_reference_model.py`. Run them from the repository root with:

```bash
python -m unittest discover -s tests -v
```

These tests check the documented baseline values, zero-acceleration behaviour, linear load-transfer scaling, and finite non-negative outputs. They validate the analytical model only; they do not test the physical vehicle.

## Model definition

The current analytical model uses rigid-body equilibrium and a Coulomb friction bound. It does not include tire load sensitivity, suspension compliance, transient pitch and roll, motor torque-speed curves, battery voltage sag, wheel-slip dynamics, steering actuator dynamics, or sensor latency.

The model is intended for engineering comparison, parameter sensitivity, and design reasoning.
