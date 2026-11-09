# Reference Vehicle Design Case

## Purpose and status

This document establishes a coherent **illustrative engineering design case** for calculations, diagrams, and software-in-the-loop studies. It is a theoretical reference model, not a measured specification of the competition robot.

All numerical outputs in this design case are calculated from the assumptions below. They must not be represented as physical test results.

## Reference configuration

| Parameter | Design value | Unit | Classification |
|---|---:|---|---|
| Total vehicle mass | 0.85 | kg | Illustrative assumption |
| Overall length | 180 | mm | Illustrative envelope |
| Overall width | 110 | mm | Illustrative envelope |
| Overall height | 210 | mm | Illustrative envelope |
| Wheelbase | 100 | mm | Design assumption |
| Front track | 100 | mm | Design assumption |
| Rear track | 100 | mm | Design assumption |
| Wheel diameter | 56 | mm | Software configuration reference |
| Wheel radius | 28 | mm | Derived from nominal diameter |
| Longitudinal CG coordinate | 50 | mm from rear axle | Symmetric design assumption |
| Lateral CG coordinate | 0 | mm from centreline | Symmetric design assumption |
| CG height | 45 | mm | Illustrative assumption |
| Gravity | 9.81 | m/s² | Physical constant |
| Design longitudinal acceleration | 0.80 | m/s² | Scenario input |
| Design lateral acceleration | 1.20 | m/s² | Scenario input |
| Illustrative friction coefficient | 0.65 | — | Scenario input; surface-dependent |

## Static load estimate

Total weight:

[
W=mg=0.85(9.81)=8.3385\;N
]

With the longitudinal CG at half wheelbase:

[
F_{front}=F_{rear}=W/2=4.1693\;N
]

For a symmetric lateral distribution, each wheel carries approximately:

[
F_{wheel}=W/4=2.0846\;N
]

These are idealized static reactions. Real four-wheel load distribution depends on chassis and support compliance.

## Longitudinal load transfer

[
\Delta F_x=\frac{m a_x h_{CG}}{L}
=\frac{0.85(0.80)(0.045)}{0.10}
=0.306\;N
]

During acceleration, approximately 0.306 N transfers from the front axle to the rear axle in this simplified model. During braking, the direction reverses.

## Lateral load transfer

[
\Delta F_y=\frac{m a_y h_{CG}}{T}
=\frac{0.85(1.20)(0.045)}{0.10}
=0.459\;N
]

This simplified result represents the load-transfer quantity under the adopted convention. Detailed wheel-by-wheel reactions require a defined chassis compliance model.

## Idealized lateral tip threshold

[
a_{y,tip}=g\frac{T}{2h_{CG}}
=9.81\frac{0.10}{2(0.045)}
=10.90\;m/s^2
]

This ideal geometric threshold is not a recommended operating limit. Tire sliding, transient roll, structural flexibility, and uneven surfaces may cause loss of control at lower acceleration.

## Drive speed reference

For a wheel radius of 0.028 m and a direct 1:1 wheel-to-motor ratio:

[
v=\omega r
]

At 250 deg/s:

[
v=250\frac{\pi}{180}(0.028)=0.1222\;m/s
]

At 300 deg/s:

[
v=300\frac{\pi}{180}(0.028)=0.1466\;m/s
]

These are ideal no-slip kinematic estimates. Actual speed depends on load, motor response, battery voltage, drivetrain losses, and tire slip.

## Design decisions

1. Keep the heaviest energy-storage component low and near the longitudinal centre.
2. Keep the camera and ranging sensors on rigid, short mounting structures.
3. Keep left/right mass distribution as symmetric as packaging allows.
4. Avoid placing heavy components at the extreme front or rear unless required by the task.
5. Use mechanical steering stops and calibrate the actuator-to-wheel mapping.
6. Validate every assumed parameter before using this model for a physical design decision.

## Traceability

This model is intended to support comparative calculations and parameter sweeps. The values are design assumptions, not claims of measured vehicle properties.
