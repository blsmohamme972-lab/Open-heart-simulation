# Android realism review — scope and checkpoints

Date: 2026-11-03. Owner correction: the target is an **Android application**, with very high performance and realism. This review focuses on **heart animation, anatomical/instrument assets, rendering engine, and tool–tissue interaction**. The ambition is world-leading realism; no comparative superiority is established by a plan.

The desktop-first platform and automatic Unreal preference in proposal OHS-PROPOSAL-001 are superseded for this review. Retain that snapshot for comparison. The new proposal is [OHS-PROPOSAL-002-ANDROID-REALISM](../../proposals/OHS-PROPOSAL-002-ANDROID-REALISM.md). Full-case physiology, anesthesia, assessment and broader production plans are not being reimplemented here.

## Working assumptions

- Native Android rendering and interaction; no assumed remote rendering service.
- Open-source tools and reusable assets preferred; noncommercial licenses may be acceptable when their actual terms permit the use and redistribution.
- Initial quality target: selected high-end Android devices, with a separately tested reduced tier. The owner has been asked about device class; no device model or minimum specification has been confirmed.
- Research/design only. No Android application, engine project, asset import or device benchmark is being claimed.

## Checkpoints

| Stage | Output | State |
|---|---|---|
| A | Corrected scope and audit brief | Uploaded in `00150f4` |
| B | Focused source review of engine, animation, assets and tools | Uploaded in `6e37271` |
| C | New Android proposal, comparison to old choices, acceptance tests and source navigation | Uploaded in `f7e57e5` |
| D1 | Requested second verification and all ten coronary phase files checked | Evidence checkpoint; see [audit](05-REVERIFICATION.md) |
| D2 | Proposal revision 2 and report reconciliation | In progress after evidence checkpoint |

Each completed stage is committed and pushed to the repository. Parallel review assistance was used; some workers stopped with workspace credit-limit errors. The coordinator continues the unsaved work and does not claim an independent clinical or runtime validation.

## Focused evidence

1. [Engine and Android rendering](01-engine-rendering.md)
2. [Heart animation and contact geometry](02-heart-animation.md)
3. [Asset candidates and licenses](03-assets-licenses.md)
4. [Functional instruments and tissue contact](04-instruments-contact.md)
5. [Second verification and concrete corrections](05-REVERIFICATION.md)

The initial inspection covered two CC BY 4.0 coronary STL phases, with results in [motion-sample-inspection.json](motion-sample-inspection.json). The second verification extends structural checks to all ten phases in [coronary-sequence-recheck.json](coronary-sequence-recheck.json). Equal mesh counts do not establish material correspondence; ordering-dependent hashes do not establish different topology. No asset binary or application code is committed. No rendered/clinical geometry approval or phone benchmark was performed.

## Final disposition

Godot Mobile/Vulkan is a provisional open-source-first candidate, conditional on a tissue-shader and device comparison. The proposed heart-animation pipeline requires a reviewed regional reference basis with shared contact geometry; instruments require functional articulation and contact models. The focused reports and new proposal retain explicit evidence and licensing limits. A separate engine reviewer checked the focused reports, inspection record and proposal 002 and found no blocking inconsistency; this is a technical consistency review, not a clinical sign-off.

No device preference was received during this review; high-end-first remains an explicit reversible assumption. “World-leading” is an ambition to test through defined comparison criteria, not an achieved result.

Documentation checks passed across 25 Markdown files and 138 local links/anchors; the inspection JSON is internally consistent and `git diff --check` passed. Existing Python example/test files and `.gitignore` match the pre-review commit `b761761`. No runtime test result is implied by these checks.
