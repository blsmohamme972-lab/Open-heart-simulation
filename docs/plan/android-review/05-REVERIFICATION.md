# Android realism — second verification

**Date:** 2026-11-03. **Baseline:** proposal 002 revision 1, commit `f7e57e5`. **Review ID:** OHS-ANDROID-RECHECK-002.

The owner requested another careful check. This audit revisits official platform documentation, the source paper and dataset, asset metadata, and the actual coronary mesh files. Two additional read-only reviewers covered Android and motion/assets; the coordinator repeated the geometry checks and reconciled their findings. This is technical/source review, not independent clinical validation.

Evidence was uploaded in `6278268`. The corrections below are incorporated into proposal revision 2 and the four supporting reports. Both reviewers re-read the revised text; the original two-file indexing diagnostic is now distinguished explicitly from the ten-file structural recheck.

## Verdict

The regional heart-motion approach and functional-tool requirements remain reasonable proposals. **The plan needed corrections before implementation:** native Android packaging, engine defaults, temporal contact synchronization, and more precise asset-readiness evidence. Godot remains a candidate; no engine or asset has passed a phone or specialist acceptance test.

| Finding | Consequence | Required correction in revision 2 |
|---|---|---|
| Native-library page-size compatibility was omitted | An otherwise convincing prototype may fail to install or run on a supported phone | Gate the complete ARM64 package, all native dependencies, alignment and runtime behavior in 4 KB/16 KB environments |
| Platform Vulkan availability was not separated clearly enough from engine requirements | API support alone can overstate the application's device coverage | Pin engine/export-template versions, ABI, SDK policy, actual renderer and feature requirements |
| Engine pacing and renderer defaults were unspecified | Automatic cadence/renderer changes can silently violate the promised quality tier | Explicit pacing/refresh policy; detect renderer fallback and admit only tested tiers |
| Shared spatial geometry did not fully specify time synchronization | A tool and tissue can use the same cage at different times and visibly intersect | Timestamped simulation snapshots, a common presentation time, moving-surface collision tests and latency/error traces |
| Two STL files were the only inspected motion samples | Structural results could not be generalized to the sequence | Inspect all ten files; retain clinical/correspondence limits |
| Tool listings lacked concrete preparation evidence | Catalogue models could be mistaken for mobile, articulated instruments | Record source face counts, animation metadata and exact credits; retain geometry/articulation gates |

## 1. Android findings and primary sources

