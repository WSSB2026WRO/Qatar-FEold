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

## 8. Calibration report template

| Known range (mm) | Image feature (px) | Estimated range (mm) | Error (mm) |
|---:|---:|---:|---:|
|  |  |  |  |

The calibration table must be populated from real measurements before the model is used as a validated range sensor.
