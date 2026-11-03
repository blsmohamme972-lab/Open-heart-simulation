# 07 — Production, tools, and validation: fresh research

Researched: **2026-11-03**. Planning only. Timelines, staffing, budgets, and gates below are project estimates, not outcomes established by the cited sources. No medical reviewers have been engaged and no prototype has been benchmarked.

## 1. Production conclusion

A credible project should start with one small, anatomically reviewed surgical interaction coupled to a visible physiological consequence. A beautifully rendered heart that ignores tool contact, or an accurate circulation model behind scripted clicks, would not meet the owner's realism goal. Build toward a complete adult on-pump CABG case through separate evidence gates for anatomy, interaction, physiology, workflow, and assessment. Do not begin with every procedure, autonomous medical staff, full free cutting, VR, and haptics simultaneously.

The existing Python heartbeat example alternates a label and two fixed pressure values; it provides neither beat-resolved cardiovascular dynamics nor validation of a new simulator. Preserve it as history, but plan a new simulation core rather than extending its outputs into medical claims.

## 2. Scope at 3, 6, 12, and 24 months

Assumption for these estimates: one experienced full-time developer, intermittent anatomy/technical art help, and scheduled access to a cardiac surgeon, perfusionist, cardiac anesthesiologist, and theatre nurse. A part-time solo developer without clinical access should expect substantially longer. These are scope ceilings, not delivery promises.

| Horizon | Credible target if previous gate passes | What is still outside that target |
|---|---|---|
| 3 months | Validated source/asset inventory; one heart/thorax region; camera/tools; circulation baseline; tissue and bounded-stitch feasibility demonstrations | Complete operation, clinical skill assessment, photorealistic whole OR |
| 6 months | A coherent vertical slice: one graft attachment task on a supported/arrested heart, team cues, controlled leak and recovery, replay | All harvesting/anastomoses, full anesthesia, arbitrary cutting |
| 12 months | Closed alpha of one complete case with clearly marked assisted stages and selected modeled complications, if slice succeeds | Broad patient population, certified training, realistic force feedback without hardware |
| 24 months | A narrower polished desktop release or advanced alpha, with more manual tasks and reviewed variants, depending on workload and funding | Guaranteed clinical equivalence, all cardiac procedures, unlimited emergency scenarios |

Before adopting dates, estimate actual work packages and dependencies, then add explicit contingency. An engine switch, new mesh topology method, or loss of clinical review invalidates the old schedule. A three-person engineering/art team may parallelize content and testing; it does not remove the hard interaction or validation research.

## 3. Tools and reproducible source control

Use ordinary Git for documents, source, small configuration, source metadata, and test cases. Use Git LFS only for licensed working binaries such as `.blend`, textures, audio, and engine assets once implementation begins. Pin editor/build versions; record exported asset hashes and import settings. GitHub currently meters LFS storage and download bandwidth, and whole new file versions consume storage. Set an explicit account budget and check owner-specific allowances before uploading large anatomy packages. [GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs).

Proposed repository boundaries:

- `docs/plan/`: this plan, decisions, evidence, review findings, and future revision history.
- `sim/`: future portable simulation library, schemas, fixtures, and tests.
- `game/`: future selected-engine source and content manifests.
- `assets/source/`: future cleared source artwork in LFS, with license records.
- `assets/derived/`: reproducible exports or pointers; no untracked provenance.
- `validation/`: future synthetic cases, review rubrics, signed review records, and benchmark outputs.

Do not initialize these implementation directories merely to make the plan appear built. There are no asset downloads or runtime additions in this task.

