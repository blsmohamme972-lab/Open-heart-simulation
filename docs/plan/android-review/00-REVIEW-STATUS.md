# Android realism review — scope and checkpoints

Date: 2026-11-03. Owner correction: the target is an **Android application**, with very high performance and realism. This review focuses on **heart animation, anatomical/instrument assets, rendering engine, and tool–tissue interaction**. The ambition is world-leading realism; no comparative superiority is established by a plan.

The desktop-first platform and automatic Unreal preference in proposal OHS-PROPOSAL-001 are superseded for this review. Retain that snapshot for comparison. The new proposal will be named **OHS-PROPOSAL-002-ANDROID-REALISM**. Full-case physiology, anesthesia, assessment and broader production plans are not being reimplemented here.

## Working assumptions

- Native Android rendering and interaction; no assumed remote rendering service.
- Open-source tools and reusable assets preferred; noncommercial licenses may be acceptable when their actual terms permit the use and redistribution.
- Initial quality target: selected high-end Android devices, with a separately tested reduced tier. The owner has been asked about device class; no device model or minimum specification has been confirmed.
- Research/design only. No Android application, engine project, asset import or device benchmark is being claimed.

## Checkpoints

| Stage | Output | State |
|---|---|---|
| A | Corrected scope and audit brief | Uploaded in `00150f4` |
| B | Focused source review of engine, animation, assets and tools | Complete; publish this checkpoint |
| C | New Android proposal, comparison to old choices, acceptance tests and source navigation | Pending |

Each completed stage is committed and pushed to the repository. Parallel review assistance was used; some workers stopped with workspace credit-limit errors. The coordinator continues the unsaved work and does not claim an independent clinical or runtime validation.

## Focused evidence

1. [Engine and Android rendering](01-engine-rendering.md)
2. [Heart animation and contact geometry](02-heart-animation.md)
3. [Asset candidates and licenses](03-assets-licenses.md)
4. [Functional instruments and tissue contact](04-instruments-contact.md)

The coordinator additionally downloaded two CC BY 4.0 coronary STL phases to temporary storage and inspected their binary geometry, with results in [motion-sample-inspection.json](motion-sample-inspection.json). Equal mesh counts did not establish compatible point indexing; registration is a required gate. No asset binary or application code is committed. No rendered/clinical geometry approval or phone benchmark was performed.
