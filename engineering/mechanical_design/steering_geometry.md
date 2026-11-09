# Conceptual Steering Geometry Study

> Conceptual design note. This is not a claim that the current physical steering linkage has been measured or matches the model.

## 1. Purpose

Steering geometry determines the relationship between actuator rotation and road-wheel angle. It affects turning radius, tire scrub, corner tracking, actuator load, and repeatability.

## 2. Ideal low-speed geometry

For wheelbase (L), track (T), and turn radius measured to the rear-axle midpoint (R):

[
	an(delta_i)=rac{L}{R-T/2},quad
	an(delta_o)=rac{L}{R+T/2}
]

The inner wheel angle (delta_i) is greater than the outer wheel angle (delta_o).

Equivalent Ackermann relation:

[
cot(delta_o)-cot(delta_i)=rac{T}{L}
]

## 3. Linkage design variables

- Steering pivot coordinates
- Steering arm length and orientation
- Tie-rod length
- Actuator crank radius
- Neutral steering angle
- Left and right mechanical stops
- Joint clearance and backlash
- Structural compliance under tire load

## 4. Actuator-to-wheel mapping

A robust control system should calibrate the mapping from steering motor encoder angle (	heta_m) to road-wheel angle (delta_w). For a nonlinear linkage, a lookup table or fitted polynomial may be more accurate than a constant ratio.

Calibration procedure:
1. Place the vehicle on a level surface.
2. Measure road-wheel angle at multiple encoder positions on both sides.
3. Repeat while approaching each point from both directions to estimate backlash.
4. Fit a monotonic mapping and inspect residual error.
5. Set mechanical limits below the point of binding or excessive joint load.

## 5. Failure modes

| Failure mode | Effect | Design control |
|---|---|---|
| Linkage binding | High motor load or stalled steering | Check full-travel clearances |
| Excessive backlash | Inconsistent wheel angle | Reduce joint clearance |
| Unequal left/right travel | Asymmetric turning | Calibrate both directions |
| Flexible steering arms | Angle error under load | Increase stiffness or reduce lever arm |
| Loose printed joint | Sudden geometry change | Retention features and inspection |

## 6. Required drawings and measurements

A released steering study requires a top-view dimensioned drawing, pivot coordinates, tie-rod length, steering arm dimensions, left/right road-wheel angle table, and a record of mechanical stop positions.
