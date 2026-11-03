# Android review — heart motion and contact geometry

Reviewed 2026-11-03. This is an animation specification and evidence review, not a completed rig or clinically validated model. The earlier “heartbeat blend shapes” recommendation was too broad for the requested fidelity.

## Evidence and its limits

Codreanu et al. used CMR tissue phase mapping in 14 healthy young men and described regional longitudinal and rotational movement, including distinct basal and apical behavior. This supports a regional motion model; it does not provide universal animation amplitudes for exposed, supported or diseased hearts. Viewing direction matters when describing rotation. [Primary study, PMID 20716369](https://pubmed.ncbi.nlm.nih.gov/20716369/).

Regional CMR tagging research also distinguishes torsion between different ventricular levels. Its full PMC page was blocked by a browser check in this review; the publication record/search evidence is not treated as full-text inspection. [PMID 18505572](https://pubmed.ncbi.nlm.nih.gov/18505572/). Do not borrow a single “normal twist angle” and apply it to every chamber and patient.

The [Sunnybrook source](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) offers cine-MRI and LV reference information under CC0; its download routes still need validation. The [versioned coronary-motion dataset](https://zenodo.org/records/10203116) provides discrete LCA surface phases under CC BY 4.0. These are complementary references, not a complete animated surgical heart. Dataset rights and the paper's rights are separate.

## Required motion channels — proposed design

| Channel | What must be represented | Wrong shortcut to detect |
|---|---|---|
| Regional ventricular deformation | Longitudinal shortening, circumferential change, wall thickening, rotation/untwisting with source-specific timing | Scaling the whole heart up and down like a balloon |
| Chamber differences | RV, LV and atria have their own geometry and timing constraints | Copying LV movement unchanged to every structure |
| Attachments and base motion | Great-vessel/pericardial constraints appropriate to the authored exposure | Floating heart or rigidly frozen base without evidence |
| Loading/support state | Different shape/motion states for loaded, unloaded and supported conditions | Normal full contraction after merely changing the ECG texture |
| Respiratory/whole-organ movement | Separately controlled displacement and tissue relationships | Adding identical large translation to every layer |
| Surgical positioning | Reorientation and support constrained by attachment anatomy | Teleporting the organ while coronaries/tools stay behind |
| Local contact | Indentation, grip, traction, release and persistent injury where modeled | Instrument entering the visible surface before the collider responds |

These are authoring requirements. Each channel's amplitude, phase, boundary conditions and supported state need measurement or reviewer approval. A sinus rhythm animation must not be reused as fibrillation with only increased playback speed. An arrested heart has no active contraction in that state, but can still deform under loading or contact. Return to beating is a reviewed transition, not an instant reset to a perfect normal loop.

Electrical activation, mechanical phase and output are separate input fields. The current scope only defines the animation interface; it does not implement the complete physiology backend. Required inputs include mechanical state, normalized cycle phase, state-specific loading envelope, respiratory phase, attachment/positioning state and active contacts. Unsupported combinations must be identifiable.

## Hybrid animation architecture

Use an offline, reviewed deformation reference to fit a compact deformation basis or rig. At runtime evaluate that basis on a low-resolution anatomical control cage. Add local contact corrections around the operative region, then map both render and collision representations from the same authoritative deformed surface. This is a proposed cost/quality compromise for Android, not a promise that any reduced model reproduces real tissue forces.

The heart cannot be animated only in a GPU vertex shader while CPU tools collide with its rest pose. Avoid synchronous full-mesh GPU readback. Prefer CPU evaluation of the compact control cage plus GPU interpolation of visual vertices; measure the mapping error at the tool tip. Use one deformation order and ownership map, with local constraints expressed relative to the current moving tissue configuration.

Coronaries, fat, sutures and landmarks bind to material coordinates or stable region mappings. They must not slide independently across the epicardium. Topology edits require explicit updated mappings and exposed wall/lumen geometry. Distinguish approximately conserved tissue material volume from changing chamber/cavity volumes; conserving the heart's entire outer enclosed volume is not a universal heartbeat rule.

| Representation | Appropriate role | Main risk / gate |
|---|---|---|
| Skeletal rig plus corrective shapes | Compact global motion and state transitions | Bone artifacts, volume loss and incorrect regional mechanics; compare against reference motion |
| Reduced control-cage/deformation basis | Shared animation/contact geometry | Basis may fail outside fitted states; bound and test the allowed envelope |
| Full morph-target sequence | Offline comparison or small fixed-topology region | Memory/bandwidth and correspondence requirements; sample count is not a medical accuracy measure |
| Vertex animation texture | Background/noninteractive playback experiments | Collision synchronization, quantization and topology changes; not baseline for surgical contact |
| Full volumetric FEM | Offline reference or carefully bounded future experiment | Constitutive/boundary-data and performance burden; not assumed feasible for whole-heart Android runtime |

Blender shape keys store positions for existing vertices; matching topology and correspondence matter. Direct manual retrieval failed during this run, so the official indexed workflow text is used only for this basic authoring constraint. [Blender workflow](https://docs.blender.org/manual/en/latest/animation/shape_keys/workflow.html). Godot's import path needs a real round-trip test for the chosen rig, shapes and metadata. [Godot 3D import](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html).

## Concrete sample inspection

Two CC BY 4.0 coronary STL phases, 10% and 50%, were downloaded to temporary workspace storage outside the repository. Both have **39,368 triangles**, **19,740 exact-coordinate unique positions** and **118 boundary edges**, with no edge having more than two incident triangles under that deduplication method. File hashes and native-coordinate bounds are in [the inspection record](motion-sample-inspection.json).

Crucially, their first-occurrence-indexed triangle connectivity hashes differ. Equal vertex/triangle counts therefore do **not** establish a valid direct morph pairing. This may be ordering/serialization rather than different anatomical topology; correspondence must be recovered and checked before interpolation. STL also supplies no unit declaration. The mesh name “walls” does not prove a modeled wall thickness or two-sided lumen tissue suitable for suturing.

This was a binary geometry/metadata inspection only: no rendering, registration, tissue mechanics or clinical acceptance was performed. The downloaded binaries are not committed.

## Acceptance fixtures

1. **Motion replay:** compare held-out landmark trajectories, regional phase, silhouette and cavity changes against the selected source. Report units, error distribution, segmentation uncertainty and reviewer disagreement.
2. **Cycle continuity:** inspect slow motion and normal playback around the loop boundary; no position/velocity pop or visible coronary slip.
3. **State transitions:** loaded/unloaded, beating/arrested and recovery transitions preserve attachments and local contacts without hidden resets.
4. **Tool synchronization:** maintain contact on the animated tissue at several phases, orientations and frame rates; measure surface-to-collider deviation at the tip.
5. **Retraction and release:** baseline movement and local contact do not double-deform tissue; residual damage remains separate from elastic recovery.
6. **Topology/LOD:** no inverted local elements, unintended self-intersection, closing lumen, missing needle anchor or reappearing wound after a supported transition.
7. **Warm Android replay:** repeat the identical contact/motion trace after thermal soak; lowering visual quality must not alter anatomical IDs or event results.

Clinical error tolerances and motion envelopes are **not yet approved**. Set them before acceptance from source uncertainty and task requirements. Avoid claiming accuracy from smoothness, frame rate or a visually convincing loop alone.

Searches covered CMR regional twist/longitudinal motion, coronary 4D CT surfaces, CAP cine-MRI, Blender shape topology and Godot import. Relevant primary pages were opened; blocked sources and the limited actual geometry inspection are distinguished above.
