# Research index — proposal 0e97de96

Fresh research (re-do, new web searches), 2026-11-03. One report per topic. Each report ends with a *Key claims and evidence* table and a numbered *Sources* list.

| # | Report | Sources cited (agent count) | Lines |
|---|---|---|---|
| 01 | [01-surgical-procedure.md](01-surgical-procedure.md) | 54 | 559 |
| 02 | [02-physiology-anesthesia-perfusion.md](02-physiology-anesthesia-perfusion.md) | 68 | 649 |
| 03 | [03-assets-licensing.md](03-assets-licensing.md) | 98 | 550 |
| 04 | [04-engine-simulation-tech.md](04-engine-simulation-tech.md) | 84 | 514 |
| 05 | [05-visual-audio-realism.md](05-visual-audio-realism.md) | n/a | 565 |
| 06 | [06-game-design-benchmarks.md](06-game-design-benchmarks.md) | 70 | 633 |
| 07 | [07-production-tools-validation.md](07-production-tools-validation.md) | 89 | 528 |
| 08 | [08-patients-complications-crisis.md](08-patients-complications-crisis.md) | 57 | 682 |
| 09 | [09-anatomy-biomechanics-data.md](09-anatomy-biomechanics-data.md) | 70 | 673 |

Report 05's agent hit the usage limit after it saved the file, so 05 has no structured summary here. Its key findings and open questions are at the end of the report itself.

## 01 — The real open heart operation, step by step

**Key findings**

- On-pump isolated CABG is the best v1. The STS database recorded 161,907 isolated CABG in 2023, 11.5% of them off-pump. By comparison there are about 22,000 isolated SAVR a year (178,014 from July 2014 to June 2022) and 17,907 isolated mitral operations (2016).
- The report maps a complete ordered CABG step list from room entry to ICU transfer: Phases A-G, about 45 steps. Each step lists who does it, tools and sutures, success criteria and typical errors. Durations not backed by a source are marked as estimates.
- Anticoagulation: heparin about 300 IU/kg. Go on bypass only when ACT is above 480 s, or above 400 s with maximal-activation devices. Heparin resistance appeared in 6 of 100 patients (ACT below 350 s after 300 IU/kg). Sources: STS/SCA/AmSECT 2018 and 2024 EACTS/EACTAIC/EBCP.
- Pump targets from the 2024 EACTS/EACTAIC/EBCP guideline: flow 2.2-2.8 L/min/m2; oxygen delivery above about 270-300 mL/min/m2; transfuse if Hb is below 6.0 g/dL; HCT 21-24% is acceptable if oxygen delivery is above 273; systolic pressure below 100 mmHg during aortic cannulation.
- Temperature rules from STS 2015: arterial outlet below 37 C; arterial-venous gradient at most 10 C; once the outlet is at or above 30 C, rewarm at most 0.5 C/min with a gradient of at most 4 C.
- Cardioplegia: antegrade at 60-100 mmHg. Retrograde at 200-400 mL/min with coronary sinus pressure 30-50 mmHg. Cold blood (Buckberg 4:1 at 4 C) is redosed every 15-30 min, with a warm 37 C 'hot shot' of about 500 mL before unclamping. The del Nido alternative is 20 mL/kg (max 1000 mL), given once and good for up to about 90 min.
- Graft flow check (transit-time flowmetry): a graft is likely patent if mean flow is above 15 mL/min, pulsatility index below 5, diastolic filling above 50% and reverse flow below 4%. Stricter thresholds are flow above 20, PI below 3 and reverse flow below 3%. 2018 ESC/EACTS rates graft flow measurement Class IIa, level B.
- Reversal: keep the protamine-to-heparin ratio below 1.0 (2024 EACTS) and never above 2.6 mg per 100 U (STS 2018). Defibrillation after unclamping: open-chest 10-30 J, with 20 J used in the CALS-ANZ protocol.
- Real timings: 3-graft on-pump CABG has median skin-to-skin 240 min, bypass time 112 min and cross-clamp 65 min. A multicentre cohort reported mean cross-clamp 58 min and mean bypass time 77 min. Isolated SAVR (STS) has median bypass time 90-96 min and cross-clamp 68-72 min. A Swiss timing study broke SAVR cross-clamp into 5 sub-steps, with suturing plus tying taking 51% of clamp time.
- Communication: a structured protocol around 8 critical bypass events cut communication breakdowns from 11.5 to 7.3 per case. AmSECT 2023 makes a checklist for every bypass case a standard (with set-up, weaning and post-bypass checklists in its appendix) and recommends closed-loop communication.
- SAVR differs from CABG mainly inside the cross-clamp phase: aortotomy, leaflet excision, decalcification and sizing, about 15 pledgeted 2-0 sutures, tying, aortotomy closure. It reuses about 75% of the CABG pipeline.
- Mitral repair adds bicaval cannulation, a left atriotomy through Sondergaard's groove, leaflet resection or ePTFE neochords, ring annuloplasty, a saline test and a TEE check for residual leak and SAM. STS repair techniques: annuloplasty 94.3%, resection 46.5%, artificial chords 22.7%. Operative mortality is 1.1% for repair vs 3.7% for replacement.

**Recommendations**

- Build v1 as a 3-graft on-pump CABG through a median sternotomy: LIMA to LAD, reversed vein to OM, reversed vein to RCA or PDA. Offer optional radial artery, endoscopic vs open vein harvest, and skeletonized vs pedicled LIMA as strategy choices.
- Put hard safety gates on critical steps: ACT at or above 480 before 'go on bypass'; systolic below 100 before aortic cannulation; ventilator on before weaning; suckers off before protamine.
- Model cardioplegia as two selectable modes (Buckberg intermittent cold blood with a redose timer; single-dose del Nido) and link missed redoses to an ischaemia meter, VF risk and weaning difficulty.
- Score every anastomosis through a suturing mini-game and turn quality into transit-time flow values (mean flow, PI, diastolic filling, reverse flow) shown after unclamping, with revise/accept choices.
- Implement closed-loop call-outs with required read-backs for the critical events: heparin, ACT, going on bypass, full flow / ventilation off, clamp on, cardioplegia, rewarm, clamp off, defibrillate, ventilate, coming off, protamine, decannulate. Track a 'communication breakdown' count in the debrief.
- Store all numeric targets (doses, pressures, flows, temperatures, times) in one data file, with the source URL and grade next to each value so they can be audited and tuned.
- Use real timings as par values: CABG cross-clamp about 58-65 min, bypass time about 77-112 min, skin-to-skin about 240 min; SAVR sub-step times from the Swiss study. Compare player times with these in the debrief.
- Sequence later content as v2 SAVR (highest reuse), v3 mitral repair, and off-pump CABG as a CABG 'hard mode'. Add the STS post-cardiac-surgery arrest protocol (3 shocks, resternotomy within 5 min) as an optional ICU scenario.

**Open questions**

- Exact aortic and two-stage venous cannula French sizes were not verified on manufacturer IFU or catalogue pages.
- Electrocautery power settings for sternotomy and LIMA takedown are UNVERIFIED. No authoritative source was found.
- Coronary arteriotomy length (4-6 mm teaching vs 3-4 mm patent text) and aortic punch sizes (4.0-4.8 mm) lack an A-grade source.
- Weaning numeric thresholds (core temperature above 36 C, K+ 4-5 mmol/L) come only from weak sources. The 2024 EACTS supplementary weaning checklist should be read directly.
- The 2024 ESC chronic coronary syndrome guideline may have replaced some 2018 ESC/EACTS CABG technique classes (skeletonization, flow measurement, vein harvest). Not confirmed.
- Exact 2023-2025 annual counts for isolated SAVR and mitral repair were not found; only derived averages and trends (AVR -40% in 2020 vs 2018, snippet only).
- Bypass and cross-clamp times for sternotomy mitral repair were not found; only robotic and minimally invasive figures.
- The 2019 EACTS MAP target of 50-80 mmHg (Class I A) was seen only through an editorial snippet; the original recommendation table was not read.
- No published universal OR call-out script exists. The proposed script is a design proposal and may need review by a cardiac team member.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 01.1 | 161,907 isolated CABG in the STS database in 2023, 11.5% (18,656) off-pump, multi-arterial grafting 17.9% | https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/ | Main justification for choosing on-pump CABG as v1. The figure comes second-hand, through a paper citing the STS 2024 update. |
| 01.2 | About 22,000 isolated SAVR per year in STS (178,014 from July 2014 to June 2022; derived average), median bypass time 90-96 min, cross-clamp 68-72 min | https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/ | Sets the volume ranking and the timing par values for v2. The per-year figure is my own derived average and hides the post-TAVR decline. |
| 01.3 | ACT above 480 s before bypass (above 400 s acceptable with maximal-activation devices); typical heparin bolus 300 IU/kg; 6 of 100 patients had ACT below 350 s after 300 IU/kg | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | Used as a hard gate and as a random-event probability in the game. A wrong value breaks realism at the most important safety step. |
| 01.4 | Protamine-to-heparin ratio should be kept below 1.0 (2024 EACTS); STS 2018 limits it to below 2.6 mg per 100 U | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | Sets the protamine dosing rule and the bleeding/coagulopathy penalties. The two guidelines differ and the 2024 wording is based on reviews. |
| 01.5 | Pump flow 2.2-2.8 L/min/m2; transfuse if Hb is below 6.0 g/dL; HCT 21-24% acceptable if oxygen delivery is above 273 mL/min/m2; systolic below 100 mmHg during aortic cannulation | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | Core values of the perfusion physiology model. They were extracted from a very long guideline page by text search. |
| 01.6 | del Nido cardioplegia 20 mL/kg up to 1000 mL, single dose for up to 90 min; Buckberg 4:1 at 4 C redosed every 15-20 min, hot shot about 500 mL at 37 C | https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478 | Defines the two cardioplegia modes and the redose timer. Adult practice varies (one adult protocol uses 1000-1200 mL plus 500 mL every 60 min). |
| 01.7 | Retrograde cardioplegia 200-400 mL/min at coronary sinus pressure 30-50 mmHg; antegrade at 60-100 mmHg; cold intermittent dosing every 20-30 min | https://academic.oup.com/ejcts/article/67/2/ezae354/8011475 | Sets the thresholds for the coronary sinus injury event and the delivery UI. The figures came from a partial page read. |
| 01.8 | Transit-time flowmetry patency predictors: mean flow above 15 mL/min, PI below 5.0, diastolic filling above 50%, reverse flow below 4% (stricter: above 20, below 3.0, below 3%) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563 | Drives graft scoring and revise/accept decisions. The source itself says cut-offs are not standardized. |
| 01.9 | Open-chest defibrillation optimal initial energy 10-30 J (CALS-ANZ protocol uses 20 J internal) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868 | Sets the default energy for the very common VF-after-unclamping event. |
| 01.10 | On-pump CABG medians: skin-to-skin 240 min, bypass time 112 min, cross-clamp 65 min, 3 grafts (n = 51, single centre) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/ | Par times for the v1 level. A small single-centre sample; the multicentre cohort shows shorter means (cross-clamp 58, bypass time 77). |
| 01.11 | 2018 ESC/EACTS classes: graft flow measurement IIa B; IMA skeletonization I B; radial artery over vein for high-grade stenosis I B; endoscopic vein harvest IIa A; no-touch vein IIa B | https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began | Justifies the conduit-choice mechanics. Taken from a commentary, not the guideline text, and may have been superseded by 2024 ESC guidance. |
| 01.12 | Fewer than 9 paired sternal wire fixation points raise deep sternal wound infection risk (p = 0.002); infection rate 1.5% in 2,672 patients | https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758 | Drives the closure mini-game risk model. It is one observational study; other sources cite 7-8 wires as typical. |

