# Research 03: Free 3D, 2D and audio assets, and their licenses

> **Purpose.** This is input for the plan's asset, art-pipeline and legal sections. It lists where to get anatomy, instruments, operating-room (OR) equipment, materials, sounds and characters for free. For each one it gives the **exact license**, whether personal or non-commercial use is allowed, and whether attribution or share-alike applies. It also describes a Blender pipeline and a license register (`ASSET_LICENSES.md`).
>
> **Status:** research only. Researched 2026-11-03.
>
> **Disclaimer:** this is not legal advice. Licenses can change, so re-check every asset page when you download it and record the date. **UNVERIFIED** means the license could not be confirmed from a primary page in this session. **(uncertain)** marks the author's estimate or a weak source.
>
> **Method:** Sketchfab model data (license, author, face count, downloadable flag) came from the public Sketchfab Data API (`https://api.sketchfab.com/v3/models/{uid}`) on 2026-11-03. Poly Haven and ambientCG holdings came from their public APIs (`api.polyhaven.com`, `ambientcg.com/api/v2`). Other facts are cited inline. The session's web-search budget ran out near the end, so a few items are left as UNVERIFIED rather than checked.

---

## 0. Summary for the plan

| Decision | Recommendation | Why (short) |
|---|---|---|
| **Base heart geometry** | **HRA (HuBMAP) 3D Reference Organ "Heart, Male" v1.3**: one GLB, 14 meshes, about 164k triangles. It has the 4 chambers, the septum, 4 valves and the papillary muscles as separate named parts. License: **CC BY 4.0**. | Its parts are already split and named, which suits interaction (cutting, highlighting, targeting). It is derived from the Visible Human, so the shapes come from a real body. CC BY is the least restrictive "real anatomy" license found. It has **no coronary arteries**, so they must be added. |
| **Surface detail and texture reference for the heart** | **Visible Heart Laboratories (Univ. of Minnesota) CC BY scans on Sketchfab**, such as "CAD Calcification: HH0581" (4.4M faces). Their **CC BY-NC** fresh human heart scans (#0614, #624, heart-lung bloc) can serve as **look reference**. | These are real donated human hearts. CC BY allows baking their detail onto the game mesh. The NC scans are fine for personal use but block any monetization. |
| **Coronary arteries, great vessels, thorax context** | **TotalSegmentator CT dataset** (CC BY 4.0, 1,228 CTs, 117 structures) gives heart, aorta, sternum and ribs 1–12. **Z-Anatomy / BodyParts3D** (CC BY-SA) gives vessels and nerves. Keep the BY-SA meshes as **separate files**. | These are the only redistributable sources with real thorax geometry. Share-alike is fine if those meshes stay separate and are shared under BY-SA. |
| **Instruments** | Model the **cardiac-specific instruments yourself** in Blender: sternal saw, Finochietto-type sternal retractor, aortic and venous cannulas, cardioplegia needle, vascular clamps. Use **CC BY** Sketchfab sets for generic instruments (Wenschel "Surgical instruments", lsirabella "Basic surgical instruments"). | No free, good-quality cardiac-specific instrument models were found. Self-made models have no license burden. |
| **OR room and equipment** | Kit-bash from CC BY models: operating table, surgical lights set, ventilator, ECG monitor, IV stand. Light the scene with the **Poly Haven CC0 HDRI "Surgery"** (16K). Use **ambientCG / Poly Haven CC0** materials for floor, walls, steel and fabric. The Charité photogrammetry OR is **CC BY-NC** and serves as layout reference. | CC0 and CC BY are safe to redistribute. |
| **Tissue materials** | No CC0 library has organ, flesh or blood textures (checked by API). Use **procedural Blender shaders** (Principled BSDF with random-walk subsurface scattering plus a wet coat) and **self-made photogrammetry of a butcher's pig heart**. Use licensed photos only as reference. | This avoids license problems, and a self-scanned pig heart belongs to you. |
| **Audio** | Prefer **Freesound CC0 / CC BY** (bone saw CC0, monitor beeps CC0, ER ambience CC0, ventilator CC0). **Synthesize** the monitor tones, alarms, electrocautery buzz and roller-pump sounds. | No free electrocautery or heart-lung-machine recordings were found. Synthesized tones can also follow the physiology model exactly. |
| **People** | **MPFB2 (MakeHuman for Blender)** for the patient and staff bodies (core assets and exports CC0). Use **Mixamo** for idle and gesture animations (free, but raw files must not be redistributed). MetaHuman is optional: since June 2025 it is no longer Unreal-only. | CC0 bodies have no attribution or share-alike burden. |
| **License hygiene** | Keep an **`ASSET_LICENSES.md` register** plus a per-asset sidecar file. **Do not commit third-party raw assets to a public git repo** unless their license allows redistribution. Never commit Sketchfab "Standard / Free Standard" assets, Mixamo raw files, MM-WHS data or restricted TotalSegmentator outputs. | A public GitHub repo counts as distribution. That triggers attribution, share-alike and non-commercial conditions, and it breaks "no standalone redistribution" terms. |

---

## 1. License primer: what matters even for a personal, non-commercial game

### 1.1 Licenses you will meet

| License (SPDX id where one exists) | Personal / non-commercial use | Commercial use | Attribution | Share-alike | Modify and share | Notes |
|---|---|---|---|---|---|---|
| **CC0 1.0** (`CC0-1.0`) | Yes | Yes | No (appreciated) | No | Yes | Poly Haven, ambientCG, Kenney, MakeHuman/MPFB core assets, some Freesound and NIH 3D items. |
| **Public domain (US Gov. work)** | Yes | Yes | Not required by copyright, but NLM terms ask for credit | No | Yes | Visible Human data falls under the NLM Terms & Conditions (§2.6). |
| **CC BY 4.0 / 3.0** (`CC-BY-4.0`, `CC-BY-3.0`) | Yes | Yes | **Yes**: title, author, source, license, and a note if modified | No | Yes | Most useful Sketchfab models, HRA organs, the TotalSegmentator dataset. |
| **CC BY-SA 4.0 / 2.1 JP** (`CC-BY-SA-4.0`, `CC-BY-SA-2.1-JP` **(uncertain SPDX id)**) | Yes | Yes | **Yes** | **Yes**: adapted material must be shared under the same license (or a compatible one) | Yes | Z-Anatomy, BodyParts3D, most Wikimedia Commons surgery photos. |
| **CC BY-NC 4.0 / 3.0** (`CC-BY-NC-4.0`) | **Yes** | **No** | **Yes** | No | Yes, non-commercially | Visible Heart Labs human hearts, Charité/Digital Surgery OR and instruments, several Freesound ambiences. |
| **CC BY-NC-SA 4.0** (`CC-BY-NC-SA-4.0`) | **Yes** | **No** | **Yes** | **Yes** | Yes, non-commercially, under the same license | eLearningUMCG and HannahNewey heart and coronary models. |
| **CC BY-ND / BY-NC-ND** | Yes, but only as is | ND: yes; NC-ND: no | Yes | n/a | **No modified versions may be shared** | Avoid these. Every game asset gets modified (decimated, retopologized, re-textured). |
| **Sketchfab "Standard" / "Free Standard"** (`LicenseRef-Sketchfab-Standard`) | Yes | Yes | Credit "in a comparable way" where others are credited | No | Use in derivatives is allowed, **but you may not make the asset available standalone or "in a way that lets others download or extract it"** ([Sketchfab licenses](https://sketchfab.com/licenses)) | Never commit these to a public repo. Even shipping them in an easy-to-extract build is risky **(uncertain)**. |
| **Mixamo terms** | Yes | Yes (royalty-free) | No | No | Use in projects is allowed; **raw character/animation files may not be redistributed**; no ML training ([Adobe Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html); [Adobe community licensing FAQ](https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/m-p/13234775)) | Never commit Mixamo FBX files to a public repo. |
| **Data-use agreements** (MM-WHS and similar) | Research use under the agreement | Usually no | Cite the papers | n/a | **No dissemination to third parties** ([MM-WHS page](https://zmiclab.github.io/zxh/0/mmwhs/)) | Meshes derived from this data probably count as "data" **(uncertain)**. Keep them private. |
| **Custom "educational use with reference"** | Yes | Unclear | Yes | n/a | Unclear | Atlas of Human Cardiac Anatomy (§2.5). Use as reference only. |

### 1.2 Where these conditions bite, even for personal use

1. **Sharing is what triggers CC conditions.** CC licenses put their conditions on *sharing*: copying, distributing, publicly displaying. If the game never leaves your PC, attribution, NC and SA are almost irrelevant. However, **pushing assets to a public GitHub repo, sending a build to a friend, posting on itch.io, or uploading gameplay videos all count as sharing.** The owner plans to "upload the plan to the repo", so the repo should hold **only the register and a download manifest, not third-party binaries**, unless every committed asset is CC0 / CC BY / CC BY-SA and correctly attributed.
2. **NonCommercial (NC).** The CC 4.0 definition is "not primarily intended for or directed towards commercial advantage or monetary compensation" ([CC BY-NC 4.0 legal code §1(i)](https://creativecommons.org/licenses/by-nc/4.0/legalcode)). A free, ad-free game is fine. **Things that may break NC:** selling the game, a paid itch.io page, in-game ads, a Patreon gating builds, a **monetized YouTube or Twitch video** of the game **(uncertain: courts and CC guidance are not settled on monetized videos)**, or use inside a company product or portfolio for paid work **(uncertain)**.
3. **ShareAlike (SA).** If you *share an adaptation*, such as a retopologized BodyParts3D heart, the adapted mesh must be released under BY-SA (or a later or compatible version). **The game's code does not have to become BY-SA.** SA applies to the adapted material, and a game that merely *contains* a separate BY-SA model is generally treated as a collection **(uncertain: no court ruling on games)**. Practical rule: **keep each SA asset in its own file and state its license.**
4. **SA plus NC-SA can conflict.** You **cannot merge** a CC BY-SA mesh (e.g. Z-Anatomy) and a CC BY-NC-SA mesh (e.g. eLearningUMCG) into **one** adapted mesh and share it. BY-SA requires the result to be BY-SA, and BY-NC-SA requires it to be BY-NC-SA. Keep them as separate objects, or use one of them only as reference.
5. **NoDerivatives (ND).** Decimation, retopology and re-texturing all create an adaptation. ND assets therefore cannot be shared in the game in modified form. **Reject ND assets.**
6. **Attribution must be specific.** For CC 4.0 that means title, author, source link, license link, and **whether you modified it** ([CC recommended practices for attribution](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution)). A credits screen plus a `CREDITS.md` satisfies the "reasonable manner" rule.
7. **Some sources require exact credit text.** BodyParts3D and the NLM require specific wording, and Digital Surgery asks for specific wording. These are quoted in §8.4.
8. **Trademarks and real products.** Remove manufacturer logos and names (e.g. Medtronic, Maquet, Stryker, Philips) from textures and UI. Copyright licenses do not cover trademarks, and logos would suggest endorsement. **Do not use fan-made models of other games' IP** (e.g. a "TF2 Medic bone saw" found on Sketchfab).
9. **AI-generated uploads.** Some Sketchfab "CC BY" models are output of AI generators. "Anesthesia Machine on a Medical Cart" by kkso199 says it was made with Meshy. Its provenance, and whether the uploader can grant CC BY at all, is unclear **(uncertain)**. Flag such assets in the register and prefer other sources.
10. **"No AI training" clauses** (Mixamo, MetaHuman, Sonniss 2024, Sketchfab NoAI tag) do not affect a normal game. They do forbid feeding these assets into generative-AI training.
11. **Ethics of human-derived data.** Visible Heart Labs hearts come from organ donors. Visible Human and CT datasets come from donors and patients. Use them respectfully (no gore exploitation), keep any donor history text out of the game, and never try to re-identify anyone. NIH 3D requires uploaders to de-identify data ([NIH 3D terms §3.1](https://3d.nih.gov/terms)).

---

## 2. Anatomy sources

### 2.1 BodyParts3D / Anatomography (DBCLS, Japan)

- **What:** whole-body polygon models with one OBJ file per organ. IDs follow the **Foundational Model of Anatomy (FMA)**, or BodyParts3D's own "BP" ids. A `conventional_part_of.txt` file gives the part-of hierarchy. Release 3.0 is from 2011-09-15. Downloads: `BodyParts3D_3.0_obj_95.zip` (521 MB, 95% reduction, 5× more triangles) and `BodyParts3D_3.0_obj_99.zip` (127 MB) ([README rel. 3.0](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html); FTP `ftp://ftp.biosciencedbc.jp/archive/bodyparts3d/`).
- **License:** **CC BY-SA 2.1 Japan** ([DBCLS license page](https://lifesciencedb.jp/bp3d/info/license/index.html); [README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20090209/README_e.html)). Derivatives must be distributed under the same license.
- **Personal use:** yes. **Commercial use:** allowed by the CC terms. **Attribution:** required, with exact text (§8.4). **SA:** yes.
- **Quality for us:** good topology for an atlas, but it is an *illustrative* adult male model built from CT and illustration, not a scan. It has no textures. The heart parts carry FMA naming. The 2011 data is old: meshes have small gaps and need cleaning. **Use Z-Anatomy's repaired version instead (§2.2).**

### 2.2 Z-Anatomy (Blender-based open atlas)

- **What:** a Blender *application template* (open via File > New > Z-Anatomy) containing a repaired, recolored and completed version of BodyParts3D with labels and definitions ([GitHub: Z-Anatomy/The-blend](https://github.com/Z-Anatomy/The-blend); [models repo](https://github.com/Z-Anatomy/Models-of-human-anatomy)). The Sketchfab previews are downloadable: "**Angiology**" is 4,065,857 faces, CC BY-SA ([sketchfab.com/3d-models/0caae8f894cc40b69f3f78adf14b9665](https://sketchfab.com/3d-models/0caae8f894cc40b69f3f78adf14b9665)), and "**Splanchnology**" is 2,016,305 faces, CC BY-SA ([5cfafb312f504815aa3fec55735607a6](https://sketchfab.com/3d-models/5cfafb312f504815aa3fec55735607a6)).
- **License:** "All the code and content shared by Z-Anatomy is under **CC BY-SA 4.0**" ([The-blend README](https://github.com/Z-Anatomy/The-blend)). **Exceptions inside the file:** "Anatomy of the Inner Ear" by University of Dundee is **CC BY-NC-SA 4.0**, and "Kidney" by Lissie Cowley is **CC BY-NC 4.0**. Neither is needed for heart surgery, but **delete them from any export.** The definitions come from Wikipedia (CC BY-SA 3.0). The separate add-ons repo reportedly lists GPL-3.0 in its metadata but CC BY-SA in its README ([ecosyste.ms index of Z-Anatomy/blender-addons](https://awesome.ecosyste.ms/projects/github.com%2Fz-anatomy%2Fblender-addons)); this is UNVERIFIED and does not matter because we only use the meshes.
- **Personal use:** yes. **Attribution:** required, with the text in §8.4 (both Z-Anatomy and BodyParts3D). **SA:** yes.
- **Use for us:** coronary arteries and veins, great vessels, phrenic nerves, ribs, costal cartilages, sternum and pectoral muscles, to give anatomical context around the heart. Keep these as **separate meshes under CC BY-SA**.

### 2.3 Human Reference Atlas (HRA, HuBMAP) 3D reference organs

- **What:** organ models made by Kristen Browne (NIAID) and others from the Visible Human Male and Female, released as GLB ([CCF 3D Reference Object Library](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html); [HRA construction paper, PMC11142047](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11142047/)). The library page lists heart female/male for v1.0 (Mar 2021), v1.1 (Dec 2021) and v1.2 (Jun 2022), in the [ccf-releases GitHub repo](https://github.com/hubmapconsortium/ccf-releases/tree/main/v1.2/models).
- **Newer version found:** `https://cdn.humanatlas.io/digital-objects/ref-organ/heart-male/v1.3/assets/3d-vh-m-heart.glb` (4.07 MB) was downloaded and inspected for this report. Probes for v1.4, v1.5 and v2.0 returned 404.
  - glTF 2.0, made with "babylon.js glTF exporter for Autodesk MAYA 2023.2". It has **18 nodes, 14 meshes, 164,119 triangles and 1 material**.
  - Named parts: `VH_M_heart`, `VH_M_heart_valve`, `VH_M_mitral_valve`, `VH_M_tricuspid_valve`, `VH_M_aortic_valve`, `VH_M_pulmonary_valve`, `VH_M_papillary_muscle_of_heart` (plus anterior, anterolateral, medial, posterior and posteromedial), `VH_M_cardiac_chamber`, `VH_M_left_cardiac_atrium`, `VH_M_right_cardiac_atrium`, `VH_M_heart_right_ventricle`, `VH_M_interventricular_septum`, `VH_M_heart_left_ventricle`.
  - **There are no coronary arteries, no pericardium, no epicardial fat and no great-vessel trunks beyond the valves** (from the node list).
- **License:** "All CCF 3D reference objects are released under **CC BY 4.0**" ([library page](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html)). The per-organ doc page shows a generic site footer reading "All Rights Reserved" ([heart-male v1.2 doc](https://hubmapconsortium.github.io/ccf-releases/v1.2/docs/ref-organs/heart-male.html)). Treat the library statement as authoritative, and assume v1.3 has the same license **(uncertain until confirmed on humanatlas.io)**.
- **Attribution:** cite the release, e.g. "Browne K, Schlehlein H, Herr II BW, Quardokus E, Bueckle A, Börner K (2022). HuBMAP CCF 3D Reference Object Library v1.2", plus a link and the license. The data comes from the Visible Human, so also add "Courtesy of the U.S. National Library of Medicine" **(uncertain whether this is required; it costs nothing to add)**.
- **Use for us:** **the recommended base heart**, because the parts are already separated and named. Add coronaries, fat, pericardium and vessel stubs yourself.

### 2.4 NIH 3D (formerly NIH 3D Print Exchange)

- **What:** a US government repository of biomedical 3D models, including a **Heart Library** of "clinically accurate heart models developed with Jump Simulation", made from patient MRI with a congenital heart disease focus ([Heart Library](https://3d.nih.gov/collections/heart-library)).
- **License:** **set per entry by the uploader.** "NIH 3D does not enforce license terms on behalf of contributors… Visitors… must review and comply with the licensing terms associated with each file" ([NIH 3D Terms §4.3](https://3d.nih.gov/terms)). The terms name no default license.
- **Heart entries checked:**

| Entry | What | License | Commercial? |
|---|---|---|---|
| [3DPX-022787](https://3d.nih.gov/entries/3DPX-022787) | "Human Heart 3d Model" (Sourav Pan / Biology Notes Online) | **Public Domain (CC0 1.0)** | Yes |
| [3DPX-001549](https://3d.nih.gov/entries/3DPX-001549/2) | "1a_Cardiovascular disease": left heart plus clear outer contour (3DPrintForHealth) | **CC0 1.0** | Yes |
| [3DPX-000900](https://3d.nih.gov/entries/3DPX-000900/2) | "Heart (CT)", a CAD heart from CT (printhuman.org) | **CC BY-NC 4.0** | No |
| [3DPX-000452](https://3d.nih.gov/entries/3DPX-000452/2) | Semilunar valve CAD model (Chris Leggett) | **CC BY-NC 4.0** | No |
| Heart Library (Jump Simulation) entries | Congenital hearts from MRI | **UNVERIFIED** (license filter exists; not checked per entry) | ? |

- **Use for us:** mostly 3D-print-oriented blood-pool or shell meshes without textures. They are useful for **pathology variants in later versions** (congenital). Check every entry's license field.

### 2.5 Open Anatomy Project and the Atlas of Human Cardiac Anatomy

- **Open Anatomy Project** (Surgical Planning Lab, Brigham and Women's Hospital) offers six atlases, including the **"Mauritanian Anatomy Laboratory Thoracic Atlas"**, viewed in the web-based Open Anatomy Browser ([openanatomy.org](https://www.openanatomy.org/)). **License: UNVERIFIED.** The site does not state one on its front page. Check each atlas's download page before use. No dedicated heart atlas is listed.
- **Atlas of Human Cardiac Anatomy** (Visible Heart Lab, Univ. of Minnesota, [vhlab.umn.edu/atlas](http://www.vhlab.umn.edu/atlas/index.shtml)) has beating-heart videos, plastinated specimens and endoscopic views. It is **not Creative Commons, but "free to use for educational purposes with adequate reference"** ([AnatomyTOOL listing](https://anatomytool.org/node/59585); **(uncertain)**, secondary source). **Use as visual reference only**, which is excellent for valve motion and endocardial color.

### 2.6 Visible Human Project (NLM)

- **Terms:** since **July 2019** the NLM Data License "has been replaced by Terms and Conditions". No registration is needed for the FTP data ([NLM getting data](https://www.nlm.nih.gov/research/visible/getting_data.html)). General NLM terms: no fees or royalties; republishers must keep data current or say it may not be current; **do not imply NLM endorsement**; credit "**Courtesy of the U.S. National Library of Medicine**" ([NLM Terms and Conditions](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html)). These general terms do not name the Visible Human specifically, so their application to it is **(uncertain)**.
- **Data:** male CT 512×512, 12-bit, 1 mm; male cryosection colour 2048×1216, 24-bit, 1 mm; 70 mm film scans 4096×2700 (1,871 images); female cryosection at 0.33 mm (over 5,000 images). PNG versions are recommended ([NLM](https://www.nlm.nih.gov/research/visible/getting_data.html)). Mirror: `data.lhncbc.nlm.nih.gov/public/Visible-Human/`. Also on the [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/collections/nlm_visible_human_project).
- **Use for us:** (a) the source of the HRA heart; (b) cryosection colour slices as **tissue colour reference**. Frozen cadaver tissue is darker and browner than living perfused tissue, so adjust by eye **(uncertain)**.

### 2.7 Visible Korean (Ajou University / KISTI)

- Serially sectioned real-colour images of 4 cadavers (male and female whole body, a male head, a female pelvis). Sectioned images, volume models and surface models are said to be **downloadable free** from the Visible Korean homepage (anatomy.co.kr) and an Ajou mirror ([J. Morphology article](https://j-morphology.com/1026-3543/article/view/103353); [Ajou anatomy site](https://sites.google.com/ajou.ac.kr/anatomy/홈)). **License / terms: UNVERIFIED.** No license text was found. Treat it as **reference only** until confirmed.

### 2.8 Embodi3D

- A community library of CT-derived STL files, including cardiac ones. Its terms page returned HTTP 403 to automated fetch. **License: UNVERIFIED**, probably per-upload and account-gated. Low priority: these are 3D-print STLs with no texture or part separation.

### 2.9 Sketchfab: heart, thorax and related anatomy (verified via API, 2026-11-03)

All of the models below are **downloadable**. "Faces" is Sketchfab's triangle count. Link format: `https://sketchfab.com/3d-models/<uid>`.

**A. CC BY 4.0 (safe to modify and share with attribution)**

| Model (uid) | Author | Faces | Notes |
|---|---|---|---|
| **CAD Calcification: HH0581** (`5396e668d3fc47bdb413041d518bd148`) | Visible Heart Laboratories (@VisibleHeartLabs) | 4,443,134 | **A real donated whole human heart** (63-year-old male, coronary disease). It is the best CC BY high-poly source to bake surface detail from. It is a diseased heart, so smooth out the calcified areas. |
| Heart0103 (`3c80c374f4a2419e9bf921bd2b64019b`) | VisibleHeartLabs | 3,363,798 | A real heart, but **pathological** (cardiomegaly, 853 g, atrial septal defect). Use for reference or a "difficult case". |
| HH0613-LAD (`9efb7a3aa6114b34961e651984bf0fae`) | VisibleHeartLabs | 220,424 | Stented LAD with calcium. Good reference for coronary disease. |
| HH229 Long Axis (`41f9608657fb4513a95b4f7b9261caa6`) | VisibleHeartLabs | 1,087,608 | Heart cut in the TEE mid-esophageal long-axis plane, showing the LV, LVOT, aortic and mitral valves. |
| Plastinated Black Bear Heart with Pericardium (`4debdb5ef91e43b3b196384d90f7f427`) | VisibleHeartLabs | 1,461,570 | An animal heart, but **the only CC BY model found with the pericardium attached**. Reference for pericardium look. |
| Porcine Heart Anatomical Plane #0001 (`7adfb01b1ed843af88bf7d2c8d8e051c`); Whole Cow Heart Fixed (`c49f873ba4be4193b880bdf624957dc4`) | VisibleHeartLabs | 600,000; 400,000 | Animal hearts. The porcine one is useful because pig hearts are common surgical training specimens. |
| Human Heart Base (`fa8eba4530a84f758ac50df3b4e168f0`) | APIL (@apil_tgh) | 38,358 | The fibrous skeleton and valve annuli from **cardiac-gated CT**. Useful for valve-surgery versions. |
| 2017000 Normal Heart. Aortic Dissection (`590c475c23594687abfed8075a36c8ec`) | APIL | 241,340 | CT blood-pool model (ITK-SNAP, Meshmixer, Blender). |
| Bicuspid Aortic Valve (`d3fda2a0b8d24a04b7bc4ce2d7827480`) | APIL | 127,264 | Pathology variant for an AVR level. |
| Realistic Human Heart (`3f8072336ce94d18b3d0d055a1ece089`) | neshallads | 22,562 | Artist-made, textured, game-ready. The most-liked heart (1,684 likes). Artistic, not scan-accurate. |
| Human heart, realistic anatomical model (`adb2c91ec8194b24b7ba431aa573a906`) | TinkerLane Studio | 20,370 | Artist-made, low-poly. |
| Human Heart (`87daa30ece974806872510fbff55c6aa`) | Balsamic_Vin | 182,174 | Artist-made (2025). |
| Human Heart (`56a4167d77a84ff9b45d6d2459b5a49e`) | bcxrlab | 71,112 | Artist-made (2026). |
| Human heart (`94505ec969cf468684d4393a3de99478`) | thunk3d.scanner | 1,120,776 | A handheld-scanner demo, probably a scan of a **plastic teaching model** **(uncertain)**. |
| Beating-heart (`d9845afb1ee64ad094adc96320c67d98`) | jalmer | 34,401, **1 animation** | A **re-upload** of "Beating Heart" by *Dreamwasabducted* ([skfb.ly/owVVo](https://skfb.ly/owVVo), CC BY). **Credit both.** Reference for a heartbeat blend-shape setup. |
| **Human Thorax** (`4aba9b2ced344bdf8f09656c6a298b50`) | Medulla (@thunderpig) | 1,690,040 | Ribs, vertebrae, discs and **costal cartilages** (bone cream, cartilage blue). Annotated. |
| **Thorax** (`c918b12c4e0c4625a5ad0392bb7d0354`) | valchanov | 2,223,386 | Made from a **2 mm CT scan**. |
| Thoracic Cage (`8e467073d7f149d0a92a712a62326447`) | Ualde (@sebaualde) | 823,492 | |
| **Sternum** (`394e7d34bf8a4614be125d90fa11e87e`) | UNCG Imaging Lab | 500,000 | A NextEngine scan of a **real human sternum** from the UNCG anthropology collection. Good for the sternotomy cut surface. |
| Sternum (`86ef7a1a71734e01b6b7443bff3364f5`) | OSU.Multimedia | 130,312 | |
| Realistic Human Lungs (`ce09f4099a68467880f46e61eb9a3531`) | neshallads | 63,974 | Artist-made, textured. Lungs are visible at the edges of the sternotomy. |

**B. CC BY-SA 4.0**: Z-Anatomy "Angiology" and "Splanchnology" (see §2.2).

**C. CC BY-NC 4.0 (personal use OK; no monetization; attribution required)**

| Model (uid) | Author | Faces | Notes |
|---|---|---|---|
| **Fresh Human Heart #0614** (`4dc368be96ad430684c0a6ded4247e08`) | VisibleHeartLabs | 300,000 | **A fresh (unfixed) human heart: the best colour reference for living-like tissue.** |
| Fresh Heart/Lung Bloc Semi-inflated (`b6a26cab3817459cbfd96945db2368bb`) | VisibleHeartLabs | 490,212 | The heart in context with the lungs. |
| Fresh Human Heart Donation #624 (`cde2a463da334dbeae73dae6911b7d7b`), #622 (`b6e15c4e95714a44ada711db1fd0612c`), Fresh Human Heart Organ Donation (`5a155b24cc79436c8996c7249e585d6f`) | VisibleHeartLabs | 400k–500k | More fresh hearts. |
| Combined Coronary Vasculature Model – Heart0256 (`00026209fef646cb893249b1ef8729c4`) | VisibleHeartLabs | 789,720 | **A real coronary tree cast/scan.** The best coronary reference found. |
| Heart0064 / Heart0126 / Heart0088 Coronary Arteries (`ee2badfb73e14d00b5453351a582d2b1`, `1b7c839f7d4f4c8ab2bfe8bdde418575`, `aaf0f303f62a4c529ae7df3978d36337`) | VisibleHeartLabs | 177k–290k | Coronary variants. |
| Plastinated Heart0137 Classic Valve View (`a82aea949e4b470f888dd43983ed83cf`) | VisibleHeartLabs | 850,000 | View of the valves from above. |
| Surgical / Charité models | see §3 | | |

**D. CC BY-NC-SA 4.0 (personal use OK; no monetization; share-alike)**

| Model (uid) | Author | Faces | Notes |
|---|---|---|---|
| Anatomical heart – codominance / left dominance / right dominance (`42d07ac1517748ea82bb05b0a362b298`, `5c10cea34fd54b5eb9e3d0ecc8ab0da2`, `89ad76f1e61847e6b4b0af215bb237dc`) | eLearningUMCG (Univ. Medical Center Groningen) | 157k–186k | **Clean, labelled coronary dominance variants.** Ideal for teaching overlays. |
| Human anatomy: heart in thorax (`22ebd4abce9440639563807e72e5f8d1`); Healthy heart and lungs (`5c62cd4d4ba04243be1062d2263d3ef0`); Thoracic & abdominal skeleton based on CT (`a423ea77377f41438d017e108e060d5e`) | eLearningUMCG | 155k–372k | |
| Cardiac Anatomy: External view (`a3f0ea2030214a6bbaa97e7357eebd58`); Coronary arteries of the heart (`00b5f4ec0b984325b453f8df07cd0cb5`) | HannahNewey | 3.0M; 2.75M | High-poly illustrative heart and coronaries. |

**Avoid:** "Abdomen Anatomy" and other eLearningUMCG items under **CC BY-NC-ND**, because ND forbids sharing modified versions.

### 2.10 Segmentation datasets (CT/MRI → meshes)

| Dataset | Content | License / access | Use for us |
|---|---|---|---|
| **TotalSegmentator dataset v2.0.1** ([Zenodo 10047292](https://zenodo.org/records/10047292)) | **1,228 CT images, 117 structures**, 23.6 GB. A 102-subject subset exists. | **CC BY 4.0** (Zenodo record). Cite the paper. | **Best redistributable real-patient source.** Classes include heart (one label in `total`), aorta, **sternum, ribs 1–12 L/R**, lungs and vertebrae. Pick a typical adult and build the thorax around the HRA heart at true scale. |
| **TotalSegmentator tool** ([GitHub](https://github.com/wasserth/TotalSegmentator)) | Segments new CTs. | Code and open tasks: **Apache-2.0**. **`heartchambers_highres`** (myocardium, LA, LV, RA, RV, aorta, pulmonary artery) and **`coronary_arteries`** (and `aortic_sinuses`) need a license. Licenses are **free for non-commercial use** via the [academic license form](https://backend.totalsegmentator.com/license-academic/); commercial use needs a paid license. `brain_aneurysm` is CC BY-NC 4.0. | Run `heartchambers_highres` and `coronary_arteries` on **CC BY CT data** (e.g. the TotalSegmentator dataset itself) to get chambers and coronaries. Under the free license, **outputs are for non-commercial use** **(uncertain whether output meshes inherit the restriction; assume they do)**. |
| **MM-WHS 2017** ([page](https://zmiclab.github.io/zxh/0/mmwhs/); [paper, PMC6839613](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6839613/)) | 120 cardiac images (60 CT, 60 MRI per the paper), whole-heart labels. The 7 substructures are LV and RV blood cavities, LA, RA, LV myocardium, ascending aorta and pulmonary artery **(substructure list from memory of the paper; uncertain)**. | **Signed data-access agreement; "commit to not disseminate the Data to any third party"**. No CC license. | Private reference or training only. **Never commit derived meshes.** |
| **ImageCHD** ([arXiv 2101.10799](https://arxiv.org/abs/2101.10799)) | 110 CT, 16 congenital types, 7-substructure labels, ages 1 month to 40 years. | **UNVERIFIED** (released to the public per the paper; terms not found). | Congenital variants for much later versions. Low priority for adult CABG/AVR. |
| ASOCA (coronary CTA), ImageCAS (about 1,000 coronary CTAs), Medical Segmentation Decathlon Task02 (LA MRI), HVSMR | Coronary and cardiac labels | **UNVERIFIED** in this session. MSD is believed to be CC BY-SA 4.0 **(uncertain)**. | Candidates for a better coronary tree. Verify before use. |

**Tooling to turn segmentations into meshes:** see §7.1 (3D Slicer + TotalSegmentator extension, Bioxel Nodes).

### 2.11 Recommended anatomy stack (v1, on-pump CABG)

1. **Heart:** HRA v1.3 male heart (CC BY) → retopologize → bake detail from HH0581 (CC BY) → add hand-modelled **coronaries** (LAD, diagonals, circumflex/OM, RCA/PDA), traced from a TotalSegmentator `coronary_arteries` output (non-commercial license) or Z-Anatomy vessels (BY-SA, kept separate) → add **epicardial fat**, **pericardium** and the **aortic root, ascending aorta, SVC/IVC and right atrial appendage** for cannulation.
2. **Thorax:** sternum (UNCG scan, CC BY) and ribs/costal cartilage (thunderpig Human Thorax, CC BY), fitted to a TotalSegmentator CT case (CC BY) for true proportions.
3. **Conduits:** LIMA and saphenous vein are hand-modelled. Use Z-Anatomy as reference for the course of the LIMA.
4. **Look reference:** VisibleHeartLabs fresh hearts (BY-NC), eLearningUMCG coronary variants (BY-NC-SA), Atlas of Human Cardiac Anatomy (reference only).

---

## 3. Surgical instruments and OR equipment

### 3.1 Sketchfab (verified via API, 2026-11-03)

**CC BY 4.0 (safe to modify and share with attribution)**

| Item | Model (uid) | Author | Faces | Notes |
|---|---|---|---|---|
| **General instrument set** | Surgical instruments (`bd0ad0180f5148f1b3b331b8ebe6e494`) | Wenschel | 1,202,202 | Soft- and hard-tissue scalpels, scissors, **clamps, needle holders, needles**, kidney tray, tissue hook. High-poly, so decimate it. |
| Basic surgical instruments | (`fde4da61ef8041688ae6a7a792260d15`) | lsirabella | 38,652 | **Molt periosteal elevator, arterial forceps, Tilley forceps, tissue forceps, Lane tissue forceps** (2026-08). |
| Medical forceps | (`46e4d6704bcb42d0a0ea907275e3c780`) | Fhay.Alonso | 31,850 | Close-up quality. |
| Needle holder | Surgical_needle Holder (`24864e4443df42f5b1439eea4631f136`) | Mmmighty_Atom | 9,668 | |
| Scissors and pincette | VR Surgical Tool Set (`c61f5a8aa3c14ec192428de4b1ad9c42`) | vaulted.dev | 15,460 | 3 scissors, a pincette, a syringe. Made for VR. |
| Mixed instruments | SURGICAL INSTRUMENT (`2971a44d334b45ff926792e92a6bcee7`) | ferofluid | 11,726 | Low-poly. |
| Retractor (generic) | Retractor V1 (`39b64baa59fd4acfb8adf68fec0186de`) | Judith Solomon (@miraclejudy3) | 38,438 | Made for a C-section VR sim. **Not a sternal retractor.** |
| Scalpels | Pair of Scalpels (`219198b5a6a34f87bdc417e2706f9482`); Scalpel (`e932802ea2144a0ea8f4d694c0eaf21d`) | sousinho; Medickz | 2,696; 1,870 | |
| **Heart-lung machine** | Heartlung Machine (`34f7d192bd8d4ca498b5e3d4948101ba`) | Kevin Gille | 8,635 | **The only one found.** A 2-day test piece from 2016, low detail. Use for blockout and remodel it. |
| **OR table** | Operating Table (`e3a4512227d34b098e2ef0d11c8a80fd`); Operating Table, High Poly (`dddfd66649b74288a4e538b19931586b`) | shashkinv1ad | 46,400; 1,157,494 | 800 likes. A good base. |
| **OR table, surgical lights, console, cart** | Realistic Medical Equipment and Accessories Set (`5460fb2767c6468eb88466d2555d273b`) | daonware | 70,937 | **Dual-arm surgical lights** plus an operating table, equipment console and utility cart. |
| Whole OR | Hospital operating room (`a27400a73f4a43fbb1dda30031cb91c2`) | Chenchanchong | 823,652 | Uploaded 2025-10. Quality not inspected **(uncertain)**. |
| Patient monitor | ECG Monitor (`47e72cd57f45414aa82e41342b299b5b`); Patient Monitor (`80db1fb4584d4feea54936ea640d00db`) | demagdev; Ram-je | 14,648; 156,478 | Replace the screen with a live render texture from the physiology model. |
| Ventilator | Medical Ventilator (`a03a99fab9314aab96fd41ec69acf1a3`); Medical Ventilation Vivo45 (`de83480754c8450992bdeae4dae2f187`) | lazarys; 7634hosi | 66,944; 106,926 | Stand-in for the anesthesia machine's ventilator. |
| IV stand and pump | Iv drip stand (`b503f5749e5841139f3bdd0bec20a7a6`); IV Device with stand (`dae36203625e414db3b0c8fff858f830`); Infusion Pump Module (`704c85be562f43598ddb0194b0c7442a`) | saba.nazir; UofA-CDH; Bambiblitzkrieg | 12,822; 144,711; 577,260 | |
| Trolley | Medical Props (`4b2e1a4c3f13432b9a0bc15355b27632`) | coa white | 102,126 | Three-tier surgical cart. |
| Mixed hospital props | Hospital Stuff (`96fb858918b14dfd94edd7cdad55333e`) | Mina.M | 1,667,332 | Beds, trolley, light, syringe and more. **Includes a "DeadBody" prop, so leave it out.** |
| Gloves and masks | Realistic Surgical Glove with Folds (`38ab320219b647b19c77dfbc66c6e43a`); surgical mask (`9a0166cd649a4d76bde85fc0ae755dfa`) | Jingfu Chen; samuelsurovic | 13,232; 19,900 | |
| Defibrillator | UK Automated External Defibrillator (`997cdb42217f4ef78b65e18e7e506e78`) | jacobwarrenlee | 3,646 | This is an AED. An OR defibrillator with **internal paddles** must be modelled by hand. |
| **Anesthesia machine** | Anesthesia Machine on a Medical Cart (`6b28fafc23244ef9a47e84dbde09b5a4`) | kkso199 | 793,091 | **AI-generated (Meshy)**, so its provenance is unclear (§1.2.9). Prefer modelling your own. |

**CC0**

| Item | Model (uid) | Author | Notes |
|---|---|---|---|
| Historical saw | Amputation Saw (`77f31b529c724b2c8c6dfd9ccf30d79e`) | Science Museum Group | About 500 years old. **Not** a modern sternal saw; museum or Easter-egg use only. |

**CC BY-NC 4.0 (personal use OK, no monetization). The highest-quality OR content found.** Requested credit (from the model pages): "Christopher Remde, Moritz Queisner, 2024, Experimental Surgery, Charité Universitätsmedizin Berlin & NMY Mixed-Reality Communication GmbH" for the instruments, and the same without NMY for the instrument tables.

| Item | Model (uid) | Author | Faces | Notes |
|---|---|---|---|---|
| **Surgical Instruments collection** | `46f5799ca36240efae3abec6e61d4c8a` | Digital Surgery (@digitalsurgery) | 614,712 | "Accurately modelled" by NMY, annotated. |
| Surgical / Instrument table collection | `a1fcfeab1ad646638089655e8b6f0e2b` | Digital Surgery | 36,181 | Photogrammetry of real back tables. |
| **Charité OR (photogrammetry)** | `9ec46c4d615a4581a235eebfb162f574` (also `fa63aa330e1048a7ab7e63a54845c6c3`) | ChrisRE / Digital Surgery | 334,808 | A real general OR at Charité Campus Mitte (2018, 500 photos). **Cite:** Queisner M, et al. *VolumetricOR…* Surg Innov 2022;29(3):406–415, [PMID 35137646](https://pubmed.ncbi.nlm.nih.gov/35137646/). |
| Body dummy prepped for surgical training | `d9bc38002292411d8437447f331dcf2f` | Digital Surgery | 32,660 | Draping and prep reference. |
| Surgical Light | `53a5881441f94e4d8c7b6464d6f13c72` | barbodoji | 39,516 | |

**Sketchfab "Free Standard" (no redistribution of the asset itself):** "anesthesia machine" by aman7830 (`c6aa260bc9f544108eb2761f321ca86b`, 47,098 faces) and "patient monitor" by inth04 (`81cfd6dd75a5401885614100e855bc93`). These are usable in the built game, but **never commit them to a public repo** ([Sketchfab licenses](https://sketchfab.com/licenses)).

### 3.2 Gaps: model these yourself (no free asset found)

Searches on Sketchfab for "finochietto", "rib spreader", "sternal saw", "bone saw", "cannula", "electrocautery", "hemostat" and "surgical stapler" found nothing suitable. Model these from catalogue photos and published dimensions. Self-made models carry no license burden, but **do not copy manufacturer logos or names**:

- **Sternal saw** (oscillating or reciprocating, with a guard/foot plate)
- **Sternal retractor** (Finochietto-type rack-and-pinion; consider a mammary retractor for LIMA harvest)
- **Arterial cannula** (aortic), **venous cannula** (two-stage), **cardioplegia cannula**, **vent**, **pump suckers**
- **Aortic cross-clamp** and side-biting clamp, **bulldog clamps**, **coronary scissors (Potts)**, **coronary probes**, **Castroviejo needle holder**, **DeBakey forceps**
- **Electrocautery pencil** (and its holster), **Yankauer suction**
- **Internal defibrillator paddles**, **temporary pacing wires and box**, **chest tubes**, **sternal wires**, **bone wax**
- **Heart-lung machine** in detail (roller-pump heads, oxygenator, reservoir, heater-cooler lines, console screen); the Kevin Gille model is a blockout base only
- **Anesthesia workstation**

**Optional photogrammetry:** scan real instruments (borrowed or cheap student sets) with Meshroom (AliceVision, **MPL-2.0** **(uncertain, not re-checked)**). The scans belong to you.

### 3.3 CC0 libraries: Poly Haven, ambientCG, Kenney

| Library | License (verified) | Relevant holdings (API, 2026-11-03) |
|---|---|---|
| **Poly Haven** | **CC0**: "You do not need to give credit or attribution…". It may be used for any purpose, including commercial ([polyhaven.com/license](https://polyhaven.com/license)). Logos, renders and site text are not CC0. | **HDRIs:** **"Surgery"** (`surgery`, Oliksiy Yakovlyev, **17000×8500 px**, tags: bed, table, hospital, lamp, operation); "Hospital Room" (`hospital_room`, 17000×8500); "Hospital Room 2" (`hospital_room_2`, Dimitrios Savva / Jarod Guest, **20480×10240**, 2024); "Children's Hospital"; "White Studio 01–06"; "Studio Small 01–09". **Textures (869 total):** 43 fabric (for drapes and gowns, re-coloured to surgical blue/green), metal plates, 127 tile and floor sets, 3 rubber. **No flesh, skin, meat or blood textures** (0 API hits). **Models (521):** mostly generic props (clipboard, cleaner bottles, drawer cabinet, desk lamp). |
| **ambientCG** | **CC0 1.0**. Credit is optional; suggested text: "Created using <asset> from ambientCG.com, licensed under CC0 1.0" ([docs.ambientcg.com/license](https://docs.ambientcg.com/license/)). | Fabric 106, Metal 214, Tiles 222, Plastic 28, Rubber 4, Leather 50 materials. **No meat, flesh, blood or fat** (0 hits; "skin" only finds Leather008). Use for the OR floor (vinyl or tiles), stainless steel (instrument trays, table), drapes and plastics. |
| **Kenney** | **CC0**. "Attribution is not required". Do not use the Kenney logo ([kenney.nl/support](https://kenney.nl/support)). | Mostly **stylized, low-poly** packs. Useful for **UI icons and prototyping** only, not for realism. |

**Not recommended unless needed:** Fab / Quixel Megascans uses the **Fab Standard License** (no standalone redistribution; full EULA UNVERIFIED). A Fab listing "CC0 – Raw Meat 4" by *plaggy* claims CC0 4K PBR ([fab.com listing](https://fab.com/listings/7ae3d759-a963-43e4-855d-ce034d489d77)), but this is **UNVERIFIED**. Textures.com: license page not retrievable, **UNVERIFIED**. AITextured uses its own "Free Commercial License" v1.1, not CC0 (**UNVERIFIED**).

---

## 4. Textures and materials for tissue, and photo references

### 4.1 What exists

- **CC0 libraries have no usable tissue textures** (§3.3: zero API hits for meat, flesh, skin, blood or fat in Poly Haven and ambientCG).
- **Paid or unclear-license meat textures** exist on CGTrader, Superhive and RenderHub (e.g. CGHawk minced-meat PBR, US$19.99). They are not needed.
- **Skin:** MakeHuman/MPFB2 skin textures are core assets under **CC0** ([MakeHuman license](https://static.makehumancommunity.org/about/license.html)). The CC BY scanned "Male surgical doctor" (deep3dstudio) shows real skin at a distance.

### 4.2 Recommended approach (no license risk)

1. **Procedural shaders in Blender** (Principled BSDF), then **bake** them to texture maps for the engine.
   - Tissue: Subsurface on with **Random Walk** (the Blender-recommended mode for organic materials, [Blender manual: SSS](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/sss.html)), red-biased radius, and a **wet coat layer** (Coat weight high, low coat roughness).
   - Use Noise and Voronoi textures for fibre direction and fat lobules. Use a curvature/AO bake for crevices.
2. **Self-made photogrammetry of a butcher's pig heart and a rack of ribs** (cheap, legal, and the result is your own copyright). Porcine hearts are widely used as cardiac surgery training models.
   - Capture under cross-polarized light to remove specular highlights from the albedo.
   - Bake to the game topology.
   - Re-tint toward human colour using the references in §4.3.
3. **Hand paint** in Blender Texture Paint over the baked base. Free alternatives such as Material Maker (MIT **(uncertain)**) or ArmorPaint (source available; binaries paid **(uncertain)**) are UNVERIFIED in this session.

**Starting values (uncertain; artistic estimates to tune against references, not measured optical data):**

| Material | Base colour (sRGB hex) | Roughness | SSS | Coat | Notes |
|---|---|---|---|---|---|
| Myocardium / epicardium where there is no fat | #7A2622 – #9E3A33 | 0.35 (under the coat) | weight 0.3–0.5; radius (1.0, 0.25, 0.12); scale 0.004–0.008 m | 0.8–1.0, roughness 0.05–0.15 | The visible surface is glossy and wet. |
| Epicardial fat (along the grooves and coronaries) | #D8B256 – #E6C779 | 0.4 | weight 0.6; radius (1.0, 0.8, 0.4) | 0.7 | Covers the LAD and RCA, which the surgeon must dissect through. |
| Pericardium (cut edges) | #D9C4B8, semi-translucent | 0.3 | weight 0.5 | 1.0 | Thin, whitish, shiny. |
| Arterial blood (fresh) | #8E0B0B – #A31212 | 0.05 | – (opaque) | 1.0 | Pools and films. Use a decal/flow system. |
| Venous / old blood | #4A0606 – #5E0A0A | 0.1–0.3 as it dries | – | 0.5 | |
| Cut sternum (cancellous bone) | #8A3A2A with #E8D9C0 cortex rim | 0.6 | low | 0.3 | Add a bone-wax waxy beige patch material. |
| Skin (prepped with povidone-iodine) | Base skin multiplied by orange-brown #9A5A1E | 0.45 | weight 0.3, radius (1.0, 0.2, 0.1) | 0 | The prep stain is a realism cue. |

### 4.3 Photo references (look, don't copy)

Looking at photos to paint your own textures is generally fine. **Projecting, tracing or cloning a photo into a texture makes the texture a derivative**, so then that photo's license applies **(not legal advice)**.

| Source | License | Notes |
|---|---|---|
| Wikimedia Commons [Category:Cardiac surgery](https://commons.wikimedia.org/wiki/Category:Cardiac_surgery) (62 files plus 10 subcategories) and [Category:Cardiopulmonary bypass](https://commons.wikimedia.org/wiki/Category:Cardiopulmonary_bypass) (36 items) | **Per file**, mostly CC BY-SA. Verified: "[Cardiac surgery operating room.jpg](https://commons.wikimedia.org/wiki/File:Cardiac_surgery_operating_room.jpg)" (Pfree2014, **CC BY-SA 4.0**, 1237×705) and "[Heart lung machine connected to patient.jpg](https://commons.wikimedia.org/wiki/File:Heart_lung_machine_connected_to_patient.jpg)" (Pfree2014, **CC BY-SA 4.0**, 1238×772) | Intraoperative series: "Abriendo Pericardio", "Corazón Humano preparado para canular", "Estabilizador Octopus…", and a 3-step sternotomy series (Russian titles: "Стернотомия…"). The licenses of these were **not checked** (API rate-limited). |
| VisibleHeartLabs fresh-heart scans (Sketchfab, CC BY-NC) | CC BY-NC 4.0 | The best 3D colour reference. |
| Atlas of Human Cardiac Anatomy (UMN) | Educational use with reference **(uncertain)** | Videos of beating valves. |
| Visible Human cryosections | NLM terms | Cadaver colour, which needs correcting (see §2.6). |
| CTSNet / YouTube surgical videos | Proprietary, viewing only (**UNVERIFIED** terms) | Watch them for motion, bleeding and wetness. **Never** extract frames into assets. |

---

## 5. Audio

### 5.1 Freesound licenses

Freesound uses **CC0**, **CC BY 4.0** and **CC BY-NC 4.0** for new uploads. Older sounds can be **CC BY 3.0 / CC BY-NC 3.0** or the retired **Sampling+ 1.0** ("similar to BY-NC" and also bans advertising) ([Freesound FAQ](https://freesound.org/help/faq/)). Credit each sound with its name, author, link and license. For many sounds, link a credits page. Freesound's **attribution list** (your download history) helps build it ([FAQ](https://freesound.org/help/faq/)). Short link format: `https://freesound.org/s/<id>/`.

### 5.2 Sounds checked (license read from the sound page unless marked)

| Need | Sound | Author | License | Specs | Notes |
|---|---|---|---|---|---|
| **Saw on bone** | [Bone saw #365422](https://freesound.org/people/Diramus/sounds/365422/) | Diramus | **CC0** | 1:12.3, WAV 44.1 kHz/24-bit mono | Recorded on a film set. A stand-in for the sternal saw; layer it with a synthesized motor whine. |
| Monitor beep (speeds up, then stops) | [Heart Monitor Beep #148897](https://freesound.org/people/samfk360/sounds/148897/) | samfk360 | **CC0** | 0:27.9, MP3 320 kbps | |
| Monitor beep, FM synth, flatline | [heartmonitor-EKG.wav #32329](https://freesound.org/people/FreqMan/sounds/32329/) | FreqMan | **CC BY 4.0** | 1:03.9, WAV 44.1/16 stereo | |
| Heartbeat with beep → flatline | [Heartbeat with beep.wav #410379](https://freesound.org/people/b-train/sounds/410379/) | b-train | **CC0** (search snippet, **uncertain**) | 12 s | |
| Flatline tone | [Flatline.wav #257796](https://freesound.org/people/xtrgamr/sounds/257796/) | xtrgamr | **CC BY 4.0** (search snippet, **uncertain**) | 8.8 s | |
| **Hospital ambience** | [emergency room hospital.wav #527438](https://freesound.org/people/bruno.auzet/sounds/527438/) | bruno.auzet | **CC0** | 3:29.3, WAV 48 kHz/16 stereo | French ER: voices, machines, doors. Duck the voices for an OR bed. |
| ICU ambience (beeps, suction, hum) | [ICU.wav #366006](https://freesound.org/people/coetzee_megan12/sounds/366006/) | coetzee_megan12 | **CC BY-NC 3.0** | 1:28.7, WAV 48/24 stereo | **Fluid suction is included.** NC. |
| **Ventilator** | [Breathing machine #703025](https://freesound.org/people/VoxHumanaMusiCurators/sounds/703025/) | VoxHumanaMusiCurators | **CC0** | 0:35.9, WAV 48/24 stereo | Anesthesia ventilator cycle. |
| Infusion pump | [hospital_IV_machine.wav #19553](https://freesound.org/people/gezortenplotz/sounds/19553/) | gezortenplotz | **CC BY 3.0** | 7.5 s, WAV 44.1/16 mono | A Baxter Colleague pump (per a comment). |
| **Suction and drill in a real OR** | [Pack "Geräusche aus dem OP" #15367](https://freesound.org/people/fankitown/packs/15367/) | fankitown | **UNVERIFIED** (pack page shows no license; check each sound) | 12 files: `OP_Sauger_5` (suction), `OP_Bohrer_*` (drill) | Real OR recordings. |
| Hospital room tone | [hospital room ambience with clock, heart beep and paging #427092](https://freesound.org/people/nixeno/sounds/427092/); [… with oxygen system noise #417957](https://freesound.org/people/nixeno/sounds/417957/) | nixeno | #427092 **UNVERIFIED**; #417957 **CC BY-NC 4.0** (snippet) | | |
| Hospital voices and footsteps | [Hospital Sounds pack #3486](https://freesound.org/people/ERH/packs/3486/) | ERH | **CC BY-NC 4.0** (snippet) | | London hospital. |

### 5.3 Gaps: synthesize

No usable free recordings were found for the **electrocautery (Bovie) buzz**, **sternal saw**, **heart-lung machine roller pump**, **cell saver** or **IABP**. Synthesize them. This is better anyway, because these sounds should follow simulation state:

- **Pulse-oximeter tone:** one beep per heartbeat, with **pitch tied to SpO₂** (lower saturation gives a lower pitch). This is a standard monitor behaviour **(well known; the exact pitch mapping varies by manufacturer, uncertain)**.
- **Alarms:** follow the **IEC 60601-1-8** priority structure: high priority is a 10-pulse burst, medium priority 3 pulses, low priority 1–2 pulses **(from memory of the standard; not re-checked in this session)**. Do not copy any brand's exact melody.
- **Roller pump:** a periodic squeeze/thump at **RPM ÷ 60 × number of rollers per second** (2 rollers per head is typical **(uncertain)**), plus motor hum.
- **Electrocautery:** a tonal buzz while the pencil is keyed, with "cut" and "coag" timbres, plus tissue sizzle (layer frying sizzles; the CC0 searches here were not exhaustive).
- **Sternal saw:** a motor whine plus the bone-contact grind (the CC0 bone saw above).

### 5.4 Other audio libraries

| Library | License | Notes |
|---|---|---|
| **Sonniss GameAudioGDC bundles** | Royalty-free, commercial use, **no attribution**. The 2024 bundle **forbids AI training** ([BPB 2024](https://bedroomproducersblog.com/2024/06/27/sonniss-gdc-2024/); [BPB 2026](https://bedroomproducersblog.com/2026/03/16/sonniss-gdc-2026-bundle/)). | Medical content **UNVERIFIED**. Good for generic room tones, UI, doors and metal handling (instrument clinks). |
| **BBC Sound Effects (RemArc licence)** | "**Personal, educational or research purposes**" only, with BBC credit ([MusicTech](https://musictech.com/news/music/the-bbc-sound-effects-archive-over-33000-free-samples)). The licence page could not be fetched, so **(uncertain)**. | Probably fine for a private build. **Redistribution in a public game build is unclear**, so avoid it in anything you share. |

---

## 6. Humans and characters

| Tool | License of what you export | Key terms | Fit |
|---|---|---|---|
| **MakeHuman 1.x / MPFB2 (Blender extension)** | **Core assets CC0.** Since the 2020 license change, exports are CC0 ([MakeHuman license](https://static.makehumancommunity.org/about/license.html); [2020 change FAQ](https://static.makehumancommunity.org/oldsite/faq/what_changed_regarding_the_license_in_2020.html)). | Code: **MPFB = GPL**, MakeHuman = **AGPL**. This does not affect exported models. **Community or third-party assets** (extra clothes, hair, skins) **carry their own licenses**, often CC BY, so check each one. | **Recommended** for the patient body (supine, draped; only the chest is detailed) and for the staff bodies under scrubs. |
| **Mixamo (Adobe)** | Royalty-free use "for personal, commercial, and non-profit projects", including games ([Adobe Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)). | **No redistribution of raw character or animation files**; no ML training ([Adobe community FAQ](https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/m-p/13234775)). Needs an Adobe account **(uncertain)**. Auto-rigging works for **biped humanoids only**. Formats: FBX, DAE. | Good for staff idle, walk, reach and hand-over animations. Keep Mixamo files **out of the public repo** (fetch them locally). |
| **Character Creator 4 (Reallusion)** | **Paid software.** Exporting needs **Export License** content. Shipping in a public game requires **registering the title** with Reallusion. Third-party stores and **in-game character-generator systems are not allowed** without permission ([Reallusion forum staff answers](https://forum.reallusion.com/Topic542475.aspx); the EULA itself is UNVERIFIED). | Not free, with complex terms. | **Not recommended.** |
| **MetaHuman (Epic)** | **Correction to the brief:** since **June 2025 (UE 5.6)** MetaHumans **may be used in other engines (Unity, Godot) and DCC tools**, including commercially. It is free under **US$1M annual revenue**; above that a UE seat (about US$1,850/yr) is needed. **No AI training** ([CG Channel, 4 Jun 2025](https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/); official [metahuman.com/license](https://www.metahuman.com/license) is login-gated, so UNVERIFIED). | **Creation still happens inside Unreal Engine 5.6+.** Autorig and texture synthesis use cloud services. The rigs are heavy (many joints and blendshapes) for a non-UE engine **(uncertain)**. | Optional for close-up faces of staff. Overkill for v1. |
| **Sketchfab CC BY people** | CC BY 4.0 | "FREE DOWNLOAD: Male surgical doctor working 222" (deep3dstudio, photogrammetry, 99,998 faces, `79e23af07d1243c789b3372c6ec72c27`); "Nurse Surgical Rigged" (bachelorgkv, 35,512 faces, `0abc982946cf445fa6c0b68a20e1514f`); "Surgeon PPE" (Indiana University AVL, photogrammetry, 3,153,747 faces, `13e20c1f731443aba481dc5d20b04f81`); "Scrubs Clothing" (whitewashstudio, 42,352 faces, `ed6863b777184edd8affbadeeeceb834`) | References and background characters. The AVL PPE scan is a good gown and mask reference. |

---

## 7. Blender pipeline

**Pin Blender 5.2 LTS** (released 2026-07-14, supported until July 2028 ([Blender 5.2 LTS](https://www.blender.org/releases/5-2/))). Blender 5.0 shipped on 2025-11-18 and 5.1 on 2026-03-17; 5.3 is in alpha. Blender's GPL covers the program, **not your models or renders** (Blender license FAQ; **(not re-checked in this session)**).

### 7.1 Steps

1. **Acquire and record.** Download, compute a SHA-256, and fill in the register row (§8) **before** editing anything. Keep the untouched original in `assets_src/third_party/<id>/original/` (git-ignored if not redistributable).
2. **Medical data → mesh** (for CT/MRI sources):
   - **3D Slicer** (BSD-style license) with the **TotalSegmentator** extension: segment, smooth (median or closing, 1–2 mm), then *Export to files* → **OBJ** (keeps segment colours) or **STL** ([Slicer forum: export](https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj/2428)). **SlicerHeart** (BSD-3-Clause, [GitHub](https://github.com/slicerheart/slicerheart)) adds valve and cardiac tools.
   - **Bioxel Nodes** (Blender extension, **GPL-3.0-or-later** for v2.0.0 of 2026-05-25, Blender 5.0+; older 0.2.x/0.3.x were MIT) imports DICOM and volumes directly into Blender ([extensions.blender.org/add-ons/bioxelnodes](https://extensions.blender.org/add-ons/bioxelnodes/)).
3. **Clean.**
   - *Mesh > Clean Up*: Merge by Distance at about 0.01 mm, Delete Loose, Fill Holes. Use Select Non-Manifold for checks.
   - The bundled **3D-Print Toolbox** extension checks intersections and thin walls.
   - **MeshLab / PyMeshLab** (GPL) handle heavy scans: Screened Poisson rebuild, isotropic remeshing, quadric decimation.
   - Set **real-world scale in metres** and check against a CT case: an adult heart is roughly 12 cm long × 8–9 cm wide × 6 cm deep **(typical textbook range; confirm with research topic 01/02)**.
4. **Retopologize.**
   - Voxel Remesh (about 0.5–1 mm voxel), then **QuadriFlow** (built-in) or **Instant Meshes** (BSD-3-Clause: "Copyright (c) 2015 Wenzel Jakob, Daniele Panozzo, Marco Tarini, and Olga Sorkine-Hornung", [LICENSE.txt](https://github.com/wjakob/instant-meshes/blob/master/LICENSE.txt)).
   - Then **Shrinkwrap** onto the high-poly, with **Multires** for sculpted corrections.
   - Suggested budgets **(uncertain; tune to engine and frame budget)**: hero heart LOD0 40–80k tris (it is seen at about 30 cm through loupes); LOD1 15k; coronaries as separate tube meshes, 5–10k each; thorax opening region 30–50k; patient body away from the field under 20k.
   - **Topology constraints from simulation** (to align with the physics/cutting research): an even edge flow across incision lines, separate shells per tissue layer (skin, fat, fascia, sternum, pericardium, epicardial fat, myocardium), and closed volumes where a soft-body tet-mesh will be generated.
5. **UV.**
   - Mark seams in hidden areas (posterior heart, along the vessel underside), Unwrap (Conformal for organic shapes), then pack.
   - Texel density **(uncertain)**: about 4096² for the heart's main UDIM tile; 2048² for the thorax field; 1024² for instruments. Use UDIMs if the engine supports them; otherwise use 2–3 materials.
   - Free helper: **TexTools** (GPL, **UNVERIFIED** current version and status).
6. **Bake** in Cycles, from high (scan or sculpt, 1–4M faces) to low.
   - Use **normal (OpenGL or DirectX to match the engine)**, AO, curvature (via the Pointiness/Geometry node or the Ambient Occlusion node), cavity, and a base-colour transfer from vertex colours or scan textures.
   - Use a cage (extrusion about 1–2 mm) and Selected-to-Active.
   - Free add-on **Bake Wrangler** (**UNVERIFIED**) automates multi-map bakes.
7. **Materials.** Principled BSDF only, so it maps to glTF (base colour, metallic, roughness, normal, emission, transmission, clearcoat). Bake procedural nodes down to images.
8. **Rig and animate the heartbeat.**
   - **Shape keys**: `atrial_systole`, `ventricular_systole`, `diastolic_fill`, and optionally `fibrillation_noise`. Drive them from an Action, or at runtime from the physiology model (ECG phase → weights). Typical cycle at 70 bpm is about 0.86 s, with systole about one-third **(uncertain; take from the physiology research)**.
   - Add a light **Lattice / Surface Deform** for the cardioplegic arrest "relaxed" pose, and an **Armature** only for rigid parts (retractor arms, clamp jaws, saw blade).
   - Export shape keys as **glTF morph targets** or FBX blend shapes. Bake them to vertex-animation textures if the engine's morph-target count is limiting.
9. **Export.**
   - **glTF 2.0 binary (.glb)** with the built-in exporter (+Y up, apply modifiers, export shape keys and custom properties). Optional Draco or meshopt compression for distribution.
   - **FBX** if the engine prefers it.
   - One file per interactive part (heart, each coronary, pericardium, sternum halves), so the game can swap or cut them.
   - Put the **asset ID and license** into the glTF `extras` (Blender custom properties), so the license travels with the file.
10. **Validate.** Run the Khronos glTF-Validator and an in-engine scale check (a 1 m reference cube), then update the register (status → `approved`).

### 7.2 Free tools and add-ons (summary)

| Tool | License | Use |
|---|---|---|
| Blender 5.2 LTS | GPL (outputs are yours) | Everything |
| Built-ins: QuadriFlow remesh, Decimate, Shrinkwrap, Multires, Rigify, glTF 2.0 I/O, Node Wrangler, LoopTools, 3D-Print Toolbox | GPL (bundled add-ons and extensions) | Cleaning, retopology, rigging, export |
| 3D Slicer + TotalSegmentator + SlicerHeart | BSD-style / Apache-2.0 (open tasks) / BSD-3 | CT/MRI → meshes |
| Bioxel Nodes 2.0.0 | GPL-3.0-or-later | DICOM in Blender |
| MeshLab / PyMeshLab | GPL | Heavy mesh repair |
| Instant Meshes | BSD-3-Clause | Quad retopology |
| Meshroom (AliceVision) | MPL-2.0 **(uncertain)** | Photogrammetry of a pig heart and of instruments |
| TexTools, Bake Wrangler, Material Maker | **UNVERIFIED** | UV, bake and texture helpers |

---

## 8. License compliance approach

### 8.1 Rules

1. **Intake gate.** Every file gets a register row *before* it enters the project. Allowed classes:
   - **A** CC0 / public domain → OK.
   - **B** CC BY → OK; attribution required.
   - **C** CC BY-SA → OK; keep as a separate file and share it under BY-SA.
   - **D** CC BY-NC / BY-NC-SA → OK for the personal build; mark as `blocks-monetization`.
   - **E** Restricted (Sketchfab Standard/Free Standard, Mixamo, DUA data, TotalSegmentator licensed-task outputs, BBC RemArc) → local only, **never in a public repo**.
   - **F** ND, unknown or AI-provenance-unclear → **reject**, or use as reference only.
2. **Repo layout.**
   - `assets_src/` holds sources. Its `third_party/<ID>/` subfolders each contain `LICENSE.txt`, `SOURCE.md` and the original.
   - `assets/` holds game-ready exports.
   - `.gitignore` excludes class **E** files (and D files too, if the repo is public and you would rather not redistribute NC material).
   - A `scripts/fetch_assets` manifest (URL + SHA-256) re-downloads ignored files.
3. **Sidecar per asset.** Place `asset.yml` next to each file with the same fields as the register. Optionally adopt the FSFE **REUSE** convention (`REUSE.toml` or `.license` files) so tools can check coverage.
4. **Credits.** Generate `CREDITS.md` and the in-game credits screen from the register: one line per asset in TASL form plus "modified" notes.
5. **Separation.** Never merge meshes from incompatible SA licenses (BY-SA with BY-NC-SA). Never merge an NC mesh into a CC BY deliverable you intend to share as CC BY.
6. **Re-check when shipping.** Before any public build or video, filter the register for `NC = yes` and `class = E`, and decide.

### 8.2 `ASSET_LICENSES.md` register format

```markdown
# Asset license register

Last reviewed: YYYY-MM-DD. Owner: <name>. One row per source asset; derived files list their source IDs.

| ID | File(s) in repo | Kind | Title (as on source) | Author / rights holder | Source URL | Retrieved | SHA-256 (original) | License (SPDX) | License URL | Class | Attribution required? | NC | SA | ND | Exact attribution text | Modifications made | Used in (scene / feature) | Public-repo OK? | Status | Notes |
|----|------------------|------|----------------------|------------------------|------------|-----------|--------------------|----------------|-------------|-------|-----------------------|----|----|----|------------------------|--------------------|---------------------------|-----------------|--------|-------|
| ANAT-0001 | assets/anatomy/heart/heart_lod0.glb | 3D mesh | 3D Reference Organ for Heart, Male v1.3 | K. Browne et al., HuBMAP / HRA | https://cdn.humanatlas.io/digital-objects/ref-organ/heart-male/v1.3/assets/3d-vh-m-heart.glb | 2026-11-03 | <hash> | CC-BY-4.0 | https://creativecommons.org/licenses/by/4.0/ | B | yes | no | no | no | "3D Reference Organ for Heart, Male v1.3" by HuBMAP Human Reference Atlas (K. Browne et al.), CC BY 4.0; derived from Visible Human data, courtesy of the U.S. National Library of Medicine. Modified. | Retopologized, coronaries and fat added, re-textured | OR scene, heart | yes | approved | License for v1.3 assumed same as v1.2 library statement (verify) |
| ANAT-0002 | assets_src/third_party/ANAT-0002/ | 3D scan (bake source) | CAD Calcification: HH0581 | Visible Heart Laboratories, Univ. of Minnesota | https://sketchfab.com/3d-models/5396e668d3fc47bdb413041d518bd148 | 2026-11-03 | <hash> | CC-BY-4.0 | https://creativecommons.org/licenses/by/4.0/ | B | yes | no | no | no | "CAD Calcification: HH0581" by Visible Heart Laboratories (https://sketchfab.com/3d-models/5396e668d3fc47bdb413041d518bd148), CC BY 4.0. Detail baked into ANAT-0001. | Normal/AO bake only | heart detail | yes | approved | Donor heart: no donor history in game text |
| SFX-0001 | assets/audio/sfx/bone_saw.wav | audio | Bone saw | Diramus | https://freesound.org/s/365422/ | 2026-11-03 | <hash> | CC0-1.0 | https://creativecommons.org/publicdomain/zero/1.0/ | A | no (credit appreciated) | no | no | no | "Bone saw" by Diramus (freesound.org/s/365422), CC0 | Trimmed, layered with synth | sternotomy | yes | approved | |
| OR-0007 | (local only) | 3D mesh | Charité University Hospital - Operating Room | Digital Surgery / Charité | https://sketchfab.com/3d-models/9ec46c4d615a4581a235eebfb162f574 | 2026-11-03 | <hash> | CC-BY-NC-4.0 | https://creativecommons.org/licenses/by-nc/4.0/ | D | yes | YES | no | no | Queisner M, Pogorzhelskiy M, Remde C, Pratschke J, Sauer IM. VolumetricOR… Surg Innov 2022;29(3):406–415. Model: ChrisRE / Digital Surgery, CC BY-NC 4.0 | Used as layout reference only | none (reference) | no (NC; keep local) | reference-only | blocks monetization if shipped |
```

Field rules:
- **License (SPDX)**: use SPDX ids. For non-SPDX terms use `LicenseRef-<Name>` (e.g. `LicenseRef-Sketchfab-Standard`, `LicenseRef-Mixamo`, `LicenseRef-NLM-Terms`, `LicenseRef-MMWHS-DUA`, `LicenseRef-TotalSegmentator-NonCommercial`).
- **Exact attribution text**: copy any wording the source requires (§8.4), word for word.
- **Status**: `review` → `approved` / `reference-only` / `rejected`.
- **Derived assets** list their source IDs in Notes, e.g. `derived from ANAT-0001 + ANAT-0002`.

### 8.3 Intake checklist (per asset)

1. Is the license shown on the asset's **own page**? (A blog or search snippet is not enough.) Save a screenshot or PDF of the page in `SOURCE.md`.
2. Is the uploader plausibly the rights holder? Reject re-uploads of commercial or game IP, AI-generated items with unclear origin, and "free" items that are ripped from paid stores.
3. Look for NC, SA or ND flags, and for special credit wording in the description (Charité, BodyParts3D, NLM).
4. Does the item contain bundled sub-assets under other licenses? (Z-Anatomy has NC parts.)
5. Are there logos or trademarks on the textures? Remove them.
6. Record the SHA-256 and the date. Decide the class (A–F) and whether it may go in the public repo.

### 8.4 Required or requested attribution texts (copy exactly)

- **BodyParts3D:** "BodyParts3D, Copyright© The Database Center for Life Science licensed by CC Attribution-Share Alike 2.1 Japan" ([README](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html)).
- **Z-Anatomy** (models): "BodyParts3D - The Database Center for Life Science - CC-BY-SA 2.1 Japan" and "Z-Anatomy - The libre 3D atlas of anatomy - CC-BY-SA 4.0". Definitions, if used: "Wikipedia - CC-BY-SA 3.0" ([The-blend README](https://github.com/Z-Anatomy/The-blend)).
- **NLM data (Visible Human):** "Courtesy of the U.S. National Library of Medicine", and do not imply NLM endorsement ([NLM terms](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html)).
- **HRA / HuBMAP:** cite the release, e.g. "Browne K, Schlehlein H, Herr II BW, Quardokus E, Bueckle A, Börner K (2022). HuBMAP CCF 3D Reference Object Library", plus the version, link and CC BY 4.0 ([library page](https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html)).
- **Digital Surgery / Charité instruments:** "Christopher Remde, Moritz Queisner, 2024, Experimental Surgery, Charité Universitätsmedizin Berlin & NMY Mixed-Reality Communication GmbH". Instrument tables: the same without "& NMY…". Charité OR: cite the Queisner 2022 *Surg Innov* paper (from the Sketchfab descriptions).
- **TotalSegmentator dataset:** cite Wasserthal J. et al., "TotalSegmentator: robust segmentation of 104 anatomical structures in CT images", *Radiology: AI* 2023, plus Zenodo DOI and CC BY 4.0 ([Zenodo record](https://zenodo.org/records/10047292)).
- **Generic CC BY (Sketchfab, Freesound):** `"<Title>" by <Author> (<URL>), licensed under CC BY 4.0 (<license URL>). Changes: <what you changed>.`
- **CC0** (Poly Haven, ambientCG, Kenney, Freesound CC0): no credit required. A courtesy line in the credits is recommended.

---

## 9. Open questions for the plan

1. **Will the repo be public?** If so, which asset classes (B, C, D) may be committed, and which are fetched locally? The recommendation is to commit A, B and C only.
2. **Will gameplay videos be monetized, or the game sold or donation-funded?** If ever, NC assets (Visible Heart fresh hearts, Charité OR, NC Freesound ambiences) must be replaceable. Build a "CC0/CC BY-only" asset set from day one.
3. **Engine choice** (from another research topic) affects the formats: glTF for Godot/Unity (via glTFast) or FBX/Interchange for Unreal, and the morph-target limits for the heartbeat.
4. **Coronary source:** apply for the free TotalSegmentator non-commercial license to get `coronary_arteries` and `heartchambers_highres`, or hand-model the coronaries from Z-Anatomy (BY-SA)?
5. **Pig-heart photogrammetry:** is the owner willing to buy and scan a pig heart, sternum and ribs (cheap, best realism, no license issues)? It needs a turntable, about 100–200 photos and cross-polarized lighting.
6. **Still UNVERIFIED** and to be checked before use: HRA v1.3 license wording on humanatlas.io; NIH 3D Heart Library per-entry licenses; Open Anatomy thoracic atlas license; Visible Korean terms; Embodi3D terms; ImageCHD / ASOCA / ImageCAS / MSD licenses; the licenses of the fankitown OR pack and nixeno #427092 on Freesound; the BBC RemArc licence text; the current Mixamo additional terms; the MetaHuman EULA text; TexTools, Bake Wrangler, Material Maker and Meshroom licenses.
