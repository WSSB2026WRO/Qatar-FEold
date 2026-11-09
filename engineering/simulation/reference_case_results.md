# Reference Case — Calculated Results

## Baseline design inputs

| Input | Value |
|---|---:|
| Mass | 0.85 kg |
| Wheelbase | 0.100 m |
| Track width | 0.100 m |
| CG height | 0.045 m |
| Wheel radius | 0.028 m |
| Friction coefficient | 0.65 |
| Gravity | 9.81 m/s² |

## Static load calculation

| Quantity | Calculated value |
|---|---:|
| Total weight | 8.3385 N |
| Front axle load, symmetric case | 4.1693 N |
| Rear axle load, symmetric case | 4.1693 N |
| Nominal load per wheel, symmetric case | 2.0846 N |

## Dynamic load-transfer scenarios

| Scenario | Acceleration | Transfer estimate |
|---|---:|---:|
| Mild acceleration | 0.20 m/s² | 0.0765 N longitudinal |
| Reference acceleration | 0.80 m/s² | 0.3060 N longitudinal |
| Stronger acceleration | 1.00 m/s² | 0.3825 N longitudinal |
| Mild lateral manoeuvre | 0.40 m/s² | 0.1530 N lateral |
| Reference lateral manoeuvre | 1.20 m/s² | 0.4590 N lateral |

## Idealized limits

| Quantity | Calculated value |
|---|---:|
| Geometric lateral tip acceleration | 10.90 m/s² |
| Friction force bound, total vehicle | 5.420 N |
| Ideal wheel speed at 250 deg/s motor speed | 0.1222 m/s |
| Ideal wheel speed at 300 deg/s motor speed | 0.1466 m/s |

## Engineering interpretation

The calculations show the influence of centre-of-gravity height and track width on geometric load transfer and lateral stability. The friction bound is a simplified Coulomb estimate; usable tractive force also depends on motor torque, tire characteristics, floor condition, and wheel slip.

The wheel-speed conversion assumes a 1:1 ratio, no slip, and a 56 mm wheel diameter. It provides the kinematic relationship between motor speed and theoretical ground speed.
