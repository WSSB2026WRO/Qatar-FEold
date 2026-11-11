# Reference Vehicle Design Case

## Why we made this model

We use this example design case to keep the calculations, diagrams, and software-in-the-loop studies consistent. It is an illustrative model, not a measured specification of our competition robot.

Every result below is calculated from the assumptions in the table. We should not describe these numbers as physical test results.

## Values used in the reference case

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

First, we calculate the vehicle weight:

[
W=mg=0.85(9.81)=8.3385\;N
]

The longitudinal centre of gravity is halfway along the wheelbase in this example, so the front and rear axle loads are:

[
F_{front}=F_{rear}=W/2=4.1693\;N
]

If the load is also shared equally from left to right, the load at each wheel is approximately:

[
F_{wheel}=W/4=2.0846\;N
]

These are ideal static reactions. The real load at each wheel can change because of chassis flexibility and how the supports are assembled.

## Longitudinal load transfer

[
\Delta F_x=\frac{m a_x h_{CG}}{L}
=\frac{0.85(0.80)(0.045)}{0.10}
=0.306\;N
]

In this simplified model, acceleration transfers about 0.306 N from the front axle to the rear axle. Under braking, the transfer is in the opposite direction.

## Lateral load transfer

[
\Delta F_y=\frac{m a_y h_{CG}}{T}
=\frac{0.85(1.20)(0.045)}{0.10}
=0.459\;N
]

This is the load-transfer quantity under the convention used in the model. To calculate each wheel reaction in more detail, we would also need a defined model for chassis and suspension compliance.

## Idealised lateral tip threshold

[
a_{y,tip}=g\frac{T}{2h_{CG}}
=9.81\frac{0.10}{2(0.045)}
=10.90\;m/s^2
]

This is only a geometric estimate. It is not a safe operating limit. Tyre sliding, sudden movement, frame flexibility, and an uneven floor can cause the robot to lose control at a lower acceleration.

## Drive speed example

For a wheel radius of 0.028 m and a direct 1:1 wheel-to-motor ratio, we use:

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

These are ideal speeds with no wheel slip. Actual speed also depends on the load, motor response, battery voltage, drivetrain losses, and tyre grip.

## Design points we want to check

1. Keep the heaviest battery or energy-storage part low and near the middle of the vehicle.
2. Mount the camera and distance sensors on supports that do not move easily.
3. Keep the left and right mass distribution as balanced as the layout allows.
4. Avoid putting heavy parts at the very front or rear unless the design needs it.
5. Use steering stops and check the relationship between motor encoder position and wheel angle.
6. Check the assumed values on the real vehicle before using this model to make a final design decision.