# Research 03: Free assets and their licenses

> **Purpose.** This report finds free 3D, 2D and audio assets for a realistic open heart surgery simulation game. It records the exact license of each one. It also proposes a Blender asset pipeline and a license register (`ASSET_LICENSES.md`), so the project stays legal now (personal, non-commercial use) and later (if it is ever released publicly).
>
> **Researched 2026-11-03 (re-do, fresh searches).** Every license below was checked on the official page on this date, unless it is marked **UNVERIFIED** or "(uncertain - snippet only)".
>
> **Disclaimer.** This is planning research for a personal, educational game. It is **not clinical guidance**, not legal advice, and the game is not a certified medical device or training tool. License terms change. Re-check each license on its official page before you download, and again before any public release.
>
> **Research limit note.** The shared web-search budget for this workflow ran out near the end of this research. A few planned look-ups (CC0 tissue textures, the CTSNet video terms, the IEC alarm-sound standard) could therefore not be searched. They are marked as gaps. A follow-up run can fill them.

---

## 0. Summary for the plan

Abbreviations used in this report: **CC** = Creative Commons. **BY** = attribution required. **SA** = ShareAlike (adaptations must use the same license). **NC** = NonCommercial. **ND** = NoDerivatives (no modified versions may be shared). **CC0** = public-domain dedication (no conditions). **GPL/AGPL** = GNU (Affero) General Public License, a "copyleft" software license. **CPB** = cardiopulmonary bypass (heart-lung machine). **OR** = operating room. **LOD** = level of detail. **HDRI** = high-dynamic-range environment image. **GLB/glTF** = the Khronos 3D transmission format. **FBX** = Autodesk interchange format. **USD** = Universal Scene Description.

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Base heart + great vessels + sternum mesh | Use **BodyParts3D 4.0** downloaded directly from the DBCLS archive. Its license page now says **CC BY 4.0** (updated 2025-02-27), so no ShareAlike applies to our edits. It has named coronary branches, 3 of 4 valves and the sternum parts. Meshes are heavily reduced (99%), so plan a re-sculpt. | [lic page](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [download](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html), [parts list](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt) |
| Ready-made full-body anatomy in Blender | **Z-Anatomy** is the fastest start, but it is **CC BY-SA 4.0**, and some bundled parts are **CC BY-NC(-SA)**. Use it as a reference and for the thorax context. Keep SA meshes in a separate folder. | [Z-Anatomy repo](https://github.com/Z-Anatomy/Models-of-human-anatomy) |
| Second "clean" heart source | **Human Reference Atlas (HRA) 3D heart** (male + female GLB, v1.2 June 2022), **CC BY 4.0**. | [CCF 3D library](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html) |
| High-realism heart reference (scans of real hearts) | **Visible Heart Lab** Sketchfab models (for example Heart0102: RCA 3 branches, LAD 4, Cx 3) are **CC BY-NC 4.0**. They are fine for this personal project. They block any commercial release, so log them as "NC - replace before commercial use". | [Heart0102](https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea) |
| CABG (coronary artery bypass graft) look reference | **CU Anschutz plastinated "Human Heart Cardiac Bypass"** scan, **CC BY-NC-SA 4.0**, 1M triangles. Use it as a reference or for the personal build only. | [model page](https://sketchfab.com/3d-models/human-heart-cardiac-bypass-98dca43ff0c146b696148e6c3e70dbc0) |
| Patient-specific / extra anatomy | Segment CT with **TotalSegmentator** (Apache-2.0 code; heart chambers and coronary tasks need a free non-commercial license key) and convert to mesh in **3D Slicer** (BSD-style). Its training dataset v2.0.1 is **CC BY 4.0** (1,228 CTs, 117 structures). | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator), [Zenodo v2.0.1](https://zenodo.org/records/10047292), [Slicer](https://slicer.readthedocs.io/en/latest/user_guide/about.html) |
| OR room furniture | Sketchfab **CC BY** models: "Realistic Medical Equipment and Accessories Set" (surgical bed, dual-arm lights, console, cart) and "Operating Table". Light with Poly Haven **CC0** hospital HDRIs. | [equipment set](https://sketchfab.com/models/5460fb2767c6468eb88466d2555d273b), [operating table](https://sketchfab.com/models/e3a4512227d34b098e2ef0d11c8a80fd), [Hospital Room HDRI](https://polyhaven.com/a/hospital_room) |
| Cardiac instruments (sternal saw, Finochietto retractor, aortic cross-clamp, CPB machine) | No good free model was found for the sternal retractor or the sternal saw. The only free CPB model is low-detail. **Model these yourself in Blender** from manufacturer photos (reference only). Use the CC BY-NC "Surgical Instruments collection" only as a reference or a personal placeholder. | [Heartlung Machine (CC BY, 8.6k faces)](https://sketchfab.com/models/34f7d192bd8d4ca498b5e3d4948101ba), [instruments (CC BY-NC)](https://sketchfab.com/models/46f5799ca36240efae3abec6e61d4c8a) |
| Materials / textures | Poly Haven and ambientCG are **CC0** (no credit needed). Neither has tissue materials, so build tissue as **procedural Blender shaders** and hand-painted textures. | [Poly Haven license](https://polyhaven.com/license), [ambientCG license](https://docs.ambientcg.com/license/) |
| Megascans | Free claiming ended on 31 Dec 2024. Most Megascans are **paid on Fab** since 2025 under the Fab Standard License (usable in any engine). Do not depend on them. | [CG Channel](https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/), [Fab licenses](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab) |
| OR audio | Freesound **CC0** recordings made in real ORs exist: surgical suction in an OR, a full surgery field recording (2 min 36 s), a defibrillator/monitor, a ventilator. Fill the gaps (cautery, sternal saw, roller pump, IEC-style alarms) by recording or synthesizing your own sounds. | [OP suction CC0](https://freesound.org/people/fankitown/sounds/250348/), [surgery CC0](https://freesound.org/people/nicotep/sounds/632733/) |
| Big SFX library | **Sonniss GDC bundles**: royalty-free, no attribution, unlimited projects. 2024+ bundles reportedly forbid AI training. The license page could not be loaded, so keep a copy of the license with the files. | [GDC 2026 bundle news](https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/) |
| Patient body and OR staff | **MPFB 2.0.18** (Blender extension; GPL-3.0-or-later code, **CC0** core assets) for the patient and staff bodies. **Microsoft Rocketbox** (**MIT**, 115 rigged avatars, facial blendshapes) for background staff. **Mixamo** animations for idle/walk only (raw files cannot be redistributed). | [MPFB](https://extensions.blender.org/add-ons/mpfb/), [MakeHuman license](https://static.makehumancommunity.org/about/license.html), [Rocketbox](https://github.com/microsoft/Microsoft-Rocketbox) |
| MetaHuman | Allowed in **any engine since MetaHuman 5.6 (June 2025)**, free under USD 1M revenue, no AI training. It needs Epic cloud services for autorig. It is optional, and overkill for masked OR staff. | [MetaHuman 5.6 release post](https://forums.unrealengine.com/t/metahuman-5-6-release/2539165), [CG Channel](https://www.cgchannel.com/?p=167592) |
| Ready Player Me | **Do not use.** Public services shut down on 31 Jan 2026 after the Netflix acquisition. | [Wikipedia](https://en.wikipedia.org/wiki/Ready_Player_Me) |
| Blender version | **Blender 5.2 LTS** (released 14 July 2026). Blender output belongs to you. Add-ons are GPL. | [releases](https://www.blender.org/download/releases/), [license](https://www.blender.org/about/license/) |
| Export format | **glTF 2.0 (GLB)** as the main format (Khronos exporter bundled, Apache-2.0). Heartbeat as **shape keys → morph targets**. Skinning is limited to **4 bone influences per vertex**. FBX as a fallback. | [glTF-Blender-IO](https://github.com/KhronosGroup/glTF-Blender-IO), [4-influence commit](https://archive.blender.org/lists/bf-extensions-cvs/2022-April/010894.html) |
| License control | Keep one row per asset in `ASSET_LICENSES.md` (template in section 8). Tag each asset **GREEN** (CC0/CC BY/MIT), **AMBER** (SA, GPL, custom), **RED** (NC, ND, editorial, unknown). Only GREEN and handled-AMBER assets may enter a public build. | [CC BY-NC 4.0 legal code](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en), [CC attribution practice](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution) |

---

## 1. How to read this report

- **License status.** "Verified" means the license was read on the official page on 2026-11-03. "UNVERIFIED" means the official page could not be reached or does not state a license. "(uncertain - snippet only)" means only a search-result snippet was available.
- **Evidence grades.** A = primary or authoritative (official license page, official docs, peer-reviewed paper, dataset record). B = reputable secondary (university page, major news/trade site, vendor documentation). C = weak (forum, blog, snippet).
- **Personal use.** Every source in the "recommended" lists allows personal, non-commercial use. The questions that matter are (a) **attribution**, (b) **ShareAlike**, (c) **NoDerivatives**, and (d) **what happens on a public or commercial release**.
- **Sketchfab model links.** These use the short form `https://sketchfab.com/models/<uid>`. Data such as face counts and dates were read from Sketchfab's public API record for each model (for example `https://api.sketchfab.com/v3/models/<uid>`).

---

## 2. Anatomy sources

### 2.1 Overview table

| Source | What you get | License (verified on) | Personal use | Attribution / SA / ND | Grade |
|---|---|---|---|---|---|
| **BodyParts3D 4.0** (DBCLS, Japan) | Whole adult male body, OBJ meshes per FMA (Foundational Model of Anatomy) part; "BP3D_4.0" archives: IS-A tree 136 MB, PART-OF tree 62 MB, **99% polygon reduction** ([download](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html)) | **CC BY 4.0**, page updated 2025-02-27 ([lic](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html)). Older releases (3.0, 2011) were **CC BY-SA 2.1 Japan** ([README 2011/2013](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html)) | Yes | BY: "BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International" ([lic](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html)). No SA for the 4.0 download. | A |
| **Z-Anatomy** | Full Blender atlas (`Z-Anatomy.zip`) built from BodyParts3D, with Wikipedia definitions | **CC BY-SA 4.0** for Z-Anatomy content. Bundled parts: BodyParts3D CC BY-SA 2.1 JP, Dundee inner ear **CC BY-NC-SA 4.0**, kidney (Lissie Cowley) **CC BY-NC 4.0**, Brainder and white matter "no license stated" ([repo](https://github.com/Z-Anatomy/Models-of-human-anatomy)). No release version is published. | Yes | BY + **SA**. Some parts NC. | A |
| **Open Anatomy Project** (Brigham and Women's SPL) | 6 atlases, including a "Mauritanian Anatomy Laboratory Thoracic Atlas". No dedicated heart atlas ([openanatomy.org](https://openanatomy.org/)) | **UNVERIFIED**. The homepage states no license. The OABrowser GitHub repo shows no LICENSE file ([oabrowser](https://github.com/mhalle/oabrowser)). A Harvard NAC page says the atlas data is under "3D Slicer License section B" (uncertain - snippet only). | Probably | Unknown | B/C |
| **NIH 3D** (formerly 3D Print Exchange) | Many heart meshes, each with its **own license** | Per entry, for example: 3DPX-011381 heart from CT, **CC BY 4.0** ([entry](https://3d.nih.gov/entries/3DPX-011381)); 3DPX-000906 heart + aorta + kidneys, **CC BY 4.0** ([entry](https://3d.nih.gov/entries/3DPX-000906/2)); 3DPX-000900 heart from CT with Blender retopology, **CC BY-NC 4.0** ([entry](https://3d.nih.gov/entries/3DPX-000900/2)) | Yes | Read each entry | A |
| **Human Reference Atlas (HRA / HuBMAP CCF)** | Heart (male + female) 3D reference organ in GLB: v1.0 March 2021, v1.1 December 2021, **v1.2 June 2022** ([CCF library](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html)). The ccf-releases repo lists versions up to v2.0 ([repo](https://github.com/hubmapconsortium/ccf-releases)). | **CC BY 4.0** ("All CCF 3D reference objects are released under Attribution 4.0 International") ([CCF library](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html)) | Yes | BY only | A |
| **Visible Human Project** (US National Library of Medicine, NLM) | Raw CT/MRI and cryosection photographs (full colour 0.33 mm in-plane; 70 mm film 0.17 mm). PNG format recommended ([getting data](https://www.nlm.nih.gov/research/visible/getting_data.html)) | No license needed since July 2019. "Terms and Conditions" replaced the old license ([getting data](https://www.nlm.nih.gov/research/visible/getting_data.html)). The NLM terms require the credit line "Courtesy of the U.S. National Library of Medicine" and no implied endorsement ([NLM T&C](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html)). Whether the general NLM terms page covers VHP exactly is (uncertain). | Yes | Credit NLM | A |
| **Embodi3D** | Community medical 3D models | **UNVERIFIED**: the terms page returned HTTP 403 | Unknown | Unknown | - |
| **AnatomyTOOL** | Images and 3D links, each with its own license | Per item. Many items are **CC BY-NC-SA**. Some are public domain. The Minnesota beating-heart videos are "not under a Creative Commons license but free to use for educational purposes" (uncertain - snippet only) ([AnatomyTOOL](https://anatomytool.org/can-i-use)) | Mostly | Mostly BY-NC-SA | C |

### 2.2 BodyParts3D: the license changed (important)

- The **old** README (data release 3.0, updated 2011-09-15; README dated 2013-04-11) says: "BodyParts3D, Copyright© The Database Center for Life Science licensed by CC Attribution-Share Alike 2.1 Japan". It also says derivative works must use the same license ([README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html)).
- The **current** license page says: "The license for this database is specified in the Creative Commons Attribution 4.0 International", last updated **2025-02-27** ([lic](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html)).
- **Consequence.** If we download BodyParts3D **directly** from the current archive, our edits only need attribution (no ShareAlike). Meshes taken from **Z-Anatomy** remain CC BY-SA 4.0, because Z-Anatomy licenses its own work that way ([Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy)).
- **Mesh quality.** The current archive only offers the **99%-reduced** meshes ([download](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html)). The 3.0 release also offered a 95%-reduced set ([README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html)). Expect low-poly organs that need remeshing and sculpting.
- **Source body.** The project describes "a three-dimensional whole-body model for an adult human male". Last content update May 2013 ([desc](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/desc.html)).

**Heart-related parts present in BodyParts3D (3.0 parts list)** ([parts list](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt)):

| Group | FMA parts found |
|---|---|
| Coronary arteries (13) | right coronary artery (FMA50039), trunk of RCA, **marginal branch of RCA**, **posterior interventricular branch of RCA**, septal branches of RCA, **right posterolateral branch**, left coronary artery (FMA50040), stem of LCA, **anterior interventricular branch (LAD)** (FMA3862), septal branches of LCA, **circumflex branch** (FMA3895) |
| Valves (4 entries) | tricuspid (FMA7234), pulmonary (FMA7246), mitral (FMA7235), generic "anatomical valve". **No aortic valve entry was found** in the extraction (uncertain: it may be grouped elsewhere). |
| Chambers / walls (16) | right/left atrium, right/left ventricle, RV outflow part, interventricular septum, papillary muscles (RV anterior/posterior/septal, LV posterior), wall of heart, myocardium |
| Great vessels | aorta, ascending aorta, arch of aorta, descending/thoracic aorta, "pulmonary artery" (no separate pulmonary trunk entry), superior vena cava, inferior vena cava |
| Sternum (4) | sternum, manubrium, body of sternum, xiphoid process |
| Missing | **No pericardium**. No diagonal or obtuse marginal branches by name. No coronary sinus or cardiac veins were found in the extraction (uncertain). |

### 2.3 Anatomical accuracy comparison (for the "as real as possible" goal)

| Source | Coronary branches | Valves | Great vessels | Real-patient realism | Comment |
|---|---|---|---|---|---|
| BodyParts3D 4.0 | RCA, marginal, PDA, posterolateral, LM, LAD, Cx, septals ([parts list](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt)) | Tricuspid, pulmonary, mitral (aortic not found) | Aorta (ascending/arch/descending), pulmonary artery, SVC, IVC | Low (idealised, 99% reduced) | Best **labelled** base; needs a re-sculpt |
| Z-Anatomy | Same base as BodyParts3D, refined in Blender ([repo](https://github.com/Z-Anatomy/Models-of-human-anatomy)) | As BodyParts3D | As BodyParts3D | Low to medium | Fast thorax context; SA license |
| HRA heart v1.2 | Not stated on the library page (uncertain) | Not stated (uncertain) | Not stated (uncertain) | Medium (built from Visible Human data by a medical illustrator, uncertain - snippet only) | Clean CC BY GLB; inspect before choosing |
| Visible Heart Lab Sketchfab scans | Heart0102: RCA 3 branches, LAD 4, Cx 3, LCA 2 ([page](https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea)) | Not described | Partial | **High** (real human hearts) | NC license |
| UMCG "Anatomical heart" (left / right / co-dominance) | Explicit coronary-dominance variants ([left dominance](https://sketchfab.com/3d-models/anatomical-heart-left-dominance-5c10cea34fd54b5eb9e3d0ecc8ab0da2)) | Not described | Yes | Medium (refined BodyParts3D) | NC-SA; good for the "coronary dominance" variation rule |
| TotalSegmentator output | Only with the licensed `coronary_arteries` task ([repo](https://github.com/wasserth/TotalSegmentator)) | No | `total` task: heart, aorta, pulmonary vein, LA appendage, SVC, IVC. Pulmonary artery only in licensed `heartchambers_highres` | High (real CT) but blob-like | Good for patient variety |

### 2.4 Sketchfab heart, coronary and thorax models (checked one by one)

Sketchfab still serves downloads in November 2026; the pages below showed a working "Download 3D Model" button. Since 2024, only CC BY and Standard models could migrate to Epic's Fab store. CC0, BY-SA, BY-NC and BY-ND models could not move (uncertain - snippet only) ([Sketchfab blog](https://sketchfab.com/blogs/community/fab-publishing-portal-open-for-sketchfab-migration/)). **Risk:** NC/SA models could disappear later, so archive a local copy plus a screenshot of the license.

| Model (author) | License | Size | Published | Use in this project | Link |
|---|---|---|---|---|---|
| Heart0102 Coronary Arteries (VisibleHeartLabs) | CC BY-NC 4.0 | 194.2k tris | 2022-11-18 | Coronary reference; personal build OK | [link](https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea) |
| Human Heart with Coronary Contrast #0084 (VisibleHeartLabs) | CC BY-NC 4.0 | 598.4k tris | 2021-12-27 | Blue-dye coronary surface; texture reference | [link](https://sketchfab.com/3d-models/human-heart-with-coronary-contrast-0084-2cb7f280960e4419ba9f505ec0c82543) |
| Other VisibleHeartLabs hearts (Heart0049, 0063, 0064, 0069, 0088, 0096, 0097, 0099, 0126, 0188, 0191, 0251, 0256) | CC BY-NC | 48.5k to 4.84M faces | various | Anatomical variation library (personal) | [API search "coronary"](https://api.sketchfab.com/v3/search?type=models&q=coronary&downloadable=true&count=24) |
| Anatomical heart - left dominance (eLearningUMCG) | CC BY-NC-SA 4.0 | 169.7k tris | 2019-08-19 | Coronary dominance variant | [link](https://sketchfab.com/3d-models/anatomical-heart-left-dominance-5c10cea34fd54b5eb9e3d0ecc8ab0da2) |
| Anatomical heart - codominance / right dominance (eLearningUMCG) | CC BY-NC-SA | 186k faces (codominance) | - | Coronary dominance variants | [API search](https://api.sketchfab.com/v3/search?type=models&q=coronary&downloadable=true&count=24) |
| Cardiac Anatomy: Coronary arteries of the heart (HannahNewey) | CC BY-NC-SA | 2.75M faces | - | Very dense reference | [API search](https://api.sketchfab.com/v3/search?type=models&q=coronary&downloadable=true&count=24) |
| Human Heart Cardiac Bypass (CU Modern Human Anatomy Program) | CC BY-NC-SA 4.0 | 1M tris | 2024-06-27 | **CABG grafts on a real heart**: best end-state reference | [link](https://sketchfab.com/3d-models/human-heart-cardiac-bypass-98dca43ff0c146b696148e6c3e70dbc0) |
| Pseudoaneurysm of Coronary Artery Graft (tl0615) | CC BY | 85.9k faces | - | Complication reference | [API search](https://api.sketchfab.com/v3/search?type=models&q=coronary&downloadable=true&count=24) |
| Anatomically Correct Human Heart (Pigcraft / s8819296) | CC BY | 1,000,048 faces | 2025-11-17 | Possible GREEN base. **Provenance unknown**: check that it is not AI-generated or a re-upload before use (uncertain) | [link](https://sketchfab.com/models/54fa880728d14c11afff78be8721620a) |
| Beating-heart (jalmer) | CC BY, 1 animation | 34,401 faces | 2022-09-28 | The description credits "Dreamwasabducted". At least **8 identical 34,401-face copies** exist under other names. **Re-upload risk**: use only the original author's upload | [link](https://sketchfab.com/models/d9845afb1ee64ad094adc96320c67d98), [search](https://api.sketchfab.com/v3/search?type=models&q=beating%20heart&downloadable=true&count=24) |
| Thoracic Cage / Caja Torácica (sebaualde / Ualde) | CC BY | 823,492 faces | 2018-08-14 | Rib cage + sternum context mesh | [link](https://sketchfab.com/models/8e467073d7f149d0a92a712a62326447) |
| Anatomy human rib cage (FrancescoMilanese) | No license shown; "now available for download on FAB" | 47.1k tris | 2017-07-06 | **UNVERIFIED**: skip | [link](https://sketchfab.com/3d-models/anatomy-human-rib-cage-0f1aa77bf02e4d438f8630bd6c53b12e) |
| 3D Animated Realistic Human Heart v10 (docjana) | No license shown; sold on CGTrader/TurboSquid | 15.1k, ~25 morph targets | 2016-03-24 | Paid; skip, but its approach (about 25 morphs) is a useful benchmark | [link](https://sketchfab.com/3d-models/3d-animated-realistic-human-heart-v10-a70c0c47fe4b4bbfabfc8f445365d5a4) |

### 2.5 Segmentation datasets you can convert to meshes

| Dataset / tool | Content | License / access | Personal use | Notes |
|---|---|---|---|---|
| **TotalSegmentator** (tool) | `total` CT task includes heart (51), aorta (52), pulmonary vein (53), left atrial appendage (61), SVC (62), IVC (63), sternum (116), costal cartilages (117) ([repo](https://github.com/wasserth/TotalSegmentator)) | Code **Apache-2.0**. `heartchambers_highres`, `coronary_arteries` and `aortic_sinuses` need a license key: free for non-commercial use, commercial use by contacting the authors ([repo](https://github.com/wasserth/TotalSegmentator)) | Yes (with free key) | Not a medical device. The README mentions v2.11/2.12 (exact current version uncertain) |
| **TotalSegmentator CT dataset v2.0.1** | 1,228 CT images, 117 structures, 23.6 GB zip, published 2023-10-27 ([Zenodo](https://zenodo.org/records/10047292)) | **CC BY 4.0** ([Zenodo](https://zenodo.org/records/10047292)) | Yes | GREEN; credit the authors |
| **MM-WHS** (Zhuang et al.) | 120 images: 60 CT/CTA + 60 MRI. Train 20+20, test 40+40. Labels: LV cavity, RV cavity, LA, RA, LV myocardium, ascending aorta, pulmonary artery ([data page](https://zmiclab.github.io/zxh/0/mmwhs/data.html)) | Signed registration form. "Recipient(s) commit to not disseminate the Data to any third party" (uncertain - snippet only). Maintenance has ended ([data page](https://zmiclab.github.io/zxh/0/mmwhs/data.html)) | Research only (uncertain) | RED for any release. Meshes derived from it should not ship |
| **ImageCAS** | 1,000 coronary CTA scans, two radiologists label the left and right coronary arteries (uncertain - snippet only) ([arXiv](https://arxiv.org/pdf/2211.01607)) | **UNVERIFIED**: no license on the repo. Access by emailing the author; a Kaggle copy exists ([repo](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT)) | Ask first | RED until the terms are known |
| **ASOCA** | 40 annotated coronary CTCA cases + 20 test cases, with centrelines (uncertain - snippet only) | Grand Challenge account plus accepted terms ([UNSW page](https://www.unsw.edu.au/research/svmg/resources/asoca-dataset)). The Scientific Data paper says it is available "to all researchers including commercial projects" (uncertain - snippet only) ([paper](https://link.springer.com/10.1038/s41597-023-02016-2)) | Yes, after approval | AMBER: read the terms when granted |
| **3D Slicer** (tool) | Segment-to-mesh export (STL/OBJ) | "BSD-style open source license", commercial use invited, **not FDA approved** ([about](https://slicer.readthedocs.io/en/latest/user_guide/about.html)) | Yes | GREEN tool |

**Recommended route.** Run TotalSegmentator on a CC BY CT (for example a case from its own CC BY dataset). Export the heart, aorta, vena cavae, sternum and ribs from 3D Slicer. Then re-topologise in Blender. This gives a GREEN, realistic, patient-like thorax. Coronary meshes from the licensed task are fine for the personal build. Log them AMBER, because the licence key terms are non-commercial.

---

## 3. Surgical instruments and OR equipment

### 3.1 Candidates found (licenses read from the official Sketchfab record)

| Item | Model (author) | License | Faces | Published | Verdict | Link |
|---|---|---|---|---|---|---|
| OR bed + dual-arm surgical lights + equipment console + cart | Realistic Medical Equipment and Accessories Set (daonware) | **CC BY** | 70,937 | 2024-12-02 | GREEN: core OR dressing | [link](https://sketchfab.com/models/5460fb2767c6468eb88466d2555d273b) |
| Operating table | Operating Table (shashkinv1ad) | **CC BY** | 46,400 (high-poly version 1,157,494) | 2021-01-29 | GREEN | [link](https://sketchfab.com/models/e3a4512227d34b098e2ef0d11c8a80fd) |
| Surgical light | Surgical Light (barbodoji) | CC BY-NC | 39,516 | - | RED for release; use the daonware lights instead | [search](https://api.sketchfab.com/v3/search?type=models&q=surgical%20light&downloadable=true&count=24) |
| Patient monitor | Patient Monitor (Ram-je) | **CC BY** | 156,478 | - | GREEN (screen will be replaced by a live UI) | [search](https://api.sketchfab.com/v3/search?type=models&q=patient%20monitor&downloadable=true&count=24) |
| Medical equipment (generic) | VitaCore-X (CMBC) | **CC BY** | 95,747 | - | GREEN (sci-fi look; check style) | [search](https://api.sketchfab.com/v3/search?type=models&q=patient%20monitor&downloadable=true&count=24) |
| Heart-lung (CPB) machine | Heartlung Machine (Kevin Gille) | **CC BY** | 8,635 | 2016-03-22 | GREEN but low detail ("done in 2 days for a test"). Use as a blockout only | [link](https://sketchfab.com/models/34f7d192bd8d4ca498b5e3d4948101ba) |
| Mixed instruments (clamps, scissors, scalpels, retractors) | Surgical Instruments collection (Digital Surgery) | CC BY-NC 4.0 | 614,712 | 2024-08-20 | Reference / personal placeholder only | [link](https://sketchfab.com/models/46f5799ca36240efae3abec6e61d4c8a) |
| Instrument table | Surgical / Instrument table collection (Digital Surgery) | CC BY-NC | 36,181 | - | Reference / personal only | [search](https://api.sketchfab.com/v3/search?type=models&q=operating%20table&downloadable=true&count=24) |
| Generic instrument | Surgical Instrument (ferofluid) | **CC BY 4.0** | 11.7k tris | 2018-03-09 | GREEN; instrument type not named | [link](https://sketchfab.com/3d-models/surgical-instrument-2971a44d334b45ff926792e92a6bcee7) |
| Needle holder | Surgical_needle Holder (Mmmighty_Atom) | **CC BY** | 9,668 | 2026-03-14 | GREEN; new upload, check provenance | [link](https://sketchfab.com/models/24864e4443df42f5b1439eea4631f136) |
| Sternal (Finochietto) retractor | **None found** on Sketchfab with a free license. Paid models exist (RenderHub "rib spreader") | - | - | - | **Model it yourself** | [search result](https://www.renderhub.com/7dmax/heavy-duty-3d-rib-spreader-thoracic-retractor-surgical-preci) |
| Sternal saw | **None found** | - | - | - | **Model it yourself** | - |
| Aortic cross-clamp, cannulae, CPB tubing | **None searched successfully** (search budget ended) | - | - | - | Model yourself; tubing is easy to make with curves | - |

**Spam warning.** The Sketchfab search for "patient monitor" also returned two "Buy Oxycodone" spam uploads labelled CC BY ([search](https://api.sketchfab.com/v3/search?type=models&q=patient%20monitor&downloadable=true&count=24)). Always open the model page, check the author's other uploads, and inspect the mesh before adding it.

### 3.2 Modelling the cardiac-specific instruments yourself

- **Finochietto sternal retractor.** Teleflex sells the "original model" with shafts "curved to follow body contour"; adult arm lengths are around 15 to 18 cm (uncertain - snippet only) ([Teleflex](https://ca.myteleflex.com/All-Categories/Surgical-Instruments/CVT/Finochietto-Retractors/p/su-FinochiettoRetractors)). Use manufacturer photos as **reference only**. Do not copy logos or engraved brand names.
- **Sternal saw.** It is a reciprocating or oscillating bone saw used for median sternotomy (uncertain - snippet only). Model a generic handpiece without brand marks.
- **CPB machine.** Start from the CC BY Kevin Gille blockout ([link](https://sketchfab.com/models/34f7d192bd8d4ca498b5e3d4948101ba)). Add roller-pump heads, an oxygenator, a reservoir and tubing in Blender. Keep consoles generic (no LivaNova, Terumo or Medtronic branding).
- **Why generic.** Brand names and trade dress belong to the manufacturer. This is the same reason marketplaces label such models "Editorial" (see section 8).

### 3.3 Poly Haven and ambientCG

| Source | License | Credit | Medical content | Link |
|---|---|---|---|---|
| **Poly Haven** (HDRIs, textures, models) | **CC0**: "You can use our assets for any purpose", redistribution allowed, credit appreciated, not required | No | **Hospital Room** HDRI (Oliksiy Yakovlyev), up to 17K, cool clinical light. **Hospital Room 2** HDRI (Dimitrios Savva, Jarod Guest), up to 20K. No medical models (categories: furniture, electronics, tools, etc.) | [license](https://polyhaven.com/license), [Hospital Room](https://polyhaven.com/a/hospital_room), [Hospital Room 2](https://polyhaven.com/a/hospital_room_2), [models](https://polyhaven.com/models) |
| **ambientCG** (PBR materials, HDRIs) | **CC0 1.0 Universal**. May be included as raw files in a video game | No (a suggested credit line is given) | Useful for floor tiles, painted walls, steel, rubber, plastics. No tissue or flesh category. "Leather" and "Cold Cuts" sets exist | [license](https://docs.ambientcg.com/license/), [list](https://ambientcg.com/list?q=meat) |

Note: Poly Haven's terms say the **website content** (logos, example renders, text) is not CC0, and scraping the site is prohibited ([license](https://polyhaven.com/license)). Download assets one by one, or use their API under the API terms.

### 3.4 Fab and Quixel Megascans (current terms)

- **Fab license types:** CC BY (free; not allowed for assets with the NoAI tag); **Standard** (free or paid, with a **Personal** tier for buyers with ≤ USD 100,000 gross revenue in the last 12 months and a **Professional** tier above that); "Personal - Reference Only" and "UEFN Source" for Fortnite content. The legacy "UE Marketplace License" is being phased out ([Fab docs](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab)).
- **Megascans:** free to all until the end of 2024, under the Standard license usable in "all engines and tools". From 2025, most assets are paid (2D/3D from USD 0.99, procedural kits USD 4.99, packs USD 24.99), with some free content. Assets downloaded through Bridge before that stay under the old **Epic Content License (Unreal-only)** unless they were added to the Fab library ([CG Channel](https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/)). The full Fab EULA page returned HTTP 403 (**UNVERIFIED** in full).
- **Recommendation:** do not plan on Megascans. If you already own some through Fab, they are usable in any engine under the Standard license. Log the tier (Personal) in the register.

---

## 4. Tissue textures, materials and photo references

### 4.1 What is free to ship vs reference-only

| Source | Content | License | Ship in game? | Link |
|---|---|---|---|---|
| Poly Haven / ambientCG | Environment, metals, plastics, tiles | CC0 | **Yes** | [Poly Haven](https://polyhaven.com/license), [ambientCG](https://docs.ambientcg.com/license/) |
| Wikimedia Commons "Median sternotomy" category | 4 photos (skin incision, sternotomy, retracted sternal edges, a diagram) | **Per file**. Example: "Стернотомия. Края грудины разведены.jpg" (retracted sternum, 2011, Maksim Kletkin) is **CC0** | CC0 files: **yes**; others: check | [category](https://commons.wikimedia.org/wiki/Category:Median_sternotomy), [CC0 file](https://commons.wikimedia.org/wiki/File:Стернотомия._Края_грудины_разведены.jpg) |
| Atlas of Human Cardiac Anatomy (Univ. of Minnesota Visible Heart Lab) | Images, videos inside beating hearts, 3D models | "Free to download and use for educational purposes". Keep the "University of Minnesota/© Medtronic" watermark and cite the atlas. Site © 2026 Regents, all rights reserved | **Reference only** (not an open license; watermark rule) | [atlas](https://www.vhlab.umn.edu/atlas/) |
| AnatomyTOOL images | Per item; many CC BY-NC-SA | NC-SA | Personal build only | [AnatomyTOOL](https://anatomytool.org/can-i-use) (uncertain - snippet only) |
| Sketchfab scans of real hearts (VisibleHeartLabs, CU Anschutz) | Photo-textured real tissue | CC BY-NC / BY-NC-SA | Personal only; **colour-pick reference** for your own shaders | see section 2.4 |
| CTSNet surgical videos, journal figures, YouTube surgery videos | Real operations | **UNVERIFIED** (CTSNet terms page returned 403). Treat as all rights reserved | **Reference only**: watch, measure, colour-pick; never copy frames | - |
| Visible Human cryosections | Real colour anatomy | NLM terms; credit NLM | Yes, with credit; good for colour sampling of myocardium and fat | [NLM](https://www.nlm.nih.gov/research/visible/getting_data.html) |

### 4.2 Recommended tissue approach (no license risk)

1. **Procedural shaders in Blender** (Principled BSDF with subsurface scattering, noise and Voronoi textures for fat lobules and muscle fibres, wet clear-coat). These are your own work, so they are GREEN.
2. **Colour-pick** values from CC0/NLM sources (Visible Human, CC0 Wikimedia photos) and from NC scans **for reference only**. Colour values are facts, not copyrighted expression (uncertain - general legal principle, not verified for every country).
3. **Bake** the procedural result to texture maps (base colour, normal, roughness, ambient occlusion, curvature) so the game engine does not need Blender nodes (see section 7).
4. Gap: CC0 photo-scanned meat/fat textures were not searched (budget ended). A follow-up search should check ambientCG and Poly Haven again for "fat", "meat" and "organic" materials.

---

## 5. Audio

### 5.1 Freesound licenses

Freesound uses three current licenses: **CC0** ("you can do pretty much what you want", but you cannot claim authorship), **CC BY 4.0** (always credit the creator), and **CC BY-NC 4.0** (credit, and "you can't earn any money" with the work). The old **Sampling+** license was retired. Freesound suggests a credit line with sound title, username, URL and license, and a separate credits page for long lists. Your account's "attribution list" records what you downloaded ([Freesound FAQ](https://freesound.org/help/faq/)). Older uploads may carry **3.0** versions of these licenses (for example ICU.wav below is CC BY-NC 3.0).

### 5.2 Verified sounds for the OR

| Need | Sound (author) | License | Length | Notes | Link |
|---|---|---|---|---|---|
| **Surgical suction in a real OR** | OP_Sauger_5.mp3 (fankitown) | **CC0** | 20.8 s | "Suction noise with clinical operating room background, directly recorded during surgery" | [link](https://freesound.org/people/fankitown/sounds/250348/) |
| **OR ambience with monitors** | Operation chirurgicale, Oaxaca (nicotep) | **CC0** | 2 min 36 s | Field recording of surgery in a clinic, electronic devices and monitoring | [link](https://freesound.org/people/nicotep/sounds/632733/) |
| ECG monitor / defibrillator beeps and voice prompts | Lifepak 12 touched.wav (residentsparking) | **CC0** | 6 min 55 s | Real device. Cut individual beeps from it | [link](https://freesound.org/s/243638) |
| Ventilator | Breathing machine (VoxHumanaMusiCurators) | **CC0** | 35.9 s | 48 kHz / 24-bit stereo | [link](https://freesound.org/people/VoxHumanaMusiCurators/sounds/703025/) |
| Room tone (HVAC) | room tone hospital exam room noisy ventilation (kyles) | **CC0** | 3 min 43 s | FLAC 48 kHz. Another user already used it in hospital VR training | [link](https://freesound.org/people/kyles/sounds/451922/) |
| Flatline tone | HL2 Style Flatline Tone (NoonerBear) | **CC0** | 6.9 s | 1 kHz tone, game-styled (less realistic) | [link](https://freesound.org/people/NoonerBear/sounds/581549/) |
| Bone saw (sternotomy stand-in) | Bone saw (Diramus) | **CC0** | 1 min 12 s | Horror foley; needs EQ to sound like a sternal saw | [link](https://freesound.org/people/Diramus/sounds/365422/) |
| Electric bone saw | Electric butcher's bone saw (Vortichez) | CC BY 4.0 | 12.2 s | Closer to a powered saw | [link](https://freesound.org/people/Vortichez/sounds/545431/) |
| Small suction | Dentist Suction and air puffer (Cheeseheadburger) | CC BY 4.0 | 62 s | Layer under OR suction | [link](https://freesound.org/people/Cheeseheadburger/sounds/141511/) |
| Heartbeat (body-conducted) | Heartbeat recorded with Contact Microphone (Schacht) | CC BY 4.0 | 20.7 s | 24-bit/48 kHz. Useful under the exposed-heart view | [link](https://freesound.org/people/Schacht/sounds/793474/) |
| Monitor beep loop | Heart Monitor Beep Loop (Zen53) | CC BY 4.0 | 9 min 53 s | **Synthesised** (KORG X-50), not a real monitor | [link](https://freesound.org/people/Zen53/sounds/678011/) |
| ICU ambience | ICU.wav (coetzee_megan12) | **CC BY-NC 3.0** | 1 min 29 s | Tagged "Operating-room". RED for release | [link](https://freesound.org/people/coetzee_megan12/sounds/366006) |
| Gloves on | Vinyl Gloves getting put on (shaderrow) | **CC BY-NC 4.0** | 36 s | RED for release; re-record instead | [link](https://freesound.org/people/shaderrow/sounds/362933/) |

**Freesound search facts:** "surgery" returned 62 results (48 CC0, 9 CC BY, 5 CC BY-NC) ([search](https://freesound.org/search/?q=surgery&f=&s=Automatic+by+relevance)). "cautery" returned only 1 unrelated result ([search](https://freesound.org/search/?q=cautery)). "peristaltic pump" returned 0 ([search](https://freesound.org/search/?q=peristaltic+pump)).

### 5.3 Audio gaps and how to fill them

| Missing sound | Plan |
|---|---|
| **Electrocautery ("Bovie") buzz and tissue sizzle** | Synthesise: a mains-hum-like buzz with band-passed noise, plus a frying/sizzle foley layer (for example, a hot pan with wet meat, recorded at home). GREEN, because it is your own recording. |
| **Sternal saw** | EQ and pitch-shift the CC0 Diramus bone saw, and layer a small electric motor recording. |
| **CPB roller pump** | Record a peristaltic aquarium/dosing pump or a slow mechanical roller. Loop at a rate tied to the pump RPM in the game. |
| **Monitor alarms** | Synthesize your own tones. Real monitors follow the IEC 60601-1-8 alarm standard, with different pulse patterns for high, medium and low priority (uncertain: the standard was not read in this research). Writing your own tones avoids both licence and trademark issues. |
| **Staff voices / call-outs** | Record volunteers, or use text-to-speech with a licence that allows game use (not researched here). |

### 5.4 Sonniss GDC Game Audio Bundles

- The **GDC 2026 bundle**: "7.47GB+ of high-quality sound effects" from 17 vendors. Royalty-free, free download, attribution not required, usable on "an unlimited number of projects for the rest of your lifetime" ([rekkerd.org, 2026-03-16](https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/)). Grade B.
- From the GDC 2024 bundle on, the license reportedly adds that the sounds **cannot be used to train AI models**, and you cannot claim them as your own (uncertain - snippet only) ([GameFromScratch](https://gamefromscratch.com/sonniss-27-5gb-sound-effect-giveaway-at-gdc-2024/)).
- The official license page (`sonniss.com/gdc-bundle-license`) showed only a bot check: **UNVERIFIED**. Save the license text that ships inside each bundle into `licenses/sonniss/`.
- Sonniss also sells a "Hospital Ambiences" library that includes operating rooms (paid; not researched further) ([Sonniss](https://sonniss.com/sound-effects/hospital-ambiences/)).

---

## 6. Humans and characters (OR staff and patient)

| Tool / library | Version / status (2026) | License | Use outside its own engine | Attribution | Recommendation |
|---|---|---|---|---|---|
| **MPFB** (MakeHuman Plugin For Blender) | **2.0.18**, released 2026-10-10. Blender 4.2 LTS and newer. Auto-rigging with Rigify, procedural skin and eye materials ([extension](https://extensions.blender.org/add-ons/mpfb/)) | Code **GPL-3.0-or-later** ([extension](https://extensions.blender.org/add-ons/mpfb/)). Core assets **CC0** ([MakeHuman](https://static.makehumancommunity.org/about/license.html)) | Yes (exported meshes are your own work; GPL covers the code, not the output) | Not required for CC0 assets. Community assets have their own licenses | **Primary** for the patient body (needs a realistic torso) and staff bodies |
| **MakeHuman** (standalone) | 1.x | Code **AGPL**, core assets **CC0** ([MakeHuman](https://static.makehumancommunity.org/about/license.html)). Since 2020, base mesh, targets and proxies count as CC0 assets (uncertain - snippet only) | Yes | No | Alternative to MPFB |
| **Mixamo** (Adobe) | Free service. 2026 status not verified (helpx FAQ returned 403) | Royalty-free for personal and commercial projects. "The only thing you can't do is distribute the raw character and animation files". No ML training (community FAQ, 2022, not written by Adobe staff) ([FAQ thread](https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/td-p/13234775)) | Yes, baked into the game | No | Idle, walk and reach animations for staff. Do not put raw FBX files in a public repo. Grade C: re-check |
| **Character Creator 5** (Reallusion) | Released 2025-08-27/28, **USD 299** perpetual, Windows 10+, FBX/OBJ export ([CG Channel](https://www.cgchannel.com/2025/08/reallusion-releases-character-creator-5/)) | Content **Standard License**: "Export content to any external software or game engine". One Standard License covers **one character** in commercial games; **Extended** for mass character output ([Reallusion](https://www.reallusion.com/license/content.html)). The page is internally inconsistent after its 2025.8.1 update | Yes | Not stated | Paid; not needed |
| **MetaHuman** (Epic) | Since **MetaHuman 5.6 (2025-06-03)**: "the EULA has been updated so that MetaHumans can be used in any engine" ([release post](https://forums.unrealengine.com/t/metahuman-5-6-release/2539165)) | Unreal Engine EULA (+ MetaHuman terms). Free under **USD 1M** yearly revenue; above that a UE seat (USD 1,850/year). Can be used in AI workflows but **not to train AI** ([CG Channel](https://www.cgchannel.com/?p=167592)). The official license page needs login: **partly UNVERIFIED** | Yes (since 5.6) | Per EULA | Optional for the surgeon close-ups. Needs Epic cloud services for autorig/texture synthesis ([CG Channel](https://www.cgchannel.com/?p=167592)) |
| **Microsoft Rocketbox** | 115 rigged avatars. Facial blendshapes added 2022 (15 visemes, 48 FACS, ARKit). Repo **archived, read-only**; last update June 2022 ([repo](https://github.com/microsoft/Microsoft-Rocketbox)) | **MIT** ([repo](https://github.com/microsoft/Microsoft-Rocketbox)) | Yes (FBX) | Keep the MIT notice | **Background staff** (anaesthetist, perfusionist, nurses). Medical-profession outfits are not described on the page (uncertain); scrubs may need re-texturing |
| **Ready Player Me** | Acquired by Netflix (December 2025). Public services **shut down 2026-01-31** ([Wikipedia](https://en.wikipedia.org/wiki/Ready_Player_Me), which cites a Medium post) | n/a | n/a | n/a | **Do not use** |

**Patient realism note.** For an open-chest view, the patient's **thorax skin, fat, sternum and draping** matter more than the face. The face is under the drape and the anaesthesia screen. Use MPFB for the body proportions. Replace the chest region with the anatomy stack (BodyParts3D/TotalSegmentator sternum and ribs + a custom incision mesh).

---

## 7. Blender pipeline

### 7.1 Tool versions and licenses

| Tool | Version / date | License | Link |
|---|---|---|---|
| Blender | **5.2 LTS** released 2026-07-14 (5.0: 2025-11-18; 5.1: 2026-03-17) | GPL v2+ (code). "What you create with Blender is your sole property" | [releases](https://www.blender.org/download/releases/), [license](https://www.blender.org/about/license/) |
| glTF-Blender-IO (import/export) | Bundled with Blender since 2.80 | **Apache-2.0** | [repo](https://github.com/KhronosGroup/glTF-Blender-IO) |
| QRemeshify (quad remesher extension) | Blender 4.2+; based on QuadWild with Bi-MDF solver; no release tags | **GPL-3.0** | [repo](https://github.com/ksami/QRemeshify) |
| Instant Meshes (external remesher) | 2015 code, 46 commits | **BSD-3-Clause-style** (plus an "Enhancements" paragraph), © Jakob, Panozzo, Tarini, Sorkine-Hornung | [license](https://raw.githubusercontent.com/wjakob/instant-meshes/master/LICENSE.txt) |
| MPFB | 2.0.18 (2026-10-10) | GPL-3.0-or-later | [extension](https://extensions.blender.org/add-ons/mpfb/) |
| 3D Slicer | current | BSD-style; not FDA approved | [about](https://slicer.readthedocs.io/en/latest/user_guide/about.html) |
| Blender Extensions Platform | - | "only offers GNU GPL compliant software" | [about](https://extensions.blender.org/about/) |

**GPL note for add-ons.** Blender's Python API is part of Blender, so published add-on scripts must be "shared under a GPL compliant license" ([Blender license](https://www.blender.org/about/license/)). This applies to add-on **code**, not to the meshes or textures you make with them.

### 7.2 Step-by-step pipeline (per anatomy or equipment asset)

| # | Step | How (Blender 5.2) | Output / check |
|---|---|---|---|
| 1 | **Intake** | Download, save the license page as a PDF/screenshot, add a row to `ASSET_LICENSES.md` (section 8) | `source/<asset-id>/` + `licenses/<asset-id>.pdf` |
| 2 | **Import** | OBJ (BodyParts3D), GLB (HRA, Sketchfab), STL (Slicer). Set the scale to metres and check real size (adult heart length is roughly 12 cm, uncertain - not researched here) | Correct scale and orientation |
| 3 | **Clean** | Merge by distance, remove loose parts, recalculate normals, fill holes, decimate scans to about 200k triangles before sculpting | Watertight, manifold mesh |
| 4 | **Sculpt / correct anatomy** | Compare with references (section 2.3). Add missing parts (aortic valve, pericardium, cardiac veins, diagonal branches). Dyntopo or voxel remesh for a high-poly sculpt | High-poly "source of truth" |
| 5 | **Retopologise** | QRemeshify (GPL-3.0) or Instant Meshes (BSD) for an automatic quad base; hand-fix edge loops around the coronary arteries and the planned incision lines | Quad mesh with edge flow for deformation |
| 6 | **UV unwrap** | Seams on the posterior heart and hidden faces; texel density consistent across organs | UV islands with margin |
| 7 | **Bake** | Cycles bake, "Selected to Active" with a **Cage** and **Cage Extrusion**, or **Max Ray Distance** when not using a cage. Bake types include Normal, Ambient Occlusion, Roughness, Diffuse, and others. **Margin** type: Extend or Adjacent Faces, size in pixels ([manual](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)) | Normal (tangent space), AO, curvature (via a geometry/pointiness bake or a shader trick), base colour |
| 8 | **Rig the heartbeat** | See 7.3 | Shape keys and/or armature |
| 9 | **LODs** | Decimate copies of the final mesh (design suggestion: hero heart LOD0 about 150k triangles, LOD1 about 40k, LOD2 about 10k; not sourced) | LOD0 to LOD2 |
| 10 | **Export** | **GLB** with Shape Keys and Skinning enabled. FBX for engines that prefer it. USD for archiving (Blender USD export not verified here) | Validate the GLB in a glTF validator |
| 11 | **Register** | Update `ASSET_LICENSES.md`: derived files, modifications, attribution text | Licence row complete |

### 7.3 Heartbeat animation options

| Option | How | Pros | Cons | Export facts |
|---|---|---|---|---|
| **A. Shape keys (recommended)** | Basis = end-diastole. Keys: end-systole, atrial contraction, and optionally "arrest/flaccid" and "fibrillation wobble". The game drives the weights from the simulated heart rate and contractility | Small, exact, easy to blend, deterministic | Linear vertex blending (no twisting) | Blender shape keys become glTF **morph targets**; the first key is the Basis (uncertain - snippet only) ([Vulkan glTF tutorial](https://docs.vulkan.org/tutorial/latest/Advanced_glTF/Tooling_Production_Pipeline/02_blender_workflow.html)). The exporter supports "animation (keyframes, skinning, and shape keys)" (uncertain - snippet only) |
| **B. Bones (armature)** | Bones for the LV/RV free walls, apex and base twist; vertex groups | Twisting motion (LV torsion), cheap | Harder to make exact volumes | glTF standard skinning keeps **4 influences per vertex**. When more exist, Blender's exporter keeps "the 4 with highest weight" and normalises them ([commit](https://archive.blender.org/lists/bf-extensions-cvs/2022-April/010894.html)) |
| **C. Alembic cache** | Bake a soft-body or cloth simulation of the beating heart to .abc | Most organic motion | Huge files; no runtime control of the heart rate | Blender supports Alembic export (not verified in this research) |
| **D. Hybrid** | Bones for global twist and position + shape keys for local bulge | Best realism | More work | Both are supported in GLB |

Benchmark: a commercial "realistic heart" model used about **25 morph targets** at 15.1k polygons ([docjana](https://sketchfab.com/3d-models/3d-animated-realistic-human-heart-v10-a70c0c47fe4b4bbfabfc8f445365d5a4)). Plan 4 to 8 morph targets for the hero heart. Add more only if profiling allows.

---

## 8. License compliance approach

### 8.1 What each license means here

| License | Personal project (now) | Public free release (later) | Commercial release (later) | Key rule (source) |
|---|---|---|---|---|
| **CC0** (Poly Haven, ambientCG, many Freesound sounds, MPFB core assets) | Yes | Yes | Yes | Do not claim authorship of the original ([Freesound FAQ](https://freesound.org/help/faq/)); no credit needed ([Poly Haven](https://polyhaven.com/license)) |
| **CC BY 4.0** (BodyParts3D 4.0, HRA, TotalSegmentator dataset, many Sketchfab/NIH models) | Yes | Yes, with credits | Yes, with credits | Keep the creator, notices and link, and "indicate if You modified the Licensed Material" (Section 3(a)) ([CC BY-NC legal code, same clause in BY](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)). Use TASL: Title, Author, Source, License ([CC wiki](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution)) |
| **CC BY-SA 4.0** (Z-Anatomy) | Yes | Yes. The **adapted asset** must be shared under BY-SA 4.0 (or later, or a compatible license) | Same | "The Adapter's License You apply must be a Creative Commons license with the same License Elements" (Section 3(b)) ([BY-SA legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)). Putting an unmodified SA work into a **collection** does not change the collection's license ([CC FAQ](https://creativecommons.org/faq/)). Practical rule: keep SA meshes as separate files, and publish those files (and edits of them) under BY-SA |
| **CC BY-NC 4.0 / BY-NC-SA** (VisibleHeartLabs, UMCG, CU Anschutz, some Freesound) | Yes | Only if the release is **not** "primarily intended for or directed towards commercial advantage or monetary compensation" ([BY-NC legal code](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)). CC "cannot advise you on what is and is not commercial use" ([CC FAQ](https://creativecommons.org/faq/)) | **No**: replace these assets first | Treat any store page, paid tier, ads or donations as a risk |
| **CC BY-ND** | Private remixing only: "The NoDerivatives licenses do not permit remixing except for private use" ([CC FAQ](https://creativecommons.org/faq/)) | Unmodified only (almost useless for game assets, which need retopology) | Unmodified only | Avoid |
| **GPL / AGPL** (Blender, MPFB code, QRemeshify, MakeHuman code) | Yes. Private modifications need not be published ([GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)) | If you **distribute** GPL code (for example a modified add-on), you must provide its source under the GPL ([GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)) | Same | The **output** of a GPL program is generally not covered, unless substantial parts of the program are copied into it ([GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)). Blender says your .blend files and art are yours ([Blender](https://www.blender.org/about/license/)). Do not link GPL code into the game engine code unless the game is GPL too |
| **MIT / BSD / Apache-2.0** (Rocketbox, Instant Meshes, glTF-Blender-IO, TotalSegmentator code, 3D Slicer) | Yes | Yes; keep the copyright and license notice | Yes | Include `THIRD_PARTY_NOTICES` |
| **"Editorial use only"** (TurboSquid, Sketchfab store, RenderHub) | Risky even now; editorial means news, commentary or education about the subject | **No** | **No** | Sketchfab Editorial: only works that comment on the subject (news, reviews, documentaries); no alterations except technical cropping ([Sketchfab licenses](https://sketchfab.com/licenses)). TurboSquid: editorial models "cannot be upgraded to allow Game Use or other commercial purposes" ([TurboSquid](https://www.turbosquid.com/help/en/articles/14829413-what-are-the-limitations-and-upgrade-policies-for-3d-model-licenses-on-turbosquid)). **Do not use** |
| **Custom / dataset agreements** (MM-WHS, ImageCAS, ASOCA, Mixamo, Sonniss, Fab Standard) | Read each one | Often no redistribution of raw data | Varies | Store a copy of the exact terms with the asset |
| **No license stated / "educational use"** (Open Anatomy, UMN atlas, Embodi3D) | Reference only | **No** | **No** | No license = all rights reserved |

### 8.2 `ASSET_LICENSES.md` register format (proposed)

One table row per **source asset**. One sub-row (or "Derived files" column) lists every game file made from it.

```markdown
# ASSET_LICENSES.md

Status legend: GREEN = CC0 / CC BY / MIT / BSD / Apache (ok for any release with credits)
               AMBER = CC BY-SA, GPL, custom terms (ok if rules followed; check before release)
               RED   = NC, ND, editorial, unknown, "educational use only" (personal build only)

| ID | Asset | Type | Author / rights holder | Source URL | License (exact, with version) | License URL | Verified on | Evidence file | Personal OK | Attribution text (TASL) | SA | ND | NC | Modified? (what) | Derived game files | Status | Release action |
|----|-------|------|------------------------|------------|-------------------------------|-------------|-------------|---------------|-------------|-------------------------|----|----|----|------------------|--------------------|--------|----------------|
| ANA-001 | BodyParts3D 4.0 heart parts | 3D mesh | Database Center for Life Science (DBCLS) | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html | CC BY 4.0 | https://creativecommons.org/licenses/by/4.0/ | 2026-11-03 | licenses/ANA-001.pdf | Yes | "BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International" — modified (remeshed, sculpted) | No | No | No | Retopo, sculpt, UV, bake | assets/anatomy/heart_LOD0-2.glb | GREEN | Credit in credits screen |
| ANA-010 | Heart0102 Coronary Arteries | 3D mesh | VisibleHeartLabs | https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea | CC BY-NC 4.0 | https://creativecommons.org/licenses/by-nc/4.0/ | 2026-11-03 | licenses/ANA-010.png | Yes | "Heart0102 Coronary Arteries" by VisibleHeartLabs, CC BY-NC 4.0 | No | No | Yes | Reference only | (none) | RED | Do not ship; reference only |
| SFX-001 | OP_Sauger_5.mp3 | Audio | fankitown | https://freesound.org/people/fankitown/sounds/250348/ | CC0 1.0 | https://creativecommons.org/publicdomain/zero/1.0/ | 2026-11-03 | licenses/SFX-001.png | Yes | (optional) | No | No | No | Trimmed, looped, EQ | audio/sfx/suction_loop.ogg | GREEN | None required |
```

Rules for the register:

1. **No row, no import.** An asset without a row may not be placed in `assets/`.
2. **Evidence file.** Save the license page (PDF or PNG) with the date. Licenses can change (BodyParts3D did: section 2.2).
3. **Exact license string.** Write "CC BY-NC 4.0", not "free" or "Creative Commons".
4. **Provenance check** for community uploads: (a) does the uploader look like the original author? (b) are there identical copies (same face count) by other users? (c) is it possibly AI-generated or ripped from a game or a paid store? If in doubt, mark RED. Section 2.4 shows a 34,401-face beating heart re-uploaded at least 8 times.
5. **Folder split.** `assets/green/`, `assets/amber_sa/`, `assets/red_personal_only/`. A build script can then exclude `red_personal_only/` from any public build.
6. **Credits screen.** Generate it from the register (Title, Author, Source, License, "modified"). Freesound also suggests linking a separate credits page when the list is long ([Freesound FAQ](https://freesound.org/help/faq/)).
7. **Code vs content.** Code licenses (GPL/MIT/Apache) go in `THIRD_PARTY_NOTICES.md`. Content licenses go in `ASSET_LICENSES.md`.
8. **AI clauses.** Note "no AI training" clauses (MetaHuman, Sonniss 2024+, Mixamo FAQ, Sketchfab NoAI tag). They do not block use in a game, but they forbid feeding the files to model training.
9. **Repo hygiene.** Do not commit raw files whose terms forbid redistribution (Mixamo raw FBX, MM-WHS images, ImageCAS, Sonniss raw libraries) to the public GitHub repository. Keep them in a local, git-ignored `vendor_private/` folder.

### 8.3 Personal project now vs future release

| Situation | What is allowed |
|---|---|
| **Now: private personal build** on your own PC | GREEN + AMBER + RED assets (respecting dataset agreements). |
| **Public GitHub repository** (the current repo is public-facing) | Committing an asset **is distribution**. Only GREEN and AMBER files may be committed, with license files beside them. RED assets stay local. |
| **Free public release** (itch.io, web build) | GREEN; AMBER with obligations (SA files published under BY-SA, GPL code with source). NC assets only if the release is clearly non-commercial (no price, ads or donations). ND and editorial: no. |
| **Commercial release** | GREEN, and AMBER where the obligations are met. Replace every NC, ND, editorial or unknown asset first. Also re-check the Fab tier (Personal ≤ USD 100k) and MetaHuman (free < USD 1M). |

---

## Game hooks

How each finding becomes a mechanic, a data value or a rule:

1. **Anatomy variation system.** Ship 2 to 3 GREEN heart variants (BodyParts3D re-sculpt, HRA male, HRA female). Add a **coronary dominance** parameter (right / left / co-dominant), modelled after the UMCG variants ([left dominance](https://sketchfab.com/3d-models/anatomical-heart-left-dominance-5c10cea34fd54b5eb9e3d0ecc8ab0da2)). The game picks the variant per case, and the player must identify the target vessel (LAD, Cx, RCA, PDA) before grafting.
2. **Named-vessel hit-testing.** Keep the BodyParts3D FMA IDs as mesh names (for example `FMA3862_LAD`). Raycasts return the anatomical name, so the game can score "graft placed on LAD distal to the lesion" ([parts list](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt)).
3. **Heartbeat driven by physiology.** Morph-target weights (diastole, systole, atrial kick) are driven each frame by the simulated heart rate and contractility. Cardioplegic arrest sets the weights to a still, flaccid key. Fibrillation uses a noise-driven "wobble" key (section 7.3).
4. **Patient variety from CT.** Use TotalSegmentator meshes from the CC BY dataset ([Zenodo](https://zenodo.org/records/10047292)) as "patient cases" with different chest sizes and heart positions, which changes the sternotomy and cannulation difficulty.
5. **Audio state machine.** Layers: room tone (CC0, kyles) + ventilator (CC0) + monitor beeps (pitch follows SpO2 if you synthesise them) + suction (CC0 OR recording) + saw / cautery one-shots + CPB pump loop whose rate follows pump RPM. The flatline/alarm tone triggers on rules from the physiology model.
6. **Instrument interaction.** The CC BY operating table and lights are fixed scenery. The cardiac instruments (Finochietto retractor, sternal saw, cross-clamp) are custom-built with articulated parts (the retractor crank opens in steps, the clamp has a ratchet), so the player's actions map to real mechanical states.
7. **Staff AI.** Rocketbox (MIT) avatars with Mixamo animations act as anaesthetist, perfusionist and scrub nurse. Their call-outs are tied to events (for example, "on bypass" when the CPB flow reaches target).
8. **Credits and compliance built in.** The credits screen is generated from `ASSET_LICENSES.md`. A build flag `PUBLIC_BUILD=true` fails the build if any RED asset is referenced.
9. **Reference viewer (debug mode).** A developer-only mode can load the NC real-heart scans side by side with the game heart for visual accuracy checks. It is excluded from public builds.

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | BodyParts3D's current license is CC BY 4.0 (license page updated 2025-02-27) | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html | A |
| 2 | BodyParts3D release 3.0 (2011) was CC BY-SA 2.1 Japan, with an SA obligation for derivatives | https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html | A |
| 3 | The current BodyParts3D download is "BP3D_4.0" OBJ at 99% polygon reduction (136 MB IS-A, 62 MB PART-OF) | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html | A |
| 4 | BodyParts3D includes RCA, marginal, PDA, LAD, Cx and septal branches; tricuspid, pulmonary and mitral valves; sternum parts; no pericardium | https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt | A |
| 5 | Z-Anatomy content is CC BY-SA 4.0; bundled kidney is CC BY-NC 4.0 and inner ear CC BY-NC-SA 4.0 | https://github.com/Z-Anatomy/Models-of-human-anatomy | A |
| 6 | All HRA/CCF 3D reference objects are CC BY 4.0; heart GLB v1.2 is from June 2022 | https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html | A |
| 7 | NIH 3D licenses differ per entry (3DPX-011381 CC BY; 3DPX-000900 CC BY-NC) | https://3d.nih.gov/entries/3DPX-011381 | A |
| 8 | Visible Human data needs no license since July 2019; NLM asks for "Courtesy of the U.S. National Library of Medicine" | https://www.nlm.nih.gov/research/visible/getting_data.html | A |
| 9 | TotalSegmentator code is Apache-2.0; heartchambers_highres and coronary_arteries need a license (free for non-commercial use) | https://github.com/wasserth/TotalSegmentator | A |
| 10 | TotalSegmentator dataset v2.0.1: CC BY 4.0, 1,228 CTs, 117 structures, 23.6 GB | https://zenodo.org/records/10047292 | A |
| 11 | MM-WHS has 120 images (60 CT, 60 MRI), 7 labelled substructures, access by signed form | https://zmiclab.github.io/zxh/0/mmwhs/data.html | A |
| 12 | VisibleHeartLabs Heart0102 is CC BY-NC 4.0, 194.2k tris, RCA 3 / LAD 4 / Cx 3 branches | https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea | A |
| 13 | CU Anschutz plastinated cardiac bypass heart is CC BY-NC-SA 4.0, 1M tris | https://sketchfab.com/3d-models/human-heart-cardiac-bypass-98dca43ff0c146b696148e6c3e70dbc0 | A |
| 14 | "Realistic Medical Equipment and Accessories Set" (bed, dual-arm lights, console, cart) is CC BY, 70,937 faces | https://sketchfab.com/models/5460fb2767c6468eb88466d2555d273b | A |
| 15 | The only free heart-lung machine found is CC BY, 8,635 faces, a 2-day test model | https://sketchfab.com/models/34f7d192bd8d4ca498b5e3d4948101ba | A |
| 16 | Poly Haven assets are CC0; credit not required; the Hospital Room HDRI goes up to 17K | https://polyhaven.com/license | A |
| 17 | ambientCG assets are CC0 1.0 and may be included as raw files in a video game | https://docs.ambientcg.com/license/ | A |
| 18 | Fab Standard license has a Personal tier (≤ USD 100,000 revenue in 12 months) and a Professional tier | https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab | A |
| 19 | Megascans were free until end of 2024; from 2025 most are paid; Bridge downloads stay under the UE-only Epic Content License | https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/ | B |
| 20 | Freesound uses CC0, CC BY 4.0 and CC BY-NC 4.0; Sampling+ was retired | https://freesound.org/help/faq/ | A |
| 21 | A CC0 Freesound recording of surgical suction "directly recorded during surgery" exists (20.8 s) | https://freesound.org/people/fankitown/sounds/250348/ | A |
| 22 | Sonniss GDC 2026 bundle: 7.47 GB+, royalty-free, no attribution, unlimited projects | https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/ | B |
| 23 | MPFB 2.0.18 (2026-10-10) is GPL-3.0-or-later; MakeHuman core assets are CC0 | https://extensions.blender.org/add-ons/mpfb/ | A |
| 24 | Microsoft Rocketbox: 115 rigged avatars, MIT license, repo archived (last update June 2022) | https://github.com/microsoft/Microsoft-Rocketbox | A |
| 25 | Since MetaHuman 5.6 (2025-06-03) MetaHumans may be used in any engine | https://forums.unrealengine.com/t/metahuman-5-6-release/2539165 | B |
| 26 | MetaHuman is free under USD 1M revenue; UE seat USD 1,850/year above; no AI training | https://www.cgchannel.com/?p=167592 | B |
| 27 | Ready Player Me public services shut down 2026-01-31 after Netflix acquired it in December 2025 | https://en.wikipedia.org/wiki/Ready_Player_Me | B/C |
| 28 | Blender 5.2 LTS was released 2026-07-14; Blender output is the user's property | https://www.blender.org/download/releases/ | A |
| 29 | Blender's glTF exporter keeps the 4 highest bone weights per vertex and normalises them | https://archive.blender.org/lists/bf-extensions-cvs/2022-April/010894.html | A |
| 30 | Sketchfab/TurboSquid "Editorial" licenses forbid game/commercial use and cannot be upgraded | https://www.turbosquid.com/help/en/articles/14829413-what-are-the-limitations-and-upgrade-policies-for-3d-model-licenses-on-turbosquid | A |

---

## Sources

1. BodyParts3D README (release 3.0, 2011; README 2013) - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html - old CC BY-SA 2.1 JP license, attribution text, file list.
2. BodyParts3D license page (updated 2025-02-27) - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html - current CC BY 4.0 license and attribution text.
3. BodyParts3D download page - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html - BP3D 4.0 archives and sizes.
4. BodyParts3D parts list (3.0) - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt - coronary, valve, chamber, vessel and sternum parts.
5. BodyParts3D description - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/desc.html - adult male body, last update 2013/05.
6. Z-Anatomy, Models-of-human-anatomy (GitHub) - https://github.com/Z-Anatomy/Models-of-human-anatomy - CC BY-SA 4.0 and third-party licenses.
7. Open Anatomy Project - https://openanatomy.org/ - list of 6 atlases; no license stated.
8. Open Anatomy Browser (GitHub) - https://github.com/mhalle/oabrowser - no LICENSE file visible.
9. NIH 3D entry 3DPX-011381 - https://3d.nih.gov/entries/3DPX-011381 - CC BY heart from CT.
10. NIH 3D entry 3DPX-000906 v2 - https://3d.nih.gov/entries/3DPX-000906/2 - CC BY heart + aorta + kidneys.
11. NIH 3D entry 3DPX-000900 v2 - https://3d.nih.gov/entries/3DPX-000900/2 - CC BY-NC heart, Blender retopology.
12. HuBMAP CCF 3D Reference Object Library - https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html - CC BY 4.0; heart GLB versions.
13. HuBMAP ccf-releases (GitHub) - https://github.com/hubmapconsortium/ccf-releases - releases up to v2.0.
14. NLM Visible Human, getting the data - https://www.nlm.nih.gov/research/visible/getting_data.html - no license since July 2019; formats and resolution.
15. NLM data Terms and Conditions - https://www.nlm.nih.gov/databases/download/terms_and_conditions.html - credit line, no endorsement.
16. AnatomyTOOL "Can I use" (snippet only) - https://anatomytool.org/can-i-use - per-item licensing, many BY-NC-SA.
17. TotalSegmentator (GitHub) - https://github.com/wasserth/TotalSegmentator - Apache-2.0; open vs licensed tasks; class list.
18. TotalSegmentator CT dataset v2.0.1 (Zenodo) - https://zenodo.org/records/10047292 - CC BY 4.0, 1,228 CTs, 117 structures.
19. MM-WHS data page - https://zmiclab.github.io/zxh/0/mmwhs/data.html - 120 images, labels, access terms.
20. ImageCAS (GitHub) - https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT - access by email; no license stated.
21. ImageCAS paper (arXiv, snippet only) - https://arxiv.org/pdf/2211.01607 - 1,000 CTA cases.
22. ASOCA dataset page (UNSW) - https://www.unsw.edu.au/research/svmg/resources/asoca-dataset - Grand Challenge access and terms.
23. ASOCA data descriptor, Scientific Data (snippet only) - https://link.springer.com/10.1038/s41597-023-02016-2 - 40 cases; commercial projects allowed.
24. 3D Slicer "About" - https://slicer.readthedocs.io/en/latest/user_guide/about.html - BSD-style license; not FDA approved.
25. Sketchfab Heart0102 (VisibleHeartLabs) - https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea - CC BY-NC 4.0, branch counts.
26. Sketchfab Heart with Coronary Contrast #0084 - https://sketchfab.com/3d-models/human-heart-with-coronary-contrast-0084-2cb7f280960e4419ba9f505ec0c82543 - CC BY-NC 4.0.
27. Sketchfab Anatomical heart, left dominance (UMCG) - https://sketchfab.com/3d-models/anatomical-heart-left-dominance-5c10cea34fd54b5eb9e3d0ecc8ab0da2 - CC BY-NC-SA 4.0.
28. Sketchfab Human Heart Cardiac Bypass (CU Anschutz) - https://sketchfab.com/3d-models/human-heart-cardiac-bypass-98dca43ff0c146b696148e6c3e70dbc0 - CC BY-NC-SA 4.0, CABG scan.
29. Sketchfab API search "coronary" - https://api.sketchfab.com/v3/search?type=models&q=coronary&downloadable=true&count=24 - list of coronary models and licenses.
30. Sketchfab API search "beating heart" - https://api.sketchfab.com/v3/search?type=models&q=beating%20heart&downloadable=true&count=24 - duplicate 34,401-face uploads.
31. Sketchfab "Anatomically Correct Human Heart" - https://sketchfab.com/models/54fa880728d14c11afff78be8721620a - CC BY, 1M faces, 2025.
32. Sketchfab "Thoracic Cage / Caja Torácica" - https://sketchfab.com/models/8e467073d7f149d0a92a712a62326447 - CC BY rib cage.
33. Sketchfab "Heartlung Machine" (Kevin Gille) - https://sketchfab.com/models/34f7d192bd8d4ca498b5e3d4948101ba - CC BY CPB blockout.
34. Sketchfab "Realistic Medical Equipment and Accessories Set" - https://sketchfab.com/models/5460fb2767c6468eb88466d2555d273b - CC BY OR set.
35. Sketchfab "Operating Table" (shashkinv1ad) - https://sketchfab.com/models/e3a4512227d34b098e2ef0d11c8a80fd - CC BY.
36. Sketchfab "Surgical Instruments collection" (Digital Surgery) - https://sketchfab.com/models/46f5799ca36240efae3abec6e61d4c8a - CC BY-NC 4.0.
37. Sketchfab "Surgical Instrument" (ferofluid) - https://sketchfab.com/3d-models/surgical-instrument-2971a44d334b45ff926792e92a6bcee7 - CC BY 4.0.
38. Sketchfab "Surgical_needle Holder" - https://sketchfab.com/models/24864e4443df42f5b1439eea4631f136 - CC BY.
39. Sketchfab API search "patient monitor" - https://api.sketchfab.com/v3/search?type=models&q=patient%20monitor&downloadable=true&count=24 - CC BY monitors; spam uploads.
40. Sketchfab API search "surgical light" - https://api.sketchfab.com/v3/search?type=models&q=surgical%20light&downloadable=true&count=24 - CC BY-NC light.
41. Sketchfab licenses help - https://help.sketchfab.com/en/articles/16152217 - Standard and CC license types.
42. Sketchfab crediting help - https://help.sketchfab.com/en/articles/16152215-crediting-users-for-3d-model-downloads - attribution requirement and format.
43. Sketchfab store license (Standard / Editorial) - https://sketchfab.com/licenses - editorial restrictions.
44. Sketchfab Fab migration blog (snippet only) - https://sketchfab.com/blogs/community/fab-publishing-portal-open-for-sketchfab-migration/ - only CC BY and Standard could migrate.
45. Poly Haven license - https://polyhaven.com/license - CC0.
46. Poly Haven "Hospital Room" HDRI - https://polyhaven.com/a/hospital_room - CC0, 17K.
47. Poly Haven "Hospital Room 2" HDRI - https://polyhaven.com/a/hospital_room_2 - CC0, 20K.
48. Poly Haven models index - https://polyhaven.com/models - categories, no medical models.
49. ambientCG license - https://docs.ambientcg.com/license/ - CC0 1.0.
50. Fab licenses and pricing (Epic docs) - https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab - CC BY, Standard Personal/Professional, USD 100k threshold.
51. CG Channel, Megascans free until end of 2024 - https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/ - 2025 pricing, legacy license.
52. Freesound FAQ - https://freesound.org/help/faq/ - license types and attribution.
53. Freesound "OP_Sauger_5.mp3" - https://freesound.org/people/fankitown/sounds/250348/ - CC0 OR suction.
54. Freesound "Operation chirurgicale, Oaxaca" - https://freesound.org/people/nicotep/sounds/632733/ - CC0 surgery ambience.
55. Freesound "Lifepak 12 touched.wav" - https://freesound.org/s/243638 - CC0 monitor/defibrillator.
56. Freesound "Breathing machine" - https://freesound.org/people/VoxHumanaMusiCurators/sounds/703025/ - CC0 ventilator.
57. Freesound "room tone hospital exam room" - https://freesound.org/people/kyles/sounds/451922/ - CC0 room tone.
58. Freesound "HL2 Style Flatline Tone" - https://freesound.org/people/NoonerBear/sounds/581549/ - CC0 flatline.
59. Freesound "Bone saw" (Diramus) - https://freesound.org/people/Diramus/sounds/365422/ - CC0 saw.
60. Freesound "Electric butcher's bone saw" - https://freesound.org/people/Vortichez/sounds/545431/ - CC BY 4.0.
61. Freesound "Dentist Suction and air puffer" - https://freesound.org/people/Cheeseheadburger/sounds/141511/ - CC BY 4.0.
62. Freesound "Heartbeat recorded with Contact Microphone" - https://freesound.org/people/Schacht/sounds/793474/ - CC BY 4.0.
63. Freesound "Heart Monitor Beep Loop" - https://freesound.org/people/Zen53/sounds/678011/ - CC BY 4.0, synthesised.
64. Freesound "ICU.wav" - https://freesound.org/people/coetzee_megan12/sounds/366006 - CC BY-NC 3.0.
65. Freesound "Vinyl Gloves getting put on" - https://freesound.org/people/shaderrow/sounds/362933/ - CC BY-NC 4.0.
66. Freesound searches "surgery" / "cautery" / "peristaltic pump" - https://freesound.org/search/?q=surgery&f=&s=Automatic+by+relevance - license counts and gaps.
67. rekkerd.org, Sonniss GDC 2026 bundle - https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/ - size and terms.
68. GameFromScratch, Sonniss GDC 2024 bundle (snippet only) - https://gamefromscratch.com/sonniss-27-5gb-sound-effect-giveaway-at-gdc-2024/ - no-AI-training clause.
69. MakeHuman community license - https://static.makehumancommunity.org/about/license.html - AGPL/GPL code, CC0 assets.
70. MPFB on Blender Extensions - https://extensions.blender.org/add-ons/mpfb/ - version 2.0.18, GPL-3.0-or-later.
71. Mixamo FAQ thread (Adobe Community, 2022) - https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/td-p/13234775 - royalty-free use, no raw-file distribution.
72. Reallusion content license - https://www.reallusion.com/license/content.html - Standard vs Extended.
73. CG Channel, Character Creator 5 release - https://www.cgchannel.com/2025/08/reallusion-releases-character-creator-5/ - date, price, formats.
74. MetaHuman 5.6 release post (Epic forum) - https://forums.unrealengine.com/t/metahuman-5-6-release/2539165 - use in any engine.
75. CG Channel, MetaHuman 5.6 licensing - https://www.cgchannel.com/?p=167592 - USD 1M threshold, seat price, AI restriction.
76. Microsoft Rocketbox (GitHub) - https://github.com/microsoft/Microsoft-Rocketbox - MIT, 115 avatars, blendshapes.
77. Ready Player Me (Wikipedia) - https://en.wikipedia.org/wiki/Ready_Player_Me - acquisition and shutdown dates.
78. Blender license - https://www.blender.org/about/license/ - GPL; output belongs to the user; add-ons GPL.
79. Blender releases - https://www.blender.org/download/releases/ - 5.0, 5.1, 5.2 LTS dates.
80. Blender manual, Render Baking (5.2 LTS) - https://docs.blender.org/manual/en/latest/render/cycles/baking.html - bake types, cage, margin.
81. glTF-Blender-IO (GitHub) - https://github.com/KhronosGroup/glTF-Blender-IO - Apache-2.0, bundled.
82. Blender glTF exporter commit (2022) - https://archive.blender.org/lists/bf-extensions-cvs/2022-April/010894.html - 4-influence limit.
83. Vulkan docs glTF Blender workflow (snippet only) - https://docs.vulkan.org/tutorial/latest/Advanced_glTF/Tooling_Production_Pipeline/02_blender_workflow.html - shape keys to morph targets.
84. QRemeshify (GitHub) - https://github.com/ksami/QRemeshify - GPL-3.0, Blender 4.2+.
85. Instant Meshes license - https://raw.githubusercontent.com/wjakob/instant-meshes/master/LICENSE.txt - BSD-3-style.
86. Blender Extensions "About" - https://extensions.blender.org/about/ - GPL-compliant software only.
87. CC BY-NC 4.0 legal code - https://creativecommons.org/licenses/by-nc/4.0/legalcode.en - NonCommercial definition; attribution clause.
88. CC BY-SA 4.0 legal code - https://creativecommons.org/licenses/by-sa/4.0/legalcode.en - Adapted Material, ShareAlike.
89. Creative Commons FAQ - https://creativecommons.org/faq/ - combining works, collections, ND private use, NC meaning.
90. CC recommended attribution practices - https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution - TASL.
91. GNU GPL FAQ - https://www.gnu.org/licenses/gpl-faq.en.html - private modifications; output not covered.
92. TurboSquid license limitations - https://www.turbosquid.com/help/en/articles/14829413-what-are-the-limitations-and-upgrade-policies-for-3d-model-licenses-on-turbosquid - editorial cannot become game use.
93. Wikimedia Commons, Median sternotomy category - https://commons.wikimedia.org/wiki/Category:Median_sternotomy - 4 photos.
94. Wikimedia Commons, retracted sternum photo - https://commons.wikimedia.org/wiki/File:Стернотомия._Края_грудины_разведены.jpg - CC0.
95. Atlas of Human Cardiac Anatomy (UMN) - https://www.vhlab.umn.edu/atlas/ - educational use, watermark rule.
96. Teleflex Finochietto retractors (snippet only) - https://ca.myteleflex.com/All-Categories/Surgical-Instruments/CVT/Finochietto-Retractors/p/su-FinochiettoRetractors - design reference.
97. RenderHub thoracic retractor listing - https://www.renderhub.com/7dmax/heavy-duty-3d-rib-spreader-thoracic-retractor-surgical-preci - paid alternative.
98. Sonniss Hospital Ambiences - https://sonniss.com/sound-effects/hospital-ambiences/ - paid OR ambience library.

---

## Summary

### Key findings

- **BodyParts3D changed license.** The current DBCLS license page says **CC BY 4.0** (updated 2025-02-27), not the old CC BY-SA 2.1 Japan ([lic](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html)). This makes it the best GREEN base for a labelled heart with named coronary branches. Its meshes are 99% reduced, so a re-sculpt and retopology are needed.
- **The most realistic free hearts are non-commercial.** Real-heart scans (VisibleHeartLabs, CU Anschutz CABG heart, UMCG dominance variants) are **CC BY-NC or BY-NC-SA**. They suit this personal project and visual reference, but they must be replaced before any commercial release.
- **Clean CC BY alternatives exist.** HRA heart GLBs ([CCF](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html)), NIH 3D CC BY hearts ([3DPX-011381](https://3d.nih.gov/entries/3DPX-011381)) and the CC BY TotalSegmentator dataset ([Zenodo](https://zenodo.org/records/10047292)).
- **OR furniture is easy; cardiac instruments are not.** CC BY OR tables, lights, monitors and a basic CPB machine exist. **No free sternal retractor or sternal saw** was found, so these must be modelled in-house.
- **Environment materials are CC0** (Poly Haven, ambientCG), including two CC0 hospital HDRIs. **No free tissue materials** were found; tissue should be procedural and baked.
- **OR audio: good CC0 core.** Real OR suction, a surgery field recording, a Lifepak monitor, a ventilator and room tone are all CC0. Cautery, sternal saw, roller-pump and standards-style alarms must be recorded or synthesised.
- **Characters:** MPFB 2.0.18 (CC0 assets) and Rocketbox (MIT) are the safest. MetaHuman is now usable in any engine (since 5.6) but is optional. **Ready Player Me is gone** (shut down 2026-01-31).
- **Pipeline:** Blender 5.2 LTS → GLB with shape-key heartbeat. Skinning is capped at 4 influences per vertex.

### Recommendations

1. Create `ASSET_LICENSES.md` and the GREEN / AMBER / RED folder split **before** importing any asset (section 8.2).
2. Base heart: BodyParts3D 4.0 (CC BY), re-sculpted against the NC real-heart scans used as reference only. Keep the FMA IDs as mesh names for gameplay hit-testing.
3. Add HRA (CC BY) and TotalSegmentator (CC BY data) hearts as anatomical variants. Use 3D Slicer for segmentation-to-mesh.
4. Use Z-Anatomy only for reference or thorax context, kept in an `amber_sa/` folder.
5. Build in-house: Finochietto retractor, sternal saw, aortic cross-clamp, cannulae and a detailed CPB console (generic, no brand marks).
6. Audio: start from the 5 CC0 OR recordings. Record or synthesise cautery, saw, pump and alarm sounds. Store the Sonniss license text inside the repo's private vendor folder.
7. Never commit RED assets or no-redistribution raw files (Mixamo FBX, MM-WHS, ImageCAS, Sonniss raw files) to the public GitHub repository.
8. Re-verify every license on the day of any public release. Licenses change (BodyParts3D just did).

### Open questions

- Does the HRA heart GLB contain coronary arteries, valves and cardiac veins? (Download and inspect; not stated on the library page.)
- Does BodyParts3D 4.0 include an aortic valve and cardiac veins? (The aortic valve was not found in the 3.0 parts list extraction.)
- What are the exact ImageCAS and ASOCA terms, and is redistribution of derived meshes allowed?
- What are the exact current Sonniss GDC license text, the full Fab EULA, the official Mixamo helpx FAQ, and the CTSNet terms? (All pages were blocked.)
- Is the 2025 CC BY "Anatomically Correct Human Heart" (1M faces) original work, or AI-generated / re-uploaded?
- Which Freesound or other CC0 sources exist for electrocautery and CPB roller pumps? (Not searchable after the search budget ran out.)
- What are the IEC 60601-1-8 alarm-tone patterns, so synthesised monitor alarms sound right? (Not researched; needs a follow-up.)
