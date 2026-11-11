# Reference Case — Calculated Results

The results on this page come from the reference model and the inputs listed below. They are calculations, not measurements from the physical robot.

## Inputs used

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

## Load-transfer examples

| Scenario | Acceleration | Calculated transfer |
|---|---:|---:|
| Mild acceleration | 0.20 m/s² | 0.0765 N longitudinal |
| Reference acceleration | 0.80 m/s² | 0.3060 N longitudinal |
| Stronger acceleration | 1.00 m/s² | 0.3825 N longitudinal |
| Mild lateral manoeuvre | 0.40 m/s² | 0.1530 N lateral |
| Reference lateral manoeuvre | 1.20 m/s² | 0.4590 N lateral |

## Idealised limits and speed estimates

| Quantity | Calculated value |
|---|---:|
| Geometric lateral tip acceleration | 10.90 m/s² |
| Friction-force bound for the whole vehicle | 5.420 N |
| Ideal wheel speed at 250 deg/s motor speed | 0.1222 m/s |
| Ideal wheel speed at 300 deg/s motor speed | 0.1466 m/s |

## What we learn from these calculations

The equations show how centre-of-gravity height and track width affect the estimated load transfer and geometric lateral stability. The friction limit is a simplified Coulomb estimate. Real usable drive force also depends on motor torque, tyre behaviour, floor condition, and wheel slip.

The wheel-speed conversion assumes a 1:1 ratio, no slip, and a 56 mm wheel diameter. It gives a theoretical relationship between motor speed and ground speed. The parameter-sweep CSV includes reference-speed columns for both 250 deg/s and 300 deg/s.