# Engineering Release Checklist

## Documentation
- [ ] Every document has a title, scope, revision date, and evidence classification.
- [ ] Units are stated for every numerical quantity.
- [ ] Assumptions are separated from source-derived facts.
- [ ] Diagrams identify schematic versus measured geometry.
- [ ] Equations define all variables.

## Mechanical
- [ ] Chassis envelope and datums documented.
- [ ] Wheelbase and track measured.
- [ ] Steering pivots and linkage dimensions measured.
- [ ] Component mass register completed.
- [ ] Centre of gravity calculated from measured inputs.
- [ ] Printed parts have CAD source and revision identifiers.
- [ ] STL meshes checked for scale, normals, closure, and fit.
- [ ] Material and print parameters documented.

## Electrical
- [ ] Wiring diagram matches physical build.
- [ ] Power supply ratings verified.
- [ ] Peak current and voltage sag measured.
- [ ] Sensor and motor port mapping verified.
- [ ] Cable strain relief and moving-part clearance inspected.

## Software
- [ ] Source version and hash recorded.
- [ ] Syntax check passes.
- [ ] State transitions reviewed.
- [ ] Sensor fault handling tested.
- [ ] Parameter units and sign conventions documented.
- [ ] CSV logs archived without modification.

## Validation
- [ ] Test procedure is repeatable.
- [ ] Acceptance criteria are numerical.
- [ ] Raw data are retained.
- [ ] Failed and inconclusive tests are documented.
- [ ] Changes trigger regression testing.
