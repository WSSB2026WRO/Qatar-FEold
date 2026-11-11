# Verification Evidence

We use this page to show which checks can be repeated from the repository. It is important for us to keep software checks and calculations separate from tests carried out on the physical robot.

## 1. Automated software checks

The GitHub Actions workflow called **Python Validation** completed successfully on 11 November 2026.

- Recorded run: [Run #216 — successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43079056309)
- Commit checked: `a9530e7c626da46464fa999080a308a67cd770dd`
- Result: **success**

The workflow carried out these steps:

1. Compiled `software/open_challenge/open_challenge.py`.
2. Compiled `software/obstacle_challenge/obstacle_challenge.py`.
3. Compiled `engineering/simulation/parameter_sweep.py`.
4. Ran the analytical model unit tests and documentation-integrity tests (8 tests in total).
5. Ran the analytical parameter sweep.
6. Uploaded `reference_design_sweep.csv` as a workflow artifact.

The sweep uses 30 input combinations: five longitudinal acceleration values (0.2–1.0 m/s²) and six lateral acceleration values (0.2–1.2 m/s²). Each row contains load-transfer and stability estimates, as well as ideal wheel-ground speed at 250 and 300 deg/s. The speed calculation assumes a 1:1 ratio and no wheel slip. The CSV can be downloaded from the Artifacts section of the workflow run.

**What we can say from this run:** both Python challenge files and the analytical script passed compilation, all eight tests passed, and the sweep finished and created its output file.

**What we cannot say from this run:** it does not prove that the programs run correctly on the EV3, that the sensors give accurate readings, or that the robot steers, avoids obstacles, completes laps, or parks correctly on the real track.

## 2. Calculations that can be repeated

The values below come from the reference model in `engineering/simulation/parameter_sweep.py`. They are also described in `engineering/simulation/reference_case_results.md`.

| Quantity | Inputs or method | Calculated result |
|---|---|---:|
| Vehicle weight | 0.85 kg × 9.81 m/s² | 8.3385 N |
| Static load per wheel | 8.3385 N ÷ 4, assuming equal load | 2.0846 N |
| Longitudinal load transfer | 0.85 kg × 0.80 m/s² × 0.045 m ÷ 0.100 m | 0.3060 N |
| Lateral load transfer | 0.85 kg × 1.20 m/s² × 0.045 m ÷ 0.100 m | 0.4590 N |
| Idealised lateral tip acceleration | 9.81 × 0.100 m ÷ (2 × 0.045 m) | 10.90 m/s² |
| Simplified friction-force bound | 0.65 × 8.3385 N | 5.420 N |
| Theoretical speed at 250°/s | 56 mm wheel, 1:1 ratio, no slip | 0.1222 m/s |
| Theoretical speed at 300°/s | 56 mm wheel, 1:1 ratio, no slip | 0.1466 m/s |

These are calculated estimates, not readings from the robot. They depend on the reference inputs and simplified assumptions. For example, the friction estimate does not include motor torque, real tyre behaviour, floor condition, or wheel slip.

## 3. Physical tests

The current repository snapshot does not contain completed physical test reports or raw EV3 mission logs. For that reason, we do not list physical sensor accuracy, steering repeatability, obstacle clearance, corner execution, lap completion, or parking accuracy as measured results.

## 4. Running the checks again

From the repository root, use:

```bash
python -m py_compile software/open_challenge/open_challenge.py
python -m py_compile software/obstacle_challenge/obstacle_challenge.py
python -m py_compile engineering/simulation/parameter_sweep.py
cd engineering/simulation
python parameter_sweep.py
```

The last command creates `reference_design_sweep.csv` in the same folder as the script.