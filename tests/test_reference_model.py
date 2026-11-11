"""Unit tests for the analytical reference-vehicle model.

These tests validate calculations only. They do not represent physical robot tests.
"""
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIMULATION_DIR = ROOT / "engineering" / "simulation"
sys.path.insert(0, str(SIMULATION_DIR))

import parameter_sweep  # noqa: E402


class ReferenceVehicleModelTests(unittest.TestCase):
    def test_reference_case_matches_documented_calculations(self):
        result = parameter_sweep.calculate(0.8, 1.2)

        self.assertAlmostEqual(result["weight_N"], 8.3385, places=4)
        self.assertAlmostEqual(result["longitudinal_transfer_N"], 0.306, places=6)
        self.assertAlmostEqual(result["lateral_transfer_N"], 0.459, places=6)
        self.assertAlmostEqual(result["ideal_tip_acceleration_m_s2"], 10.9, places=6)
        self.assertAlmostEqual(result["friction_bound_N"], 5.420025, places=6)

    def test_zero_acceleration_has_zero_load_transfer(self):
        result = parameter_sweep.calculate(0.0, 0.0)
        self.assertEqual(result["longitudinal_transfer_N"], 0.0)
        self.assertEqual(result["lateral_transfer_N"], 0.0)

    def test_load_transfer_scales_linearly_with_acceleration(self):
        low = parameter_sweep.calculate(0.2, 0.4)
        high = parameter_sweep.calculate(0.8, 1.2)

        self.assertAlmostEqual(
            high["longitudinal_transfer_N"],
            4.0 * low["longitudinal_transfer_N"],
            places=12,
        )
        self.assertAlmostEqual(
            high["lateral_transfer_N"],
            3.0 * low["lateral_transfer_N"],
            places=12,
        )

    def test_reference_outputs_are_finite_and_nonnegative(self):
        result = parameter_sweep.calculate(0.8, 1.2)
        for key, value in result.items():
            if key.endswith("_N") or key.endswith("_m_s2"):
                self.assertTrue(math.isfinite(value), key)
                self.assertGreaterEqual(value, 0.0, key)


if __name__ == "__main__":
    unittest.main()