For CI, run documentation/schema checks and lightweight simulation tests on hosted runners. Plan full engine package builds on an appropriately licensed, isolated build machine after measuring cost. Because this repository is public, do not attach a persistent workstation runner to arbitrary external pull requests; GitHub specifically warns that public PRs can compromise self-hosted runners. [GitHub secure use reference](https://docs.github.com/en/actions/reference/security/secure-use). This is an implementation design requirement, not a request to change repository settings now.

Replay reproducibility must have a declared boundary. Event ordering, scenario seeds, simulation configuration, version, and checkpoint state should replay on the same pinned build. Floating-point solvers, GPU tissue systems, and external libraries may not reproduce bit for bit across hardware. Compare defined observables within published tolerances rather than promising deterministic GPU physics everywhere.

## 4. Asset preparation and AI-assisted work

Blender is the primary offline modeling, retopology, UV, rigging, and export tool. Its GPL license governs the application, not a blanket license on the user's artwork; imported asset rights still govern the output. Official license page search text was accessible; direct page retrieval returned a fetch error in this run. Recheck the exact installed release and bundled add-ons before distribution. [Blender license](https://www.blender.org/about/license/).

3D Slicer is an optional offline segmentation and geometry-review tool, under its custom BSD-style license; extensions and source medical data have separate terms. Its documentation explicitly distinguishes the software license from clinical approval. [Slicer license and intended use](https://slicer.readthedocs.io/en/v5.12.0/user_guide/about.html). COLMAP is optional for photographing owned nonclinical props: its new BSD license does not cover every dependency. [COLMAP license](https://colmap.github.io/license.html). Neither should be embedded in the game merely because it can prepare an asset.

Procedural Blender geometry is preferable for generic instruments, tubing, trays, clamps, and simple OR furniture when no suitable item-specific license exists. Photograph only objects and spaces for which permission is available. Human likeness, branding, hospital footage, and patient data require their own permissions.

AI assistance can draft scripts, shader experiments, documentation, and nonclinical concepts. Generated coronary anatomy, surgical imagery, or material maps are not medical evidence. Every candidate needs provenance, terms applicable to the chosen service/version, anatomical review, and a human check for unwanted copied logos or artifacts. No specific third-party AI asset service is selected or cleared in this plan, and no generative model is needed in the shipped runtime.

## 5. Clinical and educational validation

INACSL's standards identify purposeful objectives, prebriefing, facilitation, evaluation, and debriefing as parts of simulation design; several cornerstone standards were revised in 2025. Use them to structure review, not to claim endorsement. [INACSL current standards](https://www.inacsl.org/healthcare-simulation-standards-of-best-practice).

Separate the following evidence:

| Evidence layer | What the project must record | What it cannot establish alone |
|---|---|---|
| Source traceability | Source version, population, units, conflicting statements, chosen scenario protocol | That implementation is accurate |
| Software verification | Conservation, stability, state transitions, reproducibility, failure handling | That model physiology matches people |
| Face/content review | Named discipline, review date/build, rubric, disagreements and corrective actions | Learning or transfer to surgery |
| Construct evidence | Preplanned comparisons of experience groups, confounders including gaming skill | Clinical competence or causality |
| Learning/transfer study | Defined outcome, ethical review where applicable, sample-size justification, comparison group, external assessment | Automatic validity of every future version |

Before an anatomy freeze, ask a surgeon and anatomy specialist to review orientation, coronary topology, tissue layers, instrument approach, and what is missing. Before a bypass freeze, ask a perfusionist and cardiac anesthesiologist to inspect causal traces and monitor behavior, including contradictory cues. Before a full-case alpha, ask a theatre nurse and surgeon to inspect task ownership, sterile interactions, handoffs, closure, and recovery.

These reviewers are required future roles, not people who have already approved the plan. Without access, the work can remain an explicitly unvalidated experimental game; it must not advance through a gate labeled clinically reviewed.

## 6. Intended use, rights, and distribution

Keep the intended use educational/entertainment with fictional cases. Do not accept patient data or offer diagnosis, patient-specific planning, device control, credentialing, or treatment recommendations. FDA examples distinguish general educational software from patient-specific medical functions; this is relevant U.S. guidance, not a universal legal determination. A disclaimer alone does not determine regulatory status. [FDA educational software examples](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices).

The current repository is public, so uploading an asset is redistribution even if the owner intends personal use. Keep reference-only or unclear-license material outside distributable assets; do not choose a project-wide license on the owner's behalf. Requirements for each asset and dependency must be satisfied separately. The final asset ledger is mandatory before any package can ship.

For public distribution, complete the relevant storefront's ratings process. Blood and gore are recognized content descriptors, but this plan does not assign an ESRB/PEGI rating. Include explicit content settings, captions, volume separation, camera comfort, and input accommodations from the start. [ESRB ratings guide](https://www.esrb.org/ratings-guide/).

## 7. Principal production risks

| Risk | Early evidence to collect | Response if it fails |
|---|---|---|
| Free assets lack surgical topology | Inspect coronaries, lumens, layers, scale, and source rights | Budget original remodeling; reduce first operative field |
| Cutting/sutures unstable or unusable | Bounded interaction spike and novice/expert usability sessions | Authored seams and stitches; label assistance honestly |
| Model looks plausible but is wrong | Coupled perturbation traces and expert disagreements | Simplify claims; recalibrate or replace failed subsystem |
| Unreal/content license conflict | Per-item licenses plus engine compatibility review | Use permissive/original content or decide engine before production |
| Schedule hidden by polish work | Weekly integrated slice and work remaining | Stop cosmetic expansion until causal task works |
| Review access unavailable | Booked review cadence before clinical gate | Keep prototype experimental and unvalidated |
| Large binary costs expand | Asset inventory and growth forecast | LFS quotas, smaller derivatives, rights-cleared external storage |
| Input cannot represent required skill | Precision task with declared assistance and movement metrics | Assess cognitive/procedural tasks; defer motor transfer claims |

## 8. Search log and unresolved questions

Queries used: `site:docs.github.com Git Large File Storage storage bandwidth billing 2026`; `site:inacsl.org healthcare simulation standards best practice evaluation educational design`; `site:fda.gov device software functions intended use medical device educational simulation`; `site:docs.github.com self hosted runners public repositories security untrusted pull request`; `site:blender.org about license freedom output artwork`; `site:esrb.org ratings guide blood gore intense violence`; official COLMAP and Slicer license searches. Opened primary pages linked above; search snippets were not treated as full-text review when page fetch failed.

Remaining owner-specific inputs: available PC/GPU, weekly hours, collaborator skills, clinical reviewer access, preferred input devices, spending limit, and whether eventual distribution remains private/personal. Defaults allow the plan to proceed; hardware and cost commitments wait until implementation scoping. No additional user answer is needed to complete this planning document.
