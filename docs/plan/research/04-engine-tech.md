# Research 04: Game engine and simulation technology

> Part of Step 1 (research) of the planning process. **No game code yet.** This file feeds plan section 4 ("Technical architecture and engine choice") and parts of sections 7 and 9.
> Research date: 2026-11-03. Sources are cited inline. **(uncertain)** marks claims I could not fully verify. **UNVERIFIED** marks licenses I could not confirm from a primary source.
> Scope: personal, non-commercial, educational game. It is not a certified medical device.
> Note: the per-session web-search budget ran out near the end of this research. A few items are therefore flagged as "from prior knowledge, not re-verified in this session".

---

## 0. Summary for the plan

1. **Engine: Unreal Engine 5.8 (pinned).** UE 5.8 shipped on 17 June 2026 and is "the last planned major UE5 release" ([Epic news](https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available), [GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/)). UE6 Early Access is targeted for **end of 2027** ([State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show)), so 5.8 is a stable base for about 2 years. It is free for personal use. It has the best rendering of the three engines for wet, translucent tissue and for a believable OR, it has MetaHumans for the OR team, it is native C++ (so medical-simulation C++ libraries plug in directly), and it supports OpenXR 1.0/1.1 for PC VR.
2. **No engine's built-in soft-body system is good enough for surgery.**
   - **Chaos Flesh** (UE) is built for character muscle deformation, with runtime low-res simulation plus offline caches. It documents **no cutting** ([Epic docs](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview)).
   - **Unity** ships only PhysX rigid bodies and Cloth ([Unity 6.3 manual](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview)).
   - **Godot's SoftBody3D** is basic and has no cutting ([Godot 4.7 docs](https://docs.godotengine.org/en/stable/tutorials/physics/soft_body.html)).
