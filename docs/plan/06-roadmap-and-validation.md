# Delivery roadmap, acceptance gates, and risk ownership

Revision: 2026-11-03. Estimates are planning assumptions for an experienced full-time developer with intermittent art and clinical review support. No staffing, purchase, expert approval or release date is committed. See [production research](research/07-production-validation.md) for evidence and limitations.

## Milestones and critical path

The critical path is **reviewable case → cleared anatomy → usable interaction → coupled physiology → slice review → full-case coverage → release evidence**. Environment polish, additional procedures and VR must not consume the capacity needed to prove that path.

| Milestone | Effort assumption | Deliverables | Exit gate and fallback |
|---|---|---|---|
| M0: Planning handoff | This documentation task | Seven fresh research reports, integrated plan, candidates, decisions and gap review | Internal documentation review; no implementation implied |
| M1: Case and license baseline | 1–2 weeks | Fictional case, first target, protocol/source map, reviewer roster, initial cleared asset sample | Surgeon/perfusion/anesthesia review scheduled; rights sufficient for chosen engine. Otherwise remain experimental or choose another asset |
| M2: Feasibility | 6–10 weeks | Packaged engine fixture; tool/tissue/stitch experiment; Pulse CPB evaluation; measured performance; decision records | Prove bounded task and causal states. If Pulse fails, fund custom backend or narrow case; if input fails, reduce manual claims |
| M3: Vertical slice | 8–12 weeks after M2 | One graft task, supported circulation, one defect/recovery, team cues, replay/debrief, art sample | All slice gates below pass; no expansion merely because visuals look good |
| M4: Full-case alpha | 12–24 weeks after M3 | One complete workflow with declared assisted stages, closure/handoff, selected failures | Complete graph coverage, persistent state, no unmodeled critical transitions |
| M5: Reviewed beta | 12–20 weeks after M4 | Usability corrections, art/audio refinement, reviewed variants, packaging/credits, regression suite | Clinical-content, technical and license reviews resolved within declared scope |
| M6: Desktop release candidate | 8–16 weeks after M5 | Reproducible package, local save migration policy, settings, credits, known-limits document | No critical defects; measured target hardware and explicit release claims |

The sequential estimate totals **47–84 working weeks before contingency**, about 11–19 full-time calendar months. Add **25–40% contingency** for integration, rework and review availability: roughly 14–27 months under these assumptions. This reconciles the 3/6/12/24-month scope guide in the production report. Part-time work, custom CPB research, or a new tissue topology method can exceed this range. Re-estimate at M2 and M3 from actual progress.

## Initial backlog and dependencies

| ID | Work package | Depends on | Responsible role | Acceptance artifact |
|---|---|---|---|---|
| P01 | Author fictional anatomy/graft/protocol case | M0 | Clinical lead + designer | Annotated case and approved/unknown rules |
| P02 | Acquire one permitted anatomy sample and tools | P01 target | Technical artist | Hashes, licenses, geometry audit |
| P03 | Package selected engine with sample | P02 | Engine developer | Repeatable build and dependency manifest |
| P04 | Precision input and contact fixture | P03 | Interaction developer | Target/passage/traction traces and usability notes |
| P05 | Bounded incision/stitch/assisted knot | P04 | Interaction developer + surgeon reviewer | Success/defect/recovery fixture |
| P06 | Pulse CPB capability evaluation | P01 | Simulation developer + perfusion/anesthesia reviewers | Supported/unsupported matrix and physiology traces |
| P07 | One clock, events and coupled defect | P05 + P06 decision | Simulation developer | Conservation, synchronization and replay evidence |
| P08 | Team requests and monitor observation model | P07 | Gameplay developer | Requested/acknowledged/completed traces and artifact case |
| P09 | Slice materials/audio/camera | P02 + P07 | Technical artist + audio designer | State-coherent close-up review pack |
| P10 | Debrief and accessibility | P08 | Designer + UI developer | Evidence-based feedback and settings test |
| P11 | Independent content/usability review | P09 + P10 | Clinical reviewers + test lead | Findings with severity and retest disposition |
| P12 | Complete-case expansion | P11 gate passed | Team | Phase-by-phase fidelity register and regression scenarios |

One person may fill several roles, but cannot silently substitute their own approval for a promised independent clinical review. No reviewers have been contacted in this task.

## Slice acceptance matrix

All thresholds below are either objective software requirements or **proposed engineering criteria**. Biological/skill thresholds require preapproved scenario-specific evidence before implementation testing.

