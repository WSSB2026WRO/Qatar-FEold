# Engineering Risk Assessment

This is our qualitative list of design risks. It records what could go wrong, what the effect might be, how we could notice it, and what control we should consider. We have not assigned numerical risk scores.

| ID | Possible hazard or failure | Possible effect | How we could detect it | Possible mitigation |
|---|---|---|---|---|
| R-01 | Gyro drift or incorrect direction | Heading error and missed turns | Stationary drift and rotation check | Recalibrate, check direction, and use plausibility limits |
| R-02 | False ultrasonic echo | Incorrect lane estimate | Compare both sensors and record unusual readings | Median filtering, reject impossible geometry, and use a close-wall guard |
| R-03 | Camera misclassification | Robot passes a pillar on the wrong side | Signature check and video review | Control lighting, confirm over several frames, and tune thresholds |
| R-04 | Camera I²C communication loss | Missing obstacle information | Count repeated communication errors | Controlled stop or a defined safe state |
| R-05 | Drive wheel slip | Incorrect distance estimate or stopping point | Compare encoder travel with measured distance | Reduce acceleration, improve grip, and calibrate the distance scale |
| R-06 | Steering linkage backlash | Inconsistent cornering | Measure wheel angle from both directions | Reduce play, inspect joints, and calibrate the motor-to-wheel mapping |
| R-07 | Printed part breaks | Loss of steering or sensor support | Visual inspection and fit check | Add rounded transitions, choose a suitable print direction, and test under load |
| R-08 | Cable catches a moving part | Sensor disconnect or mechanical jam | Check the full movement range | Route cables carefully and add strain relief |
| R-09 | Parking estimate is wrong | Incorrect final position | Repeat parking measurements | Improve boundary detection and final alignment |
| R-10 | Battery voltage changes | Different speed and response | Record battery condition | Use consistent charging and repeatable test conditions |

For the longer failure-mode list, rating method, and maintenance checks, see [System Reliability and Failure Mode Analysis](reliability/risk_assessment.md).

This table is a qualitative design review. The mitigations are actions to consider and should not be read as proof that each risk has already been tested.