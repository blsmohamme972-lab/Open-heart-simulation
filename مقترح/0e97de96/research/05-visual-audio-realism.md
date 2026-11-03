# Research 05: Visual and audio realism

> **Purpose:** Evidence for the plan proposal (مقترح) on how to make an open heart surgery simulation game look and sound as close to real life as possible. It covers tissue rendering, beating-heart motion, operating room (OR) light and layout, OR audio and alarms, legal reference sources, and low-budget production methods for a solo developer.
>
> **Researched 2026-11-03 (re-do, fresh searches).** Method note: the shared web-search budget for this run was already used up before this agent's first search. So every fact below comes from direct page fetches: official documentation, license pages, PMC full texts, Europe PMC and Crossref records, and Wikipedia pages (used mainly to locate primary references). Items that could not be checked are marked "(uncertain)" or "UNVERIFIED". A follow-up run with search budget should close the gaps listed in the Summary.
>
> **Disclaimer:** This is research for a personal, non-commercial, educational game. It is **not clinical guidance**, not a certified training device, and must not be used to make medical decisions. Numbers are given to drive believable visuals and sounds, not to treat patients.

Abbreviations used: SSS = subsurface scattering; MFP = mean free path; BSDF = bidirectional scattering distribution function; HDRP = Unity High Definition Render Pipeline; UE = Unreal Engine; CPB = cardiopulmonary bypass; HLM = heart-lung machine; LV/RV = left/right ventricle; LAD/LCx/RCA = left anterior descending / left circumflex / right coronary artery; ECG = electrocardiogram; SpO2 = pulse-oximeter oxygen saturation; VF = ventricular fibrillation; OR = operating room; CCT = correlated colour temperature; CRI (Ra) = colour rendering index; HP/MP/LP = high/medium/low priority alarm; ACT = activated clotting time.

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Tissue shading model | UE: Substrate Slab with Diffusion SSS (default for new projects from UE 5.7) or the legacy Subsurface Profile. Unity: HDRP Diffusion Profile (HDRP 17). Godot: BaseMaterial3D SSS "skin mode" + transmittance. Author and bake in Blender (Random Walk Skin SSS, Coat layer). | [UE Substrate](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine), [UE Subsurface Profile](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine), [HDRP 17 Diffusion Profile](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/diffusion-profile-reference.html), [Godot 4.7](https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html), [Blender 5.2 manual](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) |
| Wet look | Two specular lobes (UE second roughness / HDRP dual lobe) or a Coat layer, driven by a per-tissue "wetness" mask. | Same docs as above |
| Myocardium colour states | One parametric material with inputs: oxygenation, blood volume, temperature, wetness, blood mask, char mask, scar mask. Drive colour from haemoglobin absorption physics, then tune by eye. | [Prahl Hb spectra](https://omlc.org/spectra/hemoglobin/), [Jacques 2013](https://pubmed.ncbi.nlm.nih.gov/23666068/), [Blood colour](https://en.wikipedia.org/wiki/Blood) |
| Blood | Arterial bright red (SaO2 about 98-99%), venous darker (about 75%, 70-78%); dried blood shifts toward brown (methaemoglobin). No clots while heparinised (ACT > 480 s on CPB). | [Blood](https://en.wikipedia.org/wiki/Blood), [CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass) |
| Cautery | Char decal + white-grey smoke plume (about 95% water/steam; mean particle 0.07 µm for electrocautery) that can block the view; sizzle sound. | [Liu 2019 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/), [Surgical smoke](https://en.wikipedia.org/wiki/Surgical_smoke), [Electrosurgery](https://en.wikipedia.org/wiki/Electrosurgery) |
| Heart motion | Data-driven deformer: apex rotates about 11-12 deg one way, base about 4.6-4.8 deg the other (net twist about 16 deg); coronary surface points move about 10-26 mm per beat; outer heart volume changes only about 8%. | [Helle-Valle 2005](https://pubmed.ncbi.nlm.nih.gov/16286606/), [Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/), [Carlsson 2004](https://doi.org/10.1152/ajpheart.01125.2003) |
| ECG-driven timing | One master clock: cycle = 60/HR; at 75 bpm systole about 0.3 s and diastole about 0.5 s; untwisting mostly in isovolumic relaxation. | [Diastole](https://en.wikipedia.org/wiki/Diastole), [Nakatani 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3079077/) |
| Surgical lights | Central illuminance 40,000-160,000 lux (IEC 60601-2-41 range), Ra 85-100; good practice 50,000-100,000 lux central and 2,000 / 4,000 / 5,500 lux general lighting (periphery / around table / on table). | [Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting), [Hemphälä 2020](https://api.crossref.org/works/10.1177/1477153520903355), [Knulst 2009](https://doi.org/10.1177/1553350609353766) |
| Pulse-oximeter tone | Pitch falls as SpO2 falls. Use about 0.5 semitone per 1% (648 Hz at 99%, 630 Hz at 98% in a lab study). Real devices vary a lot (479-921 Hz at 100%). | [Stevenson 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/), [Loeb 2016](https://doi.org/10.1213/ane.0000000000001240) |
| Alarms | IEC 60601-1-8 priority patterns: HP = two 5-pulse blocks (10 pulses), MP = 3 pulses. Offer a toggle between the old tonal melodies and the 2020 (Amendment 2) auditory icons. | [Ribeiro Ferreira 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/), [Edworthy 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/), [Edworthy 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12106860/) |
| OR soundscape | Bed level about 67 dB SPL (58-86) in a cardiac OR recording; literature average about 77 dB, peaks above 100 dB; OR volume 71-196 m³ for reverb. | [Stevenson 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/), [McNeer 2017](https://doi.org/10.1213/ane.0000000000002118) |
| Spatial audio | Steam Audio 4.8.1 (Apache-2.0) or engine-native (UE MetaSounds for procedural tones). | [Steam Audio](https://github.com/ValveSoftware/steam-audio), [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine) |
| Anatomy base meshes | BodyParts3D (now CC BY 4.0), Z-Anatomy (CC BY-SA 4.0), HuBMAP CCF reference organs (CC BY 4.0), Visible Human (no licence needed since 2019). | [BodyParts3D licence](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [Z-Anatomy](https://github.com/LluisV/Z-Anatomy), [HuBMAP CCF](https://github.com/hubmapconsortium/ccf-3d-reference-object-library), [Visible Human](https://www.nlm.nih.gov/research/visible/visible_human.html) |
| Textures/materials | CC0 libraries (Poly Haven, ambientCG) for OR props; Material Maker (MIT) and Blender (GPL; output is yours) for procedural tissue. | [Poly Haven](https://polyhaven.com/license), [ambientCG](https://docs.ambientcg.com/license/), [Material Maker](https://github.com/RodZill4/material-maker), [Blender licence](https://www.blender.org/about/license/) |
| AI helpers | TRELLIS (MIT) is safe; Hunyuan3D 2.x licence excludes EU, UK and South Korea; Gaussian Splatting reference code is non-commercial; Stable Audio Open is free under USD 1M revenue. | [TRELLIS](https://github.com/microsoft/TRELLIS), [Hunyuan3D licence](https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/LICENSE), [3DGS licence](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md), [Stability licence](https://stability.ai/license) |
| Reference videos | Watch only, never ship or download. YouTube allows viewing for personal non-commercial use only (terms dated 2023-12-15). CTSNet terms UNVERIFIED (page blocked). | [YouTube Terms](https://www.youtube.com/t/terms) |

---

## 1. Realistic tissue rendering

### 1.1 Why tissue needs subsurface scattering

- Biological tissue scatters light strongly. Its colour comes from absorbers (blood, water, fat, melanin and others) mixed with scattering by cell structures. Jacques' review gives formulas for a "generic tissue" built from these components ([Jacques 2013, Phys Med Biol 58:R37-R61](https://pubmed.ncbi.nlm.nih.gov/23666068/)). This is the physical reason a plain diffuse texture looks like plastic.
- Haemoglobin is the main red absorber. Oxy- and deoxy-haemoglobin absorb differently, which is why arterial and venous blood differ in colour ([Blood](https://en.wikipedia.org/wiki/Blood)). Scott Prahl's tables give the molar extinction spectra of both forms; for whole blood at 150 g Hb/L, the absorption coefficient is about 0.0054 x the extinction value (cm⁻¹) ([Prahl, OMLC](https://omlc.org/spectra/hemoglobin/)). The page says "Copyright 1999 Scott Prahl" and gives no reuse licence, so use the numbers to compute colours, but do not redistribute the tables (licence UNVERIFIED).

### 1.2 Engine options for skin-like tissue

| Engine / tool | Feature | Facts that matter for tissue | Source |
|---|---|---|---|
| UE (5.7 and later) | **Substrate** | Substrate is enabled by default for new projects; projects upgraded to UE 5.7+ stay on the legacy path unless switched. Slabs can be layered. Sub-surface types: Wrap, Two-Sided Wrap, Diffusion, Simple Volume. Has SSS MFP and phase anisotropy inputs, F0/F90, Roughness plus Second Roughness (a second specular lobe for wetness), Fuzz, thin-film and "haziness" helpers. Two BSDFs cost about twice the lighting cost of one. Default `r.Substrate.BytesPerPixel` is 80. Diffusion SSS is not available on mobile. With "Blendable GBuffer", Diffusion SSS with per-pixel MFP and Haziness are not supported. DX11 and Mac "may not work entirely". Translucent materials do not get screen-space SSS. | [UE Substrate overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine) |
| UE | **Subsurface Profile** (legacy shading model) | Screen-space post-process. Parameters: Scatter Radius (world units), Subsurface Color, Falloff Color, Mean Free Path colour and distance, World Unit Scale (cm). Limits: no mobile, no backscatter, a grey outline where non-SSS objects cover SSS objects, banding with large radii. Burley mode needs Temporal Anti-Aliasing. | [UE Subsurface Profile](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine) |
| Unity HDRP 17.0.4 | **Diffusion Profile** | Scattering Color + Multiplier define how far light travels under the surface. World Scale default: 1 Unity unit = 1 m. If Max Radius is smaller than a pixel on screen, HDRP skips SSS (important for close-up surgical cameras: SSS will appear; for wide room shots it may switch off). Transmission Mode: Thick Object or Thin Object. Dual-lobe specular with Lobe Mix default 0.5. | [HDRP 17 Diffusion Profile](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/diffusion-profile-reference.html) |
| Godot 4.7 | **BaseMaterial3D SSS** | `subsurf_scatter_enabled`, `subsurf_scatter_strength`, `subsurf_scatter_skin_mode` (tuned for human skin), transmittance colour/depth (default depth 0.1)/boost; `clearcoat` (default 1.0) and `clearcoat_roughness` (default 0.5) for a wet layer. | [Godot 4.7 BaseMaterial3D](https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html) |
| Blender 5.2 LTS (authoring, baking, reference renders) | **Principled BSDF** | Subsurface Weight (normally 0 or 1), per-RGB Radius, Scale, IOR and Anisotropy (Cycles; the manual says skin is about 0.8). Methods: Christensen-Burley, Random Walk, Random Walk (Skin). Coat layer (Weight, Roughness, IOR, Tint, Normal) for a wet film; Sheen for fine fibres/dust. | [Blender 5.2 manual](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) |

Recommendation: write one "tissue master material" per engine with the same parameter names, so data from the simulation (oxygenation, wetness, temperature) drives visuals the same way whichever engine the plan picks. Engine choice itself is covered by research topic 04, not here.

### 1.3 Tissue catalogue (what the camera sees in a sternotomy)

Starting values below are **design values, not measurements** (uncertain). They are meant to be tuned against licensed reference photos and the animal-heart reference shoot in section 6.

| Tissue | Look cues | Shader recipe | Starting values (design, uncertain) |
|---|---|---|---|
| Myocardium seen through epicardium | Deep red to red-brown muscle under a thin, glossy, transparent serous layer (the visceral serous pericardium = epicardium, [Pericardium](https://en.wikipedia.org/wiki/Pericardium)). Fine vessels visible. | SSS Slab (MFP red >> green > blue) + Coat/second lobe for the epicardial film. | Wet roughness 0.1-0.2, dry 0.35-0.5; SSS radius red about 3-5 mm, green about 1 mm, blue about 0.5 mm. |
| Epicardial fat | Yellow, lobulated fat around the heart, around coronary vessels (Wikipedia confirms it is visceral fat around the heart; groove locations not confirmed this run: uncertain) ([Epicardial adipose tissue](https://en.wikipedia.org/wiki/Epicardial_adipose_tissue)). | More translucent than muscle: larger SSS radius, slightly yellow falloff, glossy. | Base colour pale yellow-cream; roughness 0.15-0.3. |
| Pericardium (opened) | Tough fibroelastic sac ([Pericardium](https://en.wikipedia.org/wiki/Pericardium)). In CABG it is opened and held up with stay sutures ([CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery)), making a "well" where blood and saline pool. | Two-sided thin material: fibrous outside (rough, white-grey), smooth glossy inside. Thin-object transmission. | Thickness: not verified (uncertain). |
| Ascending aorta | Pale cream-white wall, purse-string sutures and the arterial cannula ([CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery)). | Low SSS, medium gloss; tiny vasa vasorum detail texture. | Roughness 0.2-0.3. |
| Coronary arteries and grafts | Run on the heart surface, often partly buried in fat. | Separate meshes for the target vessel so incision and anastomosis can deform it. | n/a |
| Sternum (cut) | Ivory cortical bone, red marrow ooze from the cut face, bone wax smears. | Rough bone + animated "ooze" mask until waxed. | Bone roughness 0.6-0.8. |
| Skin and subcutaneous fat | Prepped skin (antiseptic stain), yellow fat layer under the incision. | Skin SSS profile; fat with large SSS radius. | n/a |
| Blood (fresh, pooled, dried, clot) | See 1.5. | Decals + wetness/blood render-target masks + fluid surface for pools. | See 1.5. |
| Char | Black-brown cautery spots and edges. | Char mask: darker albedo, higher roughness, slight height. | Roughness 0.7-0.9. |

### 1.4 Myocardium colour states

| State | Physiology driver (evidence) | Visual change for the game | Confidence |
|---|---|---|---|
| Normal perfused, beating | Oxygenated blood in the muscle; arterial blood is bright red ([Blood](https://en.wikipedia.org/wiki/Blood)). | Rich red-brown, glossy, moving. | High for direction, design for exact colour |
| Regional ischaemia (coronary occluded or graft blocked) | Deoxygenated blood is darker ([Blood](https://en.wikipedia.org/wiki/Blood)). Tissue starts to die within 15-30 min of loss of blood supply ([Myocardial infarction](https://en.wikipedia.org/wiki/Myocardial_infarction)). | Dusky, darker, bluish-purple patch in the territory downstream; that region moves less. | Direction from optics; appearance (uncertain) |
| Cardioplegic arrest | Cardioplegia raises extracellular potassium; at 16.2 mmol/L the resting potential reaches about -60 mV and fibres stop responding. Cold fluid (usually 4 °C) is used, and the heart cools to roughly 15-20 °C ([Cardioplegia](https://en.wikipedia.org/wiki/Cardioplegia)). The ECG goes to asystole ([Cardioplegia](https://en.wikipedia.org/wiki/Cardioplegia)). | Motion stops within minutes ([CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery)). Surface goes slack and still. With blood-based cardioplegia it stays dark red; with crystalloid it can look paler (uncertain). Optional: a faint cold "matte" look. | Physiology high; exact colour (uncertain) |
| Reperfusion (cross-clamp off) | The aortic clamp is removed and the heart is de-aired ([CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery)). | Colour returns toward red; the heart may restart in sinus rhythm or fibrillate and need internal defibrillation (incidence and energy: uncertain, see 2.4). | Partly uncertain |
| Distension (LV not vented) | Not verified this run (uncertain). | LV swells, becomes tense and shiny. Used as a "warning" visual if venting fails. | Uncertain |
| Old infarct scar | Dead muscle is replaced by collagen scar ([Myocardial infarction](https://en.wikipedia.org/wiki/Myocardial_infarction)). | White-grey, thinner patch that does not contract. Good for patient-variety cases. | Medium |

Implementation idea: compute a small lookup table offline. For oxygen saturation from 0 to 1, mix the oxy- and deoxy-haemoglobin spectra ([Prahl](https://omlc.org/spectra/hemoglobin/)), run a simple diffuse-reflectance model, and convert to sRGB. The shader then reads `colour = LUT(oxygenation, bloodVolume)`. Hand-tune the result against references. This keeps colour changes physically consistent across states.

### 1.5 Blood

| Item | Evidence | Game rule / rendering |
|---|---|---|
| Arterial vs venous colour | Arterial blood leaving the lungs is about 98-99% saturated and bright red; venous blood is about 75% (70-78%) saturated and darker red ([Blood](https://en.wikipedia.org/wiki/Blood)). | Arterial bleed = brighter, pulsatile spurts timed to the ECG; venous bleed = darker, steady ooze. On CPB, the arterial line (after the oxygenator) is bright red and the venous return line is dark red (CPB oxygenator adds oxygen and removes CO2: [CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)). |
| Clotting | Heparin is given before cannulation until ACT is above 480 s; protamine reverses it after bypass ([CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)). | No clots form while ACT > 480 s. After protamine, clot visuals (dark red jelly, thicker, less glossy) can appear in the pericardial well. |
| Dried blood | Oxidised haem forms methaemoglobin, which is brownish ([Blood](https://en.wikipedia.org/wiki/Blood)). | Blood stains on drapes, gloves and gauze darken and turn brown over time. Exact time curve (uncertain). |
| Wet maps and staining | Engine-level technique (no medical source needed). | Per-object render-target masks: `wetness` (saline, blood), `bloodAmount`, `bloodAge`. Paint at the UV of each hit or drip. Drying lowers gloss and raises roughness. Gauze and sponges use absorption masks that grow from the contact point. |
| Pooling | Engine-level technique. | Height-field "pool" surface in the pericardial well; suction lowers its level; level feeds the "visibility" score. |

### 1.6 Cautery char and smoke

| Item | Evidence | Rendering / gameplay |
|---|---|---|
| Electrosurgery basics | Generators run at about 100 kHz to 5 MHz; "cut" uses a continuous sine wave, "coag" switches the wave on and off (lower duty cycle). In wet-field cutting the vapour pocket reaches about 400 °C ([Electrosurgery](https://en.wikipedia.org/wiki/Electrosurgery)). | Two modes with different visuals: cut = clean line with small smoke; coag = wider blanching and more char and smoke. |
| Smoke composition | About 95% water/steam and 5% cellular debris; electrocautery makes the smallest particles (mean aerodynamic size 0.07 µm); laser about 0.31 µm; 77% of plume particles are under 1.1 µm ([Liu 2019, J Cancer, PMC6584931](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/)). | White-grey, thin, fast-rising wisps that fade quickly (mostly steam). Use small soft GPU particles or a light volumetric. |
| Visibility | Smoke can obscure the surgical field ([Surgical smoke](https://en.wikipedia.org/wiki/Surgical_smoke); [Liu 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/)). Smoke evacuators are described as bulky and noisy ([Surgical smoke](https://en.wikipedia.org/wiki/Surgical_smoke)). | Smoke lowers a "field visibility" value; the assistant's suction or a smoke evacuator clears it but adds noise. |
| Char | Carbonisation at high temperature (exact threshold not verified this run: uncertain). | Char decal accumulates with time-on-tissue; too much char = penalty (tissue damage). |

### 1.7 Bone dust and the sternal saw

- Median sternotomy is a vertical midline incision followed by division of the sternum with a sternal saw ([Median sternotomy](https://en.wikipedia.org/wiki/Median_sternotomy)). Key steps in the EACTS video manual (MMCTS) are: find landmarks, prepare the midline, cut while avoiding pleura, pericardium, innominate vein and aorta, control bleeding, and close with wires at correct spacing ([Reser et al. 2015, MMCTS](https://doi.org/10.1093/mmcts/mmv017)).
- No source with numbers for bone dust or saw spray was found this run (uncertain). Design: a short burst of fine pale particles and a light blood mist along the blade path, a marrow ooze mask on both cut faces, and a "bone wax" tool that stops the ooze.

---

## 2. Beating heart realism

### 2.1 Timing from the ECG

| Quantity | Value | Source |
|---|---|---|
| Cycle length | About 0.8 s at 70-75 bpm; inversely proportional to heart rate | [Cardiac cycle](https://en.wikipedia.org/wiki/Cardiac_cycle) |
| Systole vs diastole at 75 bpm | About 0.3 s systole, about 0.5 s diastole | [Diastole](https://en.wikipedia.org/wiki/Diastole) |
| Ventricular filling | About 80% early (passive, "suction"), the rest from atrial contraction ("atrial kick") | [Diastole](https://en.wikipedia.org/wiki/Diastole) |
| ECG link | P wave = start of atrial systole; QRS (Q) = start of ventricular systole; T wave = ventricular relaxation | [Cardiac cycle](https://en.wikipedia.org/wiki/Cardiac_cycle) |
| QT and rate | QT shortens as rate rises; rough rule: subtract 0.02 s for each 10 bpm above 60 | [QT interval](https://en.wikipedia.org/wiki/QT_interval) |
| Untwisting | Mostly during isovolumic relaxation | [Nakatani 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3079077/) |

Design formula (derived from the rows above; uncertain): `T_cycle = 60/HR`, `T_sys = clamp(0.30 - 0.002*(HR - 75), 0.20, 0.40)` s, `T_dia = T_cycle - T_sys`. Start the mechanical systole curve at the QRS and end it near the end of the T wave. At high heart rates the diastole shrinks most, which the player will see as a "hurried" heart.

### 2.2 Motion amplitudes (data for the deformer)

| Motion | Value | Source | Grade |
|---|---|---|---|
| Apical rotation (healthy humans, MRI tagging) | -11.6 ± 3.8 deg (speckle tracking: -10.9 ± 3.3) | [Helle-Valle 2005, Circulation](https://pubmed.ncbi.nlm.nih.gov/16286606/) | A |
| Basal rotation (MRI tagging) | 4.8 ± 1.7 deg (speckle tracking: 4.6 ± 1.3) | [Helle-Valle 2005](https://pubmed.ncbi.nlm.nih.gov/16286606/) | A |
| Net twist (derived) | About 16 deg (11.6 + 4.8) | Derived from the row above | B |
| Direction | Base rotates clockwise and apex counter-clockwise in systole (viewed from the apex); signs differ between papers | [Nakatani 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3079077/), [Sengupta 2008](https://pubmed.ncbi.nlm.nih.gov/19356451/) | A |
| Coronary point displacement per beat (3-D) | LAD (5 cm from origin) 9.6 ± 1.3 mm; LCx 12.1 ± 2.4 mm; RCA mid 26.3 ± 3.1 mm; RCA ostium 14.4 ± 1.9 mm | [Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/) | A |
| Same points, respiration (spontaneous breathing) | 5.0-7.2 mm per breath | [Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/) | A |
| Peak systolic velocity | LAD 47.5 mm/s; RCA mid 130.7 mm/s | [Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/) | A |
| Total heart volume change | Only 8.2 ± 0.8% (range 4.8-10.6%) smaller in systole | [Carlsson 2004](https://doi.org/10.1152/ajpheart.01125.2003) | A |
| RV long-axis motion (TAPSE) | 24 ± 3.5 mm; below 17 mm is abnormal | [ASE/EACVI 2015](https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf) | A |
| LV global longitudinal strain | About -20% in a healthy person | [ASE/EACVI 2015](https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf) | A |
| LV ejection fraction (normal) | 52-72% (men), 54-74% (women) | [ASE/EACVI 2015](https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf) | A |
| Wall thickening | About 15% myocyte shortening becomes about 40% radial wall thickening | [Speckle tracking](https://en.wikipedia.org/wiki/Speckle_tracking_echocardiography) | C |

What this means visually:
- The heart does **not** "balloon" much. Its outer volume changes only about 8% ([Carlsson 2004](https://doi.org/10.1152/ajpheart.01125.2003)). Most visible motion is the base moving toward the apex (long-axis shortening), the wringing twist, and wall thickening. Many games over-inflate the heart; avoid that.
- The right coronary groove moves much more (about 26 mm) than the LAD region (about 10 mm) ([Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/)). This matters for off-pump stabiliser scenes.
- In the open chest with a ventilator, add a slow respiratory shift of about 5-7 mm (the measured values are for spontaneous breathing, so ventilated values are uncertain). When ventilation is paused on full bypass, remove it (uncertain, check with topic 02).

### 2.3 Deformer design

1. **Rig:** long axis from base (AV plane) to apex. Each vertex has a normalised height `h` (0 = base, 1 = apex) and a wall depth.
2. **Twist:** rotate around the long axis by `angle(h, t) = lerp(+4.8, -11.6, h) * s(t)` degrees (signs per the Helle-Valle convention, [source](https://pubmed.ncbi.nlm.nih.gov/16286606/)), where `s(t)` is a 0-1 systolic curve. Release most of the twist during the first part of diastole (isovolumic relaxation, [Nakatani 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3079077/)).
3. **Long-axis shortening:** move the base toward the apex by about 15-25 mm at end-systole (TAPSE 24 mm on the RV side, [ASE/EACVI 2015](https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf); LV value not verified this run: uncertain). Keep the apex nearly fixed.
4. **Radial thickening:** push the endocardial side inward more than the epicardial side. Keep the outer volume change at about 8% ([Carlsson 2004](https://doi.org/10.1152/ajpheart.01125.2003)).
5. **Validation:** sample the LAD and RCA marker points and check that their 3-D path lengths are near 10 mm and 26 mm ([Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/)).
6. **Baking option:** for low-end hardware, bake one cycle from Blender into a vertex animation texture and play it back at a speed set by heart rate, with the systole/diastole split from 2.1.

### 2.4 Special states

| State | What to show | Evidence | Confidence |
|---|---|---|---|
| Beating, on partial bypass | Normal motion, smaller filling | Design | Low |
| Beating, empty, on full bypass | Smaller, fast, little filling | Design | Low (uncertain) |
| Cross-clamp + cardioplegia | Stops within minutes; asystole on ECG; cold and still | [CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery), [Cardioplegia](https://en.wikipedia.org/wiki/Cardioplegia) | High |
| Ventricular fibrillation | Ventricles "quiver" with random uncoordinated twitching; ECG shows irregular activity with no clear pattern; "coarse" vs "fine" by amplitude (fine VF can look like asystole at low gain) | [Ventricular fibrillation](https://en.wikipedia.org/wiki/Ventricular_fibrillation); VF is driven by uncoordinated wavefronts ([Dosdall 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC3984906/)) | Medium. Dominant frequency not verified (uncertain) |
| Internal defibrillation | Paddles touch the myocardium directly ([Defibrillation](https://en.wikipedia.org/wiki/Defibrillation)) | Energy in joules not verified this run (uncertain; take from topic 02) | Low |
| Reperfusion | Colour returns; then sinus rhythm or VF | [CABG](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery) | Medium |
| Distension | LV swells and becomes tense if not vented | Not verified (uncertain) | Low |

VF visual recipe (design): turn off the coordinated deformer; add 3-6 travelling noise "waves" across the ventricular surface with small amplitude (a few mm) and fast, irregular timing; coarse VF = larger amplitude; fine VF = barely visible shimmer. Couple the ECG trace to the same noise seed so the screen and heart agree.

---

## 3. Operating room realism

### 3.1 Surgical lighting

| Parameter | Value | Source | Grade |
|---|---|---|---|
| Central illuminance (Ec) of a surgical luminaire | 40,000-160,000 lux (IEC 60601-2-41 summary; Wikipedia prints the bounds reversed) | [Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting) | B |
| Maximum | 160,000 lux (IEC 60601-2-41:2013), about the strength of direct sunlight | [Operationsleuchte (de)](https://de.wikipedia.org/wiki/Operationsleuchte) | B |
| Colour rendering | Ra 85-100 | [Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting) | B |
| Light field | D50 at least 50% of D10 (D10 = diameter where light falls to 10% of Ec) | [Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting) | B |
| Power failure | Back within 5 s at not less than 50% (and not below 40,000 lux); full within 40 s | [Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting) | B |
| Measured LED lights | Ec 25-160 klux; field size (d10) 109-300 mm; segmented lights cast uneven patterns; coloured LEDs give coloured shadow edges | [Knulst 2009, Surg Innov](https://doi.org/10.1177/1553350609353766) | A |
| Recommended for open surgery | Central beam 50,000-100,000 lux; general lighting 2,000 lux at room edge, 4,000 lux around the table, 5,500 lux on the table | [Hemphälä 2020, Lighting Res Technol](https://api.crossref.org/works/10.1177/1477153520903355) | A |
| Product example | Light field adjustable 13-27 cm (Getinge Maquet PowerLED II) | [Getinge](https://www.getinge.com/int/products/maquet-powerled-ii/) | B |
| CCT | 3,000-6,700 K is the commonly quoted IEC range, not verified this run (UNVERIFIED) | none fetched | C |

Game rules:
- Use physical light units. Set two lamp heads at about 80,000-100,000 lux each at the field, the room at 2,000-5,500 lux ([Hemphälä 2020](https://api.crossref.org/works/10.1177/1477153520903355)). Use auto-exposure tuned so the field is correctly exposed and the room looks darker, the way it looks to staff and on video.
- Light-handle mini-task: the surgeon or assistant can re-aim lights. Shadows from heads and hands are a real problem that multi-head lights reduce, so a badly aimed lamp should create a shadow in the chest.

### 3.2 Layout, team and sterile field

| Element | Evidence | Confidence |
|---|---|---|
| Anaesthesia machine at the head of the table, cart beside it | [Operating theater](https://en.wikipedia.org/wiki/Operating_theater) | Medium |
| Circulating nurse and anaesthetist are not part of the sterile team and keep 12-16 inches (about 30-40 cm) from sterile objects | [Operating theater](https://en.wikipedia.org/wiki/Operating_theater) | Medium |
| Cardiac OR is a complex, team-dependent environment; human factors and teamwork are key | [Wahr et al. 2013, AHA scientific statement](https://doi.org/10.1161/CIR.0b013e3182a38efa) | A (topic level) |
| Perfusionist runs the HLM; the HLM has level detectors, bubble detectors, arterial line filter and pressure transducers | [EACTS/EACTA/EBCP 2019 CPB guideline](https://academic.oup.com/ejcts/article/57/2/210/5579397) | A |
| Typical positions: surgeon on the patient's right, first assistant on the left, scrub nurse near the surgeon, perfusionist and HLM a few metres away with line of sight to the field | Common practice; not verified this run (uncertain) | Low |

### 3.3 Camera views and magnification

| View | Notes | Evidence |
|---|---|---|
| Surgeon eye (default) | First-person view looking down into the chest, slight head bob, hands in view. | Design |
| Loupe view | Toggle to a magnified view with a smaller, sharper field and shallow depth of field. Higher magnification shrinks field of view and depth of field. Use 2.5x as the base level, with 3.5x and 4.5x as options. | Field-of-view principle: [Loupe](https://en.wikipedia.org/wiki/Loupe). The 2.5x-4.5x range for cardiac work is from the brief and not verified this run (uncertain). |
| Headlight | A narrow, very bright spot that follows the head; fills deep holes the ceiling lights miss. Brightness not verified (uncertain). | Design |
| Microscope | Not usual for open heart surgery (from the brief; not verified this run: uncertain). | Design |
| Perfusion and anaesthesia stations | Separate views with the HLM console and monitor, for team-play scenes. | [EACTS 2019](https://academic.oup.com/ejcts/article/57/2/210/5579397) for HLM components |

### 3.4 Drapes and visual dressing

- Use blue or green non-woven drapes, an antiseptic-stained skin window, and an adhesive incise film (common appearance; not verified this run: uncertain).
- Use CC0 materials for fabric, steel, plastic and floors ([Poly Haven](https://polyhaven.com/license), [ambientCG](https://docs.ambientcg.com/license/)).
- Getinge's PowerLED II page shows ambient light that can be set "from white to yellow", a cue for room mood lighting ([Getinge](https://www.getinge.com/int/products/maquet-powerled-ii/)).

---

## 4. Audio

### 4.1 Pulse-oximeter tone (the most important sound)

| Fact | Value | Source | Grade |
|---|---|---|---|
| Survey of real devices | 21 units, 11 models, 8 brands | [Loeb 2016, Anesth Analg](https://doi.org/10.1213/ane.0000000000001240) | A |
| Pitch at 100% SpO2 | 479-921 Hz across models | [Loeb 2016](https://doi.org/10.1213/ane.0000000000001240) | A |
| Pitch at 1% SpO2 | 38-404 Hz | [Loeb 2016](https://doi.org/10.1213/ane.0000000000001240) | A |
| Step type | Linear steps in 6 models, logarithmic in 6; only 6 models lowered pitch at every 1% drop; 5 stopped lowering below a threshold | [Loeb 2016](https://doi.org/10.1213/ane.0000000000001240) | A |
| Lab example | 99% = 648 Hz, 98% = 630 Hz (step 18 Hz, about 0.49 semitone); 100 ms pure-tone beeps at 80 dB SPL, 75 per minute | [Stevenson 2013, PMC3689317](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/) | A |
| Detection | Visual workload and OR noise cut detection of the 99%-to-98% change, up to 17% worse | [Stevenson 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/) | A |
| Enhanced displays | Detecting a move into or out of the target range: 87% with an enhanced display vs 57% with the standard one | [Paterson 2019, Anesth Analg](https://doi.org/10.1213/ANE.0000000000004267) | A |
| Generic monitor beep in a research soundscape | About 1450 Hz fundamental, 200 ms | [Ribeiro Ferreira 2023, PMC9934403](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/) | A |

Game implementation (design, derived from the lab values):
- One beep per detected pulse, synced to the same heart clock as the ECG and the 3-D heart.
- `f(SpO2) = 648 Hz * (630/648)^(99 - SpO2)`. This gives about 667 Hz at 100%, about 503 Hz at 90%, and about 379 Hz at 80%. These sit inside the real-device ranges ([Loeb 2016](https://doi.org/10.1213/ane.0000000000001240)).
- Option: an "enhanced" mode with extra cues (for example tremolo below the target range) as a teaching aid ([Paterson 2019](https://doi.org/10.1213/ANE.0000000000004267)). The exact enhancement design was not read this run (uncertain).
- Fun detail: the finger probe glows red because it uses a 660 nm red LED and a 940 nm infrared LED ([Pulse oximetry](https://en.wikipedia.org/wiki/Pulse_oximetry)). Only the red one is visible.

### 4.2 IEC 60601-1-8 alarm sounds

| Fact | Value | Source | Grade |
|---|---|---|---|
| Standard edition referenced | IEC 60601-1-8:2006/AMD1:2012/AMD2:2020; a 4th edition is in development | [Edworthy 2025, PMC12106860](https://pmc.ncbi.nlm.nih.gov/articles/PMC12106860/) | A |
| Pulse counts | Three pulses for cautionary (medium) and five for emergency (high) | [Edworthy 2013 review, PMC3628049](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/) | A |
| HP burst (as used from the 2020 supporting material) | Two identical five-pulse blocks separated by 190 ms, 1110 ms in total; 50 ms pulses; 5 ms rise/fall; harmonics 440, 880, 1320, 1760, 2200 Hz | [Ribeiro Ferreira 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/) | A |
| MP burst | 595 ms total; 155 ms pulses; 10 ms rise/fall; harmonics 220-1100 Hz. (3 x 155 ms + 2 x 65 ms = 595 ms, which fits three pulses) | [Ribeiro Ferreira 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/) | A (pulse count derived) |
| Spectrum | Five spectral peaks within 150-4000 Hz, as the standard suggests | [Ribeiro Ferreira 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/) | A |
| LP | 1-2 pulses (not verified this run: uncertain) | none fetched | C |
| Old melodic alarms | Short three-tone melodies with shared contours; hard to learn. Only 1 of 22 critical-care nurses (4.5%) reached 100% accuracy after two training sessions | [Edworthy 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/), [Wee & Sanderson 2008](https://pubmed.ncbi.nlm.nih.gov/18227306/) | A |
| Auditory icons (2020) | "Real-world (or stylised real-world)" sounds. Examples used in the study: breathing in and out (respiratory), short pitched bubbling pulses (SpO2), a power saw that fails to start (technical) | [Edworthy 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12106860/) | A |
| Icons vs tones | Simulated ICU: about 88% vs 43% correct; about 12 s vs 15 s to respond | [McNeer 2018, Anesthesiology](https://doi.org/10.1097/ALN.0000000000002234) | A |
| Concurrent alarms | Icons also easier to tell apart when two alarms sound at once (66 participants) | [Edworthy 2022, Appl Ergon](https://doi.org/10.1016/j.apergo.2021.103609) | A |
| Masking | Reserved alarm sounds can mask each other at all three priorities | [Bolton 2022, Hum Factors](https://doi.org/10.1177/0018720820967596) | A |
| False alarms | 85-99% of cardiopulmonary monitor alarms are false (Talley 2011, cited in review) | [Edworthy 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/) | A (secondary citation) |
| Full icon category list | Commonly listed as general, cardiovascular (heartbeat-like), artificial perfusion, ventilation, oxygen, temperature/energy delivery, drug/fluid delivery, power failure. The full list and exact icons were not verified this run (uncertain). | none fetched | C |

Game implementation:
- Synthesize alarms in-engine (no licence issue). Build pulses from the harmonic recipe above. Use MetaSounds in UE, which gives sample-accurate control in a DSP graph ([MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine)), or a small custom synth in other engines.
- Settings toggle: "Classic tonal (2006/2012)" vs "Auditory icons (2020)". Record or design the icons yourself, guided by the published descriptions.
- Add realistic false alarms (for example a probe-off SpO2 alarm). This teaches alarm fatigue without being unfair. Use a low rate so the game stays playable.

### 4.3 Heart-lung machine and field sounds

| Sound | Evidence | Design |
|---|---|---|
| Roller pump | Peristaltic (roller) pumps are cheaper and can over-pressurise if lines clamp or kink ([CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)). | Rhythmic "whirr-thump" whose rate tracks the pump RPM. Over-pressure gives a strain sound plus an alarm. |
| Centrifugal pump | Common in modern circuits; flow set by RPM ([CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)). | Smooth hum whose pitch follows RPM. |
| HLM safety alarms | Level detectors, bubble detectors, arterial line filter, pressure transducers; pressure controllers, air detectors and low-level alarms are standard console features ([EACTS 2019](https://academic.oup.com/ejcts/article/57/2/210/5579397)). | Distinct alarms for low reservoir level, air in line and high line pressure. |
| Heater-cooler | A heat exchanger warms and cools blood using water baths ([CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)). | Background fan and pump noise. |
| Sternal saw | No source with sound levels found (uncertain). | Short, loud, high-pitched buzz with a pitch drop when loaded by bone. Record a hobby oscillating saw on a bone (for example from a butcher) for a realistic layer. |
| Electrosurgery | Cut vs coag waveforms ([Electrosurgery](https://en.wikipedia.org/wiki/Electrosurgery)). Distinct activation tones for cut and coag are typical, not verified this run (uncertain). | Activation tone plus tissue sizzle; coag sizzle crackles more. |
| Suction and smoke evacuator | Smoke evacuators are noisy ([Surgical smoke](https://en.wikipedia.org/wiki/Surgical_smoke)). | Gurgle that changes with fluid vs air; louder when the tip is in air. |
| Ventilator | Not covered this run. | Cyclic bellows sound; stops when ventilation is paused on bypass (uncertain). |

### 4.4 Staff call-outs and communication

- Closed-loop communication, where the receiver repeats the message back, reduces misunderstanding; teamwork and briefings reduce errors ([EACTS/EACTA/EBCP 2019](https://academic.oup.com/ejcts/article/57/2/210/5579397); [Wahr 2013](https://doi.org/10.1161/CIR.0b013e3182a38efa)).
- Use voice lines in sender, read-back, confirm form, for example "Going on bypass" / "On bypass, full flow" / "Cross-clamp on" / "Cardioplegia going in". Exact phrasing varies by centre; the procedure topic (01) and physiology topic (02) should own the event list.
- Use text-to-speech or record friends. Avoid copying real recordings from videos.

### 4.5 Room acoustics and mix

| Fact | Value | Source |
|---|---|---|
| Background noise in a recorded cardiac OR (no alarms) | Average 67 dB SPL, range 58-86 dB SPL | [Stevenson 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/) |
| Literature OR average and peaks | About 77 dB; peaks can pass 100 dB | [Stevenson 2013 (citing others)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/) |
| OR room volume | 71.2-196.4 m³ (mean 131.1) in 40 ORs; larger rooms had worse speech intelligibility; more equipment improved it | [McNeer 2017, Anesth Analg](https://doi.org/10.1213/ane.0000000000002118) |
| Alarm and beep loudness in one study | About 74 dB(A) for stimuli | [Ribeiro Ferreira 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/) |

Mix guidance (design): bed (HVAC, machines) at about -20 dB relative to alarms; beep and alarms always audible; call-outs ducked against the saw. Use a short reverb sized for about 130 m³ ([McNeer 2017](https://doi.org/10.1213/ane.0000000000002118)).

### 4.6 Spatial audio middleware

| Option | Licence / version | Notes | Source |
|---|---|---|---|
| Steam Audio | Apache-2.0; v4.8.1 | Plugins for Unity 2017.3+, UE 4.27+, FMOD Studio 2.0+, Wwise 2023.1+ | [GitHub](https://github.com/ValveSoftware/steam-audio) |
| UE MetaSounds | Part of UE | DSP graph, sample-accurate, gameplay parameters | [Epic docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine) |
| FMOD / Wwise | UNVERIFIED (licence pages could not be fetched) | Free indie tiers exist but terms were not checked this run | n/a |

### 4.7 Sound sources and licences

| Source | Licence | Personal / non-commercial? | Attribution / share-alike / other | Source |
|---|---|---|---|---|
| Freesound | Per sound: CC0, CC BY 4.0, CC BY-NC 4.0, or retired Sampling+ | Yes (NC sounds: no money may be earned) | BY needs credit; check each file | [Freesound FAQ](https://freesound.org/help/faq/) |
| Sonniss GDC Game Audio Bundle | Royalty-free, commercial use allowed | Yes | No attribution; AI/ML training is prohibited; latest archived bundle is GDC 2024 | [Sonniss](https://sonniss.com/gameaudiogdc) |
| Pixabay | Pixabay Content License | Yes | No attribution; no standalone redistribution | [Pixabay](https://pixabay.com/service/license-summary/) |
| BBC Sound Effects (RemArc) | UNVERIFIED (site blocked from this session) | Believed personal/educational/research only (uncertain) | Check before use | n/a |
| Stable Audio Open 1.0 (AI) | Stability AI Community License; free under USD 1M annual revenue | Yes | Up to 47 s stereo at 44.1 kHz; trained on Freesound and FMA audio under CC0, CC BY or CC Sampling+ | [Model card](https://huggingface.co/stabilityai/stable-audio-open-1.0), [Licence](https://stability.ai/license) |
| Own recordings / synthesis | Yours | Yes | Best option for alarms, tones and call-outs | n/a |

---

## 5. Legitimate educational reference sources (reference only, do not ship)

| Source | What it gives | Terms | Source |
|---|---|---|---|
| YouTube surgical channels | Real operative footage for colour, motion and sound reference | You may view or listen for personal, non-commercial use; downloading or reproducing is not allowed unless the service expressly authorises it or YouTube gives written permission. Terms dated and effective 2023-12-15. | [YouTube Terms](https://www.youtube.com/t/terms) |
| CTSNet (cardiothoracic surgery network) | Large peer-reviewed video library | UNVERIFIED (terms page returned 403) | n/a |
| MMCTS (EACTS Multimedia Manual of Cardio-Thoracic Surgery) | Step-by-step videos, for example median sternotomy | Subscription required for the sternotomy chapter per Europe PMC | [Reser 2015](https://doi.org/10.1093/mmcts/mmv017) |
| ASE/EACVI chamber quantification guideline | Normal values for motion and size | Free PDF; use the numbers, do not copy figures | [ASE/EACVI 2015](https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf) |
| Visible Human Project | CT (512x512, 1 mm), MRI, colour cryosections (male 2048x1216, 0.33 mm pixels, 1,871 sections) | No licence needed since 2019; described as a public-domain library | [NLM](https://www.nlm.nih.gov/research/visible/visible_human.html) |
| Animal hearts from a butcher | Real tissue for colour, gloss and photogrammetry | Pig hearts differ from human: "Valentine" shape vs human trapezoid, tubular right atrial appendage, 2 vs 4 pulmonary vein openings, coarser trabeculations | [Crick 1998, J Anat](https://pmc.ncbi.nlm.nih.gov/articles/PMC1467827/) |

Rules for the project:
1. Keep a `reference/` folder outside the repository build. Never commit downloaded videos or screenshots.
2. Write down measurements and notes ("LAD sits in fat, glossy film over muscle") rather than copying images.
3. Facts and numbers can be reused; images, footage and text cannot.

---

## 6. High realism on a solo-developer budget

### 6.1 Pipeline that gives the most realism per hour

| Step | Tool (licence, version) | Why | Source |
|---|---|---|---|
| 1. Base anatomy | BodyParts3D (CC BY 4.0; licence page updated 2025-02-27) or Z-Anatomy (.blend/FBX, CC BY-SA 4.0) | Correct proportions and part names | [BodyParts3D](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html), [Z-Anatomy](https://github.com/LluisV/Z-Anatomy) |
| 1b. Whole-body reference organs | HuBMAP CCF 3D Reference Object Library (CC BY 4.0, GLB, V1.2; heart content not confirmed: uncertain) | Consistent organ placement in the chest | [HuBMAP CCF](https://github.com/hubmapconsortium/ccf-3d-reference-object-library) |
| 1c. Patient-specific shapes | 3D Slicer (BSD-style, "does not impose restrictions") + TotalSegmentator (Apache-2.0 code; heart chambers and coronary arteries need a free academic non-commercial licence) on public CT | Real variation between patients | [3D Slicer](https://www.slicer.org/), [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |
| 2. Sculpt and retopologise | Blender 5.2.3 LTS (released 2026-10-22; 5.3 expected 2026-11-10). GPL; what you make is yours | Clean animation-ready mesh | [Blender download](https://www.blender.org/download/), [Blender licence](https://www.blender.org/about/license/) |
| 3. Real tissue capture | Photogrammetry of an animal heart: Meshroom (MPL-2.0) or COLMAP (new BSD) | Real micro-detail and colour | [Meshroom](https://github.com/alicevision/Meshroom), [COLMAP](https://colmap.github.io/license.html) |
| 3b. Shiny surfaces | Shiny, dark or clear surfaces cause gaps in photogrammetry; matte spray is a common workaround (not usable on tissue you want to photograph for colour). Use diffuse lighting and polarising filters (common practice, uncertain). | Wet tissue is very shiny | [Photogrammetry](https://en.wikipedia.org/wiki/Photogrammetry) |
| 4. Procedural texturing | Material Maker (MIT; Godot-based procedural textures and 3-D painting); Blender shader nodes | Infinite variation (fat lobules, vessels, char) | [Material Maker](https://github.com/RodZill4/material-maker) |
| 5. Props and room | Poly Haven (CC0) and ambientCG (CC0 1.0) | No attribution needed, any use | [Poly Haven](https://polyhaven.com/license), [ambientCG](https://docs.ambientcg.com/license/) |
| 6. Engine shading | See section 1.2 | | |

### 6.2 Licence quick-check for downloaded 3-D models

| Licence | Personal / non-commercial game | Conditions | Source |
|---|---|---|---|
| CC0 | Yes | None (credit appreciated) | [Poly Haven](https://polyhaven.com/license) |
| CC BY 4.0 | Yes | Credit, link to licence, note changes | [CC deed (BY-NC-SA, BY part)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) |
| CC BY-SA 4.0 | Yes | Credit; your modified version must use the same licence | [CC deed](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) |
| CC BY-NC(-SA) 4.0 | Yes, if not "primarily intended for commercial advantage or monetary compensation" | Credit; plus SA if present | [CC deed](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) |
| CC BY-ND 4.0 | View only, in practice | You may not distribute a modified version, and game use almost always modifies (format change alone does not) | [CC BY-ND deed](https://creativecommons.org/licenses/by-nd/4.0/deed.en) |
| Sketchfab Standard | Usually yes | No resale or standalone redistribution; credit needed in some audiovisual productions | [Sketchfab licences](https://sketchfab.com/licenses) |
| Sketchfab Editorial | Avoid | No commercial or promotional use; must not be altered except cropping | [Sketchfab licences](https://sketchfab.com/licenses) |
| Fab / Quixel | UNVERIFIED (EULA page returned 403) | Check before use | n/a |

### 6.3 AI-assisted tools

| Tool | Licence | Use it for | Limits | Source |
|---|---|---|---|---|
| TRELLIS (Microsoft) | MIT for models and most code; two submodules (diffoctreerast, modified Flexicubes) have their own licences | Fast image-to-3D draft props (instrument trays, clamps) | Needs an NVIDIA GPU with at least 16 GB; tested on Linux; latest listed update 2025-03-25 | [TRELLIS](https://github.com/microsoft/TRELLIS) |
| Hunyuan3D 2.x (Tencent) | Tencent Hunyuan 3D 2.0 Community License (2025-01-21) | Textured props; 2.1 (2025-06-13) adds PBR | Not licensed in the EU, UK or South Korea; licence needed above 1M monthly users; no using outputs to improve other AI models; AI content must be labelled; ban on unauthorised practice of medicine in the acceptable-use policy. 6 GB VRAM for shape, 16 GB for shape + texture | [Repo](https://github.com/Tencent-Hunyuan/Hunyuan3D-2), [LICENSE](https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/LICENSE) |
| 3D Gaussian Splatting (Inria reference code) | Non-commercial research/evaluation only | Capturing a real OR or animal-heart scene for reference viewing | Commercial use needs written consent; real-time rendering; training used over 20 GB GPU memory in the prototype | [Licence](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md), [Overview](https://en.wikipedia.org/wiki/Gaussian_splatting) |
| Stable Audio Open 1.0 | Stability AI Community License | Ambient beds, machine textures | Up to 47 s clips; free under USD 1M revenue | [Model card](https://huggingface.co/stabilityai/stable-audio-open-1.0), [Licence](https://stability.ai/license) |

Advice: use AI for props and ambience, not for the heart. The heart and coronary anatomy must be correct, so build them from scanned data and references (6.1).

### 6.4 Engines (cost only; choice is topic 04)

| Engine | Cost facts | Source |
|---|---|---|
| Unity 6 Personal | Free up to USD 200,000 revenue and funding; splash screen optional with Unity 6; runtime fee cancelled | [Unity pricing](https://unity.com/products/pricing-updates) |
| Godot 4.7 | MIT; content you make is yours; include Godot's licence notice when redistributing | [Godot licence](https://godotengine.org/license/) |
| Unreal Engine | UNVERIFIED this run (licence and EULA pages returned 403). Commonly cited: free to use, 5% royalty above USD 1M gross per product (uncertain). | n/a |

---

## Game hooks

| # | Finding | Mechanic / data / rule |
|---|---|---|
| 1 | Hb optics: oxy = bright red, deoxy = darker ([Blood](https://en.wikipedia.org/wiki/Blood)) | `Tissue.Oxygenation` (0-1) drives the colour LUT. Graft occlusion lowers it in one coronary territory; the player can spot ischaemia by colour and by weaker motion. |
| 2 | Tissue starts to die in 15-30 min without blood ([MI](https://en.wikipedia.org/wiki/Myocardial_infarction)) | Hidden ischaemia timer per territory; past the limit, a permanent "damage" mask and score penalty. Exact clock values come from topic 02. |
| 3 | Cardioplegia: cold, K+ arrest, asystole, heart cools to 15-20 °C ([Cardioplegia](https://en.wikipedia.org/wiki/Cardioplegia)) | State `Arrested`: deformer off, ECG flat line, `Temperature` lowers gloss. Redose reminders come from topic 02. |
| 4 | ACT > 480 s on CPB; protamine reverses ([CPB](https://en.wikipedia.org/wiki/Cardiopulmonary_bypass)) | `Anticoagulated` flag disables clot spawning. After protamine, clots form in pools; ongoing bleeding becomes a skill check. |
| 5 | Arterial vs venous blood colour ([Blood](https://en.wikipedia.org/wiki/Blood)) | Bleed type sets colour and behaviour: arterial spurts pulse with the ECG; venous oozes. CPB lines are visibly red (arterial) vs dark (venous). |
| 6 | Dried blood turns brown (methaemoglobin) ([Blood](https://en.wikipedia.org/wiki/Blood)) | `bloodAge` mask darkens and browns stains over the case; drapes tell the story of the operation. |
| 7 | Smoke can block the view ([Liu 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/)) | `FieldVisibility` drops with smoke and pooled blood; the assistant's suction or smoke evacuator restores it but adds noise. |
| 8 | Coag vs cut waveforms ([Electrosurgery](https://en.wikipedia.org/wiki/Electrosurgery)) | Two cautery modes with different char, smoke and sound; overuse adds char and damage. |
| 9 | Twist about 16 deg, coronary motion 10-26 mm ([Helle-Valle](https://pubmed.ncbi.nlm.nih.gov/16286606/), [Shechter](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/)) | Deformer parameters in a data file. Off-pump scenes need a stabiliser tool to keep the target vessel within a small motion window. |
| 10 | Heart volume changes only about 8% ([Carlsson](https://doi.org/10.1152/ajpheart.01125.2003)) | Validation test: automated check that the outer mesh volume change stays within 5-11%. |
| 11 | Systole about 0.3 s, diastole about 0.5 s at 75 bpm ([Diastole](https://en.wikipedia.org/wiki/Diastole)) | A single `HeartClock` drives ECG, beep, deformer, arterial bleeding and pressure waveform. |
| 12 | VF = quivering, coarse/fine ([VF](https://en.wikipedia.org/wiki/Ventricular_fibrillation)) | State `VF`: noise deformer + ECG noise with matching seed; coarse VF responds better to shocks (rule from the same source). |
| 13 | Surgical light 40-160 klux, recommended 50-100 klux; room 2,000-5,500 lux ([Surgical lighting](https://en.wikipedia.org/wiki/Surgical_lighting), [Hemphälä](https://api.crossref.org/works/10.1177/1477153520903355)) | Physical light units; light re-aiming task; badly aimed lamp creates a shadow that lowers `FieldVisibility`. |
| 14 | Loupes shrink field of view and depth of field ([Loupe](https://en.wikipedia.org/wiki/Loupe)) | Toggle loupe view for anastomosis; precision is higher but you see less of the field (miss a bleed elsewhere). |
| 15 | SpO2 pitch about 0.5 semitone per 1% ([Stevenson](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/)) | `f(SpO2)` formula in 4.1; "eyes-free" challenge mode where the player must notice desaturation by ear. |
| 16 | HP = 10 pulses, MP = 3 pulses ([Ribeiro Ferreira](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/), [Edworthy 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/)) | Alarm manager with priorities, latching, silencing (audio pause) and escalation. |
| 17 | Auditory icons are recognised better (88% vs 43%) ([McNeer 2018](https://doi.org/10.1097/ALN.0000000000002234)) | Settings toggle "Classic tones / Auditory icons"; tutorial teaches both. |
| 18 | 85-99% of monitor alarms are false ([Edworthy 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/)) | Occasional nuisance alarms (probe off, artefact) that the player must recognise and silence; score rewards correct triage. |
| 19 | Closed-loop communication reduces errors ([EACTS 2019](https://academic.oup.com/ejcts/article/57/2/210/5579397)) | Call-out system: player commands need read-back; skipping read-back raises an "error risk" value. |
| 20 | HLM alarms: level, bubble, pressure ([EACTS 2019](https://academic.oup.com/ejcts/article/57/2/210/5579397)) | Perfusion events (low reservoir, air in line) with distinct sounds; perfusionist voice lines. |
| 21 | OR noise 58-86 dB, peaks > 100 dB ([Stevenson](https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/)) | Dynamic mix: saw and suction mask the beep; an "OR discipline" option lowers background noise in critical phases. |

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | Substrate is enabled by default for new UE projects; upgraded UE 5.7+ projects stay on the legacy path unless switched | https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine | A |
| 2 | UE Subsurface Profile is screen-space, has no backscatter, and does not work in mobile (non-deferred) rendering | https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine | A |
| 3 | HDRP 17.0.4: SSS is skipped when Max Radius is smaller than a pixel; default world scale 1 unit = 1 m; dual-lobe Lobe Mix default 0.5 | https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/diffusion-profile-reference.html | A |
| 4 | Arterial blood about 98-99% saturated (bright red); venous about 75% (70-78%) (darker red) | https://en.wikipedia.org/wiki/Blood | B |
| 5 | Cardioplegia: K+ 16.2 mmol/L gives about -60 mV (inexcitable); cold fluid usually 4 °C; heart cools to about 15-20 °C | https://en.wikipedia.org/wiki/Cardioplegia | B |
| 6 | Heparin until ACT > 480 s before cannulation; protamine reverses it | https://en.wikipedia.org/wiki/Cardiopulmonary_bypass | B |
| 7 | Electrocautery smoke: about 95% water/steam; mean particle 0.07 µm; can block the surgeon's view | https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/ | A |
| 8 | Healthy human LV rotation by MRI tagging: apex -11.6 ± 3.8 deg, base 4.8 ± 1.7 deg | https://pubmed.ncbi.nlm.nih.gov/16286606/ | A |
| 9 | Coronary 3-D displacement per beat: LAD 9.6 mm, LCx 12.1 mm, RCA mid 26.3 mm; respiration 5-7 mm | https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/ | A |
| 10 | Total heart volume falls only about 8.2% in systole | https://doi.org/10.1152/ajpheart.01125.2003 | A |
| 11 | TAPSE 24 ± 3.5 mm (abnormal < 17 mm); GLS about -20%; LVEF 52-72% (men) and 54-74% (women) | https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf | A |
| 12 | At 75 bpm: cycle about 0.8 s, systole about 0.3 s, diastole about 0.5 s | https://en.wikipedia.org/wiki/Diastole | B |
| 13 | Surgical luminaire central illuminance 40,000-160,000 lux; Ra 85-100 (IEC 60601-2-41 summary) | https://en.wikipedia.org/wiki/Surgical_lighting | B |
| 14 | Measured LED surgical lights: 25-160 klux, field 109-300 mm | https://doi.org/10.1177/1553350609353766 | A |
| 15 | Recommended: central beam 50,000-100,000 lux; general 2,000 / 4,000 / 5,500 lux | https://api.crossref.org/works/10.1177/1477153520903355 | A |
| 16 | Commercial oximeters: 479-921 Hz at 100% SpO2; only 6 of 11 models lower pitch at every 1% drop | https://doi.org/10.1213/ane.0000000000001240 | A |
| 17 | Lab oximeter tones: 648 Hz (99%) vs 630 Hz (98%); cardiac OR noise 67 dB SPL (58-86) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/ | A |
| 18 | IEC HP pulse pattern: two 5-pulse blocks, 1110 ms; MP burst 595 ms with 155 ms pulses | https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/ | A |
| 19 | IEC 60601-1-8 uses three pulses (cautionary) and five (emergency) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/ | A |
| 20 | IEC 60601-1-8:2006/AMD1:2012/AMD2:2020 recommends auditory icons; examples include breathing, bubbling and a power saw failing to start | https://pmc.ncbi.nlm.nih.gov/articles/PMC12106860/ | A |
| 21 | Auditory icons identified about 88% vs 43% for standard alarms, faster (about 12 vs 15 s) | https://doi.org/10.1097/ALN.0000000000002234 | A |
| 22 | OR volumes 71.2-196.4 m³; larger rooms have worse speech intelligibility | https://doi.org/10.1213/ane.0000000000002118 | A |
| 23 | Steam Audio is Apache-2.0, v4.8.1, with Unity, UE, FMOD and Wwise plugins | https://github.com/ValveSoftware/steam-audio | A |
| 24 | BodyParts3D is now CC BY 4.0 (licence page updated 2025-02-27) | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html | A |
| 25 | Visible Human data need no licence since 2019 | https://www.nlm.nih.gov/research/visible/visible_human.html | A |
| 26 | Hunyuan3D 2.0 community licence excludes EU, UK and South Korea | https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/LICENSE | A |
| 27 | Inria Gaussian Splatting code: non-commercial research and evaluation only | https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md | A |
| 28 | Blender 5.2.3 LTS released 2026-10-22; Blender output belongs to the user | https://www.blender.org/download/ and https://www.blender.org/about/license/ | A |
| 29 | YouTube allows viewing for personal non-commercial use only; downloading only if expressly authorised (terms 2023-12-15) | https://www.youtube.com/t/terms | A |
| 30 | Closed-loop communication reduces misunderstanding; HLM safety features include level and bubble detectors | https://academic.oup.com/ejcts/article/57/2/210/5579397 | A |

---

## Sources

1. Epic Games - Overview of Substrate Materials - https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine - Substrate features, defaults, limits.
2. Epic Games - Subsurface Profile Shading Model - https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine - SSS parameters and limits.
3. Unity - HDRP 17.0 Diffusion Profile reference - https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/diffusion-profile-reference.html - HDRP SSS settings.
4. Godot 4.7 docs - BaseMaterial3D - https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html - Godot SSS and clearcoat.
5. Blender 5.2 LTS Manual - Principled BSDF - https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html - SSS methods, coat, sheen.
6. Blender - License - https://www.blender.org/about/license/ - GPL; output belongs to the user.
7. Blender - Download - https://www.blender.org/download/ - version 5.2.3 LTS, 2026-10-22.
8. Godot - License - https://godotengine.org/license/ - MIT.
9. Unity - Pricing updates - https://unity.com/products/pricing-updates - Personal tier USD 200k; runtime fee cancelled.
10. Epic Games - MetaSounds - https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine - procedural DSP audio.
11. Prahl S. - Optical absorption of hemoglobin (OMLC) - https://omlc.org/spectra/hemoglobin/ - Hb spectra for colour LUT.
12. Jacques SL. Optical properties of biological tissues: a review (2013) - https://pubmed.ncbi.nlm.nih.gov/23666068/ - tissue optics basis.
13. Wikipedia - Blood - https://en.wikipedia.org/wiki/Blood - arterial/venous colour and saturation, methaemoglobin.
14. Wikipedia - Cardioplegia - https://en.wikipedia.org/wiki/Cardioplegia - K+ arrest, temperatures.
15. Wikipedia - Cardiopulmonary bypass - https://en.wikipedia.org/wiki/Cardiopulmonary_bypass - pumps, ACT > 480 s, components.
16. Wikipedia - Coronary artery bypass surgery - https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery - step order, stay sutures, arrest within minutes.
17. Wikipedia - Electrosurgery - https://en.wikipedia.org/wiki/Electrosurgery - frequencies, waveforms, 400 °C vapour.
18. Wikipedia - Surgical smoke - https://en.wikipedia.org/wiki/Surgical_smoke - smoke, evacuator noise.
19. Liu Y et al. J Cancer 2019 (PMC6584931) - https://pmc.ncbi.nlm.nih.gov/articles/PMC6584931/ - smoke composition and particle sizes.
20. Wikipedia - Myocardial infarction - https://en.wikipedia.org/wiki/Myocardial_infarction - 15-30 min injury, scar.
21. Helle-Valle T et al. Circulation 2005 - https://pubmed.ncbi.nlm.nih.gov/16286606/ - LV rotation by MRI tagging.
22. Sengupta PP et al. JACC Cardiovasc Imaging 2008 - https://pubmed.ncbi.nlm.nih.gov/19356451/ - twist mechanics.
23. Nakatani S. J Cardiovasc Ultrasound 2011 (PMC3079077) - https://pmc.ncbi.nlm.nih.gov/articles/PMC3079077/ - rotation directions, untwisting timing.
24. Shechter G et al. IEEE Trans Med Imaging 2006 (PMC2396264) - https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264/ - coronary displacement and velocity.
25. Carlsson M et al. Am J Physiol 2004 - https://doi.org/10.1152/ajpheart.01125.2003 - total heart volume variation.
26. Lang RM et al. ASE/EACVI chamber quantification 2015 - https://academic.oup.com/ehjcimaging/article-pdf/16/3/233/16851324/jev014.pdf - TAPSE, GLS, LVEF.
27. Wikipedia - Diastole - https://en.wikipedia.org/wiki/Diastole - 0.3 s / 0.5 s at 75 bpm.
28. Wikipedia - QT interval - https://en.wikipedia.org/wiki/QT_interval - QT rate rule.
29. Wikipedia - Cardiac cycle - https://en.wikipedia.org/wiki/Cardiac_cycle - ECG to mechanics.
30. Wikipedia - Ventricular fibrillation - https://en.wikipedia.org/wiki/Ventricular_fibrillation - VF appearance.
31. Dosdall DJ et al. Annu Rev Biomed Eng 2010 (PMC3984906) - https://pmc.ncbi.nlm.nih.gov/articles/PMC3984906/ - VF wavefronts.
32. Wikipedia - Speckle tracking echocardiography - https://en.wikipedia.org/wiki/Speckle_tracking_echocardiography - 15% to 40% thickening.
33. Wikipedia - Pericardium - https://en.wikipedia.org/wiki/Pericardium - layers.
34. Wikipedia - Epicardial adipose tissue - https://en.wikipedia.org/wiki/Epicardial_adipose_tissue - epicardial fat definition.
35. Wikipedia - Surgical lighting - https://en.wikipedia.org/wiki/Surgical_lighting - IEC 60601-2-41 summary.
36. Wikipedia (de) - Operationsleuchte - https://de.wikipedia.org/wiki/Operationsleuchte - 160,000 lux maximum.
37. Knulst AJ et al. Surg Innov 2009 - https://doi.org/10.1177/1553350609353766 - LED light measurements.
38. Hemphälä H et al. Lighting Res Technol 2020 - https://api.crossref.org/works/10.1177/1477153520903355 - lighting recommendations.
39. Getinge - Maquet PowerLED II - https://www.getinge.com/int/products/maquet-powerled-ii/ - light field 13-27 cm, ambient colour.
40. Wikipedia - Operating theater - https://en.wikipedia.org/wiki/Operating_theater - team and sterile distances.
41. Wikipedia - Loupe - https://en.wikipedia.org/wiki/Loupe - magnification vs field of view.
42. Wikipedia - Median sternotomy - https://en.wikipedia.org/wiki/Median_sternotomy - incision and saw.
43. Reser D et al. MMCTS 2015 - https://doi.org/10.1093/mmcts/mmv017 - sternotomy key steps.
44. Wahr JA et al. AHA statement, Circulation 2013 - https://doi.org/10.1161/CIR.0b013e3182a38efa - cardiac OR human factors.
45. Wahba A et al. 2019 EACTS/EACTA/EBCP CPB guideline - https://academic.oup.com/ejcts/article/57/2/210/5579397 - communication, HLM safety.
46. Loeb RG et al. Anesth Analg 2016 - https://doi.org/10.1213/ane.0000000000001240 - oximeter sonification survey.
47. Stevenson RA et al. Anesthesiology 2013 (PMC3689317) - https://pmc.ncbi.nlm.nih.gov/articles/PMC3689317/ - tone frequencies, OR noise.
48. Paterson E et al. Anesth Analg 2019 - https://doi.org/10.1213/ANE.0000000000004267 - enhanced oximeter displays.
49. Ribeiro Ferreira V et al. PLoS One 2023 (PMC9934403) - https://pmc.ncbi.nlm.nih.gov/articles/PMC9934403/ - IEC priority pulse specs.
50. Edworthy J. JAMIA 2013 (PMC3628049) - https://pmc.ncbi.nlm.nih.gov/articles/PMC3628049/ - alarm review, pulse counts, false alarm rates.
51. Edworthy JR et al. Br J Anaesth 2025 (PMC12106860) - https://pmc.ncbi.nlm.nih.gov/articles/PMC12106860/ - auditory icons, standard edition.
52. McNeer RR et al. Anesthesiology 2018 - https://doi.org/10.1097/ALN.0000000000002234 - icons vs melodic alarms.
53. Edworthy J et al. Hum Factors 2017 - https://doi.org/10.1177/0018720817712004 - alarm redesign benchmarking.
54. Edworthy JR et al. Appl Ergon 2022 - https://doi.org/10.1016/j.apergo.2021.103609 - concurrent alarms.
55. Wee AN, Sanderson PM. Anesth Analg 2008 - https://pubmed.ncbi.nlm.nih.gov/18227306/ - melodic alarm learnability.
56. Bolton ML et al. Hum Factors 2022 - https://doi.org/10.1177/0018720820967596 - alarm masking.
57. McNeer RR et al. Anesth Analg 2017 - https://doi.org/10.1213/ane.0000000000002118 - OR acoustics and room volume.
58. Wikipedia - Pulse oximetry - https://en.wikipedia.org/wiki/Pulse_oximetry - 660/940 nm LEDs.
59. Valve - Steam Audio - https://github.com/ValveSoftware/steam-audio - spatial audio licence and version.
60. Freesound - FAQ - https://freesound.org/help/faq/ - sound licences.
61. Sonniss - GDC Game Audio Bundle - https://sonniss.com/gameaudiogdc - licence terms.
62. Pixabay - License summary - https://pixabay.com/service/license-summary/ - licence terms.
63. Stability AI - Stable Audio Open 1.0 model card - https://huggingface.co/stabilityai/stable-audio-open-1.0 - specs and data.
64. Stability AI - Licence - https://stability.ai/license - USD 1M threshold.
65. Poly Haven - License - https://polyhaven.com/license - CC0.
66. ambientCG - License - https://docs.ambientcg.com/license/ - CC0 1.0.
67. Sketchfab - Licenses - https://sketchfab.com/licenses - Standard and Editorial terms.
68. Creative Commons - BY-NC-SA 4.0 deed - https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en - BY, NC, SA definitions.
69. Creative Commons - BY-ND 4.0 deed - https://creativecommons.org/licenses/by-nd/4.0/deed.en - no-derivatives rule.
70. NLM - Visible Human Project - https://www.nlm.nih.gov/research/visible/visible_human.html - data and access.
71. DBCLS - BodyParts3D licence - https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html - CC BY 4.0.
72. Z-Anatomy - GitHub - https://github.com/LluisV/Z-Anatomy - CC BY-SA 4.0.
73. HuBMAP - CCF 3D Reference Object Library - https://github.com/hubmapconsortium/ccf-3d-reference-object-library - CC BY 4.0, GLB.
74. TotalSegmentator - GitHub - https://github.com/wasserth/TotalSegmentator - licences per task.
75. 3D Slicer - https://www.slicer.org/ - BSD-style licence.
76. AliceVision - Meshroom - https://github.com/alicevision/Meshroom - MPL-2.0.
77. COLMAP - License - https://colmap.github.io/license.html - new BSD.
78. Inria - Gaussian Splatting licence - https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md - non-commercial.
79. Wikipedia - Gaussian splatting - https://en.wikipedia.org/wiki/Gaussian_splatting - method overview.
80. Wikipedia - Photogrammetry - https://en.wikipedia.org/wiki/Photogrammetry - shiny-surface limits.
81. Microsoft - TRELLIS - https://github.com/microsoft/TRELLIS - MIT, GPU needs.
82. Tencent - Hunyuan3D-2 repo and LICENSE - https://github.com/Tencent-Hunyuan/Hunyuan3D-2 and https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/LICENSE - licence and territory.
83. Material Maker - GitHub - https://github.com/RodZill4/material-maker - MIT.
84. YouTube - Terms of Service - https://www.youtube.com/t/terms - viewing and download rules.
85. Crick SJ et al. J Anat 1998 (PMC1467827) - https://pmc.ncbi.nlm.nih.gov/articles/PMC1467827/ - pig vs human heart anatomy.
86. Wikipedia - Defibrillation - https://en.wikipedia.org/wiki/Defibrillation - internal paddles touch the myocardium.

Pages that could not be fetched this run (licences or facts remain UNVERIFIED): Unreal Engine licence and EULA (403), Fab EULA (403), FMOD licensing (empty page), Wwise pricing (403), CTSNet terms (403), BBC Sound Effects licensing (blocked host), RealityScan licence (no licence text), NCBI Bookshelf/StatPearls (captcha), photonics.com articles (403), Dräger product page (403).

---

## Summary

**Key findings**
1. Tissue realism comes from three things: SSS (blood and fat glow), a wet second specular lobe or coat, and correct haemoglobin-based colour changes. All three target engines support these (UE Substrate/Subsurface Profile, HDRP 17 Diffusion Profile, Godot 4.7 SSS skin mode), and Blender 5.2 LTS can author and preview them.
2. Real heart motion is subtle in volume (about 8%) but strong in twist (about 16 deg net) and long-axis shortening. Surface points move about 10 mm (LAD region) to 26 mm (RCA groove) per beat. These numbers can drive and test a deformer.
3. The OR is very bright at the field (40-160 klux by standard; 50-100 klux recommended) and much darker around it (2,000-5,500 lux). Exposure and light aiming are part of realism and gameplay.
4. The SpO2 tone and IEC alarms are the defining OR sounds. Their patterns are documented well enough to synthesise in-engine with no licence risk: HP = two 5-pulse blocks, MP = 3 pulses, about 0.5 semitone per 1% SpO2. The 2020 amendment adds auditory icons, which work better in studies.
5. The solo-developer route is scanned anatomy (BodyParts3D CC BY 4.0, Z-Anatomy CC BY-SA 4.0, Visible Human), Blender, CC0 props, photogrammetry of an animal heart (Meshroom/COLMAP), and synthesis for alarms. AI 3-D tools are fine for props but carry licence traps (Hunyuan3D territory rules, Inria non-commercial code).

**Recommendations**
- Build one shared `TissueState` data model (oxygenation, blood volume, temperature, wetness, blood age, char, scar) and one `HeartClock`. Both feed visuals and audio in sync.
- Put all motion numbers (twist, displacement, timing) in a data file with source links, and add automated tests (volume change 5-11%, LAD path about 10 mm).
- Synthesise all monitor and alarm sounds; record or license only foley (saw, suction, cautery sizzle). Prefer CC0 and Sonniss; track every CC BY credit in a credits file.
- Use photometric lighting with values from section 3.1, and expose a light-aiming mechanic.
- Treat all videos (YouTube, CTSNet, MMCTS) as reference only. Never store them in the repository.

**Open questions (need a follow-up run with search budget)**
- Exact IEC 60601-2-41 colour temperature range (3,000-6,700 K?) and irradiance limit.
- IEC 60601-1-8 low-priority pattern, and the full 2020 auditory-icon category list (is the cardiac icon a heartbeat?).
- Loupe magnification and working distance typical in cardiac surgery (2.5x-4.5x?) and headlight lux.
- VF dominant frequency in humans, internal defibrillation energy, and the incidence of VF after cross-clamp removal.
- Typical OR team positions for cardiac surgery from a textbook or society source.
- LV long-axis (MAPSE) normal value and ventilated (open-chest) respiratory heart motion.
- Unreal Engine, Fab, FMOD, Wwise, BBC Sound Effects and CTSNet licence terms (pages blocked this run).
- Visual appearance of the arrested heart with crystalloid vs blood cardioplegia (ideally from intraoperative imaging or hyperspectral papers).
