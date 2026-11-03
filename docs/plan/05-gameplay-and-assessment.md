# Gameplay, controls, team behavior, and assessment

> **Historical desktop baseline:** the owner's current platform is Android. For animation, assets, rendering and tool interaction, use [OHS-PROPOSAL-002](../proposals/OHS-PROPOSAL-002-ANDROID-REALISM.md). The content below preserves the earlier plan; unrelated clinical/production assumptions are not newly validated by the Android review.

Revision: 2026-11-03. Design proposal grounded in [gameplay research](research/06-game-design-assessment.md); medical and motor-skill effectiveness remain unvalidated.

## Play loop

Inspect the fictional case and operative field, choose the next task, prepare tools/team, manipulate tissue, observe the result, reassess, and review the attempt. A useful game challenge is understanding and managing the consequences of actions within the modeled case. Difficulty changes assistance, information and case complexity; it never secretly changes anatomy or physiological rules.

| Mode | Player experience | Feedback |
|---|---|---|
| Orientation | Explore anatomy, identify structures and learn instruments/camera | Labels, demonstrations and no competence rating |
| Guided task | Follow one bounded interaction with reasons for prerequisites | Hints, trajectory support, pause and explicit assistance |
| Practice | Repeat the task under consistent conditions | Adjustable assistance and optional delayed feedback |
| Integrated case | Follow the complete reviewed task graph with ongoing team activity | Persistent consequences, save/pause and end-case debrief |
| Focused scenario | Investigate one supported complication | Evidence-based causal replay and a targeted repeat exercise |

The first slice opens with a prepared operative field and established simulated support. The player practices one graft attachment, inspects a modeled defect, corrects it if the scenario allows, and receives a debrief. That slice does not claim to simulate the entire operation.

## Controls to prototype

Use mouse motion in an explicit task plane, dedicated depth adjustment, a separate orientation/roll mode, remappable jaw control, and adjustable precision gain. Provide explicit active-hand switching; the other instrument can hold a reviewed constraint through assistant support. Camera controls must not accidentally manipulate tools. A magnified view improves visibility without changing anatomical scale.

Needle passage initially follows bounded curved trajectories with observable entry/exit choices. Knot completion is assisted and labeled. Record snapping, damping, auto-orientation, holding assistance, input device and precision gain. Scores from different assistance/device profiles are not equivalent.

Prototype target acquisition, curved passage and exposure-plus-manipulation before polishing menus. Measure unintended contact, positioning error, mode-switch mistakes, completion and comfort. Pilot sessions establish reasonable tolerances; no unsupported millimeter precision claim is made from a mouse or optical hand tracker.

## Team and UI

The surgeon can direct the assistant, request an instrument, ask for anesthesia/perfusion status, and request an allowed transition. Task states are visible: requested, acknowledged, active, complete or unable. Staff continue authored responsibilities; actions take simulation time and require resources. A confirmation is not proof that a physical event occurred.

Show critical patient observations, instrument state and pending communication without covering the coronary target. Detailed laboratory/circuit information opens on demand with source/sample time. An invalid or stale reading must be identifiable. Team notifications identify the observation or failed prerequisite rather than inventing a hidden diagnosis.

Keep free-form generative medical decisions out of the initial runtime. Optional speech input may map to the same deterministic commands after an ambiguity check. No network service is required for core play.

## Consequences and debrief

Record action, actor, structure, contact, state change, available observation, assistance and cause. A leak or obstructed graft must follow the modeled geometry/connection, not a random health deduction. The tutorial can block unsupported actions; case mode can allow modeled errors and explain their consequences. Interface faults and unsupported model states are reported separately from player errors.

Debrief uses separate dimensions: procedural completeness, tissue handling, modeled connection quality, use of observations, team coordination and efficiency. Show evidence clips and timelines. Do not average a severe unresolved defect away with speed points, reproduce a copyrighted assessment form without clearance, or call an automated metric “validated OSATS.” Before reviewed thresholds exist, use descriptive feedback rather than clinical pass/fail.

A short debrief asks what the player noticed, presents synchronized operative/monitor events, explains the modeled causal chain and offers one repeat exercise. This is inspired by educational debrief research, not a replacement for an expert facilitator. Counterfactual replay is another simulated run, not a real-patient prediction.

## Accessibility and content choices

Provide remapping, left-handed layouts, hold/toggle alternatives, scalable UI, color-independent cues, captions, separate sound levels, camera-motion options and reduced graphic intensity. Preserve important cues when reducing blood/smoke; supply an equivalent cue if required. Keep accessibility controls distinct from clinical hints and record assistance where comparisons depend on it.

Local saves retain task queues, tools, physiology, delayed observations, event history, content/model versions and random state. Practice rewind starts a separate attempt. Time compression is allowed only in supported stable periods and advances every subsystem consistently.

## Assessment boundary

Clinical reviewers must inspect the task, source rules, feedback and omissions. User sessions must separate familiarity with game controls from clinical experience. Reliability, learning, retention and transfer require different evidence and later study designs. This game receives no medical certification or skill credential from completing this plan.
