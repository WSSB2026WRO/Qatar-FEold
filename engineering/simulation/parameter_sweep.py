"""Reproducible conceptual parameter sweep for the Qatar FE reference design case.

This script computes analytical estimates only. It does not simulate a physical
robot, tire dynamics, motor saturation, or competition performance.
Run with: python parameter_sweep.py
"""
import csv
import math
from pathlib import Path

MASS_KG = 0.85
WHEELBASE_M = 0.100
TRACK_M = 0.100
CG_HEIGHT_M = 0.045
GRAVITY = 9.81
WHEEL_RADIUS_M = 0.028
FRICTION_COEFFICIENT = 0.65

def calculate(ax, ay):
    weight = MASS_KG * GRAVITY
    longitudinal_transfer = MASS_KG * ax * CG_HEIGHT_M / WHEELBASE_M
    lateral_transfer = MASS_KG * ay * CG_HEIGHT_M / TRACK_M
    tip_acceleration = GRAVITY * TRACK_M / (2 * CG_HEIGHT_M)
    friction_bound = FRICTION_COEFFICIENT * weight
    ideal_speed_250 = math.radians(250) * WHEEL_RADIUS_M
    ideal_speed_300 = math.radians(300) * WHEEL_RADIUS_M
    return {
        "ax_m_s2": ax,
        "ay_m_s2": ay,
        "weight_N": weight,
        "longitudinal_transfer_N": longitudinal_transfer,
        "lateral_transfer_N": lateral_transfer,
        "ideal_tip_acceleration_m_s2": tip_acceleration,
        "friction_bound_N": friction_bound,
        "ideal_speed_250_deg_s_m_s": ideal_speed_250,
        "ideal_speed_300_deg_s_m_s": ideal_speed_300,
    }

def main():
    rows = []
    for ax in (0.2, 0.4, 0.6, 0.8, 1.0):
        for ay in (0.2, 0.4, 0.6, 0.8, 1.0, 1.2):
            rows.append(calculate(ax, ay))
    output = Path(__file__).with_name("reference_design_sweep.csv")
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} analytical cases to {output}")

if __name__ == "__main__":
    main()
