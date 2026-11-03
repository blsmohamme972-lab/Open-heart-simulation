# Android review — engine and rendering

Research accessed **2026-11-03**. This replaces the desktop engine recommendation for the corrected Android scope. It is planning only: no builds, assets, frame rates or device tests were produced. Scope here is rendering supporting heart animation and surgical-tool interaction; full-case physiology and OR production are outside this review.

## Provisional decision

Start the comparison with **Godot Mobile on Vulkan**, using an explicitly declared high-end Android device tier. This satisfies an open-source-first engine preference and gives an integrated editor, scene system and Android export path. Maintain a separately tested **Compatibility/OpenGL ES** visual tier only if broader device coverage is required. Do not promise identical appearance between renderers. Godot documents different feature sets and recommends Mobile/Compatibility instead of Forward+ for mobile workloads. [Renderer overview](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html)

This recommendation is conditional: anatomy readability, tool contact, heart motion and sustained performance must pass together. “World-class” is a quality goal requiring comparison evidence, not a property conferred by an engine name. If Godot cannot meet the agreed scene after a bounded optimization experiment, compare **Unity URP** if a proprietary engine is acceptable. If open source is mandatory, the alternative is a substantially more expensive custom Android application around **Filament**; it is not a drop-in game engine.

## Corrections to the previous plan

| Previous assumption | Android correction |
|---|---|
| Unreal preferred because of desktop materials and C++ | Evaluate mobile renderers on actual Android GPUs; desktop screenshots are not selection evidence. |
| Desktop 1080p/60 and 120 Hz tissue worker | Neither is an Android guarantee. Define device, render resolution and sustained thermal workload before budgets. |
| Standard subsurface shading provides realistic tissue | Godot's built-in SSS is Forward+ only; Mobile needs a custom approximation or another tested solution. |
| Portable native core makes integration straightforward | Android adds ABI/build/driver/lifecycle constraints; GPU compute capability does not establish reliability. |
| Filament is MIT | Official Filament license is **Apache-2.0**. |
| Free or open engine clears anatomy rights | Engine, models, texture sources and derivatives need independent license records. |

