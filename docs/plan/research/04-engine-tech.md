# Research 04 — Engine and simulation technology

Research refreshed **2026-11-03**. Planning only; no engine, solver, benchmark or integration has been built or tested. Source-backed capabilities are distinguished below from proposed engineering choices. Sources were searched and opened on the research date; software versions and commercial terms must be checked again when implementation begins.

## Recommendation and conditions

Use **Unreal Engine 5.8 as the initial desktop prototype candidate**, Blender for authored geometry, and a small, independently testable C++ interaction/physiology interface. Pin an exact supported patch and toolchain after the first packaged-build experiment. Epic's official announcement establishes 5.8 availability; it does not establish suitability for surgical simulation. [Epic announcement](https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available)

The first interactive scope should be an arrested-heart CABG task with a bounded operative region, authored incision boundaries, explicit vessel openings, and constrained needle/thread interactions. Full arbitrary cutting and physically simulated knot tying are separate research goals. This is a feasibility decision, not a claim that authored interactions reproduce all operative mechanics.

Unreal is preferred provisionally because its C++ integration and material tooling suit a visually detailed desktop scene. This is an engineering judgment, not a measured ranking. Unity 6.3 LTS is the practical fallback if its prototype demonstrates better development velocity or a maintainable SOFA integration. Godot remains a legitimate alternative if unrestricted engine licensing or lower tooling cost dominates; it should not be dismissed merely because it has fewer medical examples.

