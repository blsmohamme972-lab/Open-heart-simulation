# Evidence check 04: Game engine and simulation technology

> Checked 2026-11-03 by an independent fact-checker (fresh searches). Counts: confirmed 13, corrected 4, refuted 0, unverified 0. (The 12 claims flagged in INDEX.md: confirmed 9, corrected 3, refuted 0, unverified 0. The 5 extra checks: confirmed 4, corrected 1.)
>
> Method: I ran fresh web searches and opened the pages with a page reader (WebFetch). Release dates with a year were taken from GitHub release Atom feeds (`releases.atom`), because the release pages show only day and month. Some pages blocked the reader: unrealengine.com (license page, news pages; HTTP 403), kickstarter.com (403), the Vega FEM host (503), and dblp. Evidence from a search snippet only is marked "snippet". This file is research for a game. It is not clinical guidance.

## Verdict table

| ID | Claim (short) | Verdict | Correct value / note | Evidence [links] | Grade A/B/C |
|---|---|---|---|---|---|
| 04.1 | UE royalty 5% above first US$1M; 3.5% if also on EGS "since Oct 2024"; non-game seat fee US$1,850/seat/yr | CORRECTED | 5% of lifetime gross above the first US$1M is right, and EGS sales are royalty-free. Seat fee is right: US$1,850 per seat per year for non-game companies with > US$1M annual gross revenue, in force from UE 5.4 (late April 2024). **But the 3.5% rate was only announced in Oct 2024. It applies from 1 Jan 2025, and only if the game launches on the Epic Games Store at the same time as, or before, other PC/Android stores.** Otherwise the rate reverts to 5%. | [PocketGamer.biz 2 Oct 2024](http://www.pocketgamer.biz/unreal-engine-royalty-fee-reducing-to-35-for-games-landing-on-epic-games-store-on-launch-day/); [GameFromScratch](https://gamefromscratch.com/unreal-engine-launch-everywhere-with-epic/); [Engadget 12 Mar 2024](https://www.engadget.com/epic-will-charge-non-game-developers-1850-per-seat-to-use-unreal-engine-162015997.html); [Epic FAQ (snippet)](https://www.unrealengine.com/en-US/faq) | B (official page 403) |
| 04.2 | UE 5.8 released 17 Jun 2026; last UE5 release; UE6 previews ~late 2027 | CONFIRMED | Released 17 June 2026 at State of Unreal (Unreal Fest Chicago). Epic calls 5.8 the last **planned** major UE5 release, and does not rule out a 5.9. UE6 Early Access / first public preview is targeted for the end of 2027, with the full release 12-18 months later. I found no source for the "23 June" Epic homepage date. | [Epic forum post 17 Jun 2026](https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274); [80.lv](https://80.lv/articles/unreal-engine-5-8-is-out-today-with-big-optimization-improvements-and-mesh-terrain); [PCGH](https://www.pcgameshardware.de/Unreal-Engine-Software-239301/News/State-of-Unreal-2026-UE6-UE-5-8-MegaLights-1545629/); [GameBusiness.jp](https://www.gamebusiness.jp/article/2026/06/19/27258.html); [WN Hub](https://wnhub.io/news/engines/item-51157) | B |
| 04.3 | Unity Personal free to US$200k revenue+funding, splash optional; Pro US$2,310/yr from 12 Jan 2026; Havok dropped from 6.3 | CONFIRMED | Unity page: "up to $200,000 in revenue and funding"; "Splash screen optional with Unity 6"; Pro "$2,310/yr per seat" ($210/mo). The FAQ says Havok is dropped "starting with Unity 6.3 LTS". The summary line on the same page says "6.0 LTS", which is the inconsistency the report noted. CG Channel independently confirms the 5% rise on 12 Jan 2026 and Havok removal "beginning with the upcoming Unity 6.3 LTS release". | [Unity pricing updates](https://unity.com/products/pricing-updates); [CG Channel 10 Nov 2025](https://www.cgchannel.com/?p=171673) | A / B |
| 04.4 | Godot 4.7-stable 18 Jun 2026; Mobile renderer recommended for XR; SSS/SSR Forward+ only | CONFIRMED | GitHub Atom feed: 4.7-stable `2026-06-18T12:18Z` (the year is now confirmed). GamingOnLinux reported the release on 19 Jun 2026. Godot's 4.7.1 post (14 Jul 2026): "nearly four weeks since ... Godot 4.7". 4.7 release page: "we now recommend new XR projects use the Mobile renderer". In the 4.7 renderer tables, SSS, SSR, SDFGI and volumetric fog are supported only in Forward+. | [Godot releases feed](https://github.com/godotengine/godot/releases.atom); [Godot 4.7](https://godotengine.org/releases/4.7/); [Godot 4.7.1 post](https://godotengine.org/article/maintenance-release-godot-4-7-1/); [Renderers docs](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html); [GamingOnLinux](https://www.gamingonlinux.com/2026/06/godot-engine-4-7-is-out-bringing-a-new-asset-store-hdr-support-steam-frame-support/) | A |
| 04.5 | SOFA v26.06.00 published 15 Jul 2026; LGPL 2.1-or-later (applications/projects and tutorials GPL) | CONFIRMED | Atom feed: v26.06.00 `2026-07-15T14:10Z` (year confirmed). The sofa-framework.org news post "SOFA v26.06 has been released!" is dated 21 Jul 2026. README: LGPL "version 2.1 of the License, or (at your option) any later version". The GPL exceptions are applications/projects and applications/tutorials (GPL "version 2 ... or any later version"). There is also a third exception the report omits: "directories with a license file specifying a different license". | [SOFA releases feed](https://github.com/sofa-framework/sofa/releases.atom); [SOFA README](https://github.com/sofa-framework/sofa); [LICENSE-LGPL.md](https://raw.githubusercontent.com/sofa-framework/sofa/master/LICENSE-LGPL.md); [sofa-framework.org](https://www.sofa-framework.org/) | A |
| 04.6 | iMSTK discontinued 2 May 2025; Apache 2.0; last tag v7.0.0 (Sep 2023) | CONFIRMED | README: "Support and development ... has been discontinued as of May-02-2025"; "iMSTK is licensed under Apache 2.0". The GitLab tags API lists v7.0.0 as the latest tag (committed 2023-09-14), and the GitLab group is titled "iMSTK (ARCHIVED)". | [iMSTK README (raw)](https://gitlab.kitware.com/iMSTK/iMSTK/-/raw/master/README.md); [GitLab tags API](https://gitlab.kitware.com/api/v4/projects/iMSTK%2FiMSTK/repository/tags); [GitLab group](https://gitlab.kitware.com/iMSTK) | A |
| 04.7 | SofaUE5-Renderer is GPL-3, visual only, requires UE 5.0.3 | CONFIRMED | The full README was read, not just a snippet: "This Unreal Engine plugin is under GPL-3 license" (other licenses on request); "Unreal Engine version 5.0.3"; "SOFA version >= 22.12"; "only the VisualModel are mapped into UE5". Two-way coupling "will soon be avaible". The report's quote "two-way communication is not yet available" is a paraphrase, but the meaning is right. InfinyTech3D: rendering "without interaction". | [SofaUE5-Renderer](https://github.com/InfinyTech3D/SofaUE5-Renderer); [SOFA plugin page](https://www.sofa-framework.org/?p=23087) | A / B |
| 04.8 | SofaUnity: Standard Unity Asset Store EULA; only tested on Windows; SOFA > 23.06 | CONFIRMED | README: "Standard Unity Asset Store EULA"; "Only tested on Windows for now"; "SOFA version > 23.06". The Asset Store listing independently shows the Standard Unity Asset Store EULA, a free price, and v24.12.00 (8 May 2025). Its text (snippet) is stricter: "Linux, Mac or android support is not possible right now". | [SofaUnity](https://github.com/InfinyTech3D/SofaUnity); [Asset Store listing](https://assetstore.unity.com/packages/tools/physics/sofa-physics-engine-for-unity-270170) | A / B |
| 04.9 | 3D Systems Touch: 3.3 N max, > 0.88 N continuous, 1 kHz, ~0.055 mm; list US$2,800 | CORRECTED | All specs are right. The price is not: US$2,800 appears only on an unavailable MatterHackers listing. A current US reseller lists **US$3,910 (backorder, 4-6 weeks)**, and RS no longer stocks the device. There is no official price. Use **US$2,800-3,910**. | [3D Systems Touch](https://www.3dsystems.com/haptics-devices/touch); [RoboticsCenter listing](https://www.roboticscenter.ai/store/product/3dsystems-phantom-touch/); [MatterHackers](https://matterhackers.com/store/l/3d-systems-touch-haptic-device/sk/M12PCJ5U) | A (specs) / C (price) |
| 04.10 | Haply Inverse3: 0.01 mm, 4 kHz, up to 10 N; UK reseller £5,965.15 | CONFIRMED | Haply: "Up to 0.01 mm", "4 kHz" haptic refresh, "Up to 10 N". heise independently gives 0.01 mm and 4 kHz. Vertical Realities: £5,965.15, backordered, VAT status not stated. The workspace and continuous force are still not published, and the 10 N figure comes only from the manufacturer. | [Haply Inverse3](https://www.haply.co/inverse3); [heise](https://heise.de/-11132059); [Vertical Realities](https://shop.verticalrealities.com/products/inverse3) | A / B / C |
| 04.11 | Quest 3 hand tracking: 1.73 cm error and 38.33 ± 31.29 ms motion-to-photon "in best conditions" | CORRECTED | 1.73 cm (Quest Pro 1.22 cm) is the error "in best-performing conditions" (static test, knuckle tracking point), confirmed by the PubMed abstract. Jitter is 1.11 cm. **The 38.33 ± 31.29 ms motion-to-photon value is a mean from the dynamic test, not a best-case value.** The abstract calls latency "highly variable": 14.4-220.5 ms for Quest 3. | [PubMed abstract via Europe PMC, PMID 40053653](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Robotic%20Characterization%20of%20Markerless%20Hand-Tracking%22&resultType=core&format=json); [Author page](https://ericg5.github.io/ResearchPortfolio/papers/characterization); [DOI](https://doi.org/10.1109/TVCG.2025.3549182) | A / B |
| 04.12 | Quest 3: 72 Hz min (90 recommended), 13.8 ms, < 200 draw calls, < 1.5M triangles | CONFIRMED | Meta comparison page (fetched again): 72 Hz minimum, 90 Hz recommended, "13.8 ms (at 72 Hz)", "< 200" draw calls, "< 1.5M" triangles. Meta's Unreal guide agrees on the floor ("Interactive applications must achieve a minimum of 72 FPS"). It gives scenario ranges for Quest 3/3S: 200-300 draw calls (busy simulation), 400-600 (medium), 700-1000 (light), and 1.3-1.8M triangles. | [Meta device comparison](https://developers.meta.com/vr/resources/device-optimization-comparison/); [Meta Unreal guide](https://developers.meta.com/horizon/documentation/unreal/unreal-debug-android) | A |
| 04.X1 | Liu 2026 is a "VR proximal anastomosis for MIDCAB" simulator (Unity3D, Cosserat + XPBD, Geomagic Touch, validity 0.78 from 10 surgeons) | CORRECTED | The operation is wrong. The paper studies **vein-to-aorta (proximal) anastomosis in MICS CABG** (off-pump, multivessel CABG through a left intercostal incision; 132 cases by one surgeon), not MIDCAB. Everything else is right: Unity3D, Cosserat rods + XPBD for vessels and sutures, Geomagic Touch, 10 experts, validity index 0.78 (preliminary). | [Liu et al., Vessel Plus 2026;10:13](https://www.oaepublish.com/articles/2574-1209.2025.103) | A |
| 04.X2 | Nguyen 2020: only ~65% of approaches met real time; haptics 100-1000 Hz | CONFIRMED | "only 65% of the developed computational approaches really satisfied this constraint"; "This rate must be between 100 Hz and 1000 Hz". | [PMC7053477](https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477/); [HAL record](https://hal.sorbonne-universite.fr/hal-02550828) | A |
| 04.X3 | H3DAPI is GPL-2.0; last release 2.4.0 (29 Apr 2019) | CONFIRMED | GitHub README: "Released on: Mon, 29-Apr-2019"; the sidebar shows the GPL-2.0 license. MacPorts independently lists version 2.4.0 under "GPL-2+" (GPL-2.0 or later). | [H3DAPI GitHub](https://github.com/SenseGraphics/h3dapi); [MacPorts h3dapi](https://ports.macports.org/port/h3dapi/summary) | A / B |
| 04.X4 | Unity 6.0 LTS support ended Oct 2026; 6.3 LTS supported to Dec 2027 | CONFIRMED | "Unity 6.0 LTS is supported with two-year LTS through October 2026"; "Unity 6.3 LTS is supported with two-year LTS until December 2027". Enterprise and Industry plans get one extra year. | [Unity 6](https://unity.com/releases/unity-6); [Unity 6 support](https://unity.com/releases/unity-6/support) | A |
| 04.X5 | iMSTK paper: < 5 ms physics per frame, ~2,000 constraints optimal, ~7,000 before instability, haptics 500-1000 Hz, i9-12900HK laptop | CONFIRMED | Full text: "less than 5 milliseconds (ms) per frame"; "∼2000 constraints for optimal performance"; "up to ∼7000 constraints before simulation instability becomes noticeable"; "must execute at 500–1000 Hz"; "Core i9-12900 HK ... 32 GB of RAM". Knot detection is future work ("We will also integrate a knot detection algorithm"). The report's wording is a paraphrase. | [Moore et al. 2023, Frontiers in VR](https://www.frontiersin.org/articles/10.3389/frvir.2023.1130156/full) | A |

## Details

### 04-1
- PocketGamer.biz (2 Oct 2024): "Epic is lowering its royalty fee to 3.5% for games made in Unreal Engine starting January 1st, 2025", "those games must be released on launch day on the Epic Games Store", and "Epic currently charges ... a 5% fee on all lifetime revenue above $1 million".
- GameFromScratch: the program is called "Launch Everywhere with Epic". It requires an EGS release "before or at the same time you release it on other stores", and the rate reverts to 5% otherwise.
- Engadget (12 Mar 2024): US$1,850 per seat for non-game users; "Companies that make less than $1 million in annual gross revenue won't have to pay"; effective "with the release of Unreal Engine 5.4 in late April".
- The official license page still returned 403. An Epic FAQ snippet says "the 5% royalty is calculated on the amount over and above the first $1 million USD", provided the Release Form is filed on time.

### 04-2
- Epic forum announcement dated 17 Jun 2026; 80.lv "Unreal Engine 5.8 is Out Today" (17 Jun 2026).
- PCGH: "Die UE 5.8 ist nach derzeitiger Planung die letzte große Ausgabe der Reihe" ("by current plans, UE 5.8 is the last major release in the series"). A 5.9 is left open. UE6: "Eine erste öffentliche Vorschau ... für das Ende des Jahres 2027", with the finished version "12 bis 18 Monate später".
- GameBusiness.jp (19 Jun 2026): UE6 early access is planned for the end of 2027, with the full release 12-18 months later.

### 04-3
- Unity pricing page (fetched again): Personal "up to $200,000 in revenue and funding"; "Splash screen optional with Unity 6"; Pro "$2,310/yr per seat, prepaid yearly", "$210/mo"; Runtime Fee cancelled "As of September 12, 2024".
- CG Channel: "a 5% increase in the price of its Pro and Enterprise subscriptions on 12 January 2026", and Havok is removed "beginning with the upcoming Unity 6.3 LTS release".

### 04-4
- GitHub `releases.atom`: 4.7-stable updated 2026-06-18T12:18:02Z; 4.7.1-stable 2026-07-14. In the same feed, 4.7.2-stable shows 2026-08-22, while the report gives 18 Aug from gamedev.net. That date was not flagged and was not checked further.
- The 4.7 docs renderer tables show SSS, SSR, SDFGI and volumetric fog as "Not supported" in Compatibility and Mobile, and "Supported" in Forward+. Mobile is "Recommended for desktop and standalone headsets".

### 04-5
- `releases.atom`: v26.06.00 2026-07-15T14:10:08Z; v25.06.00 2025-07-24. v25.12.00 shows 2026-02-11 in the feed (the Atom "updated" time); the releases page shows 05 Feb.
- README license text is quoted in the table. LICENSE-LGPL.md is "Version 2.1, February 1999" with the "any later version" clause.

### 04-6
- README (raw): discontinued "as of May-02-2025"; "licensed under Apache 2.0".
- Tags API: v7.0.0 committed 2023-09-14, v6.0.0 2022-06-21, v5.0.0 2021-10-01.

### 04-7
- README: GPL-3; UE 5.0.3; SOFA >= 22.12 with SofaPhysicsAPI; only VisualModel components are mapped. A future two-way integration "will soon be avaible" (sic).
- This was a snippet-only claim in the report. It is now confirmed from the full page.

### 04-8
- README quotes are given in the table. The Unity Asset Store listing shows a free "Extension Asset" under the "Standard Unity Asset Store EULA", latest version 24.12.00 (8 May 2025).

### 04-9
- 3D Systems: "0.75 lbf (3.3 N)" max, "> 0.2 lbf (> .88 N)" continuous, "> 450 dpi (~0.055 mm)", "1 KHz refresh rate", 6-DOF sensing and 3-DOF force.
- RoboticsCenter: "$3,910.00 USD", backorder, 4-6 weeks. MatterHackers: "List Price $2,800.00", product unavailable.

### 04-10
- Haply product page: "Up to 0.01 mm", "4 kHz", "Up to 10 N". No workspace, DOF or price is given ("contact our team").
- heise: "resolves up to 0.01 mm", "refresh rate of 4 kHz". Vertical Realities: "£5,965.15", backordered.

### 04-11
- Abstract (PMID 40053653; IEEE TVCG 31(5):3025-3034, 2025): "in best-performing conditions, the Quest Pro outperformed the Quest 3 with 1.22 cm of average error compared to 1.73 cm"; jitter "1.77 cm and 1.11 cm"; latency "highly variable for the Quest Pro (15.8 - 229.2 ms) and Quest 3 (14.4 - 220.5 ms)".
- Author page: "motion-to-photon latency values of 33.20±18.01 ms and 38.33±31.29 ms". This was Test 3, which uses the dynamic trajectories.
- The conclusion (hand tracking is too coarse for mm-scale suturing) still holds.

### 04-12
- Meta comparison page quotes are given in the table. 1000/72 = 13.9 ms; Meta rounds it to 13.8 ms.
- Meta's Unreal guide scenario ranges are given in the table. The report's section 5.1 row (200-300 draw calls for a busy simulation; 1.3-1.8M triangles) matches the guide.

### 04-X1
- Abstract: "This study examines the learning curve for vein-to-aorta anastomosis in minimally invasive coronary artery bypass grafting (MICS CABG)"; "132 consecutive off-pump MICS CABG procedures with multi-vessel grafting"; "an overall validity index of 0.78 (exceeding the 0.7 threshold)".
- MIDCAB appears only in the Discussion, as the authors' earlier work. The Limitations section says comprehensive validity and reliability have not been established.

### 04-X2
- Results: "only 65% of the developed computational approaches really satisfied this constraint". Introduction: systems "hardly satisfied both acceptable model accuracy and real-time computation speed".

### 04-X3
- README: version 2.4.0 "Released on: Mon, 29-Apr-2019". MacPorts: version "2.4.0", license "GPL-2+". The "avoid (share-alike)" advice stands.

### 04-X4
- The Unity 6 page and the Unity 6 support page both give these dates. Unity docs label 6000.3 and 6000.0 as "LTS".

### 04-X5
- The full-text quotes are given in the table. They support the report's "≤ 5 ms physics" budget and its planning value of 2k-8k tets.

## Resolved open questions

1. **Exact UE EULA royalty and seat-fee terms (open question 1). Resolved from secondary sources; the official page is still 403.** The royalty is 5% of lifetime gross above the first US$1M per product, and EGS sales are royalty-free. Since 1 Jan 2025 the rate is 3.5% if the game launches on EGS at the same time as, or before, other PC/Android stores. Non-game companies with > US$1M annual gross revenue pay US$1,850 per seat per year (since UE 5.4, late April 2024). Students, educators and hobbyists stay free. [PocketGamer.biz](http://www.pocketgamer.biz/unreal-engine-royalty-fee-reducing-to-35-for-games-landing-on-epic-games-store-on-launch-day/); [Engadget](https://www.engadget.com/epic-will-charge-non-game-developers-1850-per-seat-to-use-unreal-engine-162015997.html). For this personal, non-commercial project there is no cost either way.
2. **Unity 6.6 / 6.7 / Unity 7 status (open question 9). Resolved.** The Unity docs version selector (Nov 2026) shows 7000.0 "Alpha", 6000.7 "Beta", 6000.6 "Current", 6000.3 "LTS", 6000.0 "LTS", and 6000.4/6000.5 "Legacy". Unity's 6.7 manual: "Unity 6.7 is a beta release". The public Unity 7.0 alpha was announced on Unity Discussions ("We're excited to kick off the public Alpha for Unity 7.0", ~6-9 Oct 2026). No official page found says that 6.7 will be an LTS. [Unity 6.6 manual](https://docs.unity.com/en-us/engine/6000.6/manual); [Unity 6.7 manual](https://docs.unity.com/en-us/engine/6000.7/manual); [Unity 7.0 alpha thread](https://discussions.unity.com/t/unity-7-0-alpha-is-now-available/1738310).
3. **Chaos Flesh maturity in UE 5.8 (open question 6). Partly resolved.** The UE 5.8 API plugin index gives the plugin path as `Engine\Plugins\Experimental\ChaosFlesh\ChaosFlesh.uplugin`, so it still ships as an **Experimental** plugin. The 5.8 release notes list its new features ("In UE 5.8, Chaos Flesh includes: ...") with no maturity label. [UE API ChaosFlesh](https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/ChaosFlesh); [UE 5.8 notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes).
4. **Haply Inverse SDK loop rate over WebSocket (open question 3). Partly resolved.** Haply's protocol docs say the simulation channel is a WebSocket on port 10001, and "The service sends exactly one state update for each message it receives from your client". The cadence "is entirely driven by your send rate". So Isaac Lab's 200 Hz is Isaac Lab's own streaming choice, not a device or SDK limit. The docs give no maximum rate, so a benchmark of the real round-trip rate is still needed. [Haply WebSocket protocol](https://docs.haply.co/inverseSDK/service/realtime/websocket-protocol); [Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/source/how-to/haply_teleoperation.html).

Not resolved:
- **SOFA-UE5 Kickstarter outcome.** The forum post (19 Nov 2025) says only "This plugin will be open-source", has no replies or updates, and the Kickstarter page returned 403.
- **Vega FEM.** The USC host returned 503. Mirrors say 4.0 is BSD 3-clause (snippet only).

## Edits made to the report

File: `research/04-engine-simulation-tech.md`

1. Section 1.2, Unreal row: "Since Oct 2024 the rate is 3.5% if the game also ships on the Epic Games Store." -> "Since 1 Jan 2025 (announced Oct 2024, "Launch Everywhere with Epic") the rate is 3.5% if the game launches on the Epic Games Store at the same time as, or before, other PC/Android stores; otherwise it reverts to 5% [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-1]."
2. Key claims row 4: "3.5% if also on the Epic Games Store (since Oct 2024)" -> "3.5% if the game launches on the Epic Games Store at the same time as or before other stores (from 1 Jan 2025; announced Oct 2024) [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-1]".
3. Section 4.1, Touch price cell: "List **US$2,800** at one reseller ("currently unavailable"; uncertain)" -> "List **US$2,800** at one reseller ("currently unavailable"); a current US reseller lists **US$3,910** (backorder). No official price [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-9]".
4. Summary, key finding 8: "Touch (3.3 N, 1 kHz, ~US$2,800 list)" -> "Touch (3.3 N, 1 kHz, ~US$2,800-3,910 at resellers [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-9])".
5. Section 0, VR hand tracking row: "Quest 3 hand-tracking error is 1.73 cm in the best case, motion-to-photon 38 ms" -> "Quest 3 hand-tracking error is 1.73 cm in the best-performing (static) conditions; mean motion-to-photon latency is 38 ms (± 31 ms) in dynamic tests, and overall latency ranges 14.4-220.5 ms [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-11]".
6. Section 4.4, motion-to-photon row: "**38.33 ± 31.29 ms**" -> "**38.33 ± 31.29 ms** (dynamic tests, not best case; overall latency 14.4-220.5 ms) [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-11]".
7. Key claims row 24: "1.73 cm error, 38.33 ms motion-to-photon (best conditions)." -> "1.73 cm error (best-performing static conditions); 38.33 ± 31.29 ms motion-to-photon (dynamic tests; overall latency 14.4-220.5 ms) [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-11]."
8. Section 2.3, Liu row: "**VR proximal anastomosis for MIDCAB** (most heart-relevant)" -> "**VR proximal (vein-to-aorta) anastomosis for MICS CABG** (minimally invasive multivessel CABG, not MIDCAB) [Step 2 check: corrected, see verification/04-engine-simulation-tech-check.md#04-x1] (most heart-relevant)".

No item was UNVERIFIED, so no "(unverified in Step 2)" markers were added.

## Sources

1. PocketGamer.biz, "Unreal Engine royalty fee reducing to 3.5% ..." (2 Oct 2024) - http://www.pocketgamer.biz/unreal-engine-royalty-fee-reducing-to-35-for-games-landing-on-epic-games-store-on-launch-day/
2. GameFromScratch, "Unreal Engine Launch Everywhere with Epic" - https://gamefromscratch.com/unreal-engine-launch-everywhere-with-epic/
3. Engadget, "Epic will charge non-game developers $1,850 'per seat'" (12 Mar 2024) - https://www.engadget.com/epic-will-charge-non-game-developers-1850-per-seat-to-use-unreal-engine-162015997.html
4. Epic Unreal Engine FAQ (snippet; page 403) - https://www.unrealengine.com/en-US/faq
5. Epic forum, "Unreal Engine 5.8 Released" (17 Jun 2026) - https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274
6. 80.lv, "Unreal Engine 5.8 is out today" - https://80.lv/articles/unreal-engine-5-8-is-out-today-with-big-optimization-improvements-and-mesh-terrain
7. PC Games Hardware, "State of Unreal 2026" - https://www.pcgameshardware.de/Unreal-Engine-Software-239301/News/State-of-Unreal-2026-UE6-UE-5-8-MegaLights-1545629/
8. GameBusiness.jp (19 Jun 2026) - https://www.gamebusiness.jp/article/2026/06/19/27258.html
9. WN Hub, UE 5.8 and UE6 date - https://wnhub.io/news/engines/item-51157
10. Unity, "Changes to Unity subscription plans and pricing" - https://unity.com/products/pricing-updates
11. CG Channel, Unity 2026 price changes (10 Nov 2025) - https://www.cgchannel.com/?p=171673
12. Unity 6 releases - https://unity.com/releases/unity-6 ; support page - https://unity.com/releases/unity-6/support
13. Unity 6.6 / 6.7 manuals (version selector) - https://docs.unity.com/en-us/engine/6000.6/manual ; https://docs.unity.com/en-us/engine/6000.7/manual
14. Unity Discussions, "Unity 7.0 Alpha is now available" - https://discussions.unity.com/t/unity-7-0-alpha-is-now-available/1738310 ; "Unity 7 is here" - https://discussions.unity.com/t/unity-7-is-here/1738415
15. Godot GitHub releases feed - https://github.com/godotengine/godot/releases.atom
16. Godot 4.7 release page - https://godotengine.org/releases/4.7/ ; 4.7.1 post - https://godotengine.org/article/maintenance-release-godot-4-7-1/
17. Godot renderers docs (4.7) - https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html
18. GamingOnLinux, Godot 4.7 is out (19 Jun 2026) - https://www.gamingonlinux.com/2026/06/godot-engine-4-7-is-out-bringing-a-new-asset-store-hdr-support-steam-frame-support/
19. SOFA GitHub releases feed - https://github.com/sofa-framework/sofa/releases.atom ; README - https://github.com/sofa-framework/sofa ; LICENSE-LGPL.md - https://raw.githubusercontent.com/sofa-framework/sofa/master/LICENSE-LGPL.md ; site - https://www.sofa-framework.org/
20. iMSTK README (raw) - https://gitlab.kitware.com/iMSTK/iMSTK/-/raw/master/README.md ; tags API - https://gitlab.kitware.com/api/v4/projects/iMSTK%2FiMSTK/repository/tags ; group - https://gitlab.kitware.com/iMSTK
21. SofaUE5-Renderer - https://github.com/InfinyTech3D/SofaUE5-Renderer ; SOFA plugin page - https://www.sofa-framework.org/?p=23087
22. SofaUnity - https://github.com/InfinyTech3D/SofaUnity ; Asset Store listing - https://assetstore.unity.com/packages/tools/physics/sofa-physics-engine-for-unity-270170
23. Unreal forum, SOFA-UE5 Kickstarter post - https://forums.unrealengine.com/t/bringing-sofa-physics-engine-biomechanical-simulation-to-unreal-engine-5-kickstarter-now-live/2676465
24. 3D Systems Touch - https://www.3dsystems.com/haptics-devices/touch
25. RoboticsCenter Touch listing - https://www.roboticscenter.ai/store/product/3dsystems-phantom-touch/ ; MatterHackers - https://matterhackers.com/store/l/3d-systems-touch-haptic-device/sk/M12PCJ5U
26. Haply Inverse3 - https://www.haply.co/inverse3 ; heise - https://heise.de/-11132059 ; Vertical Realities - https://shop.verticalrealities.com/products/inverse3
27. Haply WebSocket protocol docs - https://docs.haply.co/inverseSDK/service/realtime/websocket-protocol ; Isaac Lab Haply - https://isaac-sim.github.io/IsaacLab/main/source/how-to/haply_teleoperation.html
28. Godden, Steedman, Pan 2025, IEEE TVCG 31(5):3025-3034, PMID 40053653 (Europe PMC record) - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Robotic%20Characterization%20of%20Markerless%20Hand-Tracking%22&resultType=core&format=json ; author page - https://ericg5.github.io/ResearchPortfolio/papers/characterization
29. Meta device optimization comparison - https://developers.meta.com/vr/resources/device-optimization-comparison/ ; Meta Unreal guide - https://developers.meta.com/horizon/documentation/unreal/unreal-debug-android
30. Liu et al. 2026, Vessel Plus 10:13 - https://www.oaepublish.com/articles/2574-1209.2025.103
31. Nguyen, Ho Ba Tho, Dao 2020, Applied Bionics and Biomechanics - https://pmc.ncbi.nlm.nih.gov/articles/PMC7053477/
32. H3DAPI GitHub - https://github.com/SenseGraphics/h3dapi ; MacPorts - https://ports.macports.org/port/h3dapi/summary
33. Moore et al. 2023, iMSTK, Frontiers in VR - https://www.frontiersin.org/articles/10.3389/frvir.2023.1130156/full
34. UE 5.8 API plugin index, ChaosFlesh - https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/ChaosFlesh ; UE 5.8 release notes - https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes
