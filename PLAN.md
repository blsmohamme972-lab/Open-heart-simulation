# Open Heart Surgery Simulation — Master Plan

**Updated: 2026-11-03 · Planning complete · Research, integrated design and internal document review finished.**

Build a serious, highly realistic open-heart surgery simulation game for personal/noncommercial use. Realism means coherent anatomy, instruments, tissue interaction, physiology, teamwork, visuals and sound. This plan does not certify medical accuracy or clinical training effectiveness. No game code was changed in this task; the existing small Python heartbeat example is not the planned simulator.

## Recommended starting point

Develop a **desktop PC game centered on one adult elective on-pump CABG case**, played primarily as the surgeon with simulated anesthesia, perfusion, assistant and nursing roles. Start with **one coronary anastomosis on an exposed, arrested heart with functioning simulated bypass support**, one modeled defect/recovery path and a replay/debrief. Expand to the complete arrival-to-ICU workflow only after that interaction works convincingly.

Use **Unreal Engine 5.8 as the feasibility candidate**, **Blender** for asset preparation, and **Pulse 4.4.0 as the first physiology candidate** behind a replaceable interface. These choices are conditional on build, licensing, interaction, CPB and performance experiments. Unity 6.3 LTS is the practical fallback; Godot remains an alternative. A custom reduced physiology backend is an explicit scope/funding decision if Pulse cannot support the case. See the sourced [engine](docs/plan/research/04-engine-tech.md) and [physiology](docs/plan/research/02-physiology-perfusion.md) reports.

Initially use bounded tissue regions, authored cut paths, constrained needle handling and explicitly assisted knots. Record each task's fidelity. Unrestricted surgery, calibrated knot mechanics, VR and force feedback need separate feasibility work before becoming release commitments.

## Read the detailed plan

| Document | What it specifies |
|---|---|
| [01 — Scope and fidelity](docs/plan/01-scope-and-fidelity.md) | Intended experience, assumptions, platform, first slice, full-case boundaries and stopping rules |
| [02 — Clinical simulation model](docs/plan/02-clinical-simulation-model.md) | Task graph, anatomy/instrument contracts, physiology coupling, units, observations and verification cases |
| [03 — Technical architecture](docs/plan/03-technical-architecture.md) | Engine/backend decisions, module boundaries, tools/tissue/stitches, clock, replay and performance gates |
| [04 — Assets and presentation](docs/plan/04-assets-and-presentation.md) | Anatomy/OR/tool priorities, Blender pipeline, provenance, tissue materials, motion and audio |
| [05 — Gameplay and assessment](docs/plan/05-gameplay-and-assessment.md) | Modes, desktop controls, team tasks, consequences, debrief, accessibility and assessment limits |
| [06 — Roadmap and validation](docs/plan/06-roadmap-and-validation.md) | Milestones, dependencies, responsible roles, acceptance matrix, cost model and risks |
| [Asset candidates](docs/plan/ASSET_LICENSES.csv) | Item URLs, creators, license evidence, redistribution conditions and blocked candidates |
| [Final gap review](docs/plan/research/00-gap-review.md) | Source spot checks, resolved contradictions, remaining gates and review limits |
| [Progress and upload record](docs/plan/PROGRESS.md) | Completed stages, repository checkpoints, upload outcomes and remaining work |

## Fresh research

All seven domains were researched again on 2026-11-03 using primary sources where available. Each report separates evidence, proposals and remaining uncertainty; earlier drafts remain in Git history.

1. [Surgical procedure and team workflow](docs/plan/research/01-surgical-procedure.md)
2. [Physiology, anesthesia and perfusion](docs/plan/research/02-physiology-perfusion.md)
3. [Assets and licensing](docs/plan/research/03-assets-licensing.md)
4. [Engine and simulation technology](docs/plan/research/04-engine-tech.md)
5. [Visual and audio realism](docs/plan/research/05-visual-audio-realism.md)
6. [Gameplay, controls and assessment](docs/plan/research/06-game-design-assessment.md)
7. [Production and validation](docs/plan/research/07-production-validation.md)

The [research prompts](docs/plan/research/PROMPTS.md) are retained with updated evidence rules. Reports are a targeted planning review, not a systematic literature review. Source availability, licensing checks, runtime tests and expert clinical review are different kinds of evidence.

## Decisions and why they matter

| ID | Planning decision | Reason / reconsideration gate |
|---|---|---|
| D01 | One adult elective on-pump CABG case first | Broad enough to exercise the coupled systems; narrow enough to author and review |
| D02 | Anastomosis slice before full operation | Tests the hardest input/tissue/physiology connection early |
| D03 | Desktop first, offline core | Avoids assuming VR/haptic hardware; precision assistance is recorded honestly |
| D04 | Provisional Unreal + Blender | Native integration and presentation candidate; must pass licensing/build/interaction tests |
| D05 | Evaluate Pulse before funding custom CPB | Existing extracorporeal support is a starting point, not proof of surgical CPB fidelity |
| D06 | One state owner and one simulation clock | Prevents disconnected monitors, double-counted volume and inconsistent time compression |
| D07 | Cleared permissive/original anatomy baseline | Public repository distribution and engine compatibility must both be satisfied |
| D08 | Deterministic authored staff logic | Readiness, requests and completion stay tied to real simulated state |
| D09 | Descriptive multi-dimensional debrief | Avoids equating speed or a single score with surgical competence |
| D10 | Clinical and runtime validation are future gates | This research task cannot establish either by assertion |

## Material changes from the old drafts

- The current direct BodyParts3D archive license differs from the old page; acquisition provenance must identify which terms apply. ShareAlike anatomy is not assumed compatible with Unreal. See exact evidence in [asset research](docs/plan/research/03-assets-licensing.md).
- Pulse ECMO capability is not treated as a ready CABG/CPB implementation. Pump-supported arrest, reservoir behavior, protection and recovery need explicit experiments.
- Conflicting clinical teaching details are recorded; universal dosing tables and guessed surgical-time scoring thresholds are not adopted as executable rules.
- National complication percentages are not used as random player-failure odds. Every modeled event needs a defined causal scenario.
- OSATS, cognitive-training studies and haptic studies support different claims. None validates this game's automated score or transfer to surgery.
- The existing Python example is acknowledged as pre-existing demonstration code, correcting the old skeleton's statement that no code existed.

## Delivery path

**Case and cleared anatomy → tool/tissue and CPB feasibility → coupled anastomosis slice → clinical/usability review → complete-case alpha → reviewed desktop release.** Additional procedures, PC VR and haptics follow separate gates.

The initial estimate is **47–84 full-time working weeks before contingency**, or roughly **14–27 months including 25–40% contingency**, under the staffing/reviewer assumptions in the roadmap. A 3-month feasibility result, 6-month slice and 12-month alpha are scope guides, not guarantees. A solo part-time effort or substantial custom simulation research can take longer. Re-estimate after the first feasibility experiments.

The next implementation step, when requested, is to select one fictional case and target region, verify one anatomy sample's rights/geometry, package the engine fixture, and run tool/stitch and CPB experiments. No implementation or purchase is part of this planning task.

## Open inputs and limits

Target PC/GPU, available weekly hours, team skills, budget, reviewer access, preferred input devices and eventual distribution scope remain unknown. The plan uses reversible defaults and does not require an answer to finish planning. Before implementation commitments, these determine hardware targets, schedule and which tasks can be manual.

No downloaded meshes, licensed media package, clinical sign-off, performance benchmark, validated physiology extension or educational transfer study exists from this task. Those are measurable future deliverables. User instruction remains: **plan only, and upload each completed planning stage to the repository**.
