# 3D-Printing Design Notes

## 1. Why we use custom printed parts

We use custom 3D-printed parts when the standard EV3 pieces do not give us the adapter, short link, spacer, or connection shape we need. When we design one, we have to think about its shape, print direction, material, fit, and the direction of the force it will carry.

## 2. Shape and strength

When we prepare a part for printing, we should:
- Leave enough material around holes and narrow sections.
- Use rounded transitions where the part will carry repeated loads.
- Avoid sudden changes in thickness where stress may build up.
- Leave suitable clearance for pins, axles, and connected parts.
- Remember that printer accuracy and material shrinkage can change the final size.
- Choose the print direction so the layer lines support the main load.

## 3. Choosing a material

We compare materials by looking at:
- Stiffness and tensile strength.
- Resistance to impacts.
- Fatigue behaviour after repeated loading.
- Operating temperature.
- Layer bonding.
- How consistently the printer produces the part.

For a joint that carries a large load, we should check the printed part in the direction it will actually be used. A filament datasheet alone does not tell us how a printed part will behave.

## 4. What to record for each print

A useful manufacturing note includes the material and filament grade, nozzle diameter, layer height, number of walls, infill pattern and density, print orientation, bed and nozzle temperatures, and any post-processing.

## 5. Checking the printed part

After printing, we inspect the overall size, pin and axle interfaces, hole diameter and spacing, wall thickness, mesh connections, watertightness, and surface normals. We also check the fit with the parts that will connect to it and make sure moving parts have enough clearance.

## 6. Checking it under load

We should test the part under a load similar to the one it will carry on the robot. After repeated use, we look for bending, cracks, layer separation, loose fits, and wear.

## 7. Keeping design files together

For each part, we should keep the STL export with its original CAD model, dimensioned drawing, units, revision name, and mesh inspection note. When we make a new version, we keep the earlier geometry so we can compare the changes.