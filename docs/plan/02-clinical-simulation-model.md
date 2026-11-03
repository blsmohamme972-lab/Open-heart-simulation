# Clinical state, procedure graph, and physiology design

Revision: 2026-11-03. Proposed software model, not instructions for performing surgery. Sources and uncertainty are detailed in [research 01](research/01-surgical-procedure.md) and [research 02](research/02-physiology-perfusion.md). No numerical clinical protocol is approved by this plan.

## Three models with one authoritative state

Keep the procedure task graph, physiological state, and physical anatomy distinct but coupled. Procedure completion follows verified state changes; it does not write an arbitrary healthy value into the patient. Likewise, an animated clamp must change the actual connection graph before physiology or monitors respond.

The task graph includes arrival/preparation, anesthesia/monitoring, team briefing, chest access, conduit preparation, exposure/target review, bypass readiness, circuit connection, supported circulation/protection, graft construction, recovery, separation, protocol-specific reversal/removal, closure, sign-out and ICU handover. The [research graph](research/01-surgical-procedure.md#proposed-complete-case-task-graph) records representative roles and equipment. Accepted sequences vary; the final case needs an explicit local/protocol variant.

## Proposed authoring schemas

| Record | Required fields |
|---|---|
| Case | ID/version; fictional patient parameters; anatomy version; coronary/graft map; chosen protocol; objectives; initial state; enabled complications; reviewer status |
| Task | ID; owner; prerequisites; permitted concurrency; equipment/resources; request/acknowledgment/completion events; completion observations; failure/recovery branches; assistance level |
| Structure | Persistent ID; anatomical name; coordinate system/scale; surface and collision meshes; layer; connectivity/lumen graph; contact/damage parameters; provenance |
| Instrument | ID; geometry; tip/jaw function; degrees of freedom; grasp/contact rules; sterile status; failure state; target tissues |
| Connection | Endpoints; open/clamped/connected state; resistance/leak abstraction; secured state; simulated air flag; source task |
| Parameter | Name; value or distribution; units; source and location; population/context; model mapping; uncertainty; reviewer; approval/version |
| Observation | Channel; true state source; sampling clock; delay/filter; unit; signal quality; last valid sample; artifact mode |
| Event | Ordered ID; simulation time; actor; action; affected structure; inputs; before/after state; observation evidence; assistance; cause parent; scenario/build versions |

All schemas are design contracts only; there is no executable data file or drug-dose configuration in this task.

## Coupled variables

The first circulation model should track compartment volumes/pressures, native heart contribution, circuit flow, reservoir balance, oxygen transport at an explicitly reduced level, temperature, rhythm/mechanical state, ventilation support, blood loss and replacement. Add myocardial-protection history and graft connectivity as scenario-specific subsystems. Anticoagulation/coagulation begin as reviewed coarse states with delayed observations, not claims of complete hemostatic physiology.

Evaluate Pulse first behind an adapter, using small analytical/reduced-model fixtures to check expected behavior. If Pulse cannot support the required CPB transitions, explicitly choose a funded custom reduced backend or narrow the scenario. Neither candidate is assumed to provide validated open-reservoir surgical CPB out of the box. The adapter must prove that ownership of blood volume, flows, oxygen transport, actions and time is unambiguous. Never run two independent authoritative circulation models and choose whichever vital sign looks better.

Illustrative engineering equations, to be reviewed for the selected model:

- Each compartment obeys `dV/dt = sum(inflow) - sum(outflow) + external sources - external sinks`.
- A resistance element may use `Q = (P_upstream - P_downstream) / R`; this is a lumped approximation, not universal vascular mechanics.
- For linear compliance, use `P = (V - V0) / C`; cardiac elastance requires time-varying chamber parameters and defined boundary conditions.
- Whole-system blood accounting includes patient, bypass reservoir/tubing, field loss, suction/cell-salvage abstractions, and administered volume. Display particles do not create or remove authoritative blood.

Record units at every interface. Validate conversions between liters/milliliters, seconds/minutes, pressure and temperature. Add physiologic complexity only when a case objective requires it and a calibration/validation method exists.

## State-to-observation examples

| Trigger | Authoritative change | Visible/audible consequences | Test obligation |
|---|---|---|---|
| Needle misses/tears modeled vessel margin | Attachment geometry, damage, local leak coefficient | Visible defect and leak when the modeled pressure difference supports it | Defect persists after camera changes/save/load |
| Suction collects field fluid | Field-to-suction transfer according to selected route | Smaller pool; tubing/collection response | No double-counted blood; route affects returned/lost volume |
| Venous drainage becomes inadequate | Circuit inflow/reservoir and cardiac loading change | Flow/pressure/reservoir cues, team notification | Support cannot continue indefinitely from an empty reservoir |
| Cross-clamp state changes | Relevant vascular connections change | Flow distribution and protection-dependent mechanical state | Clamp alone must not imply both complete arrest and adequate protection |
| Electrical rhythm changes | Electrical state; mechanical response follows separate modeled rules | ECG, mechanical motion, arterial waveform can diverge | No universal beat-per-ECG animation |
| Pulse sensor has poor signal during support | Observation quality changes | Pleth/SpO2/tone use the selected sensor policy | Sensor artifact must not change actual oxygen transport |
| Assistance snaps a needle trajectory | Input trajectory constrained and logged | Visible assistance indicator; outcome still evaluated | Debrief and comparisons use the correct assistance category |

Some effects in this table require further clinical review; the purpose is to prevent disconnected systems, not assert the exact magnitude or timing of real responses.

## Team and workflow behavior

Use deterministic task/state logic for staff. A command can be requested, acknowledged, delayed, refused with a reason, or completed. Only completion changes the relevant state. Equipment and actor resources are reserved to prevent one assistant performing two physical tasks at once. The player can inspect outstanding requests.

Recovery paths must preserve history: return to support rechecks prerequisites; repair does not erase prior damage; counting a missing object remains unresolved until the inventory is reconciled. Avoid real-time generative clinical advice. Optional narrative variation must never alter clinical rules.

## Time, uncertainty, and model failure

Use one authoritative simulation clock with recorded task timestamps. Maintain separate exposure counters and wall-clock playtime. Pausing a teaching session freezes every relevant solver and actor; fast-forward advances all coupled subsystems consistently and is unavailable during unsupported interaction states. Planned sample delays remain expressed in simulation time.

For unsupported input or solver instability, stop at the last valid checkpoint, flag the model failure, and exclude the segment from assessment. Do not silently clamp a wildly wrong state back to normal. Carefully bounded numerical protection is allowed only when logged and justified.

Do not assign population mortality probabilities to random game failures. A selected scenario may include initial uncertainty, but its mechanism, seed, and limits are recorded. No postoperative risk estimate is presented as a real patient prediction.

## Minimum physiology verification suite for future implementation

1. Closed-circuit baseline: stable state and conserved accounted volume over declared duration.
2. Known transfer/bleed: integrated loss equals compartment changes within specified tolerance.
3. Pump-only support: correct ownership of systemic flow when mechanical heart activity is absent.
4. Pump/drainage restriction: monotonic, explainable responses without invented volume.
5. Clamp/protection combinations: independent effects and defined unsupported states.
6. Rhythm/sensor separation: electrical activity, mechanical output, and measured pulse can differ.
7. Leak/repair: pressure-dependent modeled loss and retained event history.
8. Step-size sensitivity: outputs remain within agreed envelopes when the solver step is reduced.
9. Save/load/replay: state and observables reproduce within declared build/hardware tolerances.
10. Boundary/fault tests: invalid units, negative volume, missing sample, adapter disconnect, and recovery branch.

Clinical envelopes and numeric tolerances must be approved in the future fixture set. Passing software invariants is necessary but does not validate biological fidelity.
