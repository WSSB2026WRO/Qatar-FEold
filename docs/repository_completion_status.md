# Qatar FE — Repository Status

**Repository:** [WSSB2026WRO/Qatar-FE](https://github.com/WSSB2026WRO/Qatar-FE)  
**WRO team number:** **6038**  
**Branch:** `main`  
**Portfolio date:** 11 November 2026

## What this repository contains

We use this repository to keep the work for Team 6038's WRO Future Engineers robot in one place. It includes our Python/Pybricks programs for the Open and Obstacle Challenges, the matching LEGO EV3 block projects, hardware and port information, mechanical and electrical notes, Pixy2 documentation, vehicle-dynamics calculations, engineering diagrams, reliability notes, validation files, and automated software checks.

## Two ways of programming the EV3

We have included two versions of the challenge programs:

- **Python:** our Pybricks MicroPython programs.
- **LEGO EV3 blocks:** the native graphical projects for both challenges.

Keeping both versions lets us compare the programming workflow, preparation and build time, startup delay, control-cycle timing, mission time, debugging, and reliability on the EV3. The comparison criteria are explained in [Implementation Comparison](../software/implementation_comparison.md).

We are interested in timing differences, including differences smaller than one second. Build time, startup delay, and control-cycle duration are different things, so we keep them separate. At the moment, this repository does not contain a paired timing dataset for both implementations. We therefore do not claim that one version is faster.

## Pixy2 illumination note

The front illumination is part of the Pixy2 camera assembly. The camera connects to EV3 sensor port S4 through I²C. It is not a separate lamp on motor port D. Port D is unused by both challenge programs.

## Automated checks recorded here

The repository records a successful GitHub Actions run on 11 November 2026:

- [Python Validation — run #216, successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43079056309)
- Commit checked: `a9530e7c626da46464fa999080a308a67cd770dd`
- Both Python challenge programs and the analytical script passed Python compilation.
- Eight analytical and documentation-integrity tests passed.
- The 30-case analytical parameter sweep finished and generated its CSV artifact.

These checks tell us that the Python files compile and that the listed automated tests and calculations ran. They do not prove that the robot completed a physical run, and they do not test the EV3 block projects.

## How we label the evidence

We use these labels in the engineering notes:

- **Configured:** a value set in the program or device configuration.
- **Assumed:** an input chosen for a reference calculation.
- **Calculated:** a result worked out from an equation and stated inputs.
- **Simulated:** a result produced by the analytical parameter sweep.
- **Measured:** an observation taken from the physical robot and supported by a measurement record.

The vehicle-dynamics results are calculations based on a reference case. The Pixy2 distance equation is a configured empirical model; a physical camera-calibration dataset is not included. The validation folder contains a test framework and record template, but no completed physical mission logs or paired sub-second timing logs.

## Other project files

The custom-parts folder contains inspection notes for three named STL models, but the original STL and native CAD files are not in this repository snapshot. The video folder is an index and does not contain committed demonstration videos. We list these limits so readers can see what is actually available here.

The root README is the starting point for the portfolio. The other folders contain the software, diagrams, calculations, tests, and media indexes.