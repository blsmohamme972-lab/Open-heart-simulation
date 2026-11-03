# Research 03 — Assets, provenance and Blender production

Research refreshed **2026-11-03**. Planning only: no third-party binaries were acquired or added to this repository. License statements were checked against publisher pages or public item APIs; suitability for surgery remains unvalidated. The [candidate register](../ASSET_LICENSES.csv) records candidates, not installed assets.

## Recommendation and corrections

Use **directly acquired BodyParts3D archive geometry, a pinned HRA heart, original Blender instruments and tissue surfaces, CC0 room materials, and original procedural audio** as the baseline. Spend the art budget on the open chest, coronary target and instrument tips. An anatomical atlas supplies starting shapes, not interactive surgical models.

Four corrections materially change the earlier report:

1. **BodyParts3D is now CC BY 4.0 at the official archive.** Its license page records a 2025-02-27 update; the old lifesciencedb page still displays BY-SA 2.1 Japan. Acquire through the archive page linking the new license and retain that provenance. Do not silently relicense a Z-Anatomy derivative. [Current license](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [update history](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/update.html), [older license page](https://lifesciencedb.jp/bp3d/info/license/index.html).
2. **Keeping a ShareAlike mesh in a separate file does not establish Unreal compatibility.** Epic's EULA §6(c) expressly lists CC BY-SA among non-compatible licenses. Z-Anatomy is therefore blocked from the proposed Unreal runtime unless separately licensed or the engine decision changes. [Unreal EULA](https://www.unrealengine.com/eula/unreal).
3. **HRA v1.3 was previously recommended while its exact license was uncertain.** This refresh pins the independently traceable **v1.2 library** for assessment. A newer organ requires its release metadata and geometry inspection, not an automatic upgrade. [Official library and license](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html).
4. The earlier inventory mixed license checks with unverified geometry claims and marketplace descriptions. This shortlist separates **license evidence**, **downloadability**, **anatomical acceptance** and **shipping approval**. No candidate currently passes all four because this is planning only.

## Anatomy shortlist

| Candidate and creator | License evidence; adaptation/public repository rights | Intended use and gate |
|---|---|---|
| **BodyParts3D release 4.0**, Kousaku Okubo / Database Center for Life Science; [downloads](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html) | [CC BY 4.0](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html). Personal/commercial adaptation and redistribution permitted with credit and changes recorded. Downloads include `isa_BP3D_4.0_obj_99.zip` and `partof_BP3D_4.0_obj_99.zip`. | Preferred thorax, skeleton and vessel context. Record organ IDs, release, hashes and source license; reconcile old package notices before import. Atlas reduction level is not surgical quality. |
| **HRA / HuBMAP Heart, Male, library v1.2**, Browne, Schlehlein and library collaborators; [exact GLB](https://github.com/hubmapconsortium/ccf-releases/blob/main/v1.2/models/VH_M_Heart.glb) | [Library CC BY 4.0 and citation](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html). Adaptation/public redistribution allowed with attribution and change notices. | Preferred heart candidate. Inspect exterior, chambers, great vessels and coronaries. Do not reuse prior v1.3 mesh counts as facts about this file. Cadaver-derived geometry does not establish living-heart motion. |
| **HRA Heart, Female, library v1.2**, same library; [exact GLB](https://github.com/hubmapconsortium/ccf-releases/blob/main/v1.2/models/VH_F_Heart.glb) | Same verified library license. | Later diversity candidate after coherent thorax registration; unrelated donors must not become an anatomically inconsistent composite. |
| **Z-Anatomy**, Gauthier Kervyn and collaborators; [repository](https://github.com/Z-Anatomy/Models-of-human-anatomy) | CC BY-SA 4.0 stated, with included NC/NC-SA exceptions. Compliant adaptations permitted by source terms; **blocked in Unreal baseline**. | Offline reference or alternative-engine route. Inspect individual provenance; inner-ear and kidney exceptions prevent uniform labeling of whole-atlas exports. |
| **NIH 3D Heart, Male, 3DPX-021000**, HRA; [entry](https://3d.nih.gov/entries/3DPX-021000) | Readable entry showed an empty Licensing field. **NIH-entry license UNVERIFIED**; acquire through verified HRA source instead. | Discovery/provenance cross-check, not independently cleared for inclusion. |
| **NIH 3D Human Heart 3d Model, 3DPX-022787**, Sourav Pan / Biology Notes Online; [entry](https://3d.nih.gov/entries/3DPX-022787) | Prior report claimed CC0; current readable entry did not expose the license. **UNVERIFIED; blocked pending metadata.** | Illustration candidate, not automatically patient-derived or suitable for surgery. |
| **TotalSegmentator v2.0.1 dataset**, Jakob Wasserthal / University Hospital Basel; [record](https://zenodo.org/records/10047292) | CC BY 4.0 verified in [record API](https://zenodo.org/api/records/10047292). Compliant data/mesh adaptation and redistribution permitted. | Optional thorax reference. Its 1,228 CT images / 117 structures do not constitute a complete coronary surgical dataset. Select and inspect one adult case. |
| **TotalSegmentator v3.0.0 dataset**, same creator; [record](https://zenodo.org/records/22688904) | CC BY 4.0 verified in [record API](https://zenodo.org/api/records/22688904). | Newer alternative published 2026-09-10: 1,939 images / 117 structures, including pediatric cases. Pin release and case selection. |

NIH hosts contributor-selected licenses; federal hosting does not put every entry in the public domain. Users must independently verify conclusions from models. [NIH terms §4.3 and §5](https://3d.nih.gov/terms).

**Other sources:** [Visible Human](https://www.nlm.nih.gov/research/visible/getting_data.html) is available under linked [NLM terms](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html), requiring acknowledgement and version/currentness disclosure. It is a segmentation/reference route, not a ready surgical asset. [Open Anatomy](https://www.openanatomy.org/) lists six atlases mainly covering other regions; this search did not establish a suitable adult CABG heart asset and license. Embodi3D and additional Sketchfab hearts remain **UNVERIFIED** until individually selected. [MM-WHS](https://zmiclab.github.io/zxh/0/mmwhs/) requires recipients not to disseminate data to third parties: exclude it from the public pipeline without permission explicitly covering intended derivatives.

Dataset, segmentation software and model weights have separate terms. A dataset's CC BY license does not clear every inference tool or specialized weight set. Do not assume restricted outputs become unrestricted by converting them to meshes.

## Instruments, operating room and materials

The following Sketchfab items were rechecked through their public `/v3/models/{id}` APIs on the research date. All four returned `isDownloadable: true` and the listed license URL. Descriptions such as “realistic” were not accepted as clinical validation.

| Exact candidate | Creator; verified terms | Plan |
|---|---|---|
| [Surgical instruments](https://sketchfab.com/3d-models/surgical-instruments-bd0ad0180f5148f1b3b331b8ebe6e494) | Wenschel; [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); [evidence](https://api.sketchfab.com/v3/models/bd0ad0180f5148f1b3b331b8ebe6e494) | Generic set candidate. Credit/change notices required; public source redistribution permitted. Inspect instrument identities, jaw geometry, proportions and pivots. |
| [Heartlung Machine](https://sketchfab.com/3d-models/heartlung-machine-34f7d192bd8d4ca498b5e3d4948101ba) | Kevin Gille; CC BY 4.0; [evidence](https://api.sketchfab.com/v3/models/34f7d192bd8d4ca498b5e3d4948101ba) | Blockout only. Author describes a short modeling test, not validated circuit design. Rebuild and validate connections/screens. |
| [Realistic Medical Equipment and Accessories Set](https://sketchfab.com/3d-models/realistic-medical-equipment-and-accessories-set-5460fb2767c6468eb88466d2555d273b) | daonware; CC BY 4.0; [evidence](https://api.sketchfab.com/v3/models/5460fb2767c6468eb88466d2555d273b) | Candidate table/lights/furniture. Verify scale, articulation and field clearance; remove unlicensed marks. |
| [Surgical Instruments collection](https://sketchfab.com/3d-models/surgical-instruments-collection-46f5799ca36240efae3abec6e61d4c8a) | Digital Surgery; [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); [evidence and requested credit](https://api.sketchfab.com/v3/models/46f5799ca36240efae3abec6e61d4c8a) | Noncommercial alternative. Public redistribution allowed under NC conditions, with requested attribution. Exclude from later commercial packaging unless relicensed. |
| [Surgery HDRI](https://polyhaven.com/a/surgery) | Oliksiy Yakovlyev / Poly Haven; [CC0 1.0](https://polyhaven.com/license) | Reflections/lighting reference, not a geometric OR or sterile layout. Attribution optional; public source redistribution permitted. |
| [Metal032](https://ambientcg.com/view?id=Metal032) | ambientCG; [CC0 1.0](https://docs.ambientcg.com/license/) | Background metal starting material; calibrate instrument roughness separately. Public files/derivatives permitted without attribution requirement. |

**Original art backlog:** sternal saw/retractor, vascular clamps, needle holders, atraumatic forceps, curved needles, coronary scissors, cannulas, tubing/connectors, suction, internal paddles, pacing wires, drains, sutures and tissue cross-sections. These are planned originals, not acquired assets or proof that suitable models do not exist.

Model from measured functional geometry, multiple lawful references and clinician review. Do not trace a restricted model and label the result original. Avoid copying logos, proprietary screen art or product photography. Blender's software license does not impose GPL on original output; imported content retains its conditions. [Blender FAQ](https://www.blender.org/support/faq/).

## Audio and people

Prefer original event-driven monitor pulses, pump loops and tool sounds so rate, pitch, starts/stops and alarms follow simulation state. Record authorship and project license when created.

Two specific alternatives are [Monitor hotler](https://freesound.org/people/iluminati_2705/sounds/536706/) by iluminati_2705 and [Hospital waiting room](https://freesound.org/people/bassboybg/sounds/201638/) by bassboybg. Both item pages specify **CC0 1.0**, permitting derivatives/public redistribution without mandatory credit. Neither was auditioned. Waiting-room audio is not OR ambience and may contain voices: exclude it from the baseline pending listening/privacy review. Fixed monitor audio is a timbre reference or placeholder, not the final physiological heartbeat source. Freesound terms are per item, not library-wide. [Freesound FAQ](https://freesound.org/help/faq/#licenses).

Use **MPFB core body/rig/skin assets** for patient and staff placeholders. The [official license](https://github.com/makehumancommunity/mpfb2/blob/master/LICENSE.md) separates GPL-3.0-or-later software from **CC0 1.0 bundled graphical assets and output**. Third-party clothing needs separate records. Hands, gloves, gown cuffs, instrument grips and bimanual task animation require correction; a generic rig does not establish surgical handling.

[Mixamo's FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) permits royalty-free project use, but does not establish raw-animation redistribution permission. Exclude it from the public-source baseline pending full terms review. MetaHuman and Character Creator are optional later candidates, **UNVERIFIED for this pipeline**, not necessary dependencies.

## Proposed Blender pipeline

1. **Intake:** record item/version, creator, license evidence, acquisition date and file hash. Separate source, working derivative and engine export. Keep unresolved/restricted content outside the repository and build manifest.
2. **Anatomy audit:** establish scale/orientation with named landmarks. Map coronary branches, conduits, great vessels, pericardium and chest layers to scenario structures. Have a clinician review spatial relationships and the target site before texturing.
3. **Interaction topology:** separate exterior, cut surface, vessel lumen and collision/solver meshes. Add local topology at incision, cannulation and suture regions. Preserve wall thickness, continuity and attachment metadata. Global decimation alone cannot produce this.
4. **Rig:** distinguish heartbeat, respiration, tool displacement and whole-heart positioning. Prevent double deformation when a solver takes ownership. Bind coronaries, fat and sutures to the same moving surface; keep stable anatomical IDs across LODs.
5. **Materials:** author wetness, fat, blood and cautery states procedurally; bake only from cleared sources. Review tissue color under neutral and surgical lighting. Cross-sections and blood pools need state-dependent geometry/materials.
6. **Export:** pin units, axes, naming, collision conventions and animation ownership in an engine-compatible preset. Test one round trip before mass export. Keep source `.blend` and export hashes traceable.
7. **Acceptance:** inspect scale, normals, intersections, maximum retraction, collision alignment, exposed lumen, tool-tip visibility, render cost and credits. Record clinical and visual approval separately.

These are proposed requirements. No mesh, render, soft-body model or import was tested in this refresh. An anatomically plausible still image cannot validate deformation, cutting, suturing or fine motor interaction.

## Rights policy and acquisition gates

Personal use does not supply missing rights; a public GitHub upload distributes files. CC0 is simplest; CC BY requires credit/license/change notices; NC restricts purposes; SA imposes adaptation conditions; ND is unsuitable for the modified-asset pipeline. Check exact licenses, not search filters. [CC BY legal code](https://creativecommons.org/licenses/by/4.0/legalcode), [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/), [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).

For each acquired asset add `source_version`, `acquired_at`, `sha256`, `local_path`, `license_evidence_path`, `changes`, `credit_text`, `medical_reviewer`, `technical_reviewer`, `engine_compatibility` and `shipping_status`. Candidate metadata is insufficient for shipping. Credits must travel in the repository and distributed game; public-source permission and packaged-build permission are separate checks. Do not apply the repository code license to third-party assets.

Stop an asset at intake if terms are missing, contradictory, incompatible with the engine or inadequate for intended use. Choose a verified substitute or original modeling. “Free,” “educational,” download availability and attribution alone do not establish permission. Copy the exact BodyParts3D acknowledgement from its source license and the Digital Surgery credit from its item metadata when those assets are acquired.

## Search record, limitations and next decisions

Queries included `site.humanatlas.io heart male v1.3 license`, `site.z-anatomy.com license BodyParts3D`, `site.3d.nih.gov 3DPX-022787`, `site.makehumancommunity.org MPFB license`, `site.zenodo.org TotalSegmentator dataset`, and `site.freesound.org monitor Creative Commons 0`. Publisher pages were opened. Sketchfab and Zenodo APIs supplied fields omitted by browser extraction; the HRA repository API confirmed v1.2 filenames. No binaries were downloaded, no geometry or audio was inspected, and no clinical endorsement was obtained.

Next: acquire one coherent anatomical base, reconcile package notices, build one coronary target and two instruments, then review them with a clinician inside the selected engine. Coronary walls, tissue mechanics, donor registration, instrument geometry and license evidence remain acceptance gates. Evaluate this small sample before committing to large packs.