3. **Build an engine-agnostic C++ "TissueCore" on XPBD.** It covers soft tissue, cutting, tearing, suturing thread, needle insertion, grasping and retraction. This is the approach the recent surgical-simulation literature converges on, for example iMSTK ([Moore et al. 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)) and the 2025 CABG IMA-harvest simulator ([Wang et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)). Keeping it out of the engine also makes the fallback engine (Unity) cheap to switch to.
4. **iMSTK was discontinued on 2 May 2025.** Its README carries a "SUNSET NOTICE" ([Kitware/iMSTK on GitHub](https://github.com/Kitware/iMSTK); latest tag v7.0.0). It remains **Apache-2.0**, which makes it excellent reference code to study and borrow from (suturing, needle insertion, PBD + haptics, SPH bleeding coupled to Pulse). It should **not** be a runtime dependency.
5. **SOFA (LGPL-2.1+, v26.06.00, actively developed)** is the gold-standard open FEM framework for surgical simulation. Use it **offline**, as the accuracy reference for calibrating TissueCore's XPBD stiffness values. Its Unreal bridge is only a GPL-3 render-only plugin targeting UE 5.0.3 ([SofaUE5-Renderer](https://github.com/InfinyTech3D/SofaUE5-Renderer)), so it is not usable as the runtime.
6. **Blood is layered, not "one fluid simulation":**
   - physiology-driven bleed rate (from Pulse)
   - GPU particles for jets and drips, timed to the arterial pressure waveform
   - a pooled-volume level in the pericardial well
   - a painted wetness/blood mask on tissue
   - optional small-scale SPH with screen-space rendering for close-up pooling ([Müller 2003](https://matthias-research.github.io/pages/publications/sca03.pdf), [van der Laan 2009](https://www.win.tue.nl/~wstahw/edu/2IV05/andrei/particle_rendering/provided/p91-van_der_laan.pdf))
7. **Beating heart: hybrid "physiology-driven target shapes + XPBD shell".** Blend-shape or keyframe targets are driven by Pulse's ventricular volume and heart rate. A compliant XPBD soft body follows the targets, so instruments can still indent and retract the heart. For v1 (on-pump CABG, see [research 01](01-surgical-procedure.md)) the **heart is arrested during the most precise work (anastomoses)**, which removes the hardest coupling exactly where precision matters most.
8. **Target platform: Windows PC desktop at 60 Hz first, PC VR via OpenXR at 90 Hz second.** Meta Quest 3 standalone is **not recommended**. Its 13.8 ms budget at 72 Hz, <200 draw calls and <1.5M triangles ([Meta](https://developers.meta.com/vr/resources/device-optimization-comparison/)), plus the loss of Lumen and Nanite under the mobile forward renderer ([Meta](https://developers.meta.com/horizon/documentation/unreal/unreal-forward-renderer/)), conflict with "as close as possible to real".
9. **Haptics are optional but designed in from day 1.** Use a 1 kHz haptic thread with virtual coupling. The best value device is the **3D Systems Touch** (3.3 N peak, 1 kHz, USB, OpenHaptics with Unity/Unreal plugins; [3D Systems](https://www.3dsystems.com/haptics-devices/touch)). **Quest 3 hand tracking averages about 1.7 cm error** ([Godden et al. 2025](https://ericg5.github.io/ResearchPortfolio/papers/characterization)), which is far too coarse for suturing, so controllers or a stylus are needed for fine work.
10. **Fallback stack: Unity 6.3 LTS plus the same TissueCore** (via a C API and P/Invoke). Quick-prototype alternatives are Obi Softbody/Rope/Fluid (paid, $55/$37/$60 per seat) and SofaUnity (free, Windows-only). Pulse Unity (Apache-2.0) covers physiology.

---

## 1. Engine comparison

### 1.1 Versions and licenses (as of 2026-11-03)

| | **Unreal Engine 5.8** | **Unity 6.3 LTS** (6.x tech stream) | **Godot 4.7** |
|---|---|---|---|
| Current version | **5.8**, released 17 Jun 2026, last planned major UE5 release. A 5.8.x hotfix line is expected. **UE6 Early Access targeted for end of 2027**; full release 12–18 months later ([Epic](https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show), [GameStar](https://www.gamestar.de/artikel/unreal-engine-6-early-access-2027-roadmap,3454807.html)) | **6.3 LTS**, supported until Dec 2027 ([Unity](https://unity.com/ja/releases/unity-6)). One third-party blog lists 6.4 (Mar 2026), 6.5 (Jun 2026), 6.6 as current, and a 6.7 LTS planned for end of 2026 ([issoh.co.jp](https://www.issoh.co.jp/md/tech/10417)) **(uncertain)** | **4.7** (docs list 4.7 as stable: [Godot docs](https://docs.godotengine.org/en/stable/tutorials/physics/soft_body.html)). 4.6 shipped in Jan 2026 with Jolt as default 3D physics ([GameFromScratch](https://gamefromscratch.com/godot-4-6-released/)) |
| License | Unreal Engine EULA. **Free** for individuals and hobbyists. **5% royalty only on lifetime gross revenue above US$1M per product**. Seats ($1,850/user/yr) are only needed by companies with **>$1M annual revenue** ([Epic FAQ via search](https://www.unrealengine.com/en-US/faq), [Road to VR](https://roadtovr.com/unreal-engine-royalty-free-first-1-million-revenue/)). Epic's own license page returned HTTP 403 to my fetcher, so I verified the terms through Epic's FAQ snippet and secondary sources. | Unity Editor Software Terms. **Personal: free up to US$200,000 revenue plus funding** (12-month window). **Splash screen optional** in Unity 6. Pro is $2,310/seat/yr from 12 Jan 2026. Runtime Fee cancelled 12 Sep 2024 ([Unity pricing](https://unity.com/products/pricing-updates)) | **MIT**. Ship the copyright and license notice, for example by linking godotengine.org/license in the credits ([Godot license](https://godotengine.org/license/)) |
| Personal non-commercial use? | **Yes, $0** | **Yes, $0** (Personal) | **Yes, $0** |
| Attribution / share-alike | No share-alike. Keep EULA notices. | No share-alike | Attribution (MIT notice). No share-alike. |
| Source access | Full C++ source on GitHub (needs an Epic account link) | Closed source (C# scripting, native plugins) | Fully open |

### 1.2 Feature comparison for *this* project

| Need | Unreal 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| **Photoreal tissue rendering** (wet speculars, subsurface scattering, translucency, blood film) | Best. Substrate materials (production-ready since 5.7: [MoguraVR/forum](https://forums.unrealengine.com/t/unreal-engine-5-7-released/2673913)), subsurface profiles, Lumen GI (**Lumen Lite beta, ~2× faster than Lumen high quality** in 5.8: [release notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?lang=en-US)), MegaLights production-ready in 5.8 | Good in HDRP, but **HDRP is in maintenance mode, with no new features** since the "Render Pipelines strategy for 2026" post (23 Feb 2026). URP is Unity's "long term focus" ([Unity](https://unity.com/topics/render-pipelines-strategy-for-2026)) | Adequate (Forward+ renderer). Weaker GI, subsurface scattering and post-processing tooling |
| **Built-in soft bodies** | **Chaos Flesh**: tetrahedral soft body (iso-surface stuffing, TetWild or radial tetrahedralization). Kinematic and weak constraints to skeletal meshes. Collides with convex/analytic rigid bodies. Designed for **character muscle**, with runtime low-res simulation plus offline high-res caches. **No cutting documented** ([Epic docs](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview)). 5.8 adds fat/muscle/skeleton layer interaction and performance work ([5.8 notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?lang=en-US)). Status label for 5.8 not found **(uncertain; historically Experimental)** | **None built-in.** Built-in physics is a PhysX integration with rigid bodies and Cloth only ([Unity 6.3 manual](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview)). Havok was dropped from Pro starting 6.3 ([Unity](https://unity.com/products/pricing-updates)). Third-party: **Obi Softbody** (oriented-particle XPBD, $55/seat, v7.2 of 25 Aug 2026, [Asset Store](https://assetstore.unity.com/packages/tools/physics/obi-softbody-130029)) | **SoftBody3D**: mesh-based, with a "simulation precision" setting. More robust under Jolt. Physics interpolation does not apply. Pinned points via attachments. **No cutting or tearing** ([Godot docs](https://docs.godotengine.org/en/stable/tutorials/physics/soft_body.html)). Under Jolt, SoftBody3D has no Area3D interaction ([godot-jolt README](https://github.com/godot-jolt/godot-jolt)) |
| **Cloth** (drapes, gauze, pericardium sheet) | **Chaos Cloth is production-ready in 5.8** ([5.8 notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?lang=en-US)) | Unity Cloth (basic). Obi Cloth (paid) | SoftBody3D as cloth |
| **Fluids** | Niagara GPU particles (mature). **Niagara Fluids** offers 2D templates for games and 3D for cinematics, with a warning that it "may result in a GPU crash on Windows" ([Epic docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-fluids-in-unreal-engine)). Status (Experimental vs production) conflicts between sources **(uncertain)** | VFX Graph (GPU particles). **Obi Fluid** ($60/seat, v7.2, [Asset Store](https://assetstore.unity.com/packages/tools/physics/obi-fluid-63067)) | GPUParticles3D only. No fluid solver |
| **Characters (OR team)** | **MetaHuman**: covered by the standard UE EULA since June 2025, free under $1M revenue ([CG Channel](https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/), [metahuman.com/license](https://www.metahuman.com/en-US/license)). MetaHuman Crowd is experimental in 5.8 | MetaHumans may be exported to Unity per the June 2025 change. One April 2026 blog disputes this **(uncertain; check the EULA)** | Same as Unity |
| **Nanite / large static scenes** | Nanite for the static OR, instruments and props. Nanite skinning is experimental. Deforming tissue cannot use Nanite (it needs a dynamic vertex buffer) | GPU Resident Drawer (URP/HDRP) | Visibility ranges/LOD |
| **Native code for medical libraries** | **C++ native**. Pulse has an official UE plugin (Apache-2.0, Win64, built for UE 4.27–5.3, rebuild needed for 5.8: see [research 02](02-physiology-perfusion.md), [Kitware/Lumeto](https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/)). iMSTK can be used "directly from C++" ([Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)). 3D Systems **HapticsDirect for Unreal** plugin (Win64, with source) ([Fab/Marketplace](https://unrealengine.com/marketplace/en-US/product/hapticsdirect-for-unreal/reviews)) | C# with native plugins via P/Invoke. Has the **largest medical-simulation plugin ecosystem**: Pulse Unity (free, Apache-2.0, multi-platform, no IL2CPP out of the box), iMSTK-Unity 2.0 (Oct 2023, Unity 2021.3, now unmaintained), SofaUnity (free, Windows-only), HapticsDirect for Unity | GDExtension (C++). No medical plugins found |
| **Iteration speed for a solo developer** | Slower: C++ compile times, heavy editor (~100+ GB with source) **(uncertain size)**. Blueprints help | Fast (C# hot reload) | Fastest and lightest |
| **AI-assisted development** | 5.8 ships an "Unreal MCP server plugin" ([GameFromScratch](https://gamefromscratch.com/unreal-engine-5-8-released/)) | Good C# tooling | Good (GDScript/C#) |

### 1.3 VR via OpenXR

| | Unreal 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| OpenXR core | Built-in OpenXR plugin. **OpenXR 1.0 and 1.1 runtimes supported**, and either can be disabled ([5.8 notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?lang=en-US)). 5.8 adds experimental **Steam Frame** support and a PICO controller OpenXR plugin enabled in the VR template | Unity OpenXR plug-in plus **Unity OpenXR: Meta** package. From OpenXR 1.14, Meta 2.1 is at feature parity with the Oculus plugin, and Unity recommends migrating to OpenXR ([Unity docs](https://docs.unity3d.com/6/Documentation/Manual/xr-meta-quest-develop.html)) | OpenXR built in. 4.5 added render models, D3D12 OpenXR and Vulkan foveation. **4.6 added OpenXR 1.1 and one universal Android APK**. The vendors plugin is optional from 4.6 ([Road to VR](https://www.roadtovr.com/openxr-update-godot-unity-game-engine/), [Godot docs](https://docs.godotengine.org/en/stable/tutorials/xr/deploying_to_android.html)) |
| PC VR (Quest 3 over Link/Air Link, Index, Steam Frame) | Yes. Deferred or forward renderer, Instanced Stereo, MSAA with forward | Yes. URP or HDRP. HDRP supports PC VR with single-pass instanced rendering ([HDRP VR docs](https://docs.unity.cn/Packages/com.unity.render-pipelines.high-definition%4015.0/manual/VR-Overview.html)) | Yes (Forward+/Mobile) |
| Quest 3 standalone | Yes, but **mobile forward renderer: no Nanite, no Lumen** ([Meta](https://developers.meta.com/horizon/documentation/unreal/unreal-forward-renderer/)). An open Meta investigation reports that the Meta XR plugins labelled for 5.8 are actually built for 5.7.0 ([Meta feedback](https://developers.meta.com/horizon/feedback/vr/investigations/1053459897316880/)) | Yes, with **URP only**. HDRP cannot build for Android ([Unity issue tracker](https://issuetracker.unity3d.com/issues/quest-2-hdrp-planar-reflection-probe-does-not-work-with-vr-when-built-for-windows-standalone)) | Yes. The 4.7 docs advise the **Compatibility (OpenGL) renderer** for Android XR "for the time being" ([Godot docs](https://docs.godotengine.org/en/4.7/tutorials/xr/deploying_to_android.html)) |
| Hand tracking | OpenXR hand-tracking extension (XR_EXT_hand_tracking) via the OpenXR plugin; MetaXR plugin | XR Hands package; Meta OpenXR | OpenXR hand tracking |

### 1.4 Verdict

| Criterion (weight) | UE 5.8 | Unity 6.3 | Godot 4.7 |
|---|---|---|---|
| Visual realism (×3) | **5** | 4 (HDRP frozen) | 3 |
| Soft-tissue path (×3) | 3 (custom C++ needed; Chaos Flesh not for cutting) | **4** (more plugins, though most are paid, stale or Windows-only) | 2 |
| Native integration of C++ medical libraries (×2) | **5** | 3 | 3 |
| VR (×2) | 4 | **5** | 4 |
| Solo-dev iteration (×2) | 3 | 4 | **5** |
| Characters/OR (×1) | **5** | 3 | 2 |
| Long-term stability (×1) | 4 (5.8 frozen as final UE5) | 4 (LTS) | 4 |
| **Weighted total (out of 70)** | **58** | **57** | 44 |

The scores are close. The deciding factors are the owner's "as close as possible to real" goal (rendering) and the fact that the physics core will be custom C++ anyway, which Unreal hosts natively. Unity is a strong fallback, and choosing it later stays cheap **if** TissueCore is kept engine-agnostic.

---

## 2. Soft-tissue simulation options

### 2.1 What the surgical-simulation literature actually uses

| Method | Accuracy | Speed / stability | Cutting & suturing friendliness | Used by |
|---|---|---|---|---|
| **Mass-spring** | Low. It is hard to justify physically, because it discretizes the equations of motion as well as the object ([Alterovitz & Goldberg](https://robby.cs.unc.edu/publications/Alterovitz2003_TR.pdf)) | Fast. Explicit integration is unstable when stiff | Easy: add or remove springs | Older simulators. Viscoelastic MSD inside PBD for laparoscopic cholecystectomy ([Xu et al. 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5830759/)) |
| **PBD / XPBD** (position-based dynamics; XPBD adds compliance so stiffness is independent of time step and iteration count) | Medium. XPBD with FEM-based constraints (Neo-Hookean) approaches FEM quality | **Unconditionally stable** and real time. Small substeps beat many iterations ([Macklin et al. 2019 "Small Steps"](https://diglib.eg.org/handle/10.1145/3309486-3340247)) | **Best**: remove or split constraints locally; mesh-free variants exist ([Berndt et al. 2017, IEEE CG&A 37(3)](https://doi.org/10.1109/MCG.2017.45)) | **iMSTK** (xPBD main solver; [Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)). **IMA-harvest CABG simulator** (PBD, 5 ms step, 5 iterations; [Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)). Catheter-ablation beating heart in PBD ([Wang & Wu 2021](https://doaj.org/article/cb9d85655d3148b08962356cdf1bca8a)). Obi (Unity), Chaos Cloth (UE) |
| **FEM** (corotational, StVK, hyperelastic; implicit) | **High** | Costly. Real time needs tricks: asynchronous preconditioners ([Courtecuisse et al. 2014](https://hal.archives-ouvertes.fr/hal-01097108)), model reduction ([Vega](https://viterbi-web.usc.edu/~jbarbic/code/index.html)), GPU | Hard: the model must be rebuilt or remeshed on cuts (a survey of cutting methods is in [Wu, Westermann & Dick 2015](https://diglib.eg.org/handle/10.1111/cgf12528)) | **SOFA** (cataract, hepatectomy and brain demonstrators). Chaos Flesh, PhysX 5 deformable volumes |
| **Meshless / particles** (SPH, shape matching) | Medium | Fast | Natural topology change | Bleeding (SPH), connective tissue strands (SPH + distance constraints in [Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)) |

**Takeaway:** for an **interactive, cut-heavy, suture-heavy** game, XPBD on tetrahedral meshes (volumetric organs) and triangle/rod meshes (membranes, vessels, thread) is the pragmatic standard. FEM (SOFA) is the accuracy reference.

### 2.2 Candidate libraries and engines

| Option | License (exact) | Personal use? | Attribution / share-alike | Status (Nov 2026) | Fit |
|---|---|---|---|---|---|
| **SOFA Framework** | **LGPL-2.1-or-later** for the core. `applications/projects` and `applications/tutorials` are GPL. Some directories carry their own license ([GitHub](https://github.com/sofa-framework/sofa)) | Yes | LGPL: ship the license and allow relinking if distributed. No share-alike on your own code when dynamically linked | **Active**: v26.06.00 (15 Jul 2026). Last commit 3 Nov 2026 ([releases](https://github.com/sofa-framework/sofa/releases)). Geomagic and Falcon haptic plugins ([SOFA Geomagic](https://www.sofa-framework.org/?p=23007)) | **Offline FEM reference and calibration tool.** Cutting plus contact during topology change is "not trivial" (maintainer, 2021: [SOFA forum](https://www.sofa-framework.org/community/forum/topic/2d-incision-with-phantom-omni/)). SOFA's own rendering is weak, which is why Filasofia exists ([Poliakov et al. 2023](https://arxiv.org/abs/2311.14508)) |
| **SofaUnity** (InfinyTech3D) | **Standard Unity Asset Store EULA** (free asset, version 24.12.00 of 8 May 2025). Depends on LGPL SOFA DLLs ([Asset Store](https://assetstore.unity.com/packages/tools/physics/sofa-physics-engine-for-unity-270170)). Other licenses are available on request ([GitHub](https://github.com/InfinyTech3D/SofaUnity)) | Yes | EULA terms | **Windows only**. Liver cutting and carving demos, haptics, VR/AR, two-way coupling ([GitHub](https://github.com/InfinyTech3D/SofaUnity)) | Fallback-stack option for Unity |
| **SofaUE5-Renderer** | **GPL-3.0** ([GitHub](https://github.com/InfinyTech3D/SofaUE5-Renderer)) | Yes (GPL is fine for private use; distributing a build would have to be GPL) | **Copyleft** | UE **5.0.3**, render-only (only VisualModels mapped; gravity and timestep are the only parameters). A Nov 2025 Kickstarter for a full open-source UE5 plugin reported no outcome ([UE forum](https://forums.unrealengine.com/t/bringing-sofa-physics-engine-biomechanical-simulation-to-unreal-engine-5-kickstarter-now-live/2676465)) | **Not usable as runtime.** Re-check in 2027 |
| **iMSTK** (Kitware) | **Apache-2.0** ([Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)) | Yes | Keep LICENSE/NOTICE. No share-alike | **Discontinued 2 May 2025** (README sunset notice; last tag v7.0.0; [GitHub mirror](https://github.com/Kitware/iMSTK)). iMSTK-Unity 2.0 (Oct 2023, Unity 2021.3; [docs](https://imstk-unity.readthedocs.io/en/latest/releases.html)) | **Reference code**: xPBD with distance/volume/FEM/dihedral constraints; needle insertion constraint with barycentric puncture points; thread with bend constraints plus line-mesh CCD; OpenHaptics, VRPN and Haply Inverse3 device support; SPH bleeding coupled to Pulse ([Kitware](https://www.kitware.com/imstk-integrates-pulse-physiology/)). **Do not depend on it** |
| **PositionBasedDynamics** (Jan Bender) | **MIT** (checked LICENSE in repo) ([GitHub](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics)) | Yes | MIT notice | Active (last commit 1 Sep 2026). FEM-based PBD, strain-based dynamics, XPBD constraints, **stiff rods** (Deul et al. 2018 direct solver), substepping | **Primary reference and borrowable code** for TissueCore |
| **Obi** (Softbody / Rope / Fluid / Cloth, Virtual Method) | **Standard Unity Asset Store EULA**, "Extension Asset", per seat. Softbody **$55**, Rope **$37**, Fluid **$60**, all v7.2 of 25 Aug 2026, Unity 6000.0.82 ([Softbody](https://assetstore.unity.com/packages/tools/physics/obi-softbody-130029), [Rope](https://marketplace.unity.com/packages/tools/physics/obi-rope-55579), [Fluid](https://assetstore.unity.com/packages/tools/physics/obi-fluid-63067)) | Yes (paid) | EULA. No redistribution of source | Active. Oriented-particle XPBD with a CPU/GPU solver. **Rope supports tearing and cutting**. Softbody cutting is not advertised ([Obi site](https://obi.virtualmethodstudio.com/)) | Unity fallback only. Good for **suture thread** (Obi Rope) in a quick prototype |
| **PhysX 5 deformable volumes** (FEM) | **BSD-3-Clause** ([GitHub, v5.12.0, Oct 2026](https://github.com/NVIDIA-Omniverse/PhysX)) | Yes | BSD notice | Active. **GPU-only (CUDA, Volta+)**. "Soft Body" was renamed "Deformable Volume" in 5.5. Simulation tet mesh plus collision tet mesh ([docs](https://nvidia-omniverse.github.io/PhysX/physx/5.6.1/docs/DeformableBodyOverview.html)). Shapes and simulation meshes cannot be attached or detached while in a scene (5.12 changelog) | Poor fit: NVIDIA-only, no runtime cutting **(uncertain)**, and UE uses Chaos rather than PhysX |
| **NVIDIA Warp** | **Apache-2.0** (checked LICENSE.md) ([GitHub](https://github.com/NVIDIA/warp)) | Yes | Apache NOTICE | Active (commit 2 Nov 2026). Python→CUDA kernels; `warp.fem`; soft-body examples; differentiable | **Offline tool**: differentiable fitting of XPBD compliance against SOFA or measured data. Not a runtime (Python/CUDA) |
| **Vega FEM** (Barbič) | **BSD-3-Clause** ([USC code page](https://viterbi-web.usc.edu/~jbarbic/code/index.html)) **(secondary sources)** | Yes | BSD notice | Mature and slow-moving | Model-reduced StVK, real time for non-cut organs. Little benefit over XPBD for a cut-heavy game |
| **AMD FEMFX** | **MIT** ([GPUOpen](https://gpuopen.com/femfx/)) | Yes | MIT notice | Status not checked **(uncertain)** | CPU tet FEM with fracture. Reference only |
| **Chaos Flesh** (UE) | UE EULA | Yes | UE EULA | Ships with UE 5.8 | Use for **non-interactive** secondary motion only, such as fat or muscle jiggle, and as an **in-engine TetWild tetrahedralizer** (Dataflow) |
| **Ten Minute Physics** (M. Müller) | **UNVERIFIED** (no LICENSE file at the root of the `matthias-research/pages` repo) | Learn from, don't copy | – | Active (commit 6 Oct 2026). Tutorials on unbreakable soft bodies and on embedding a high-res mesh in a low-res tet mesh for "100×" speed-ups ([site](https://matthias-research.github.io/pages/tenMinutePhysics/index.html)) | Concept reference |

**Tetrahedralization tools:**
- **UE Chaos Flesh Dataflow** offers TetWild and iso-surface stuffing in-engine ([Epic](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview)).
- External options are **fTetWild** (MPL-2.0, **UNVERIFIED**) and **TetGen** (AGPL-3.0 for non-commercial use, **UNVERIFIED**; avoid linking it into the runtime).

### 2.3 Recommended TissueCore design (summary; details in §3)

- **Solver.** XPBD with **substepping**: one iteration per substep, N substeps per physics tick ([Small Steps](https://diglib.eg.org/handle/10.1145/3309486-3340247)). Parallel Jacobi or graph-coloured Gauss–Seidel on CPU first (Unreal task graph). Optional GPU compute port later.
- **Constraints:**
  - tet volume + Neo-Hookean FEM constraints for organ volumes (Macklin & Müller 2021, "A Constraint-based Formulation of Stable Neo-Hookean Materials"; from prior knowledge, not re-verified this session)
  - stretch + dihedral bending for membranes (pericardium, pleura, vessel walls, fascia, as in [Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/))
  - stretch-shear + bend-twist rods for thread
  - attachment, grasp, needle-insertion and contact constraints
- **Embedded rendering.** A low-res simulation tet mesh drives a high-res render mesh through barycentric embedding on the GPU (the technique in Müller's tutorial and in Chaos Flesh). Render meshes are 50–200k triangles per organ. Simulation meshes are 1–10k tets in interactive zones **(uncertain sizes; validate in spikes)**.
- **Calibration.** Fit XPBD compliance per tissue type against SOFA FEM runs (offline), optionally with Warp's differentiability. Literature values for tissue Young's modulus (myocardium, aorta, pericardium) come from research 05/06 (realism).
- **Engine boundary.** A C API with double buffers: TissueCore runs on its own thread at fixed `dt_phys`. The engine reads the latest positions and interpolates. Haptics read a local linearized proxy at 1 kHz (§4).

---

## 3. Hard problems and known techniques

### 3.1 Incision (skin, subcutaneous tissue, cautery)

- **What must happen** (per research 01, Phase B): a midline skin incision, then cautery down to periosteum, staying midline and scoring the line for the saw.
- **Technique options:**
  1. **Element deletion**: simple, but loses volume and looks jagged.
  2. **Element splitting / remeshing along the blade path**: accurate, but has the most edge cases.
  3. **Virtual node algorithm**: duplicate elements with "virtual" nodes, so cuts stay clean without tiny elements (Molino, Bao & Fedkiw, SIGGRAPH 2004; from prior knowledge, not re-verified).
  4. **Snapping**: move nearby nodes onto the cut surface, then split along existing faces.
  5. **Mesh-free PBD cutting with oriented-particle skinning** ([Berndt 2017](https://doi.org/10.1109/MCG.2017.45)).
  6. **Topology-preserving local remeshing** for membranes ([Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)).
  
  The full taxonomy is in [Wu et al. 2015](https://diglib.eg.org/handle/10.1111/cgf12528) ([preprint](https://www.cs.cit.tum.de/fileadmin/w00cfj/cg/Research/Publications/2014/STAR/STAR_preprint.pdf)).
- **Recommendation:**
  - Use **layered skin**: a 2.5D surface shell for epidermis/dermis plus a thin tet layer for fat, in authored "cuttable zones" with denser simulation meshes.
  - Cut by **snapping plus splitting of triangles/tets intersected by the swept blade surface**.
  - Visual detail comes from a **render-target "incision mask"** (bleeding edge, dermis colour, cautery char) painted in UV space. This keeps the geometry modest.
- **Electrocautery:** a heat-diffusion field on the surface (Berndt 2017 models electrocautery heat diffusion). It drives blanching and char textures, a smoke particle emitter, and "sealed" flags on small bleeders.

### 3.2 Median sternotomy and retraction

- The sternum is **rigid bone**. Model it as two rigid halves joined by a **pre-authored midline split surface**.
- The saw's progress follows the scored line (research 01 B2). Deviation from the midline is measured, and the cut path is "baked" into a pre-fractured mesh at the actual saw trajectory, within ± a few mm.
- Bone-dust particles and marrow oozing come from a physiology-scaled venous bleed source; **bone wax** stops it.
- The **sternal retractor** is an articulated rigid body (rack and crank). Each crank step increases the spread. Soft-tissue attachments (pericardium, pleura, fat) are XPBD attachment constraints to the sternal halves, so they stretch realistically.
- **Error cues:** over-spreading tears tissue (§3.3), and rib or brachial-plexus strain can be a score penalty **(design choice)**.

### 3.3 Tearing

- XPBD produces **Lagrange multipliers, which give constraint force estimates**. This enables "breakable" constraints ([XPBD paper](https://matthias-research.github.io/pages/publications/XPBD.pdf); [IPSJ report](https://ipsj.ixsq.nii.ac.jp/record/183598/files/IPSJ-CG17167010.pdf)).
- **Rule:** if a constraint's strain exceeds ε_tear (or force exceeds F_tear) for more than *k* consecutive substeps, remove it and split the shared vertices. This is the same topological operation as cutting, so tearing reuses the cutting code path.
- **Per-tissue thresholds** (atrial wall is friable, aorta tougher, fat very weak) come from the realism research. They then trigger bleeding sources (§3.8) and score events. iMSTK uses a similar threshold-based removal for blunt dissection ([Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)).

### 3.4 Suturing (purse-strings, anastomoses, closure) and knot tying

**Real targets** (research 01):
- 2-0 Ethibond aortic purse-strings with bites into the media (about 2 mm entry–exit)
- 3-0/4-0 Prolene for the RA and retrograde cannula purse-strings
- **7-0/8-0 Prolene** for coronary anastomoses
- steel wires for sternal closure

**Thread model:**
- **Cosserat rod in PBD**: positions plus quaternion orientations, so bending and twist are coupled ([Kugelstadt & Schömer, SCA 2016](https://animation.rwth-aachen.de/media/papers/2016-SCA-Cosserat-Rods.pdf)). Alternatives are the Deul et al. 2018 direct solver for stiff rods (implemented in [PositionBasedDynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics)) and newer "Stable Cosserat Rods" (SIGGRAPH 2025, [Utah](https://graphics.cs.utah.edu/research/projects/stable-cosserat-rods/Stable_Cosserat_Rods-SIGGRAPH25.pdf); details not reviewed).
- **Inextensibility**: thread must not stretch. Solve the 1D distance chain directly with a **tridiagonal (Thomas) solve** each substep ([Xu & Liu 2018, IJCARS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6015127/)). The classical alternative is "Follow-the-Leader" ([Brown, Latombe & Montgomery 2004](https://doi.org/10.1007/s00371-003-0226-y)).
- **Resolution**: 100–300 segments per suture. Segment length is about 1–2 mm for 7-0 work **(uncertain; tune in spike)**.
- **Self-collision and thread–tool collision** need **continuous collision detection** between line segments (iMSTK uses Qi et al. 2017 line-mesh CCD; [Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)).

**Needle–tissue interaction** (follow iMSTK's design):
- The needle is a rigid curved arc (3/8 or 1/2 circle) held by the needle driver.
- **Puncture**: when tip force along the needle axis exceeds a puncture threshold, create a puncture point stored as **barycentric coordinates on the punctured triangle**.
- An **insertion constraint** keeps the needle shaft on the puncture point while allowing sliding along its arc.
- After exit, **thread–tissue constraints** let the thread slide through the puncture points with friction.
- Tension in the thread pulls the tissue edges together, which is how purse-strings cinch and anastomoses approximate.

**Knot tying:**
- Fully physical knots (stable under tension with friction) are research-grade and fragile at game time steps.
- **Recommendation:** use a **hybrid**.
  1. Detect the instrument-tie gesture topologically: a wrap around the needle-driver jaws, then grasping the free end and pulling through. Knot-identification by topology is the idea in Brown 2004.
  2. Replace the wrap with a **procedurally generated knot geometry** (square or surgeon's knot) whose rope segments stay simulated. Physical tightening ("cinching") applies tension to the tissue.
  3. Score throw count, direction alternation (square vs granny), and tension (too loose leaks, too tight cuts through friable tissue).
  4. Purse-string snaring with **Rumel tourniquets** works the same way: a rigid tube slides along both thread ends and is clamped.
- **Scale problem:** 7-0/8-0 thread is about 0.05 mm, and real surgeons wear about 3.5× loupes. Provide a **"loupe" magnified camera mode** and **motion scaling/tremor filtering** on input. Precision of mouse or VR controller is otherwise insufficient.

### 3.5 Tool–tissue collision and grasping

- **Tools** (forceps, needle driver, scissors, cautery, suction, clamps) are kinematic rigid bodies driven by input, or by a virtual-coupling spring when haptics are present.
- **Collision proxies:**
  - capsules/convex shapes for shafts
  - **signed distance fields (SDF)** for complex jaws
  - **CCD for thin, fast tools** (blades, needles), to avoid tunnelling at 1–2 mm per substep
- **Contact**: XPBD contact constraints between tissue particles/surface triangles and tool SDFs, with Coulomb friction.
- **Grasping**: on jaw closure, find tissue vertices inside the jaw volume and create **attachment constraints** to jaw-local positions. Release on jaw opening, or **tear** if force exceeds tissue strength (§3.3). iMSTK-Unity 2.0 improved grasping in this way ([release notes](https://imstk-unity.readthedocs.io/en/latest/releases.html)).
- **Haptic force** = coupling-spring force between the device proxy and the simulated tool (§4).

### 3.6 Retraction and exposure

- **Retractors** (sternal, IMA "Skyhook", Army-Navy, pericardial stay sutures) are kinematic rigid bodies plus attachment or contact constraints.
- **Pericardial well**: pericardial edges are sutured to the retractor or drapes, which is an attachment constraint to the world.
- The **heart** is lifted or positioned with laps and slings, or by the assistant. In the game, the AI assistant applies scripted retraction forces as constraints. The player can also do it.

### 3.7 Clamping vessels (aortic cross-clamp, bulldogs, snares)

- **Geometry**:
  - Vessels are a **tube shell** (triangle mesh with stretch and bending constraints, plus an internal **pressure/volume constraint** driven by local blood pressure).
  - A **1D centreline with a radius field** couples the vessel to the physiology/flow model.
- **Clamp action**: clamp jaws are rigid. Closing them flattens the tube through contact. When the jaw gap is less than about 2× wall thickness, the vessel is "occluded".
- **Coupling**: set the downstream flow resistance to ∞ in the physiology/perfusion model (Pulse plus the custom CPB layer; research 02). Effects:
  - a pressure drop distal to the clamp
  - loss of pulsation in the visual
  - flags for "clamp on/off" events, cross-clamp timer, cardioplegia delivery path
- **Errors to model**: partial occlusion (leak, blood in the field), clamping too close to cannula, clamping a calcified segment (an embolism risk flag; design choice), and an unclamped cardioplegia vent.

### 3.8 Blood

**Real behaviours needed** (research 01/02):
- arterial spurting synced with systole
- venous welling and oozing
- marrow ooze
- pooling in the pericardial well
- suction returning blood to the cardiotomy reservoir (on CPB)
- clotting and drying over time
- cardioplegia/saline irrigation clearing the field

**Layered architecture (recommended):**

| Layer | Technique | Driven by | Budget (GPU) |
|---|---|---|---|
| 1. Source flow | Each bleeding site (cut vessel, tear, puncture, cannula site) has an **orifice area A** and a **local pressure P(t)** taken from the physiology engine (aortic/arterial or venous pressure waveform). Flow Q ≈ C_d·A·√(2ΔP/ρ) (orifice equation), capped by vessel flow | Pulse hemorrhage action receives total ΣQ, so the patient bleeds. iMSTK did exactly this two-way coupling (SPH loss → Pulse hemorrhage; Pulse femoral flow → SPH inlet) ([Kitware](https://www.kitware.com/imstk-integrates-pulse-physiology/)) | CPU, negligible |
| 2. Jets and drips | GPU particles (Niagara / VFX Graph). Emission rate ∝ Q, exit velocity ∝ √ΔP, **pulsed with the arterial waveform**. Collide against tissue depth buffer/SDF. On impact, spawn decals and add mass to layer 3/4 | Layer 1 | ≤0.7 ms |
| 3. Pooling | Per cavity (pericardial well, pleural spaces): a **volume budget V(t)** = Σ inflow − suction − spill, rendered as a **height-field fluid surface** clipped to cavity geometry (simple 2D shallow-water or a smoothed level plane with ripples). Optional **Niagara Fluids 2D** for the surface **(uncertain status)** | Layer 1, suction tool | ≤0.5 ms |
| 4. Surface wetness | **Render-target blood/wetness mask** in each organ's UV space. Painted by particle impacts and flow-down gradients, decays (drying darkens and turns matte), cleared by irrigation/sponging. Drives albedo, roughness, clearcoat and a thin-film shader | Layers 2/3 | ≤0.3 ms |
| 5. Optional close-up SPH | Small SPH domain (≤20–50k particles, **uncertain**) near the active bleeder, rendered with **screen-space fluid rendering** (depth splat + curvature-flow or narrow-range smoothing + thickness for absorption) ([Müller, Charypar & Gross 2003](https://matthias-research.github.io/pages/publications/sca03.pdf); blood-specific: [Müller, Schirm & Teschner 2004](https://cgweb.informatik.uni-freiburg.de/publications/2004_THC_bloodSimulation.pdf); rendering: [van der Laan, Green & Sainz 2009](https://www.win.tue.nl/~wstahw/edu/2IV05/andrei/particle_rendering/provided/p91-van_der_laan.pdf); iMSTK SPH: [Kitware](https://kitware.com/sph-fluid-simulation-in-imstk)) | Layer 1 | ≤1.5 ms, desktop only |

- **Suction**: the suction tip removes volume from layer 3 and particles in radius. It reports "returned volume" to the perfusion module (cardiotomy reservoir), or to waste when using the cell saver or wall suction **(design choice)**.
- **Clotting (simplified)**: a site's effective A decays with time when pressure is low and the site is packed or cauterized. Heparinized blood (on CPB) does not clot, which matters for realism after heparin and protamine.
- **Avoid** a full 3D FLIP/SPH fluid for the whole field. It is too costly for VR and adds little over layers 2–4 visually (judgement call).

### 3.9 The beating heart

| Approach | Realism | Interactivity (tools can push it) | Coupling to physiology | Cost | Verdict |
|---|---|---|---|---|---|
| A. Skeletal animation / **blend shapes** (keyframes from gated 4D CT, e.g. 11 phases of the R–R interval registered to a reference: [Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)) | High (shape is real) | None (kinematic) | Easy: map cardiac phase and stroke volume to blend weights | Very low | Use as **target shapes** |
| B. **XPBD soft body following targets** (shape matching or attachment constraints with compliance toward the animated target; shape matching per Müller et al. 2005 "Meshless deformations based on shape matching", from prior knowledge) | High | **Yes**: indents, retracts, reacts to clamps and slings | Through targets plus stiffness changes | Low–medium | **Recommended** |
| C. **Active-strain XPBD**: fibre-direction constraints whose rest length is scaled by an activation a(t) from the physiology engine (time-varying elastance → activation) | Medium–high (emergent shape) | Yes | Direct | Medium. Hard to tune shape | Later (v2+) experiment |
| D. Full electromechanical FEM (as in research cardiology codes) | Highest | Yes | Native | Far beyond real time | No |

**Recommended mapping (approach A+B):**

| Physiology input (Pulse/custom, research 02) | Drives |
|---|---|
| Heart rate, cardiac cycle phase | Blend-shape timeline speed and phase |
| LV and RV volumes, normalized (EDV→ESV) | Blend weight amplitude (bigger stroke volume means bigger motion) |
| Contractility / elastance | Target-follow stiffness (a weak heart is floppier) |
| Rhythm: **VF** | High-frequency noisy target perturbations ("bag of worms") |
| Rhythm: asystole or **cardioplegic arrest** | Targets off, stiffness lowered to passive myocardium |
| Distension (vented vs not) | Base-shape scale |
| Respiration (pre-bypass) | Lungs and mediastinum translate the whole heart. Lungs can use Chaos Flesh or blend shapes |

The heart's **surface mesh** (epicardium with coronaries, fat and veins) is embedded in the simulation tet mesh, about 3–8k tets **(uncertain)**. Coronary targets for anastomosis need local mesh refinement.

**v1 simplification:** during grafting the heart is **arrested and still** (cross-clamp plus cardioplegia, research 01 Phase F), so the micro-suturing runs on a quasi-static body. Beating matters for opening, cannulation (Phase D), reperfusion and weaning (Phases G–H). An off-pump variant (v3/v4) would need a stabilizer device (suction "octopus"), modelled as local attachment constraints that damp motion.

### 3.10 Cannulation (aortic, two-stage venous, retrograde cardioplegia)

The sequence per research 01 Phase D. Each step is a combination of mechanics already described:

| Step | Mechanics | Physiology / perfusion coupling |
|---|---|---|
| Purse-strings (2× aortic, 1× RA, 1× coronary sinus) | Needle and thread (§3.4) with "bite depth" measured: needle path depth vs vessel-wall layer (media vs full thickness) | Full-thickness bite on the aorta creates a bleeding source |
| Snare with Rumel tourniquets | Rigid tube sliding on the thread ends; clamp | – |
| Aortotomy (stab inside purse-string) | Small cut (§3.1) in the vessel shell. Arterial jet (§3.8), pulsatile | Bleed rate from aortic pressure. Score: systolic BP control (anaesthesia lowers it to about 90–100 mmHg; research 01) |
| Insert cannula | Rigid tube with an **insertion constraint** (like the needle) through the hole. Orientation and depth checked against targets | Malposition (e.g. directed into the arch vessels, or dissection) produces a complication flag |
| Cinch and tie | Snare tightens (purse-string closes around the cannula) and stops the leak | Bleed site A → 0 |
| De-air and connect | Backbleed fills the line. **Air in line** detection: the player must fill the cannula with blood before connecting | Air embolism risk flag |
| Go on bypass | Perfusion module takes over (research 02) | CPB flow, reservoir level |

### 3.11 Other interactions worth listing for the plan

- **Sponges/laps**: Chaos Cloth (production-ready in 5.8). They absorb blood: the wetness mask darkens and the volume is removed.
- **Irrigation**: a particle stream adds clear fluid to the pool and washes the wetness mask.
- **Instruments in hand**: an IK-driven MetaHuman surgeon/assistant shows what the AI team is doing.
- **Sternal wires**: rigid-ish rods (Cosserat with high stiffness), twisted in a gesture-recognized sequence.

---

## 4. Haptics and hand tracking

### 4.1 Devices

| Device | Peak / continuous force | Workspace | Update rate | Interface / OS | Price | Notes |
|---|---|---|---|---|---|---|
| **3D Systems Touch** | **3.3 N** peak / >0.88 N continuous | Listed as >431 × 348 × 165 mm on the current page. Older specs said ~160 × 120 × 70 mm **(uncertain: page figure looks like the usable reach)** | **1 kHz** | USB 2.0/3.0. Windows 10/11, Ubuntu 24.04 | ≈ US$2,800 list (reseller, may be stale) **(uncertain)** | 6-DOF sensing, 3-DOF force. Stiffness ≥1.0–2.3 N/mm. 0.055 mm resolution ([3D Systems](https://www.3dsystems.com/haptics-devices/touch)) |
| **3D Systems Touch X** | **7.9 N** / >1.75 N | >355 × 228 × 180 mm | **up to 4 kHz** | USB | Not found | 0.023 mm resolution (same source) |
| **Force Dimension omega.3** | **12 N** | Ø160 × 110 mm | up to 4 kHz | USB 2.0 | Not found (research-grade, high) | <0.01 mm resolution ([spec sheet](https://www.forcedimension.com/images/doc/specsheet_-_omega3.pdf)). sigma.7 (7-DOF with grip force) specs not verified **(uncertain)** |
| **Haply Inverse3** | Not verified | Not verified | 4 kHz | USB. WebSocket SDK | Not found | 0.01 mm resolution ([Haply](https://haply.squarespace.com/inverse3)). Supported by iMSTK (README) |
| **Novint Falcon** | Not verified | Approx. ±6 cm × ±6 cm × 10 cm valid range (ROS wrapper, unofficial; [ros_falcon_interface](https://github.com/ZhuoyunZhong/ros_falcon_interface)) | ~1 kHz **(uncertain)** | USB (no hubs on Windows) | Second-hand only; discontinued **(uncertain)** | Open driver **libnifalcon** ([GitHub](https://github.com/libnifalcon/libnifalcon)), license **UNVERIFIED** (BSD per memory). Supported by CHAI3D and SOFA |
| **SenseGlove Nova 2** (force-feedback glove) | Up to 20 N per finger (magnetic brakes, resistive only) | Hand | – | Wireless. Unity/Unreal SDK **(uncertain)** | **US$5,999 excl. VAT per set** ([SenseGlove](https://www.senseglove.com/product/nova-2/)) | Gives grip "size/stiffness" feel, not tool-tip forces. Poor fit for instrument surgery |

### 4.2 SDKs

| SDK | License | Personal use | Engines | Notes |
|---|---|---|---|---|
| **OpenHaptics** (3D Systems) | Proprietary. **UNVERIFIED** terms. A "Developer Edition" exists. 3D Systems offers a demo request ([3D Systems](https://3dsystems.com/node/17361), [EST](https://est-kl.com/openhaptics)) | Presumably yes with a device **(uncertain)** | **HapticsDirect plug-ins for Unity and Unreal**. The Unreal plugin is Win64 with source ([Marketplace](https://unrealengine.com/marketplace/en-US/product/hapticsdirect-for-unreal/reviews)); its license is **UNVERIFIED** | Windows 10/11 and Linux (Ubuntu 20+). Touch driver 2022.8.1+ |
| **CHAI3D** | **BSD-3-Clause** ("Revised BSD"), checked in repo `copyright.txt` ([chai3d.org](https://chai3d.org/download/license)) | Yes | Engine-agnostic C++ | Supports Force Dimension, 3D Systems Phantom/Touch, Novint Falcon, Leap. **Last commit Aug 2024** ([GitHub](https://github.com/chai3d/chai3d)), so slow-moving. Cite the Eurohaptics 2003 paper if publishing |
| **Force Dimension SDK** | Proprietary, **UNVERIFIED** | **(uncertain)** | C/C++, Python bindings | Version 3.7.3+ referenced by Quanser ([Quanser](https://docs.quanser.com/quarc/documentation/force_dimension_read_block.html)) |
| **Haply SDK** | **UNVERIFIED** | **(uncertain)** | WebSocket, language-agnostic | Isaac Lab uses it |

### 4.3 Haptic architecture (standard practice)

- **Separate haptic thread at 1 kHz** (Touch) or up to 4 kHz (Touch X, omega). iMSTK requires 500–1000 Hz and runs physics at least as fast as haptics ([Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)). The IMA simulator runs haptics at 1 kHz with visuals at about 60 Hz ([Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)).
- **Virtual coupling**: a spring-damper between the device position and the simulated tool. It is preferred over direct coupling for stability (iMSTK paper; concept from Colgate et al. 1995, from prior knowledge).
- **Intermediate representation**: the physics thread (100–500 Hz) publishes local contact planes and stiffness around the tool tip. The haptic thread renders forces against this local model at 1 kHz.
- **Force scaling**: the Touch peaks at 3.3 N, so scale real forces down (e.g. the sternal saw or retractor crank) and use visual/audio cues for large forces.

### 4.4 VR hand tracking and controller alternatives

- **Accuracy:** Quest 3 hand tracking had about **1.73 cm average positional error** (best case) and 1.11 cm jitter in a robotic study ([Godden, Steedman & Pan 2025](https://ericg5.github.io/ResearchPortfolio/papers/characterization)). Quest 2 had about 1.1 cm fingertip error, 9.6° joint error and **45 ms delay** ([Behavior Research Methods study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/)).
- **Conclusion:** hand tracking is fine for gross actions (taking instruments, gestures, menus, pointing to the scrub nurse) but **not for suturing**, which needs sub-millimetre control.
- **Controllers** are much more precise (sub-mm headset/controller tracking under good conditions; not verified this session).
- **Proposed "precision mode":** hold a trigger to engage 1:3–1:5 motion scaling with tremor filtering (a one-euro-style low-pass; design choice) when doing fine work.
- **Mixing a desk-mounted haptic stylus with VR** is possible: register the stylus base in VR space, and the user sits at a desk. It works for a single-device "surgeon's dominant hand" mode **(design choice; uncertain comfort)**.
- **Recommendation for input modes:**
  1. Desktop: mouse/keyboard with contextual tools and motion scaling (v1)
  2. Desktop plus haptic stylus (v1.5)
  3. PC VR with controllers and precision mode (v2)
  4. PC VR plus haptic stylus (experimental)

---

## 5. Performance budgets

### 5.1 Frame budgets

| Mode | Refresh | Frame budget | Notes |
|---|---|---|---|
| Desktop | 60 Hz | **16.67 ms** | Lumen, SSS, SPH close-up allowed |
| PC VR | 90 Hz | **11.11 ms** (target ≤10 ms to leave compositor/reprojection headroom) | Stereo; MSAA/forward preferred |
| PC VR | 120 Hz | 8.33 ms | Not targeted |
| Quest 3 standalone | 72 Hz (90 recommended) | **13.8 ms** at 72 Hz | **<200 draw calls, <1.5M triangles/frame**, 2064×2208 per eye, 8 GB RAM, XR2 Gen 2 ([Meta](https://developers.meta.com/vr/resources/device-optimization-comparison/)) |
| Haptics | 1,000 Hz | **1.0 ms** | Separate thread; must never miss |

### 5.2 Proposed budget split (targets for spikes, **uncertain until measured**)

Reference hardware assumption: 8-core desktop CPU and an RTX 4070-class GPU for 60 Hz desktop and 90 Hz PC VR **(design assumption)**.

| Item | Desktop 60 Hz | PC VR 90 Hz | Thread / unit |
|---|---|---|---|
| Game logic, AI team, physiology (Pulse at 50 Hz internal steps, 10–15× real time; research 02) | 2.0 ms | 1.5 ms | Game thread (Pulse can run on a worker) |
| **TissueCore XPBD** (fixed tick e.g. 120–240 Hz × 2–4 substeps) | ≤6 ms per frame across 3–4 worker cores | ≤4 ms | Async worker threads, decoupled from render |
| Thread/suture rods (1–3 active, 100–300 segments) | ≤0.5 ms | ≤0.5 ms | Same |
| Collision (tool SDFs, CCD for thread/needle) | ≤1 ms | ≤0.8 ms | Same |
| Render thread / draw submission | ≤4 ms | ≤4 ms | Render thread |
| GPU: base OR scene (Nanite static, MegaLights or baked) | ~6 ms (with Lumen or Lumen Lite) | ~4 ms (baked GI and few dynamic lights; **no full Lumen in VR**) | GPU |
| GPU: tissue (embedded-mesh deformation in compute, SSS, wet shading) | ~2 ms | ~2 ms | GPU |
| GPU: blood layers 2–4 (+5 desktop) | ~1.5 ms (+1.5 SPH) | ~1.5 ms (no SPH) | GPU |
| GPU: post-processing, UI | ~1.5 ms | ~1 ms | GPU |
| **GPU total** | **~12.5 ms of 16.7** | **~8.5 ms of 11.1** | |
| Haptics | <0.2 ms per 1 ms tick | same | Haptic thread |

### 5.3 Simulation sizes (starting points to validate)

- **Published data points:**
  - iMSTK (CPU, Gauss–Seidel xPBD, laptop i9-12900HK): solved constraints in **<5 ms**, with about **500 constraints per organ typical, ~2,000 "optimal", and up to ~7,000 before instability is noticeable** ([Moore 2023](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156)). This is very modest. A parallel/SIMD solver or GPU XPBD should scale well beyond it.
  - The IMA simulator ran at **60 Hz visual, 1 kHz haptics, PBD at 5 ms step with 5 iterations** on an RTX 4080 with an i7-13700HK ([Wang 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/)).
  - Müller's 2003 SPH ran 5,000 particles at 25 fps on 2003 hardware ([sca03](https://matthias-research.github.io/pages/publications/sca03.pdf)). Modern GPUs handle tens of thousands at 60 Hz **(uncertain)**.
- **Proposed targets** (desktop/PC VR):
  - **active** high-detail region (the current surgical step): 5–15k tets plus 20–60k constraints
  - **passive** organs: low-res (≤2k tets) or kinematic
  - **render meshes** of 50–200k triangles per hero organ via embedding
- **Level-of-detail by surgical phase:** only the tissues relevant to the current step (research 01 phases) are fully simulated. The others are frozen, kinematic or cached. This is the single most important performance lever.
- **Quest 3 standalone (if ever):** total ≤2–3k tets, no SPH, baked lighting, under 200 draw calls. This is a reduced "lite" mode and not a v1 target.

### 5.4 Engine-specific performance notes

- **UE:** deforming meshes must avoid CPU re-upload of large vertex buffers every frame. Instead, upload the simulation positions (small) to a GPU buffer and compute render vertices in a compute pass (Mesh Deformer/Deformer Graph, or a custom vertex factory; Deformer Graph status in 5.8 is **(uncertain)**). Topology changes from cutting re-upload only the affected render **chunks**, so split organs into chunks of about 5–10k triangles.
- **UE VR:** use forward shading plus MSAA for VR (Meta's recommendation for Quest, generally good for PC VR as well), Instanced Stereo, and baked lighting with a few dynamic shadowed lights (OR lamps).
- **Unity (fallback):** use the `Mesh` API with `GraphicsBuffer`/`NativeArray` and compute-shader embedding. Burst/Jobs for a C# XPBD solver if TissueCore is not used.

---

## 6. Recommended stack

### 6.1 Primary stack

| Layer | Choice | License | Why |
|---|---|---|---|
| Platform | **Windows 10/11 PC**. Desktop 60 Hz first; PC VR (OpenXR) 90 Hz second | – | Realism needs desktop-class GPU and CPU. Haptic devices are USB/PC |
| Engine | **Unreal Engine 5.8** (pinned; evaluate UE6 only after its EA stabilizes, late 2027 at earliest) | UE EULA (free for personal use; royalty only above $1M/product) | Best rendering (Substrate, SSS, MegaLights, Lumen/Lumen Lite), MetaHumans, Chaos Cloth for drapes and sponges, native C++ for TissueCore/Pulse/haptics, OpenXR 1.1 |
| Tissue physics | **TissueCore**: own C++20 library, XPBD + substeps, tet/shell/rod constraints, cutting/tearing/suturing/needle/grasp. Reuses ideas and code from **PositionBasedDynamics (MIT)** and **iMSTK (Apache-2.0, sunset)** with notices kept | Own code + MIT + Apache-2.0 notices | No engine provides surgical soft tissue. Engine-agnostic means the fallback stays cheap |
| Thread | Cosserat-rod PBD + tridiagonal inextensibility + segment CCD | Own (papers cited) | Literature-proven for surgical thread and knots |
| Tetrahedralization | **UE Chaos Flesh Dataflow (TetWild / iso-surface stuffing)** in-engine; fTetWild offline if needed | UE EULA / MPL-2.0 (**UNVERIFIED**) | No extra dependency |
| Physiology | **Pulse 4.4** via the UE plugin, rebuilt for 5.8 (research 02) | Apache-2.0 | Two-way coupling with bleeding (iMSTK precedent) |
| Blood | Niagara GPU particles + pooled-volume height-field + render-target wetness. Optional SPH (own or Niagara compute) for desktop close-ups | UE EULA / own | Layered approach (§3.8) |
| Haptics (optional) | 3D Systems **Touch** + OpenHaptics / **HapticsDirect for Unreal**, or **CHAI3D** device layer (BSD-3) for multi-vendor support. 1 kHz thread with virtual coupling | OpenHaptics/HapticsDirect **UNVERIFIED**; CHAI3D BSD-3 | Affordable, 1 kHz, and already has an Unreal plugin |
| VR | UE **OpenXR** plugin (vendor-neutral). Avoid relying on the Meta XR plugin (5.8 version mismatch under investigation) | UE EULA | PC VR across Quest Link, Index and Steam Frame |
| Offline calibration | **SOFA v26.06** (LGPL-2.1+) FEM reference scenes; **NVIDIA Warp** (Apache-2.0) for differentiable fitting | LGPL / Apache-2.0 | Tunes XPBD compliance to FEM-quality behaviour without running FEM at runtime |
| DCC | **Blender** (GPL; your output files are yours) for retopology, UVs, blend shapes, weight painting (from prior knowledge, not re-verified) | GPL-2.0+ (tool only) | Free |

### 6.2 Fallback stack (if UE C++ velocity is too slow for a solo developer, or VR becomes the primary target)

| Layer | Choice | License |
|---|---|---|
| Engine | **Unity 6.3 LTS**, or the next LTS when released. **URP** (Unity's long-term focus; also the only Quest path), or HDRP for desktop visuals, accepting its maintenance-only status | Unity Personal (free to $200k; splash optional) |
| Tissue physics | **Same TissueCore** via a C API and P/Invoke native plugin (preferred). Or, for a fast prototype: **Obi Softbody $55 + Obi Rope $37 + Obi Fluid $60** (XPBD, CPU/GPU), or **SofaUnity** (free; Windows-only; FEM with cutting demos) | Own / Standard Asset Store EULA (per seat) / Standard EULA + LGPL SOFA DLLs |
| Physiology | **Pulse Unity** asset (free, Apache-2.0; IL2CPP caveat) | Apache-2.0 |
| Haptics | HapticsDirect for Unity (**UNVERIFIED** license) or CHAI3D via native plugin | – |
| VR | Unity OpenXR + Unity OpenXR: Meta | Unity |

**Not recommended: Godot 4.7.** It is MIT and very approachable, with good OpenXR, but its renderer, its soft-body support (no cutting) and the absence of any medical-simulation ecosystem make "as close as possible to real" much harder. It is acceptable only for throwaway 2D/UI or logic prototypes.

### 6.3 De-risking spikes (to schedule in the roadmap, before content production)

| # | Spike | Pass criterion | Time box |
|---|---|---|---|
| S1 | TissueCore XPBD tet organ in UE 5.8: grasp, retract, and a blade cut through an authored zone | 10k tets, ≥120 Hz physics with 4 substeps, <6 ms per frame, no tunnelling, no explosion after 100 random cuts | 2–3 weeks |
| S2 | Suture: curved needle puncture/insertion, thread sliding, purse-string cinch, gesture-triggered square knot | 200-segment thread stable at 120 Hz, knot holds under tension, <0.5 ms | 2 weeks |
| S3 | Blood: Pulse-driven pulsatile jet from an aortotomy, pooling, suction returning volume, wetness mask | Bleed volume matches Pulse hemorrhage within 5%. GPU <1.5 ms at 1080p | 1–2 weeks |
| S4 | Beating heart: blend-shape targets driven by Pulse LV volume and HR, plus an XPBD follow shell indented by a tool; switch to arrest/VF | Visually plausible at HR 60–120, indentation stable | 1–2 weeks |
| S5 | Haptics: Touch at 1 kHz with virtual coupling against S1 tissue | No buzzing or instability. Force is continuous across cuts | 1 week (needs device) |
| S6 | PC VR 90 Hz: S1+S3+S4 scene in OpenXR | ≥90 fps sustained on reference GPU with no reprojection | 1 week |

If S1/S2 take more than 2× their time box in UE, re-run them in Unity with Obi to compare velocity. That comparison is the trigger for the fallback stack.

---

## 7. Open questions

1. **Chaos Flesh status label and runtime API in 5.8**: is it still Experimental? Can tet topology be modified at runtime? The docs do not say. If yes, it could host some non-cut tissues.
2. **Niagara Fluids status in 5.8** (production vs experimental): sources conflict, and the docs warn of GPU crashes on Windows.
3. **OpenHaptics / HapticsDirect license terms** and whether a free developer edition still exists in 2026.
4. **Pulse UE plugin rebuild for 5.8**: effort unknown (research 02 flags UE 5.4+ as "build from source").
5. **Reference hardware** the owner actually has (GPU/CPU, headset, haptic device or none). It changes the budgets in §5.
6. **Target scale of interactivity**: how much is fully simulated vs authored/guided? This is a game-design decision for Step 2 that sets the TissueCore scope.
7. **Meta XR plugin vs pure OpenXR in UE 5.8**: whether passthrough or Meta-specific features are wanted at all (probably not, for a fully virtual OR).
8. **fTetWild and TetGen licenses** (marked UNVERIFIED), if an external tetrahedralizer is needed beyond UE Dataflow.
9. **MetaHuman licensing outside Unreal**: only relevant if the fallback to Unity happens. One 2026 blog contradicts the 2025 change; check Epic's current license FAQ.

---

## 8. Sources (main ones, grouped)

- **Engines:**
  - Unreal: [UE 5.8 announcement](https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available), [5.8 release notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?lang=en-US), [State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show), [Chaos Flesh docs](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh-overview), [Niagara Fluids docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-fluids-in-unreal-engine)
  - Unity: [Unity pricing updates](https://unity.com/products/pricing-updates), [Unity render-pipeline strategy 2026](https://unity.com/topics/render-pipelines-strategy-for-2026), [Unity 6.3 physics overview](https://docs.unity.com/en-us/engine/6000.3/manual/physics-section/physics-overview), [Unity Meta Quest docs](https://docs.unity3d.com/6/Documentation/Manual/xr-meta-quest-develop.html)
  - Godot: [Godot license](https://godotengine.org/license/), [Godot soft body docs](https://docs.godotengine.org/en/stable/tutorials/physics/soft_body.html), [Godot Android XR docs](https://docs.godotengine.org/en/4.7/tutorials/xr/deploying_to_android.html)
  - Meta: [Meta Quest 3 vs 2 optimization](https://developers.meta.com/vr/resources/device-optimization-comparison/), [Meta UE forward renderer](https://developers.meta.com/horizon/documentation/unreal/unreal-forward-renderer/)
  - MetaHuman: [MetaHuman license (CG Channel)](https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/)
- **Simulation frameworks:**
  - SOFA: [SOFA GitHub](https://github.com/sofa-framework/sofa), [SofaUnity](https://github.com/InfinyTech3D/SofaUnity), [SofaUE5-Renderer](https://github.com/InfinyTech3D/SofaUE5-Renderer)
  - iMSTK: [iMSTK paper](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2023.1130156), [iMSTK repo (sunset notice)](https://github.com/Kitware/iMSTK), [iMSTK + Pulse](https://www.kitware.com/imstk-integrates-pulse-physiology/)
  - Libraries: [PositionBasedDynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics), [PhysX](https://github.com/NVIDIA-Omniverse/PhysX), [Warp](https://github.com/NVIDIA/warp), [Obi](https://obi.virtualmethodstudio.com/)
- **Papers:**
  - Solvers: [XPBD 2016](https://matthias-research.github.io/pages/publications/XPBD.pdf), [Small Steps 2019](https://diglib.eg.org/handle/10.1145/3309486-3340247)
  - Cutting: [Cutting survey 2015](https://diglib.eg.org/handle/10.1111/cgf12528), [PBD cutting 2017](https://doi.org/10.1109/MCG.2017.45), [Courtecuisse 2014](https://hal.archives-ouvertes.fr/hal-01097108)
  - Thread: [Cosserat PBD 2016](https://animation.rwth-aachen.de/media/papers/2016-SCA-Cosserat-Rods.pdf), [Surgical thread 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6015127/), [Knot tying 2004](https://doi.org/10.1007/s00371-003-0226-y)
  - Fluids: [SPH 2003](https://matthias-research.github.io/pages/publications/sca03.pdf), [SPH blood 2004](https://cgweb.informatik.uni-freiburg.de/publications/2004_THC_bloodSimulation.pdf), [Screen-space fluids 2009](https://www.win.tue.nl/~wstahw/edu/2IV05/andrei/particle_rendering/provided/p91-van_der_laan.pdf)
  - Surgical simulators: [IMA harvest simulator 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939391/), [PBD beating heart 2021](https://doaj.org/article/cb9d85655d3148b08962356cdf1bca8a), [Viscoelastic PBD 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5830759/)
- **Haptics and tracking:** [3D Systems Touch](https://www.3dsystems.com/haptics-devices/touch), [OpenHaptics](https://est-kl.com/openhaptics), [CHAI3D license](https://chai3d.org/download/license), [omega.3 spec](https://www.forcedimension.com/images/doc/specsheet_-_omega3.pdf), [libnifalcon](https://github.com/libnifalcon/libnifalcon), [SenseGlove Nova 2](https://www.senseglove.com/product/nova-2/), [Quest 3 hand tracking](https://ericg5.github.io/ResearchPortfolio/papers/characterization), [Quest 2 hand tracking](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/)