## 02 — Physiology, anesthesia and perfusion

**Key findings**

- No open-source physiology engine models CPB. Kitware Pulse (Apache-2.0, C++ with C/C#/Java/Python interfaces) is the most mature and game-ready option. Its version page lists 4.4.0 as August 2026. It has free Unity and Unreal plugins. It has no cross-clamp, cardioplegia, venous reservoir, heat exchanger or anticoagulation. Its ECMO pump is an 'ideal flow source'. It models only the ventricles (no atria), uses a template ECG, and its validated drug list lacks vasopressin, heparin, protamine, amiodarone, lidocaine, milrinone and dobutamine.
- Pulse runs at a 20 ms time step (about 10-15x real time on laptops, per a forum post). The Unity Asset Store package is v4.3.1 (5 Feb 2025), free, under the Standard Unity Asset Store EULA. BioGears is Apache-2.0 (8.2.0, date uncertain). OpenCOR and ECGSYN are GPL-3.0. CircAdapt and HumMod licenses could not be verified.
- 2024 EACTS/EACTAIC/EBCP CPB guideline (BJA 2025;134:917-1008): usual flow 2.2-2.8 L/min/m2; minimum DO2 280 mL/min/m2 (Class I, Level A); MAP 50-80 mmHg (I-A); pressors to push MAP above 80 mmHg not recommended (III-B); transfuse red cells if Hct <18% (I-C), consider at 18-24% (IIb), not above 24% (III); arterial outlet temperature max 37 C (I-A); protamine:heparin ratio <1.0 (I-B); alpha-stat for high-moderate hypothermia (IIa-B); treat K+ above 6.5-7 mmol/L.
- STS/SCA/AmSECT 2015 temperature guideline: arterial outlet <37 C, arterial-venous gradient <=10 C when cooling and rewarming (I-C); when outlet >=30 C, gradient <=4 C and rewarming <=0.5 C/min (IIa-B). Bladder temperature can read 2-4 C below brain temperature during rewarming. STS 2018 anticoagulation guideline: ACT >480 s (>400 s with maximal-activation devices); protamine <2.6 mg per 100 IU heparin; rebound infusion 25 mg/h for up to 6 h.
- Cardioplegia: Buckberg 4:1 blood:crystalloid at 4 C, maintenance every 15-20 min, warm 'hot shot' before unclamping. del Nido 1:4, 20 mL/kg (max 1000 mL), 4 C, given over 1-4 min at 250-450 mL/min, single dose up to 90 min; per 1 L Plasma-Lyte A it contains KCl 26 mEq, lidocaine 130 mg, mannitol 3.2 g, MgSO4 2 g, NaHCO3 13 mEq. HTK 20-25 mL/kg over 6-8 min, protection claimed up to 180 min (manufacturer only). Antegrade root pressure 60-100 mmHg; retrograde 200-400 mL/min at coronary sinus pressure 30-50 mmHg.
- Vital-sign event responses with sources: hemodilution at CPB start lowers viscosity (about -25% at Hct 30%, -45% at Hct 20%; +2% per C of cooling) and causes the initial MAP fall. BIS falls about 1.2 per C of cooling. Propofol levels are 28% higher at 34 C. Fentanyl falls 30-60% at CPB start. Reperfusion VF after unclamping was 74-96% in older series vs 9-16% in a modern RCT. Post-op AF is 30-40% after CABG. Pacemaker after aortic valve replacement is 2-4% within 30 days.
- Drug dose ranges and half-lives for PK/PD: norepinephrine 0.01-0.3 (up to 1) ug/kg/min, t1/2 2-3 min; epinephrine 0.01-0.3 ug/kg/min; vasopressin 0.01-0.04 U/min, t1/2 10-35 min, no rise in PVR; dobutamine 2-20 ug/kg/min, t1/2 about 2 min; milrinone 50 ug/kg load then 0.375-0.75 ug/kg/min, t1/2 2.3-2.4 h; propofol Eleveld reference parameters V1 6.28 L, CL 1.79 L/min, ke0 0.146/min. CALS-ANZ arrest rules: 3 stacked shocks, re-sternotomy within 5 min, internal defibrillation 20 J, epinephrine 50-100 ug.

**Recommendations**

- Adopt a hybrid approach. Build a custom 0-D real-time core in the game engine: 4-chamber time-varying elastance heart, 3-element Windkessels, Ursino-type baroreflex, an explicit CPB circuit (reservoir, pump, oxygenator, heat exchanger, cardioplegia, vents, suction), O2/CO2 transport, temperature, heparin to ACT, and PK/PD. Run it at a fixed 50 Hz (20 ms) step.
- Use Pulse 4.4.0 (Apache-2.0) as a validation oracle for off-pump behaviour and drug responses, and optionally live for the induction and ICU/arrest scenes. Pin the version and keep the LICENSE and NOTICE files.
- Do not ship GPL code (ECGSYN, OpenCOR). Re-implement the McSharry ECG model and the Smith/Ursino/Westerhof equations from the papers. Use MIT-BIH (ODC-By 1.0) only as reference data, with attribution.
- Encode the guideline targets (DO2 >=280, MAP 50-80, Hct triggers, temperature gradient and rate limits, ACT >480 s, protamine ratio <1.0) as a scoring and rules engine. The surgical state machine should change only physiology inputs, never displayed vital signs.
- Keep every number in a versioned JSON parameter file with its source URL and evidence grade, so a clinician or perfusionist can review it. Mark design-estimate PD effect sizes as tunable.
- Support three cardioplegia options (Buckberg, del Nido, HTK) with different redosing timers and side effects (glucose rise, hemodilution, hyponatraemia that should not be corrected) as meaningful player choices.

**Open questions**

- What are the CircAdapt and HumMod licenses? Neither could be verified on an official page.
- HTK (Custodiol) dose and 180-min protection claim come only from manufacturer or trial-registry snippets. A primary study or the current label is needed.
- There are no sourced time constants for heart-lung-machine dynamics (how fast MAP falls at CPB start, reservoir level dynamics), for ACT test turnaround, or for the exact ACT-vs-heparin-concentration curve. Perfusionist input or the full ECCSIM/Orpheus papers are needed.
- PD effect sizes (EC50/Emax) for norepinephrine, vasopressin, phenylephrine and milrinone in anesthetized cardiac patients were not found in game-ready form. The values in the report are design estimates.
- Which hypothermia classification should the game display: the CPB-study bands (mild 32-35 C, moderate 28-32 C) or the circulatory-arrest consensus bands in EACTS 2024 Table 3?
- Ambiguous guideline wording should be confirmed against the PDF: LCOS printed as 'cardiac index of 2.4 L/min/m2', and NIRS 'below 15% of baseline'.
- StatPearls (bot check) and the AHA 2025 algorithm PDF (403) could not be read directly. Their dose values are snippet-only and need a human check.
- BioGears 8.2.0 release date conflicts (README says January 2025; Releases page shows '12 Dec' with no year).
- The Pulse version page title says 4.3.0 while its content lists 4.4.0 (Aug 2026). Confirm the 4.4.0 tag on GitLab before pinning.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 02.1 | Pulse Physiology Engine latest version is 4.4.0, released August 2026, adding a new ECMO VV/VA device model (the page title still says 4.3.0). | https://pulse.kitware.com/version.html | This sets which engine version the plan pins. The page labelling is inconsistent, and the version falls after the model's knowledge cutoff. |
| 02.2 | The Pulse Unity asset is v4.3.1 (5 Feb 2025), free, under the Standard Unity Asset Store EULA (not Apache-2.0 for the package itself). | https://assetstore.unity.com/packages/slug/139773 | License and version of the main Unity integration path; this EULA differs from the engine's Apache-2.0 license. |
| 02.3 | The Pulse ECMO model uses an ideal flow source and does not simulate anticoagulation, thrombosis or hemolysis; Pulse has no CPB model. | https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html | This is the main justification for building a custom CPB core instead of using Pulse alone. |
| 02.4 | CircAdapt has no verifiable license on its official pages (UNVERIFIED). | https://framework.circadapt.org/latest/userguide/installation.html | Decides whether CircAdapt can be used at all; a missing license means no use rights. |
| 02.5 | del Nido adult dose is 20 mL/kg, max 1000 mL for patients over 50 kg, 1:4 blood:crystalloid at 4 C, single dose up to about 90 min. | https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf | Drives the cardioplegia mechanic and the redosing timer. Institutional protocols vary. |
| 02.6 | Custodiol HTK single dose is 20-25 mL/kg over 6-8 min and protects for up to 180 min. | https://clinicaltrials.gov/study/NCT01681095 | Comes only from manufacturer/trial snippets and is likely to be overstated or variable. |
| 02.7 | STS/SCA/AmSECT: when arterial outlet is >=30 C, keep the arterial-venous gradient <=4 C and rewarming rate <=0.5 C/min (Class IIa, B); outlet <37 C. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ | These are core scoring rules for the temperature mechanic. |
| 02.8 | EACTS 2024 recommends a protamine-to-heparin ratio <1.0 (Class I, B), while STS 2018 limits it to <2.6 mg per 100 IU heparin. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | The two guidelines express the dosing rule differently; the protamine mechanic depends on reading it correctly. |
| 02.9 | ACT >480 s is a reasonable target during CPB (>400 s with maximal-activation/microcuvette devices); heparin bolus 300-400 IU/kg. | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/ | This is the hard gate before starting bypass in the game. |
| 02.10 | EACTS 2024: MAP 50-80 mmHg on CPB (Class I, A) and minimum DO2 280 mL/min/m2 (Class I, A); flow 2.2-2.8 L/min/m2. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | These are the primary perfusion scoring targets. |
| 02.11 | CALS-ANZ: internal defibrillation 20 J, up to 3 stacked external shocks, re-sternotomy within 5 min, epinephrine 50-100 ug instead of 1 mg. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/ | Defines the post-cardiac-surgery arrest scenario, which differs from standard ACLS. |
| 02.12 | Heparin half-life is dose-dependent: about 30 min at 25 IU/kg, 60 min at 100 IU/kg, 150 min at 400 IU/kg. | https://www.thebloodproject.com/ufaq/what-is-the-half-life-of-unfractionated-heparin-2/ | Drives the ACT decay and redosing mechanic. It is a secondary, snippet-only source. |

## 03 — Free assets and their licenses

**Key findings**

- BodyParts3D has a new license. The DBCLS license page (updated 2025-02-27) says CC BY 4.0, not the old CC BY-SA 2.1 Japan. Downloaded directly (BP3D 4.0), it is the best attribution-only base heart. It has named coronary parts (RCA, marginal, PDA, posterolateral, LM, LAD, Cx, septals), the tricuspid, pulmonary and mitral valves, the great vessels and the sternum. It has no pericardium, and no aortic valve was found in the parts list. Meshes are 99% reduced, so it needs a re-sculpt.
- Z-Anatomy is CC BY-SA 4.0. Some bundled parts are CC BY-NC(-SA): the Dundee inner ear and the Cowley kidney. Use it for reference and thorax context only, and keep its meshes in an SA-segregated folder.
- The most realistic free hearts are non-commercial. Real-heart scans are CC BY-NC 4.0 (VisibleHeartLabs Heart0102: RCA 3 / LAD 4 / Cx 3 branches) or CC BY-NC-SA 4.0 (CU Anschutz plastinated CABG heart, 1M tris; UMCG coronary-dominance variants). They are fine for the personal build, but must be replaced before any commercial release.
- Attribution-only alternatives: the HRA/CCF 3D heart GLBs (CC BY 4.0, v1.2 June 2022), NIH 3D 3DPX-011381 and 3DPX-000906 (CC BY 4.0), and the TotalSegmentator CT dataset v2.0.1 (CC BY 4.0; 1,228 CTs; 117 structures; 23.6 GB). TotalSegmentator code is Apache-2.0. Its heartchambers_highres and coronary_arteries tasks need a free non-commercial license key.
- MM-WHS needs a signed form and forbids redistribution. ImageCAS (1,000 CTA scans) has no stated license and is shared by email request. ASOCA is accessed through Grand Challenge. Treat derived meshes from MM-WHS and ImageCAS as personal-only.
- CC BY OR scenery exists on Sketchfab: a medical equipment set (bed, dual-arm lights, console, cart; 70,937 faces), an operating table (46,400 faces), patient monitors, and a low-detail heart-lung machine (8,635 faces). No free sternal (Finochietto) retractor or sternal saw was found, so these must be modelled in-house. Sketchfab search results also contain spam and duplicate re-uploads (for example 8+ copies of a 34,401-face beating heart), so provenance checks are needed.
- Poly Haven and ambientCG are CC0, and Poly Haven has two CC0 hospital HDRIs (up to 17K and 20K). Neither has tissue materials, so tissue should be procedural Blender shaders baked to textures. Megascans have been mostly paid on Fab since 2025. The Fab Standard license has a Personal tier for buyers with up to USD 100k revenue in the last 12 months.
- Freesound has a usable CC0 OR core: suction recorded during surgery, a 2 min 36 s surgery field recording, a Lifepak 12 monitor/defibrillator, a ventilator, and hospital room tone. Some useful sounds are CC BY-NC (ICU.wav 3.0, gloves). Cautery, sternal saw and roller-pump sounds are missing and must be recorded or synthesised. Sonniss GDC bundles are royalty-free with no attribution; 2024+ bundles reportedly ban AI training.
- Characters: MPFB 2.0.18 (2026-10-10; GPL-3.0-or-later code, CC0 core assets) and Microsoft Rocketbox (MIT, 115 rigged avatars, repo archived) are the safest. MetaHuman may be used in any engine since 5.6 (June 2025), free under USD 1M revenue, with no AI training. Mixamo forbids redistributing raw files. Ready Player Me shut down its public services on 2026-01-31 after the Netflix acquisition.
- Pipeline: use Blender 5.2 LTS (released 2026-07-14); Blender output belongs to the user and add-ons are GPL. The bundled glTF exporter is Apache-2.0. Shape keys become morph targets, and skinning is capped at 4 influences per vertex (the exporter keeps the top 4 and normalises them). Free remeshers: QRemeshify (GPL-3.0) and Instant Meshes (BSD-3-style). The report includes an ASSET_LICENSES.md template with GREEN/AMBER/RED status.

**Recommendations**

- Create ASSET_LICENSES.md (one row per source asset, with exact license string, verification date, evidence screenshot, TASL attribution, SA/NC/ND flags, derived files and a GREEN/AMBER/RED status). Set up green/, amber_sa/ and red_personal_only/ folders before importing anything.
- Build the base heart from BodyParts3D 4.0 (CC BY 4.0) downloaded directly from DBCLS. Re-sculpt and retopologise it against NC real-heart scans used as reference only. Keep the FMA IDs as mesh names for gameplay hit-testing (for example FMA3862_LAD).
- Add anatomical variants from the HRA heart (CC BY) and TotalSegmentator meshes made from its CC BY dataset via 3D Slicer. Model a coronary-dominance parameter after the UMCG variants.
- Model the cardiac-specific instruments in-house: Finochietto retractor, sternal saw, aortic cross-clamp, cannulae and a detailed CPB console. Keep them generic with no brand marks. Use the CC BY OR set and operating table for scenery, and Poly Haven CC0 hospital HDRIs for lighting.
- Make tissue as procedural Blender shaders baked to normal/AO/curvature/base-colour maps. Colour-pick only from CC0 or NLM sources and from NC scans used as reference.
- Audio: start from the CC0 Freesound OR recordings (suction, surgery ambience, Lifepak, ventilator, room tone). Record or synthesise cautery, saw, roller-pump and monitor alarm sounds. Keep Sonniss and other no-redistribution raw libraries out of the public repo.
- Characters: use MPFB 2.0.18 for the patient and staff bodies, Rocketbox (MIT) for background staff, and Mixamo for animations (baked only). Do not use Ready Player Me. MetaHuman is optional.
- Pipeline: Blender 5.2 LTS → GLB with a shape-key heartbeat (4-8 morph targets) and optional bones for torsion (max 4 influences per vertex). FBX as a fallback. Validate the GLB files.
- Never commit RED assets (NC, ND, editorial, unknown licenses, dataset-restricted files) to the public GitHub repository. Add a PUBLIC_BUILD check that fails if any RED asset is referenced. Re-verify all licenses on the day of any public release.

**Open questions**

- Does the HRA heart GLB (v1.2 or later v2.x) contain coronary arteries, valves and cardiac veins? It must be downloaded and inspected.
- Does BodyParts3D 4.0 include an aortic valve and cardiac veins? They were not found in the 3.0 parts-list extraction.
- What are the exact license terms for ImageCAS (repo states none) and ASOCA (Grand Challenge terms), and may derived meshes be redistributed?
- The official Sonniss GDC license page, the full Fab EULA, the Adobe helpx Mixamo FAQ, the MetaHuman license page and the CTSNet terms were blocked or required login. Their current exact wording is unverified.
- Is the 2025 CC BY 'Anatomically Correct Human Heart' (1M faces) original work, or AI-generated / re-uploaded? Who is the original author of the widely re-uploaded 34,401-face beating heart (credited to 'Dreamwasabducted')?
- Are there CC0 sources for electrocautery, sternal saw and CPB roller-pump sounds, and CC0 photo-scanned fat/meat textures? The search budget ran out before these could be searched.
- What are the IEC 60601-1-8 alarm-tone pulse patterns, so synthesised monitor alarms sound right?
- Embodi3D terms (HTTP 403) and Open Anatomy atlas data license (not stated) remain UNVERIFIED.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 03.1 | BodyParts3D is now licensed CC BY 4.0 (license page last updated 2025-02-27). The older 3.0 release was CC BY-SA 2.1 Japan. | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html | It decides whether our edited base heart must be ShareAlike. A wrong reading changes the license of the core anatomy asset. |
| 03.2 | The current BodyParts3D download (BP3D 4.0) only offers 99%-reduced OBJ meshes (136 MB IS-A, 62 MB PART-OF), and the parts list has no aortic valve or pericardium entries. | https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html | It drives how much sculpting and retopology work the anatomy pipeline needs. |
| 03.3 | All HRA/CCF 3D reference objects, including the male and female heart GLB (v1.2, June 2022), are CC BY 4.0. | https://hubmapconsortium.github.io/ccf/pages/ccf-3d-reference-library.html | It is the main clean CC BY alternative heart. Its version and anatomical detail were not inspected. |
| 03.4 | The TotalSegmentator heartchambers_highres and coronary_arteries tasks need a license key that is free only for non-commercial use. The code is Apache-2.0. | https://github.com/wasserth/TotalSegmentator | It decides whether CT-derived coronary meshes can ship in a public or commercial build. |
| 03.5 | The TotalSegmentator CT dataset v2.0.1 is CC BY 4.0, with 1,228 CT images, 117 structures and 23.6 GB. | https://zenodo.org/records/10047292 | It is the proposed source of GREEN patient-variant thorax meshes. |
| 03.6 | VisibleHeartLabs Sketchfab hearts (for example Heart0102) are CC BY-NC 4.0, and the CU Anschutz CABG heart is CC BY-NC-SA 4.0. | https://sketchfab.com/3d-models/heart0102-coronary-arteries-6e3ddf0caa2640b39aa240f8c4ffc1ea | These are the most realistic hearts. NC status blocks any commercial release and decides the reference-only policy. |
| 03.7 | Megascans have been mostly paid on Fab since 2025. Bridge-downloaded legacy Megascans remain under the Unreal-only Epic Content License. The Fab Standard Personal tier is for buyers with no more than USD 100,000 revenue in 12 months. | https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/ | It decides whether Megascans can be relied on for free, engine-agnostic environment assets. The full Fab EULA could not be fetched. |
| 03.8 | Sonniss GDC bundles (including the GDC 2026 bundle, 7.47 GB+) are royalty-free, need no attribution and allow unlimited projects; bundles from 2024 on forbid AI training. | https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/ | It would be the main large SFX library. The official license page was blocked, so the terms come from secondary sources. |
| 03.9 | Since MetaHuman 5.6 (2025-06-03), MetaHumans can be used in any engine. They are free under USD 1M yearly revenue (UE seat USD 1,850/year above that) and may not be used to train AI. | https://www.cgchannel.com/?p=167592 | It decides whether MetaHuman is allowed if the game is not built in Unreal. The official license page needed login. |
| 03.10 | Ready Player Me public services shut down on 2026-01-31 after Netflix acquired the company in December 2025. | https://en.wikipedia.org/wiki/Ready_Player_Me | It rules out an avatar pipeline option. The Wikipedia article cites only a Medium blog post. |
| 03.11 | MPFB 2.0.18 (released 2026-10-10) is GPL-3.0-or-later code, and MakeHuman core assets are CC0. | https://extensions.blender.org/add-ons/mpfb/ | It is the primary patient and staff body source. The CC0 output status determines that no attribution or copyleft applies to exported characters. |
| 03.12 | Blender's glTF exporter keeps only the 4 highest bone weights per vertex (normalised), and shape keys export as glTF morph targets. | https://archive.blender.org/lists/bf-extensions-cvs/2022-April/010894.html | It sets the heartbeat rig design limits (vertex-group budget and choosing morphs vs bones). |

## 04 — Game engine and simulation technology

**Key findings**

- Current engines as of Nov 2026: Unreal Engine 5.8 was released 17 June 2026 and is reportedly the last UE5 release. Unity's current LTS is 6.3, supported to Dec 2027; Unity 6.0 LTS support ended Oct 2026. Godot 4.7-stable was tagged 18 June 2026. All three are free for a personal, non-commercial project.
- No engine ships soft-tissue cutting good enough for surgery. Unreal's Chaos Flesh is built for character muscle and relies on offline caching, and its docs never mention cutting. Unity's built-in physics offers only Cloth for deformables. Godot/Jolt soft bodies have no cutting.
- SOFA v26.06.00 (15 Jul 2026, LGPL-2.1-or-later) is the only active open medical-physics framework. SofaUnity is under the Unity Asset Store EULA and only tested on Windows. The Unreal bridge SofaUE5-Renderer is GPL-3 and visual-only (snippet only).
- Kitware iMSTK (Apache 2.0) was discontinued on 2 May 2025; its last tag is v7.0.0 (Sept 2023). It is still useful as reference code for needle puncture, suturing and level-set bone cutting.
- XPBD makes stiffness independent of iteration count and time step. The 'Small Steps' paper shows that n substeps with 1 iteration each beat 1 step with n iterations. The most heart-relevant recent simulator (Liu et al. 2026, Vessel Plus, VR proximal anastomosis for CABG) used Unity3D, Cosserat rods with XPBD for vessels and sutures, and a Geomagic Touch.
- Published real-time numbers are modest. iMSTK targets <5 ms of physics per frame, with ~2,000 constraints optimal on a laptop i9 and haptics at 500-1000 Hz. A 2013 GPU mass-spring model ran >100K masses at 1 kHz on a Tesla C2050. A 2026 paper runs deformation at 60-100 Hz and haptics at >=1000 Hz on a separate thread. Only ~65% of approaches in a 2020 review met real time.
- Knot tying is unsolved even in iMSTK ('planned but not implemented'). A knot minigame plus a scripted knot is the practical game approach.
- PhysX 5 deformable volumes (formerly FEM soft bodies) use a fixed corotated model and a CUDA-style API. Cutting or tearing requires the precomputed (cooked) data to be updated.
- Quest 3 standalone targets: 72 Hz minimum (90 recommended), 13.8 ms frame budget, <200 draw calls, <1.5M triangles. UE physics substepping is not supported on mobile. Quest 3 hand tracking has 1.73 cm error and 38 ms motion-to-photon latency in the best case, too coarse for suturing.
- Haptics: 3D Systems Touch gives 3.3 N max at 1 kHz, ~US$2,800 list. Haply Inverse3 gives 4 kHz, 0.01 mm and up to 10 N, at GBP 5,965 from a reseller. Force Dimension omega.x gives 12 N at up to 4 kHz with SDK 3.17. CHAI3D 3.3 is BSD-3. H3DAPI is GPL-2.0 and stale (2019).
- Pulse Physiology Engine 4.4.0 (Aug 2026, Apache 2.0) has Unreal and Unity integrations. It adds an ECMO device with VV/VA cannulation, which could be a starting point for the bypass (CPB) state.

**Recommendations**

- Main stack: Unreal Engine 5.8, desktop first at 60 Hz (16.7 ms), with optional PC VR at 90 Hz (11.1 ms) through OpenXR 1.1. Use Chaos Cloth for drapes and Niagara plus custom compute for blood.
- Write an engine-agnostic C++ XPBD core as an Unreal plugin module, so it can be ported to Unity (native DLL) or Godot (GDExtension). It should cover tetrahedral soft bodies, Cosserat-rod suture thread, needle puncture with a sliding constraint, attachment constraints for retraction, SDF tool collision and strain-based tearing. Base it on MIT references (PositionBasedDynamics, Jolt ideas, Ten Minute Physics).
- Fallback stack: Unity 6.3 LTS with URP, plus SofaUnity/SOFA or Obi XPBD assets, or the same native core.
- Beating heart: a baked Blender animation (Alembic, then PCA morph targets) acts as the kinematic target. A low-res XPBD tet body follows it with weak constraints. Pulse drives the heart rate. Exploit the arrested heart during cardioplegia for the anastomosis phase.
- Blood in layers: wetness/stain decals and flow maps, GPU particles (Niagara 2D only for spurts, baked to flipbooks), a small SPH pool with suction, and screen-space fluid rendering. Bleeding rate comes from Pulse.
- Use scripted-plus-physics design for skin incision, sternotomy (saw-path skill check, level-set inspired) and knots (minigame). Use full physics for retraction, needle bites, thread and local tissue response.
- Physics budget: <=5 ms per frame on desktop, 8-16 XPBD substeps with 1 iteration each, a planning value of 2k-8k sim tets for the heart, and visual meshes skinned to the sim mesh. Add quality presets and automatic fallbacks.
- Do not target Quest 3 standalone for the full simulation. Use hand tracking only for coarse actions. Use a controller precision mode, mouse or haptic stylus for suturing.
- Make haptics an optional tier behind a CHAI3D-style device abstraction. Use Touch as the entry device and Inverse3 or omega as the better ones. Clamp output forces to each device's maximum.
- Run SOFA v26.06 offline (Python) as a validation reference for deformation behaviour. Do not build on iMSTK or H3DAPI.

**Open questions**

- Exact current Unreal Engine EULA royalty and seat-fee text (unrealengine.com returned 403; terms come from a snippet and Wikipedia).
- Did the SOFA-to-Unreal Kickstarter plugin (posted 19 Nov 2025) ship, and under which license?
- Real achievable haptic loop rate of the Haply Inverse SDK over its WebSocket service (Isaac Lab streams at 200 Hz).
- Current license terms and prices for OpenHaptics, the Force Dimension SDK, the Haply SDK, Touch X, omega.x and Obi assets (UNVERIFIED).
- Vega FEM license and version (barbic.usc.edu was not reachable; UNVERIFIED).
- Chaos Flesh maturity label (Experimental / Beta / Production) in UE 5.8. The docs do not state it.
- Achievable tetrahedron count with cutting in our own XPBD core on a mid-range PC. This needs a benchmark spike.
- Can Pulse 4.4.0's ECMO model be extended to a full CPB circuit (venous reservoir, cardioplegia, vent)?
- Unity 6.6 / 6.7 LTS / Unity 7 status (single weak source) and the future of HDRP.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 04.1 | Unreal Engine royalty is 5% of lifetime gross product revenue above the first US$1M; 3.5% if also released on the Epic Games Store (since Oct 2024); non-game seat fee US$1,850/seat/year for >$1M revenue. | https://www.unrealengine.com/en-US/license | Engine choice depends on license terms. The official page returned 403, so the figures come from a search snippet and Wikipedia (https://en.wikipedia.org/wiki/Unreal_Engine_5). |
| 04.2 | Unreal Engine 5.8 was released 17 June 2026 and is the last UE5 release; UE6 previews are expected around late 2027. | https://gamefromscratch.com/unreal-engine-5-8-released/ | Sets the engine version to pin. The UE6 timing is snippet-only and the Epic homepage date (23 June) differs. |
| 04.3 | Unity Personal is free up to $200,000 revenue and funding, splash screen optional; Pro is $2,310/yr per seat from 12 Jan 2026; Havok Physics is no longer included from Unity 6.3. | https://unity.com/products/pricing-updates | These are the fallback engine's cost terms. The page itself is inconsistent about whether Havok removal starts at 6.0 LTS or 6.3. |
| 04.4 | Godot 4.7-stable was released 18 June 2026; Godot recommends the Mobile renderer for XR, and SSS/SSR are Forward+ only. | https://github.com/godotengine/godot/releases/tag/4.7-stable | The year is inferred (the tag page shows only day and month). The renderer limits drive the decision not to use Godot as the main engine. |
| 04.5 | SOFA v26.06.00 was published 15 July 2026 and SOFA is LGPL 2.1-or-later (GPL for applications/projects and tutorials). | https://github.com/sofa-framework/sofa/releases | Main open medical-physics dependency for the fallback and validation path. The year is inferred from the version number. |
| 04.6 | iMSTK development was discontinued as of 2 May 2025; it is Apache 2.0 and its last tag is v7.0.0 (Sept 2023). | https://gitlab.kitware.com/iMSTK/iMSTK | Decides that iMSTK must not be a foundation. Checked through the GitLab API and README. |
| 04.7 | SofaUE5-Renderer is GPL-3, visual-only (no two-way coupling), and requires UE 5.0.3. | https://github.com/InfinyTech3D/SofaUE5-Renderer | Snippet only. If wrong, SOFA in Unreal could be a viable main path. |
| 04.8 | SofaUnity is licensed under the Standard Unity Asset Store EULA and is only tested on Windows; it supports SOFA >23.06. | https://github.com/InfinyTech3D/SofaUnity | Defines the platform and license limits of the fallback stack. |
| 04.9 | 3D Systems Touch: 3.3 N max force, >0.88 N continuous, 1 kHz USB, ~0.055 mm resolution; list price US$2,800 at one reseller. | https://www.3dsystems.com/haptics-devices/touch | Sets the entry haptic device and the force clamp. The price comes from https://matterhackers.com/store/l/3d-systems-touch-haptic-device/sk/M12PCJ5U (C grade, product unavailable). |
| 04.10 | Haply Inverse3: 0.01 mm resolution, 4 kHz refresh, up to 10 N; UK reseller price GBP 5,965.15. | https://www.haply.co/inverse3 | Recommended better haptic device. The price is from a reseller (https://shop.verticalrealities.com/products/inverse3) and the workspace is unverified. |
| 04.11 | Quest 3 hand tracking has 1.73 cm positional error and 38.33 +/- 31.29 ms motion-to-photon latency in best conditions. | https://doi.org/10.1109/TVCG.2025.3549182 | Drives the input rule that hand tracking is not used for suturing. Read through the author portfolio summary, not the full paper. |
| 04.12 | Quest 3 performance targets: 72 Hz minimum (90 Hz recommended), 13.8 ms at 72 Hz, <200 draw calls, <1.5M triangles per frame. | https://developers.meta.com/vr/resources/device-optimization-comparison/ | Justifies excluding Quest 3 standalone. Meta's Unreal guide gives different ranges (200-1000 draw calls, 1.3-1.8M triangles). |

## 06 — Game design and benchmarks

**Key findings**

- Web search was unavailable for this run because the shared WebSearch budget was already used up when this agent started. All 70 sources were gathered by fetching known primary pages directly: PubMed records through the Europe PMC article, references and citations API, official sites, and TSDA and RCSEd PDFs converted to text.
- The TSDA Cardiac Surgery Simulation Curriculum (copyright 2015) works as a ready level-design document. It has 6 modules (CPB, CABG, AVR, MAE, AIAD, SDCF) and 29 sessions of 2-4 h each. It includes explicit assessment tools: VAAT (13 items, 1-5), ACAT (12), CPBAT (8) and SEAT (5). Its mastery rule is a score of 4 or better on every item, with minimum repetitions of 10, 7 and 5. Its crisis timers are MAE 3 and 2 min, AIAD 3 and 20 min, SDCF 4 min, and a full CPB run within 30 min.
- Coronary anastomosis is the task with the most evidence. One meta-analysis (12 studies) found skill SMD 1.68 and time 205.9 s faster, with no effect of simulator fidelity (O'Dwyer 2022). Another (11 studies) found SMD 2.18 for skill and 2.00 for time (Sidik 2026). Expert vs trainee motion values are published: spacing SD 1.72 vs 2.14 mm, hand path 6,714 vs 10,154 mm, stitch time 4.6 vs 6.4 s (Wang 2026).
- For CPB, cognitive and decision scores separated experts from trainees, but technical scores did not (Hermsen 2021). At Boot Camp, residents most often missed the ACT check (3) and communicated poorly with the perfusionist (4), and massive air embolism was the hardest crisis (Hicks 2011).
- OSATS global ratings separated training levels where checklists did not (Martin 1997). Experts reached consensus on only 40 of 146 anastomosis checklist items (Vaporciyan 2017), and no cardiac simulation study validated its assessment tool (Ribeiro 2018). The game should therefore use configurable graded rubrics and must not claim its scores are validated.
- NOTSS v2.0 (2019) has 4 categories and 12 elements (names confirmed from the handbook table), rated 1-4 plus N/A. The handbook says it is not for summative assessment and allows free reproduction for personal and not-for-profit use. The ANTS prototype has 4 categories and 15 elements.
- In STS terms, the CABG composite has 4 domains: mortality, morbidity, IMA use and medications. Morbidity covers 5 complications: reoperation, stroke, kidney failure, chest wound infection and prolonged ventilation. Operative mortality means in-hospital death or death within 30 days if discharged. These definitions support an end-of-case outcome card.
- Gamification and practice schedule both have evidence. In the Top Gun competition, the pass rate rose from 13% to 73% and residents averaged 23 practice anastomoses (Enter 2015). Spaced practice beat massed practice for retention and transfer (Moulton 2006). Beating-heart training beat non-beating training (Wu 2021).
- Lessons from games: copy Trauma Center's tool palette, timer and C-S ranks, and avoid Surgeon Simulator's deliberately awkward controls where individual keys move each finger. On hardware, the 3D Systems Touch has 6-DOF sensing, 3-DOF force output and a 3.3 N maximum. Unity XR Hands 1.5.1 exposes 26 points per hand. Haptics helped in 6 of 8 RCTs (Rangarajan 2020).

**Recommendations**

- Build the MVP as a CPB run using the 7 Steps of CPB plus CABG to the LAD, with two crisis drills (protamine reaction and massive air embolism). Start with desktop mouse, keyboard and gamepad controls, and gate entry with a Learn mode that requires 90%.
- Score in 4 visible layers: Technical (VAAT, ACAT and CPBAT-style items 1-5 computed from telemetry), Process and safety (7-step checklist plus never events such as no heparin, no ACT check, air in the line, or cross-clamping without flow down), Non-technical (NOTSS-style and SEAT for crises), and Outcome (an STS-style 4-domain card). A run passes only if every item scores 4 or better, all crisis timers are met and no never event occurs.
- Keep every rubric threshold (mm, degrees, seconds) in data files. Calibrate them against the published expert and trainee values and expert review. Show anchored examples of a 1, 3 and 5 for each item, following Lou 2014.
- Write our own rubric text inspired by the TSDA tools rather than copying them, because the TSDA curriculum forbids reproduction without permission. NOTSS terms may be used with credit under its not-for-profit permission.
- Make the perfusionist, anaesthetist, scrub nurse and assistant AI teammates that use closed-loop commands. Add an AI director modelled on the Ramphal simulator operator. Voice input through Vosk (Apache-2.0) is optional, with a radial menu always available.
- Ship timeline replay and a debrief from the start. The debrief should blend PEARLS with the TSDA questions: what went well, what went wrong, questions. Add spaced re-tests at the start of each session, minimum-repetition progress bars and a Top Gun-style challenge leaderboard.
- Phase 2 adds VR with controllers by default and optional XR Hands tracking, then AVR, AIAD and a playable perfusionist. Phase 3 adds an optional haptic stylus (3D Systems Touch) and multiplayer.

**Open questions**

- What is the exact wording of the 7 OSATS global rating items? They are given from memory and need checking against the full text of Martin 1997.
- Feins 2017 reports a massive air embolism final score of 0.68 ± 0.14 against scores of about 4.5 for the other modules. Is this a typo or a different scale?
- The TSDA AIAD objective says femoral cannulation 'within 3 minutes of the time air is recognized'. This looks like a copy error from the MAE module, so what trigger was intended?
- The licences of the TSDA VAAT PDF, the ANTS handbook, the Unity XR Hands package, the OpenHaptics SDK and the Vosk models are not verified.
- KindHeart and HeartWorks official pages could not be reached (404/503), so their current owner and products are unconfirmed.
- What is the STS prolonged-ventilation threshold, and what are the full morbidity definitions? They need the STS data specifications.
- What score thresholds should each rubric level use? They need expert review or playtest calibration.
- Academic VR cardiac surgery projects and hand-tracking accuracy studies were not covered because keyword search was unavailable. A follow-up run with search budget should fill this gap.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 06.1 | TSDA crisis time targets: MAE retrograde SVC perfusion within 3 min of recognising air and normal CPB re-instituted within 2 min of root de-airing; AIAD femoral cannulation within 3 min and repair within 20 min; SDCF CPB re-established within 4 min; full CPB run within 30 min. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | These become hard-coded game timers and pass/fail rules. The AIAD wording looks copy-pasted, and these are simulator training targets, not clinical standards. |
| 06.2 | The TSDA/JCTSE Vessel Anastomosis Assessment Tool has 13 items, each scored 1-5, plus time to completion and overall pass/fail. | https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf | It is the core technical scoring rubric. Its licence is unstated, so reuse rights need checking. |
| 06.3 | The TSDA curriculum (copyright 2015) states that no part may be reproduced, distributed or used without permission. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | This decides whether rubric text can go into the game or must be rewritten as our own. |
| 06.4 | NOTSS v2.0 has 4 categories and 12 elements rated 1-4 plus N/A, is not for summative assessment, and may be reproduced for personal, organisational or not-for-profit use but not commercially. | https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf | This is the basis of the non-technical scoring layer and of permission to use NOTSS terms. |
| 06.5 | Feins 2017: 27 residents at 8 institutions; final mean scores CPB 4.80, CABG 4.41, AVR 4.51, AIAD 4.52, SDCF 4.76, and MAE 0.68 (likely an error). The TSDA preface instead reports 30 residents and more than 3,600 hours. | https://pubmed.ncbi.nlm.nih.gov/27570162/ | These are benchmark scores for the target level of mastery. The MAE value and the 27 vs 30 resident counts conflict. |
| 06.6 | STS CABG composite has 4 domains (operative mortality, major morbidity, IMA use, perioperative medications) over a 36-month window. Morbidity covers 5 complications: reoperation, stroke, kidney failure, chest wound infection and prolonged ventilation. | https://publicreporting.sts.org/acsd-exp | This drives the end-of-case outcome card. Thresholds such as prolonged ventilation were not defined on the fetched pages. |
| 06.7 | Expert vs trainee suturing metrics: inter-stitch spacing SD 1.72 vs 2.14 mm, hand path 6,714 vs 10,154 mm, needle loading 1.9 vs 2.5 s, stitch 4.6 vs 6.4 s. | https://pubmed.ncbi.nlm.nih.gov/42696816/ | These are used as calibration anchors for rubric scores 3 and 5. The paper is recent (2026) and the values come from a 3D-printed model. |
| 06.8 | Coronary anastomosis simulation meta-analysis: skill SMD 1.68 and time 205.9 s faster across 12 studies and 274 subjects, with no significant effect of simulator fidelity. | https://pubmed.ncbi.nlm.nih.gov/35143631/ | It justifies putting the budget into practice loops and feedback rather than maximum fidelity. |
| 06.9 | 3D Systems Touch haptic device: 6-DOF position sensing, 3-DOF force feedback, 3.3 N maximum force, more than 0.88 N continuous, 1 kHz over USB, OpenHaptics SDK with Unity and Unreal compatibility. | https://www.3dsystems.com/haptics-devices/touch | These specs set the haptics design limits. The SDK licence and price are unverified. |
| 06.10 | Unity XR Hands package version 1.5.1 exposes 26 tracked points per hand using OpenXR joint naming, and OpenXR is the only provider. | https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html | It affects the VR input design and the version to pin. The package licence was not verified. |
| 06.11 | Top Gun competition: 12 components on a 1-5 scale, pass with all raters rising from 13% to 73%, time falling from 11:10 to 9:04, and an average of 23 practice anastomoses. | https://pubmed.ncbi.nlm.nih.gov/25595829/ | It is the main evidence for the challenge and leaderboard mode, and gives par-time values. |
| 06.12 | Boot Camp CPB: 3 of 30 residents did not verify ACT before going on bypass, 4 communicated poorly with the perfusionist, and massive air embolism produced the most errors. | https://pubmed.ncbi.nlm.nih.gov/20451929/ | It justifies the choice of MVP crises and the tutorial trap moments. |

## 07 — Production, tools, validation and legal

**Key findings**

- Scope benchmarks: Surgeon Simulator (comedic, 4 people) went from a 48-hour jam to a commercial release in 48 days. Project Hospital (realistic, planned for 2-4 people) took about 2.5-3 years. An academic VR perfusion simulator (UE4, Quest 2) was first published with a single 'initiating CPB' scenario. Realism is what drives cost, so the first milestone should be a physiology-first vertical slice of one CPB phase.
- Free version-control tiers (as of 2026-11): GitHub Free LFS gives 10 GiB storage and 10 GiB bandwidth per month, with a 2 GB per-file limit, and CI downloads count against bandwidth. Unity Version Control since 1 Mar 2026 has no seat fee, 25 GB storage and 100 GB egress. Perforce P4 is free for 5 users and 20 workspaces. Diversion Indie gives 5 free users and 100 GB. Anchorpoint's free plan is single-user and non-commercial only.
- CI: GitHub Free includes $12 of Actions compute per month (Linux 2-core at $0.006/min, about 2,000 min). Public-repo and self-hosted runners are free. The $0.002/min self-hosted fee was postponed. The current GameCI actions are unity-builder@v4 and unity-test-runner@v4, and the Unity Personal license needs the UNITY_LICENSE, UNITY_EMAIL and UNITY_PASSWORD secrets.
- Physiology regression tests can reuse the Orpheus CPB simulator validation (Searles 2021). It took expert ranges from a survey of 335 perfusionists (MAP on CPB 54±7 to 82±9 mmHg; flow index 2.34±0.35 L/min/m2), found the simulator valid for patients of 50-110 kg, with pump flows of 3.5-5.5 L/min and cardioplegia at 250-400 mL/min antegrade and 100-225 mL/min retrograde. It used parameter sweeps and Bland-Altman plots. Pulse keeps baseline scenario results and grades error up to 30% as 'fair'.
- Medical validation should follow the Messick/Kane frameworks. Cook & Hatala 2016 discourage the term 'face validity'. Delphi studies typically set consensus at about 75% agreement, decided in advance (Diamond 2014). A cardiac example used 11 surgeons and counted consensus when 70% rated an item ≥3.5/5 (Cristancho 2012). A Dutch Delphi of 114 experts cut 237 scenarios down to 13 crisis scenarios.
- AI 3D tools have very different terms. TRELLIS.2 is MIT, but its nvdiffrast dependency is licensed for research/evaluation only. The Hunyuan3D 2.1 license excludes the EU, UK and South Korea. Meshy free-plan outputs come with a CC BY 4.0 license. RealityScan 2.0 is free under US$1M revenue (otherwise $1,250/seat/year), and Epic claims no rights in your output. The US Copyright Office's Part 2 report (Jan 2025) says prompts alone do not make you the author.
- Legal position: FDA lists training games that simulate cardiac arrest scenarios as not medical devices. Under MDCG 2019-11 (rev.1 June 2025), step 4 asks whether the software acts for individual patients. Steam bans content 'intended to shock or disgust'. ESRB rated Surgeon Simulator T and Surgeon Simulator 2 M. HIPAA Safe Harbor lists 18 identifiers, including full-face and comparable images.

**Recommendations**

- Months 0-3: build a physiology-first vertical slice of one phase (initiate CPB, cross-clamp, cardioplegia arrest) with 1 complication. Start the medical-fact register and CI regression tests against the Orpheus expert ranges from day 1.
- Months 3-6: one complete abstracted operation (CABG or AVR). Months 6-12: CPB, CABG and AVR plus complications, following the STS/TSDA curriculum module order. Months 12-24: 3-4 procedures, polish, and an optional small validation study. Apply a cut-line rule to protect scope.
- Pick version control by engine: Unity Version Control (25 GB free) for Unity; Perforce P4 self-hosted or Diversion Indie for Unreal. If using Git LFS, keep raw scans and CT out of it and cache LFS objects in CI.
- Use 6 test layers: engine-free physiology unit tests; regression against baselines and expert ranges (±10% for set values, hard fail outside clinical ranges); deterministic input replays on a fixed timestep; bot-surgeon scenario tests; screenshot tests for monitors; and data-integrity checks that every parameter has a fact ID and every asset has a license row.
- Asset policy: CC0 (Poly Haven, ambientCG) and your own Blender, Meshroom or COLMAP work first. Keep CC BY-SA (Z-Anatomy) and NC assets isolated and flagged. Use AI tools only for props, edit the output by hand, and disclose it in the Steam AI survey. Avoid Hunyuan3D in the EU/UK/South Korea and avoid nvdiffrast-based pipelines.
- Validation: get SME review from all 4 roles (surgeon, perfusionist, anesthesiologist, OR nurse), then a modified Delphi of 2-3 rounds with consensus set in advance at ≥75% rating ≥4/5. Report any study using the Cheng 2016 items. Never claim the game is 'validated'.
- Legal: show a not-a-medical-device disclaimer at first launch. Add no patient-specific features (no loading a real patient's CT). Use only public, licensed, de-identified imaging and ship meshes, not DICOM. Use fictional equipment brands. Add a clinical-detail (gore) setting to target ESRB T / PEGI 12-16.

**Open questions**

- Which engine (Unity vs Unreal vs Godot)? This decides the version-control and CI stack.
- Where does the owner live and publish? This matters for the Hunyuan3D territory exclusion and whether GDPR applies.
- Might the game ever be sold or take donations? If so, NC-licensed assets and the Anchorpoint free plan become blockers.
- Can at least one perfusionist, cardiac surgeon, cardiac anesthesiologist and OR nurse be recruited for review or a Delphi?
- Does Steam require an external age-rating certificate for this content? (unverified)
- Do Azure DevOps really offer unlimited free LFS storage, and are GitLab Free limits per project? (only snippets seen)
- What are the exact attribution terms of the Stability AI Community License, and may Tripo free-plan outputs be used commercially? (sources conflict)
- Does running nvdiffrast for a hobby game count as 'research or evaluation' under its license?

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 07.1 | GitHub Free includes 10 GiB Git LFS storage and 10 GiB LFS bandwidth per month. Without a payment method, LFS is disabled until next month once bandwidth is exceeded, and GitHub Actions LFS downloads count against the owner's bandwidth. | https://docs.github.com/en/billing/concepts/product-billing/git-lfs | This is the core storage constraint if the project uses Git. It can block work mid-month. |
| 07.2 | Unity Version Control since 1 Mar 2026: no per-seat charge (cloud), 25 GB storage per org per month free, 100 GB egress per month free; overage $0.14/GB-month and $0.10/GB. | https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges | This is the recommended VCS for Unity, and the terms changed recently (2026), so they could change again. |
| 07.3 | Perforce P4 (Helix Core) is free for up to 5 users and 20 workspaces with no stated time limit; above the limits the server reportedly caps at 1,000 files. | https://www.perforce.com/products/helix-core/free-version-control | This is the recommended VCS for Unreal. The 1,000-file cap comes from a snippet only. |
| 07.4 | GitHub Free includes $12/month of Actions compute. Linux 2-core costs $0.006/min (about 2,000 min). The self-hosted $0.002/min fee planned for 1 Mar 2026 was postponed. | https://docs.github.com/en/billing/concepts/product-billing/github-actions | The CI budget depends on this, and GitHub's billing model changed in 2026. |
| 07.5 | The Tencent Hunyuan3D 2.1 Community License (13 Jun 2025) excludes the EU, UK and South Korea from its territory; use there is unlicensed. | https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE | If the owner is in an excluded region, using this tool would breach the license. |
| 07.6 | TRELLIS.2 is MIT licensed, but its nvdiffrast dependency is under the NVIDIA Source Code License, limited to research or evaluation purposes only. | https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt | The permissive top-level license hides a restrictive dependency, and the risk depends on how 'evaluation' is interpreted. |
| 07.7 | RealityScan 2.0 (released 17 Jun 2025) is free for individuals and companies with < US$1M revenue in the past 12 months, otherwise $1,250/seat/year. EULA s.6: Epic gets no rights in the content you produce. | https://www.realityscan.com/license | This is the main photogrammetry tool option, and both the free threshold and output ownership need confirming. |
| 07.8 | Meshy free-plan outputs are licensed to the user under CC BY 4.0 (credit Meshy); paid plans give private ownership. | https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models | It sets the attribution duties for any AI props, and vendor terms change often. |
| 07.9 | Orpheus CPB simulator validation: expert ranges from 335 perfusionists (MAP on CPB 54±7 to 82±9 mmHg; arterial pump flow index 2.34±0.35 L/min/m2); valid for patients of 50-110 kg, pump flows of 3.5-5.5 L/min, and cardioplegia at 250-400 mL/min antegrade and 100-225 mL/min retrograde. | https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf | These numbers become regression-test envelopes and alarm thresholds. Some table values (e.g., CVP on CPB 2±2) came from imperfect PDF text extraction. |
| 07.10 | Delphi consensus: in a review of 100 studies the median threshold was 75%, and only 42 of 86 studies claiming consensus set it a priori. | https://doi.org/10.1016/j.jclinepi.2013.12.002 | This number sets the recommended consensus rule, but it was seen only via secondary snippets, and the DOI was not opened. |
| 07.11 | FDA lists 'Games that simulate various cardiac arrest scenarios to train health professionals in advanced cardiopulmonary resuscitation' among software functions that are not medical devices (page current as of 09/29/2022). | https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices | This is the key regulatory basis for treating the game as a non-device. The guidance is nonbinding and can be revised. |
| 07.12 | Unity Personal is free for individuals and small organizations with less than $200K USD of revenue and funds raised in the last 12 months, and the splash screen can be customized. | https://unity.com/products/unity-personal | It confirms the engine license fits, and Unity has changed these terms several times since 2023. |

## 08 — Patient cases, complications and crisis management

**Key findings**

- Baseline rates for an average CABG patient: in the STS 2018 isolated-CABG development sample (439,092 records, 2011-2014), operative mortality was 2.4%, stroke 1.3%, renal failure 2.2%, prolonged ventilation 9.3%, reoperation 2.4%, DSWI 0.3% and composite morbidity/mortality 15.0%. The models predict mortality and renal failure well (c 0.80-0.83) but reoperation (0.62) and stroke (0.70) poorly.
- STS candidate predictors for the patient schema: age, sex, BMI/BSA, EF, dialysis/creatinine, diabetes and how it is controlled, chronic lung disease, status, PCI history and timing, previous CABG, shock/ECMO, IABP, inotropes, left main and proximal LAD disease, valve disease. The calculator only requires age and sex; blank fields are imputed.
- Anatomy variant frequencies: right dominance 72-90%, left 8-33%, co-dominance 3-7%. Intramyocardial LAD 11.5-21.7%. Porcelain aorta 2-9.3% of elective CABG. Major re-entry injury at redo sternotomy 2.8% (6,627 cases), with mortality 18.6-26% after injury in older series. No incidence data were found for LIMA injury, poor veins or small targets.
- Arrest after cardiac surgery (STS 2017 and ERC 2021) differs from standard ACLS: 3 shocks within about 1 minute (success 78%, then 35%, then 14%); DDD pacing at 80-100/min with maximum output; no routine epinephrine; amiodarone 300 mg after 3 failed shocks; resternotomy within 5 minutes; six team roles; a 5-item resternotomy set. About half of these patients survive.
- Perfusion rules backed by guidelines: ACT above 480 s (above 400 s with maximal-activation tests). Heparin resistance means more than 500 U/kg is needed to reach ACT 480 s (incidence 4-26%). For HIT, bivalirudin 1 mg/kg bolus, 2.5 mg/kg/h infusion and 50 mg in the prime, with ACT above 300 s. Protamine-to-heparin ratio below 1.0 and never above 2.6 mg per 100 U. Arterial outlet below 37 C; temperature gradient no more than 4 C and rewarming no faster than 0.5 C/min once outlet is 30 C or warmer. DO2 at least 280 mL/min/m2. Transfuse on CPB if HCT is below 18%. Systolic pressure below 100 mmHg during cannulation.
- The AmSECT massive air embolism template gives an ordered protocol: stop the pump, clamp and ventilate; Trendelenburg and carotid compression; move the venous cannula to the SVC; retrograde perfusion at 1-2 L/min for 1-2 minutes with the root vent on; FiO2 100%; restart CPB at higher flow and pressure; consider about 45 minutes of hypothermia. Mills and Ochsner outcomes: 4 of 13 patients died instantly.
- Iatrogenic dissection occurs in 0.06-0.6% of cases depending on cannulation site, with about 30% mortality if recognised and more than double if missed. Oxygenator change-out historically ran about 1 per 4,000 cases in UK surveys. Vasoplegia occurs in 5-45%, with drug-dose tables available. PC-ECLS is used in 0.3-3.6% of cases with about 34% survival; forcing weaning with high-dose inotropes is Class III.
- Usable outcome effect sizes: CPB time OR 1.57 per 30 min for death (snippet only). RBC transfusion OR 1.77 for mortality, 2.06 for renal failure and 1.79 for prolonged ventilation. Post-CPB MAP below 65 mmHg gives OR 1.12 per 10 min for new RRT. Reoperation for bleeding: 30-day mortality 4.8% vs 2.2%. These are observational and overlap, so the model needs a shrinkage factor.
- Team evidence: guidelines recommend pre-CPB and weaning checklists (Class I). Five cardiac crisis checklists exist: CPB failure, systemic air embolism, venous air lock, protamine reaction and heparin resistance; their steps are not published. Crisis checklists cut missed life-saving steps from 23% to 6%. A structured handover cut technical errors from 6.24 to 1.52 per handover. Teamwork failures were the strongest predictor of errors in the cardiac OR.
- Licences: the EACTS 2024 CPB guideline is CC BY-NC-ND 4.0. The vasoplegia review is CC BY 4.0. The Stanford Emergency Manual is CC BY-NC-ND, version not verified. The CC BY-NC-SA 4.0 licence for the Ariadne checklists is not verified (third-party copy only). STS and AmSECT documents state no open licence. Pulse Physiology Engine 4.4.0 is Apache-2.0 and includes an ECMO model.

**Recommendations**

- Use the STS 2018 isolated-CABG rates as the stored baseline (outcomeBaselines.json). Make reoperation and stroke depend mostly on in-game events, because STS discrimination for those two is weak.
- Author 12 patient profiles from STS predictors, covering very low to very high risk, redo, dialysis, shock, porcelain aorta, IMLAD, HIT and RV dysfunction. Calibrate each one by hand in the official STS calculator. The calculator host could not be reached from this session and must be allowed or used by the owner.
- Implement the 20 intraoperative events using the shared schema (cause, incidence, signs, ordered role-based steps, clock, mishandling modifier) and the default per-case probabilities in section 2.21.
- Implement the ICU arrest scenario exactly as the STS 2017 / ERC 2021 protocol. It has the clearest timings (1-minute shocks or pacing, 5-minute resternotomy) and suits a role-assignment team mini-game.
- Encode the anticoagulation, temperature, DO2/HCT and protamine rules as hard UI constraints and alarms, for example a 'Go on bypass' button locked until ACT exceeds 480 s.
- Build the outcome model as baseline log-odds plus a shrinkage factor (start at 0.6) times the sum of ln(OR) times exposure. Show each modifier's contribution in the debrief, and tune it so a messy typical case stays near the STS composite rate of 15%.
- Re-write all checklist and protocol text in original wording, keep a credits page with source links, and treat NC-ND sources (EACTS 2024 CPB, Stanford Emergency Manual) as read-only references.
- Add closed-loop read-back, pre-bypass and weaning checklists, and an end-of-case ICU handover mini-game. Missed items should create hidden latent errors that can surface later.

**Open questions**

- Exact STS predicted risk values for each authored profile. This needs manual use of the calculator and a review of its terms and conditions, which were not read.
- EuroSCORE II coefficients, which could serve as an open-formula alternative to STS, were not verified.
- The step contents of the Tarola five cardiac crisis checklists and of the EACTS 2024 weaning checklist (Supplementary Appendix 6) were not read.
- The massive-bleeding product algorithm (fibrinogen, platelets, PCC, viscoelastic thresholds) in the 2024 EACTS/EACTAIC patient blood management guideline was not read.
- The internal defibrillation energy for adult open-chest shocks (commonly quoted as 10-20 J) is unverified.
- No incidence data were found for LIMA injury, poor veins, small or diffuse targets, RV failure at weaning, coronary air embolism or cardioplegia hyperkalaemia.
- The official licence pages for the Stanford Emergency Manual (returned HTTP 503) and the Ariadne OR crisis checklists (projectcheck.org returned no text) need to be checked.
- Whether the Koch 2006 odds ratios are per unit of RBC transfused or per transfused patient; per unit is suggested by a secondary citation but not confirmed.
- The full Salis 2008 paper, to confirm OR 1.57 per 30 min of CPB and to get cross-clamp-specific effect sizes.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 08.1 | STS 2018 isolated CABG development-sample rates: operative mortality 2.4%, stroke 1.3%, renal failure 2.2%, prolonged ventilation 9.3%, reoperation 2.4%, DSWI 0.3%, composite 15.0% | https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf | This is the baseline of the whole outcome model. If it is wrong, every computed outcome shifts. |
| 08.2 | In the PDF text, peri-arrest epinephrine 'smaller doses (eg, 50 to 300 mg boluses)' reads as mg; micrograms are almost certainly intended | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A unit error here would produce a 1000-fold dose error in game data. |
| 08.3 | Sequential shock success after cardiac surgery is 78% for the first shock, 35% for the second and 14% for the third; resternotomy within 5 minutes; amiodarone 300 mg after 3 failed shocks, then 150 mg, then 900 mg over 24 h | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | These numbers drive the core arrest mini-game timings and its probability of success. |
| 08.4 | Bivalirudin for HIT on CPB: 1 mg/kg bolus, 2.5 mg/kg/h infusion, 50 mg in prime, ACT about 2.5x baseline (>300 s); argatroban 0.1 mg/kg bolus then 5-40 ug/kg/min | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | These are doses shown to players. They come from a long PDF extraction and should be double-checked. |
| 08.5 | Heparin resistance is defined as more than 500 U/kg heparin to reach ACT 480 s, with incidence 4-26%; AT concentrate comes in 500 IU vials with the formula (target% - current%) x kg / 1.4 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/ | This sets the trigger and the treatment math for a frequent game event. The source is a review, not a guideline. |
| 08.6 | Temperature rules: arterial outlet below 37 C; gradient no more than 10 C; no more than 4 C and rewarming no faster than 0.5 C/min when outlet is 30 C or warmer | https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ | These are hard UI alarm thresholds, and secondary summaries disagree on the 4 C and 10 C figures. |
| 08.7 | DO2 of at least 280 mL/min/m2 is Class I, Level A to reduce AKI; transfuse on CPB if HCT is below 18% (Hb 6.0); do not transfuse if HCT is above 24% with adequate DO2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | These drive the perfusion scoring and transfusion rules. The class and level were read from PDF text extraction. |
| 08.8 | CPB duration OR 1.57 per 30 min for in-hospital death (Salis 2008, 5,006 patients) | https://db.cngb.org/search/literature/18948034 | This is the largest modifier in the outcome model, and it was seen only as a snippet. |
| 08.9 | RBC transfusion OR 1.77 for mortality, 2.06 for renal failure and 1.79 for prolonged ventilation, applied per unit transfused | https://pubmed.ncbi.nlm.nih.gov/16607235/ | If these odds ratios are per transfused patient rather than per unit, the model over-penalises multi-unit transfusion. |
| 08.10 | The 2024 EACTS/EACTAIC/EBCP CPB guideline is licensed CC BY-NC-ND 4.0 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | No-derivatives limits how the guideline text may be reused in the game. |
| 08.11 | The Ariadne Labs OR Crisis Checklists are CC BY-NC-SA 4.0 (third-party copy, April 2017 revision) | https://www.scribd.com/document/518857653/Or-Crisis-Checklists-Harvard | The licence is unverified on the official site, and share-alike would affect how the game may be distributed. |
| 08.12 | PC-ECLS is used in 0.3-3.6% of cardiac surgery with 34% survival to discharge; start support before lactate reaches 4 mmol/L | https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf | This drives the failure-to-wean branch and the survival odds for the ECMO/VAD path. |

## 09 — Anatomy and tissue biomechanics data

**Key findings**

- Chamber and wall norms are well sourced (ASE/EACVI 2015, CMR 2020). LV wall is 0.6-1.0 cm in men and 0.6-0.9 cm in women. RV wall is 3 ± 1 mm. LV EDV by CMR is 155 ± 30 mL in men and 123 ± 22 mL in women. Aortic annulus is 26 ± 3 mm in men and 23 ± 2 mm in women. Proximal ascending aorta is 30 ± 4 mm in men and 27 ± 4 mm in women.
- Heart weight in healthy young men (n=232) is 331 ± 56.7 g, with a 95% reference range of 233-383 g. LV mass by CMR is 121 ± 28 g in men and 83 ± 21 g in women. The female whole-heart default of about 226-272 g is derived, not measured.
- Coronary lumen sizes from Dodge 1992: LM 4.5 mm, proximal LAD 3.7 mm, distal LAD 1.9 mm. Women's arteries are about 9% smaller. Proximal RCA (2.8-3.9 mm) and LCx (3.4-4.2 mm) sizes depend on dominance. Typical bypass target is 2.14 ± 0.52 mm, and targets under 1.5 mm are a risk factor for graft occlusion.
- Coronary dominance in 4,000 angiograms: right 85.5%, left 9.7%, co-dominant 4.8%. LAD length is about 105 mm and LM length about 12.6 mm (cadaver study, n=60).
- Conduits (Otsuka 2013): IMA is 1.9-2.6 mm wide with a 180-430 µm wall. SVG is 3.1-8.5 mm wide with a 180-650 µm wall. Burst pressure is 3,196 mmHg for IMA and 1,599 mmHg for SV (König 2009). Suture retention is about 1.35-1.72 N for IMA and 1.92 N for SV.
- Sternum by CT (n=200): total length is 154 mm in men and 133 mm in women. Body thickness is about 8-9 mm. Each pericardial layer is 0.5-1.0 mm thick (under 2 mm on CT), with 20-25 mL of fluid. Epicardial fat has no agreed normal value; it is about 5-7 mm over the RV and thickest in the AV and interventricular grooves.
- Myocardium: the Holzapfel-Ogden (HO) parameter sets are tabulated, including HO2009 and an averaged set (a 0.28 kPa, af 18.1 kPa, bf 16.5). A fit to human data (Sommer) is also available. The Land 2015 benchmark uses an active fibre stress of 60 kPa at 15 kPa cavity pressure.
- Measured interaction forces: needle puncture of porcine heart wall takes 1.37 N at 1 mm/s and 0.88 N at 100 mm/s. Sternal retraction to 10 cm takes about 223-226 N on average and up to 349 ± 78 N (individual maximums ranged 159-494 N). No measured forceps grasp forces were found.
- Coronary motion (biplane angiography): a point 5 cm down the LAD moves 9.6 mm per beat at a peak of 47.5 mm/s. The mid RCA moves 26.3 mm at 130.7 mm/s. The heart shifts about 4.9 mm head-to-foot per breath. LV peak twist is 10-19° and rises with age. Stabilisers reduce motion by about 76-81% (snippet only).
- Blood viscosity is about 4 cP at Hct 40%. It is about 25% lower at Hct 30%. One source gives about +2% per °C of cooling, but measured data suggest about +3% per °C (2.44 to 6.07 cSt from 37 to 6 °C).
- STS/SCA/AmSECT 2018 guideline: an ACT above 480 s on CPB is reasonable (IIa). Above 400 s is often accepted on maximally activated devices. Protamine should stay below 2.6 mg per 100 U of heparin. A 300 IU/kg heparin bolus is common practice.
- Bleeding rates from specific surgical wounds are poorly documented. Needle-hole leaks were 20-57 mL/min per test anastomosis ex vivo (snippet only). An orifice-flow model, Q = Cd·A·sqrt(2ΔP/ρ), gives calibrated estimates, for example about 140 mL/min through a 1 mm arterial hole.
- Licences: the TotalSegmentator dataset v3.0.0 (2026-09-10) is CC BY 4.0, with 1,939 CT scans and 117 structures. TotalSegmentator code v2.18.0 is Apache-2.0, but the heart-chamber and coronary sub-models need a free non-commercial licence. 3D Slicer 5.12.4 uses a BSD-style licence. MONAI 1.6.1 is Apache-2.0. Visible Human data falls under NLM Terms (2019) and needs the credit line 'Courtesy of the U.S. National Library of Medicine'. ASOCA is closed access on the UK Data Service (UKDS). The ImageCAS and MM-WHS data licences are UNVERIFIED.

**Recommendations**

- Turn the section 6 parameter table into the first data file (anatomy_defaults.json). Give every value a source and an evidence grade.
- Build two reference patients (male, BSA about 1.9; female, BSA about 1.6). Add a variant generator for dominance (85/10/5), epicardial fat thickness and target-vessel diameter, with targets under 1.5 mm marked as poor.
- Use the HO law with the averaged parameter set offline to make reference stress-strain curves. Fit the real-time XPBD or Neo-Hookean model to those curves. Treat peak active stress (default 60 kPa, range 30-120) as a tuning knob matched to EF and wall thickening.
- Before tuning gameplay feel, unit-test the soft-body solver against the Land 2015 ellipsoid benchmarks.
- Gameplay thresholds: needle puncture about 1.1 N, falling at higher speed. Stitch tear-out at about 1.4 N (IMA) and 1.9 N (SV). Graft rupture at the burst pressure. A complication flag when retractor force exceeds about 350 N.
- Beating-heart mode: LAD motion of about 10 mm at about 48 mm/s, cut by about 80% with a stabiliser. Make RCA targets the hard level. Reward placing stitches in the mid-diastolic quiet window.
- Coagulation state machine: 300 IU/kg heparin, ACT above 480 s before CPB, protamine 1 mg/100 U capped at 2.6. Model bleeding as orifice flow times a coagulation factor, capped by upstream flow.
- Mesh pipeline: TotalSegmentator dataset (CC BY 4.0), then TotalSegmentator (get the free non-commercial licence for heartchambers_highres and coronary_arteries), then 3D Slicer 5.12.4, then Blender. Credit NLM for any Visible Human reference. Avoid ASOCA and ImageCAS until their licences are confirmed.
- Re-verify every value graded C or marked UNVERIFIED before it drives a scoring rule. The web-search budget ran out during this research, and a follow-up search session could close several gaps.

**Open questions**

- Atrial wall thickness and normal diameters of diagonal, OM and PDA branches were not verified.
- UDPB chest-tube mL thresholds per bleeding class are UNVERIFIED. No measured bleeding rates were found for cannulation sites or arteriotomies.
- Human ascending aorta UTS in MPa (Pichamuthu 2013 full text) and coronary intima/media UTS were not found. The coronary adventitia value of 1.3-1.4 MPa is snippet-only.
- No needle insertion force was found for coronary or vessel wall (only myocardium), and no measured forceps grasp forces in cardiac surgery.
- USP <881> knot-pull minimums for 4-0 to 7-0 polypropylene were not verified.
- Sternum-specific bone properties and wire cut-through force are missing. Rib cortical bone is being used as a proxy.
- All motion data are closed-chest. How the heart moves with the chest open and on a ventilator is undocumented here.
- ImageCAS and MM-WHS data licences are unverified. The ASOCA licence conflicts: the UKDS End User Licence (closed) versus a reported CC BY 4.0.
- No Mooney-Rivlin parameter sets for cardiac tissues were verified.
- Pericardium UTS values conflict: 3.14 MPa versus 22 MPa for untreated tissue in two studies with different protocols.

**Claims flagged for verification in Step 2**

| # | Claim | Source | Why it matters |
|---|---|---|---|
| 09.1 | Holzapfel-Ogden 2009 myocardium parameters: a=0.059 kPa, b=8.023, af=18.472 kPa, bf=16.026, as=2.481 kPa, bs=11.120, afs=0.216 kPa, bfs=11.436. Averaged literature set: a 0.28, b 8.82, af 18.1, bf 16.5, as 3.0, bs 9.5, afs 0.4, bfs 10.9. | https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751 | This is the core passive material default for the heart. The values came from a flattened table and could be transposed. |
| 09.2 | Sommer human-data fit of the reduced HO model: a=0.809 kPa, b=7.474, af=1.911 kPa, bf=22.063, an=0.227 kPa, bn=34.802, afs=0.547 kPa, bfs=5.691. | https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/ | This is the only human-tissue parameter set. The fetch tool warned that column alignment came from a flattened table. |
| 09.3 | Needle rupture force in porcine heart wall (1.1 mm tri-pointed needle) is 1.37 ± 0.11 N at 1 mm/s and 0.88 ± 0.08 N at 100 mm/s. | https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196 | It sets the haptic and visual puncture threshold for every stitch. |
| 09.4 | Sternal retractor maximum total force for full retraction to 10 cm is 349.4 ± 77.9 N. Mean first-retraction force is 222.8 N (straight) and 226.4 N (curved). Individual maximums ranged 159-494 N. | https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560 | It sets the retractor complication threshold. Part of the detail came from a secondary citing paper. |
| 09.5 | Native burst pressure is 3,196 ± 1,264 mmHg for IMA (n=16) and 1,599 ± 877 mmHg for SV (n=7). IMA suture retention is 138 ± 50 gf. | https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094 | It sets graft failure rules. The paper's own n values are inconsistent (Methods say 18 IMA and 4 SV). |
| 09.6 | Compiled native-vessel values: ITA burst 3,073 mmHg, suture retention 1.72 N, compliance 11.5%/100 mmHg. SV burst 2,134 mmHg, suture retention 1.92 N, compliance 25.6%/100 mmHg. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/ | It sets stitch tear-out thresholds and the derived wall stiffness. It is a secondary compilation whose original references were not traced. |
| 09.7 | Blood viscosity is about 4 cP at Hct 40%, about 25% lower at Hct 30%, about 45% lower at Hct 20%, and rises about 2% per 1 °C of cooling. | https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/ | It drives the perfusion and bleeding models. The review gives no primary source, and the per-degree figure conflicts with Stammers 2003 measurements (about 3% per °C). |
| 09.8 | STS/SCA/AmSECT 2018: maintaining ACT above 480 s during CPB is reasonable (Class IIa). Above 400 s is acceptable on maximally activated devices. Protamine should be limited to below 2.6 mg per 100 U heparin. | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | These are the core rules of the coagulation state machine. The class and LOE labels should be checked against the guideline PDF. |
| 09.9 | TotalSegmentator dataset v3.0.0 (published 2026-09-10) is CC BY 4.0, with 1,939 CT scans, 117 structures and 37.4 GB. | https://zenodo.org/records/6802613 | It is the recommended mesh source data. The version and date are very recent and the licence must be correct. |
| 09.10 | TotalSegmentator code is Apache-2.0 (v2.18.0, 2026-08-12). The heartchambers_highres, coronary_arteries and aortic_sinuses tasks need a separate licence, free for non-commercial use. | https://github.com/wasserth/TotalSegmentator | It decides whether heart-chamber and coronary segmentation can be used for free. The weight licence terms were not read in full. |
| 09.11 | ASOCA data files on the UK Data Service are closed access under the UK Data Service End User Licence and need owner permission. The Scientific Data paper metadata reportedly lists CC BY 4.0. | https://reshare.ukdataservice.ac.uk/855916/ | The two licence statements conflict. This decides whether the best open coronary dataset with meshes is usable. |
| 09.12 | Human LAD adventitia ultimate tensile stress is about 1,430 ± 604 kPa circumferential and 1,300 ± 692 kPa axial, about 3 times that of media and intima. | https://scite.ai/authors/gerhard-holzapfel-wmX1ny | It is the coronary tear threshold and is snippet-only. The original Holzapfel 2005 AJP-Heart paper was not read. |