Godot's SSS limitation is explicit in its [material guide](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html#subsurface-scattering); Filament's terms are explicit in its [LICENSE](https://github.com/google/filament/blob/main/LICENSE).

## Candidate comparison

| Candidate | Android suitability and limitations | License/decision |
|---|---|---|
| Godot Mobile/Vulkan | Mobile-focused forward renderer; suitable candidate for a small, carefully lit operative field. Custom tissue shading and supported-device testing are required. | Engine **MIT**, with notices; third-party components retain their own terms. Provisional first choice. [Godot license](https://godotengine.org/license/) |
| Godot Compatibility/OpenGL ES | Broader hardware reach, fewer features; materials, lighting and texture imports may differ. Test this as an intentional quality tier rather than relying on an invisible runtime fallback. | Same engine license. Useful fallback for coverage, not proof of equal fidelity. [Renderer differences](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html) |
| Unity URP | Supports Vulkan and OpenGL ES 3.0+; selectable forward/deferred paths. URP and HDRP projects are not interchangeable, so desktop HDRP skin features cannot simply be carried over. | Proprietary Unity terms; open URP package source does not make the whole engine open source. Conditional fallback after a measured comparison. [URP compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/requirements.html), [editor terms](https://unity.com/legal/editor-terms-of-service/software) |
| Unreal mobile renderer | Mobile Forward supports precomputed-lighting workflows; Mobile Deferred offers a different light/shader tradeoff. Desktop rendering on mobile is documented as experimental/costly. Standard mobile paths do not provide Nanite/Lumen. | Proprietary EULA, source access with restrictions. Include only if a specific mobile prototype beats alternatives; no desktop-quality presumption. [Shading modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-rendering-and-shading-modes-for-unreal-engine), [mobile feature matrix](https://dev.epicgames.com/documentation/unreal-engine/rendering-features-reference), [EULA](https://www.unrealengine.com/eula/unreal) |
| Filament in a native Android application | Android-focused PBR renderer with material models including subsurface; application, authoring workflow, touch UI, collision, surgical state and asset management still need implementation/integration. | **Apache-2.0**, preserve applicable license/NOTICE obligations and third-party terms. Custom-renderer alternative only, not primary plan. [Project](https://github.com/google/filament), [materials](https://google.github.io/filament/Materials.md.html) |

An MIT engine does not require every asset to be MIT. CC BY or suitably handled CC BY-SA anatomy can coexist with an open engine, but attribution, derivative licensing and redistribution obligations remain. Conversely, a noncommercial asset is not automatically open source or suitable for a public asset repository. Asset clearance belongs to the separate item-level review.

## Android capability and sustained-performance requirements

Android documents Vulkan availability from API 24 and Vulkan 1.1 support on 64-bit Android 10+ devices. This does **not** mean identical extensions, texture formats, drivers or throughput. Android Vulkan Profiles define feature bundles with different coverage; their published percentages are dated observations, not this project's support promise. Query capabilities and test named physical devices instead of selecting by Android version alone. [Vulkan overview](https://developer.android.com/games/develop/vulkan/overview), [Android Vulkan Profiles](https://developer.android.com/ndk/guides/graphics/android-vulkan-profile)

Use at least one Adreno and one Mali/Immortalis device, plus the eventual lowest supported device. Record SoC/GPU, RAM, OS, driver, refresh rate and API/format features. Emulator or desktop editor success cannot establish phone performance. The native extension build must also survive background/resume, screen changes and graphics-context recreation without losing interaction state.

Frame pacing is distinct from average FPS. Android's Swappy library supports OpenGL and Vulkan presentation pacing. Verify the selected engine/version's actual integration and settings; do not assume enabling VSync alone is enough. Record present intervals and missed deadlines. [Android Frame Pacing](https://developer.android.com/games/sdk/frame-pacing)

ADPF exposes thermal/performance information so applications can adapt workload before it becomes unsustainable. Plan a supported Android integration, with a fallback policy when signals are unavailable. Reduce resolution, secondary shadows and decorative effects before altering anatomically meaningful geometry or contact behavior. Fixed-performance benchmarking is useful for comparisons but does not replace a normal-mode thermal soak. [ADPF overview](https://developer.android.com/games/optimize/adpf), [best practices](https://developer.android.com/games/optimize/adpf/best-practices-adpf)

Godot compute shaders require a RenderingDevice renderer, and its documentation specifically warns about mobile driver problems. Therefore baseline heart animation and local contact must not require a large GPU compute solver. Any compute deformation path needs device feature checks, measured synchronization cost and a CPU/authored fallback; avoid per-frame GPU readback for tool collision. [Compute shader documentation](https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html)

## Godot material limits that affect the decision

| Feature | Mobile / Compatibility | Forward+ |
|---|---|---|
| Built-in SSS and screen-space reflections | Neither supported | Supported |
| Screen/depth texture access | Both supported | Supported |
| Normal/roughness buffer | Neither supported | Supported |

These differences are documented in the [renderer matrix](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html). Screen-space **refraction** is distinct from reflection: it samples the image behind a transparent surface, cannot include off-screen objects or refract itself/other transparent layers, and can produce incorrect edge distortion. Alpha blending has ordering problems and does not cast shadows; depth pre-pass helps opaque portions but does not solve every transparent intersection. These restrictions also matter in Forward+. [Material transparency/refraction](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html)

**Required shader experiment:** opaque micro-normal/roughness tissue, region-specific thickness-based diffuse/backlight approximation, controlled specular wetness and reflection probes; optional shallow scattering lookup only if it improves reference agreement. Compare tissue boundaries, fat and coronary visibility under moving lights. Do not use transparent red material as a substitute for SSS, or promise visual parity with Forward+. If the approximation fails the visual gate, reconsider the renderer/engine before acquiring more content.

## Proposed visual pipeline

Prioritize the operative field: correct silhouette and coronary layout, stable close-up normals, believable wetness, coherent motion, readable tool tips and contact shadows. Use baked surrounding illumination and a tightly controlled movable surgical light. Start with opaque tissue plus a roughness/specular wetness mask; restrict translucent layers and blood particles because their overlap increases fragment cost and sorting artifacts. A thickness-informed scattering approximation must be reviewed under multiple light directions, not only its best screenshot.

Android recommends ASTC as a primary compression option with ETC2 fallback where needed. Godot's high-quality mobile import selects ASTC in Mobile/Forward+; Compatibility ignores that high-quality option and uses the other supported import path. Validate the shipped GPU format rather than the source PNG/JPEG size. Preserve sRGB color data separately from linear normal/roughness/thickness data, generate mipmaps, and test compressed coronaries and tool markings at the closest supported view. [Android texture guide](https://developer.android.com/games/optimize/textures), [Godot image import](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html)

Keep high-resolution authoring assets separate from runtime LODs. Render and collision meshes may differ but must share stable anatomical identifiers and transformations. A visually displaced heart surface with an unchanged collider fails the interaction requirement. Permit higher quality only after the base scene has thermal headroom; no unlimited-resolution textures, real-time ray tracing or arbitrary fluid solver is assumed.

## Concrete engine comparison and exit gates

**Proposed test fixture:** one licensed heart/thorax operative region, phase-driven heart animation, two articulated instruments, a localized indentation/grasp, one bounded incision transition, a small blood/wetness effect and touch controls. Use the same camera path, anatomy, motion, lighting intent, interaction script and presentation resolution in each candidate. Record equivalent feature settings rather than pretending all engines produce identical shading.

**Proposed engineering targets, not measurements:** aim initially for 60 FPS/16.67 ms on the selected high-end tier; test a deliberate 30 FPS/33.33 ms tier only if needed and reassess precision/usability. Start at a fixed 1920×1080-equivalent render workload, then evaluate adaptive resolution. No hardware-independent 60 FPS promise is made.

Run cold startup and 30-minute normal-mode sessions at recorded brightness, ambient conditions, charge state and display settings. Capture CPU/GPU timings, p95/p99 presented intervals, missed frames, thermal status, memory peaks/growth and touch-to-visible latency. Repeat the hardest camera/contact sequence after warming. Judge improvements at equal visual quality and include shader-compilation stalls and resume behavior.

Pass only if: (1) anatomical and contact review accepts the displayed scene; (2) all supported devices meet their declared sustained frame/latency envelopes; (3) no contact drift, missed input, corrupt materials or unbounded memory growth appears; (4) fallback behavior preserves interaction meaning; and (5) packaged dependency/asset licenses are complete. Set numeric latency and memory limits after selecting devices and performing an initial profile, before final acceptance.

If Godot misses a gate, first identify shader, animation, collision or platform overhead. Time-box one focused repair, then run the equivalent Unity URP comparison if proprietary licensing is acceptable. Escalate to Filament only with evidence that renderer control justifies building the missing engine systems. Final selection remains pending these future tests; this research itself demonstrates no performance result.

Searches covered official renderer features, Android Vulkan/device profiles, Swappy, ADPF, texture compression/import, compute constraints and engine licenses. The prior desktop-first recommendation is superseded for Android; no claim here depends on desktop Lumen/Nanite availability.
