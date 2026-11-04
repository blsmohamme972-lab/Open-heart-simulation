# Research 02: Physiology, anesthesia and perfusion

> **Purpose:** This report gathers evidence for the physiology, anesthesia and perfusion layer of a realistic open-heart surgery simulation game. The game is personal, non-commercial and educational. It is not a certified medical device. The report covers: (1) open-source physiology engines, (2) the cardiopulmonary bypass (CPB) circuit and its targets, (3) the vital signs to show and how they react to surgical events, (4) anesthesia and vasoactive drugs with doses usable in a pharmacodynamic model, and (5) a recommended modelling approach.
>
> **Researched 2026-11-03 (re-do, fresh searches).** All facts come from searches and page reads done on this date. Older reports in `docs/plan/` were not read.
>
> **Disclaimer:** This is **not clinical guidance**. Doses, targets and thresholds are collected to make a game behave realistically. They are simplified and must never be used to treat a patient. Where sources disagree, both values are given. "(uncertain)" marks values I could not confirm. "(uncertain - snippet only)" marks values seen only in a search-result snippet because the page itself could not be fetched. "(design estimate)" marks values I propose for gameplay tuning that no source states directly.

**Abbreviations (defined once):** ABG = arterial blood gas; ACT = activated clotting time; AF = atrial fibrillation; AKI = acute kidney injury; BIS = bispectral index; BSA = body surface area; CI = cardiac index; CO = cardiac output; CPB = cardiopulmonary bypass; CVP = central venous pressure; DO2(i) = oxygen delivery (indexed to BSA); ECG = electrocardiogram; ECMO = extracorporeal membrane oxygenation; EtCO2 = end-tidal carbon dioxide; Hb = haemoglobin; Hct = haematocrit; HTK = histidine-tryptophan-ketoglutarate (Custodiol); MAP = mean arterial pressure; NIRS = near-infrared spectroscopy (cerebral oximetry, rScO2); PA = pulmonary artery; PCWP = pulmonary capillary wedge pressure; PD = pharmacodynamics; PK = pharmacokinetics; SvO2 = mixed venous oxygen saturation; SVR = systemic vascular resistance; VF = ventricular fibrillation; XC = aortic cross-clamp.