**Engine selection depends on asset rights.** Epic's EULA restricts combining its technology with incompatible licenses, explicitly including GPL and CC BY-SA, and distinguishes dynamic linking for LGPL. Do not import a GPL Unreal bridge or assume a CC BY-SA anatomical model becomes compatible because it is stored separately. Use original/permissively licensed anatomy, obtain appropriate alternative rights, or reassess the engine. An offline authoring tool's license and the license of its output are separate questions. [Epic EULA, §6(c)](https://www.unrealengine.com/eula/unreal)

## Engine comparison

| Candidate | Verified terms and capabilities | Project implication |
|---|---|---|
| Unreal 5.8 | Proprietary EULA. Eligible personal/noncommercial use has no seat charge; the standard game royalty is 5% of applicable lifetime product gross revenue above US$1 million, subject to exclusions/other terms. Commercial non-game seat cases differ. Preserve required notices. [Licensing](https://www.unrealengine.com/license) | No upfront engine purchase assumed for this personal game. Engine source is not generally redistributable in this public repository. Archive accepted terms and keep third-party entitlements separate. |
| Unity 6.3 LTS | Proprietary editor terms. Personal is free within eligibility criteria, including the US$200,000 revenue/funding threshold; 2026 Pro list price is US$2,310/seat/year prepaid. Runtime Fee cancelled. 6.3 LTS support is listed through December 2027. [Pricing](https://unity.com/products/pricing-updates), [release/support page](https://unity.com/releases/unity-6) | Strong C# iteration candidate; plugin native-library packaging, render-pipeline choice and build-backend compatibility need experiments. Personal/noncommercial intent alone is not an exemption from every eligibility condition. |
| Godot 4.7.2 | Official download page lists 4.7.2. Engine is MIT, permitting personal/commercial use with copyright/license notices; bundled third-party notices also apply. [Download](https://godotengine.org/download/windows/), [license](https://godotengine.org/license/) | No engine royalties or revenue eligibility ceiling. More custom integration is likely for this particular plan, but prototype results must decide rather than an invented numerical engine score. |

Unreal provides screen-space subsurface-profile shading with artist-controlled scattering. Unity HDRP also provides subsurface scattering. Neither renders living myocardium correctly simply by choosing a skin preset: tissue thickness, blood film, epicardial fat, illumination and reference calibration still require authored materials. [Epic material documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine), [Unity HDRP documentation source](https://github.com/Unity-Technologies/Graphics/blob/master/Packages/com.unity.render-pipelines.high-definition/Documentation~/skin-and-diffusive-surfaces-subsurface-scattering.md)

Godot's SoftBody3D documentation describes mesh-based deformation and pinned points, warns that configuration can produce unstable-looking results, and notes interpolation limitations. It does not document surgical cutting or suturing. Likewise Unity's physics roadmap documents its general-purpose physics systems, not a ready cardiac-surgery solver. [Godot SoftBody3D](https://docs.godotengine.org/en/stable/tutorials/physics/soft_body.html), [Unity physics team update](https://discussions.unity.com/t/physics-development-status-and-next-milestones-may-2025/1637988)

## What tissue solvers can and cannot establish

**Chaos Flesh:** Epic describes tetrahedral soft-body deformation, primarily for character muscles, using low-resolution runtime geometry and optionally cached high-resolution results. It supports kinematic/weak constraints and forms of collision. Its overview does not establish runtime incision remeshing, vessel-wall puncture, arbitrary suturing or validated tissue parameters. Use it as a candidate for intact gross deformation only; do not make the first playable case depend on undocumented topology changes. [Chaos Flesh overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-flesh-overview)

**XPBD:** the original paper introduces compliance and constraint-force estimates to address conventional PBD's time-step/iteration-dependent stiffness. The later *Small Steps* paper shows benefits from substeps in its experiments. These are numerical methods, not evidence of cardiac tissue accuracy. Contact, friction, anisotropy, mesh resolution, integration error and calibration remain decisive; avoid saying “unconditionally stable” for an entire surgical simulator. An XPBD prototype is appropriate for bounded retraction and thread constraints because complexity can be controlled. [Macklin, Müller and Chentanez, 2016](https://matthias-research.github.io/pages/publications/XPBD.pdf), [Macklin et al., 2019](https://matthias-research.github.io/pages/publications/smallsteps.pdf)

**FEM/SOFA:** SOFA is a modular medical-simulation framework, not a single validated heart model. Its main libraries are LGPL-2.1-or-later according to its README; check licenses for every selected plugin/component. It can provide a comparison implementation for indentation/retraction experiments, initially offline. A FEM result is not ground truth unless constitutive laws, boundary conditions, geometry and numerical convergence have independent support. [SOFA repository](https://github.com/sofa-framework/sofa), [licensing statement](https://github.com/sofa-framework/sofa/blob/master/README.md)

**Mass-spring or blend-shape deformation:** reasonable for early interaction sketches or secondary tissue motion, but should not generate claimed force accuracy or infer tissue damage without calibration. The choice between these and XPBD/FEM is a proposed quality/cost tradeoff. For anatomy requiring wall thickness and lumen preservation, a surface-only mesh needs additional structure whichever solver is used.

## Dependency and integration decisions

| Dependency | Verified license/status | Decision for this plan |
|---|---|---|
| PositionBasedDynamics | MIT; library for rigid/deformable/fluid methods. Preserve its license and third-party notices. [Repository](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) | Evaluate selected methods in a standalone fixture; do not assume it supplies a complete surgical workflow. |
| iMSTK | Apache-2.0; maintainers state support/development discontinued 2025-05-02. [Repository notice](https://github.com/Kitware/iMSTK) | Study examples or deliberately maintained pinned code; no dependency on future upstream fixes. Retain license/NOTICE and audit transitive dependencies if adopting code. |
| SofaUE5-Renderer | GPL-3.0; README targets UE 5.0.3, Windows, and limited scene control. [Repository](https://github.com/InfinyTech3D/SofaUE5-Renderer) | Blocked from baseline UE runtime: licensing and functionality/version gaps. Do not interpret “full integration coming” as delivered functionality. |
| SofaUnity | Main asset uses Standard Unity Asset Store EULA; README documents older tested Unity releases and Windows. [Repository](https://github.com/InfinyTech3D/SofaUnity) | Fallback experiment only; verify current package price, exact dependencies, source redistribution rights and Unity 6.3 packaged build before adoption. |
| PhysX deformables | Documented FEM deformables use CUDA-compatible GPU hardware. [NVIDIA documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/DeformableBodyOverview.html) | Optional comparison, not portable baseline. Exact version/component license inventory remains **UNVERIFIED** here; not approved for import. |
| NVIDIA Warp | Apache-2.0 Python framework for CPU/GPU kernels. [Repository](https://github.com/NVIDIA/warp) | Optional offline experiment/calibration tool. It does not remove the need to implement, validate and package a tissue model. |
| CHAI3D | Core BSD-3-Clause; preserve notices/disclaimers and avoid implied endorsement. External modules can differ. [License](https://www.chai3d.org/download/license), [module warning](https://www.chai3d.org/download/doc/html/chapter21-license.html) | Optional device abstraction after a physical haptic device is selected. |
| OpenHaptics | Vendor SDK exists; redistribution/license terms were not established from its product page. [Official page](https://www.3dsystems.com/haptics-devices/openhaptics) | **UNVERIFIED** for distribution; no download/package assumption or claim that device/SDK access is free. |

A stable C ABI around small data types can preserve solver code across engines, but switching still requires new input, rendering, materials, build, asset and UI integrations. Portability reduces exposure; it does not make migration cheap.

## Proposed surgical interaction strategy

All choices in this section are **proposed abstractions requiring clinical review**.

| Interaction | First implementation boundary | Evidence to collect before expanding |
|---|---|---|
| Grasp/retract | Local deforming patch with anatomical attachments; explicit grasp/release state, collision shapes and tension limits | Displacement/contact comparison; clinician review of attachment behavior; no instrument tunnelling in bounded tests |
| Incise | Pre-authored cut corridor and controlled topology transitions; newly exposed inner surface carries persistent tissue identity | Continuity of UVs, collision, tissue labels and volume accounting after a cut; review visible wall layers |
| Cannulate/clamp | Vessel lumen/occlusion states and attachment constraints; position/depth checks within supported geometry | Correct downstream perfusion changes; no magical flow through a closed route; clear supported failure states |
| Needle/stitch | Curved needle path through entry/exit anchors; compliant thread; measurable bite placement and edge approximation | Thread cannot teleport across wall; no impossible wall attachment; leak/narrowing response reviewed against task intent |
| Knot | Explicit assisted knot action with recorded tension/state, visibly identified as assistance | Later self-contact/friction knot research must demonstrate reproducible holding/sliding behavior before claiming manual knot realism |
| Heart motion | Authored cycle synchronized to physiological state, with local contact deformation; separate arrest and abnormal-motion states | ECG/mechanical timing coherency; team review of arrest/reperfusion transitions; no automatic normal output after rhythm change |
| Bleeding/suction | Authoritative compartment volumes and flow rates; render particles, pools and wetness from that state | Lost, pooled, suctioned, discarded and returned blood reconcile; visual particle count never determines circulating volume |

Arbitrary cuts require remeshing or alternative topology management, persistent anatomical labels, new collision surfaces and updated constraints. Free knot tying adds difficult self-contact, friction and entanglement. These are multidisciplinary research workstreams, not small shader features. Restricting the first case allows precision and physiological consistency to be tested before enlarging the interaction space.

## Proposed runtime architecture

One simulation clock owns time, event ordering and pause. Player/team commands become timestamped domain events with stable IDs. Tissue interactions emit semantic results such as vessel opening, occlusion, leak area and attachment; physiology consumes these through a documented boundary. The renderer receives immutable snapshots and cannot directly change patient blood volume or bypass state. Monitor displays include their own sampling, delay and signal-quality behavior.

Use meters, seconds, kilograms and explicit conversions at engine boundaries; Unreal scene units need an adapter. Collision, visual and physiological representations share stable anatomical IDs but need not share polygon topology. Version scenario data, units, solver settings, seed and source provenance in saved cases. CPU logic/physiology and local tissue workers should have bounded workloads; GPU work initially handles presentation. Avoid synchronous GPU readback in a time-critical interaction path.

Record commands plus periodic snapshots for debrief. Do not promise cross-platform bitwise determinism for floating-point, multithreaded or GPU physics. Validate repeatability within stated tolerances on a pinned build; use snapshot-based replay when necessary. If overloaded, degrade secondary visual effects first. Do not silently slow physiological time or lose critical events.

## Performance, VR and haptics

**Proposed targets, not measurements:** desktop 1080p at 60 frames/s gives 16.67 ms/frame. Initial allocation: GPU presentation p95 below 12 ms; CPU main-thread p95 below 6 ms; tissue worker below 4 ms per 120 Hz update, subject to measured convergence. CPU/GPU work overlaps, so these are separate budgets, not additive promises. Hardware is not yet chosen; record CPU, GPU, RAM, driver, resolution and quality settings before every benchmark. Track p95/p99, worst stalls and memory growth across a 30-minute representative session.

Optional PC VR at 90 Hz allows 11.11 ms/frame and needs a separate stereo render/input budget. OpenXR provides a common XR API, not universal extension support, precision guarantees or automatic portability. Test the actual headset/runtime/controller combination. Standalone mobile VR is deferred because it would require another content and performance target. [Khronos OpenXR](https://www.khronos.org/openxr/)

Force-feedback haptics require a separate high-rate servo and device-specific stability limits; CHAI3D examples separate a greater-than-1 kHz haptic thread from graphics. A simplified local contact proxy and bounded force output should survive missed simulation updates. Never place the full organ solve, allocations, logging or blocking engine calls in that loop. Controllers/optical hands lack equivalent physical resistance; score and assistance profiles must identify the input method. [CHAI3D example architecture](https://www.chai3d.org/download/doc/html/chapter5-example.html)

## Experiments before production commitment

Time boxes below are planning estimates for an experienced developer, not delivery commitments. Run in sequence where dependencies require it.

1. **License/build gate, 3–5 working days:** package a clean UE desktop scene using one cleared anatomy derivative and original tool; record exact engine/toolchain/dependency versions and license manifest. Failure changes the asset/engine decision before content production.
2. **Interaction gate, 2–4 weeks:** one vessel patch, grasp/retract, authored incision, one stitch and assisted knot. Measure penetration, numerical drift, placement repeatability and supported failure responses over repeatable stress cases. A visually plausible video alone does not pass.
3. **Coupling gate, 1–2 weeks:** controlled bleeding, occlusion and suction drive physiological compartments and monitor snapshots. Pass conservation/unit tests and pause/resume replay; use expert-approved scenarios from physiology research.
4. **Presentation/performance gate, 1–2 weeks:** representative OR lighting, close-up tissue, two tools, monitor and blood effects. Pass measured budgets on agreed hardware with a 30-minute soak; reduce visual or interaction scope if needed.
5. **Fallback gate, only if triggered:** implement the same interaction fixture in Unity with the same acceptance tests. Select by correctness, maintainability, licensing and development effort, not screenshots alone.
6. **VR/haptic gates, later:** device-specific latency, force stability and usability trials; pass independently before either becomes a promised release feature.

## Search log, corrections and remaining uncertainty

Queries included official Unreal release/licensing and Chaos Flesh capability; Unity 2026 pricing/LTS/physics; Godot download/license/SoftBody3D; SOFA bridge/license; XPBD/substeps; NVIDIA deformables; CHAI3D/OpenHaptics; OpenXR. Primary documentation, author papers and maintainer repositories were opened; search snippets alone were not used to approve a runtime dependency.

This refresh removes the previous draft's unsupported certainty about a universal custom tissue engine, universal solver stability, SOFA as ground truth, measured-looking performance counts, cheap engine migration and best-value haptic hardware. It also makes the Unreal/CC BY-SA/GPL compatibility issue explicit. Exact patch compatibility, distribution entitlements for optional SDKs, actual hardware, organ material data, unrestricted cuts and knot physics remain unresolved. The first milestone must close these uncertainties with evidence; no medical accuracy or real-time performance has been demonstrated by this planning work.
