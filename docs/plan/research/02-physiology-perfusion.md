# Research 02 — Physiology, Anesthesia and Perfusion Simulation

> Step 1 research input for plan section 3, "Physiology, anesthesia and perfusion simulation".
> Researched on 2026-11-03. This is a personal, educational, non-commercial game. **It is not a medical device.**
> All doses and targets below are here so the game can behave realistically. They are not clinical guidance.
> Claims carry inline source links. "(uncertain)" marks values I could not confirm from a primary source.
> "UNVERIFIED" marks a license I could not confirm.

---

## 0. Summary

- **Core engine: Kitware Pulse Physiology Engine 4.4.0 (Apache-2.0).** It is the only open, maintained and validated whole-body engine with official Unity (C#) and Unreal plugins, and it is free to use. It models cardiovascular, respiratory, blood chemistry/ABG, PBPK drugs, the anesthesia machine, hemorrhage, arrhythmias/CPR, and, since 4.4.0, a VA/VV ECMO device. It has **no cardiopulmonary-bypass (CPB), aortic cross-clamp, cardioplegia, coagulation/heparin/ACT, atrial fibrillation or computed ECG.**
- **The CPB, coagulation, myocardial-protection and monitor-signal layers must be custom-built.** The most promising route is to drive Pulse's VA-ECMO device (it has right-atrium and ascending-aorta cannula sites) as the "heart-lung machine" core. Custom reservoir, pump, heat-exchanger, cardioplegia and ACT logic sit around it.
- **The main technical risk:** in Pulse, asystole, PEA and VF "suppress hemodynamics", and later actions have no effect during them. A cardioplegic arrest therefore may not coexist with ECMO-driven perfusion. **A 1–2 week spike must test this first.** If it fails, the fallback is a custom 0-D lumped-parameter model (time-varying elastance plus Windkessel) that uses Pulse as a tuning reference.
- Guideline numbers to drive the CPB sim: pump flow 2.2–2.8 L/min/m²; MAP on bypass 50–80 mmHg (Class I A); DO₂i ≥ 280 mL/min/m² (Class I A); transfuse if Hct < 18%; ACT > 480 s; heparin 300–400 IU/kg; protamine-to-heparin ratio < 1:1; arterial outlet ≤ 37 °C; cooling/rewarming gradient ≤ 10 °C (≤ 4 °C and ≤ 0.5 °C/min once the outlet is ≥ 30 °C); blood cardioplegia every 20–30 min; del Nido single dose for up to 90 min.

---

## 1. Open-source physiology engines usable in a game

### 1.1 Kitware Pulse Physiology Engine — recommended core

| Item | Finding |
|---|---|
| License | **Apache-2.0** with a NOTICE file ([pulse.kitware.com](https://pulse.kitware.com/)). Personal and commercial use are both allowed. Attribution means keeping the LICENSE/NOTICE files. There is no share-alike. |
| Latest version | **4.4.0 (August 2026)**. History: 4.0.0 (Sep 2021), 4.1.0 (Mar 2022), 4.2.0 (Oct 2023), 4.3.0 (Sep 2024), 4.3.1 (Jan 2025) ([version history](https://pulse.kitware.com/version.html)) |
| Language/APIs | C++17 core. Interfaces for C, C#, Java and Python ([pulse.kitware.com](https://pulse.kitware.com/)). |
| Unity | Free Asset Store package (C# API). Windows, macOS, Linux, Android, iOS, xrOS and WebGL. Includes an optional vitals monitor and example scenes. Apache-2.0. It exposes only part of the C++ functionality and **does not work out of the box with IL2CPP** ([Kitware: Pulse on Unity Asset Store](https://www.kitware.com/pulse-is-now-available-on-the-unity-asset-store/), [Pulse Unity 4.1](https://kitware.com/pulse-unity-4-1-released)). |
| Unreal | Free plugin made with Lumeto under an Epic MegaGrant. Apache-2.0. Actor Component plus Blueprints and an example vitals monitor. Win64 only. Marketplace builds cover UE 4.27–5.3 ([Kitware/Lumeto blog](https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/), [Kitware forum](https://discourse.kitware.com/t/unreal-engine-5-1/999)). UE 5.4+ would need building from source (uncertain). |
| Time step / speed | Internal step 0.02 s (50 Hz) ([Kitware forum](https://discourse.kitware.com/t/changing-step-size/1068)). Runs "10-15x real time" on laptops ([Kitware forum](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547)). `AdvanceModelTime` loses time if the request is not a multiple of the step ([GitLab issue 18](https://gitlab.kitware.com/physiology/engine/issues/18)). |
| Cardiovascular | Lumped R-C circuit with ~31 compartments. Time-varying-elastance LV/RV (double Hill). **Atria are not modeled.** Valves are ideal (no backflow). Baroreflex present. **No dicrotic notch.** Hemorrhage is flow- or severity-based, plus internal (abdomen). Also pericardial effusion, CPR, IV fluids ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). |
| Arrhythmias | Sinus brady/tachy, asystole, PEA, coarse/fine VF, stable/unstable/pulseless VT (ACLS set added in 4.1). Transitions take ~60 s, except asystole/PEA/VF, which are instant. **"Asystole, PEA, and VF suppress hemodynamics, so later actions have no effect during them."** **No AF, flutter, heart block or pacing** ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). Defibrillation waveform added in 4.4.0 ([versions](https://pulse.kitware.com/version.html)). |
| ECG | A stored waveform played back at the current HR. It is **not computed** from electrical activity ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). |
| Blood chemistry | ABG assessment (pH, HCO₃⁻, PaO₂, PaCO₂, SaO₂), base excess, Hb/Hct, lactate, K⁺, Na⁺, Ca²⁺, glucose, creatinine, CBC and a partial metabolic panel. **Coagulation is not modeled.** Platelets and WBC are excluded ([blood chemistry methodology](https://pulse.kitware.com/_blood_chemistry_methodology.html)). |
| Drugs | PBPK pharmacokinetics plus a sigmoid-Emax pharmacodynamic model. 17 drugs: albuterol, etomidate, epinephrine, fentanyl, furosemide, ketamine, lorazepam, midazolam, morphine, naloxone, pralidoxime, prednisone, propofol, rocuronium, succinylcholine, norepinephrine, phenylephrine. Stated limitations: the plasma-concentration calculation "is currently incorrect", responses take 30–60 s regardless of drug, EC50s are too high, there are no interactions, and validation is qualitative ([drugs methodology](https://pulse.kitware.com/_drugs_methodology.html)). **Missing for this game:** milrinone, dobutamine, vasopressin, heparin, protamine, sufentanil/remifentanil, cisatracurium, nitroglycerin, amiodarone, CaCl₂, TXA, insulin. 4.3.0 added cardiovascular and respiratory "modifier actions" that can scale mechanics directly ([versions](https://pulse.kitware.com/version.html)). |
| Anesthesia machine | Pressure-controlled only. FiO₂, PEEP, RR, I:E. Failures include leaks, Y-piece disconnect, valve obstruction, soda-lime failure, vaporizer failure and O₂ supply loss. The documentation names only **desflurane** as an agent. The model is marked "under development" ([anesthesia machine methodology](https://pulse.kitware.com/_anesthesia_machine_methodology.html)). |
| ECMO (4.4.0) | New device model with VA and VV configurations. 14 cannula sites, **including right atrium, SVC, IVC and ascending aorta**. The centrifugal pump is an *ideal flow source* (default 3.0 L/min) with no pressure-flow curve. The oxygenator uses a diffusion model (DL_O₂ 5, DL_CO₂ 10 mL/s/mmHg) with sweep flow and FdO₂. Bag/infuser compounds include Blood, Saline and PackedRBC. **No heat exchanger, anticoagulation, hemolysis or thrombosis.** VA is validated by an automated scenario only ([ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)). |
| Cardiopulmonary bypass | **Not modeled.** There is no bypass, aortic cross-clamp or cardioplegia ([CV methodology](https://pulse.kitware.com/_cardiovascular_methodology.html)). |

### 1.2 Other engines and models

| Engine / model | License (personal use?) | Status | What it gives us | Verdict |
|---|---|---|---|---|
| **BioGears** (ARA) | Apache-2.0, personal use OK ([GitHub BioGearsEngine/core](https://github.com/BioGearsEngine/core)) | Last release in the README notes is 8.2.0 (Jan 2025). Last push 2026-01-17 per an ecosyste.ms index (uncertain). The old `Engine` repo was archived in Jan 2024 ([search summary](https://github.com/BioGearsEngine/Engine)). | The ancestor of Pulse (Pulse forked it in 2017). Similar systems. The oldest speed figure I found is "90Hz for 2x real-time" (BioGears slides, uncertain). No maintained Unity/Unreal plugin found (uncertain). | Second choice. No advantage over Pulse for CPB. |
| **CircAdapt** (Maastricht) | **Restricted.** Granted "for educational, non-commercial and research purposes" to "Academic Researchers" (university staff/students). Revocable. Source only for "Developer Users" ([CircAdapt license](https://framework.circadapt.org/latest/license.html)). A hobbyist is **not clearly covered**, so treat it as **not allowed** without written permission. | Active; releases up to 2602 ([framework.circadapt.org](https://framework.circadapt.org/)). C++ core with Python, plus a FIMH 2025 paper ([Maastricht CRIS](https://cris.maastrichtuniversity.nl/en/publications/the-circadapt-framework-create-fast-computational-models-of-cardi/)). | Best-in-class ventricular mechanics and interaction (VanOsta2024 model). Real-time ([circadapt.org](https://www.circadapt.org/)). | Do not embed. Read its papers for ideas only. |
| **HumMod** (UMMC / HC Simulation) | "Freely usable for personal, educational, and research purposes". You may not modify or reverse-engineer the engine; XML may be edited for personal use; commercial use needs written approval ([HumMod agreement](https://hummod.org/agreement)) | Windows-only exe, ©2016 ([hummod.org](https://hummod.org/)). About 5000 variables ([Hester et al. 2011](https://www.frontiersin.org/articles/10.3389/fphys.2011.00012/full)). | Very broad integrative physiology (renal, endocrine, long-term). | Not embeddable in a game engine. Use as a reference only. |
| **Physiolibrary / Physiomodel** (Modelica) | Physiolibrary: **BSD-3-Clause** since 3.0.0 (2023-10-09) ([GitHub modelica-3rdparty/Physiolibrary](https://www.github.com/modelica-3rdparty/Physiolibrary)). Physiomodel (HumMod 1.6 port): UNVERIFIED. | Maintained | Modelica components (hydraulic, gases, thermal) that can be exported as FMUs. | Optional reference for building a custom 0-D model. |
| **OpenCOR / libOpenCOR + CellML models** | OpenCOR: GPL-3.0. libOpenCOR: Apache-2.0 ([OpenCOR licensing](https://github.com/opencor/opencor/blob/80e6cce0d4d853e1f5ab6424505b2ea7d545a441/doc/user/licensing.html), [search summary](https://opencor.ws/developer/thirdPartyLibraries.html)). Physiome Model Repository licenses are per model: **UNVERIFIED** ([PMR](https://models.physiomeproject.org/)). | Maintained | The Smith 2004 minimal CV model with ventricular interaction and valve dynamics ([CellML file](https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml)). It is also in BioModels as SBML MODEL1006230000, listed as CC0 (uncertain, [OmicsDI](https://www.omicsdi.org/dataset/biomodels/MODEL1006230000)). | Good equations for the fallback custom model. Re-implementing from the paper (Med Eng Phys 2004;26:131) avoids license questions. |
| **Explain engine** (Radboudumc, T. Antonius) | **MIT** ([GitHub explain-labs](https://github.com/explain-labs)) | Active (Nov 2026) | Dependency-free JS cardiorespiratory engine with ventilator, PDA and ECLS scenarios. It runs in a Web Worker. Neonatal focus; adult support is unclear ([explain-engine](https://github.com/explain-labs/explain-engine)). | Good *architecture* reference (JSON model definition, worker loop). Wrong patient population. |
| **ECMOjo** (Univ. Hawaii) | BSD ([SourceForge](https://sourceforge.net/projects/ecmojo)) | Old (Java) | Screen-based VA/VV ECMO trainer with circuit faults ([search summary](https://www.intuitionlabs.ai/software/intensive-care-critical-care/ecmo-management-platforms/ecmojo)). | Reference for perfusion UI and failure scenarios. |
| **Windkessel / lumped models** | The math is free to implement | n/a | Two-element (R, C) and three-element (adds characteristic impedance) arterial load ([Westerhof et al. 2009, PubMed 18543011](https://pubmed.ncbi.nlm.nih.gov/18543011/)). | Building block for the fallback and for the CPB circuit's arterial side. |

### 1.3 Comparison for this game

| | Fidelity (whole body) | CPB support | Speed | Game integration effort | License fit |
|---|---|---|---|---|---|
| Pulse 4.4 | High (validated per system) | Partial (VA-ECMO device only) | 10–15× RT at 50 Hz | **Low** (Unity/Unreal plugins) | Excellent |
| BioGears 8.x | High | None | ~2× RT at 90 Hz (old, uncertain) | Medium–high (C++ only) | Excellent |
| CircAdapt | Very high (heart) | None | Real-time | Medium | **Blocked** |
| HumMod | Very high (integrative) | None | Unknown | Not feasible (closed exe) | Personal OK, no modification |
| Custom 0-D (Smith/Windkessel) | Low–medium (only what we build) | Full (we design it) | Microseconds per step | Medium (we write and validate it) | Excellent |
| Explain | Medium (neonate) | ECLS (neonatal) | Real-time at 2 kHz | Medium (JS) | Excellent (MIT) |

---

## 2. Cardiopulmonary bypass (CPB) circuit

### 2.1 Components (what to model and show)

Typical circuit order: venous cannula(s) → venous line → **venous reservoir** (hard-shell open, or a closed bag) → **arterial pump** (roller or centrifugal) → **heat exchanger** (usually built into the oxygenator) → **membrane oxygenator** (microporous polypropylene hollow fibre; sweep gas inside the fibres, blood outside) → **arterial line filter/bubble trap** → arterial cannula (usually ascending aorta; sometimes axillary or femoral). Accessory parts: **cardiotomy suckers**, **LV/aortic-root vent**, **cardioplegia delivery system** (separate pump, heat exchanger, pressure line), **hemofilter (ultrafiltration)**, safety monitors and PVC tubing ([OpenAnesthesia: CPB components](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)).

- **Pumps.** Roller pumps compress the tubing; over-occlusion means spallation, hemolysis or rupture. Centrifugal pumps are "non-occlusive", "preload dependent and afterload-sensitive", and "should always be combined with a flow probe" ([2024 EACTS/EACTAIC/EBCP CPB guideline, BJA 2025, PMC11947607](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
  - *Game model:* roller flow = RPM × stroke volume per revolution (it ignores afterload). Centrifugal flow comes from an H-Q curve: flow drops when the line kinks or MAP rises, and it reverses at low RPM (uncertain shape; tune by feel).
- **Oxygenator gas control.** Raising sweep flow increases CO₂ removal. O₂ transfer depends on sweep FiO₂/flow and on blood flow and Hb ([OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)). Guideline: "gas flow be adapted to avoid hypercapnic acidosis" (I C) ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). Pulse's ECMO oxygenator already implements this diffusion behaviour ([Pulse ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)).
- **Venous drainage.** Gravity, or vacuum-assisted (VAVD). Hemolysis rose at −80 mmHg compared with −40 mmHg; −40 to −60 mmHg looked safe. VAVD needs an approved reservoir, negative-pressure monitoring (I C) and a reservoir **level sensor** (I C) ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
- **Monitoring (Class I C):** ultrasonic arterial flow measurement; pressure pre- and post-oxygenator and on the cardioplegia line; continuous SvO₂ and Hct (I B); CO₂ flush before priming (I B) ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).
- **Prime.** Crystalloid (balanced salt) ± colloid ([OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)). Guideline: minimize prime volume and use retrograde/antegrade autologous priming (I A). Starches and routine mannitol are not recommended (III) ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)). Conventional adult total prime is about 2–2.5 L ([patent description](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5429184)); modern low-prime/MiECC circuits use less (exact figure uncertain). Plasma-Lyte prime can cause hypocalcaemia ([guideline refs](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

### 2.2 Key perfusion targets (game "rules")

| Parameter | Target / rule | Source |
|---|---|---|
| Pump flow | 2.2–2.8 L/min/m² at moderate hypothermia to normothermia; set from BSA and planned temperature before CPB (I C). The classic textbook figure is 2.4. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Oxygen delivery (DO₂i) | **≥ 280 mL/min/m²** (I A, reduces AKI stage 1). Goal-directed perfusion with 280–300 at normothermia (IIa B). Nadir < 280 gave AKI 29.8% vs 12.1% in the GIFT cohort. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [GIFT NCT02250131](https://clinicaltrials.gov/study/NCT02250131) |
| MAP on CPB | **50–80 mmHg**, using vasoconstrictors or vasodilators once anesthetic depth and flow are adequate (I A). Vasoplegia → α1-agonist and/or vasopressin (I C). Methylene blue / hydroxocobalamin / angiotensin II as rescue (IIa–IIb). | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [Conundrum of MAP on CPB, PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) |
| SBP during aortic cannulation | Commonly kept < 100 mmHg (dissection risk) | [2024 guideline text](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| Hematocrit | Transfuse PRBC if **Hct < 18% (Hb 6.0 g/dL)** (I C). At 18–24%, transfuse based on oxygenation (IIb B). Do not transfuse if Hct > 24% with acceptable DO₂ (III C). Hct 21–24% is acceptable if DO₂ > 273. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| SvO₂ | Monitor continuously (I B). SvO₂ > 75% was associated with less AKI. | [2024 guideline](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| Temperature limits | Arterial outlet **< 37 °C** (I). Arterial–venous gradient **≤ 10 °C** during cooling and rewarming (I). With the outlet ≥ 30 °C: gradient **≤ 4 °C** and rewarming **≤ 0.5 °C/min** (IIa B). Wean on PA or nasopharyngeal temperature (IIa C). | [STS/SCA/AmSECT 2015, PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/) |
| Hypothermia categories (core) | Mild 28.1–34 °C; high-moderate 24.1–28; low-moderate 20.1–24; deep 14.1–20. Cerebral metabolic rate falls 6–7%/°C. Note that perfusion slang often calls 32–35 °C "mild" (uncertain mapping). | [2024 guideline Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Acid–base | Alpha-stat (uncorrected) is standard for adults at mild–moderate hypothermia. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Lactate | Peak > 3 mmol/L during CPB occurs in 10–20% and goes with morbidity (low output). > 5 mmol/L goes with higher mortality. | [Ranucci 2006, PMC1794481](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1794481/), [Seghrouchni 2022, PMC8767239](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8767239/) |
| Glucose | Keep ≤ 180 mg/dL (10 mmol/L) with an IV insulin infusion | [STS 2009 guideline (Lazar), via MPOG measure](https://measures.mpog.org/Spec/Public/71) |
| Potassium | Rises with cardioplegia. Treat if > 6.5–7 mmol/L (ultrafiltration, calcium, insulin). Aim for about 4–5 before weaning (uncertain; Stanford guide says ~5). | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Calcium | Hypocalcaemia from hemodilution and citrated products; treat if there is bleeding, arrhythmia or hypotension. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

Derived formulas for the sim (standard physiology):
- `CaO2 (mL/dL) = 1.34 × Hb × SaO2 + 0.003 × PaO2`
- `DO2i = pump flow index (L/min/m²) × CaO2 × 10`
- Hemodilution on going on bypass: `Hct_on = Hct_pre × BV / (BV + prime + crystalloid)`, with BV ≈ 70 mL/kg (male) or 65 mL/kg (female) (uncertain)
- Viscosity is about 4 cP at Hct 40%, about 25% lower at Hct 30% and about 45% lower at Hct 20%. It rises about 2% per °C of cooling ([PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/)). This drives the MAP drop when bypass starts.

### 2.3 Anticoagulation: heparin, ACT, protamine

| Item | Value | Source |
|---|---|---|
| Heparin initial dose | **300–400 IU/kg** (total body weight) | [Cartwright & Mundell, BJA Educ 2023, PMC9947996](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996); [Levy review](https://www.hematologyandoncology.net/archives/september-2013/the-effects-of-cardiopulmonary-bypass-on-coagulation/) |
| ACT target | **> 480 s** with uncoated circuits and cardiotomy suction. Surveyed practice is 400–500 s. ACT checks "at regular intervals" with re-dosing (I C). One study gave 5000 IU boluses if ACT < 480. | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [Brazilian RCT PMC7731843](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7731843/) |
| Baseline ACT | About 120 s (Hemochron study: 122.9 ± 21.1 s). It depends on the device. | [search summary of Hemochron study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6728977) (uncertain) |
| Heparin resistance | ACT ≤ 480 s despite 300–400 (or 500) U/kg. Antithrombin < 60% raises the odds. Treat with AT concentrate (I B). | [PMC9947996](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996), [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Protamine dose | About 1 mg per 100 U heparin. Keep the **protamine-to-heparin ratio < 1.0** and avoid overdosing (I B). STS/SCA cap: 2.6 mg/100 U. A low-dose infusion of 25 mg/h may follow (rebound). | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [PMC9947996](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996), [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/) |
| Protamine rate | Give slowly over 10–15 min (≤ 20 mg/min per OpenAnesthesia; label limits are slower, uncertain) | [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/) |
| Heparin rebound | 10–15% of patients given > 400 IU/kg; heparin detectable up to 2 h | [PMC9947996](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996) |
| Protamine reactions | **Type I:** isolated hypotension (fast injection, histamine). **Type II:** anaphylactic/anaphylactoid (hypotension, bronchospasm, high airway pressure). **Type III:** catastrophic pulmonary vasoconstriction (PA pressure ↑, RV failure, systemic hypotension). Incidence 0.06–10.6%. Risks: NPH insulin, fish allergy, other allergies. Treatment: stop or slow the infusion, give fluids (via aortic cannula), phenylephrine/norepinephrine/vasopressin/CaCl₂, epinephrine/milrinone, inhaled NO, albuterol; in severe cases re-heparinize and return to CPB. | [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/) |
| Alternatives (HIT) | Bivalirudin 1 mg/kg then 2.5 mg/kg/h (ACT > 300 s); argatroban 0.1 mg/kg then 5–25 µg/kg/min | [2024 guideline text](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| TXA | Maximum total 100 mg/kg (seizures above that) | [ERAS cardiac review, PMC8446225](https://pmc.ncbi.nlm.nih.gov/articles/PMC8446225) |

*Game model:* track heparin as a one-compartment PK whose half-life lengthens with dose (uncertain, ~1–2.5 h). Make ACT a monotonic function of heparin concentration (dose-response slope per patient, adding heparin-resistance variability), with extra prolongation from hemodilution and hypothermia (uncertain). Protamine neutralizes heparin 1 mg : 100 U at once. Excess protamine raises ACT a little and worsens bleeding ([guideline text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

### 2.4 Cardioplegia (myocardial protection)

| Solution | Composition / ratio | Dosing | Source |
|---|---|---|---|
| Buckberg-type blood cardioplegia | 4 parts blood : 1 part crystalloid (variants 1:1 to 5:1). Cold or tepid/warm. | Cold, intermittent **every 20–30 min**. Antegrade root pressure 60–100 mmHg. Retrograde 200–400 mL/min at coronary-sinus pressure 30–50 mmHg. Arrest in 30–60 s antegrade or 2–4 min retrograde. | [2024 guideline text](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| **del Nido** | 1 part blood : 4 parts crystalloid. Per litre of Plasma-Lyte A: 20% mannitol 16.3 mL, 50% MgSO₄ 4 mL, 8.4% NaHCO₃ 13 mL, KCl 13 mL (~26 mEq), 1% lidocaine 13 mL. | **20 mL/kg single dose, about 90 min of protection.** Given at 8–12 °C, 100–200 mmHg, 200–300 mL/min. Re-dosing protocols vary (e.g. every 45 min in one series, or after 60–90 min) (uncertain). | [del Nido review PMC6066678](https://pmc.ncbi.nlm.nih.gov/articles/PMC6066678), [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| HTK (Custodiol, Bretschneider) | Intracellular-type crystalloid, nearly sodium-free (causes iso-osmotic hyponatraemia; do not correct) | **20–25 mL/kg over 6–8 min** at root pressure 40–60 mmHg. Single dose, claimed up to ~3 h. | [Köhler brochure via search](https://annalscts.com/article/view/2881/pdf), [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| St Thomas No. 2 (Plegisol) | Extracellular-type crystalloid | Multidose | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

Guideline principles for the game: myocardial protection should be tailored to the patient (I C), and TOE should check LV/RV function before and after CPB (I B). Do not ventilate the lungs or give CPAP during cross-clamp (III A) ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

*Game model:* an "ischaemia clock" starts at cross-clamp. Each solution has a protection window (blood 20–30 min, del Nido ~90 min, HTK ~180 min). After the window, electrical activity returns (fibrillatory waves on ECG, rising myocardial temperature, uncertain) and a "myocardial injury" score builds up. Injury drives post-bypass contractility (stunning → low-output syndrome) and reperfusion VF probability.

---

## 3. Vital signs to display: normal, abnormal and event responses

### 3.1 Monitor channels and ranges

| Channel | Normal (anesthetised adult unless noted) | Abnormal / alarm ideas | Source |
|---|---|---|---|
| HR / ECG | 60–100 bpm; under anesthesia often 50–80 (uncertain) | < 40 or > 130; any VF/VT/asystole | standard |
| Arterial BP (radial A-line) | MAP 70–105 mmHg; diastolic 60–90 | MAP < 60 off-pump; MAP outside 50–80 on pump | [Edwards card via search](https://edwards.com/healthcare-professionals/pages/normal-hemodynamic-parameters-and-lab-values-card) |
| CVP / RAP | 2–6 mmHg (higher under positive-pressure ventilation) | > 15 (RV failure, tamponade, protamine type III); ~0 on full CPB | [Bootsma 2021, PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533) |
| PA pressure | 15–30 / 8–15 mmHg; PH = mean PAP **> 20 mmHg** | Mean > 35–40 (protamine type III, mitral disease); PCWP > 18 | [PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533), [PH definitions PMC10971453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10971453/) |
| PCWP | 6–12 mmHg | > 18 (LV failure) | [PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533) |
| CO / CI | CO 4–8 L/min; CI 2.5–4.0 L/min/m²; SV 60–100 mL | Low-output syndrome: CI ≤ ~2.4 L/min/m² with end-organ dysfunction (guideline wording) | [PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533), [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| SVR / PVR | SVR 800–1200 dyn·s·cm⁻⁵; PVR < 250 | SVR < 700 means vasoplegia (uncertain cut-off) | [PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533) |
| SvO₂ | 60–80% (on CPB aim > 75%) | < 60% | [PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533) |
| SpO₂ | 97–100% on FiO₂ 0.5–1.0 | < 92%. **The pleth signal is lost on full non-pulsatile CPB** (pulse oximetry needs a pulsatile signal) | standard (uncertain wording) |
| EtCO₂ | 35–45 mmHg; PaCO₂–EtCO₂ gap about 1–5 mmHg | Sudden drop means low CO, embolism or disconnect. ~0 when ventilation stops on full CPB. | [TTUHSC handout](https://healthedu.ttuhsc.edu/applicationfiles/EduFiles/PowerPoint/318313.Notes.pdf) (uncertain) |
| Temperature | Nasopharyngeal/PA/bladder 36–37.5 °C | > 37 °C during rewarming; < 36 °C at weaning | [PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/), [PMC8446225](https://pmc.ncbi.nlm.nih.gov/articles/PMC8446225) |
| Urine output | ≥ 0.5 mL/kg/h | < 0.5 mL/kg/h for 6 h = KDIGO AKI criterion | [KDIGO via Merck](https://www.merckmanuals.com/professional/multimedia/table/staging-criteria-for-acute-kidney-injury-kdigo-2012) |
| ABG | pH 7.35–7.45; PaCO₂ 35–45 mmHg; PaO₂ 80–100 on air (on CPB, high on purpose; target uncertain, ~150–250); HCO₃⁻ 22–26; BE −2 to +2 | pH < 7.25; BE < −5 | standard lab ranges ([patient.info](https://patient.info/treatment-medication/arterial-blood-gases)) (uncertain BE) |
| Lactate | < 2 mmol/L | > 3 (hyperlactatemia); > 5 (mortality signal) | [PMC1794481](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1794481/), [PMC8767239](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8767239/) |
| K⁺ | 3.5–5.0 mmol/L (4–5 at weaning) | < 3.5 (arrhythmia); > 6.5 (treat) | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Glucose | 4–10 mmol/L (≤ 180 mg/dL) | > 10 mmol/L (insulin) | [MPOG/STS](https://measures.mpog.org/Spec/Public/71) |
| Hb / Hct | Pre-op Hb 12–16; on CPB Hct ≥ 21–24% | Hct < 18% means transfuse | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| ACT | ~120 s baseline; > 480 s on CPB | < 400 on pump = clot risk (game failure state) | §2.3 |
| BIS (if shown) | 40–60 | > 60 = awareness risk; hypothermia lowers BIS ~1.2/°C | [OFACAR trial PMC13460324](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324), [2024 guideline text](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| Cerebral oximetry (rSO₂, optional) | Baseline > 50% | Fall > 15% from baseline = malperfusion | [2024 guideline text](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) |
| Perfusion screen | Flow (L/min and index), RPM, line pressures, reservoir level, sweep/FiO₂, T_arterial/T_venous/T_water, SvO₂/Hct inline, cardioplegia volume/pressure/timer, cross-clamp and CPB timers | Level low, air, high line pressure, ΔT > 10 °C | §2 |

### 3.2 ECG rhythms the game needs

| Rhythm / change | When it happens in cardiac surgery | Pulse native? |
|---|---|---|
| Sinus rhythm, sinus brady/tachy | Baseline; response to drugs and stimulation | Yes |
| **Atrial fibrillation / flutter** | Atrial cannulation/handling during surgery; post-op AF in 20–50% (valve 30–40%, combined 40–50%), peak on post-op days 2–3 | **No** ([POAF review PMC11784400](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11784400/)) |
| **Cardioplegic asystole** (flat line) | 30–60 s after antegrade cardioplegia | Asystole yes, but hemodynamics are suppressed (see risk) |
| **VF** (coarse/fine) | Reperfusion after cross-clamp removal: reported 10–80% (24–57% in cohorts). Internal defibrillation commonly starts at about 10–20 J (protocols escalate 2→20 J, then 30–50 J). Amiodarone prophylaxis lowers incidence. | Yes; defibrillation added in 4.4 ([search summary of studies](https://journal.hsforum.com/index.php/HSF/article/download/519/523/525)) |
| VT, PEA, asystole (non-plegic) | Ischaemia, hyperkalaemia, air, failure to wean | Yes |
| **Complete heart block / junctional; epicardial pacing (AAI/DDD/VVI)** | After cardioplegia, valve surgery or hyperkalaemia. Preferred order: sinus > atrial pacing > AV pacing > ventricular pacing, at HR 80–100 for weaning (flash-card level source, uncertain). | **No** |
| **ST elevation / depression, T-wave changes** | Ischaemia, coronary air (often the RCA → inferior leads, uncertain), graft problems. Chest-wall changes at sternotomy can produce T-wave changes. | **No** ([MGH Clinical Anesthesia Procedures](https://anesth.unboundmedicine.com/anesthesia/view/ClinicalAnesthesiaProcedures/728321/0/Anesthesia_for_Cardiac_Surgery___Induction)) |
| Peaked T waves | Hyperkalaemia after cardioplegia | No |
| Electrocautery artefact | Every time diathermy is used. A big realism win. | No |

### 3.3 How vitals respond to surgical events (state machine spec)

Times and magnitudes marked (uncertain) are design targets to tune, not literature values.

| Event | HR | Arterial line / MAP | CVP / PA | SpO₂ / EtCO₂ | Temp / labs | ECG | Typical player response |
|---|---|---|---|---|---|---|---|
| Induction + intubation | ±, often ↓ | MAP falls ~20–30% (uncertain); worse with propofol than etomidate | ↓ | EtCO₂ trace appears (35–40) | — | sinus | Vasopressor bolus (phenylephrine), fluids |
| Skin incision / **sternotomy** / retraction | ↑ (sympathetic surge, uncertain +10–20 bpm) | ↑ (uncertain +20–40 mmHg) | ↑ slightly | Lungs **deflated during the saw cut** → brief loss of EtCO₂ waveform | — | possible T-wave changes | Deepen anesthesia / opioid bolus ([MGH](https://anesth.unboundmedicine.com/anesthesia/view/ClinicalAnesthesiaProcedures/728321/0/Anesthesia_for_Cardiac_Surgery___Induction)) |
| Pericardiotomy / heart handling | ectopy | transient ↓ when heart is lifted | variable | — | — | PACs/PVCs, AF | Warn the surgeon, treat the rhythm |
| **Heparin** 300–400 U/kg | — | mild ↓ (uncertain) | — | — | **ACT ~120 → > 480 s within ~3–5 min (uncertain)** | — | Check ACT before cannulation |
| **Aortic cannulation** | — | **SBP held < 100 mmHg** | — | — | — | — | Lower BP (deepen, vasodilator) |
| **Venous (RA) cannulation** | ↑ / AF | ↓ (blood loss, impaired venous return) | ↓ | — | — | **AF/atrial ectopy** | Volume via aortic cannula, cardiovert or proceed |
| **Initiate CPB** (go on pump) | becomes irrelevant as heart empties | **MAP falls at first** (hemodilution: viscosity −40%, AV pressure −54% in one study), then recovers. **Waveform flattens to non-pulsatile** at full flow (target 2.2–2.8 L/min/m²). | CVP → ~0–5; PA → near 0 | **Ventilation stopped** → EtCO₂ → 0; SpO₂ pleth lost | **Hct drops** (e.g. 38% → 25–28%); cooling begins if planned | sinus → slow | Vasopressor to MAP 50–80; check SvO₂/DO₂i ([PMC9918189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9918189/), [rk.md summary](https://rk.md/2016/hypotension-initiation-cardiopulmonary-bypass/)) |
| **Cross-clamp + cardioplegia** | **0 (asystole)** in 30–60 s | Brief MAP dip as cardioplegia returns (uncertain) | — | — | **K⁺ rises** (to ~5–6, uncertain); HTK → Na⁺ ↓ | **flat line** | Start the ischaemia timer; plan re-dose (blood 20–30 min) |
| On-pump maintenance | — | MAP 50–80 (I A) | ~0 | — | ACT every ~20–30 min (uncertain), ABG alpha-stat, glucose ≤ 180, lactate < 3, UO ≥ 0.5 mL/kg/h | asystole | Titrate flow, FiO₂, sweep, vasoactives, heparin |
| **Rewarming** | — | MAP often falls (vasodilation) | — | — | ΔT ≤ 4 °C, ≤ 0.5 °C/min, outlet < 37 °C; BIS rises → awareness risk | — | Top up anesthesia; slow the rewarm |
| **Cross-clamp off (reperfusion)** | **VF in 10–80%**, or slow sinus/junctional/heart block | pulsatility returns as the heart ejects | — | — | K⁺ washout | **VF** → 10–20 J internal shocks | Defibrillate, amiodarone/lidocaine, pacing |
| **Wean / come off CPB** | 80–100 (pacing if needed) | pulsatile, MAP target ~65 (uncertain); inotropes if LV stunned | CVP/PA rise as the venous line is clamped and volume is given | **Ventilation resumed** (lungs re-expanded, FiO₂ 1.0) → EtCO₂ returns; SpO₂ returns | Core ≥ 36 °C (NP ≤ 37); K⁺ 4–5; Hb ~7.5–8 (uncertain) | sinus/paced | Checklist (I C), TOE ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)) |
| **Protamine** | ↑ or ↓ (bradycardia possible) | **Type I:** MAP ↓. **Type II:** MAP ↓↓ plus airway pressure ↑. **Type III:** MAP ↓↓↓. | **Type III: PA ↑↑, CVP ↑ (RV failure)** | SpO₂ ↓ in type II/III | ACT back to baseline | — | Slow or stop, vasopressors, iNO, re-heparinize and go back on pump ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) |
| **Bleeding** (surgical) | ↑ | ↓ (pulse pressure narrows) | ↓ | EtCO₂ ↓ with falling CO; SpO₂ late ↓ | Hb ↓ after fluids; lactate ↑ | sinus tachy → PEA | Volume/blood, surgical control. On CPB: **reservoir level falls** unless suckers return the blood. |
| **Vasoplegia** | ↑ | MAP < 50 despite adequate flow | ↓ | — | — | — | α1-agonist and/or vasopressin (I C), methylene blue (IIa) |
| Air embolism (coronary) | ↓ / VF | ↓ | ↑ | — | — | **ST elevation** (inferior if RCA, uncertain) | Raise perfusion pressure, de-air |
| Tamponade (post-closure) | ↑ | ↓, pulsus paradoxus | CVP ↑ (equalization) | — | — | low voltage | Re-open (Pulse has a pericardial-effusion action) |

---

## 4. Anesthesia (enough to drive the anesthesia/perfusion side)

### 4.1 Induction and maintenance

| Phase | Drug | Typical dose (adult) | Effect to simulate | Pulse has it? | Source |
|---|---|---|---|---|---|
| Premed / co-induction | Midazolam | 0.02–0.05 mg/kg (uncertain); benzodiazepine-free practice is growing (B-Free trial) | Sedation, mild BP ↓ | Yes | [B-Free JAMA Surg 2025, PMC11780505](https://pmc.ncbi.nlm.nih.gov/articles/PMC11780505/) |
| Opioid (balanced) | Fentanyl | **10–25 µg/kg** total (balanced). High-dose techniques used 50–100 µg/kg historically. | HR ↓, chest-wall rigidity, blunts the sternotomy response | Yes | [MGH Clinical Anesthesia Procedures](https://anesth.unboundmedicine.com/anesthesia/view/ClinicalAnesthesiaProcedures/728321/0/Anesthesia_for_Cardiac_Surgery___Induction) |
| Opioid | Sufentanil | 1–5 µg/kg (balanced); TCI (Gepts) Ce ~0.5 ng/mL | as above | **No** | [MGH](https://anesth.unboundmedicine.com/anesthesia/view/ClinicalAnesthesiaProcedures/728321/0/Anesthesia_for_Cardiac_Surgery___Induction), [OFACAR PMC13460324](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324) |
| Opioid | Remifentanil | infusion; reduce ~30% per 5 °C of cooling (Hofmann elimination) | — | **No** | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |
| Hypnotic | **Etomidate** | 0.25–0.35 mg/kg | Least myocardial depression; most stable hemodynamics after induction | Yes | [Erlangen analysis](https://link.springer.com/10.1186/cc13988), [Heliyon 2024 SR](https://doaj.org/article/1c3e7bda0b2a4008959842da2a93435e) |
| Hypnotic | Propofol | Titrated bolus (uncertain 0.5–1.5 mg/kg); TCI (Schnider) Ce 2–4 µg/mL | SVR ↓ and BP ↓ (dose-dependent) | Yes | [OFACAR](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324) |
| Adjunct | Ketamine | 0.5 mg/kg (opioid-free protocol) | HR/BP ↑ | Yes | [OFACAR](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324) |
| NMB | Rocuronium / cisatracurium | Rocuronium 0.6–0.9 mg/kg (RSI); cisatracurium 0.15 mg/kg | Paralysis; minimal CV effect | Roc yes / cis no | [Erlangen](https://link.springer.com/10.1186/cc13988), [OFACAR](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324) |
| Maintenance | Sevoflurane / isoflurane / desflurane | ~0.5–1 MAC. MAC at age 40: sevo 1.80% (Mapleson) or 2.03% (Cooter 2020); iso 1.17%; des 6.6%. **−6 to −6.5% per decade of age.** BIS 40–60. | SVR ↓, contractility ↓ (dose-dependent) | **Desflurane only** (via anesthesia machine) | [Cooter et al. BJA 2020, PMC7034808](https://pmc.ncbi.nlm.nih.gov/articles/PMC7034808) |
| On CPB | Volatile via the oxygenator sweep (approved vaporizer, I C; monitor oxygenator exhaust, IIa B), or propofol TIVA. IV anesthetics/opioids at least at the pre-CPB dose (IIa B). Polymethylpentene membranes pass little volatile → awareness risk. Opioid plasma levels fall ~50% when CPB starts (hemodilution). Fentanyl/sufentanil sequestered in the lungs are released at separation. N₂O around CPB is contraindicated (III B). | — | — | [2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) |

### 4.2 Vasopressors and inotropes

Infusion ranges from a 2026 open-access pharmacology table ([J Anesth Analg Crit Care 2026, PMC13689082](https://pmc.ncbi.nlm.nih.gov/articles/PMC13689082/)). Effect arrows are CO/CI, SVR, MAP and HR.

| Drug | Receptors | Infusion range | CO | SVR | MAP | HR | Pulse native? | Notes for the sim |
|---|---|---|---|---|---|---|---|---|
| **Norepinephrine** | α1 > β1 ≫ β2 | 0.01–0.3 µg/kg/min | ~/↑ | ↑↑ | ↑↑ | ~/↑ | Yes | First-line vasoconstrictor on and off pump |
| **Epinephrine** | β1 ≥ α ≥ β2 | 0.01–0.1 µg/kg/min (higher in rescue) | ↑↑ | ↑ | ↑↑ | ↑↑ | Yes | Inotrope for low-output syndrome; raises lactate and glucose (uncertain magnitude) |
| Dopamine | β1 ≈ α > β2, D1 | 5–20 µg/kg/min | ↑ | ↑ | ↑ | ↑↑ | No | Rarely first choice now |
| Phenylephrine | α1 | 0.5–5 µg/kg/min (boluses 50–200 µg common, uncertain) | ~ | ↑↑ | ↑↑ | ~ (reflex ↓) | Yes | Pure vasoconstrictor; the go-to bolus on CPB |
| **Dobutamine** | β1 > β2 | 2.5–20 µg/kg/min | ↑ | ~/↓ | ↑ | ↑ | **No** | Inotrope; tachycardia/arrhythmia risk |
| **Milrinone** | PDE-III inhibitor | 0.125–0.5 µg/kg/min per the table; product monograph: **50 µg/kg load over 10 min, then 0.375–0.75 µg/kg/min**. Half-life ~2.3 h, renal (80–90% unchanged). | ↑↑ | ↓↓ | ↓ | ↑ | **No** | Inodilator; lowers PVR (good for RV/PH); accumulates in renal failure ([monograph summary](https://www.unboundmedicine.com/harrietlane/view/Davis-Drug-Guide/51505/all/milrinone)) |
| **Vasopressin** | V1, V2 | 0.03–0.06 U/min (other sources 0.01–0.1) | ↓ | ↑↑ | ↑↑ | ~ | **No** | Vasoplegia; no V1 receptors in pulmonary vessels → PVR is spared |
| Levosimendan | Ca²⁺ sensitizer, K_ATP | 0.05–0.2 µg/kg/min | ↑↑ | ↓↓ | ↓ | ↑ | No | Long-acting metabolite |
| Isoproterenol | β1, β2 | 2–20 µg/min | ↑ | ~/↓ | ~ | ↑ | No | Bradycardia/heart block bridge |
| Angiotensin II | AT1 | 10–80 ng/kg/min | ↓ | ↑↑ | ↑↑ | ~ | No | Rescue for vasoplegia (IIb C) |

Also used (the game can include them): CaCl₂ (hypocalcaemia, protamine reaction); MgSO₄; amiodarone/lidocaine (reperfusion VF); nitroglycerin, sodium nitroprusside, nicardipine, clevidipine (vasodilators on CPB; the guideline gives no preference); insulin; NaHCO₃; antithrombin concentrate; TXA ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/), [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)).

**Scoring hook — Vasoactive-Inotropic Score (Gaies 2010):** VIS = dopamine + dobutamine + 100 × epinephrine + 100 × norepinephrine + 10 × milrinone + 10 000 × vasopressin (U/kg/min). Doses are in µg/kg/min ([medicalalgorithms summary](https://www.medicalalgorithms.com/vasoactive-inotropic-score-vis-of-gaies-et-al-for-neonates-and-infants-following-cardiopulmonary-bypass)). Use it as a "how sick / how well managed" metric after bypass.

### 4.3 Pharmacology model for the game

- Pulse PBPK covers about half the drug list, and its PD is admittedly coarse ([drugs methodology](https://pulse.kitware.com/_drugs_methodology.html)). **Recommendation:** a game-side PK/PD module for all titratable drugs: three-compartment mammillary model, effect site (ke0), sigmoid Emax. Its outputs drive Pulse's cardiovascular **modifier actions** (4.3+): heart elastance (contractility), systemic/pulmonary resistance, venous tone, and HR set-point.
- Published PK parameter sets to implement from the papers: Schnider/Marsh (propofol), Minto (remifentanil), Gepts (sufentanil) ([OFACAR used Schnider/Gepts](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324)). Bypass adjustments: add the prime volume to V1 when CPB starts (~50% concentration drop), scale clearance with temperature (remifentanil −30% per 5 °C), and release lung-sequestered opioid at separation ([2024 guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/)).

---

## 5. Recommended modelling approach

### 5.1 Decision

**Pulse 4.4.x as the patient core, plus custom game-side modules, gated by an early spike test.** If the spike fails, use the fallback: a custom 0-D model for the bypass phase.

Why:
1. Pulse gives validated, coupled cardiovascular, respiratory, gas-exchange, acid-base, PBPK, anesthesia-machine and hemorrhage physiology for free. It already has Unity and Unreal plugins, a permissive Apache-2.0 license, and speed headroom (10–15× real time lets us fast-forward through long waits).
2. Pulse 4.4's **VA-ECMO with right-atrium drainage and ascending-aorta return is topologically central CPB**. Its oxygenator diffusion model and sweep/FdO₂ controls give realistic PaO₂/PaCO₂ behaviour without extra work ([Pulse ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html)).
3. Everything specific to cardiac surgery is missing and has to be custom anyway, whichever engine we pick: cardioplegia, cross-clamp, ACT/heparin/protamine, heat exchanger and patient cooling, reservoir dynamics, AF/pacing/ST-segment ECG. No open engine has it (§1).
4. Every alternative is worse. CircAdapt is license-blocked, HumMod cannot be embedded, BioGears adds nothing over Pulse, and Explain is neonatal.

### 5.2 Architecture (proposed)

```
 Game engine (Unity or Unreal) — render @60–90 fps
 ├── SimulationHost (worker thread, fixed 0.02 s ticks, time-scale 1×–10×)
 │    ├── Pulse 4.4 patient (CV, resp, blood chem, PBPK, anesthesia machine, hemorrhage)
 │    ├── CPBModule (custom)      → drives Pulse ECMO (VA, RA→Ao): flow, sweep, FdO2, infuser
 │    │     reservoir volume/level, roller|centrifugal pump (H-Q curve), VAVD, suckers/vent returns,
 │    │     heat exchanger + 2-compartment patient thermal model, hemofilter, alarms, prime/hemodilution
 │    ├── MyocardiumModule (custom) cross-clamp, cardioplegia type/dose/temp/route, ischaemia clock,
 │    │     arrest/return of activity, stunning → Pulse heart-elastance modifier, reperfusion VF chance
 │    ├── CoagulationModule (custom) heparin PK, ACT, AT level, protamine, rebound, bleeding multiplier
 │    ├── PharmacologyModule (custom) PK/PD for drugs Pulse lacks → Pulse CV modifiers
 │    └── ScenarioDirector (data-driven JSON) complications: protamine type I–III, vasoplegia, AF,
 │          heart block, air embolism, oxygenator failure, line kink, pump/power failure, awareness
 └── MonitorSignals (custom) ECG synthesizer (rhythm state machine + morphology), ABP/CVP/PA waveform
       upsampling 50→250 Hz, pleth, capnogram, artefacts (diathermy, line flush, damping)
```

Notes:
- **Surgical bleeding round-trip.** A Pulse hemorrhage action is the blood leaving the vessels. The custom sucker returns that volume to the reservoir. The reservoir feeds back through the ECMO pump/infuser ("Blood" compound). This conserves mass, so the reservoir level is meaningful.
- **ECG.** Pulse's ECG is template playback with no AF or ST changes. Build our own: a rhythm state machine fed by sim HR/K⁺/ischaemia/temperature, with beat morphology either (a) re-implemented from McSharry's dynamical model (paper: IEEE TBME 2003; the reference code ECGSYN is **GPL-3.0**, so re-implement from the equations rather than linking it ([PhysioNet ECGSYN](https://physionet.org/content/ecgsyn/1.0.0/))), or (b) using templates from **PTB-XL (CC BY 4.0, attribution required; 21 799 ten-second 12-lead ECGs at 500 Hz, with ST/T-change and MI classes)** ([PhysioNet PTB-XL](https://physionet.org/content/ptb-xl/1.0.3/)). PTB-XL AF rhythm labels exist in its SCP statements (uncertain).
- **Waveform resolution.** At 50 Hz a beat at 72 bpm has about 41 samples. Upsample with cubic interpolation and add a synthetic dicrotic notch (Pulse has none) for display.
- **Pulse version lag.** Check whether the Unity C# / Unreal plugin builds expose the 4.4 ECMO API. If not, build the plugin from source (uncertain effort). Avoid IL2CPP-only targets, or patch for them.
- **Patient variety.** Pulse 4.2+ patient settings (sex, BMI, MAP, pulse pressure) and conditions (heart failure, anemia — not validated). Valve disease (AS/MR) is not modelled because Pulse valves are ideal; approximate it with custom resistance/regurgitant paths (uncertain feasibility inside Pulse's circuit).

### 5.3 Spike tests (do these first, ~1–2 weeks)

1. Pulse 4.4 VA-ECMO with RA→ascending-aorta cannulas at 4.5–5 L/min (2.4 L/min/m² × 1.9–2.0 m²). Set the ventilator off and the heart to **asystole** (or VF) for 60 simulated minutes. **Pass:** MAP 50–80 achievable with phenylephrine/norepinephrine; PaO₂ and PaCO₂ controllable by FdO₂ and sweep; lactate stable; no solver failure. **Fail:** asystole "suppresses hemodynamics" and ECMO flow does not perfuse. → Workaround to try: keep the Pulse heart beating at minimal elastance (via modifier) while the ECG layer shows asystole. If that fails too → fallback 5.4.
2. Hemodilution: infuse 1.5 L of saline prime through the ECMO bag at CPB start → Hct falls ~25–35% relative, MAP dips.
3. Weaning: ramp ECMO flow to 0 with the heart back in sinus and contractility reduced by 30% → CO, MAP, CVP and PA rise plausibly.
4. Performance: Pulse plus all modules at 10× time scale on the target PC (< 20% of one core at 1×, uncertain target).

### 5.4 Fallback: custom 0-D model

- Closed-loop lumped circuit. Time-varying elastance LV/RV (+ optional atria) with ventricular interaction ([Smith et al. 2004](https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml)). Three-element Windkessel for the systemic and pulmonary arterial trees ([Westerhof 2009](https://pubmed.ncbi.nlm.nih.gov/18543011/)). Venous capacitances with unstressed volumes. Diode valves with optional regurgitant/stenotic resistances. Baroreflex on HR, SVR, elastance and venous unstressed volume.
- CPB nodes: RA drain → reservoir → pump → oxygenator (O₂/CO₂ diffusion like Pulse's ECMO) → aorta. Simple lung, O₂ dissociation curve, Henderson–Hasselbalch acid-base, and a lactate generator when DO₂i < ~270–280 mL/min/m².
- RK4 at 1–5 ms. Cost per step is negligible. Tune all baselines to the Pulse and literature numbers in this document.
- License: our own code. Equations come from papers, so there are no license constraints.

### 5.5 Validation approach (for the "as close to real" goal)

- Write each table row in §2–§3 as an automated scenario assertion. Example: "on CPB start, MAP drops ≥ 15% within 60 s then recovers with 100 µg phenylephrine".
- Run Pulse's own validation scenarios after each engine upgrade.
- In-game "teaching mode" shows which guideline rule a player broke (e.g. ΔT > 10 °C, ACT < 480 s on pump, Hct < 18%, MAP < 50).
- A medical-accuracy review pass (plan Step 3) should check every "(uncertain)" item.

---

## 6. License summary for recommended items

| Item | License | Personal / non-commercial OK | Attribution | Share-alike |
|---|---|---|---|---|
| Pulse engine, Pulse Unity asset, Pulse Unreal plugin | Apache-2.0 | Yes (commercial too) | Keep LICENSE/NOTICE | No |
| BioGears | Apache-2.0 | Yes | Keep LICENSE/NOTICE | No |
| Physiolibrary (Modelica) ≥ 3.0.0 | BSD-3-Clause | Yes | Keep copyright notice | No |
| Explain engine | MIT | Yes | Keep copyright notice | No |
| ECMOjo | BSD (variant UNVERIFIED) | Yes | Keep notice | No |
| libOpenCOR / OpenCOR | Apache-2.0 / GPL-3.0 | Yes | Yes | OpenCOR: yes (GPL) if distributed |
| Physiome/CellML model files | UNVERIFIED (per model) | Probably | Probably | Unknown |
| Smith 2004 SBML in BioModels | CC0 (uncertain) | Yes | No | No |
| PTB-XL ECG dataset | CC BY 4.0 | Yes | **Yes** (cite Wagner et al.) | No |
| ECGSYN code | GPL-3.0 | Yes, but linking makes the game GPL if distributed → re-implement instead | Yes | Yes |
| HumMod | Custom: free for personal/educational/research; no engine modification; commercial needs approval | Yes (as a separate tool) | Not stated | n/a |
| CircAdapt | Custom academic license, revocable; "Academic Researchers" only | **No / unclear for a hobbyist** | — | — |

---

## 7. Open questions

1. Does Pulse 4.4 VA-ECMO still perfuse when the cardiac rhythm is asystole or VF (the Pulse docs say those states "suppress hemodynamics")? This decides 5.1 versus 5.4.
2. Do the Pulse Unity/Unreal packages expose the 4.4.0 ECMO and defibrillation APIs, or must we build them from source?
3. Which engine (Unity or Unreal) does the plan choose? The Unreal plugin is Win64-only, with marketplace builds up to UE 5.3. The Unity asset breaks with IL2CPP.
4. Exact protamine infusion-rate limit (label vs OpenAnesthesia), ACT baseline per device, del Nido re-dose interval, and the PaO₂ target on CPB: all marked uncertain.
5. Does PTB-XL include AF rhythm labels suitable for template extraction? Is CC BY attribution in the credits enough? (Yes, per the license.)
6. How deep should valve pathology go (AS, MR) when Pulse valves are ideal?
7. Is real-time fidelity enough at 50 Hz, or do we need a smaller Pulse step for waveform realism (CPU cost ×2–×4)?

---

## 8. Key sources

- Pulse: [home](https://pulse.kitware.com/), [versions](https://pulse.kitware.com/version.html), [cardiovascular](https://pulse.kitware.com/_cardiovascular_methodology.html), [drugs](https://pulse.kitware.com/_drugs_methodology.html), [anesthesia machine](https://pulse.kitware.com/_anesthesia_machine_methodology.html), [blood chemistry](https://pulse.kitware.com/_blood_chemistry_methodology.html), [ECMO](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html), [4.2 release](https://kitware.com/pulse-4-2-release), [Unity](https://www.kitware.com/pulse-is-now-available-on-the-unity-asset-store/), [Unreal](https://www.kitware.com/kitware-and-lumeto-develop-pulse-unreal-plugin-for-medical-simulation-and-training-on-unreal-engine/), [forum: performance](https://discourse.kitware.com/t/hummod-vs-biogears-vs-pulse/1547), [forum: step size](https://discourse.kitware.com/t/changing-step-size/1068)
- 2024 EACTS/EACTAIC/EBCP Guidelines on CPB in adult cardiac surgery: [EJCTS 2025;67(2):ezae354](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) and [BJA 2025 co-publication, PMC11947607](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) (full text read via the Europe PMC XML)
- STS/SCA/AmSECT temperature guideline 2015: [PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)
- MAP on CPB editorial: [PMC9918189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9918189/)
- Anticoagulation for CPB (BJA Education 2023): [PMC9947996](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996)
- Protamine reactions: [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)
- CPB components: [OpenAnesthesia](https://www.openanesthesia.org/keywords/cardiopulmonary-bypass-components-mechanisms-of-gas-exchange-priming-solutions-and-additives/)
- del Nido review: [PMC6066678](https://pmc.ncbi.nlm.nih.gov/articles/PMC6066678)
- GIFT trial: [NCT02250131](https://clinicaltrials.gov/study/NCT02250131)
- Hyperlactatemia: [PMC1794481](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1794481/), [PMC8767239](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8767239/)
- PA catheter normal values: [Bootsma et al. 2021, PMC7917533](https://pmc.ncbi.nlm.nih.gov/articles/PMC7917533)
- Vasoactive pharmacology table: [PMC13689082](https://pmc.ncbi.nlm.nih.gov/articles/PMC13689082/)
- MAC and age: [Cooter et al. BJA 2020, PMC7034808](https://pmc.ncbi.nlm.nih.gov/articles/PMC7034808)
- Cardiac anesthesia induction: [MGH Clinical Anesthesia Procedures](https://anesth.unboundmedicine.com/anesthesia/view/ClinicalAnesthesiaProcedures/728321/0/Anesthesia_for_Cardiac_Surgery___Induction), [OFACAR RCT, PMC13460324](https://pmc.ncbi.nlm.nih.gov/articles/PMC13460324)
- POAF: [PMC11784400](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11784400/)
- KDIGO AKI: [Merck table](https://www.merckmanuals.com/professional/multimedia/table/staging-criteria-for-acute-kidney-injury-kdigo-2012)
- PH definition: [PMC10971453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10971453/)
- Engines: [BioGears core](https://github.com/BioGearsEngine/core), [CircAdapt license](https://framework.circadapt.org/latest/license.html), [HumMod agreement](https://hummod.org/agreement), [Physiolibrary](https://www.github.com/modelica-3rdparty/Physiolibrary), [Explain](https://github.com/explain-labs), [ECMOjo](https://sourceforge.net/projects/ecmojo), [Westerhof Windkessel](https://pubmed.ncbi.nlm.nih.gov/18543011/), [Smith 2004 CellML](https://models.physiomeproject.org/workspace/smith_chase_nokes_shaw_wake_2004/file/f7b732c9707abdba5a55d471c49baf7dee92b036/smith_chase_nokes_shaw_wake_2004.cellml)
- ECG data/models: [PTB-XL](https://physionet.org/content/ptb-xl/1.0.3/), [ECGSYN](https://physionet.org/content/ecgsyn/1.0.0/)

Network note: `cvanes.stanford.edu` (Stanford CPB guide) could not be reached from this session (blocked host), so its numbers come only from search snippets and are marked uncertain.
