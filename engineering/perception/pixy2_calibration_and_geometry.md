# Pixy2 Vision Calibration and Geometric Reconstruction

## 1. Purpose

The Obstacle Challenge program uses Pixy2 colour signatures to identify red and green pillars. The camera does not directly measure range. Range and lateral position must be estimated from calibrated image geometry.

## 2. Coordinate conventions

Define image coordinates:
- (u): horizontal pixel coordinate, increasing to the right;
- (v): vertical pixel coordinate, increasing downward;
- ((u_c,v_c)): calibrated image centre;
- (f_x,f_y): effective focal lengths in pixel units.

Define vehicle coordinates:
- (X): forward;
- (Y): left;
- (Z): upward.

## 3. Pinhole bearing model

For horizontal pixel coordinate (u):

[
\alpha=\tan^{-1}\left(\frac{u-u_c}{f_x}\right)
]

The effective focal length may be estimated from the horizontal field of view (phi_h) and image width (N_u):

[
f_x=\frac{N_u/2}{\tan(\phi_h/2)}
]

## 4. Ground-plane range model

If a visible pillar base is assumed to lie on a known ground plane, a calibrated camera height and downward pitch can be used to estimate ground range. For a camera with height (h_c), downward pitch (	heta), and vertical ray angle (eta), a simplified planar model is:

[
d=\frac{h_c}{\tan(\theta+\beta)}
]

This model is sensitive to the exact pixel coordinate representing the pillar base, camera pitch, and mounting height. It is not interchangeable with a top-edge image-height model.

## 5. Empirical calibration alternative

The supplied program uses an empirical vertical-image model:

[
d=\frac{K}{v-v_0}
]

with configured constants (K) and (v_0). The model should be fitted from a set of known distances rather than assumed universal.

Recommended calibration:
1. Fix the camera in its final mount.
2. Place a pillar at a series of measured distances.
3. Capture multiple frames at each distance.
4. Record the same block feature (e.g. bottom edge or centre) consistently.
5. Fit (K) and (v_0) by least squares.
6. Plot residual error versus distance.
7. Repeat under the competition lighting conditions.

## 6. Colour classification

Signature IDs are camera configuration labels, not universal colour codes. Verify red and green signature IDs in the final PixyMon configuration. Record lighting, exposure, ambient illumination, and background conditions.

## 7. Confidence and temporal filtering

A detection should be accepted only when:
- signature is permitted;
- block dimensions exceed minimum thresholds;
- aspect ratio is plausible;
- block location is within the expected image region;
- detection persists across a defined number of frames.

A median or trimmed-mean filter can reduce single-frame jitter. Do not average detections across different pillar identities.

## 8. Calibration report — illustrative analytical dataset

The following table is a **synthetic calculation example** generated from the empirical model configured in the supplied program:

\[
d_{estimated}=\frac{K}{v-v_0},\qquad K=20100,\quad v_0=63
\]

For this example, the reference distances are hypothetical inputs. The image feature coordinate is rounded to the nearest pixel, and the estimated range is recalculated from that rounded coordinate.

| Known range (mm) | Image feature (px) | Estimated range (mm) | Error (mm) |
|---:|---:|---:|---:|
| 200 | 164 | 199.0 | -1.0 |
| 250 | 143 | 251.2 | +1.2 |
| 300 | 130 | 300.0 | 0.0 |
| 400 | 113 | 402.0 | +2.0 |
| 500 | 103 | 502.5 | +2.5 |
| 600 | 96 | 609.1 | +9.1 |
| 700 | 92 | 693.1 | -6.9 |
| 800 | 88 | 804.0 | +4.0 |

### Calculation method

\[
Error=d_{estimated}-d_{known}
\]

\[
d_{estimated}=\frac{20100}{v-63}
\]

For example, at the hypothetical 600 mm reference distance, the rounded image feature is 96 px:

\[
d_{estimated}=\frac{20100}{96-63}=609.1\text{ mm}
\]

The resulting illustrative error is +9.1 mm.

### Interpretation

The example shows how pixel quantization affects range estimation. As the detected feature approaches the offset (v_0), a one-pixel change can produce a larger distance error. Calibration should therefore use repeated measurements across the full operating range and report mean absolute error, maximum absolute error, and residual distribution.

**Data status:** Every row above is synthetic and calculated from the configured model. It is not a real Pixy2 measurement and must not be presented as experimental validation. Replace this table with recorded camera observations before declaring the range model calibrated.
