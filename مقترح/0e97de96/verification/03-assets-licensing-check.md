# Evidence check 03: Free assets and their licenses

> Checked 2026-11-03 by an independent fact-checker (fresh searches). Counts: confirmed 10, corrected 7, refuted 0, unverified 0. (17 items: the 12 flagged claims 03.1 to 03.12 plus 5 extra statements 03.X1 to 03.X5. Flagged claims alone: confirmed 7, corrected 5.)
>
> Method: official pages were fetched directly where possible. Data files were downloaded and inspected: the BodyParts3D 4.0 parts lists and element lists, the HRA heart v1.3 graph and GLB, the glTF-Blender-IO exporter source, the Sketchfab API records, the Poly Haven API and PyPI. Some pages could not be fetched (Epic EULA pages, Fab EULA, glTF spec page: HTTP 403). Where evidence comes only from a search snippet, this is stated.

## Verdict table

| ID | Claim (short) | Verdict | Correct value / note | Evidence [links] | Grade A/B/C |
|---|---|---|---|---|---|
| 03.1 | BodyParts3D now CC BY 4.0 (page updated 2025-02-27); 3.0 was CC BY-SA 2.1 JP | CONFIRMED | CC BY 4.0, history entry 2025/02/27 (the License section itself says "Last updated : 2025/02/25"). The 2011 README says CC BY-SA 2.1 Japan. | [lic](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [LATEST README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/README_e.html), [2011 README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html) | A |
| 03.2 | BP3D 4.0 offers only 99%-reduced OBJ (136 MB / 62 MB); parts list has no aortic valve or pericardium | CORRECTED | 99% only, 136 MB IS-A and 62 MB PART-OF: correct. No pericardium: correct. **But the 4.0 parts lists do include the aortic valve** (FMA7236, BP9447) and its three cusps, with element meshes (FJ2426, FJ2431, FJ2435). | [download](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html), [isa_parts_list_e.txt](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/isa_parts_list_e.txt), [partof_element_parts.txt](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/partof_element_parts.txt) | A |
| 03.3 | All HRA/CCF 3D objects, incl. heart GLB v1.2 (June 2022), are CC BY 4.0 | CORRECTED | CC BY 4.0: correct (also on v1.3). **The latest heart is v1.3** (male and female; graph metadata dated 2024-06-15), not v1.2. The v1.3 male GLB has chambers, septum, papillary muscles and 4 valves, but no coronaries, cardiac veins or great vessels. | [lod.humanatlas.io heart-male](https://lod.humanatlas.io/ref-organ/heart-male/), [v1.3 graph](https://lod.humanatlas.io/ref-organ/heart-male/v1.3/graph.jsonld), [v1.3 GLB](https://cdn.humanatlas.io/digital-objects/ref-organ/heart-male/v1.3/assets/3d-vh-m-heart.glb) | A |
| 03.4 | TotalSegmentator heartchambers_highres and coronary_arteries need a license key, free only for non-commercial use; code Apache-2.0 | CONFIRMED | Both tasks are listed "Available with a license"; "free licenses available for non-commercial usage"; commercial use by contacting the author. The LICENSE file and PyPI say Apache 2.0. | [README](https://raw.githubusercontent.com/wasserth/TotalSegmentator/master/README.md), [LICENSE](https://raw.githubusercontent.com/wasserth/TotalSegmentator/master/LICENSE), [PyPI](https://pypi.org/project/TotalSegmentator/) | A |
| 03.5 | TotalSegmentator CT dataset v2.0.1: CC BY 4.0, 1,228 CTs, 117 structures, 23.6 GB | CONFIRMED | All values match the Zenodo record (published 2023-10-27). The Academic Torrents mirror also lists CC BY 4.0. | [Zenodo](https://zenodo.org/records/10047292), [Academic Torrents](https://academictorrents.com/details/1dfeb3186514b40a2c212c21d494c665766bfbf4) | A |
| 03.6 | VisibleHeartLabs hearts (e.g. Heart0102) CC BY-NC 4.0; CU Anschutz CABG heart CC BY-NC-SA 4.0 | CONFIRMED | The Sketchfab API gives Heart0102 by-nc/4.0 and #0084 by-nc/4.0. The Cardiac Bypass heart is by-nc-sa/4.0 with 1,000,000 faces. The CU Anschutz OER hub says its plastinate library is CC BY-NC-SA 4.0. | [Sketchfab API Heart0102](https://api.sketchfab.com/v3/models/6e3ddf0caa2640b39aa240f8c4ffc1ea), [API bypass heart](https://api.sketchfab.com/v3/models/98dca43ff0c146b696148e6c3e70dbc0), [CU Anschutz OER hub](https://medschool.cuanschutz.edu/ms-modern-human-anatomy/student-resources/OERAnatomyHub) | A |
| 03.7 | Megascans mostly paid on Fab since 2025; Bridge legacy under UE-only Epic Content License; Fab Personal tier ≤ USD 100k / 12 months | CONFIRMED | Epic: "All Megascans will be free until the end of 2024 under Fab's Standard License". 2025 prices: $0.99 per asset, $4.99 procedural kits, $24.99 packs, plus some free content. Bridge access "licensed for use with Unreal Engine and Twinmotion only". Personal tier: "not generated more than $100,000 USD in gross revenue from commercial activity in the last 12 months". | [Epic forum (official)](https://forums.unrealengine.com/t/upcoming-changes-to-quixel-related-to-fabs-launch-in-october/2024362), [Bridge docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine), [Fab licenses](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab) | A/B |
| 03.8 | Sonniss GDC bundles (2026: 7.47 GB+) royalty-free, no attribution, unlimited projects; 2024+ bundles forbid AI training | CORRECTED | The official license page could be read. It is **Version 2.0, effective 27 August 2026**. It is royalty-free, needs no attribution, allows unlimited projects and **forbids AI training**. It also forbids passing the sounds on as sound effects. Its terms follow the **download date**, not the bundle year: earlier downloads follow the version in force that day. Bundle size 7.47 GB confirmed. | [Sonniss license](https://sonniss.com/gdc-bundle-license/), [BPB 2026 bundle](https://bedroomproducersblog.com/2026/03/16/sonniss-gdc-2026-bundle/) | A |
| 03.9 | MetaHuman any engine since 5.6 (2025-06-03); free < USD 1M (seat USD 1,850/yr); no AI training | CORRECTED | Any engine since 5.6, the USD 1M limit and the USD 1,850/year seat: confirmed. **The no-AI-training rule is outdated.** On 2026-10-29 Epic published "UE devs can now choose to train AI Models on their projects": an updated UE EULA that lets developers opt in to AI training on their own UE and MetaHuman projects (seen only as a snippet; the official page returned 403). | [CG Channel](https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/), [Digital Production](https://digitalproduction.com/2025/06/05/metahumans-graduate-ready-for-unity-godot-and-the-fab-cash-register/), [Epic post](https://www.unrealengine.com/ue-devs-can-now-choose-to-train-ai-models-on-their-projects), [daily.dev](https://daily.dev/posts/ue-devs-can-now-choose-to-train-ai-models-on-their-projects-kqebavnzd), [Game Developer](https://www.gamedeveloper.com/programming/epic-is-updating-the-eula-to-allow-ai-training-on-outputs-from-unreal-engine-and-metahuman) | B/C |
| 03.10 | Ready Player Me public services shut down 2026-01-31 after Netflix acquisition (Dec 2025) | CONFIRMED | PocketGamer.biz (2025-12-22): acquired by Netflix for an undisclosed fee (reported 2025-12-19), and "will shut down its services on January 31st, 2026, including ... PlayerZero". | [PocketGamer.biz](https://www.pocketgamer.biz/netflix-acquires-avatar-creation-platform-ready-player-me/) | B |
| 03.11 | MPFB 2.0.18 (2026-10-10) GPL-3.0-or-later; MakeHuman core assets CC0 | CONFIRMED | Versions page: 2.0.18 released October 10, 2026, Blender 4.2 LTS+, "GNU General Public License v3.0 or later". MakeHuman FAQ: the base mesh, targets and proxies became CC0 in 2020; the MPFB FAQ says the core assets are CC0. | [MPFB versions](https://extensions.blender.org/add-ons/mpfb/versions/), [MakeHuman 2020 license FAQ](https://static.makehumancommunity.org/oldsite/faq/what_changed_regarding_the_license_in_2020.html), [MPFB FAQ](https://static.makehumancommunity.org/mpfb/faq/can_i_sell_models.html) | A |
| 03.12 | Blender glTF exporter keeps only the 4 highest bone weights (normalised); shape keys → morph targets | CORRECTED | Shape keys → morph targets: confirmed. **4 is only the default.** The "Bone Influences" setting (default 4, min 1) can raise it, and "Include All Bone Influences" exports all of them. When there are more than N, the exporter keeps "the N with highest weight ... (and normalized)". The manual warns that viewers may show wrong results for values other than 4 or 8. | [Blender 4.2 manual, glTF](https://docs.blender.org/manual/en/4.2/addons/import_export/scene_gltf2.html), [exporter `__init__.py`](https://github.com/KhronosGroup/glTF-Blender-IO/blob/main/addons/io_scene_gltf2/__init__.py), [primitive_extract.py](https://github.com/KhronosGroup/glTF-Blender-IO/blob/main/addons/io_scene_gltf2/blender/exp/primitive_extract.py) | A |
| 03.X1 | TotalSegmentator current version "v2.11/2.12 (uncertain)" | CORRECTED | The current release is **2.18.0** (PyPI, uploaded 2026-08-12). | [PyPI](https://pypi.org/project/TotalSegmentator/) | A |
| 03.X2 | BodyParts3D has no diagonal branch, coronary sinus, cardiac veins or separate pulmonary trunk | CORRECTED | The 4.0 lists include the diagonal branch (FMA3860), the coronary sinus (FMA4706), the great, middle, small and anterior cardiac veins, and the pulmonary trunk (FMA8612). The 3.0 list already had the coronary sinus and the great, middle and small cardiac veins. No obtuse marginal branch and no pericardium in either list. | [isa_parts_list_e.txt](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/isa_parts_list_e.txt), [3.0 parts list](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt) | A |
| 03.X3 | Blender 5.2 LTS released 2026-07-14 (5.0 2025-11-18, 5.1 2026-03-17) | CONFIRMED | All three dates match; 5.2 is labelled LTS. | [Blender releases](https://www.blender.org/download/releases/) | A |
| 03.X4 | Poly Haven Hospital Room HDRI up to 17K; Hospital Room 2 up to 20K | CONFIRMED | API max_resolution: [17000, 8500] (Oliksiy Yakovlyev) and [20480, 10240] (Dimitrios Savva, Jarod Guest). | [API hospital_room](https://api.polyhaven.com/info/hospital_room), [API hospital_room_2](https://api.polyhaven.com/info/hospital_room_2) | A |
| 03.X5 | Adult heart length roughly 12 cm (marked "uncertain - not researched") | CONFIRMED | OpenStax A&P 2e: "12 cm (5 in) in length, 8 cm (3.5 in) wide ... 6 cm (2.5 in) in thickness". Mass: female 250–300 g, male 300–350 g. | [OpenStax 19.1](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy) | A |

## Details

### 03-1
The DBCLS license page states: "The license for this database is specified in the Creative Commons Attribution 4.0 International" ("Last updated : 2025/02/27"). The LATEST README is a separate official document. Its update history has "2025/02/27 'License' is updated" and "2013/06/19 3D data (Release 4.0) is updated". Its License section header reads "Last updated : 2025/02/25", a two-day internal mismatch that does not matter. The 2011 README (release 3.0) says: "Creative Commons Attribution-Share Alike 2.1 Japan". Attribution text for 4.0: "BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International".

### 03-2
The download page lists only `isa_BP3D_4.0_obj_99.zip` (136 MB) and `partof_BP3D_4.0_obj_99.zip` (62 MB), both "Polygon reduction rate = 99%". The 3.0 README also offered 95% data. I downloaded the current `isa_parts_list_e.txt` (2,906 lines) and `partof_parts_list_e.txt` (1,369 lines). They contain "FMA7236 BP9447 aortic valve" and the right posterior, anterior and left posterior cusps of the aortic valve. `partof_element_parts.txt` maps the aortic valve to element files FJ2426, FJ2431 and FJ2435, so meshes exist. No line matches "pericardi". The report's "no aortic valve" came from the old 3.0 list (`20110915/parts_list_e.txt`), which indeed has no aortic valve entry.

### 03-3
The CCF library page states "All CCF 3D reference objects are released under Attribution 4.0 International (CC BY 4.0)" but lists only heart v1.0 to v1.2. The HRA linked-data server (`lod.humanatlas.io/ref-organ/heart-male/` and `.../heart-female/`) lists v1.0, v1.1, v1.2 and **v1.3**. The v1.3 graph has `"dct:license": "https://creativecommons.org/licenses/by/4.0/"` and `"dct:created": "2024-06-15"`. The v1.3 male GLB (4.07 MB, babylon.js exporter for Maya 2023.2) has 18 nodes. They cover the heart, cardiac chamber, left and right atrium, left and right ventricle, interventricular septum, the aortic, mitral, pulmonary and tricuspid valves, a generic heart valve, and 5 named papillary muscles. It has no coronary artery, cardiac vein, aorta or pulmonary trunk node. One caveat: an NIH 3D record notes a licensing change at v1.3 for the brain, so "all objects CC BY" may not hold for every older version of every organ. Check the version you download.

### 03-4
README (master): the openly available tasks are "Openly available for any usage (Apache-2.0 license)". `heartchambers_highres`, `coronary_arteries`, `aortic_sinuses` (and others) are under "Available with a license", with "free licenses available for non-commercial usage" and commercial use via jakob.wasserthal@usb.ch. The LICENSE file is Apache License 2.0, and PyPI also lists "Apache 2.0". A maintainer note quoted on the Slicer forum adds that segmentations from restricted models are not to be used to train new models (snippet only).

### 03-5
Zenodo record 10047292: "Dataset with segmentations of 117 important anatomical structures in 1228 CT images", "Version 2.0.1", license "Creative Commons Attribution 4.0 International", "Files (23.6 GB)", "Published October 27, 2023". The Academic Torrents mirror of the v2 dataset also gives CC BY 4.0.

### 03-6
Sketchfab API: "Heart0102 Coronary Arteries" (VisibleHeartLabs) has license url `http://creativecommons.org/licenses/by-nc/4.0/`, 194,226 faces, published 2022-11-18. "Human Heart with Coronary Contrast #0084" is by-nc/4.0 with 598,412 faces. "Human Heart Cardiac Bypass" (stetterAnschutz) is `by-nc-sa/4.0` with 1,000,000 faces, published 2024-06-27. "Anatomical heart - left dominance" (eLearningUMCG) is by-nc-sa/4.0 with 169,657 faces. The CU Anschutz Modern Human Anatomy OER hub, an independent institutional page, says "Many of our 3D models and our entire plastinate library" are "CC BY-NC-SA under Creative Commons 4.0".

### 03-7
Epic's official forum notice "Upcoming changes to Quixel related to Fab's launch in October" gives the following. Free until end of 2024 under the Fab Standard License. From 2025, prices start at $0.99 (2D/3D), $4.99 (procedural kits) and $24.99 (packs), and "some free Megascans content will remain available". Bridge and Quixel.com downloads are under the Epic Content License. Epic's Bridge plugin docs add: "This unlimited Megascans access is licensed for use with Unreal Engine and Twinmotion only" ("UE-Only Content"). Epic's Fab docs define the Personal tier: "For buyers who have not generated more than $100,000 USD in gross revenue from commercial activity in the last 12 months". The full Fab EULA (fab.com/eula) still returned 403. A 2026 third-party page reports that most Megascans are still paid.

### 03-8
The official page `sonniss.com/gdc-bundle-license` loaded in this check. It shows "Version 2.0 · Effective 27 August 2026" and applies to sound effects downloaded on or after that date; earlier downloads are governed by the version published on their download day, and earlier versions are archived. Key terms: "worldwide, non-exclusive, royalty-free license"; "Licensee may use the licensed sound effects on an unlimited number of projects"; "without attribution to the original creator"; "expressly prohibited from using any sound effects licensed under this Agreement for the purpose of training" AI. Redistributing the sounds as sound effects (raw or modified, alone or in packs) is not allowed. Bedroom Producers Blog (2026-03-16) gives the 2026 bundle as 7.47 GB, 347+ WAV files. The "17 vendors" figure was not checked.

### 03-9
CG Channel (2025-06-04) and Digital Production (2025-06-05) both report the following. From 5.6, MetaHuman is under the standard UE EULA and usable in "games created in other engines, like Unity or Godot". It is free "under $1 million/year in revenue", and seats "currently cost $1,850/year". At that time it could not be used to train AI. Then on 2026-10-27/28, Game Developer, Renderu and WN Hub reported Tim Sweeney saying Epic is "working to remove this restriction from EULA terms". A 2026-10-29 Epic post, "UE devs can now choose to train AI Models on their projects", is summarised by daily.dev (2026-10-30) as: Epic "updated the Unreal Engine End User License Agreement so developers can opt in to training AI models on their own Unreal Engine and MetaHuman projects". Per the search summary, existing users accept it on the EULA acceptance page and Fab sellers keep the NoAI tag. The Epic page itself returned 403, so the exact EULA wording is not verified. Grade B/C.

### 03-10
PocketGamer.biz (2025-12-22) says: "Avatar-creation platform Ready Player Me has been acquired by Netflix for an undisclosed fee" and "Ready Player Me will shut down its services on January 31st, 2026, including its online avatar creation tool, PlayerZero". It cites a TechCrunch report of 2025-12-19. One blog (Ryan Schultz) gives 30 January for the avatar-creator tools, but 31 January is the date most sources report. Wikipedia's only citation is still a Medium post, but the claim now has an independent trade-press source.

### 03-11
The Blender Extensions versions page lists 2.0.18 (October 10, 2026), 2.0.17 (July 22, 2026) and earlier, all "4.2 LTS and newer", under "GNU General Public License v3.0 or later". The MakeHuman FAQ "What changed regarding the license in 2020?" says the targets, proxies and base mesh moved from AGPL "source code" to CC0 graphical assets in September 2020 (MakeHuman 1.2.0, released 2020-11-06). The MPFB FAQ says all core assets (base mesh, targets, skins...) are CC0. Community assets keep their own licenses.

### 03-12
Blender 4.2 manual, glTF add-on: "Data - Shape Keys: Export shape keys (morph targets)". Under "Data - Skinning": "Bone influences: How many joint vertex influences will be exported. Models may appear incorrectly in many viewers with value different to 4 or 8", and "Include All Bone Influences: Export all joint vertex influences". In the current exporter source (`io_scene_gltf2/__init__.py`, v5.4.11), `export_influence_nb` has "default=4, min=1" and there is an `export_all_influences` option. `primitive_extract.py` logs: "There are more than {N} joint vertex influences. The {N} with highest weight will be used (and normalized)". glTF stores influences in sets of 4 (JOINTS_n/WEIGHTS_n). The spec page itself returned 403, so its exact wording on multiple sets is not quoted.

### 03-X1
PyPI JSON for TotalSegmentator shows releases 2.13.0 (2026-03-17), 2.14.0 (2026-06-10), 2.15.0 (2026-07-01), 2.16.0 (2026-07-21), 2.17.0 (2026-07-29) and **2.18.0 (2026-08-12)**, license "Apache 2.0". The README still uses a 2.11.0 Docker tag in an example, which explains the report's guess.

### 03-X2
Current lists (`LATEST/isa_parts_list_e.txt`, `partof_parts_list_e.txt`, `isa_element_parts.txt`) include:
- FMA3860 "diagonal branch of anterior descending branch of left coronary artery" (10 element meshes);
- FMA4706 "coronary sinus" (FJ2655) and FMA4707 "great cardiac vein" (FJ2656), plus the middle, small and anterior cardiac veins;
- FMA8612 "pulmonary trunk" (FJ2966).

The 3.0 list (`20110915/parts_list_e.txt`) already contained the coronary sinus and the great, middle and small cardiac veins. Neither list has a pericardium or an obtuse marginal entry.

### 03-X3
blender.org/download/releases: "Blender 5.0 ... Released on November 18th, 2025"; "Blender 5.1 ... Released on March 17th, 2026"; "Blender 5.2 LTS ... Released July 14th, 2026". No newer release is listed.

### 03-X4
Poly Haven public API: `hospital_room` has authors {"Oliksiy Yakovlyev": "All"} and max_resolution [17000, 8500]. `hospital_room_2` has authors Dimitrios Savva (Photography) and Jarod Guest (Processing), with max_resolution [20480, 10240], i.e. 17K and 20K.

### 03-X5
OpenStax Anatomy & Physiology 2e, section 19.1: "A typical heart is approximately the size of your fist: 12 cm (5 in) in length, 8 cm (3.5 in) wide, and 6 cm (2.5 in) in thickness". Female hearts weigh about 250–300 g and male hearts about 300–350 g. This supports the report's scale check ("roughly 12 cm"). No edit was made because the statement is correct.

## Resolved open questions

1. **Does the HRA heart GLB contain coronary arteries, valves and cardiac veins?** Resolved (A, direct inspection). The latest version is v1.3 (male and female, CC BY 4.0). The v1.3 male GLB contains the 4 chambers, the interventricular septum, the **aortic, mitral, pulmonary and tricuspid valves**, and 5 named papillary muscles. It has **no coronary arteries, no cardiac veins and no great vessels**. Use it for the valve and chamber interior. Coronaries must come from BodyParts3D or be modelled. Sources: [v1.3 graph](https://lod.humanatlas.io/ref-organ/heart-male/v1.3/graph.jsonld), [v1.3 GLB](https://cdn.humanatlas.io/digital-objects/ref-organ/heart-male/v1.3/assets/3d-vh-m-heart.glb).
2. **Does BodyParts3D 4.0 include an aortic valve and cardiac veins?** Resolved (A): **yes, both.** The aortic valve is FMA7236 with three cusps (element meshes FJ2426, FJ2431, FJ2435). The cardiac veins are the coronary sinus FMA4706, great FMA4707, middle FMA4713, small FMA4714 and anterior FMA76767. The 4.0 lists also add a diagonal branch (FMA3860) and the pulmonary trunk (FMA8612). There is still no pericardium. Sources: [isa_parts_list_e.txt](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/isa_parts_list_e.txt), [partof_element_parts.txt](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/partof_element_parts.txt).
3. **What is the exact current Sonniss GDC license text?** Resolved (A). Version 2.0, effective 27 August 2026; terms follow the download date. It is royalty-free and worldwide, allows unlimited projects and needs no attribution. AI training is prohibited, and so is redistributing the sounds as sound effects (raw, modified or in packs); finished projects may be distributed. Source: [sonniss.com/gdc-bundle-license](https://sonniss.com/gdc-bundle-license/). The Fab EULA, the Adobe Mixamo helpx FAQ and the CTSNet terms remain unverified: the Fab EULA returned 403 and the others were not retried.
4. **What are the IEC 60601-1-8 alarm-tone patterns?** Partly resolved (C, secondary sources; the standard was not read).
   - High priority: a 10-pulse burst made of "two identical groups of 5 PULSES with a pause between each group".
   - Medium priority: a 3-pulse burst.
   - Low priority: 1 or 2 pulses, optionally repeated.
   - Higher priority uses faster bursts and shorter pulses that repeat more often.
   - Pulse fundamental 150–1000 Hz, with at least 4 harmonics in 300–4000 Hz within ±15 dB of the fundamental. A vendor guide citing AMD2:2020 instead says "at least five peaks" in 150–4000 Hz.

   Exact pulse and burst timings (Table 3 of the standard) were not obtained. Sources: [Har-El 6.3.3.1](https://standards.har-el.com/Projects/181701/60601-1-8/html/A2SubCl-6-3-3-1-a-priority-encoded.htm), [MSP Indy](https://mspindy.com/technical-articles/using-audible-alarms-in-medical-equipment-iec-60601-1-8/).

Also noted, not resolved: ImageCAS is now distributed through a Kaggle dataset page (per its README and the ImageCAS-X paper), but no license field was found. The ASOCA terms are only visible after a Grand Challenge login.

## Edits made to the report

All edits are in `research/03-assets-licensing.md`, in place, each with the marker "[Step 2 check: corrected, see verification/03-assets-licensing-check.md#03-N]".

1. §0 table, BodyParts3D row (03.2): "It has named coronary branches, 3 of 4 valves and the sternum parts." -> "It has named coronary branches, all 4 valves (the current 4.0 parts lists include the aortic valve, FMA7236) and the sternum parts [marker #03-2]."
2. §0 table, HRA row (03.3): "(male + female GLB, v1.2 June 2022), **CC BY 4.0**." -> "(male + female GLB; latest is v1.3, graph metadata dated 2024-06-15; v1.2 was June 2022), **CC BY 4.0**. It has chambers, septum, papillary muscles and all 4 valves, but no coronary arteries, cardiac veins or great vessels [marker #03-3]."
3. §0 table, Sonniss row (03.8): "2024+ bundles reportedly forbid AI training. The license page could not be loaded, so keep..." -> "The official license (Version 2.0, effective 27 August 2026; terms follow the download date, not the bundle year) forbids AI training and forbids redistributing the sounds as sound effects [marker #03-8]. Keep..."
4. §0 table, MetaHuman row (03.9): "free under USD 1M revenue, no AI training." -> "free under USD 1M revenue. The former no-AI-training rule was changed by an Epic EULA update announced 2026-10-29 that lets developers opt in to AI training on their own UE/MetaHuman projects; re-check the current EULA [marker #03-9]."
5. §0 table, Export format row (03.12): "Skinning is limited to **4 bone influences per vertex**." -> "Skinning exports **4 bone influences per vertex by default** (the exporter's "Bone Influences" setting can raise this, or "Include All Bone Influences"; many viewers expect 4 or 8) [marker #03-12]."
6. §2.1 HRA row (03.3): "v1.0 March 2021, v1.1 December 2021, **v1.2 June 2022**" -> "v1.0 March 2021, v1.1 December 2021, v1.2 June 2022, and **v1.3** (latest; listed at lod.humanatlas.io, graph metadata dated 2024-06-15) [marker #03-3]".
7. §2.2 Valves row (03.2): "**No aortic valve entry was found** in the extraction (uncertain: it may be grouped elsewhere)." -> "The 3.0 list has no aortic valve entry, but the **current 4.0 IS-A/PART-OF lists include the aortic valve (FMA7236) and its three cusps** [marker #03-2]."
8. §2.2 Great vessels row (03.X2): '"pulmonary artery" (no separate pulmonary trunk entry)' -> '"pulmonary artery" (the 4.0 lists also have a separate pulmonary trunk, FMA8612 [marker #03-X2])'.
9. §2.2 Missing row (03.X2): "No diagonal or obtuse marginal branches by name. No coronary sinus or cardiac veins were found in the extraction (uncertain)." -> "No obtuse marginal branch by name. The 4.0 lists do include a diagonal branch (FMA3860), the coronary sinus (FMA4706) and the great, middle, small and anterior cardiac veins (the 3.0 list already had the coronary sinus and great/middle/small cardiac veins) [marker #03-X2]."
10. §2.3 BodyParts3D valves cell (03.2): "Tricuspid, pulmonary, mitral (aortic not found)" -> "Tricuspid, pulmonary, mitral, aortic (aortic in the 4.0 lists) [marker #03-2]".
11. §2.3 HRA row (03.3): "HRA heart v1.2 | Not stated on the library page (uncertain) | Not stated (uncertain) | Not stated (uncertain)" -> "HRA heart v1.2 (latest v1.3) | None in the v1.3 male GLB | Aortic, mitral, pulmonary, tricuspid | None (chambers, septum, valves and papillary muscles only) [marker #03-3]".
12. §2.5 TotalSegmentator notes (03.X1): "The README mentions v2.11/2.12 (exact current version uncertain)" -> "The current release is v2.18.0 (PyPI, 2026-08-12) [marker #03-X1]".
13. §5.4 Sonniss, bullet 2 (03.8): appended "The current official license forbids AI training for any sounds downloaded under it; its terms follow the download date, not the bundle year [marker #03-8]."
14. §5.4 Sonniss, bullet 3 (03.8): "The official license page (`sonniss.com/gdc-bundle-license`) showed only a bot check: **UNVERIFIED**." -> "The official license page (...) was readable in Step 2: Version 2.0, effective 27 August 2026. It applies to downloads on or after that date (...). It grants a royalty-free license for unlimited projects without attribution, forbids AI training, and forbids passing the sounds on as sound effects (...) [marker #03-8]."
15. §6 MetaHuman row (03.9): appended to "...but **not to train AI** ([CG Channel](...))" the text "; an Epic EULA update announced 2026-10-29 lets developers opt in to AI training on their own UE/MetaHuman projects [marker #03-9]."
16. §7.2 step 4 (03.X2): "Add missing parts (aortic valve, pericardium, cardiac veins, diagonal branches)." -> "Add missing parts (pericardium; BP3D 4.0 has the aortic valve, cardiac veins and a diagonal branch, but refine them if the 99% reduction leaves them too coarse) [marker #03-X2]."
17. §7.3 option B export facts (03.12): "glTF standard skinning keeps **4 influences per vertex**. When more exist, Blender's exporter keeps "the 4 with highest weight" and normalises them" -> "glTF stores skin weights in sets of **4 influences** (JOINTS_n/WEIGHTS_n). Blender's exporter exports 4 by default ("Bone Influences", configurable, or "Include All Bone Influences"); when more exist, it keeps the N with the highest weight and normalises them ... [marker #03-12]".
18. §8.2 rule 8 (03.9): "(MetaHuman, Sonniss 2024+, Mixamo FAQ, Sketchfab NoAI tag)" -> "(MetaHuman until Epic's EULA update announced 2026-10-29, Sonniss, Mixamo FAQ, Sketchfab NoAI tag) [marker #03-9]".
19. Key claims #4 (03.2): "tricuspid, pulmonary and mitral valves; sternum parts" -> "tricuspid, pulmonary and mitral valves (and, in the 4.0 lists, the aortic valve) [marker #03-2]; sternum parts".
20. Key claims #6 (03.3): "heart GLB v1.2 is from June 2022" -> "heart GLB v1.2 is from June 2022, and the latest heart version is v1.3 [marker #03-3]".
21. Key claims #26 (03.9): "no AI training" -> "no AI training until Epic's EULA update announced 2026-10-29 (opt-in AI training on own projects) [marker #03-9]".
22. Key claims #29 (03.12): "keeps the 4 highest bone weights per vertex and normalises them" -> "keeps the 4 highest bone weights per vertex by default (configurable "Bone Influences") and normalises them [marker #03-12]".
23. Summary, Pipeline bullet (03.12): "Skinning is capped at 4 influences per vertex." -> "Skinning exports 4 influences per vertex by default (configurable) [marker #03-12]."

No item was UNVERIFIED, so no "(unverified in Step 2)" tags were added. The open-question lists in the report were left unchanged; their answers are in the section above.

## Sources

1. DBCLS BodyParts3D license page - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html
2. BodyParts3D LATEST README (4.0, update history) - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/README_e.html
3. BodyParts3D 2011 README (3.0, CC BY-SA 2.1 JP, 95%/99%) - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html
4. BodyParts3D download page - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html
5. BodyParts3D 4.0 IS-A parts list - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/isa_parts_list_e.txt
6. BodyParts3D 4.0 PART-OF parts list - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/partof_parts_list_e.txt
7. BodyParts3D 4.0 element lists - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/isa_element_parts.txt , https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/partof_element_parts.txt
8. BodyParts3D 3.0 parts list - https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/parts_list_e.txt
9. HuBMAP CCF 3D Reference Object Library - https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html
10. HRA LOD heart-male versions - https://lod.humanatlas.io/ref-organ/heart-male/ ; heart-female - https://lod.humanatlas.io/ref-organ/heart-female/
11. HRA heart-male v1.3 graph - https://lod.humanatlas.io/ref-organ/heart-male/v1.3/graph.jsonld
12. HRA heart-male v1.3 GLB - https://cdn.humanatlas.io/digital-objects/ref-organ/heart-male/v1.3/assets/3d-vh-m-heart.glb
13. TotalSegmentator README - https://raw.githubusercontent.com/wasserth/TotalSegmentator/master/README.md
14. TotalSegmentator LICENSE - https://raw.githubusercontent.com/wasserth/TotalSegmentator/master/LICENSE
15. TotalSegmentator on PyPI - https://pypi.org/project/TotalSegmentator/
16. Slicer forum, TotalSegmentator v2 (licensed tasks, snippet) - https://discourse.slicer.org/t/totalsegmentator-v2/32470
17. Zenodo TotalSegmentator dataset v2.0.1 - https://zenodo.org/records/10047292
18. Academic Torrents mirror of the v2 dataset - https://academictorrents.com/details/1dfeb3186514b40a2c212c21d494c665766bfbf4
19. Sketchfab API, Heart0102 - https://api.sketchfab.com/v3/models/6e3ddf0caa2640b39aa240f8c4ffc1ea
20. Sketchfab API, Human Heart Cardiac Bypass - https://api.sketchfab.com/v3/models/98dca43ff0c146b696148e6c3e70dbc0
21. Sketchfab API, #0084 and UMCG left dominance - https://api.sketchfab.com/v3/models/2cb7f280960e4419ba9f505ec0c82543 , https://api.sketchfab.com/v3/models/5c10cea34fd54b5eb9e3d0ecc8ab0da2
22. CU Anschutz OER Anatomy Hub - https://medschool.cuanschutz.edu/ms-modern-human-anatomy/student-resources/OERAnatomyHub
23. Epic forum, Upcoming changes to Quixel related to Fab's launch - https://forums.unrealengine.com/t/upcoming-changes-to-quixel-related-to-fabs-launch-in-october/2024362
24. Epic docs, Quixel Bridge plugin - https://dev.epicgames.com/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine
25. Epic docs, Fab licenses and pricing - https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab
26. CG Channel, Megascans free until end of 2024 - https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/
27. Sonniss GDC bundle license (v2.0) - https://sonniss.com/gdc-bundle-license/
28. Bedroom Producers Blog, Sonniss GDC 2026 bundle - https://bedroomproducersblog.com/2026/03/16/sonniss-gdc-2026-bundle/
29. CG Channel, MetaHuman 5.6 licensing - https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/
30. Digital Production, MetaHumans graduate - https://digitalproduction.com/2025/06/05/metahumans-graduate-ready-for-unity-godot-and-the-fab-cash-register/
31. Epic, UE devs can now choose to train AI models on their projects (2026-10-29; 403, snippet only) - https://www.unrealengine.com/ue-devs-can-now-choose-to-train-ai-models-on-their-projects
32. daily.dev summary of the Epic post (2026-10-30) - https://daily.dev/posts/ue-devs-can-now-choose-to-train-ai-models-on-their-projects-kqebavnzd
33. Game Developer, Epic is updating its EULA (2026-10-27) - https://www.gamedeveloper.com/programming/epic-is-updating-the-eula-to-allow-ai-training-on-outputs-from-unreal-engine-and-metahuman
34. Renderu, Epic will allow AI training (2026-10-28) - https://renderu.com/en/news/post/28756
35. Epic, UE pricing update ($1,850 seat) - https://www.unrealengine.com/en-US/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april
36. PocketGamer.biz, Netflix acquires Ready Player Me - https://www.pocketgamer.biz/netflix-acquires-avatar-creation-platform-ready-player-me/
37. Wikipedia, Ready Player Me - https://en.wikipedia.org/wiki/Ready_Player_Me
38. Blender Extensions, MPFB - https://extensions.blender.org/add-ons/mpfb/ ; versions - https://extensions.blender.org/add-ons/mpfb/versions/
39. MakeHuman license page - https://static.makehumancommunity.org/about/license.html
40. MakeHuman FAQ, license change 2020 - https://static.makehumancommunity.org/oldsite/faq/what_changed_regarding_the_license_in_2020.html
41. MPFB FAQ, can I sell models - https://static.makehumancommunity.org/mpfb/faq/can_i_sell_models.html
42. Blender 4.2 manual, glTF 2.0 add-on - https://docs.blender.org/manual/en/4.2/addons/import_export/scene_gltf2.html
43. glTF-Blender-IO exporter source - https://github.com/KhronosGroup/glTF-Blender-IO/blob/main/addons/io_scene_gltf2/__init__.py , https://github.com/KhronosGroup/glTF-Blender-IO/blob/main/addons/io_scene_gltf2/blender/exp/primitive_extract.py
44. Blender releases - https://www.blender.org/download/releases/
45. Poly Haven API - https://api.polyhaven.com/info/hospital_room , https://api.polyhaven.com/info/hospital_room_2
46. OpenStax Anatomy & Physiology 2e, 19.1 Heart Anatomy - https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy
47. Microsoft Rocketbox (archived 2026-10-02, MIT, 115 avatars) - https://github.com/microsoft/Microsoft-Rocketbox
48. Har-El, IEC 60601-1-8 subclause 6.3.3.1 - https://standards.har-el.com/Projects/181701/60601-1-8/html/A2SubCl-6-3-3-1-a-priority-encoded.htm
49. MSP Indy, audible alarms IEC 60601-1-8 - https://mspindy.com/technical-articles/using-audible-alarms-in-medical-equipment-iec-60601-1-8/
50. ImageCAS repository - https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT ; ImageCAS-X paper - https://arxiv.org/pdf/2608.30404
