# Android review — anatomical and instrument assets

Checked 2026-11-03. The preferred pipeline uses rights-cleared source geometry plus original surgical detail and motion authoring. A marketplace model is not accepted merely because it looks realistic. “Open source,” “free to download” and “noncommercial permission” are different conditions.

## Shortlist and exact use boundaries

| Candidate / creator | Exact source and permission evidence | Proposed use and remaining gate |
|---|---|---|
| BodyParts3D 4.0 / Database Center for Life Science | [Archive download](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html); [CC BY 4.0 license](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html) | Thorax/anatomical context. Acquire under updated archive terms, preserve required credit/change notices; geometry not inspected in this review |
| HRA male heart v1.2 / Browne, Schlehlein and collaborators | [Exact GLB](https://github.com/hubmapconsortium/ccf-releases/blob/main/v1.2/models/VH_M_Heart.glb); [library CC BY 4.0 terms](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html) | Reference organ candidate; no claim of complete coronary walls, surgical topology or living motion |
| Coronary 4D reconstruction / Psiuk-Maksymowicz et al. | [Pinned record 10203116](https://zenodo.org/records/10203116); [API license CC BY 4.0](https://zenodo.org/api/records/10203116) | LCA surface phases for motion research; two phases inspected structurally. Attribution/changes required; not a whole-heart animation asset |
| Sunnybrook Cardiac Data / Perry Radau and Sunnybrook contributors | [Publisher page, including CC0 1.0 terms](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) | Cine-MRI/LV motion reference. Page confirms permission, but extracted download links are absent: acquisition route unresolved. Other CAP cohorts do not inherit this license |
| Four-chamber CT mesh cohort / Rodero, Strocchi et al. | [Record 4590294](https://zenodo.org/records/4590294); [API license CC BY 4.0](https://zenodo.org/api/records/4590294) | Twenty end-diastolic geometries and associated outputs; optional offline model source. API listing does not establish time-resolved vertex animation or mobile readiness |
| Surgical instruments / Wenschel | [Item](https://sketchfab.com/3d-models/surgical-instruments-bd0ad0180f5148f1b3b331b8ebe6e494); [API confirms CC BY 4.0](https://api.sketchfab.com/v3/models/bd0ad0180f5148f1b3b331b8ebe6e494) | Candidate visual/blockout base. Downloadability rechecked; geometry not acquired. Jaws, dimensions, articulation and tips need inspection/rebuild |
| Surgical Instruments collection / Digital Surgery | [Item](https://sketchfab.com/3d-models/surgical-instruments-collection-46f5799ca36240efae3abec6e61d4c8a); [API confirms CC BY-NC 4.0](https://api.sketchfab.com/v3/models/46f5799ca36240efae3abec6e61d4c8a) | Noncommercial alternative with attribution and purpose restrictions. Recheck full credit requirements at acquisition; no commercial reuse assumption |
| Original heart target surfaces and functional tools / project artists | No acquired file yet; source references and final project rights must be recorded | Preferred for coronary wall/lumen, precise tip/jaw geometry and deforming patches when existing assets fail the functional review |

The coronary concept record `10203115` resolves through the API to the versioned record `10203116`; pin the latter. Its metadata lists ten STL phases at ten-percent cycle increments and a video. The author paper is [PMID 38273032](https://pubmed.ncbi.nlm.nih.gov/38273032/). The dataset's license does not automatically permit copying every journal figure or unrelated patient material.

The four-chamber cohort is a potentially useful **static modeling base**, not a finished rig. Combining its myocardium with HRA/BodyParts3D vessels from different sources requires anatomical registration and review. Do not present a composite as a coherent patient scan.

## What was actually inspected

Two coronary STL files were acquired to temporary storage and parsed for geometry metadata. [The JSON record](motion-sample-inspection.json) preserves exact filenames, hashes, counts, native bounds, boundary/nonmanifold edge counts and limitations. No binary asset is uploaded to the repository. The two phases' indexed connectivity comparison differs, so direct vertex-index interpolation is not cleared. Scale, surface correspondence, vessel-wall thickness and clinical suitability remain unresolved.

All other candidates above were checked at the source/metadata level only. No new HRA mesh, CT cohort, instrument kit, sound or texture was downloaded or visually approved.

## Required anatomy asset contract

Each accepted anatomical asset needs: source/release/hash/license, explicit units and coordinate frame, named structures, chamber/vessel connectivity, landmarks, thickness where interaction needs it, anatomical attachment regions, render mesh, motion/control mesh, collision mesh, cuttable regions, material regions, source-to-export mapping and reviewer status.

Separate vascular lumen surface from actual wall material. A printable closed shell, a segmentation boundary and a surgical wall model are different representations. Preserve coronary branches and vessel openings when reducing geometry; do not trade them away for a lower triangle count. Local operative detail matters more than uniformly dense background anatomy.

## Instrument asset contract

The mesh must document actual dimensions and measurement provenance, functional tips, jaw and hinge axes, opening range, ratchet/lock behavior where present, grip regions, contact surfaces, cutting edges, needle curvature, articulation animation and collision proxies. Blade sharpness, stiffness, friction and tissue response are model parameters requiring evidence; a material name such as “steel” does not establish them.

Use original measured models for the fine needle holder, atraumatic forceps, scissors, vascular clamp and needle before building the full catalogue. Manufacturer diagrams can be references only when lawfully available; they do not automatically license copied mesh geometry or logos. Instrument scale and function need a surgical reviewer, even for commercially sold models.

## Mobile preparation

Keep the editable high-detail source and generate engine-specific derivatives. In Blender: establish scale/orientation; reconstruct needed walls; retopologize the active region; define stable anatomical IDs; rig/bake motion; bind attachments; create collision and LOD versions; author PBR maps; and test one export/import round trip before batch processing. Blender output retains imported-content obligations; the application license is not the asset license. [Blender FAQ](https://www.blender.org/support/faq/).

Do not bake lighting highlights into base color. Keep color maps in the correct color space and geometry/roughness/thickness data linear. Mipmaps and compression must preserve thin vessel borders and tool-tip readability at the closest supported view. KTX2/Basis can be useful transport/texture tooling, but actual importer support and GPU format must be tested in the selected engine; packaging size is not runtime memory use. [Khronos artist guide](https://github.com/KhronosGroup/3D-Formats-Guidelines/blob/main/KTXArtistGuide.md).

Runtime budgets are to be profiled, not selected by arbitrary “AAA” polygon or texture labels. Preserve the active contact mesh when visual LOD changes. Additional material detail that consumes thermal headroom without improving anatomy recognition or contact readability is lower priority.

## Rights and release gates

CC0 and CC BY candidates are the baseline; the latter requires attribution/license/change notices. NC assets remain clearly segregated and cannot be carried into a later commercial release by assumption. The prior Unreal-specific ShareAlike conflict does not become a universal prohibition in a Godot project, but each adaptation's obligations still apply. Neither a private-use intention nor an engine change clears missing rights.

Before shipping, extend the [existing asset ledger](../ASSET_LICENSES.csv) with the exact acquired file/version, hash, evidence snapshot, credit text, modifications, export lineage, public-source/package rights and reviewer result. This review does not silently mark candidates as approved.

Search/recheck covered publisher anatomy licenses, versioned Zenodo APIs, CAP terms, specific Sketchfab item APIs, Blender output rights and Khronos texture guidance. No unverified marketplace or AI-generated anatomy is selected as anatomical ground truth.
