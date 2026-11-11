# Steering Geometry and Linkage

![STR-001 — Ackermann steering geometry](../../docs/drawings/STR-001_ackermann_steering.svg)

## 1. Why steering geometry matters

We use the steering geometry to understand how the steering motor turns the road wheels. It affects the turning radius, tyre scrub, path through a corner, motor load, and how repeatable the steering can be.

## 2. Ideal geometry at low speed

For wheelbase (L), track (T), and turn radius (R) measured from the centre of the rear axle:

[
\tan(\delta_i)=\frac{L}{R-T/2},\quad
\tan(\delta_o)=\frac{L}{R+T/2}
]

The inner wheel angle (delta_i) is larger than the outer wheel angle (delta_o).

The equivalent Ackermann relationship is:

[
\cot(\delta_o)-\cot(\delta_i)=\frac{T}{L}
]

## 3. Measurements and dimensions we need

When we describe the linkage, we should include:
- Steering pivot positions.
- Steering arm length and direction.
- Tie-rod length.
- Actuator crank radius.
- Straight-ahead or neutral steering angle.
- Left and right mechanical stops.
- Joint clearance and backlash.
- Flex in the parts when the tyres are loaded.

## 4. Connecting motor angle to wheel angle

Our control program needs to relate the steering motor encoder angle (	heta_m) to the actual road-wheel angle (delta_w). If the linkage is not linear, a lookup table or fitted polynomial may describe it better than one constant ratio.

We can check this relationship by:

1. Putting the vehicle on a level surface.
2. Measuring the wheel angle at several encoder positions in both directions.
3. Approaching each position from the left and right to estimate backlash.
4. Fitting a monotonic mapping and checking the remaining error.
5. Setting the software limits before the linkage binds or puts too much load on a joint.

## 5. Problems we should look for

| Possible problem | What it can cause | What we can check |
|---|---|---|
| Linkage binding | High motor load or stalled steering | Move through the full steering range |
| Too much backlash | Wheel angle changes from run to run | Check joint clearance |
| Different left/right travel | Different turning behaviour | Measure both directions |
| Flexible steering arms | Wheel angle changes under load | Increase stiffness or shorten the lever |
| Loose printed joint | Steering geometry changes suddenly | Check retention and inspect regularly |

## 6. What the steering drawing should show

For the steering assembly, we should include a top view, pivot positions, tie-rod length, steering-arm dimensions, actuator travel, left and right wheel angles, and the mechanical stops.