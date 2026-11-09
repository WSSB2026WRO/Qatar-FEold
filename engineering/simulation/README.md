# Analytical Simulation and Parameter Studies

## Scope

The scripts and tables in this directory are analytical design studies based on an explicitly stated reference case. They are not physics-engine simulations and do not claim physical validation.

## Reference inputs

- Vehicle mass: 0.85 kg
- Wheelbase: 0.100 m
- Track width: 0.100 m
- Centre-of-gravity height: 0.045 m
- Wheel radius: 0.028 m
- Illustrative friction coefficient: 0.65
- Gravity: 9.81 m/s²

See [Reference Vehicle Design Case](../design_basis/reference_vehicle_design_case.md) for assumptions and derivations.

## Reproduction

Run:

```bash
python parameter_sweep.py
```

The script writes `reference_design_sweep.csv` containing longitudinal and lateral load-transfer estimates over a parameter grid.

## Interpretation

The model is intentionally simple. It excludes:
- tire load sensitivity;
- suspension and chassis compliance;
- transient pitch and roll;
- motor torque-speed curves;
- battery voltage sag;
- wheel slip dynamics;
- steering actuator dynamics;
- sensor latency and measurement noise.

Use the results for design comparison and educational analysis only.