| Area | Required check | Pass evidence |
|---|---|---|
| Anatomy | Review named coronary routes, target/neighbor structures, layers, scale, lumen and instrument approach | All blocking anatomy findings resolved in recorded review |
| Workflow | Exercise every supported transition and at least one invalid/recovery path per critical transition | No unreachable required state, bypassed prerequisite, lost task or duplicate resource ownership |
| Contact/stitch | Replay defined normal and fast-motion/thin-wall fixtures | No unsupported attachment or unresolved tunnelling in those fixtures; supported limits documented |
| Volume/substances | Baseline, leak, prime, suction route and support transition | Accounting residual within fixture-specific tolerance; no unexplained mass creation |
| Physiology | Pump-supported arrest, drainage limitation, oxygenator change, recovery, artifact | Reviewed direction/time envelopes and explicit unsupported behavior |
| Time/replay | Pause, time compression, checkpoint/resume and same-build replay | Events and state agree within declared tolerances; observations retain delay |
| Presentation | Cross-check motion, ECG, pulse, pump, clamp, leak, suction and captions | No contradictory causal cues across the authored scenarios |
| Performance | Named hardware; 30-minute representative soak | Targets in [architecture](03-technical-architecture.md) met or transparently revised before scope freeze |
| Usability | Pilot target selection, needle passage and two-tool exposure across user experience levels | Recorded failure modes corrected; acceptable input thresholds established before comparative assessment |
| Rights | Audit every asset and dependency in package | No unknown/blocked item; required credits and licenses included |
| Claims | Compare marketing/help/debrief against actual supported behavior | No claimed clinical certification, arbitrary surgery, calibrated forces or transfer without evidence |

Pilot size and study power are different questions. Small iterative sessions can expose interface problems but cannot justify statistical claims of clinical learning or transfer. Design any later educational study for its actual outcome and review requirements.

## Cost and capacity model

No purchases are made or subscriptions activated. Free tools/assets do not imply free development. Before M1, create a budget using **planned hours × actual quoted rate**, plus workstation gaps, storage/build usage, content work, reviewer sessions and contingency. Record donated time as capacity rather than pretending it is guaranteed.

| Cost bucket | Default | Trigger for spending decision |
|---|---|---|
| Engine/editor and Blender | Use eligible no-upfront-cost route | Eligibility changes or necessary paid functionality |
| Anatomy/instruments | Cleared free base + original work | Retopology/details exceed available art time |
| Clinical review | Obtain actual availability/quotes | Mandatory before any “clinically reviewed” milestone |
| Compute/storage | Existing capable PC if verified; budgeted LFS/build use | Measured hardware or storage shortfall |
| VR/haptics | Zero in desktop baseline | Separate device/SDK feasibility decision |
| Audio/voice | Original procedural cues and temporary text/captions | Reviewed script ready for recorded voices |

Use actual quotes rather than fabricated medical consulting rates. If the budget is near zero, narrow scope and timeline; do not remove clinical review while retaining the same accuracy claim.

## Risk register

| Risk | Severity | Owner | Trigger / mitigation |
|---|---|---|---|
| Inaccurate anatomy or clinical rules | Critical | Clinical lead | Conflicting/missing evidence → block rule/claim until resolved |
| Tissue/stitch controls cannot represent task | High | Interaction lead | Failed M2 fixture → bounded assistance, narrower claims or alternate input |
| Pulse does not support surgical CPB | High | Simulation lead | Failed transition/circuit experiment → custom-model scope/cost decision |
| Asset/engine rights conflict | Critical | Asset lead | Unknown/incompatible terms → reject import; substitute or change engine |
| Coupled systems violate mass/time | Critical | Simulation lead | Conservation/replay failure → stop expansion and repair ownership |
| Reviewer access unavailable | High | Producer | Missed clinical gate → experimental status; no false sign-off |
| Schedule overwhelmed by full-case scope | High | Producer | Slice not passing → defer manual harvest/closure, VR and extra procedures |
| Performance requires expensive hardware | High | Engine lead | Measured budget fail → optimize active field/effects; publish narrower target |
| Scores measure game familiarity | High | Assessment lead | Pilot confounding → familiarization, descriptive feedback, no competence claims |
| Public repository includes restricted data | Critical | Asset lead | Missing provenance → quarantine outside build/repo and use cleared synthetic content |
| Unsupported solver state produces false clinical result | Critical | Simulation lead | Invalid state → checkpoint stop and model-failure label |
| Upload credentials fail | Delivery blocker | Repository owner/environment | Preserve local staged commits and package; restore authenticated write access |

## Definition of plan completion versus game completion

The plan is complete when research, coherent decisions, implementation work packages, evidence limits, measurable gates and remaining owner inputs are documented and internally checked. Upload is a separate delivery requirement and must be reported honestly if blocked.

The game is complete only after future implementation, validation and packaging gates pass for its declared scope. This documentation task cannot confer clinical validity, runtime performance, asset inspection or educational effectiveness.