Android 15 introduced support for 16 KB page-size devices. Native code includes engine libraries and third-party plugins, not only a project-owned solver. Require compatible export templates/dependencies, ELF and package alignment checks, and execution with the page size verified. Current guidance recommends AGP 8.5.1+ and NDK r28+ alongside compatible prebuilts; that does not replace runtime testing. The live page checked today states **February 1, 2027** for blocking noncompliant Google Play updates targeting Android 15+. Recheck distribution policy at release; private installation still needs device compatibility. [Official page-size guidance](https://developer.android.com/guide/practices/page-sizes).

Godot's current exported-project requirements list Android 9.0 for Mobile/Forward+ and Android 7.0 for Compatibility. These are engine minimums, not evidence of this application's performance. [System requirements](https://docs.godotengine.org/en/stable/about/system_requirements.html#exported-godot-project).

Godot documents Android Swappy enabled by default and an automatic pacing mode that can lower cadence. Therefore a proposed 60 FPS tier needs a pinned, tested pacing/refresh policy. [Swappy mode](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-display-window-frame-pacing-android-swappy-mode). Renderer fallback also requires explicit handling: log the actual backend and admit a Compatibility tier only after its own tests. [Renderer switching](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html#switching-between-renderers).

The earlier feature table remains correct: Godot Mobile has no built-in SSS, SSR or normal/roughness buffer. A custom tissue approximation is an unproved implementation task. The AGI quickstart now recommends **Android Performance Analyzer for system profiling**; AGI remains documented for frame profiling. Qualify the selected profiling tool against the actual phone/driver instead of declaring AGI universally unavailable or deprecated. [AGI quickstart](https://developer.android.com/agi/start), [APA](https://developer.android.com/android-performance-analyzer).

## 2. Motion and contact: spatial agreement is insufficient

Godot's interpolation documentation explains that rendered transforms can represent an earlier state than the current physics tick. [Physics interpolation](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/physics_interpolation_introduction.html). A shared mesh mapping does not eliminate that temporal difference.

**Proposed contract:** keep timestamped authoritative tissue/tool snapshots and accepted input events. Advance cardiac phase and tool state within the declared simulation/substep scheme. Evaluate swept contact against both moving participants. Present tools, tissue, attached threads and contact cues using a consistent presentation time. Geometry/topology revisions travel with the snapshot; do not interpolate across incompatible wound topology. Reset interpolation history on a discontinuity. This is an implementation design, not a feature provided automatically by enabling engine interpolation.

Measure geometric mapping error and temporal lag separately. Test a stationary tool against beating tissue, moving tools against moving tissue, variable rendering cadence, frame stalls, arrest transitions, LOD changes and resume. Cursor prediction may remain visual; it must not commit puncture/cut events from unaccepted input. Freeze the solver tick/substep policy within each tested configuration and record overload behavior. Smooth rendering alone does not validate collision timing.

## 3. Ten coronary files rechecked

All ten STL files in [versioned record 10203116](https://zenodo.org/records/10203116) were read from temporary storage outside the repository; eight were newly downloaded, and the earlier two were rechecked. Every file matches the publisher's MD5. The original two also reproduce their previously recorded SHA256 values.

| Check | Result for each of the ten files |
|---|---|
| File length / triangle-record layout | 1,968,484 bytes; expected binary layout passes |
| Triangles | 39,368 |
| Exact-coordinate unique positions | 19,740 |
| Edges incident to one triangle | 118 |
| Edges incident to more than two triangles | 0 |
| Exact zero-area triangles / nonfinite vertex occurrences | 0 / 0 |

Exact filenames, checksums, method and limitations are recorded in [coronary-sequence-recheck.json](coronary-sequence-recheck.json). No binary assets are committed. These checks do not test self-intersections, vertex manifoldness, near-degeneracy, rendering, scale or clinical suitability. Boundary edges may be intended vessel ends; do not close them blindly.

The [source paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10811335/) describes a method preserving mesh connectivity, using one patient's high-resolution reference and ten coarser dynamic CT phases. Thus the previous ordering-dependent digest mismatch is **not evidence of different anatomical topology or unusable data**. Recover the export correspondence before morphing; segmentation registration does not establish tissue material-point motion. The sparse phases also do not independently validate an interpolated velocity/acceleration curve or exposed/unloaded-heart behavior. STL still supplies no declared physical unit; resolve coordinates and units from the acquisition/export lineage before scaling.

## 4. Assets and rights rechecked

The official [BodyParts3D archive](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [HRA library](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html), [coronary metadata](https://zenodo.org/api/records/10203116) and [four-chamber metadata](https://zenodo.org/api/records/4590294) retain the recorded CC BY 4.0 terms. The [Sunnybrook page](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) retains its CC0 terms, but a usable direct download route remains unresolved. These checks do not extend permissions to unrelated datasets.

| Item | API metadata rechecked | Interpretation |
|---|---|---|
| [Wenschel instruments](https://api.sketchfab.com/v3/models/bd0ad0180f5148f1b3b331b8ebe6e494) | CC BY 4.0; downloadable; 1,202,202 faces, 601,132 vertices, zero animations | Offline reference candidate; optimization and functional inspection required |
| [Digital Surgery collection](https://api.sketchfab.com/v3/models/46f5799ca36240efae3abec6e61d4c8a) | CC BY-NC 4.0; downloadable; 614,712 faces, 307,445 vertices, zero animations | Noncommercial reference candidate; preserve item-specific credits |

Counts refer to the source listings, not measured exported Android geometry. Zero listed animations does not establish whether jaws are separable or riggable. Neither instrument binary was acquired. Preserve Digital Surgery's requested credit naming Christopher Remde, Moritz Queisner (2024), Experimental Surgery, Charité Universitätsmedizin Berlin and NMY Mixed-Reality Communication GmbH; capture the exact credit text at acquisition.

## 5. What remains unresolved

No phone model, minimum performance tier, reviewed tissue-force parameters, clinical error thresholds, custom material, rig, contact implementation or APK exists. Those remain explicit future gates. Healthy CMR, a coronary CT reconstruction and a noncardiac suturing study cannot collectively certify this simulator. Revision 2 preserves these limits while adding the corrections above.

Another agent should compare this audit, [the revised proposal](../../proposals/OHS-PROPOSAL-002-ANDROID-REALISM.md), the four supporting reports and both inspection records. Improve an identified gate with evidence; do not treat repeated source checking as a completed device benchmark.