**Evidence grades:** A = primary or authoritative (guideline, peer-reviewed paper, textbook, official docs or license page). B = reputable secondary (university or society teaching page, vendor page, review summary). C = weak (blog, forum, video, search snippet).

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Physiology core | **Hybrid.** Write a custom real-time lumped (0-D) model that includes the CPB circuit. Use the Kitware Pulse engine as an offline reference ("oracle") to check pre-bypass and post-bypass behaviour, and optionally as the live engine for those phases. | Pulse has no CPB or cardiac surgery model ([Pulse CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). Its ECMO pump is an "ideal flow source" with no anticoagulation model ([Pulse ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). |
| Engine license | Pulse is Apache-2.0. Personal and commercial use are allowed. Keep the LICENSE and NOTICE files. No share-alike. | [Pulse home](https://pulse.kitware.com/), [NOTICE](https://gitlab.kitware.com/physiology/engine/-/raw/stable/NOTICE) |
| Pulse version to pin | Pulse 4.4.0 (listed as August 2026). The free Unity asset is 4.3.1 (5 Feb 2025). | [Pulse versions](https://pulse.kitware.com/version.html), [Unity Asset Store](https://assetstore.unity.com/packages/slug/139773) |
| Solver rate | Physiology step 20 ms (50 Hz), the same as Pulse. Up to 40 ms is acceptable; above 60 ms is unreliable. | [Pulse about](https://pulse.kitware.com/_about_pulse.html), [Kitware forum](https://discourse.kitware.com/t/changing-step-size/1068) (C) |
| Heart model | Use a time-varying elastance heart with **four chambers**, because Pulse models only the ventricles (no atria, so no real AF). | [Pulse CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html), [Suga & Sagawa 1973](https://scilit.net/publications/7c0ae8fc02a2142815b3b1438ddbad30) |
| Arterial tree | Use a 3-element Windkessel (characteristic impedance + resistance + compliance). | [Westerhof 2009](https://pubmed.ncbi.nlm.nih.gov/18543011/) |
| Reflexes | Use an Ursino-type baroreflex (heart rate, resistance, venous unstressed volume). | [Ursino 1998 index](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985) (C) |
| ECG | Synthesize ECG with a McSharry-type ODE model, **re-implemented from the paper** (ECGSYN code is GPL-3.0). | [PhysioNet ECGSYN](https://physionet.org/content/ecgsyn/) |
| Pump flow rule | 2.2-2.8 L/min/m² at moderate hypothermia to normothermia. Score DO2i ≥ 280 mL/min/m². | [EACTS/EACTAIC/EBCP 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| MAP rule on CPB | 50-80 mmHg (Class I, Level A). Pushing MAP above 80 mmHg with vasopressors is "not recommended" (Class III). | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Temperature rules | Arterial outlet ≤ 37 °C. Arterial-venous gradient ≤ 10 °C. When outlet ≥ 30 °C: gradient ≤ 4 °C and rewarming ≤ 0.5 °C/min. | [STS/SCA/AmSECT 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/), [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Transfusion rule on CPB | Transfuse red cells if Hct < 18% (Hb 6.0 g/dL). Consider at 18-24%. Do not transfuse if Hct > 24% with adequate DO2. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Anticoagulation | Heparin 300-400 IU/kg. ACT > 480 s before and during CPB (> 400 s with some assays). Protamine:heparin ratio < 1.0. | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/), [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Cardioplegia options | Offer three: Buckberg 4:1 blood (every 15-30 min), del Nido 1:4 (20 mL/kg, max 1000 mL, up to 90 min), and HTK (single dose perfused over 6-8 min, about 1.5-2 L in adults per the UK SmPC; manufacturer brochure 20-25 mL/kg; the label states no protection time, and 120-180 min appears only in manufacturer material) [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-6]. | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf), [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [Custodiol trial](https://clinicaltrials.gov/study/NCT01681095) (C) |
| Acid-base | Default to alpha-stat in adults (Class IIa). Offer pH-stat as an option that adds CO2 to the sweep. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Drug PK/PD | Use an effect-compartment PK/PD model (Emax/Hill). Take half-lives from the sources. Use Eleveld parameters for propofol. | [Eleveld 2018](https://pesquisa.bvsalud.org/ses/resource/pt/mdl-29661412) (C), [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/) |
| Arrest after surgery | Use the CALS rules: 3 stacked shocks, re-sternotomy within 5 min, internal defibrillation 20 J, epinephrine 50-100 µg rather than 1 mg. | [CALS-ANZ 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) |

---

## 1. Open-source physiology engines and models

### 1.1 Comparison table

| Engine / model | Version and date | License (verified?) | Personal use? | Attribution / share-alike | APIs and game integration | CPB / ECMO | Arrest / arrhythmia | Hemorrhage | Drugs | Maturity / notes |
|---|---|---|---|---|---|---|---|---|---|---|
| **Kitware Pulse Physiology Engine** | 4.4.0, listed as "Aug 2026" ([versions](https://pulse.kitware.com/version.html)). 4.3.1 Jan 2025, 4.3.0 Sep 2024 ([versions](https://pulse.kitware.com/version.html)). | Apache-2.0, verified ([Pulse home](https://pulse.kitware.com/); [NOTICE](https://gitlab.kitware.com/physiology/engine/-/raw/stable/NOTICE)) | Yes | Attribution: keep the LICENSE and NOTICE and mark your changes. No share-alike. | C++ core. Interfaces for C, C#, Java and Python ([Pulse home](https://pulse.kitware.com/)). Free Unity asset 4.3.1 under the **Standard Unity Asset Store EULA** ([Asset Store](https://assetstore.unity.com/packages/slug/139773)). Free Unreal plugin as an Actor Component for Blueprints, first built for UE 4.26/5.0 ([Kitware 2022](https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/)). | ECMO VV/VA device model is new in 4.4.0. It uses an ideal flow source and has no anticoagulation, thrombosis or hemolysis. No CPB ([ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). | Asystole, PEA, coarse and fine VF, VT, pulseless VT and CPR are modelled. The ECG is a stored waveform, not computed from cardiac electrical activity ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). | Yes: flow-rate or severity model. Hypovolemic shock is defined as a 35% blood-volume loss ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). | 17 validated drugs, including etomidate, epinephrine, fentanyl, ketamine, midazolam, morphine, propofol, rocuronium, succinylcholine, norepinephrine and phenylephrine. **Not listed:** vasopressin, heparin, protamine, amiodarone, lidocaine, milrinone, dobutamine ([Drugs methodology](https://pulse.kitware.com/_drugs_methodology.html)). | Most mature open option. Fork of BioGears 6.1.1 ([NOTICE](https://gitlab.kitware.com/physiology/engine/-/raw/stable/NOTICE)). 20 ms step ([about](https://pulse.kitware.com/_about_pulse.html)). Runs "10-15x real time" on laptops ([forum](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547)) (C). |
| **BioGears** (Applied Research Associates) | The README lists 8.2.0 as "January 2025" ([GitHub](https://github.com/BioGearsEngine/core)). The Releases page shows "8.2.0, 12 Dec" with no year ([releases](https://github.com/BioGearsEngine/core/releases)) (uncertain). | Apache-2.0, verified ([GitHub](https://github.com/BioGearsEngine/core)) | Yes | Same as Pulse | C++ with SWIG bindings; C# bindings since 7.5.0. Unreal compatibility work in 7.3.x ([releases](https://github.com/BioGearsEngine/core/releases)). | Not found | Not stated on the pages read | Not stated | Added drugs include TXA, Plasma-Lyte and naloxone ([releases](https://github.com/BioGearsEngine/core/releases)). | The 8.x line was called "experimental through May 2024" ([releases](https://github.com/BioGearsEngine/core/releases)). Smaller game ecosystem than Pulse. |
| **CircAdapt** (Maastricht) | Framework docs are labelled "2509" (inference: Sept 2025) ([install docs](https://framework.circadapt.org/latest/userguide/installation.html)). | **Custom EULA** (KTF B.V. for Maastricht University and Maastricht UMC+): free, revocable, for educational, non-commercial and research use by academic researchers only; no distribution of the framework or improvements without written permission ([license page](https://framework.circadapt.org/latest/license.html)). [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-4] | Only for academic researchers, non-commercial (EULA) | Unknown | C++ library + pyCircAdapt (Python) + CircAdaptUI ([Osta 2025](https://cris.maastrichtuniversity.nl/en/publications/the-circadapt-framework-create-fast-computational-models-of-cardi/)) (C). Web simulator described as "real-time" ([circadapt.org](https://www.circadapt.org/)). | No | No (mechanics-focused) | No | No | Excellent cardiac mechanics (chambers, valves, tissue adaptation) ([circadapt.org](https://www.circadapt.org/)). Do not link it until the license is confirmed. |
| **OpenCOR + CellML models** | No release listed on GitHub ([repo](https://github.com/opencor/opencor)) | OpenCOR app: **GPL-3.0** ([repo](https://github.com/opencor/opencor)). An older 2015 paper said Apache-2.0 (C). | Yes | GPL is copyleft: a game that ships GPL code must be GPL. | Desktop tool for running CellML models. Not a game runtime. | No | Model-dependent | Model-dependent | No | Use it to **study** published models such as Smith 2004 ([PMR CellML](https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml)) (C), then re-implement the equations. Per-model license: UNVERIFIED (one BioModels entry is said to be CC0 (uncertain - snippet only)). |
| **HumMod** | Windows model; download at hummod.org ([Frontiers 2011](https://www.frontiersin.org/articles/10.3389/fphys.2011.00012/pdf)) (C) | **UNVERIFIED.** Described in a forum as a "closed-source desktop app" ([forum](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547)) (C). | Unknown | Unknown | XML model files; no game API | No | Limited | Yes (integrative) | Some | Very broad (thousands of variables) but not built for real-time games. The Modelica port **Physiomodel** (based on HumMod 1.6.1) is "GPL 3.0 for everybody or BSD 3-clause between registered parties" ([GitHub](https://github.com/physiology/Physiomodel)) (uncertain - snippet only). |
| **Physiolibrary (Modelica)** | 3.0.0, 2023-10-09 (uncertain - snippet only) | BSD-3-Clause, except `Resources/*` ([license page](https://build.openmodelica.org/Documentation/Physiolibrary.UsersGuide.License.html)) (uncertain - snippet only) | Yes | Attribution only | Modelica; needs export (FMU) | Build your own | Build your own | Build your own | No | Good building blocks for prototyping in OpenModelica. |
| **Simple lumped models** (Windkessel, time-varying elastance, Smith 2004, Ursino 1998) | Papers from 1973-2009 | Equations are not copyrighted. Only copied *code* carries a license. | Yes | Cite the papers | Write in C#/C++ in the engine | Add yourself | Add yourself | Ursino: venous unstressed volume dominates the early hemorrhage response ([index](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985)) (C) | Add yourself | Fast, fully controllable, CPB-ready. **Recommended core.** |
| **ECGSYN** (ECG generator) | 1.0.0, 3 Dec 2003 ([PhysioNet](https://physionet.org/content/ecgsyn/)) | **GPL-3.0** ([PhysioNet](https://physionet.org/content/ecgsyn/)) | Yes | Copyleft if the code is distributed | Matlab/Octave, C, Java | n/a | Morphology parameters for P, Q, R, S and T waves, plus HRV ([PhysioNet](https://physionet.org/content/ecgsyn/)) | n/a | n/a | Re-implement from McSharry et al., IEEE TBME 2003 (50(3):289-294) to avoid GPL. |
| **MIT-BIH Arrhythmia Database** (reference ECG data) | 1.0.0, 24 Feb 2005 ([PhysioNet](https://physionet.org/content/mitdb/1.0.0/)) | ODC Attribution License v1.0 ([PhysioNet](https://physionet.org/content/mitdb/1.0.0/)) | Yes | Attribution required; no share-alike | Data files (48 half-hour 2-lead records) | n/a | Real arrhythmia examples to tune waveforms | n/a | n/a | Use it to check the synthetic ECG by eye. |

### 1.2 What Pulse can and cannot do for an open-heart game

**Strengths (useful directly):**
- Validated whole-body model with "zero-dimensional lumped-parameter circuit analogs" for all major systems ([about](https://pulse.kitware.com/_about_pulse.html)).
- ACLS arrhythmias with ECG waveforms since 4.1.0 (Mar 2022): asystole, VF, PEA and VT ([versions](https://pulse.kitware.com/version.html)).
- Anesthesia machine, mechanical ventilator and ECMO device models ([Pulse home](https://pulse.kitware.com/)).
- ECMO sweep-gas behaviour is validated: PCO2 falls from about 70 mmHg at 2 L/min sweep to about 25 mmHg at 10 L/min ([ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). This is a good sanity check for our own oxygenator model.
- Unity and Unreal integration exists and is free ([Asset Store](https://assetstore.unity.com/packages/slug/139773); [Kitware 2022](https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/)).

**Gaps (each needs custom work):**
1. **No CPB model.** The cardiovascular page does not model cardiac surgery or bypass ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). The ECMO pump is an "ideal flow source" with no pressure-flow curve. It does "not simulate anticoagulation requirements, circuit thrombosis, hemolysis" ([ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). There is no venous reservoir, no cross-clamp, no cardioplegia arrest and no heat exchanger.
2. **Ventricles only.** "The atria are not included in the heart model" ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). Post-operative AF and atrial pacing therefore cannot be modelled mechanically.
3. **ECG is not electrical.** It is a stored one-cycle waveform stretched to the cycle length ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). ST changes and heart block would need custom templates.
4. **PD simplifications.** Emax means "the expected effect of the drug rather than the maximum effect", so "overdose is not possible for most drugs". EC50 values "were unknown for the majority of the drugs" and were estimated from peak concentration. The page also says "the plasma concentration calculation is currently incorrect" ([Drugs methodology](https://pulse.kitware.com/_drugs_methodology.html)).
5. **Missing cardiac drugs** (see the table in 1.1).
6. **Validation is imperfect.** The validation summary shows 28 "Bad" results (> 30% deviation) for the standard male and 53 for the standard female ([about](https://pulse.kitware.com/_about_pulse.html)).

**Performance:** default step 20 ms, "which can be reduced, as necessary" while keeping real-time execution ([about](https://pulse.kitware.com/_about_pulse.html)). Developers say 0.04 s is "pretty ok" and that above 0.06 s results become "pretty unreliable" ([forum](https://discourse.kitware.com/t/changing-step-size/1068)) (C). Throughput is about "10-15x real time" ([forum](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547)) (C).

### 1.3 Classic lumped models to build the custom core

| Model | Key idea | Numbers useful for tuning | Source |
|---|---|---|---|
| Time-varying elastance (Suga & Sagawa 1973) | E(t) = P(t) / [V(t) − Vd]. Emax is load-independent and tracks contractility. | Epinephrine raised Emax from about 6.6 to 12.2 mmHg/mL (dog LV, n = 9). Heart rate shortened Tmax without changing Emax. | [Suga & Sagawa 1973](https://scilit.net/publications/7c0ae8fc02a2142815b3b1438ddbad30) (C) |
| 3-element Windkessel (Westerhof) | Resistance + compliance + characteristic impedance. The 2-element model explains diastolic decay but "fell short in systole". | Parameter values are not extracted here. Fit them to the normal ranges in §3. | [Westerhof 2009](https://pubmed.ncbi.nlm.nih.gov/18543011/) |
| Minimal haemodynamic model (Smith, Chase et al. 2004) | Closed loop with ventricular interaction. Valves "open on pressure, close on flow". Built to run fast at the bedside. | CO falls about 9% when thoracic pressure rises from −4 to 0 mmHg. BP goes from 120/80 to 165/130 mmHg when SVR doubles. | [Med Eng Phys 26(2):131-139](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_71751123) (C); [CellML](https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml) (C) |
| Carotid baroreflex (Ursino 1998) | Reflex control of HR, resistance, contractility and venous unstressed volume. | Venous unstressed volume control "plays the major role in the early hemodynamic response to acute hemorrhage". | [Am J Physiol index](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985) (C) |
| CPB training simulators (Riley & O'Kane 1977, Orpheus, ECCSIM, Tokaji) | Lumped circulation + time-varying elastance + baroreflex + plasma refilling, driven by a heart-lung machine model. | Tokaji: 4 control parameters reproduce hypertensive, stable and hypotensive patterns at CPB initiation and weaning. | [Perfusion.com summary](https://perfusion.com/an-educational-training-simulator-for-advanced-perfusion-techniques-using-a-high-fidelity-virtual-patient-model/) (B); [search summary](https://perfusion.com/?p=38318) (C) |

---

## 2. Cardiopulmonary bypass circuit

Main sources: the **2024 EACTS/EACTAIC/EBCP Guidelines on CPB in adult cardiac surgery** (Wahba et al., Br J Anaesth 2025;134(4):917-1008, doi 10.1016/j.bja.2025.01.015; also published in EJCTS) ([PMC11947607](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). This revises the **2019 EACTS/EACTA/EBCP guideline** ([PMC10634377](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/)). The US sources are the **STS/SCA/AmSECT** guidelines on temperature (2015) ([PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)) and anticoagulation (2018) ([PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)). The AmSECT site lists the STS/SCA/AmSECT guideline series ([AmSECT](https://amsect.org/Policy-Practice/Perfusion-Safety/STS-SCA-AmSECT-Guidelines)) (B).

### 2.1 Components (what the player sees and controls)

| Component | Function and facts | Game-relevant numbers | Source |
|---|---|---|---|
| Venous cannula(s) and drainage | Drain from the right atrium or SVC/IVC. Gravity drainage or vacuum-assisted venous drainage (VAVD). | VAVD up to −60 mmHg showed no added hemolysis. −80 mmHg increased hemolysis. Monitoring venous-line negative pressure with VAVD is Class I. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Venous reservoir (open hard-shell or closed bag) | Holds the drained blood. Open: easy drug access but a blood-air interface. Closed: more sterile, lower capacity, needs a separate suction circuit. | One study: priming volume 1180 mL (closed) vs 760 mL (open). | [OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/) (B); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Arterial pump: roller or centrifugal | Roller pumps squeeze tubing. Centrifugal pumps spin cones and are "gentler on blood cells". A meta-analysis found no outcome difference. | Example setup: Sarns or Revolution centrifugal main pump; Stockert S5 rollers for cardioplegia, vent and suction. | [OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/) (B); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Membrane oxygenator | Microporous polypropylene hollow fibres. O2 is set mainly by FiO2; CO2 removal is set by sweep flow. Polymethylpentene membranes pass volatile anesthetics poorly, which risks awareness if volatile is given in the sweep. | Example: CAPIOX FX25 with hard-shell reservoir. | [OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/) (B); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Heat exchanger / heater-cooler unit | Counter-current water around the oxygenator fibres and the cardioplegia coil. Because of the *M. chimaera* outbreak, units should sit outside the OR and be decontaminated. | *M. chimaera* mortality 40-65%; latency often > 6 years. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Arterial line filter | Traps gaseous microemboli. Often integrated into the oxygenator. | An integrated filter saves 100-250 mL of prime. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Cardioplegia delivery system | Separate pump and heat exchanger. Blood is mixed 4:1 (Buckberg) or 1:4 (del Nido). Delivery line pressure is monitored. | See §2.8. | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Cardiotomy suction, cell saver | Returns shed blood. Washing it with a cell saver gave higher post-op Hb in one study. | Stop cardiotomy suction when protamine starts (Class IIa, Level C). | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Vents (aortic root, LV) | Decompress the heart; de-airing. | No numbers found (uncertain). | [OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/) (B) |
| Hemofilter (ultrafiltration) | Removes plasma water. | Removing > 32 mL/kg by conventional ultrafiltration was linked to more AKI in one cohort. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Gas supply, blender, vaporizer, scavenging | O2 and air; CO2 to flush the circuit before priming (about 5 min reaches 97-98% CO2). Scavenger limits: +10 cmH2O and −0.5 cmH2O. | Monitoring oxygenator exhaust volatile concentration is Class IIa. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Checklists | An institution-approved CPB checklist during setup and before starting CPB is Class I, Level C. A weaning checklist is recommended. | — | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

**Worked real-world setup (good default for the game).** Cleveland Clinic adult practice ([Kim et al., JECT 2014;46:317-323](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)):
- Prime: 2000 mL Plasma-Lyte A + 50 mEq NaHCO3 + 10,000 IU heparin. Minimum operating prime 719 mL using retrograde autologous priming.
- Mannitol 50 g after CPB starts.
- Flow 2.0-2.4 L/min/m². MAP > 65 mmHg.
- Sweep set for PaO2 > 150 mmHg and PaCO2 35-45 mmHg.
- Heparin 400 IU/kg into a central line. Target ACT > 480 s.
- Protamine "at a 1:1 ratio of the loading dose".

### 2.2 Priming volume and hemodilution

- Hemodilution depends on the ratio of patient blood volume to prime volume ([OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)) (B).
- Minimizing prime and using retrograde or antegrade autologous priming is **Class I, Level A**. Starch primes are Class III. Routine mannitol in the prime is Class III. Keeping pH 7.35-7.45 and avoiding hyperchloraemic acidosis is Class IIa ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
- Estimated blood volume (EBV) is usually 70 mL/kg for adult men and 65 mL/kg for women ([search summary of perfusion literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC6586263)) (uncertain - snippet only).
- Post-dilution Hct ≈ Hct_pre × EBV / (EBV + prime + other clear fluids). This is the standard form. The sources describe the inputs but I did not see the closed formula printed (uncertain).
- **Worked example (design):** 80 kg man, Hct 40%, EBV 5600 mL. With a 1200 mL net prime, Hct = 40 × 5600 / 6800 ≈ **32.9%**. If 1000 mL of del Nido crystalloid also enters the circulation, Hct = 40 × 5600 / 7800 ≈ **28.7%**. This is why del Nido "may initially increase the level of hemodilution" ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).
- **Viscosity:** about 4 cP at Hct 40%. It falls about 25% at Hct 30% and about 45% at Hct 20%. It rises about 2% per 1 °C of cooling ([Ranucci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/)). This explains the drop in MAP when CPB starts (§3.4).

### 2.3 Pump flow and oxygen delivery

| Item | Value | Class / level | Source |
|---|---|---|---|
| Usual flow (moderate hypothermia to normothermia) | 2.2-2.8 L/min/m² | Text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Set the estimated flow before CPB from BSA and planned temperature | — | I, C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Minimum DO2 | 280 mL/min/m², to reduce stage-1 AKI | I, A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Goal-directed perfusion lower threshold during normothermic CPB | DO2 280-300 mL/min/m² | IIa, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Other "critical DO2" values in studies | 250-300; 270 (Australasian, > 19,000 patients); 231 for any AKI | Evidence text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Mortality predictors in a perfusion database | MAP < 50 mmHg; CI < 1.6 L/min/m² | Evidence text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Lower risk of time below threshold | DO2 < 300 for > 15 min with CPB > 121 min gave 50% AKI in one study | Evidence text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| SvO2 strategy | Keeping SvO2 > 75% was associated with less stage-1 AKI | Evidence text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Adequacy markers | SvO2, O2 extraction, rScO2, VCO2, VCO2/VO2, lactate. "No validated threshold presently exists." | IIa, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

**DO2 formula (for the game):** DO2i = pump flow index × CaO2 × 10. CaO2 = 1.34 × Hb × SaO2 + 0.003 × PaO2. The guideline gives the concept: DO2 is pump flow × O2 content, which depends on Hb and SaO2 ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). The constants 1.34 and 0.003 are textbook constants that I did not verify in this research.
- *Example (design):* flow 2.4 L/min/m², Hb 9 g/dL, SaO2 100%, PaO2 250 mmHg → CaO2 ≈ 12.8 mL/dL → **DO2i ≈ 307**, which passes.
- *Example (design):* same flow with Hb 7.5 g/dL → **DO2i ≈ 259**, which fails. The player must raise flow or transfuse.

### 2.4 Mean arterial pressure on CPB

| Recommendation | Class / level | Source |
|---|---|---|
| Keep MAP **50-80 mmHg** with vasoconstrictors or vasodilators, after confirming adequate anesthetic depth and pump flow | I, A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Using vasopressors to push MAP above 80 mmHg on CPB is not recommended | III, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Routinely targeting a high MAP to prevent AKI is not recommended | III, A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Target individual autoregulation limits when available | IIa, A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Treat vasoplegia with α1 agonists and/or vasopressin | I, C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Refractory vasoplegia: methylene blue or terlipressin | IIa, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Hydroxocobalamin or angiotensin II | IIb, C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| During aortic cannulation, keep systolic pressure "commonly below 100 mmHg" to lower dissection risk | Practice statement | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| After CPB, MAP < 65 mmHg for ≥ 10 min was linked to new dialysis (adjusted OR 1.12) | Evidence text | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| MAP < 50 mmHg linked to about 30% higher in-hospital mortality. Stroke risk rose about 13% per 10 min at 55-64 mmHg and about 16% per 10 min below 55 mmHg (retrospective). | Review | [Ranucci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) |

Vasoplegia (for game events) is defined in one review as MAP < 65 mmHg with CI often > 2.2 L/min/m² and SVR < 800 dyn·s/cm⁵. Its incidence after CPB is 5-44% ([Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/)).

### 2.5 Temperature management

**STS/SCA/AmSECT 2015** (Engelman et al., J Extra Corpor Technol 2015;47(3):145-154) ([PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)):

| # | Recommendation | Class / level |
|---|---|---|
| 1 | Use oxygenator arterial outlet temperature as a surrogate for brain temperature | I, C |
| 2 | Assume the outlet temperature **underestimates** brain perfusate temperature during warming | I, C |
| 3 | Keep arterial outlet temperature **< 37 °C** | I, C |
| 4 | Cooling: arterial-venous gradient **≤ 10 °C** (to avoid gas emboli) | I, C |
| 5 | Rewarming: arterial-venous gradient **≤ 10 °C** (to avoid outgassing) | I, C |
| 6 | PA or nasopharyngeal temperature is reasonable for weaning and just after CPB | IIa, C |
| 7 | When outlet ≥ 30 °C: gradient **≤ 4 °C** | IIa, B |
| 8 | When outlet ≥ 30 °C: rewarming rate **≤ 0.5 °C/min** | IIa, B |
| 9 | When outlet < 30 °C: maximum gradient 10 °C | IIa, C |
| — | No recommendation on the best weaning temperature | — |

Other facts from the same guideline: bladder and rectal temperatures can read **2-4 °C lower** than the brain during rewarming, so nasopharyngeal monitoring is preferred then ([PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)).

**EACTS 2024** ([PMC11947607](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)):
- Limit the oxygenator arterial outlet to a maximum of 37 °C (Class I, Level A).
- Consider normothermic CPB to reduce neurocognitive dysfunction when adequate DO2 can be kept (IIa, B).
- Four RCTs found slow rewarming was linked to less postoperative cognitive dysfunction.
- Heat-exchanger to arterial-inflow gradient must not exceed 10 °C. Start cooling only after CPB is established.
- Brain metabolic rate falls 6-7% per °C.

**Classification differences (pick one and label it in the game):**

| Scheme | Mild | Moderate | Deep | Source |
|---|---|---|---|---|
| Common CPB studies | 32-35 °C | 28-32 °C | — | [PMC9145413 summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9145413/) (C) |
| Other CPB studies | 32.1-35 or 34-36 °C | 30-32 or 28-30 °C | < 30 °C "severe" | [same search summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9145413/) (C) |
| Circulatory-arrest consensus (EACTS 2024 Table 3) | 28.1-34 °C | High-moderate 24.1-28; low-moderate 20.1-24 °C | 14.1-20 °C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

**Myocardial temperature:** myocardial O2 consumption falls about 50% per 10 °C fall. del Nido at 4 °C cools the myocardium below 15 °C. Cleveland targets a septal probe below 10 °C and alerts if it rises above 15 °C ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).

**Cold-induced arrhythmia:** below about 28-30 °C the myocardium becomes irritable and prone to VF. One source says spontaneous VF or asystole can happen below 25 °C ([search summary incl. PMC8904885](https://pmc.ncbi.nlm.nih.gov/articles/PMC8904885)) (C; these sources concern accidental hypothermia, not CPB).

### 2.6 Haematocrit and transfusion on CPB

| Rule | Class / level | Source |
|---|---|---|
| Transfuse red cells if **Hct < 18% (Hb 6.0 g/dL)** | I, C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Hct 18-24%: consider red cells based on tissue oxygenation (DO2 > 273 mL/min/m² and satisfactory cerebral oximetry) | IIb, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Do **not** transfuse if Hct > 24% with acceptable DO2 and extraction | III, C | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Antithrombin concentrate is first-line for antithrombin deficiency (heparin resistance) | I, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| No prophylactic FFP on CPB | III, B | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Japanese guideline: Hct ≥ 21% and/or Hb ≥ 7.0 g/dL on CPB | — | (uncertain - snippet only) [JECT 2026 article](https://ject.edpsciences.org/articles/ject/full_html/2026/02/ject250087/ject250087.html) |

### 2.7 Anticoagulation: heparin, ACT and protamine

| Item | Value | Grade / class | Source |
|---|---|---|---|
| Heparin bolus | Weight-based is reasonable (IIa, C). Example 300 IU/kg. High-dose arm 400 IU/kg. Rebound risk with > 400 IU/kg. | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Heparin bolus in practice | 400 IU/kg into a central line | A | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Higher dose not better | 450 vs 300 IU/kg RCT (n = 269): no bleeding difference | A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| ACT target | > 480 s is reasonable (IIa, C). With maximal-activation or microcuvette devices, > 400 s is often accepted. | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| ACT in current practice | > 480 s; Australian survey 480 s (range 400-500). Coated circuits have used 250-300 s in studies. | A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Baseline ACT (no heparin) | About 70-120 s (some assays up to 180 s). One 1979 control group had a mean of 131 s. | C | [search summary](https://ebmconsult.com/articles/lab-test-act-activated-clotting-time) (uncertain - snippet only) |
| Heparin concentration target | > 4 IU/mL (Gravlee). Subclinical coagulation was still seen above 4.1 IU/mL. | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Heparin half-life (dose-dependent) | About 30 min at 25 IU/kg, 60 min at 100 IU/kg, 150 min at 400 IU/kg | B/C | [The Blood Project](https://www.thebloodproject.com/ufaq/what-is-the-half-life-of-unfractionated-heparin-2/) (uncertain - snippet only) |
| ACT monitoring | Measure before CPB and at regular intervals (Class I, Level C). Redose by ACT. | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Protamine ratio (Europe) | **Protamine-to-heparin ratio < 1.0** is recommended (I, B). A ratio of 1.3 was worse than 0.8. | A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/) |
| Protamine ratio (US) | Limit to **< 2.6 mg protamine per 100 IU heparin** (IIa, C). Platelet dysfunction above 5:1. Titrating to residual heparin is IIa, B. | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Protamine in practice | 1:1 of the loading heparin dose (i.e. 1 mg per 100 IU) | A | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Heparin rebound | Protamine infusion 25 mg/h for up to 6 h (IIb, C) | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Protamine reactions | Anaphylaxis < 1%, about 60% of them before CPB ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)). Overall adverse reactions 0.06-10.6%. Horrow types: I = hypotension; II = anaphylactic/anaphylactoid; III = catastrophic pulmonary hypertension and RV failure. Give slowly: the protamine label limit is ≤ 50 mg in any 10-min period (about 5 mg/min); OpenAnesthesia gives ≤ 20 mg/min or the whole dose over 10-15 min [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-x1]. | A / B | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/); [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/) (uncertain - snippet only) |
| Protamine collapse | With pulmonary hypertension and collapse after protamine: stop protamine, resuscitate, restart CPB with full anticoagulation (I, C) | A | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Heparin-induced thrombocytopenia (HIT) alternative | Bivalirudin first-line in acute HIT type 2 (IIa, B): 1.0 mg/kg load, 2.5 mg/kg/h, 50 mg in the prime, half-life about 25 min, ACT target 2.5 × baseline | A | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |

### 2.8 Cardioplegia

**General (EACTS):**
- Arrest uses high potassium, 8-20 mEq/L ([EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/)).
- Antegrade delivery into the aortic root at **60-100 mmHg**. Retrograde into the coronary sinus at **200-400 mL/min** with a sinus pressure of **30-50 mmHg**.
- Time to arrest: **30-60 s antegrade** vs **2-4 min retrograde**.
- Retrograde delivery may protect the RV incompletely.
- Cold intermittent doses are given **every 20-30 min**. All from [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/).
- Evidence is "not sufficient" to prefer blood, crystalloid or del Nido in specific patients ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

| Solution | Type | Ratio / composition | Dose | Temperature | Redosing / duration | Source |
|---|---|---|---|---|---|---|
| **Buckberg (modified, Cleveland)** | Blood (extracellular) | 4:1 blood:crystalloid. Crystalloid = dextrose-based, KCl, tromethamine buffer, CPD calcium chelator. Induction KCl 36 mEq/500 mL; maintenance 36 mEq/L; reperfusion 15 mEq/500 mL. | Induction about 500 mL, maintenance about 1000 mL, reperfusion about 500 mL of crystalloid (approximate bag volumes) | 4 °C induction and maintenance. Warm "hot shot" at 37 °C just before removing the cross-clamp. | Maintenance every **15-20 min** | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| **del Nido (adult, Cleveland)** | Blood:crystalloid **1:4**. Per 1000 mL Plasma-Lyte A: KCl 26 mEq, 1% lidocaine 13 mL (130 mg), 20% mannitol 16 mL (3.2 g), 50% MgSO4 4 mL (2 g), NaHCO3 13 mEq. | **20 mL/kg, max 1000 mL for > 50 kg.** Half dose if XC < 30 min. Delivered over 1-4 min at 250-450 mL/min. | 4 °C at Cleveland; Boston Children's (original protocol) delivers at 8-12 °C [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-5] | Single dose. "After 90 minutes of aortic clamp time, the surgeon decides" on more. Up to 90 min ischemia per [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/). | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| **Custodiol HTK (Bretschneider)** | Intracellular crystalloid, nearly sodium-free | Single antegrade dose perfused over **6-8 min** (never shorter): UK SmPC gives 1 mL/min per g heart weight, about **1.5-2 L** in adults, at 80-110 mmHg, then 40-60 mmHg after arrest; the manufacturer brochure states 20-25 mL/kg at 40-60 mmHg. Repeat dose, if needed, 1-2 min (200-400 mL). | Cold (SmPC: 6-10 °C) | The SmPC states **no** cardioplegic protection time (and says benefit/risk for procedures < 90 min is not confirmed); 120-180 min appears only in manufacturer brochures; one perfusion protocol redoses 10 mL/kg before 120 min [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-6]. Causes iso-osmotic hyponatraemia that **should not be corrected**. | [Custodiol trial NCT01681095](https://clinicaltrials.gov/study/NCT01681095) (uncertain - snippet only); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **St Thomas' No. 2 (Plegisol)** | Extracellular crystalloid | — | Multidose | Cold | Every 20-30 min (general rule) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

**Failure-to-arrest rules (game events):** failure to arrest within **1-2 min** suggests incomplete clamping, aortic insufficiency with LV distension, a wrongly set pump head, a closed bag or too little potassium. Watch PA pressure for LV distension ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).

**Glucose side effect:** Buckberg is dextrose-based and raises glucose. del Nido is not dextrose-based ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).

**del Nido redosing:** the best strategy is unknown. One adult protocol redosed retrograde 250 mL at 90 min and then every 30 min ([D'Angelo 2022 / search summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8972223/)) (uncertain - snippet only).

### 2.9 Sweep gas, oxygenation and acid-base

- Sweep gas is O2/air. **FiO2 sets PaO2** and **sweep flow sets CO2 removal** ([OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)) (B).
- PaO2 target: > 150 mmHg ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)). One older study used a window of 150-250 mmHg ([JECT 1995 summary](https://ject.edpsciences.org/articles/ject/pdf/1995/01/ject1995271p15.pdf)) (C). PaCO2 35-45 mmHg ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).
- Sweep:blood (V/Q) ratio: 0.6 gave normal PaCO2 in a 1,077-case paediatric study. An older paper recommended at least 1.0 ([search summary](https://ject.edpsciences.org/10.1051/ject/202052112)) (C; values differ).
- Starting at FiO2 0.21 avoids hyperoxic perfusate ([search summary, JECT 1999](https://ject.edpsciences.org/10.1051/ject/1999313145)) (C).
- **Alpha-stat** (uncorrected gases) is the standard adult strategy. It is Class IIa, B for high-moderate hypothermia because of better neuro outcomes in 3 RCTs from the 1990s. **pH-stat** (temperature-corrected) adds CO2 to the sweep ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
- Our oxygenator model can be checked against Pulse: PCO2 about 70 → 25 mmHg as sweep rises from 2 to 10 L/min ([Pulse ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)).

### 2.10 Electrolytes, glucose and other labs on CPB

| Lab | Rule / behaviour | Source |
|---|---|---|
| Potassium | Rises after cardioplegia. Consider treatment (ultrafiltration, calcium, insulin) above **6.5-7 mmol/L**. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/) |
| Sodium | HTK causes iso-osmotic hyponatraemia. Do not correct it. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Calcium | Falls with hemodilution and citrated blood. CaCl2 **5-15 mg/kg** gives a transient rise in BP, SVR, CI and stroke volume. | [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Magnesium | May be considered for arrhythmia prophylaxis (IIb, B) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Glucose | STS 2009: keep ≤ 180 mg/dL (≈ 10 mmol/L) ([MPOG measure](https://measures.mpog.org/Spec/Public/71)) (B). EACTS 2019 cites up to 10 mmol/L for diabetics and < 7.8 mmol/L for non-diabetics ([EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/)). | as cited |
| Lactate | Peak ≥ 4.0 mmol/L during surgery in 42.7% of 370 patients, linked to more AF (19.9% vs 5.3%) and longer stays. Postoperative ≥ 4.4 mmol/L predicts mortality. Thresholds vary (2.2-7.25). | [search summary incl. PMC4797582](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4797582/) (C) |
| pH | Keep 7.35-7.45 (IIa, B) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

---

## 3. Vital signs to display and simulate

### 3.1 Baseline normal values (anesthetized adult, before bypass)

| Signal | Normal | Abnormal / alarm idea | Source |
|---|---|---|---|
| MAP | 70-105 mmHg | < 65 (hypotension); > 110 (hypertension) (design) | [VUMC sheet](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| CVP | 0-8 mmHg (other sources 2-6) | > 12 suggests RV failure, overload or tamponade (design) | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B); [search summary](https://vimbook.vumc.org/cardiology/right-heart-catheterization) (C) |
| PA systolic / diastolic | 15-25 / 6-12 mmHg | Sudden rise after protamine = Type III reaction | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| Mean PA | 9-16 mmHg | — | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| PCWP | 5-12 mmHg (sources range 4-12 to 8-12) | High in LV failure, mitral disease, LV distension | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| Stroke volume | 60-135 mL/beat | — | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| CO / CI | 4-8 L/min / 2.5-4.0 L/min/m² | Low cardiac output syndrome after CPB: CI 2.4 L/min/m² (as printed in the guideline) **plus** end-organ dysfunction | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| SVR | 800-1200 dyn·s/cm⁵ = (MAP − CVP) × 80 / CO | < 800 with MAP < 65 suggests vasoplegia | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B); [Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/) |
| PVR | 155-255 dyn·s/cm⁵ (as printed) | — | [VUMC](https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf) (B) |
| SvO2 | 60-75% or 65-75% (sources vary) | On CPB, aim > 75% (associated with less AKI) | [search summary](https://open-exam-prep.com/study-guides/ccrn/cardiovascular-hemodynamics/hemodynamic-monitoring-values) (C); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| BIS | 40-60 target range (used in a 2000-patient trial) | < 40 too deep; > 60 awareness risk | [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/) |
| NIRS (rScO2) | Patient's own baseline | Baseline < 50% = high risk. A fall greater than about 15-20% from baseline triggers action. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Urine output | ≥ 0.5 mL/kg/h | KDIGO AKI stage 1: < 0.5 mL/kg/h for 6 h | [KDIGO summary](https://www.scottishintensivecare.org.uk/?p=3595) (C) |
| HR, SpO2, EtCO2, temperature | Standard textbook values (HR 60-100/min, SpO2 ≥ 95%, EtCO2 35-45 mmHg, core 36-37.5 °C) | — | Not separately sourced in this research (uncertain) |

### 3.2 Values on bypass

| Signal | Target on CPB | Source |
|---|---|---|
| Pump flow | 2.2-2.8 L/min/m² (practice example 2.0-2.4) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| MAP | 50-80 mmHg | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| DO2i | ≥ 280 mL/min/m² | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Hct | Transfuse < 18%; grey zone 18-24% | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| ACT | > 480 s (> 400 s with some devices) | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| PaO2 / PaCO2 | > 150 / 35-45 mmHg | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Arterial outlet temperature | ≤ 37 °C | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/) |
| BIS | Falls about **1.2 units per °C** of cooling. Patient state index falls 0.84/°C cooling and rises 0.7/°C rewarming. One goal-directed trial used BIS 45-60 off CPB and 40-45 on CPB. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Venous line pressure (VAVD) | Not more negative than about −60 mmHg | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| SpO2 / pulse waveform | Lost with non-pulsatile full flow. NIRS is useful in non-pulsatile flow. | Inference from [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) (uncertain) |
| EtCO2 | Near zero when the lungs are not ventilated and there is no pulmonary blood flow. Continuing ventilation or CPAP during cross-clamp is **not recommended** (III, A). | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); the EtCO2 value is a physiological inference (uncertain) |

### 3.3 ECG rhythms to support

| Rhythm | When it appears in the game | Rates and data | Source |
|---|---|---|---|
| Sinus rhythm (± tachycardia) | Baseline. Tachycardia and hypertension with skin incision, sternotomy and sternal spread. | Even very high sufentanil doses "cannot reliably prevent the responses to sternotomy and sternal spread". BP rises more often than HR. | [search summary incl. BMC Anesthesiol 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322556) (C) |
| Asystole / isoelectric line | After cardioplegia: 30-60 s antegrade, 2-4 min retrograde | — | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Slow, wide-complex activity, then return of rhythm | During cardioplegia washout and the warm "hot shot" before unclamping | No numbers found (design) | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) (hot shot only) |
| Ventricular fibrillation (reperfusion VF) | After cross-clamp removal | Older series 74-96%. Modern CABG RCT: 15.9% placebo, 11.8% lidocaine, 8.9% amiodarone (p = 0.41). Lidocaine 100 mg 2 min before release: 70% → 11% in one RCT. | [search summary](https://arya.mui.ac.ir/article_10381.html) (C); [NCT00587483](https://clinicaltrials.gov/study/NCT00587483) (C) |
| VF during deep cooling | Below about 28-30 °C, with handling | — | [search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8904885) (C) |
| Heart block | After aortic valve replacement | Permanent pacemaker in 2-4% within 30 days; mostly complete AV block. Cumulative 5.0% at 1 year. | [search summary](https://repub.eur.nl/pub/56438) (C) |
| Atrial fibrillation | Post-op (ICU or epilogue phase) | 30-40% after CABG, up to 64% with valve surgery. Peaks on days 2-3. | [Heart review](https://heart.bmj.com/cgi/doi/10.1136/hrt.2007.132795) (C via snippet) |
| ST changes | Ischaemia, graft problems, air in coronaries after de-airing | Not sourced in this research (uncertain) | — |
| VF / pulseless VT / asystole / PEA (arrest) | Complication events | ACLS waveform set already exists in Pulse 4.1.0+ | [Pulse versions](https://pulse.kitware.com/version.html) |

### 3.4 How vital signs respond to surgical events (event-response table)

"Δ" values marked (design) are my proposed effect sizes for the game. They follow the direction stated in the sources and should be tuned in playtests.

| Event | Physiology change to apply | Expected display | Source / basis |
|---|---|---|---|
| Induction (etomidate or propofol + fentanyl + rocuronium) | ↓ sympathetic tone, ↓ SVR (propofol vasodilates), apnoea → ventilator | MAP −10 to −25% (design). Etomidate is more stable. BIS falls to 40-60. | [etomidate review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331132/) (C via snippet); [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/) |
| Skin incision, sternotomy, sternal spread | Noxious stimulus → ↑ SVR, ↑ HR, ↑ VO2 | SBP and MAP rise (e.g. +15-30%, design). HR rises less often. Opioid-dose effect plateaus. | [search summary incl. PMC4322556](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322556) (C) |
| Heparin bolus | Heparin PK → ACT rise | ACT from about 100-130 s to > 480 s within minutes (timing design) | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/) |
| Aortic cannulation | Requires SBP < 100 mmHg. Higher SBP raises a dissection-risk flag. | Player must lower BP before cannulation | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Go on bypass (partial → full flow) | Venous drainage to the reservoir. Pump flow source. Prime mixes in (Hct drop). Viscosity ↓ → SVR ↓. Pulsatility lost. | MAP falls transiently (hemodilution). Pulse pressure → near 0. CVP → about 0. PA pressure → low. Hct about 40 → 29-33%. | [Ranucci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/); 1975 study: A-V pressure difference −54% with viscosity −42% ([search summary](https://rk.md/2016/hypotension-initiation-cardiopulmonary-bypass/)) (C) |
| Stop ventilation (full flow) | Lungs idle | EtCO2 → about 0. SpO2 trace lost. NIRS and inline SvO2 become the main monitors. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) (ventilation stop); display is inference |
| Fentanyl kinetics at CPB start | Hemodilution + circuit binding | Plasma fentanyl −30 to −60% after a bolus (about −30% with infusion) → awareness risk if not redosed | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Cooling | Heat exchanger. Gradient ≤ 10 °C. | NP and bladder temperature fall; viscosity +2%/°C; BIS −1.2/°C; propofol levels rise (+28% at 34 °C); VF risk below 28-30 °C | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/); [Ranucci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Aortic cross-clamp + cardioplegia | Coronary flow = 0. K+ load. Heart arrests. | ECG isoelectric in 30-60 s. K+ rises. Myocardial temperature < 15 °C (septal < 10). Start ischaemia timer and redose timer. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Ischaemic period | Myocardial warming and washout | Myocardial temperature > 15 °C or LV distension (high PA pressure) → alert, redose | [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf) |
| Rewarming | Heat exchanger. Gradient ≤ 4 °C and ≤ 0.5 °C/min above 30 °C. | NP temperature rises faster than bladder (bladder lags 2-4 °C). Anesthetic depth lightens. | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Hot shot + cross-clamp removal | Coronary reperfusion | Probability of VF (game: 10-20% modern baseline, lower with lidocaine or Mg; design based on the RCT above). Rhythm returns; possible heart block. | [NCT00587483](https://clinicaltrials.gov/study/NCT00587483) (C) |
| Weaning | Ventilation resumes. Venous line partly clamped → preload to the heart. Pump flow ↓. Inotropes or pacing as needed. | CVP and PA pressures rise. Pulsatile arterial trace returns. EtCO2 returns. CO from the heart. LCOS if CI is low with organ dysfunction. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Protamine | Heparin neutralized (ratio < 1.0). Stop cardiotomy suction. | ACT returns toward baseline. Reaction chance: type I hypotension; type II anaphylaxis (< 1%); type III PA pressure surge with RV failure. | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Bleeding (surgical or coagulopathic) | Volume loss → baroreflex (venous unstressed volume first) | HR ↑, MAP ↓, CVP ↓. Hct falls with crystalloid. Pulse defines hypovolemic shock as a 35% blood-volume loss. | [Ursino index](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985) (C); [Pulse CV](https://pulse.kitware.com/_cardiovascular_methodology.html) |
| Arrest in the ICU after surgery | CALS pathway | See §4.3 | [CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) |

---

## 4. Anesthesia and drugs

### 4.1 Induction and maintenance

| Drug | Typical dose | Onset / duration | Main effects to model | Source |
|---|---|---|---|---|
| **Etomidate** | 0.2-0.6 mg/kg; usual 0.3 mg/kg over 30-60 s | Onset < 1 min; duration 3-5 min at 0.3 mg/kg | Stable hemodynamics; cortisol suppression for 6-8 h | [Pfizer label](https://www.pfizermedical.com/amidate) and [drugs.com](https://www.drugs.com/pro/etomidate.html) (uncertain - snippet only) |
| **Propofol** | Cardiac induction 0.5-1.5 mg/kg titrated. Maintenance ≥ 50 µg/kg/min if an opioid is the main agent, ≥ 100 µg/kg/min if propofol is the main agent (Diprivan label). The generic label says 25-100 µg/kg/min (conflict). | Fast | Vasodilation → BP drop. Levels +28% at 34 °C. | [medlibrary Diprivan](https://medlibrary.org/lib/rx/meds/diprivan/page/2/) (uncertain - snippet only); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Fentanyl** | Open heart surgery 20-50 µg/kg, up to 150 µg/kg (Hospira label). Another label gives 50-100 µg/kg with O2 and a relaxant. | — | Blunts the stress response (not fully at sternotomy). Plasma level −30 to −60% at CPB start. | [drugs.com fentanyl](https://www.drugs.com/pro/fentanyl-injection.html) (uncertain - snippet only); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Rocuronium** | 0.6 mg/kg for intubation (0.6-1.2 mg/kg gives good conditions in < 2 min) | Clinical duration about 31 min (15-85) at 0.6 mg/kg | Paralysis; longer action in hypothermia | [FDA Zemuron label (archived)](https://webarchive.library.unt.edu/eot2008/20090118024358/http:/www.fda.gov/medwatch/safety/2008/Aug_PI/Zemuron_PI.pdf) (uncertain - snippet only); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Volatile (sevoflurane / isoflurane)** | Via the ventilator, or the oxygenator on CPB | — | Use approved delivery equipment (I, C). Monitor exhaust (IIa, B). No nitrous oxide around CPB. | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Midazolam, ketamine, morphine, succinylcholine | Not sourced in this research | — | Already in the Pulse drug library (validated) | [Pulse drugs](https://pulse.kitware.com/_drugs_methodology.html) |

**Awareness:** the UK NAP5 audit confirmed a high risk of accidental awareness in cardiac anesthesia ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). This becomes a game risk when fentanyl is diluted or volatile is lost through a PMP oxygenator.

### 4.2 Vasopressors and inotropes

| Drug | Receptors | Dose range | Half-life / onset | Effect to model | Source |
|---|---|---|---|---|---|
| **Norepinephrine** | α1 >> β1 | 0.01-0.3 µg/kg/min, titrated up to 1 µg/kg/min | t½ 2-3 min | ↑ SVR, ↑ MAP; HR about unchanged; CI may rise. No diastolic rise of about 20 mmHg at 0.3 µg/kg/min suggests non-response. | [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/); [Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/) |
| **Epinephrine** | β1 > β2 > α | 0.01-0.3 µg/kg/min (shock up to 0.05-2 µg/kg/min). Arrest: 1 mg every 3-5 min (ACLS). **CALS: 50-100 µg only.** | t½ < 5 min | Low dose: ↑ HR, ↑ contractility, ↓ SVR. High dose: ↑ SVR. ↑ PA pressure. | [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/); [StatPearls](https://www.ncbi.nlm.nih.gov/sites/books/NBK482160/) (uncertain - snippet only); [CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) |
| **Vasopressin** | V1 | 0.01-0.04 U/min; usually 0.03 U/min. > 0.04 U/min risks skin necrosis. | t½ 10-35 min (sources vary) | ↑ SVR. Does **not** raise PVR. HR ↓. CO may fall. First-line for vasoplegia together with α1 agonists. | [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/); [Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Phenylephrine** | Pure α1 | Bolus 50-100 µg in aliquots. Infusions of 25-100 µg/min were studied in obstetrics only (uncertain transfer). | Fast; short | ↑ SVR. Reflex bradycardia. ↓ contractility. Not for cardiogenic shock. | [StatPearls](https://www.ncbi.nlm.nih.gov/sites/books/NBK534801/) (uncertain - snippet only); [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/) |
| **Dobutamine** | β1 (± β2, α1) | 2-20 µg/kg/min (rarely 40) | Onset 1-2 min; peak up to 10 min; t½ about 2 min | ↑ contractility, ↑ HR (tachycardia > 10 µg/kg/min without extra CO); ↓ SVR at low dose | [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470431/) (uncertain - snippet only); [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/) |
| **Milrinone** | PDE-III inhibitor | Load 50 µg/kg over 10 min, then 0.375-0.75 µg/kg/min (standard 0.5). Lower doses in renal impairment. | t½ 2.3-2.4 h | ↑ contractility, ↓ SVR and PVR → hypotension (more above 0.5 µg/kg/min) | [Pfizer label](https://www.pfizermedicalinformation.com/milrinone-lactate/dosage-admin) (uncertain - snippet only); [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/) |
| **Levosimendan** | Ca²⁺ sensitizer | 0.1-0.2 µg/kg/min | t½ 1 h (metabolite 70-80 h) | ↑ contractility, ↓ SVR. Not available in the US. RCTs showed no mortality benefit. | [Shankar 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Calcium chloride** | — | 5-15 mg/kg | Transient | ↑ BP, SVR, CI and SV | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| **Methylene blue** | NO/cGMP pathway | Dose not found (UNVERIFIED) | — | Rescue for refractory vasoplegia (IIa, B) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

**Weaning rule:** "Forcing weaning from CPB using high-dose inotropic drugs and vasoconstrictors is not recommended". Short-term mechanical support should be considered in difficult weaning ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). Pre-emptive milrinone reduced the need for extra inotropes in one small RCT (n = 49) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

### 4.3 Antiarrhythmics and arrest after cardiac surgery

| Drug / action | Dose | Use in the game | Source |
|---|---|---|---|
| **Amiodarone (arrest)** | 300 mg bolus, then 150 mg | Refractory VF/pVT (ACLS) | [ACLS summary](https://acls-algorithms.com/new-2025-aha-acls-guideline-changes/2025-adult-cardiac-arrest-algorithm-changes/) (C); CALS says "consider" without a dose ([CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/)) |
| **Amiodarone (non-arrest)** | 150 mg over 10 min, then 1 mg/min for 6 h, then 0.5 mg/min. Repeat 150 mg for breakthrough VF/VT. | Post-op AF/VT | [Nexterone label summary](https://www.drugs.com/pro/nexterone.html) (uncertain - snippet only) |
| **Lidocaine (arrest)** | 1-1.5 mg/kg, then 0.5-0.75 mg/kg | Refractory VF/pVT | [AHA 2025 algorithm](https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/Algorithm-ACLS-CA-Circular-250620.pdf?sc_lang=en) (uncertain - snippet only; the PDF returned 403) |
| **Lidocaine (prevent reperfusion VF)** | 100 mg 2 min before XC release, or 1.5-2 mg/kg | Lowers VF chance at unclamping | [search summary](https://arya.mui.ac.ir/article_10381.html) (C) |
| **Internal defibrillation** | **20 J** via internal paddles (other protocols 10-10-20 J, escalating to 50 J) | Open chest | [CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/); [search summary](https://arya.mui.ac.ir/article_10381.html) (C) |
| **CALS sequence** | Up to **3 stacked external shocks** for VF/pVT. Compressions may be withheld for up to 60 s. Pace in **DOO** mode for asystole or bradycardia. **Re-open the chest within 5 min** (within 10 days of surgery). Epinephrine **50-100 µg**, not 1 mg. | Post-op arrest scenario | [CALS-ANZ 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) |
| Arrest incidence after cardiac surgery | 0.7-5.2%, mostly within 24 h | Event probability | [search summary](https://aminer.org/pub/6373072790e50fcafd0ecb2a/the-australasian-anzscts-anzics-guidelines-on-cardiothoracic-advanced-life-support-cals-anz) (C) |

### 4.4 Pharmacokinetic / pharmacodynamic model for the game

**Recommended structure** (standard PK/PD; equations are textbook, design):
1. **PK:** a 1- to 3-compartment model per drug. Short-acting infusions (catecholamines) use 1 compartment with k = ln 2 / t½. Propofol uses 3 compartments.
2. **Effect site:** dCe/dt = ke0 × (Cp − Ce). This delays the effect behind the plasma level.
3. **PD (Hill/Emax):** Effect = E0 + Emax × Ceᵞ / (EC50ᵞ + Ceᵞ). Apply the effect to a **model parameter** (SVR, Emax contractility, HR set-point, venous tone, BIS), not directly to the displayed vital sign. This lets the physiology produce the vital-sign change. Pulse instead applies effects as a fraction of the baseline vital sign ([Pulse drugs](https://pulse.kitware.com/_drugs_methodology.html)).
4. **CPB modifiers:** add prime volume to the volume of distribution at CPB start (fentanyl −30 to −60%) and apply temperature effects (propofol +28% at 34 °C; reduced clearance in hypothermia) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

**Propofol (Eleveld 2018):** for a 35-year-old, 170 cm, 70 kg man: V1 6.28 L, V2 25.5 L, V3 273 L, CL 1.79 L/min, Q2 1.75 L/min, Q3 1.11 L/min, ke0 0.146 min⁻¹ ([Eleveld 2018 abstract](https://pesquisa.bvsalud.org/ses/resource/pt/mdl-29661412)) (uncertain - snippet only; covariate equations not checked). Prediction precision < 30% for plasma levels and BIS; bias −27% in older subjects ([search summary](https://repositorio.udd.cl/handle/11447/1047)) (C).

**Proposed starter parameters (design estimates; tune by playtest).** The half-lives are sourced; the effect sizes are not:

| Drug | t½ (sourced) | Target parameter | Emax (design) | EC50 (design) | Hill γ (design) |
|---|---|---|---|---|---|
| Norepinephrine | 2.5 min ([Shankar](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/)) | SVR | +120% | dose eq. 0.15 µg/kg/min | 1.5 |
| Epinephrine | 3 min (< 5) ([Shankar](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/)) | Contractility (Emax) / HR / SVR | +85% Emax (Suga anchor 6.6 → 12.2) ([Suga](https://scilit.net/publications/7c0ae8fc02a2142815b3b1438ddbad30)) | 0.05 µg/kg/min | 1.5 |
| Vasopressin | 20 min (10-35) ([Kato](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/)) | SVR (no PVR effect) | +60% | 0.02 U/min | 1 |
| Phenylephrine | about 5 min (uncertain) | SVR; reflex HR ↓ | +50% | 100 µg bolus equivalent | 1 |
| Dobutamine | 2 min ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470431/)) | Contractility; HR; SVR ↓ | +60% contractility | 5 µg/kg/min | 1.2 |
| Milrinone | 2.35 h ([Shankar](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/)) | Contractility ↑; SVR/PVR ↓ | +40% / −30% | 0.4 µg/kg/min | 1 |
| Heparin → ACT | 30-150 min, dose-dependent ([Blood Project](https://www.thebloodproject.com/ufaq/what-is-the-half-life-of-unfractionated-heparin-2/)) | ACT | ACT reaches > 480 s at a heparin level of about 3-4 IU/mL (target > 4 IU/mL per [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)) | — | — |
| Protamine | Immediate binding | Heparin neutralized at about 1 mg per 100 IU; overdose effects above ratio 1.3 | — | — | — |

---

## 5. Recommended modelling approach

### 5.1 Options compared

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| **A. Pulse as the whole engine** | Validated systems; drugs; ACLS rhythms; ventilator; free Unity and Unreal plugins; Apache-2.0 ([Pulse home](https://pulse.kitware.com/)) | No CPB, cross-clamp or cardioplegia. ECMO pump is an ideal flow source with no anticoagulation ([ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). Ventricles only. Template ECG. Key cardiac drugs missing. Known PD shortcuts ([Drugs](https://pulse.kitware.com/_drugs_methodology.html)). | Not enough for the core loop |
| **B. Custom lumped model only** | Full control over CPB, cardioplegia, temperature, heparin and ACT. Light and deterministic. Can be written in C# or C++ inside the engine. | Validation must be built by us. Wider scope (O2/CO2 transport, PK). | Good, but risky without a reference |
| **C. Hybrid (recommended)** | Custom CPB-aware core for the game. Pulse used (a) offline as a validation oracle for off-pump phases and drug responses, and (b) as an optional live engine for the pre-op, induction and ICU or arrest scenes. | Two models to keep in step. Hand-off between them is complex if both run live. | **Recommended** |

### 5.2 Proposed custom core (structure)

1. **Heart:** 4 chambers with time-varying elastance (Emax, Tmax per chamber) ([Suga & Sagawa 1973](https://scilit.net/publications/7c0ae8fc02a2142815b3b1438ddbad30)). Valves "open on pressure, close on flow" ([Smith 2004](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_71751123)). A rhythm module gates contraction (sinus, AF = irregular RR with no atrial kick, VF = no ejection, asystole, paced). A cardioplegia state sets Emax ≈ 0.
2. **Vessels:** systemic and pulmonary 3-element Windkessels ([Westerhof 2009](https://pubmed.ncbi.nlm.nih.gov/18543011/)), plus venous capacitance with unstressed volume. Coronary flow is a branch that the cross-clamp sets to 0.
3. **Reflexes:** Ursino-style baroreflex acting on HR, SVR, contractility and venous unstressed volume ([Ursino 1998](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985)). Anesthetic depth damps the reflex gain (design).
4. **CPB circuit:** venous line (gravity or VAVD) → reservoir (volume state; low-level alarm) → pump (flow source, or centrifugal with an RPM-pressure curve) → oxygenator (O2 transfer by FiO2; CO2 by sweep; check against Pulse ECMO numbers) → heat exchanger (water temperature, gradient limits) → arterial filter → aortic cannula (line pressure). Side circuits: cardioplegia pump and heat exchanger, vents, cardiotomy suction, cell saver, hemofilter.
5. **Blood:** volume, Hct (dilution formula), viscosity(Hct, temperature) feeding resistance ([Ranucci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/)). O2 content, DO2, VO2 (temperature-scaled: −6-7%/°C for brain; myocardium −50% per 10 °C). SvO2, lactate (accumulates when DO2 < critical value). K+, glucose, Ca²⁺. Heparin → ACT.
6. **Temperature:** core, nasopharyngeal (fast) and bladder (lags 2-4 °C during rewarming) ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)), plus myocardial temperature.
7. **PK/PD:** §4.4.
8. **Monitors:** ECG (re-implemented McSharry model or our own templates); arterial, CVP and PA waveforms from the circuit pressures; numbers averaged like a real monitor; BIS from the anesthetic effect-site level and temperature (−1.2/°C); NIRS from cerebral DO2.

### 5.3 Update rates (design, based on Pulse practice)

| Layer | Rate | Reason / source |
|---|---|---|
| Circulation and CPB circuit ODEs | **50 Hz (dt = 20 ms)**, fixed step; sub-step to 5-10 ms if valves are unstable | Pulse uses 20 ms ([about](https://pulse.kitware.com/_about_pulse.html)); > 60 ms is unreliable ([forum](https://discourse.kitware.com/t/changing-step-size/1068)) (C) |
| Waveform rendering (ECG, arterial, CVP, PA) | 250-500 samples/s, interpolated from the 50 Hz state plus ECG synthesis | Smooth display (design) |
| Numeric vitals | Refresh 1 Hz. HR averaged over 5-10 beats. MAP averaged over beats. | Monitor-like behaviour (design) |
| PK/PD, temperature, gas exchange, labs | 1-10 Hz | Slow processes (design) |
| ABG, ACT, K+, glucose, Hct lab results | Shown only on request, after a delay of about 1-3 min (design, uncertain) | Realism of point-of-care testing |
| Game time scaling | 1× default. 2-10× "fast-forward" during stable bypass. | Pulse runs 10-15× real time, which shows this is feasible ([forum](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547)) (C) |

### 5.4 How the surgical state machine drives the physiology

The surgical layer must never set vital signs directly. It only changes **model inputs**. The physiology then produces the numbers. Proposed states and their inputs:

| State | Entry condition (rule check) | Physiology inputs changed |
|---|---|---|
| PreOp / Induction | Monitoring attached | Drug boluses; ventilator on; noxious stimulus = 0 |
| Incision / Sternotomy | BIS 40-60 (design check) | Noxious stimulus ↑ → sympathetic drive ↑ ([PMC4322556 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322556)) |
| Heparinization | Heparin given | Heparin PK; ACT must exceed 480 s before CPB ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)) |
| Cannulation (aortic, then venous) | SBP < 100 mmHg for aortic ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)) | Adds circuit nodes; bleeding or dissection risk if rules are broken |
| Initiate CPB | ACT OK; checklist done (Class I) | Venous drainage opens; pump ramps up; prime volume added; ventilation can stop |
| Full flow / cooling | Flow 2.2-2.8 L/min/m²; MAP 50-80 | Heat-exchanger target; gradient check ≤ 10 °C ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)) |
| Cross-clamp + cardioplegia | Vent ready; cardioplegia chosen | Coronary flow = 0; K+ dose → arrest; ischaemia timer; redose timer (15-30 min or 90 min for del Nido) |
| Repair (procedure mini-games) | Heart arrested | Timers; myocardial warming; blood loss to suction |
| Rewarming | Repair near completion | Gradient ≤ 4 °C; ≤ 0.5 °C/min; outlet ≤ 37 °C |
| De-airing + unclamp | Hot shot given (optional) | Coronary flow restored; reperfusion VF roll; rhythm resumes |
| Weaning | NP temperature about 36-37 °C (no formal target ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/))); K+ < 6.5; Hct; ventilation on; checklist | Venous line partly clamped; flow ↓; inotropes or pacing |
| Protamine / decannulation | Off CPB, stable | Heparin neutralization; reaction roll; stop cardiotomy suction |
| Hemostasis / closure | ACT near baseline | Bleeding model; transfusion; closure |
| ICU / epilogue | — | AF and arrest probabilities over days; CALS scenario |

---

## Game hooks

1. **Perfusion console mini-game.** Sliders for pump flow (L/min), sweep flow (L/min), FiO2, heat-exchanger water temperature and VAVD vacuum. Live DO2i readout. **Score:** time-weighted fraction with DO2i ≥ 280 and MAP 50-80 ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
2. **"Area below DO2 300" penalty.** Penalize the worst single episode more than the total, because the maximal-amplitude episode predicted AKI better (OR 4.9) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
3. **Hemodilution planner.** Before CPB the player picks prime volume and retrograde autologous priming. The game predicts on-pump Hct with the dilution formula (EBV 70/65 mL/kg). If the prediction is below 20%, prompt to reduce clear prime or add blood ([PMC6586263 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC6586263)) (uncertain).
4. **Transfusion decision.** At Hct < 18%, transfusing is "correct" (+points). At 18-24%, the decision depends on DO2 and NIRS. Transfusing above 24% loses points ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
5. **Heparin/ACT gate.** CPB cannot start until ACT > 480 s (a hard rule). Rare heparin resistance event (Garvin ≈ 17% ACT failure) ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)). Fix: more heparin or antithrombin concentrate (Class I).
6. **ACT drift.** Heparin decays with a dose-dependent half-life (about 150 min at 400 IU/kg). The player must recheck ACT about every 30 min (design) and redose.
7. **Protamine dosing.** The player sets a ratio. Ratio < 1.0 is optimal ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). Above 2.6 mg/100 IU is excessive and raises bleeding ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/)). Rate > 20 mg/min raises the chance of a type I reaction (design). Rare type III event: PA pressure spike, RV failure, resume CPB (Class I action).
8. **Forgetting to stop cardiotomy suction** at protamine leads to a clot-in-circuit event (design; based on the IIa, C rule).
9. **Cardioplegia choice.** Buckberg: redose timer every 15-20 min plus glucose rise. del Nido: 20 mL/kg (max 1000 mL), up to 90 min, more dilution. HTK: one dose over 6-8 min, hyponatraemia that must *not* be corrected (a trap). Sources: [Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf), [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/).
10. **Arrest check.** The heart must arrest within 1-2 min, else diagnose the cause (incomplete clamp, aortic insufficiency, pump head, closed bag) ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).
11. **Myocardial temperature probe.** Alarm above 15 °C ([Kim 2014](https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf)).
12. **Antegrade vs retrograde delivery.** Line pressure limits: root 60-100 mmHg, coronary sinus 30-50 mmHg at 200-400 mL/min. Exceeding the coronary-sinus limit causes "venous injury" (design) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
13. **Temperature rules engine.** Live check of arterial outlet ≤ 37 °C, gradient ≤ 10 °C, and when ≥ 30 °C gradient ≤ 4 °C and rate ≤ 0.5 °C/min. Breaking a rule adds "neuro risk" points ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)).
14. **Two temperature probes.** Nasopharyngeal leads and bladder lags 2-4 °C during rewarming. A player who weans on bladder temperature alone gets an "afterdrop" event (design) ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)).
15. **Cold heart irritability.** Below 28-30 °C, handling the heart has a chance of VF (design probability) ([PMC8904885 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8904885)) (C).
16. **Unclamp VF roll.** Base chance about 15%. About 10% with lidocaine 1.5 mg/kg or amiodarone pre-treatment (design from the RCT arms 15.9 / 11.8 / 8.9%). Internal paddles 20 J ([CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/)).
17. **Hyperkalaemia after cardioplegia.** K+ > 6.5-7 mmol/L needs a choice: ultrafiltration, calcium or insulin ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). It delays weaning (rhythm or block).
18. **Awareness meter.** Hidden "awareness risk" rises if BIS > 60, fentanyl falls 30-60% at CPB start without a redose, or volatile is given through a PMP oxygenator ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
19. **BIS realism.** BIS drops 1.2 per °C of cooling, so a low BIS on cold bypass is not a reason to cut anesthetic ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
20. **Vasopressor choice.** Norepinephrine, phenylephrine and vasopressin all raise MAP. Vasopressin spares PVR, which is better in RV failure ([Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/)). Pushing MAP > 80 mmHg on CPB with pressors is penalized ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
21. **Vasoplegia event** (5-44% incidence ([Kato 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/))): MAP < 65, SVR < 800, CI normal or high. Ladder: α1 agonist or vasopressin → methylene blue or terlipressin → hydroxocobalamin ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
22. **Weaning checklist UI** (Class I recommended): temperature, rhythm and pacing, K+ and Ca²⁺, Hct, ventilation on, de-airing confirmed, inotropes ready, TOE. Forcing weaning with high-dose drugs is penalized (Class III) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
23. **Difficult weaning branch.** Low CI with organ dysfunction (LCOS) → inotrope (milrinone or dobutamine) → mechanical support option ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
24. **Post-op AF epilogue.** 30-40% chance after CABG, higher after valve surgery, on day 2-3 ([Heart review](https://heart.bmj.com/cgi/doi/10.1136/hrt.2007.132795)) (C). Treat with an amiodarone regimen (150 mg / 10 min → 1 mg/min) ([label summary](https://www.drugs.com/pro/nexterone.html)) (C).
25. **ICU arrest scenario (CALS).** 3 stacked shocks → re-sternotomy within 5 min → internal 20 J; epinephrine 50-100 µg; DOO pacing for asystole ([CALS-ANZ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/)).
26. **AV block after aortic valve surgery.** About 2-4% need a pacemaker. Epicardial pacing wires give a DOO/DDD pacing mini-game ([search summary](https://repub.eur.nl/pub/56438)) (C).
27. **Lactate as a delayed truth signal.** Lactate rises minutes after poor DO2. Peak ≥ 4 mmol/L leads to a worse outcome score ([PMC4797582 summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4797582/)) (C).
28. **Glucose.** Keep ≤ 180 mg/dL. Buckberg cardioplegia and stress raise glucose; the insulin decision is the player's ([MPOG / STS 2009](https://measures.mpog.org/Spec/Public/71)) (B).

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | Pulse is Apache-2.0, C++ with C, C#, Java and Python interfaces | https://pulse.kitware.com/ | A |
| 2 | Pulse 4.4.0 is listed as "Aug 2026" and adds a new ECMO VV/VA device model (the page heading reads "Version 4.4.0"; the "4.3.0" string on the page is only a Font Awesome 4.3.0 stylesheet path, not a Pulse version) [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-1] | https://pulse.kitware.com/version.html | A |
| 3 | The Pulse ECMO pump is an ideal flow source and does not model anticoagulation, thrombosis or hemolysis; no CPB model exists | https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html | A |
| 4 | Pulse models only the ventricles; its ECG is a stored template, not electrical | https://pulse.kitware.com/_cardiovascular_methodology.html | A |
| 5 | Pulse runs with a 20 ms time step | https://pulse.kitware.com/_about_pulse.html | A |
| 6 | The Pulse Unity asset is free, version 4.3.1 (5 Feb 2025), under the Standard Unity Asset Store EULA | https://assetstore.unity.com/packages/slug/139773 | A |
| 7 | Pulse's validated drug list lacks vasopressin, heparin, protamine, amiodarone, lidocaine, milrinone and dobutamine | https://pulse.kitware.com/_drugs_methodology.html | A |
| 8 | ECGSYN 1.0.0 is GPL-3.0; MIT-BIH 1.0.0 is ODC-By 1.0 | https://physionet.org/content/ecgsyn/ ; https://physionet.org/content/mitdb/1.0.0/ | A |
| 9 | OpenCOR repository is GPL-3.0 | https://github.com/opencor/opencor | A |
| 10 | CircAdapt is under a custom EULA: free, revocable, educational/non-commercial/research use by academic researchers only [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-4] | https://framework.circadapt.org/latest/license.html | A |
| 11 | Usual CPB flow is 2.2-2.8 L/min/m² | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 12 | Minimum DO2 of 280 mL/min/m² is Class I, Level A | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 13 | MAP 50-80 mmHg on CPB is Class I, Level A; pressors to > 80 mmHg is Class III | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 14 | Transfuse at Hct < 18% (Class I, C); consider at 18-24% (IIb); not above 24% (III) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 15 | Oxygenator arterial outlet ≤ 37 °C (EACTS I-A; STS I-C) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ | A |
| 16 | Above 30 °C outlet: gradient ≤ 4 °C and rewarming ≤ 0.5 °C/min (IIa, B); ≤ 10 °C gradient otherwise | https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ | A |
| 17 | ACT > 480 s is reasonable during CPB; > 400 s with maximal-activation devices | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/ | A |
| 18 | Protamine:heparin ratio < 1.0 recommended (I, B) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 19 | Protamine ratio should stay < 2.6 mg/100 IU heparin; rebound infusion 25 mg/h up to 6 h | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/ | A |
| 20 | del Nido adult: 20 mL/kg, max 1000 mL (> 50 kg), 1:4 blood:crystalloid, 4 °C at Cleveland (8-12 °C at Boston Children's), 1-4 min at 250-450 mL/min; composition as listed [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-5] | https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf | A |
| 21 | del Nido single dose for up to 90 min of ischaemia | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 22 | Antegrade root pressure 60-100 mmHg; retrograde 200-400 mL/min at coronary-sinus pressure 30-50 mmHg; arrest 30-60 s vs 2-4 min | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 23 | HTK single dose perfused over 6-8 min, about 1.5-2 L in adults (UK SmPC; brochure: 20-25 mL/kg); the label gives no cardioplegic protection time, and 120-180 min is a manufacturer-brochure claim only [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-6] | https://www.medicines.org.uk/emc/product/14445/smpc | A |
| 24 | Alpha-stat is IIa, B for adults with high-moderate hypothermia | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 25 | BIS falls about 1.2 units per °C of cooling; propofol level 28% higher at 34 °C; fentanyl falls 30-60% at CPB start | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 26 | K+ > 6.5-7 mmol/L on CPB should be treated | https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ | A |
| 27 | CALS: 3 stacked shocks, re-sternotomy within 5 min, internal 20 J, epinephrine 50-100 µg | https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/ | A |
| 28 | Vasopressin 0.01-0.04 U/min; t½ 10-35 min; no rise in PVR | https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/ | A/B |
| 29 | Norepinephrine 0.01-0.3 (up to 1) µg/kg/min, t½ 2-3 min; milrinone t½ 2.3-2.4 h | https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/ | B |
| 30 | Viscosity 4 cP at Hct 40%, −25% at 30%, −45% at 20%, +2%/°C cooling | https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/ | A |

---

## Sources

1. Pulse Physiology Engine - home page - https://pulse.kitware.com/ - license, APIs, platforms, methodology list.
2. Pulse - version history - https://pulse.kitware.com/version.html - 4.4.0 (Aug 2026) and earlier features (ACLS 4.1.0, ECMO, drugs).
3. Pulse - About - https://pulse.kitware.com/_about_pulse.html - 20 ms step, lumped circuits, validation counts.
4. Pulse - ECMO methodology - https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html - ECMO model, limits, sweep validation.
5. Pulse - Drugs methodology - https://pulse.kitware.com/_drugs_methodology.html - drug list, PBPK and PD approach and limits.
6. Pulse - Cardiovascular methodology - https://pulse.kitware.com/_cardiovascular_methodology.html - heart model, arrhythmias, ECG, hemorrhage, no CPB.
7. Pulse NOTICE file - https://gitlab.kitware.com/physiology/engine/-/raw/stable/NOTICE - Apache-2.0, fork of BioGears 6.1.1, third-party libraries.
8. Unity Asset Store - Pulse Physiology Engine - https://assetstore.unity.com/packages/slug/139773 - version 4.3.1, 5 Feb 2025, free, Standard EULA.
9. Kitware - Pulse on the Unity Asset Store (2019) - https://www.kitware.com/pulse-is-now-available-on-the-unity-asset-store/ - Unity asset contents.
10. Kitware - Pulse Unreal plugin (2022) - https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/ - UE 4.26/5.0, Actor Component, Apache-2.0.
11. Kitware Discourse - Changing step size - https://discourse.kitware.com/t/changing-step-size/1068 - 0.04 s OK, > 0.06 s unreliable (C).
12. Kitware Discourse - HumMod vs BioGears vs Pulse - https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547 - 10-15× real time; HumMod described as closed source (C).
13. BioGears core (GitHub) - https://github.com/BioGearsEngine/core - Apache-2.0, 8.2.0 noted Jan 2025.
14. BioGears releases - https://github.com/BioGearsEngine/core/releases - release history, Unreal and C# notes.
15. CircAdapt - https://www.circadapt.org/ - model description, real-time web simulator, no license shown.
16. CircAdapt framework install docs - https://framework.circadapt.org/latest/userguide/installation.html - version label 2509, no license text.
17. Osta et al. 2025, CircAdapt Framework (Maastricht record) - https://cris.maastrichtuniversity.nl/en/publications/the-circadapt-framework-create-fast-computational-models-of-cardi/ - architecture (C++, Python, UI) (C).
18. OpenCOR (GitHub) - https://github.com/opencor/opencor - GPL-3.0.
19. Smith, Chase et al. 2004 CellML model (Physiome Model Repository) - https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml - minimal CV model (C).
20. Smith et al. 2004 bibliographic record - https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_71751123 - Med Eng Phys 26(2):131-139, results (C).
21. Hester et al. 2011, HumMod (Frontiers in Physiology) - https://www.frontiersin.org/articles/10.3389/fphys.2011.00012/pdf - HumMod description and download (C).
22. Physiomodel (GitHub) - https://github.com/physiology/Physiomodel - Modelica port of HumMod; dual license (C).
23. Physiolibrary license page - https://build.openmodelica.org/Documentation/Physiolibrary.UsersGuide.License.html - BSD-3-Clause (C).
24. Ursino 1998, carotid baroregulation model (index) - https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/60319985 - baroreflex model, hemorrhage response (C).
25. Westerhof, Lankhaar & Westerhof 2009, The arterial Windkessel - https://pubmed.ncbi.nlm.nih.gov/18543011/ - 3-element Windkessel.
26. Suga & Sagawa 1973, time-varying elastance (record) - https://scilit.net/publications/7c0ae8fc02a2142815b3b1438ddbad30 - Emax concept and epinephrine effect (C).
27. PhysioNet ECGSYN - https://physionet.org/content/ecgsyn/ - version, date, GPL-3.0, parameters.
28. PhysioNet MIT-BIH Arrhythmia Database - https://physionet.org/content/mitdb/1.0.0/ - ODC-By 1.0, contents.
29. Wahba et al. 2024 EACTS/EACTAIC/EBCP Guidelines on CPB in adult cardiac surgery (BJA 2025) - https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/ - most CPB targets and recommendations.
30. 2019 EACTS/EACTA/EBCP Guidelines on CPB in adult cardiac surgery - https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377/ - K+, BIS, glucose, protamine ratio data, weaning checklist.
31. Engelman et al. 2015 STS/SCA/AmSECT temperature management during CPB - https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ - temperature recommendations.
32. Shore-Lesserson et al. 2018 STS/SCA/AmSECT anticoagulation during CPB - https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/ - heparin, ACT, protamine, bivalirudin.
33. AmSECT - STS/SCA/AmSECT guidelines page - https://amsect.org/Policy-Practice/Perfusion-Safety/STS-SCA-AmSECT-Guidelines - list of the joint guidelines (B).
34. Kim et al. 2014, del Nido cardioplegia at the Cleveland Clinic (JECT 46:317-323) - https://ject.edpsciences.org/articles/ject/pdf/2014/04/ject-46-317.pdf - circuit setup, Buckberg and del Nido protocols.
35. Custodiol-HTK trial record - https://clinicaltrials.gov/study/NCT01681095 - HTK dose and duration (C, via search summary).
36. D'Angelo et al. 2022, re-dosing of del Nido - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8972223/ - redosing practice (C).
37. OpenAnesthesia - CPB components, gas exchange, priming - https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/ - circuit components (B).
38. OpenAnesthesia - Protamine reactions - https://www.openanesthesia.org/keywords/protamine-reactions/ - reaction types, rate limit (C, snippet).
39. Ranucci et al. 2023, Arterial pressure management on CPB - https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/ - viscosity numbers, MAP outcome data.
40. VUMC CVICU - Hemodynamic Parameters sheet - https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf - normal hemodynamic values (B).
41. Kato et al. 2024, Vasopressin in cardiovascular surgery - https://pmc.ncbi.nlm.nih.gov/articles/PMC11676985/ - vasoplegia definition, vasopressin doses and half-life.
42. Shankar et al. 2022, Vasoactive medication in cardiogenic shock - https://pmc.ncbi.nlm.nih.gov/articles/PMC8829716/ - vasoactive doses, receptors, half-lives.
43. Pfizer milrinone dosage page - https://www.pfizermedicalinformation.com/milrinone-lactate/dosage-admin - milrinone dosing (C, snippet).
44. StatPearls - Dobutamine - https://www.ncbi.nlm.nih.gov/books/NBK470431/ - dose, onset, half-life (C, snippet).
45. StatPearls - Phenylephrine - https://www.ncbi.nlm.nih.gov/sites/books/NBK534801/ - bolus dose (C, snippet).
46. StatPearls - Epinephrine - https://www.ncbi.nlm.nih.gov/sites/books/NBK482160/ - arrest and infusion doses (C, snippet).
47. AHA 2025 Adult Cardiac Arrest Circular Algorithm - https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/Algorithm-ACLS-CA-Circular-250620.pdf?sc_lang=en - lidocaine doses (C, snippet; PDF returned 403).
48. ACLS-algorithms 2025 changes - https://acls-algorithms.com/new-2025-aha-acls-guideline-changes/2025-adult-cardiac-arrest-algorithm-changes/ - amiodarone 300/150 mg (C).
49. Karcher et al. 2022, CALS-ANZ guidelines - https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/ - post-cardiac-surgery arrest protocol.
50. Reperfusion VF trial (lidocaine vs amiodarone) - https://arya.mui.ac.ir/article_10381.html and https://clinicaltrials.gov/study/NCT00587483 - VF rates and internal shock energies (C).
51. Pfizer Amidate (etomidate) label - https://www.pfizermedical.com/amidate - induction dose (C, snippet).
52. Diprivan label (medlibrary) - https://medlibrary.org/lib/rx/meds/diprivan/page/2/ - cardiac anesthesia dosing (C, snippet).
53. Zemuron (rocuronium) archived FDA label - https://webarchive.library.unt.edu/eot2008/20090118024358/http:/www.fda.gov/medwatch/safety/2008/Aug_PI/Zemuron_PI.pdf - intubating dose and duration (C, snippet).
54. Fentanyl injection label (drugs.com) - https://www.drugs.com/pro/fentanyl-injection.html - high-dose fentanyl (C, snippet).
55. Nexterone label (drugs.com) - https://www.drugs.com/pro/nexterone.html - amiodarone infusion regimen (C, snippet).
56. Eleveld et al. 2018 propofol PK/PD model (abstract record) - https://pesquisa.bvsalud.org/ses/resource/pt/mdl-29661412 - parameters for a reference patient (C, snippet).
57. Post-operative lactate study - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4797582/ - lactate thresholds (C, snippet).
58. Heart (BMJ) review on post-CABG AF - https://heart.bmj.com/cgi/doi/10.1136/hrt.2007.132795 - AF incidence and timing (C, snippet).
59. Pacemaker after SAVR (Erasmus record) - https://repub.eur.nl/pub/56438 - heart block and pacemaker rates (C, snippet).
60. Hypothermia and VF review - https://pmc.ncbi.nlm.nih.gov/articles/PMC8904885 - VF below 28-30 °C (C, snippet).
61. The Blood Project - heparin half-life - https://www.thebloodproject.com/ufaq/what-is-the-half-life-of-unfractionated-heparin-2/ - dose-dependent half-life (C, snippet).
62. MPOG measure (STS glucose guideline) - https://measures.mpog.org/Spec/Public/71 - glucose ≤ 180 mg/dL (B).
63. BMC Anesthesiology 2015, sternotomy response - https://pmc.ncbi.nlm.nih.gov/articles/PMC4322556 - sternotomy hemodynamics (C, snippet).
64. Perfusion.com - virtual patient CPB simulator - https://perfusion.com/an-educational-training-simulator-for-advanced-perfusion-techniques-using-a-high-fidelity-virtual-patient-model/ - existing CPB simulator design (B).
65. Hemodilution and blood-volume estimation (Lee et al.) - https://pmc.ncbi.nlm.nih.gov/articles/PMC6586263 - EBV 70/65 mL/kg (C, snippet).
66. Hypothermia categories in CPB studies - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9145413/ - mild and moderate ranges (C, snippet).
67. Scottish Intensive Care Society - KDIGO AKI staging - https://www.scottishintensivecare.org.uk/?p=3595 - urine output criteria (C, snippet).
68. JECT 1995 oxygenator comparison - https://ject.edpsciences.org/articles/ject/pdf/1995/01/ject1995271p15.pdf - PaO2 150-250 window (C, snippet).

---

## Summary

**Key findings**
- **No open engine models CPB.** Pulse (Apache-2.0; 4.4.0 listed Aug 2026) is the most mature and game-ready engine, with free Unity and Unreal plugins. It lacks cross-clamp, cardioplegia, a venous reservoir, heat exchange and anticoagulation. Its ECMO pump is an ideal flow source. It models only the ventricles, uses a template ECG, and lacks several cardiac drugs.
- **The CPB targets are well defined by current guidelines:**
  - flow 2.2-2.8 L/min/m²;
  - DO2 ≥ 280 mL/min/m² (I-A);
  - MAP 50-80 mmHg (I-A);
  - Hct transfusion trigger < 18% (I-C);
  - arterial outlet ≤ 37 °C (I-A / I-C);
  - gradient ≤ 10 °C, and ≤ 4 °C with ≤ 0.5 °C/min above 30 °C (IIa-B);
  - ACT > 480 s (IIa-C);
  - protamine ratio < 1.0 (I-B);
  - alpha-stat (IIa-B).
- **Cardioplegia protocols with exact numbers** are available for Buckberg, del Nido and HTK. HTK numbers come mainly from manufacturer material.
- **Vasoactive and antiarrhythmic dose ranges and half-lives** are available for a PK/PD model. Effect sizes (EC50, Emax) are not published in a game-ready form and must be tuned.
- **CALS rules** for post-cardiac-surgery arrest differ from standard ACLS: 20 J internal shocks, re-sternotomy within 5 min, epinephrine 50-100 µg.

**Recommendations**
1. Build a **custom 0-D core** in the game engine: 4-chamber time-varying elastance heart, 3-element Windkessels, Ursino baroreflex, explicit CPB circuit, O2/CO2 transport, temperature, heparin/ACT and PK/PD. Run it at **50 Hz**.
2. Use **Pulse 4.4.0 as a validation oracle**, and optionally live for the off-pump scenes. Pin the version, keep the LICENSE and NOTICE, and mark any changes.
3. **Re-implement** ECGSYN and the CellML models from their papers. Do not ship GPL code. Use MIT-BIH (ODC-By) only as reference data, with attribution.
4. Encode the guideline tables as a **rules engine** for scoring. The surgical state machine changes only physiology *inputs*, never displayed numbers.
5. Keep a **parameter file** (JSON) with every value and its source URL, so a medical reviewer can audit and tune it.

**Open questions**
- CircAdapt is under a custom academic, non-commercial EULA [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-4]. The HumMod license is unverified. Ask the authors before using it.
- The HTK protection time (180 min) and dose come from manufacturer material only. The UK SmPC (rev. 05/2024) gives a 6-8 min perfusion of about 1.5-2 L and no protection time [Step 2 check: corrected, see verification/02-physiology-anesthesia-perfusion-check.md#02-6].
- There is no source for heart-lung-machine time constants (e.g. how fast MAP falls at CPB start in seconds), for ACT turnaround time, or for the exact ACT-vs-heparin curve. These need perfusionist input or the full ECCSIM/Orpheus papers.
- PD effect sizes (EC50, Emax) for norepinephrine, vasopressin, phenylephrine and milrinone in anesthetized cardiac patients were not found in usable form.
- Which hypothermia classification the game should show (CPB-study bands vs the circulatory-arrest consensus bands).
- The guideline wording for LCOS ("cardiac index of 2.4") and NIRS ("below 15% of baseline") is ambiguous as printed. Confirm against the PDF.
- StatPearls and AHA PDF pages could not be read directly (bot check / 403). Their numbers are snippet-only and should be re-checked by a human.
