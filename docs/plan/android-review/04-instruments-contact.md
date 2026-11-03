# Android review — functional instruments and tissue contact

Reviewed 2026-11-03. Proposed behavior and acceptance tests for assets/animation; no surgical protocol, calibrated force model or Android prototype is delivered.

## Why geometry alone is insufficient

A believable tool needs correct dimensions, articulation, contact geometry and tissue response together. The operative tip should determine its behavior; touching a whole-tool bounding box is not sufficient for a needle, scissor blade or vessel clamp. A visually closed jaw must not leave its contact model open, and an active edge must not cut from a distant handle collider.

Jackson and Cavuşoğlu model curved-needle interaction through friction, compression and cutting contributions, with phantom-based experimental validation. Their work supports separating these mechanisms; its calibration is not a universal human-coronary parameter set. [Primary paper, PMID 24683499](https://pubmed.ncbi.nlm.nih.gov/24683499/).

A recent XPBD open-suturing simulator used VR and bimanual haptic hardware with a specific noncardiac task. It is relevant technical evidence, but neither its reported frame rates nor user judgments establish Android coronary-suture performance. [Westergaard et al., DOI 10.1016/j.cag.2025.104507](https://pubmed.ncbi.nlm.nih.gov/41403563/).

## Functional model catalogue

All rows below are proposed simulation contracts; dimensions and tissue parameters require selected-tool evidence and review.

| Tool family | Required kinematics/contact state | Observable response |
|---|---|---|
| Atraumatic forceps | Two jaw contact regions; grip/release; defined jaw opening and friction abstraction | Tissue follows the actual grip, can slip under supported conditions, and deforms locally |
| Needle holder | Jaw/hinge or spring action as appropriate to the chosen model; needle grasp transform; lock where present | Needle orientation follows the holder without teleporting to the desired trajectory |
| Curved needle | Tip, shaft curvature, entry/exit and swept path | Puncture, tissue passage and drag are distinct; off-curve displacement cannot be treated as identical to following the curve |
| Scissors | Paired blades, pivot and closing sweep | Only tissue in the supported blade intersection region changes topology |
| Scalpel | Oriented edge/contact, supported incision corridor | Persistent incision surface and collision changes, rather than a painted line alone |
| Vascular clamp | Articulated jaw placement and closed/locked state | Local compression plus explicit lumen/connection occlusion state |
| Retractor | Anchored contact/support surfaces and movement limits | Distributed displacement and preserved tissue attachments, not whole-heart translation |
| Suction | Tip aperture, contact/occlusion state and declared collection route | Pool reduction follows the active tip and available fluid; no fluid creation |
| Cannula/tubing | Insertion/attachment region, connection state, bend/kink abstraction | Geometry and connected-flow state remain consistent |
| Electrosurgery handpiece | Tip activation/contact, selected authored tissue-effect state | Localized effect and matching visual cue; no full thermal-injury prediction claim |

The same visible tool may have a detailed render mesh and simpler contact representation. Their transforms, articulation and supported contact envelope must be checked at every opening angle. Fine tip silhouettes must survive visual LOD changes and magnification.

## Touch and stylus interaction

Use a magnified operative view with an offset control zone so the finger does not cover the needle tip. Provide separate position, depth, roll/orientation and jaw controls; make the active control mode visible. Offer a stylus path where hardware supports it. Android exposes pressure, tilt, orientation and hover information, but availability/calibration vary. Screen pressure is not a calibrated surgical grip or tissue force. [Android stylus documentation](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features).

Pinch-to-zoom must not accidentally move an engaged tool. Track pointer IDs and cancel/reacquire cleanly when touch focus is lost. Background/resume and orientation changes preserve or safely suspend the task. Input prediction may smooth a cursor, but irreversible tissue/contact events must use authoritative accepted input and be reproducible.

True independent bimanual 6-DOF control is not supplied by a flat touchscreen. Prototype two modes: sequential tool switching with explicit assistant holding, and a two-control-zone mode. Record assistance, snapping, gain and auto-orientation. Compare usability before deciding which mode best preserves the task. Phone vibration is a cue, not actual tissue resistance.

## Local physics and topology

Animate the regional control surface first, resolve tool contact against that moving geometry, then map its contact correction to the render surface. Use swept/continuous collision tests for thin structures and fast tools, with bounded substeps as needed. Verify that a deforming collider is spatially synchronized with what the user sees. Disabling contact while the heart moves would fail the realism goal.

Start with a bounded local deformable patch and explicit anatomical attachments. XPBD is a candidate numerical method; it does not supply correct tissue properties automatically. [Original XPBD paper](https://matthias-research.github.io/pages/publications/XPBD.pdf). The MIT [PositionBasedDynamics library](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) is a code/reference candidate; selected dependencies, ARM64 build and Android integration are untested. No library adoption is implied by this review.

Keep cosmetic contact, elastic deformation, irreversible damage and connection state separate. For example, a clamp can indent a vessel and change its modeled lumen; these effects need consistent ownership. Wound surfaces, attachment IDs and future punctures must survive visual LOD or animation-state changes. Unsupported collisions or numerical failures are model faults, not automatic patient penalties.

Suturing begins with acquisition, orientation, bounded curved passage, tissue anchors, thread motion/tension abstraction and visible edge approximation. Use explicit assisted knot completion initially. Unrestricted knots require self-contact, friction, sliding/locking and reproducible retention tests; neither a knot-shaped mesh nor a closing animation proves this behavior. Preserve the original high-fidelity ambition through a measurable expansion path rather than silently describing assistance as free surgery.

## Acceptance tests

| Fixture | Required result |
|---|---|
| Jaw sweep and grip | Visible jaws and colliders agree; release does not leave a hidden attachment |
| Moving-heart contact | Tool remains on the same material region; no coronary sliding or rest-pose collision |
| Fast motion / thin vessel | No unsupported tunnelling within the declared input-speed envelope |
| Needle curvature | Same entry and path replay yields consistent anchors; no impossible straight-through teleport |
| Clamp placement | Compression/occlusion follows the actual selected structure, not the nearest label |
| Incision/LOD | Exposed surface, wound and contact topology persist after quality changes |
| Suture tension/release | Supported geometry responds consistently; assisted completion is recorded |
| Touch interruption | Pointer loss, UI gesture, background/resume and camera movement do not create unintended tissue actions |
| Warm-device repeat | Contact outcomes remain equivalent within declared numerical tolerances after thermal adaptation |

Set task-specific displacement/contact tolerances after device, tool dimensions and anatomical source resolution are established. A screen pixel error is not automatically a clinically acceptable millimeter error. This review establishes what must be measured, not invented precision claims.

Fresh research used primary needle-interaction and suturing papers, the XPBD author paper, the PBD maintainer repository and Android input documentation. Only publication abstracts were used for the cited biomedical studies; no complete reproduction or patient-tissue calibration was performed.
