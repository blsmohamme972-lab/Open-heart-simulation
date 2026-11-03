# Research 04: Game engine and simulation technology

> **Purpose:** Pick the engine, physics, rendering, VR and haptics technology for a realistic open heart surgery simulation game. Use evidence, not opinion. The game is personal, non-commercial and educational.
>
> **Researched 2026-11-03 (re-do, fresh searches).** I worked independently from older reports. The shared web-search budget ran out partway through. After that I checked facts by opening known official pages directly (WebFetch). Claims that rest only on a search snippet say "(uncertain - snippet only)".
>
> **Disclaimer:** This is game-design research. It is **not clinical guidance**, and the game is **not** a certified medical device or a validated training simulator. Anatomy and procedure accuracy are covered in Research 01 and 02.
>
> **Evidence grades:** A = primary/authoritative (official docs, license page, peer-reviewed paper). B = reputable secondary (vendor page, university page, review summary, official forum post). C = weak (blog, reseller, search snippet).

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence [links] |
|---|---|---|
| Main engine | **Unreal Engine 5.8** (desktop first, 60 Hz). Optional PC VR at 90 Hz. | UE 5.8 released 17 June 2026 [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/); 5.8 release notes: Chaos Cloth "production ready", OpenXR 1.0 and 1.1 runtimes supported [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) |
| Engine license | Fine for personal use. A 5% royalty applies only after US$1M lifetime gross revenue per product. | [unrealengine.com/license](https://www.unrealengine.com/en-US/license) (uncertain - snippet only, page returned 403); [Wikipedia UE5](https://en.wikipedia.org/wiki/Unreal_Engine_5) |
| Fallback engine | **Unity 6.3 LTS** with URP, plus SofaUnity (SOFA) or an XPBD asset. This is the faster path to ready-made surgical physics. | Unity 6.3 LTS supported to Dec 2027 [Unity 6](https://unity.com/releases/unity-6); SofaUnity has cutting, haptics and VR but is Windows-only [SofaUnity](https://github.com/InfinyTech3D/SofaUnity) |
| Not chosen as main | Godot 4.7: MIT license and Jolt soft bodies. But its rendering is weaker for XR and it has no surgical-sim ecosystem. Use it only for small prototypes. | [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html); [SoftBody3D](https://docs.godotengine.org/en/stable/classes/class_softbody3d.html) |
| Soft-tissue core | Write our own **engine-agnostic C++ XPBD solver**: tetrahedral soft bodies, Cosserat-rod thread, and attachment constraints. Use substeps (n small steps with 1 iteration each). | XPBD [Macklin 2016](https://matthias-research.github.io/pages/publications/XPBD.pdf); substepping [Small Steps](https://mmacklin.com/smallsteps.pdf); a 2026 cardiac anastomosis simulator used Cosserat rods + XPBD in Unity [Liu 2026](https://www.oaepublish.com/articles/2574-1209.2025.103) |
| Off-the-shelf medical physics | **SOFA v26.06** (LGPL) is the only live, maintained open medical-physics framework. **iMSTK is discontinued** (since 2 May 2025). Do not base new work on it. | [SOFA releases](https://github.com/sofa-framework/sofa/releases); [iMSTK GitLab](https://gitlab.kitware.com/iMSTK/iMSTK) |
| Chaos Flesh | Do not use it for cutting. It targets character muscle and uses offline caching, and its docs never mention cutting. Use it only for idle tissue jiggle, if at all. | [Chaos Flesh overview](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview) |
| PhysX 5 deformables | Avoid for cutting. It needs CUDA-style buffers, and topology changes need recooked data. | [PhysX DeformableVolume](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html) |
| Beating heart | Hybrid: a baked beat animation (Blender, then Alembic or morph targets) is the kinematic target. A low-res XPBD soft body is bound to it with weak constraints. Heart rate is driven by the Pulse physiology engine. | Kinematic + weak constraint pattern [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview); PCA morph-target import [UE Alembic](https://dev.epicgames.com/documentation/unreal-engine/alembic-file-importer-in-unreal-engine); Pulse is Apache-2.0 with UE and Unity plugins [Pulse](https://pulse.kitware.com/) |
| Blood | Layered: wet/stain decals and masks, GPU particles, and a small SPH pool rendered as a screen-space fluid. Niagara Fluids 2D only for spurts and smoke. | SPH for surgery sims [Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf); screen-space fluid [NVIDIA GDC 2010](https://developer.download.nvidia.com/presentations/2010/gdc/Direct3D_Effects.pdf); Niagara Fluids warning [UE docs](https://dev.epicgames.com/documentation/unreal-engine/niagara-fluids-in-unreal-engine) |
| Frame budgets | Desktop 60 Hz gives 16.7 ms per frame. PC VR 90 Hz gives 11.1 ms. Keep physics at about 5 ms or less per frame. The haptic loop runs at 1 kHz on its own thread. | iMSTK "< 5 ms per frame" [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156); deformation at 60–100 Hz with haptics at ≥1000 Hz [He 2026](https://doi.org/10.1016/j.cag.2025.104524) |
| Standalone Quest 3 | Not a target for the full simulation. At most a light demo. | Quest 3 limits: 72 Hz min, 13.8 ms, <200 draw calls, <1.5M triangles [Meta](https://developers.meta.com/vr/resources/device-optimization-comparison/); UE physics substepping "not currently supported on mobile" [UE](https://dev.epicgames.com/documentation/unreal-engine/physics-sub-stepping-in-unreal-engine) |
| VR hand tracking | Use it only for coarse actions (menus, grabbing retractors). Use a controller, mouse or haptic stylus for needle work. | Quest 3 hand-tracking error is 1.73 cm in the best case, motion-to-photon 38 ms [Godden 2025](https://doi.org/10.1109/TVCG.2025.3549182) |
| Haptics (optional tier) | Abstract the device behind CHAI3D-style interfaces (CHAI3D is BSD-3). Entry device: 3D Systems Touch (3.3 N, 1 kHz). Better: Haply Inverse3 (4 kHz, 0.01 mm). | [Touch specs](https://www.3dsystems.com/haptics-devices/touch); [Inverse3](https://www.haply.co/inverse3); [CHAI3D license](https://www.chai3d.org/download/license) |

---

## 1. Engine comparison (state as of November 2026)

### 1.1 Current versions

| Engine | Current version found | Date | Source (grade) |
|---|---|---|---|
| Unreal Engine | **5.8** (5.8.1 hotfix mentioned on forum) | Released 17 June 2026 (forum and GameFromScratch). Epic homepage lists 23 June 2026 (uncertain). | [Epic forum](https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274) (B, snippet); [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/) (B); [Wikipedia](https://en.wikipedia.org/wiki/Unreal_Engine_5) (B) |
| Unreal Engine 6 | Not released. Reports say 5.8 is the last UE5 release, with UE6 previews "late 2027ish". | — | (uncertain - snippet only) [Epic forum search snippet](https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274) |
| Unity | **6.3 LTS** is the current LTS (support to Dec 2027). Unity 6.0 LTS support ended Oct 2026. | 6.3 LTS: late 2025 | [Unity 6 releases](https://unity.com/releases/unity-6) (A) |
| Unity (tech stream) | 6.4 (19 Mar 2026) and 6.5 (16 Jun 2026). 6.6 is the newest "Supported" release. 6.7 LTS is in beta, expected end of 2026. Unity 7 is in alpha. | — | [issoh.co.jp blog](https://www.issoh.co.jp/md/tech/10417) (C, uncertain - snippet only, page 403) |
| Godot | **4.7** stable (4.7.1 on 14 Jul, 4.7.2 on 18 Aug 2026) | 4.7-stable tagged 18 June (year inferred 2026) | [GitHub 4.7-stable](https://github.com/godotengine/godot/releases/tag/4.7-stable) (A); [Godot 4.7 page](https://godotengine.org/releases/4.7/) (A); 4.7.x dates [gamedev.net](https://gamedev.net/news/5172-godot-engine-472-stable-released/) (C, snippet) |

### 1.2 License and cost (personal / non-commercial use)

| Engine | License model | Personal use OK? | Key terms | Source |
|---|---|---|---|---|
| Unreal Engine 5.8 | Epic Unreal Engine EULA (source-available, not open source) | **Yes, free** | 5% royalty on lifetime gross product revenue **above the first US$1M**. Sales in the Epic Games Store are royalty-free. Since Oct 2024 the rate is 3.5% if the game also ships on the Epic Games Store. Non-game companies with >US$1M revenue pay a seat fee of US$1,850 per seat per year (from April 2024). | Royalty threshold: [unrealengine.com/license](https://www.unrealengine.com/en-US/license) (A, but **uncertain - snippet only**, 403 on fetch); 3.5% and seat fee: [Wikipedia UE5](https://en.wikipedia.org/wiki/Unreal_Engine_5) (B) |
| Unity 6 Personal | Unity Editor Software Terms | **Yes, free** | Personal plan: "available to customers with up to $200,000 in revenue and funding". "Splash screen optional with Unity 6". Pro costs **$2,310/yr per seat** (or $210/month) after a 5% rise from **12 Jan 2026**. Runtime Fee cancelled 12 Sep 2024. **Havok Physics for Unity is no longer included** from Unity 6.3. | [Unity pricing updates](https://unity.com/products/pricing-updates) (A) |
| Godot 4.7 | **MIT (Expat)** | **Yes** | You can use it for any purpose. When you redistribute it, include the copyright and license notice; a link to godotengine.org/license in the credits is enough. Your game content is yours. | [Godot license](https://godotengine.org/license/) (A) |

**Takeaway:** All three engines are free for this project. None of them is a cost blocker.

### 1.3 Physics, soft bodies and fluids built into each engine

| Capability | Unreal 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| Rigid physics | Chaos (replaced PhysX in UE5) [Wikipedia](https://en.wikipedia.org/wiki/Unreal_Engine_5) | Built-in 3D physics is "an integration of the Nvidia PhysX engine" [Unity docs](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview). Havok was removed from paid plans in 6.3 [Unity](https://unity.com/products/pricing-updates) | Jolt is the default for new 3D projects since 4.6 [GameFromScratch](https://gamefromscratch.com/godot-4-6-released/) (C, snippet) |
| Volumetric soft bodies | **Chaos Flesh**: tetrahedral FEM-style deformables for "character muscle deformation". It simulates "low-resolution geometry at runtime" plus "cached results from an offline simulation". Tet meshing uses iso-surface stuffing, TetWild or a radial method. A Solver Actor controls "sub-stepping, threading models". [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview). In 5.8: "Procedural interactions between layers (fat, muscle, skeletal)" and "major performance and simulation updates" [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes); [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/) | None built in. The docs list only Cloth as a deformable [Unity docs](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview). Needs third-party tools (SofaUnity, Obi, iMSTK-Unity). | `SoftBody3D` (surface or volume soft body; `simulation_precision` defaults to 5). The docs say Jolt's soft body is "faster and more reliable" than GodotPhysics3D [Godot docs](https://docs.godotengine.org/en/stable/classes/class_softbody3d.html). Jolt soft bodies support edge, dihedral-bend, **Cosserat rod**, tet-volume and long-range attachment constraints [Jolt](https://github.com/jrouwe/JoltPhysics) |
| Cutting or tearing of soft bodies | Not mentioned in the Chaos Flesh docs [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview) | Third-party only (SofaUnity has "cutting and carving" examples [SofaUnity](https://github.com/InfinyTech3D/SofaUnity)) | Not provided |
| Cloth (drapes, gauze) | Chaos Cloth is "production ready" in 5.8 [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) | Cloth component [Unity docs](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview) | SoftBody3D used as cloth [Godot docs](https://docs.godotengine.org/en/stable/classes/class_softbody3d.html) |
| Fluids | Niagara Fluids: "2D templates for games and 3D templates for cinematics". Warning: "Fluids scenes can be graphically intensive, and may result in a GPU crash on Windows". Recommends baking to flipbooks [Niagara Fluids](https://dev.epicgames.com/documentation/unreal-engine/niagara-fluids-in-unreal-engine) | VFX Graph particles. Fluids need third-party tools (for example Obi Fluid [Obi](https://obi.virtualmethodstudio.com/)) | GPU particles only; fluids need custom compute (compute shaders only in Forward+ / Mobile [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html)) |
| Physics substepping | Yes on desktop. "Not currently supported on mobile devices" [UE substepping](https://dev.epicgames.com/documentation/unreal-engine/physics-sub-stepping-in-unreal-engine) | Fixed timestep (standard) | `physics_ticks_per_second` (standard; not re-verified here) |

### 1.4 Rendering (wet tissue, skin, blood)

| Feature | Unreal 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| Global illumination | Lumen (software and hardware ray tracing) [Wikipedia](https://en.wikipedia.org/wiki/Unreal_Engine_5); **Lumen Lite** new in 5.8 for lower-end hardware [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/) | HDRP (high end) or URP | SDFGI and VoxelGI, **Forward+ only** [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html) |
| Many dynamic lights (OR lamps) | **MegaLights** is production-ready in 5.8 [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/) | — | Forward+: 512 lights per cluster [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html) |
| Subsurface scattering (tissue) | Substrate materials (since 5.2) [Wikipedia](https://en.wikipedia.org/wiki/Unreal_Engine_5) | HDRP: yes. **HDRP does not list Android/Quest** and "doesn't support OpenGL or OpenGL ES devices" [HDRP requirements](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/System-Requirements.html) | SSS, SSR and TAA are **Forward+ only** [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html) |
| High-poly anatomy | Nanite: clusters of up to 128 triangles, streamed [Wikipedia](https://en.wikipedia.org/wiki/Unreal_Engine_5) | Standard LOD | Standard LOD |
| Render pipeline churn | — | SRP "Compatibility Mode" was planned for full removal in 6.4; custom passes must use Render Graph [Unity forum, staff post 12 Sep 2025](https://discussions.unity.com/t/planned-breaking-changes-in-unity-6-4/1682100) | — |

**Takeaway:** Unreal has the strongest out-of-the-box realism for wet, lit tissue. Godot's best features (SSS, SSR) live in Forward+. But Godot recommends the **Mobile** renderer for XR [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html), so realism drops in VR.

### 1.5 VR support

| Item | Unreal 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| OpenXR | "OpenXR 1.0 and 1.1 runtimes are supported", bundled OpenXR 1.1.46. Steam Frame support is experimental. OpenXR stereo-layer underlays. [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) | OpenXR plugin. XR Hands 1.5.1: "the OpenXR package is the only plug-in provider that supports hand tracking" [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html). HoloLens 2 dropped in 6.4 [Unity forum](https://discussions.unity.com/t/planned-breaking-changes-in-unity-6-4/1682100) | Built-in OpenXR. 4.7 adds "day one production-ready support for Android XR and Steam Frame". "We now recommend new XR projects use the Mobile renderer" [Godot 4.7](https://godotengine.org/releases/4.7/) |
| Hand tracking | Via OpenXR / Meta plugin | XR Hands + Meta Aim Hand [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html) | Hand interaction profile with pinch, grasp and poke; XRHandTracker joint data [Godot hand tracking](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html) |

### 1.6 C++ plugin integration (to embed our physics core or SOFA)

| Engine | How | Source |
|---|---|---|
| Unreal | `.Build.cs` module with `Type = ModuleType.External`. Static libs go in `PublicAdditionalLibraries`. DLLs use `PublicDelayLoadDLLs` and are staged with `RuntimeDependencies.Add`. Guidance covers `THIRD_PARTY_INCLUDES_START/END` and RTTI mismatches. **This is the most direct path, because the engine itself is C++.** | [UE third-party libraries](https://dev.epicgames.com/documentation/unreal-engine/integrating-third-party-libraries-into-unreal-engine) (A) |
| Unity | Native plugin (C ABI DLL) called from C# via P/Invoke. This is the pattern SofaUnity uses ("SofaVerseAPI DLL"). | [SofaUnity](https://github.com/InfinyTech3D/SofaUnity) (A) |
| Godot | GDExtension. 4.7 adds "a dedicated section for GDExtensions" in Project Settings. | [Godot 4.7](https://godotengine.org/releases/4.7/) (A) |

---

## 2. Soft-tissue simulation libraries and methods

### 2.1 Library comparison (versions, licenses, status)

| Library | Version / date | License (exact) | Personal use | Attribution / share-alike | Engine bridges | Status | Source |
|---|---|---|---|---|---|---|---|
| **SOFA Framework** | **v26.06.00**, published 15 Jul 2026 (news post 21 Jul 2026). Previous: v25.12.00 (5 Feb 2026), v25.06.00 (24 Jul 2025). | "SOFA is LGPL, except: applications/projects (GPL), applications/tutorials (GPL)". LGPL means 2.1 "or (at your option) any later version". | Yes | LGPL: keep notices. If you modify SOFA itself, share those changes. Dynamic linking from a closed game is allowed. No NoDerivatives clause. | SofaPython3; SofaUnity; SofaUE5 (visual only) | **Active** (2 releases per year) | [Releases](https://github.com/sofa-framework/sofa/releases) (A); [README license section](https://github.com/sofa-framework/sofa) (A); [sofa-framework.org](https://www.sofa-framework.org/) (A) |
| SofaPython3 | Ships with SOFA. v25.12 builds use Python 3.12 (plus a 3.10 Linux build). NumPy >2.0 supported since v25.12. | LGPL-2.1 (third-party listing) | Yes | LGPL | — | Active | [SofaPython3 docs](https://sofapython3.readthedocs.io/en/latest/_sources/content/Installation.rst.txt) (B, snippet); license (uncertain - third-party listing) [code.gouv.fr](https://repos.ecosystem.code.gouv.fr/hosts/GitHub/repositories/sofa-framework%2FSofaPython3/dependencies) (C) |
| **SofaUnity** (InfinyTech3D) | No GitHub release tag listed. Supports SOFA >23.06 and Unity >2020.3 (tested 2020.3.17, 2021.3.19). A user reports running SofaUnity-URP v25.12 on Unity 6000.0.51f1 (Python scenes crashed because of a python313 vs python312 DLL mismatch). | "Standard Unity Asset Store EULA" (other licenses on request). Bundles LGPL SOFA DLLs. | Yes | Asset Store EULA: embed only, no standalone redistribution | Unity | Active-ish. **"Only tested on Windows for now."** | [SofaUnity](https://github.com/InfinyTech3D/SofaUnity) (A); [Discussion #273](https://github.com/InfinyTech3D/SofaUnity/discussions/273) (C, snippet) |
| SofaUE5-Renderer | Requires UE 5.0.3 and SOFA ≥22.12. **Visual only**: "two-way communication is not yet available". | **GPL-3** (commercial license on request) | Yes, but GPL-3 forces your whole game to be GPL if you distribute it | Share-alike (GPL) | Unreal | Old. A Kickstarter for a new open-source SOFA-UE5 plugin was posted 19 Nov 2025; its status is unknown. | [SofaUE5-Renderer](https://github.com/InfinyTech3D/SofaUE5-Renderer) (B, **uncertain - snippet only**); [UE forum Kickstarter post](https://forums.unrealengine.com/t/bringing-sofa-physics-engine-biomechanical-simulation-to-unreal-engine-5-kickstarter-now-live/2676465) (B) |
| SOFA Cosserat plugin | No release tags | **LGPL-3.0** | Yes | LGPL | SOFA | Active repo (523 commits) | [SofaDefrost/Cosserat](https://github.com/SofaDefrost/Cosserat) (A) |
| **iMSTK** (Kitware) | Last tag **v7.0.0** (commit 14 Sep 2023). iMSTK-Unity 2.0 (30 Oct 2023) is based on v7.0. | **Apache 2.0** | Yes | Attribution (NOTICE); no share-alike | Unity asset; Unreal is possible via C++ | **DISCONTINUED**: "Support and development … has been discontinued as of May-02-2025." The GitLab group is marked "(ARCHIVED)". | [iMSTK README via GitLab](https://gitlab.kitware.com/iMSTK/iMSTK) (A); [Unity 2.0](https://www.kitware.com/imstk-unity-2-0-released/) (B) |
| NVIDIA PhysX SDK 5 | 5.x. The GitHub page lists "PhysX SDK 5.12.0" (as the ovphysx 0.7 compatibility entry; uncertain whether this is the newest standalone SDK). | **BSD-3-Clause** | Yes | Attribution | Unity (built-in PhysX); standalone | Active | [PhysX GitHub](https://github.com/NVIDIA-Omniverse/PhysX) (A) |
| PhysX deformable volume (old name "FEM soft body") | Renamed in 5.5: `PxSoftBody` became `PxDeformableVolume`. A new "Deformable Surface" was added for cloth and shells. | BSD-3 | Yes | Attribution | — | Active, but API churn | [Migration 5.4 to 5.5](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/MigrationTo55.html) (A) |
| **Jolt Physics** | No version shown on the page | **MIT** | Yes | Keep the notice | Godot (default), Source mod, 2 UE plugins | Active (used in Horizon Forbidden West, Death Stranding 2) | [Jolt](https://github.com/jrouwe/JoltPhysics) (A) |
| NVIDIA Warp | 1.19.x mentioned (Windows-on-Arm wheels began at 1.19.0). Needs CUDA 13 wheels, R580+ driver, Turing+ GPU. macOS is CPU only. | **Apache-2.0** | Yes | Attribution | Python (not a game runtime) | Active | [Warp](https://github.com/NVIDIA/warp) (A) |
| Newton | Built on Warp; Linux Foundation project (contributed 29 Sep 2025) | Code **Apache-2.0**, docs **CC-BY-4.0** | Yes | Attribution for docs | Python, robotics-focused (MuJoCo-Warp, VBD, MPM) | Active | [Newton](https://github.com/newton-physics/newton) (A); [Linux Journal](https://www.linuxjournal.com/node/1341367) (C, snippet) |
| PositionBasedDynamics (Bender) | No version shown | **MIT**: "free even for commercial applications" | Yes | Keep the notice | C++ library | Reference code | [PBD library](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) (A) |
| SPlisHSPlasH (SPH) | No version shown | **MIT** | Yes | Keep the notice | C++ library (GPU neighbor search only) | Reference code | [SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) (A) |
| Vega FEM | **UNVERIFIED** (the host barbic.usc.edu was not reachable from this session's network). From memory it is BSD-3 v4.0, but I could not confirm that. | UNVERIFIED | — | — | — | Probably unmaintained (uncertain) | barbic.usc.edu must be allowed in the session's network settings to verify |
| Obi (Rope / Softbody / Cloth / Fluid) | Version not shown on the site. Softbody uses an "advanced oriented-particle XPBD solver"; Rope is "tearable/cuttable". | Unity Asset Store EULA (price UNVERIFIED) | Yes | Embed only | Unity | Commercial asset | [Obi site](https://obi.virtualmethodstudio.com/) (B); [Asset Store EULA](https://unity.com/legal/as-terms) (A) |
| Pulse Physiology Engine | **4.4.0** (Aug 2026). Adds an **ECMO device with venovenous and venoarterial cannulation**. | **Apache 2.0** | Yes | Attribution | UE plugin (Actor Component) and free Unity asset | Active | [Pulse](https://pulse.kitware.com/) (A); [Pulse versions](https://pulse.kitware.com/version.html) (A) |

### 2.2 Methods: what each solves and what it costs

| Method | Strength | Weakness for heart surgery | Evidence |
|---|---|---|---|
| Mass-spring | Very fast and simple. Over 100K masses at 1000 Hz on a 2010-era GPU (Tesla C2050). | Inaccurate under large strain. Hard to tune to real material values. | [Etheredge 2013, JCGT](https://jcgt.org/published/0002/02/03/) (A); "mass-spring or linear FEM … suffer from inaccuracies under large strains or rotations" [Stanford](https://sr.stanford.edu/?p=343) (B, snippet) |
| Linear / corotational FEM | Physically based. Corotation fixes rotation artifacts. PhysX uses a "fixed corotated model". | Needs implicit solvers. Topology changes (cuts) force a matrix or preconditioner update. | [PhysX DeformableVolume](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html) (A); Courtecuisse 2014 uses "implicit time integration of a non-linear finite-element model" with an "asynchronous update at low frequency" preconditioner, updated on cuts [HAL](https://hal.archives-ouvertes.fr/hal-01097108) (A, abstract snippet) |
| Precomputed / reduced FEM, neural surrogates | Very fast at runtime | "cannot handle topological changes such as cutting" | [Nguyen 2020 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A) |
| **XPBD** | Fixes "iteration count and time step dependent constraint stiffness" in PBD. Unconditionally stable. Easy to add constraints (volume, FEM, rods, attachments). | It is an approximation. Needs substeps to stay stiff. | [XPBD paper](https://matthias-research.github.io/pages/publications/XPBD.pdf) (A) |
| **XPBD with substeps** | "Performing a single large time step with n constraint solver iterations is less effective than computing n smaller time steps, each with a single constraint solver iteration." | More collision checks per frame | [Small Steps, Macklin et al.](https://mmacklin.com/smallsteps.pdf) (A) |
| PBD mesh-free cutting | Cutting without remeshing; includes electrocautery heat diffusion | Older approach (built on NVIDIA Flex) | [Berndt 2017, IEEE CG&A 37(3):24–31](https://katalog.dhi-paris.fr/vufind/Record/NLM271455039) (B, abstract) |
| SPH fluids | Good for interactive blood. The 2003 paper names "virtual surgery simulators" as a target and was interactive with "up to 5000 particles" (2003 hardware). | Surface reconstruction is costly | [Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf) (A) |

### 2.3 What published surgical simulators actually achieve

| System / paper | Model | Size | Rate | Hardware | Source |
|---|---|---|---|---|---|
| iMSTK (hiatal hernia, cholecystectomy; Unity + 2 Touch devices) | XPBD (distance, volume, FEM, dihedral) | 2,485 cells (stomach); 1,295 deformable cells (gallbladder scene); ~2,000 constraints "optimal", ~7,000 before instability | Target "< 5 ms per frame"; haptics "500–1000 Hz" | Laptop i9-12900HK, 32 GB | [Moore et al. 2023, Frontiers in VR](https://doi.org/10.3389/frvir.2023.1130156) (A) |
| VICTAR (Vrest Medical) | GPU volumetric mass-spring | >100K masses | **1000 Hz** | NVIDIA Tesla C2050 | [Etheredge 2013](https://jcgt.org/published/0002/02/03/) (A) |
| Courtecuisse et al. | GPU FEM | — | 1.4 FPS on CPU vs **46.15 FPS on GPU** | GPU | via [Nguyen 2020 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A) |
| Cotin et al. (liver) | Hybrid precomputed FEM + mass-tensor | ~6,500 tets; 760 vertices at 40 Hz | 500 Hz haptics, 40 Hz model | — | [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A) |
| Joldes et al. (brain) | TLED FEM | 15,050 elements / 16,710 nodes | 1 kHz haptics | — | [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A) |
| Energy-based haptic rendering (2026) | GPU deformation with shape constraints + energy virtual coupling | — | Deformation **60–100 Hz**, haptics **≥1000 Hz** on a separate thread | GPU | [He et al. 2026, Computers & Graphics 134:104524](https://doi.org/10.1016/j.cag.2025.104524) (A, abstract) |
| **VR proximal anastomosis for MIDCAB** (most heart-relevant) | **Cosserat rods + XPBD** for vessels **and** sutures | Not reported | Not reported | **Unity3D**, Geomagic Touch | [Liu et al. 2026, Vessel Plus 10:13](https://www.oaepublish.com/articles/2574-1209.2025.103) (A). Validity index 0.78 from 10 surgeons (single-centre, limited validation) |

**Review-level finding:** Only about 65% of the reviewed computational approaches met real-time constraints. Most systems "hardly satisfied both acceptable model accuracy and real-time computation speed" [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A). **Plan implication:** budget for approximation. Do not try for full FEM accuracy.

---

## 3. Hard problems and proven techniques

### 3.1 Mesh cutting (skin incision, pericardiotomy, aortotomy, arteriotomy)

| Technique | How it works | Pros | Cons | Evidence |
|---|---|---|---|---|
| A. Element removal (threshold) | Remove tets or edges whose strain or damage passes a threshold, then rebuild the surface | Simple, robust | Jagged edges and volume loss | iMSTK removes "cells/edges in the geometry when those values exceed a threshold" [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A) |
| B. Element splitting / remeshing + solver update | Split tets along the blade path, then refresh the solver data | Clean cut | Hard to implement. FEM needs a preconditioner update. | [Courtecuisse 2014](https://hal.archives-ouvertes.fr/hal-01097108) (A, abstract) |
| C. Mesh-free PBD cutting | Particles and oriented particles with adaptive skinning | No remeshing | Visual skinning is complex | [Berndt 2017](https://katalog.dhi-paris.fr/vufind/Record/NLM271455039) (B) |
| D. **Scripted incision + local physics** (recommended for a game) | The player draws the cut path. Validate it against a target line (length, depth, angle). Swap in a pre-cut mesh with an XPBD "opening" spring, plus decals. | Predictable and beautiful | Less freedom | Design choice; matches the Chaos Flesh approach of runtime low-res + authored high-res [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview) |

PhysX deformables need recooking: "Runtime topology changes such as tearing or cutting require the precomputed data to be updated" [PhysX docs](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html) (A).

**Recommendation:** Use D for the long skin and sternal incisions. Use B in simplified form (split along a pre-authored "cut-ready" seam of tets) for aortotomy and coronary arteriotomy. Fall back to A for small tears.

### 3.2 Tearing

- Use the XPBD distance/FEM constraint "break" rule: remove the constraint when its strain exceeds a limit. iMSTK lists tearing as a predefined interaction, and its Unity 2.0 asset has a "Tearing Component for line meshes" [Kitware](https://www.kitware.com/imstk-unity-2-0-released/) (B).
- Game rule: excess retraction force or thread tension tears tissue or tears the suture through ("cheese-wiring"). This becomes a scored error.

### 3.3 Suturing, needle and knot tying

| Sub-problem | Proven technique | Evidence |
|---|---|---|
| Thread | **Cosserat rod** (stretch, shear, bend, twist) solved with XPBD. Cosserat constraints are available in the MIT PBD library and in Jolt. | Liu 2026 used Cosserat + XPBD for sutures [Vessel Plus](https://www.oaepublish.com/articles/2574-1209.2025.103) (A); [PBD library](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) (A); [Jolt](https://github.com/jrouwe/JoltPhysics) (A) |
| Thread collision | Continuous collision detection between line meshes (thread-thread, needle-thread) | [iMSTK paper](https://doi.org/10.3389/frvir.2023.1130156) (A) |
| Needle puncture | Detect contact plus tip orientation. Store the puncture point as barycentric coordinates on a surface triangle. Add a constraint that binds the puncture to the needle's tangential motion, so "the needle slide[s] through the punctured tissue". | [iMSTK paper](https://doi.org/10.3389/frvir.2023.1130156) (A) |
| Knot tying | **Not solved even in iMSTK** ("knot detection is planned but not implemented"). | [iMSTK paper](https://doi.org/10.3389/frvir.2023.1130156) (A) |
| Game approach for knots | A gesture or minigame (correct wrap count and direction, tension in a target band), then a scripted knot animation snapped onto the rod | Design choice, because of the gap above |

### 3.4 Tool-tissue collision, retraction and clamping

- **Collision:** Use signed distance fields (SDFs) or capsules for rigid tools against tissue particles. iMSTK uses implicit colliders: level sets and SDFs [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A).
- **Retraction (sternal retractor, pericardial stay sutures):** Use XPBD attachment constraints (Jolt calls them "long-range attachment constraints (tethers)" [Jolt](https://github.com/jrouwe/JoltPhysics)). Drive them with the retractor's opening distance.
- **Vessel clamping (aortic cross-clamp, bulldogs):** Combine (1) a geometry constraint that squeezes the vessel cross-section with (2) a **hemodynamic switch**: zero flow downstream, tied to the physiology model. Pulse is Apache-2.0 with UE and Unity plugins [Pulse](https://pulse.kitware.com/) (A).
- **Two-way rigid/soft coupling:** iMSTK replaced its rigid solver with "PBD rigid" to get "two-way interactions between rigids and deformables" [Kitware](https://www.kitware.com/imstk-unity-2-0-released/) (B). Lesson: put tools and tissue in **one** XPBD solver.

### 3.5 Blood

| Layer | Technique | Cost | Evidence |
|---|---|---|---|
| 1. Wetness, staining, pooling look | Painted masks or decals on tissue (render-target painting), flow maps for trickles | Very low | Standard technique (no single source; uncertain) |
| 2. Spurts and oozing | GPU particles (Niagara or VFX Graph). Niagara Fluids 2D for small spurts; bake to flipbooks where possible. | Low–medium | [Niagara Fluids](https://dev.epicgames.com/documentation/unreal-engine/niagara-fluids-in-unreal-engine) (A) |
| 3. Pooled blood in the field, suction | Small SPH pool (thousands of particles) with suction removing particles | Medium | [Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf) (A); MIT SPH reference [SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) (A) |
| 4. Rendering particle blood | **Screen-space fluid rendering**: depth of particles as sphere sprites, then Gaussian bilateral blur (or curvature flow), then normals from depth, then shade with thickness for absorption | Medium | [NVIDIA GDC 2010](https://developer.download.nvidia.com/presentations/2010/gdc/Direct3D_Effects.pdf) (B), citing van der Laan et al., I3D 2009 |
| 5. Bleeding rate realism | Couple local bleeding to a whole-body physiology model | Low CPU | iMSTK cites Feiger et al. (2020), which couples a local SPH arterial hemorrhage model with a whole-body lumped physiology model [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A) |

### 3.6 The beating heart

| Option | Description | Interaction | Cost | Verdict |
|---|---|---|---|---|
| 1. Baked animation only | Blender keyframes or simulation, exported as Alembic. In UE, import as a **Skeletal Mesh with morph targets compressed by PCA** ("most efficient playback method when vertex count stays constant") or as a Geometry Cache (flipbook). | None (tools pass through) | Very low | Use for distant or background views |
| 2. **Hybrid (recommended)** | Baked beat = kinematic target. A low-res tet XPBD body follows it with **weak constraints**. Tool contacts deform it locally. Playback speed = heart rate from the physiology model. | Good | Low–medium | Same pattern as Chaos Flesh: "Kinematic constraints bind the tetrahedral geometry to the Skeletal Mesh… Weak constraints bind it to the simulation vertices" [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview) (A) |
| 3. Physiology-driven electromechanical FEM | Electrophysiology + active contraction FEM | Full | Far beyond real time for a game | Not recommended (uncertain; no single source fetched) |

UE Alembic limits: only 3- and 4-sided polygons; Geometry Cache has no adjacency buffer [UE Alembic](https://dev.epicgames.com/documentation/unreal-engine/alembic-file-importer-in-unreal-engine) (A).
Simplification: during on-pump surgery with cardioplegic arrest, the heart is still for the main anastomosis phase (domain knowledge; confirm in Research 01/02). So the full beating simulation matters only before cross-clamp and after it is released.

### 3.7 Cannulation (aortic, right atrial) and the bypass circuit

- **Mechanics:** Purse-string suture (needle and thread, section 3.3), then a stab incision (scripted cut D), then cannula insertion. Model the cannula as a rigid capsule with a sliding constraint through the puncture, like iMSTK's needle sliding [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156). Then tighten the tourniquet (snare constraint).
- **Physiology:** Pulse 4.4.0 now has an **ECMO device with VV and VA cannulation** and "dynamic cardiovascular circuit integration" [Pulse versions](https://pulse.kitware.com/version.html) (A). VA-ECMO is not a full cardiopulmonary bypass machine (no venous reservoir or cardioplegia line in that description). Treat it as a **starting point** that may need extension (uncertain).

### 3.8 Sternotomy (bone cutting)

- **Proven research approach:** volumetric bone with a **level set / SDF**. The saw contact is "directly sampled from the level set". The volume is updated and re-rendered by GPU ray casting of only the modified region (iMSTK osteotomy trainer) [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A).
- **Game approach (recommended):** a scripted saw path along the midline with a skill check (alignment, depth, speed), a progressive mesh swap or dissolve mask, bone-dust particles, and sound. Then the sternal retractor opens (attachment constraints).

---

## 4. Haptic devices, SDKs and VR hand tracking

### 4.1 Haptic devices

| Device | Force (max / continuous) | Workspace | Resolution | Rate | DOF (sense / force) | Price | SDK | Source |
|---|---|---|---|---|---|---|---|---|
| **3D Systems Touch** | **3.3 N** / >0.88 N | >431 × 348 × 165 mm | ~0.055 mm (>450 dpi) | USB, **1 kHz** | 6 / 3 | List **US$2,800** at one reseller ("currently unavailable"; uncertain) | OpenHaptics; Unity and Unreal plug-ins | [3D Systems](https://www.3dsystems.com/haptics-devices/touch) (A); [MatterHackers](https://matterhackers.com/store/l/3d-systems-touch-haptic-device/sk/M12PCJ5U) (C) |
| 3D Systems Touch X | **7.9 N** / >1.75 N | >355 × 228 × 180 mm | ~0.023 mm | USB, **up to 4 kHz** | 6 / 3 | Not listed (UNVERIFIED) | OpenHaptics | [3D Systems](https://www.3dsystems.com/haptics-devices/touch) (A) |
| **Haply Inverse3** | "up to 10 N" | Not listed (UNVERIFIED) | **0.01 mm** | **4 kHz** | 3-DOF force | **£5,965.15** (UK reseller, backordered; VAT unclear) | Inverse SDK: local Inverse Service, JSON over WebSocket `ws://localhost:10001`; examples in Python, JS, C++, Rust; Unity package | [Haply](https://www.haply.co/inverse3) (A); [Inverse SDK](https://docs.haply.co/inverseSDK/) (A); [Vertical Realities](https://shop.verticalrealities.com/products/inverse3) (C) |
| Force Dimension omega.3 / .6 / .7 | **12.0 N** (omega.7 gripper 8.0 N) | ∅160 × 110 mm | <0.01 mm | USB 2.0, **up to 4 kHz** | 3 / 3 (omega.7: + gripper force) | Not listed (UNVERIFIED) | Force Dimension SDK **3.17** (3.17.7 files); Windows, macOS (Intel, Apple Silicon), Linux | [omega](https://www.forcedimension.com/products/omega) (A); [SDK](https://www.forcedimension.com/software/sdk) (A) |

Notes:
- Isaac Lab's Haply integration streams device data over WebSocket at **200 Hz** and defaults `limit_force` to 2.0 N [Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/source/how-to/haply_teleoperation.html) (B, snippet). A WebSocket bridge may be too slow for a stiff 1 kHz loop. **Test the real loop rate before committing** (uncertain).
- The 3D Systems OpenHaptics Unity plugin on the Asset Store is **deprecated** ("no longer available for purchase and will no longer be supported") [Asset Store](https://assetstore.unity.com/packages/tools/integration/3d-systems-openhaptics-unity-plugin-134024) (B, snippet). 3D Systems now lists "HapticsDirect plug-ins available for Unity and Unreal" [OpenHaptics](https://www.3dsystems.com/haptics-devices/openhaptics) (A).

### 4.2 Haptics SDKs

| SDK | Version / date | License | Personal use | Notes | Source |
|---|---|---|---|---|---|
| OpenHaptics (3D Systems) | Version not stated. Windows 10/11 64-bit and Ubuntu 20+. | **UNVERIFIED** (an old article said $950 per commercial seat and free for academics; outdated) | Probably yes (UNVERIFIED) | HapticsDirect for Unity and Unreal | [OpenHaptics](https://www.3dsystems.com/haptics-devices/openhaptics) (A); old pricing [Computerworld](https://www.computerworld.com/?p=1564104) (C, snippet) |
| Force Dimension SDK | 3.17 | **UNVERIFIED** | Ships with device (uncertain) | C/C++; works with CHAI3D, H3D, MATLAB, LabVIEW | [FD SDK](https://www.forcedimension.com/software/sdk) (A) |
| Haply Inverse SDK | Current docs | **UNVERIFIED** | Ships with device (uncertain) | Language-agnostic WebSocket JSON | [Inverse SDK](https://docs.haply.co/inverseSDK/) (A) |
| **CHAI3D** | **3.3** latest listed (date not shown; older 3.2.0, 3.1.1, 3.0.0) | **Revised BSD (3-clause)**: "allows unlimited redistribution for any purpose" | Yes | Attribution; no share-alike. Supports Force Dimension and 3D Systems devices plus a custom device template. | [CHAI3D license](https://www.chai3d.org/download/license) (A); [Releases](https://www.chai3d.org/download/releases) (A); [chai3d.org](https://www.chai3d.org/) (A) |
| H3DAPI / HAPI | **2.4.0**, released 29 Apr 2019 | **GPL-2.0** | Yes | **Share-alike** (GPL infects distribution). Stale. **Avoid.** | [H3DAPI GitHub](https://github.com/SenseGraphics/h3dapi) (A) |

### 4.3 Haptic loop rate: why 1 kHz

- "Force to be streamed real-time at a minimum rate of 1000 Hz … within a maximum time span of 1 ms" [Etheredge 2013](https://jcgt.org/published/0002/02/03/) (A).
- The iMSTK haptic module "must execute at 500–1000 Hz" [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A).
- A review gives "100 Hz to 1000 Hz" as the range for uninterrupted collision feel [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) (A).
- Pattern: deformation runs at 60–100 Hz on the GPU, haptics at ≥1000 Hz on a separate thread, connected by **virtual coupling** [He 2026](https://doi.org/10.1016/j.cag.2025.104524) (A). iMSTK offers "direct coupling and dynamic virtual coupling" [Frontiers 2023](https://doi.org/10.3389/frvir.2023.1130156) (A).
- Stability rule of thumb (Colgate passivity): K ≤ 2B/T, where K is virtual stiffness, B is damping and T is the sample period. A faster loop allows stiffer contact [Basdogan chapter](https://mysite.ku.edu.tr/wp-content/uploads/sites/352/2023/07/VRbookChapter.pdf) (B, uncertain - snippet only).

### 4.4 VR hand tracking for fine motor work

| Metric | Value | Device | Source |
|---|---|---|---|
| Positional error (best conditions) | **1.73 cm** (Quest Pro 1.22 cm) | Quest 3 | [Godden et al. 2025, IEEE TVCG 31(5)](https://doi.org/10.1109/TVCG.2025.3549182) (A) |
| Jitter | 1.11 cm (Quest Pro 1.77 cm) | Quest 3 | same |
| Motion-to-photon latency | **38.33 ± 31.29 ms** | Quest 3 | same |
| Fingertip error | ~1.1 cm (central targets 0.79 cm, peripheral 1.3 cm) | Quest 2 | [Abdlkarim et al. 2023, Behav Res Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC10830632/) (A) |
| Joint angle error / delay | 9.6° / 45.0 ms | Quest 2 | same |
| Meta guidance | Hand tracking "is not intended to replace controllers in all scenarios", especially precision-heavy games. Fast Motion Mode tracks at 60 Hz. | Quest | [Meta hand tracking](https://developers.meta.com/horizon/documentation/unity/unity-handtracking-overview) (A) |

**Conclusion:** A centimetre-scale error is far too coarse for placing a needle at millimetre scale. **Use hand tracking only for coarse actions.** For suturing, use a controller with "precision mode" (scaled motion), a mouse/tablet on desktop, or a haptic stylus.

---

## 5. Performance budgets

### 5.1 Frame budgets

| Target | Frame time | Physics budget (proposed) | Render budget (proposed) | Logic, UI, audio | Source / basis |
|---|---|---|---|---|---|
| Desktop 60 Hz | **16.7 ms** | ≤5 ms (XPBD, all substeps) | ≤9 ms | ≤2 ms | 1000/60. Physics cap from iMSTK "< 5 ms per frame" [Frontiers](https://doi.org/10.3389/frvir.2023.1130156) |
| PC VR 90 Hz | **11.1 ms** | ≤4 ms (async thread) | ≤6 ms (stereo) | ≤1 ms | 1000/90 (proposed split, uncertain) |
| Quest 3 standalone 72 Hz | **13.8 ms** | — | — | — | Meta: 72 Hz minimum, 90 Hz recommended; <200 draw calls; <1.5M triangles; XR2 Gen 2, 8 GB RAM, 2064 × 2208 per eye [Meta comparison](https://developers.meta.com/vr/resources/device-optimization-comparison/) (A) |
| Quest 3 in Unreal | — | — | 200–300 draw calls for a "busy simulation"; 1.3M–1.8M triangles | — | [Meta UE guide](https://developers.meta.com/horizon/documentation/unreal/unreal-debug-android) (A) |
| Haptic loop | **1 ms** (1 kHz) | Contact query + coupling only | — | — | [Etheredge 2013](https://jcgt.org/published/0002/02/03/) (A) |

Quest 3 display: 2,064 × 2,208 per eye, 72/90/120 Hz modes [Meta compare](https://www.meta.com/quest/compare/) (A, uncertain - snippet only).

### 5.2 Physics substeps and element counts (planning values)

| Item | Proposed value | Reasoning / evidence |
|---|---|---|
| XPBD substeps per frame | 8–16 at 60 Hz (dt ≈ 2.1–1.0 ms), 1 iteration each | [Small Steps](https://mmacklin.com/smallsteps.pdf) (A). Exact count to be tuned (uncertain). |
| Heart tet mesh (sim) | 2,000–8,000 tets on CPU (multi-threaded); more on GPU | iMSTK is optimal at ~2,000 constraints on a laptop CPU [Frontiers](https://doi.org/10.3389/frvir.2023.1130156). Reviewed FEM systems used 6,500–30,000 elements [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477). (Planning value, uncertain.) |
| Visual mesh | 50k–300k triangles, skinned to the sim tets | Chaos Flesh pattern: runtime low-res + high-res visual [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview). Fits the Quest triangle caps only at the low end. |
| Suture thread | 60–200 rod segments (planning value, uncertain) | Cosserat rods [Liu 2026](https://www.oaepublish.com/articles/2574-1209.2025.103) |
| SPH blood pool | 2,000–20,000 particles on GPU (planning value, uncertain) | 5,000 particles were interactive in 2003 [Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf) |
| Tet meshing tool | fTetWild (MPL-2.0) offline; or Ten Minute Physics' "Tetrahedralizer for Blender" | [fTetWild](https://github.com/wildmeshing/fTetWild) (A); [Ten Minute Physics #13](https://matthias-research.github.io/pages/tenMinutePhysics/index.html) (B). fTetWild's most complex test needed >32 GB of RAM. |

---

## 6. Recommended stack and fallback stack

### 6.1 Recommended stack (desktop-first realism)

| Layer | Choice | Version | License | Why |
|---|---|---|---|---|
| Engine | Unreal Engine | 5.8 (stay on 5.8.x; UE6 is not due before ~2027) | Epic EULA; royalty only above $1M | Best tissue rendering (Substrate, Lumen, MegaLights, Nanite); native C++; OpenXR 1.1 [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) |
| Physics core | **Own C++ library "HeartSim Core"**: XPBD tets + Cosserat rods + attachment/puncture constraints + SDF tool collision. Built as a UE plugin module. | — | Our own code, built on MIT references (PBD library, Jolt ideas) | One solver for tools, tissue and thread (the iMSTK lesson). No dependency on a discontinued project. Portable to Unity or Godot. [XPBD](https://matthias-research.github.io/pages/publications/XPBD.pdf); [PBD lib MIT](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) |
| Reference / validation | SOFA v26.06 run offline (Python) to compare deformation of test scenes | v26.06.00 | LGPL-2.1+ | A mature, maintained biomechanics reference [SOFA](https://github.com/sofa-framework/sofa/releases) |
| Physiology | Pulse Physiology Engine (UE plugin) | 4.4.0 | Apache 2.0 | Vitals, drugs, hemorrhage, ECMO-style cannulation [Pulse](https://pulse.kitware.com/) |
| Cloth (drapes) | Chaos Cloth | 5.8 | Epic EULA | Production ready [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) |
| Blood FX | Niagara particles + decals + custom SPH compute + screen-space fluid shader | — | Own code; SPH reference MIT | Sections 3.5 |
| Asset pipeline | Blender (GPL; outputs are yours) → fTetWild (MPL-2.0) → UE | — | [Blender](https://www.blender.org/about/license/); [fTetWild](https://github.com/wildmeshing/fTetWild) | Free tools; outputs can be used freely |
| Haptics (optional) | CHAI3D-style device abstraction; device: Touch (entry) or Inverse3 | CHAI3D 3.3 | BSD-3 | [CHAI3D](https://www.chai3d.org/download/license) |
| VR (optional) | PC VR through OpenXR at 90 Hz | OpenXR 1.1 | — | Quest standalone is too constrained [Meta](https://developers.meta.com/vr/resources/device-optimization-comparison/) |

**Main risks and mitigations:**
1. *A custom solver takes time.* Mitigation: start from Ten Minute Physics soft-body tutorials #10 and #12 and the MIT PBD library. Build vertical slices (one pericardium cut, one anastomosis stitch) before scaling up.
2. *Unreal's learning curve and build size.* Mitigation: keep all game logic data-driven; keep the core headless and unit-tested.
3. *Royalty / EULA changes.* Low risk for non-commercial use, but recheck the EULA before any public release (the license page could not be fetched; it returned 403).

### 6.2 Fallback stack (faster to a playable prototype)

| Layer | Choice | Version | License | Why |
|---|---|---|---|---|
| Engine | Unity | 6.3 LTS (support to Dec 2027) | Personal: free under $200k | Most published surgical sims use Unity (iMSTK-Unity, SofaUnity, Liu 2026) [Unity 6](https://unity.com/releases/unity-6) |
| Render | URP (also covers Quest); HDRP only for desktop high-end | — | — | HDRP has no Android/Quest support listed [HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/System-Requirements.html) |
| Physics | SofaUnity + SOFA, **or** Obi Softbody/Rope (XPBD), **or** the same "HeartSim Core" native DLL | SOFA ≥23.06 | Asset Store EULA + LGPL | SofaUnity has cutting/carving, haptics, VR and two-way coupling but is "Only tested on Windows" [SofaUnity](https://github.com/InfinyTech3D/SofaUnity) |
| Physiology | Pulse Unity asset | 4.4.0 | Apache 2.0 | [Pulse](https://pulse.kitware.com/) |

**Risks:** SofaUnity is Windows-only and has had Python DLL version mismatches [Discussion #273](https://github.com/InfinyTech3D/SofaUnity/discussions/273). Unity changed pricing and plans several times (Runtime Fee cancelled 2024; price rise 2026; Havok removed in 6.3) [Unity](https://unity.com/products/pricing-updates). The Unity Asset Store EULA prohibits using assets to train AI/ML without consent [EULA](https://unity.com/legal/as-terms).

### 6.3 Why not Godot 4.7 as the main engine

- Pros: MIT license [Godot](https://godotengine.org/license/), Jolt soft bodies with Cosserat rods [Jolt](https://github.com/jrouwe/JoltPhysics), and GDExtension for C++.
- Cons: SSS, SSR and volumetric fog are Forward+ only, and Godot recommends the Mobile renderer for XR [Godot renderers](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html). It has no surgical-sim ecosystem, no SOFA bridge and no Pulse plugin (Pulse lists only UE and Unity [Pulse](https://pulse.kitware.com/)).
- Use: quick physics prototypes of the C++ core (cheap to iterate).

### 6.4 Why not iMSTK, H3DAPI or PhysX deformables as the base

- iMSTK: discontinued 2 May 2025; last tag v7.0.0 (2023) [GitLab](https://gitlab.kitware.com/iMSTK/iMSTK). Still useful as **readable Apache-2.0 reference code** for needle puncture, suturing and level-set bone cutting.
- H3DAPI: GPL-2.0, last release 2019 [GitHub](https://github.com/SenseGraphics/h3dapi).
- PhysX deformable volumes: CUDA-centred API, renamed in 5.5, and recooking is needed on cuts [PhysX](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html).

---

## Game hooks

| Finding | Game mechanic / data value / rule |
|---|---|
| XPBD compliance α (inverse stiffness) is independent of iteration count [XPBD](https://matthias-research.github.io/pages/publications/XPBD.pdf) | Each tissue type (skin, pericardium, aorta wall, coronary artery, myocardium) gets a **compliance value in a data table**. Designers tune feel without touching code. |
| Constraint break on strain (tearing) [Kitware](https://www.kitware.com/imstk-unity-2-0-released/) | **Tissue-tear error**: over-retraction or too much thread tension tears tissue, which adds bleeding and a score penalty. |
| Needle puncture + sliding constraint [iMSTK](https://doi.org/10.3389/frvir.2023.1130156) | **Bite quality score**: entry angle, depth and exit distance are measured at puncture and exit points (barycentric coordinates) and compared with targets. |
| Knot tying is unsolved in research [iMSTK](https://doi.org/10.3389/frvir.2023.1130156) | **Knot minigame**: throw count, direction and tension band, followed by a scripted knot. |
| Cosserat-rod thread [Liu 2026](https://www.oaepublish.com/articles/2574-1209.2025.103) | Thread tangles, tension readout, and "parachute" anastomosis technique possible (thread slack must be managed). |
| Level-set bone cutting [iMSTK](https://doi.org/10.3389/frvir.2023.1130156) | **Sternotomy skill check**: saw deviation from midline (mm), speed; a deviation over a threshold triggers a complication event. |
| Kinematic + weak constraint heart [Chaos Flesh](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview) | Heart beat speed = Pulse heart rate. Arrhythmia events change the animation clip. A **still heart after cardioplegia** opens the "anastomosis window". |
| Pulse physiology (Apache 2.0) [Pulse](https://pulse.kitware.com/) | Vitals monitor, drug responses, blood loss leading to hypotension. Cross-clamp time and bypass time become scored timers. |
| Pulse ECMO VV/VA cannulation [Pulse versions](https://pulse.kitware.com/version.html) | Prototype **"go on bypass" / "come off bypass"** states (needs extension for full CPB; uncertain). |
| SPH + suction [Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf) | **Field visibility mechanic**: pooled blood hides anatomy. The player must suction. Bleeding rate comes from physiology. |
| Haptics 1 kHz, Touch max 3.3 N [3D Systems](https://www.3dsystems.com/haptics-devices/touch) | Force feedback scaled into the device range. Clamp output to ≤3.3 N (Touch) or ≤10 N (Inverse3). Tissue stiffness maps to a force curve. |
| Hand-tracking error 1.73 cm [Godden 2025](https://doi.org/10.1109/TVCG.2025.3549182) | **Input rule**: hand tracking only for grab/menu. **Precision mode** (scaled motion 1:3 to 1:5, planning value) for suturing with controllers. |
| 60 Hz desktop / 90 Hz VR budgets [Meta](https://developers.meta.com/vr/resources/device-optimization-comparison/) | **Quality presets**: "Desktop Realistic" (60 Hz, high tet count) and "VR" (90 Hz, lower tet count, simpler blood). |
| Only ~65% of reviewed approaches reach real time [Nguyen 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477) | **Design rule**: every heavy effect needs a cheap fallback (baked or decal) selected automatically when frame time exceeds budget. |

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | Unreal Engine 5.8 was released 17 June 2026. | https://gamefromscratch.com/unreal-engine-5-8-released/ | B |
| 2 | In UE 5.8, "Chaos cloth is production ready". OpenXR 1.0 and 1.1 runtimes are supported (OpenXR 1.1.46). | https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes | A |
| 3 | Chaos Flesh targets character muscle, simulating low-res geometry at runtime plus offline-cached high-res results. Its docs do not mention cutting. | https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview | A |
| 4 | The Unreal royalty is 5% of lifetime gross above US$1M; 3.5% if also on the Epic Games Store (since Oct 2024); non-game seat fee $1,850/yr. | https://www.unrealengine.com/en-US/license ; https://en.wikipedia.org/wiki/Unreal_Engine_5 | A (snippet) / B |
| 5 | Unity Personal applies up to $200,000 revenue and funding, with optional splash screen. Pro costs $2,310/yr per seat from 12 Jan 2026. Havok is no longer included from 6.3. | https://unity.com/products/pricing-updates | A |
| 6 | Unity 6.3 LTS is supported until Dec 2027; 6.0 LTS through Oct 2026. | https://unity.com/releases/unity-6 | A |
| 7 | Godot 4.7-stable was tagged 18 June (2026). Godot recommends the Mobile renderer for XR. | https://github.com/godotengine/godot/releases/tag/4.7-stable ; https://godotengine.org/releases/4.7/ | A |
| 8 | Godot SSS, SSR, SDFGI and volumetric fog are Forward+ only. | https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html | A |
| 9 | SOFA v26.06.00 was published 15 Jul 2026. SOFA is LGPL 2.1 or later (apps and tutorials GPL). | https://github.com/sofa-framework/sofa/releases ; https://github.com/sofa-framework/sofa | A |
| 10 | iMSTK was discontinued as of 2 May 2025. It is Apache 2.0, last tag v7.0.0. | https://gitlab.kitware.com/iMSTK/iMSTK | A |
| 11 | SofaUnity is under the Standard Unity Asset Store EULA and only tested on Windows. | https://github.com/InfinyTech3D/SofaUnity | A |
| 12 | SofaUE5-Renderer is GPL-3 and visual-only (no two-way coupling). | https://github.com/InfinyTech3D/SofaUE5-Renderer | B (snippet) |
| 13 | XPBD removes iteration-count and time-step dependence of stiffness. | https://matthias-research.github.io/pages/publications/XPBD.pdf | A |
| 14 | n substeps × 1 iteration beats 1 step × n iterations. | https://mmacklin.com/smallsteps.pdf | A |
| 15 | iMSTK target is < 5 ms per frame; ~2,000 constraints optimal; haptics at 500–1000 Hz. | https://doi.org/10.3389/frvir.2023.1130156 | A |
| 16 | GPU mass-spring reached >100K masses at 1000 Hz on a Tesla C2050. | https://jcgt.org/published/0002/02/03/ | A |
| 17 | Deformation runs at 60–100 Hz on the GPU and haptics at ≥1000 Hz on a separate thread. | https://doi.org/10.1016/j.cag.2025.104524 | A |
| 18 | A 2026 VR CABG proximal-anastomosis simulator used Unity3D, Cosserat rods + XPBD and a Geomagic Touch; validity index 0.78. | https://www.oaepublish.com/articles/2574-1209.2025.103 | A |
| 19 | PhysX deformable volumes use a fixed corotated model; cutting or tearing needs updated precomputed data. | https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html | A |
| 20 | 3D Systems Touch: 3.3 N max, >0.88 N continuous, 1 kHz, ~0.055 mm. Touch X: 7.9 N, up to 4 kHz. | https://www.3dsystems.com/haptics-devices/touch | A |
| 21 | Haply Inverse3: 0.01 mm, 4 kHz, up to 10 N; UK reseller price £5,965.15. | https://www.haply.co/inverse3 ; https://shop.verticalrealities.com/products/inverse3 | A / C |
| 22 | Force Dimension omega.x: 12.0 N, ∅160 × 110 mm, <0.01 mm, up to 4 kHz; SDK 3.17. | https://www.forcedimension.com/products/omega | A |
| 23 | CHAI3D is BSD-3; latest listed release 3.3. H3DAPI is GPL-2.0, last release 2.4.0 (29 Apr 2019). | https://www.chai3d.org/download/license ; https://github.com/SenseGraphics/h3dapi | A |
| 24 | Quest 3 hand tracking: 1.73 cm error, 38.33 ms motion-to-photon (best conditions). | https://doi.org/10.1109/TVCG.2025.3549182 | A |
| 25 | Quest 3 targets: 72 Hz min (90 recommended), 13.8 ms, <200 draw calls, <1.5M triangles. | https://developers.meta.com/vr/resources/device-optimization-comparison/ | A |
| 26 | UE physics substepping is not supported on mobile. | https://dev.epicgames.com/documentation/unreal-engine/physics-sub-stepping-in-unreal-engine | A |
| 27 | Pulse 4.4.0 (Aug 2026) is Apache 2.0, adds ECMO with VV/VA cannulation, and has UE and Unity integrations. | https://pulse.kitware.com/version.html ; https://pulse.kitware.com/ | A |
| 28 | Blender outputs (.blend, renders) belong to the user and can be used commercially. | https://www.blender.org/about/license/ | A |

---

## Sources

1. Unreal Engine 5.8 Released (GameFromScratch) - https://gamefromscratch.com/unreal-engine-5-8-released/ - 5.8 date and feature list (MegaLights, Lumen Lite, Chaos Flesh/Cloth updates).
2. Unreal Engine 5.8 Released (Epic forum) - https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274 - release confirmation, 5.8.1, UE6 timing (snippet).
3. Unreal Engine 5.8 Release Notes - https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes - Chaos Cloth production ready, Chaos Flesh layers, OpenXR 1.1.46, Steam Frame, mobile renderer.
4. Introducing the Chaos Flesh System - https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview - Flesh design, tet meshing, constraints, caching.
5. Niagara Fluids in Unreal Engine - https://dev.epicgames.com/documentation/unreal-engine/niagara-fluids-in-unreal-engine - 2D/3D templates, GPU crash warning.
6. Physics Sub-stepping in Unreal Engine - https://dev.epicgames.com/documentation/unreal-engine/physics-sub-stepping-in-unreal-engine - substepping, not supported on mobile.
7. Integrating Third-Party Libraries into Unreal Engine - https://dev.epicgames.com/documentation/unreal-engine/integrating-third-party-libraries-into-unreal-engine - C++ plugin integration.
8. Alembic File Importer in Unreal Engine - https://dev.epicgames.com/documentation/unreal-engine/alembic-file-importer-in-unreal-engine - PCA morph targets and Geometry Cache for heart beat.
9. Unreal Engine license page - https://www.unrealengine.com/en-US/license - royalty terms (snippet only; 403).
10. Unreal Engine 5 (Wikipedia) - https://en.wikipedia.org/wiki/Unreal_Engine_5 - 3.5% EGS rate, $1,850 seat fee, Nanite and Lumen facts.
11. Changes to Unity subscription plans and pricing - https://unity.com/products/pricing-updates - Personal threshold, Pro price, Havok removal, Runtime Fee cancellation.
12. Unity 6 releases - https://unity.com/releases/unity-6 - 6.3 LTS and 6.0 LTS support periods.
13. Planned breaking changes in Unity 6.4 (Unity staff post) - https://discussions.unity.com/t/planned-breaking-changes-in-unity-6-4/1682100 - SRP Compatibility Mode removal, HoloLens drop.
14. Unity 6.3 Physics overview - https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview - built-in PhysX, Cloth only.
15. HDRP System Requirements - https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/System-Requirements.html - HDRP platforms (no Android/Quest listed).
16. Unity XR Hands 1.5 - https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html - OpenXR hand tracking in Unity.
17. Unity Asset Store EULA - https://unity.com/legal/as-terms - asset use and modification rules, no AI training.
18. issoh.co.jp Unity version article - https://www.issoh.co.jp/md/tech/10417 - Unity 6.4/6.5/6.6/6.7 dates (snippet only, C).
19. Godot 4.7 release page - https://godotengine.org/releases/4.7/ - XR features, Mobile renderer recommendation.
20. Godot 4.7-stable tag - https://github.com/godotengine/godot/releases/tag/4.7-stable - release date 18 June.
21. Godot SoftBody3D docs (4.7) - https://docs.godotengine.org/en/stable/classes/class_softbody3d.html - soft body, Jolt preference.
22. Godot renderers docs - https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html - Forward+ / Mobile / Compatibility features, XR advice.
23. Godot OpenXR hand tracking - https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html - hand interaction profile, pinch/poke.
24. Godot license - https://godotengine.org/license/ - MIT terms.
25. Godot 4.6 Released (GameFromScratch) - https://gamefromscratch.com/godot-4-6-released/ - Jolt default (snippet).
26. Jolt Physics - https://github.com/jrouwe/JoltPhysics - MIT, soft-body constraint types including Cosserat rods.
27. SOFA releases - https://github.com/sofa-framework/sofa/releases - v26.06.00 and prior dates.
28. SOFA GitHub README - https://github.com/sofa-framework/sofa - license section (LGPL 2.1+, GPL exceptions).
29. SOFA website - https://www.sofa-framework.org/ - LGPL statement, v26.06 news.
30. SofaUnity - https://github.com/InfinyTech3D/SofaUnity - license, Windows-only, features.
31. SofaUnity discussion #273 - https://github.com/InfinyTech3D/SofaUnity/discussions/273 - Unity 6 / Python DLL mismatch (snippet).
32. SofaUE5-Renderer - https://github.com/InfinyTech3D/SofaUE5-Renderer - GPL-3, visual-only (snippet).
33. SOFA to UE5 Kickstarter post - https://forums.unrealengine.com/t/bringing-sofa-physics-engine-biomechanical-simulation-to-unreal-engine-5-kickstarter-now-live/2676465 - planned open-source plugin.
34. SofaDefrost Cosserat plugin - https://github.com/SofaDefrost/Cosserat - LGPL-3.0 rods.
35. iMSTK GitLab (README and tags) - https://gitlab.kitware.com/iMSTK/iMSTK - discontinued 2 May 2025, Apache 2.0, v7.0.0.
36. Moore et al. 2023, "The interactive medical simulation toolkit (iMSTK)", Frontiers in VR - https://doi.org/10.3389/frvir.2023.1130156 - XPBD, needle, suturing, level-set bone, performance.
37. iMSTK Unity 2.0 Released - https://www.kitware.com/imstk-unity-2-0-released/ - suturing, tearing component, PBD rigid.
38. NVIDIA PhysX GitHub - https://github.com/NVIDIA-Omniverse/PhysX - BSD-3, SDK 5.12.0 listing.
39. PhysX Migration 5.4 to 5.5 - https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/MigrationTo55.html - soft body renamed to deformable volume.
40. PhysX Deformable Volume docs - https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableVolume.html - corotated model, cutting caveat.
41. NVIDIA Warp - https://github.com/NVIDIA/warp - Apache-2.0, platforms.
42. Newton physics - https://github.com/newton-physics/newton - Apache-2.0 / CC-BY-4.0, solvers.
43. Linux Foundation welcomes Newton (Linux Journal) - https://www.linuxjournal.com/node/1341367 - governance date (snippet).
44. Macklin, Müller, Chentanez 2016, XPBD - https://matthias-research.github.io/pages/publications/XPBD.pdf - compliant constraints.
45. Macklin et al. 2019, Small Steps in Physics Simulation - https://mmacklin.com/smallsteps.pdf - substepping.
46. Ten Minute Physics - https://matthias-research.github.io/pages/tenMinutePhysics/index.html - soft-body, tetrahedralizer and fluid tutorials.
47. Müller, Charypar, Gross 2003, Particle-Based Fluid Simulation for Interactive Applications - https://matthias-research.github.io/pages/publications/sca03.pdf - SPH for surgery sims.
48. Green 2010, Screen Space Fluid Rendering for Games (NVIDIA GDC) - https://developer.download.nvidia.com/presentations/2010/gdc/Direct3D_Effects.pdf - screen-space fluid steps.
49. SPlisHSPlasH - https://github.com/InteractiveComputerGraphics/SPlisHSPlasH - MIT SPH solvers.
50. PositionBasedDynamics library - https://github.com/InteractiveComputerGraphics/PositionBasedDynamics - MIT PBD/XPBD, Cosserat.
51. fTetWild - https://github.com/wildmeshing/fTetWild - MPL-2.0 tet meshing.
52. Blender license - https://www.blender.org/about/license/ - GPL; outputs belong to the user.
53. Etheredge, Kunst, Sanders 2013, "Harnessing the GPU for Real-Time Haptic Tissue Simulation", JCGT 2(2) - https://jcgt.org/published/0002/02/03/ - 100K masses at 1 kHz, 1 ms rule.
54. Nguyen, Ho Ba Tho, Dao 2020, Systematic review, Applied Bionics and Biomechanics - https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477 - rates, element counts, trade-offs.
55. He et al. 2026, "Energy-based haptic rendering for real-time surgical simulation", Computers & Graphics 134:104524 - https://doi.org/10.1016/j.cag.2025.104524 - 60–100 Hz deformation, ≥1 kHz haptics.
56. Courtecuisse et al. 2014, Medical Image Analysis 18(2):394–410 - https://hal.archives-ouvertes.fr/hal-01097108 - FEM cutting with preconditioner update (abstract).
57. Berndt, Torchelsen, Maciel 2017, IEEE CG&A 37(3) - https://katalog.dhi-paris.fr/vufind/Record/NLM271455039 - PBD cutting (record).
58. Liu et al. 2026, VR proximal anastomosis simulator, Vessel Plus 10:13 - https://www.oaepublish.com/articles/2574-1209.2025.103 - Unity3D + XPBD Cosserat + Geomagic Touch.
59. Stanford real-time FEA project page - https://sr.stanford.edu/?p=343 - mass-spring/linear FEM limits (snippet).
60. 3D Systems Touch - https://www.3dsystems.com/haptics-devices/touch - specs.
61. MatterHackers Touch listing - https://matterhackers.com/store/l/3d-systems-touch-haptic-device/sk/M12PCJ5U - $2,800 list price.
62. 3D Systems OpenHaptics - https://www.3dsystems.com/haptics-devices/openhaptics - OS support, HapticsDirect.
63. Unity Asset Store OpenHaptics plugin - https://assetstore.unity.com/packages/tools/integration/3d-systems-openhaptics-unity-plugin-134024 - deprecated (snippet).
64. Computerworld OpenHaptics 3.0 pricing - https://www.computerworld.com/?p=1564104 - old $950 per seat (snippet, outdated).
65. Force Dimension omega.x - https://www.forcedimension.com/products/omega - specs.
66. Force Dimension SDK - https://www.forcedimension.com/software/sdk - SDK 3.17, platforms.
67. Haply Inverse3 - https://www.haply.co/inverse3 - 0.01 mm, 4 kHz, 10 N.
68. Haply Inverse SDK docs - https://docs.haply.co/inverseSDK/ - WebSocket architecture.
69. Vertical Realities Inverse3 - https://shop.verticalrealities.com/products/inverse3 - £5,965.15 price.
70. Isaac Lab Haply teleoperation - https://isaac-sim.github.io/IsaacLab/main/source/how-to/haply_teleoperation.html - 200 Hz WebSocket stream (snippet).
71. CHAI3D license - https://www.chai3d.org/download/license - BSD-3.
72. CHAI3D releases - https://www.chai3d.org/download/releases - version 3.3.
73. CHAI3D home - https://www.chai3d.org/ - device support and features.
74. H3DAPI - https://github.com/SenseGraphics/h3dapi - GPL-2.0, v2.4.0 (2019).
75. Meta device optimization comparison - https://developers.meta.com/vr/resources/device-optimization-comparison/ - Quest 3 budgets.
76. Meta Unreal Android debug guide - https://developers.meta.com/horizon/documentation/unreal/unreal-debug-android - Quest draw-call and triangle ranges.
77. Meta hand tracking overview - https://developers.meta.com/horizon/documentation/unity/unity-handtracking-overview - hand tracking limits.
78. Meta Quest compare - https://www.meta.com/quest/compare/ - Quest 3 resolution and refresh (snippet).
79. Godden, Steedman, Pan 2025, IEEE TVCG 31(5):3025–3034 - https://doi.org/10.1109/TVCG.2025.3549182 - Quest 3 hand-tracking accuracy (via https://ericg5.github.io/ResearchPortfolio/papers/characterization).
80. Abdlkarim et al. 2023, Behavior Research Methods 56(2) - https://pmc.ncbi.nlm.nih.gov/articles/PMC10830632/ - Quest 2 fingertip accuracy.
81. Pulse Physiology Engine - https://pulse.kitware.com/ - Apache 2.0, UE and Unity integrations.
82. Pulse version history - https://pulse.kitware.com/version.html - 4.4.0 (Aug 2026), ECMO.
83. Basdogan et al., haptics book chapter - https://mysite.ku.edu.tr/wp-content/uploads/sites/352/2023/07/VRbookChapter.pdf - 1 kHz rule and passivity (snippet).
84. Obi (Virtual Method) - https://obi.virtualmethodstudio.com/ - XPBD Softbody, cuttable Rope.

---

## Summary

### Key findings
1. **Engines (Nov 2026):** Unreal 5.8 (June 2026, likely the last UE5 release), Unity 6.3 LTS (supported to Dec 2027), Godot 4.7 (June 2026). All are free for this personal project.
2. **No engine ships surgical-grade soft-tissue cutting.** Chaos Flesh is for character muscle with caching. Unity has only Cloth. Godot/Jolt soft bodies have no cutting.
3. **SOFA v26.06 (LGPL)** is the only live open medical-physics framework. Its Unity bridge works on Windows. Its Unreal bridge is GPL-3 and visual-only.
4. **iMSTK is discontinued (2 May 2025)**. Use it only as Apache-2.0 reference code.
5. **XPBD with substeps** is the practical core method. It is used by the most heart-relevant recent simulator (Cosserat rods + XPBD, Unity, 2026).
6. **Published real-time numbers are modest:** about 2,000 constraints optimal on a laptop CPU, a <5 ms physics target, and 60–100 Hz deformation with a ≥1 kHz haptic thread.
7. **Quest 3 standalone is too constrained** for the full simulation. Hand tracking (about 1.7 cm error, 38 ms motion-to-photon) is too coarse for suturing.
8. **Haptics:** Touch (3.3 N, 1 kHz, ~US$2,800 list) is the entry device. Inverse3 (4 kHz, 0.01 mm, ~£5,966) and omega.x (12 N) are the better ones. CHAI3D (BSD-3) is the best open abstraction layer.
9. **Pulse 4.4.0** (Apache 2.0) gives physiology, now including ECMO-style VA/VV cannulation, with UE and Unity plugins.

### Recommendations
- **Main:** Unreal Engine 5.8, desktop 60 Hz first, optional PC VR 90 Hz. Build our own engine-agnostic C++ XPBD core (tets, Cosserat thread, puncture, attachment, SDF tools). Add Pulse for physiology, Chaos Cloth for drapes, a layered blood system, and a hybrid baked + XPBD beating heart.
- **Fallback:** Unity 6.3 LTS (URP) with SofaUnity, Obi, or the same native core.
- Use **scripted-plus-physics** design for incisions, sternotomy and knots. Use full physics for retraction, needle bites, thread and local tissue response.
- Keep **quality presets** and automatic fallbacks to stay inside 16.7 ms (desktop) or 11.1 ms (VR).
- Make haptics an **optional tier** behind a device abstraction.

### Open questions
1. Exact Unreal EULA text as of Nov 2026 (the license page returned 403). Recheck before any public release.
2. Whether the SOFA-UE5 Kickstarter plugin shipped, and under what license.
3. Real loop rate of the Haply Inverse SDK through WebSocket in a game loop (is it 1 kHz or more?).
4. Current OpenHaptics, Force Dimension SDK and Haply SDK license terms and prices (UNVERIFIED).
5. Vega FEM license and version (host not reachable; UNVERIFIED).
6. Chaos Flesh status label (Experimental / Beta / Production) in 5.8. The docs do not say.
7. Achievable tet count for our XPBD core with cutting on a mid-range PC. This needs a benchmark spike.
8. Whether Pulse's ECMO model can be extended to a full cardiopulmonary bypass circuit (reservoir, cardioplegia, vent).
9. Unity 6.6 / 6.7 LTS / Unity 7 status (single weak source).

*Method note: the shared web-search budget was used up partway through this research. Later facts were checked by opening known official URLs directly. Some pages (unrealengine.com, Khronos registry, fab.com, MDPI, HAL) returned 403 or bot blocks. Claims from those pages are marked "snippet only". The host barbic.usc.edu was not reachable from this session's network.*
