# Pixy2 Camera Geometry and Calibration Notes

![CAM-001 — Pixy2 camera geometry](../../docs/drawings/CAM-001_pixy2_camera_geometry.svg)

## 1. What the camera does

In the Obstacle Challenge, we use the Pixy2 to detect the red and green pillar signatures. The camera and its built-in illumination are one assembly connected to EV3 sensor port S4 through I²C.

The camera does not directly give us the distance to a pillar. Our program estimates distance and side position from the image.

## 2. Coordinate directions

For the image, we use:
- (u): horizontal pixel coordinate, increasing to the right.
- (v): vertical pixel coordinate, increasing downward.
- ((u_c,v_c)): calibrated image centre.
- (f_x,f_y): effective focal lengths in pixels.

For the vehicle, we use:
- (X): forward.
- (Y): left.
- (Z): upward.

## 3. Estimating the horizontal bearing

For horizontal image coordinate (u):

[
\alpha=\tan^{-1}\left(\frac{u-u_c}{f_x}\right)
]

We can estimate the effective focal length from the horizontal field of view (phi_h) and image width (N_u):

[
f_x=\frac{N_u/2}{\tan(\phi_h/2)}
]

## 4. Estimating range from the ground plane

If the bottom of a visible pillar is on a known flat ground plane, camera height and downward angle can be used to estimate its distance. For camera height (h_c), downward pitch (	heta), and vertical ray angle (\\betaeta), a simplified model is:

[
d=\frac{h_c}{\tan(\theta+\beta)}
]

The result depends on the exact image point chosen at the pillar base, the camera angle, and the mounting height. This is not the same method as estimating distance from the apparent height of a block. The angles (	heta) and (\\betaeta) are measured in the vertical camera plane.

## 5. Empirical model used in our program

Our current program uses an empirical relationship based on the vertical image coordinate:

[
d=\frac{K}{v-v_0}
]

The constants (K) and (v_0) are set in the program. They describe the model we are using; they are not universal Pixy2 camera constants.

The reference table in this document was calculated from these constants and rounded pixel coordinates. It is not a set of readings collected from the camera.

## 6. Colour signatures

Signature numbers depend on the Pixy2 configuration. In our documented setup, signature 1 means red and signature 2 means green. Lighting, exposure, surrounding colours, and the background can all affect what the camera detects.

## 7. Filtering detections

The program checks the signature, minimum block dimensions, aspect ratio, image region, and whether the detection remains present over several frames. Filtering can reduce changes caused by a single frame, but detections belonging to different pillars must still be treated as separate objects.

## 8. Reference calibration calculation

### 8.1 Model in the program

The Obstacle Challenge program uses:

[
d=\frac{K}{v-v_0}
]

where:
- (d) is estimated camera-to-pillar distance in millimetres.
- (v) is the selected vertical image feature in pixels.
- (K=20100\;\text{px}\cdot\text{mm}).
- (v_0=63\;\text{px}).

To create the reference image-coordinate column, we use the inverse equation:

[
v=v_0+\frac{K}{d}
]

### 8.2 Reference calculation table

| Known range (mm) | Image feature (px) | Estimated range (mm) | Error (mm) |
|---:|---:|---:|---:|
| 150 | 197 | 150.00 | 0.00 |
| 200 | 164 | 199.01 | -0.99 |
| 250 | 143 | 251.25 | +1.25 |
| 300 | 130 | 300.00 | 0.00 |
| 350 | 120 | 352.63 | +2.63 |
| 400 | 113 | 402.00 | +2.00 |
| 450 | 108 | 446.67 | -3.33 |
| 500 | 103 | 502.50 | +2.50 |
| 600 | 96 | 609.09 | +9.09 |
| 700 | 92 | 693.10 | -6.90 |
| 800 | 88 | 804.00 | +4.00 |
| 900 | 85 | 913.64 | +13.64 |

**Important:** The image coordinates are calculated reference values. We get them by rounding (v=v_0+K/d) to the nearest pixel. The estimated distances and errors are then calculated from those rounded coordinates. They are not camera observations.

**Error convention:** (e=d_{estimated}-d_{known}). A positive value means the estimate is higher than the reference distance; a negative value means it is lower.

### 8.3 One calculation example

For a reference distance of 600 mm, the rounded image feature is 96 px:

[
d=\frac{20100}{96-63}=609.09\;\text{mm}
]

[
e=609.09-600=+9.09\;\text{mm}
]

### 8.4 Summary of the reference table

| Metric | Result |
|---|---:|
| Number of reference points | 12 |
| Mean absolute error (MAE) | 3.86 mm |
| Root mean square error (RMSE) | 5.50 mm |
| Maximum absolute error | 13.64 mm |
| Maximum error location | 900 mm reference range |

### 8.5 What the numbers tell us

The error becomes larger at longer distances because the equation becomes more sensitive to pixel rounding as (v) gets closer to (v_0). This follows from the inverse relationship between image position and estimated distance.

The useful range of this model depends on how much error we can accept. It cannot be decided only by how far away the camera can still see a pillar.

### 8.6 What still needs to be measured

We calculated this reference table from the configured equation and rounded pixel coordinates. It helps us check the formula and the error calculation, but it does not show how accurately the real camera measures distance.

We still need to collect camera observations at known distances and write up a physical calibration report.