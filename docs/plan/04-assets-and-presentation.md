# Asset pipeline, anatomy, visuals, and audio

Revision: 2026-11-03. Detailed source evidence is in [assets research](research/03-assets-licensing.md), the [candidate register](ASSET_LICENSES.csv), and [realism research](research/05-visual-audio-realism.md). No third-party asset has been acquired, inspected in 3D, or approved for shipping.

## Baseline acquisition plan

Use direct BodyParts3D archive geometry under its updated CC BY 4.0 terms for thoracic context; evaluate a pinned HRA v1.2 heart; make the surgical target surfaces, coronary wall/lumen details and essential instrument geometry in Blender. Combining unrelated atlas donors requires deliberate registration and review, not automatic overlay. Use original procedural tissue materials and sound; optional cleared CC0/CC BY props can speed the background environment.

A usable asset must pass four different checks: rights, acquisition/version provenance, anatomical or functional suitability, and runtime performance. The candidate register establishes only the current research evidence. Blank acquisition/hash fields are intentional. Public GitHub asset upload is redistribution even for a personal project.

Z-Anatomy is excluded from the Unreal baseline because of its ShareAlike/engine compatibility issue. NIH entries with missing license fields remain blocked. Noncommercial alternatives stay separate from any future commercial package. Reference videos, device photographs and published diagrams are links for research, not downloadable game assets.

## Asset priority and acceptance

| Priority | Content | Acceptance requirement |
|---|---|---|
| P0 | One coronary target, conduit segment, needle, fine holder and forceps | Reviewable scale, lumen/wall, tips, grasp/puncture regions, contact mesh and stable IDs |
| P1 | Heart/great vessels/pericardium and exposed thorax | Correct orientation, attachments, exposure, landmark continuity and deformation ownership |
| P1 | CPB circuit, clamps, cannulas, suction and monitors | Connection topology and device state correspond to simulation; no decorative disconnected circuit |
| P2 | Access layers, saw/retractor, harvesting field, closure/drains | Each modeled phase has its declared interaction level and failure states |
| P2 | Patient/staff hands and nearby equipment | Credible grips, sterile field, occlusion, practical reach and collision |
| P3 | Whole OR, staff bodies, distant props, ambience | Context and performance without obscuring the operation |

## Blender-to-engine workflow

1. **Intake:** record original URL, creator, exact file/version, license evidence, credit, modification permissions and engine compatibility. Hash acquired files. Keep blocked sources out of build paths.
2. **Anatomy audit:** establish units/axes, chest/heart orientation, coronary connectivity, donor relationships and named landmarks. Document missing layers and surgical regions.
3. **Surgical topology:** create separate render, collision and solver meshes; author wall thickness/lumen and cut/attachment regions. Do not rely on globally decimated atlas surfaces for suturing.
4. **Deformation:** define ownership of baseline heartbeat, respiratory displacement, positioning and local contact. Attach vessels/fat/sutures consistently. Avoid double-deforming the same vertices.
5. **Materials:** separate myocardium, fat, pericardium, vessel wall, bone, muscle, skin, blood film/pools, cautery and cloth. Use state-driven masks and cleared texture inputs.
6. **Export:** pin names, axes, units, pivots, scale, LODs, contact IDs, material slots and animation settings. Validate one round trip before bulk conversion.
7. **Review:** inspect neutral lighting and surgical lighting, maximum retraction, exposed sections, normals, collision alignment, readability and performance. Save source/derived relationships and review outcome.

Future ledger fields also include local paths, evidence snapshots, exact credit text, changes, software/dependency license, clinical reviewer/build, technical reviewer/build, and release status. Produce credits from the same manifest used by packaging. Do not choose a project-wide content license that overrides upstream licenses.

## Visual/audio coherence

The operative field receives most of the detail budget. Stable lighting, fine-tool visibility, useful contrast, correct coronary routes and tissue response matter more than distant equipment. Use subsurface/wet-surface shading where appropriate; calibrate material appearance under both neutral and operating lights. More gloss or more blood alone does not establish realism.

Drive heart motion from mechanical state; keep ECG electrical phase separate. Include arrested, low-function and abnormal-motion states with reviewed transitions. Blood visuals derive from authoritative loss, pool and suction state; color/visibility settings cannot change physiology. Smoke/cautery and instrument sounds require matching device activation and contact state.

Monitor audio comes from the observation model, including signal quality and delays. Original alarm designs must not be advertised as IEC compliant without the relevant standard review and testing. Pump, suction and tool loops start/stop with actual equipment state. Dialogue reports actor-specific request, acknowledgment and completion. Captions identify speakers and meaningful device sounds.

Provide a stable surgeon view, deliberate camera orbit/reposition and a magnified task view. Avoid automatic dramatic camera movement during fine manipulation. Patient and team placement should preserve real spatial constraints while keeping the desktop task usable; assistance and camera privileges are declared in the task record.

## Reference and acceptance pack

For each slice, prepare an original annotated landmark diagram, material comparison sheet, tool-tip close-ups, supported deformation range, motion/monitor synchronization clips, sound-event matrix and license manifest. These are future deliverables, not artifacts already generated. Clinical reviewers judge anatomy and causal cues; art reviewers judge presentation; both record disagreements rather than replacing one review with the other.
