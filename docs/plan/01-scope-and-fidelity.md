# Scope, intended experience, and fidelity contract

Planning revision: 2026-11-03. These are proposed product decisions. Research evidence is in [surgical workflow](research/01-surgical-procedure.md), [game design](research/06-game-design-assessment.md), and [production](research/07-production-validation.md).

## Product definition

Create a serious, visually convincing single-player open-heart surgery game for an adult audience interested in anatomy and procedural reasoning. The player acts primarily as the surgeon with a simulated assistant, scrub/circulating staff, cardiac anesthesiologist, and perfusionist. Outcomes should follow modeled actions, anatomy, support conditions, and case parameters. The game is not a patient-specific predictor or a credentialing tool.

The first complete case is an **adult elective on-pump CABG through median sternotomy**. A fictional reviewed graft map should include LIMA–LAD and one additional conduit/target only if that case rationale is clinically defensible. Graft count and conduit choice are case data, not universal surgical rules. The first playable vertical slice is much smaller: **one distal anastomosis on an exposed, arrested heart with simulated bypass support, an observable defect/recovery path, and a debrief**.

No game is implemented by this planning task. Existing Python example code remains unchanged.

## Defaults and unresolved owner inputs

| Decision | Planning default | When to revisit |
|---|---|---|
| Platform | Windows desktop first; keyboard and mouse | Before engine/hardware benchmark |
| Intended use | Personal, noncommercial educational game | Before public distribution or changing claims |
| Connectivity | Offline core; local saves and debrief | Only if collaboration is later requested |
| Engine candidate | Unreal, contingent on performance and license gates | End of feasibility phase |
| Artwork | Blender; item-cleared permissive anatomy plus original surgical detail | Before importing each source asset |
| Team | Small team or experienced solo developer with specialist review access | Before committing dates/budget |
| Languages | Externalized UI text; English clinical terminology first | Before recording dialogue; add Arabic if desired |
| PC VR / haptics | Optional later tracks, never required to play desktop | After desktop slice is usable and measured |

Hardware, budget, weekly availability, and clinical contacts were not supplied. The plan does not assume the user owns a powerful GPU, VR headset, haptic device, or paid software.

## What “as close as possible to real” means here

Each fidelity dimension has a separate review. A visual pass cannot excuse a failed physiological or workflow review.

| Dimension | Required observable behavior | Evidence needed before claiming fidelity |
|---|---|---|
| Anatomy | Correct orientation, layers, vessel continuity, surgical landmarks and scale | Annotated source provenance and specialist geometry review |
| Workflow | Valid dependencies, parallel tasks, team ownership and recovery paths | Versioned case protocol and multidisciplinary review |
| Interaction | Tool tips contact tissue; damage and constraints persist; authored assistance is visible | Contact/stitch scenarios and usability observations |
| Physiology | Support, bleeding, rhythm, ventilation and protection cause coherent state changes | Conservation checks, sensitivity traces, clinical review of selected cases |
| Appearance/audio | Tissue motion, field visibility, equipment, monitor signals and sounds agree | Recorded scenario review, material/landmark checks |
| Human factors | Readable field, useful cameras, stable input, interpretable feedback | User sessions across gaming/clinical experience levels |
| Assessment | Feedback cites actual events and separates assistance from performance | Reviewed rubric; later studies for educational claims |

Fidelity levels are recorded per task: **manual modeled**, **constrained modeled**, **team-operated modeled**, **authored presentation**, or **omitted**. Never label an assisted animation as free manual surgery. A learning mode can expose hidden states; case mode displays clinically plausible observations with their modeled delay and uncertainty.

## Scope ladder

| Tier | Included | Exit condition |
|---|---|---|
| Feasibility | One reviewed vessel patch, needle/forceps interaction, local tissue response, circulation/CPB toy cases, license evidence | Hard risks are measured; chosen stack supports the slice |
| Vertical slice | One graft attachment task, bounded needle/stitch handling, supported circulation, controlled defect/leak, team cues, save/replay/debrief | Interaction and causal feedback meet [validation gates](06-roadmap-and-validation.md) |
| Full-case alpha | Arrival to handover, including exposure, conduit work, bypass/protection, grafting, recovery, closure and counts | Every phase has declared fidelity; no dead-end workflow or disappearing injuries |
| Desktop v1 | One polished reviewed case plus focused practice modules and a small failure library | Reproducible build, rights-cleared assets, performance, usability and content review |
| Later | Additional patient/coronary variation, valve surgery, richer harvest/closure, optional PC VR and force feedback | New scope has separate content, interaction, licensing and validation gates |

Initial full-case alpha may use team-operated or authored stages for conduit harvest, anesthesia induction, and portions of closure. Their physical consequences and team dependencies still exist. A debrief labels these stages. Expanding them to manual tasks is subsequent work, not an undisclosed shortcut.

Explicitly deferred: unrestricted cutting anywhere, arbitrary tissue tearing, clinically calibrated knot mechanics, complete coagulation/drug pharmacology, patient CT import, live medical devices, competitive speed leaderboards, multiplayer, standalone mobile/Quest, and autonomous language-model medical reasoning. These can only return through a scoped design change.

## Success and stopping rules

The slice succeeds when a player can complete a bounded surgical task, observe why a deliberate error changes the connection or patient state, recover through an allowed path, and understand a truthful debrief. It fails if progression depends on arbitrary clicks, anatomy looks convincing but has wrong topology, assistance is hidden, or physiology is a disconnected HUD animation.

If fine needle control remains unusable after the defined interaction spike, ship a clearly constrained procedural experience and narrow the skill claims. If anatomical/clinical review is unavailable, retain an experimental status. If a required content license conflicts with the engine, replace the asset or change the stack before production. Scope reduction must be documented rather than hidden behind better graphics.
