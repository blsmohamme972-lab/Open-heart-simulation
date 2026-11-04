# Evidence check 02: Physiology, anesthesia and perfusion

> Checked 2026-11-03 by an independent fact-checker (fresh searches). Counts: confirmed 12, corrected 5, refuted 0, unverified 0.
>
> Scope: the 12 claims flagged in `research/INDEX.md` (02.1-02.12), plus 5 extra statements from the report (02.X1-02.X5). Pages were opened and read (WebFetch, or curl + text extraction) unless marked "snippet". This is a check of the game design evidence. It is **not clinical guidance**.

## Verdict table

| ID | Claim (short) | Verdict | Correct value / note | Evidence [links] | Grade A/B/C |
|---|---|---|---|---|---|
| 02.1 | Pulse latest is 4.4.0 (Aug 2026) with a new ECMO VV/VA model; page title still says 4.3.0 | CORRECTED | 4.4.0 (August 2026) with a new ECMO device model (VV and VA) is confirmed. The page does **not** say 4.3.0 as a Pulse version: the HTML title is "Pulse Physiology Engine", the heading is "Version 4.4.0", and "4.3.0" is only in a `font-awesome-4.3.0` stylesheet path. GitLab tag not checkable (HTTP 403). | [Pulse versions](https://pulse.kitware.com/version.html); [Kitware webinar, 30 Sep 2026](https://www.kitware.com/webinars/whats-new-in-pulse/) | A (official) |
| 02.2 | Pulse Unity asset v4.3.1 (5 Feb 2025), free, Standard Unity Asset Store EULA | CONFIRMED | 4.3.1, "FREE", "Standard Unity Asset Store EULA". The listing showed the date as "Feb 6, 2025" (a one-day, probably time-zone difference). The engine code itself stays Apache-2.0. | [Unity Asset Store listing](https://assetstore.unity.com/packages/tools/integration/pulse-physiology-engine-139773); [Kitware 2019 announcement](https://www.kitware.com/pulse-is-now-available-on-the-unity-asset-store/) | A (official listing) |
| 02.3 | Pulse ECMO uses an ideal flow source; no anticoagulation, thrombosis or hemolysis; no CPB model | CONFIRMED | "uses an ideal flow source for the centrifugal pump"; "does not simulate anticoagulation requirements, circuit thrombosis, hemolysis, or other complications". No CPB model is listed in the 4.4.0 changes or the ECMO page. | [Pulse ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html); [Pulse versions](https://pulse.kitware.com/version.html) | A |
| 02.4 | CircAdapt has no verifiable license on its official pages | CORRECTED | A license page exists: a custom **End User License Agreement** (KTF B.V. for Maastricht University and Maastricht UMC+). The license is free, revocable, non-transferable and limited to "educational, non-commercial and research purposes". Licensees are defined as academic researchers (university staff or students). Developers may not distribute the framework or improvements without written permission. Improvements become the licensor's property. | [CircAdapt license page](https://framework.circadapt.org/latest/license.html) | A (official) |
| 02.5 | del Nido adult: 20 mL/kg, max 1000 mL > 50 kg, 1:4 blood:crystalloid at 4 °C, single dose up to about 90 min | CORRECTED (minor) | Dose, cap and ratio are confirmed. The temperature depends on the institution: 4 °C at Cleveland (Kim 2014), but **8-12 °C** in the original Boston Children's protocol. EACTS 2024: single dose "for up to 90 min of ischaemia". The original (paediatric) protocol rarely redoses (cross-clamp > 3 h or electrical activity). | [Matte & del Nido 2012, PMC4557532](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557532/); [EACTS 2024, PMC11947607](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/) | A |
| 02.6 | Custodiol HTK single dose 20-25 mL/kg over 6-8 min; protects up to 180 min | CORRECTED | UK SmPC (rev. 01/05/2024): perfusion 1 mL/min per g heart weight, about **1.5-2 L** in adults, over **6-8 min** ("should not be shorter under any circumstances"). Pressure 80-110 mmHg, then 40-60 mmHg after arrest. Temperature 6-10 °C. Repeat dose 1-2 min (200-400 mL). The SmPC states **no** cardioplegic protection time. 20-25 mL/kg appears in a manufacturer brochure (snippet only). 120-180 min appears only in manufacturer material. | [Custodiol UK SmPC](https://www.medicines.org.uk/emc/product/14445/smpc/print); [Perfusion.com HTK quick reference](https://perfusion.com/quick-reference-custodiol-cardioplegia/); [PMC8384279](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8384279/) | A (label) / C (brochure) |
| 02.7 | STS/SCA/AmSECT: outlet ≥ 30 °C → gradient ≤ 4 °C and rewarming ≤ 0.5 °C/min (IIa, B); outlet < 37 °C | CONFIRMED | Exact wording in the Ann Thorac Surg version: "temperature gradient ... of ≤4°C (Class IIa, Level B)"; "rewarming rate ≤0.5°C/min (Class IIa, Level B)"; "<37°C" (Class I, Level C); ≤ 10 °C gradient when cooling or rewarming (Class I, Level C). | [Engelman 2015, Ann Thorac Surg 100:748-57 (STS PDF)](https://www.sts.org/sites/default/files/documents/Guidelines_CPB%20Temperature%20Management.pdf) | A |
| 02.8 | EACTS 2024 protamine:heparin ratio < 1.0 (I, B); STS 2018 < 2.6 mg per 100 IU | CONFIRMED | EACTS 2024 Recommendation Table 38: "A protamine-to-heparin ratio < 1.0 is recommended" (I, B). STS 2018: "reasonable to limit the ratio of protamine/heparin to less than 2.6 mg protamine/100 Units of heparin" (IIa, C). The two rules do not conflict. The EACTS ratio is in the usual 1 mg per 100 IU convention (interpretation). | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [STS 2018, PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/); [GuidelineCentral summary](https://guidelinecentral.com/guideline/19856) | A |
| 02.9 | ACT > 480 s reasonable (> 400 s with maximal-activation/microcuvette devices); heparin bolus 300-400 IU/kg | CONFIRMED | STS 2018: ACT > 480 s (IIa, C). For maximal-activation or microcuvette instruments, "values above 400 seconds are frequently considered therapeutic". STS gives weight-based dosing as IIa, C, with 300 IU/kg only as an example. 300-400 IU/kg is the usual practice range (JECT 1996; European survey: 300 IU/kg most common). | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/); [GuidelineCentral](https://guidelinecentral.com/guideline/19856); [JECT 1996](https://ject.edpsciences.org/articles/ject/pdf/1996/02/ject1996282p67.pdf) (snippet) | A |
| 02.10 | EACTS 2024: MAP 50-80 mmHg (I, A); minimum DO2 280 mL/min/m² (I, A); flow 2.2-2.8 L/min/m² | CONFIRMED | Table 40: "MAP be maintained between 50 and 80 mmHg" (I, A); pressors above 80 mmHg "not recommended" (III, B). Table 41: "minimal value of DO2 of 280 ml/min/m2" (I, A). The flow range 2.2-2.8 L/min/m² is narrative text ("most perfusionists usually set"), not a graded recommendation. | [EACTS 2024 full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/); [EJCTS record, doi 10.1093/ejcts/ezae354](https://opinvisindi.is/items/566b3da2-831f-497e-a6a4-c20235a84617) | A |
| 02.11 | CALS-ANZ: internal 20 J, up to 3 stacked shocks, re-sternotomy within 5 min, adrenaline 50-100 µg not 1 mg | CONFIRMED | CALS-ANZ text confirms all four items, plus the 10-day window and DOO pacing. An erratum corrected the dose unit from "50-100 mg" to **50-100 µg**. STS 2017 (independent): three sequential shocks before compressions, resternotomy within 5 min, no routine full-dose epinephrine ("smaller doses (eg, 50 to 300 µg boluses)"). ERC 2021 also gives up to three shocks and resternotomy within 5 min. The 20 J energy is stated only in CALS-ANZ. | [CALS-ANZ, PMC10692601](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/); [erratum, PMC10692630](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692630/); [STS 2017 consensus PDF](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf); [ERC 2021, PMC8190767](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767/) | A |
| 02.12 | Heparin half-life about 30 / 60 / 150 min at 25 / 100 / 400 IU/kg | CONFIRMED | ACCP 9th ed. (Chest 2012): "increases from approximately 30 min after an IV bolus of 25 units/kg, to 60 min with an IV bolus of 100 units/kg, to 150 min with a bolus of 400 units/kg". | [Garcia et al., Chest 2012, PMC3278070](https://pmc.ncbi.nlm.nih.gov/articles/PMC3278070/) | A |
| 02.X1 | Protamine: "Give no faster than 20 mg/min" | CORRECTED | The label limit is "not to exceed 50 mg of protamine sulfate in any 10-minute period" (about 5 mg/min). 20 mg/min is an OpenAnesthesia teaching value ("no more than 20 mg per minute or 10-15 minutes for the entire dose"). | [Health Canada protamine monograph](https://pdf.hres.ca/dpd_pm/00083834.PDF); [NZ Medsafe datasheet](https://medsafe.govt.nz/profs/Datasheet/p/Protaminesulphateinj.pdf); [OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/) | A (labels) |
| 02.X2 | Eleveld 2018 propofol reference parameters (snippet-only in report) | CONFIRMED | PubMed abstract: "A 35-yr-old, 170 cm, 70 kg male (without concomitant anaesthetic drugs) has a V1, V2, V3, CL, Q2, Q3, and ke0 of 6.28, 25.5, 273 litres, 1.79, 1.75, 1.11 litres min-1, and 0.146 min-1". Note: these values assume no concomitant drugs; an erratum exists (BJA 2018;121:519). | [PubMed 29661412](https://pubmed.ncbi.nlm.nih.gov/29661412/) (via NCBI E-utilities) | A |
| 02.X3 | CaO2 = 1.34 × Hb × SaO2 + 0.003 × PaO2 (constants marked unverified) | CONFIRMED | BJA Education 2020: 1.34 is "Hüfner's constant" (mL/g); solubility 0.023 mL/dL/kPa, which equals about 0.003 mL/dL/mmHg (0.023 / 7.5). The report's two DO2i examples (307 and 259) recompute correctly. | [Kane et al., BJA Educ 2020, PMC7807956](https://pmc.ncbi.nlm.nih.gov/articles/PMC7807956/) | A |
| 02.X4 | ECGSYN and OpenCOR are GPL-3.0 | CONFIRMED | PhysioNet ECGSYN: "GNU General Public License version 3", v1.0.0, 3 Dec 2003. OpenCOR `LICENSE.txt`: "GNU GENERAL PUBLIC LICENSE Version 3". | [PhysioNet ECGSYN](https://physionet.org/content/ecgsyn/); [OpenCOR LICENSE.txt](https://raw.githubusercontent.com/opencor/opencor/master/LICENSE.txt) | A |
| 02.X5 | Arrest lidocaine 1-1.5 then 0.5-0.75 mg/kg; amiodarone 300 then 150 mg (AHA PDF returned 403 for the report) | CONFIRMED | AHA 2025 ACLS posters (© 2025 AHA, JN-2788): "Amiodarone IV/IO dose: First dose: 300 mg bolus. Second dose: 150 mg"; "Lidocaine IV/IO dose: First dose: 1-1.5 mg/kg. Second dose: 0.5-0.75 mg/kg". | [AHA 2025 ACLS posters (Irish Heart Foundation copy)](https://irishheart.ie/wp-content/uploads/2026/02/JN-2788_ACLS-Posters-International-English.pdf) | A |

## Details

### 02-1
Pulse version page (read with curl): HTML `<title>` = "Pulse Physiology Engine", page heading "Version 4.4.0", list entries "Pulse v4.4.0 (August 2026)", "Pulse v4.3.1 (January 2025)", "Pulse v4.3.0 (September 2024)". The only "4.3.0" strings besides the history entry are in `font-awesome-4.3.0/css/font-awesome.min.css` on this page and on `_docs.html`. 4.4.0 notes: "Added a new Extracorporeal Membrane Oxygenation (ECMO) device model to replace the previous functionality". The model supports venovenous and venoarterial cannulation. An independent Kitware page announces a webinar on "What's New in the Pulse Physiology Engine 4.4.0" (30 Sep 2026) that lists "Addition of an ECMO model". The GitLab tags and releases pages returned HTTP 403, so the git tag itself is not confirmed.

### 02-2
Unity Asset Store listing (read 2026-11-03): latest version "4.3.1", "Feb 6, 2025", "FREE", "Standard Unity Asset Store EULA". The one-day difference from the report (5 Feb) is treated as rounding. The Kitware 2019 announcement confirms the asset is free and links to the open-source GitLab project. The engine itself is Apache-2.0, but the Asset Store package is distributed under the Store EULA.

### 02-3
The Pulse ECMO methodology page says: "The current ECMO implementation uses an ideal flow source for the centrifugal pump". It also says the model "does not simulate anticoagulation requirements, circuit thrombosis, hemolysis, or other complications", and lists these as future work. The page does not mention cardiopulmonary bypass, and the 4.4.0 change list has no CPB item. A Kitware search summary notes that the earlier 4.2 "ECMO" support was explicitly "NOT A MODEL" (snippet).

### 02-4
`framework.circadapt.org/latest/license.html` (linked as "License" in the documentation navigation) is the "END USER LICENSE AGREEMENT TO THE CIRCADAPT FRAMEWORK" between You and "KTF B.V. on behalf of Maastricht University ... and academisch ziekenhuis Maastricht". Grant: "a free, revocable, non-exclusive, non-transferable, non-sublicensable License ... for educational, non-commercial and research purposes within the Licensed Field". "User" and "Developer User" are defined as an "Academic Researcher", meaning a university employee or a student. Developers may not "distribute or sell ... any Improvements ... without proper acknowledgement and prior written permission of Licensor". "Any Improvements shall be the property of Licensor". The licensor may terminate "at any time, with or without cause". **Consequence for the plan:** a hobby game developer who is not an academic researcher is probably outside the license, and shipping CircAdapt code is not allowed. Keep CircAdapt out of the build and use it only as published literature.

### 02-5
Matte & del Nido, JECT 2012;44:98-103 (PMC4557532) says del Nido is "generally given as a single 20-mL/kg dose" (10 mL/kg if the cross-clamp time is under 30 min). The arresting dose is capped at 1 L for patients over 50 kg. The mix is four parts crystalloid to one part blood, delivered at **8-12 °C**. Redosing is not normally given, except for electrical activity or cross-clamp times over 3 hours. EACTS 2024 (text, ref. 329 = D'Angelo 2022): "It can be administered as a single dose for up to 90 min of ischaemia". The 4 °C value comes from the Cleveland protocol (Kim 2014). The report row is labelled "Cleveland", so the correction only adds the range.

### 02-6
UK SmPC (Custodiol, date of revision 01/05/2024), section 4.2A:
- "The perfusion rate is 1 ml/minute/gram heart weight ... leading to a total volume of Custodiol between 1.5 and 2 litres."
- "Temperature of the solution 6° C – 10° C".
- Pressure "initially ... 80 to 110 mmHg", then "40 – 60 mmHg" after arrest.
- "the perfusion time must be 6 – 8 minutes ... should not be shorter under any circumstances."
- Additional perfusion: "1 – 2 minutes (equivalent to 200 – 400 ml)".
- "a positive benefit/risk ratio for the use of Custodiol in short surgery procedures (<90 minutes) has not been confirmed yet".

The SmPC gives no cardioplegic protection time. Its only duration is "up to five hours" for cold storage of a heart for transplant. 20-25 mL/kg over 6-8 min at 40-60 mmHg comes from a manufacturer brochure (search snippet only; the PDF could not be extracted). A perfusion quick reference redoses "10ml/kg ... before 120 minutes of myocardial ischaemia". A propensity-matched study (PMC8384279) of cross-clamp ≥ 120 min found a trend to worse outcomes with single-dose HTK than with multidose cold blood. **Game use:** model HTK as a 6-8 min infusion of about 20-25 mL/kg, with a redose option around 90-120 min. Do not grant 180 min of free protection.

### 02-7
The STS-hosted PDF of Engelman et al., Ann Thorac Surg 2015;100:748-57 (co-published in JECT 47:145-54 and JCVA 29:1104-13) gives these recommendations:
- "Surgical teams should limit arterial outlet blood temperature to <37°C" (Class I, Level C).
- Cooling and rewarming gradients "should not exceed 10°C" (Class I, Level C).
- When outlet ≥ 30 °C, a gradient "of ≤4°C" and a "rewarming rate ≤0.5°C/min" (both Class IIa, Level B).
- When outlet < 30 °C, a "maximal gradient of 10°C" (IIa, C).

All values match the report.

### 02-8
EACTS 2024 Recommendation Table 38 says "A protamine-to-heparin ratio < 1.0 is recommended to avoid overdosing of protamine" (Class I, Level B, refs 489, 492). The text adds that the exact ratio and monitoring method "remain to be determined". The STS 2018 page (read via WebFetch) says "It is reasonable to limit the ratio of protamine/heparin to less than 2.6 mg protamine/100 Units of heparin" (Class IIa, Level C). It also gives a low-dose protamine infusion "(25 mg/h) for up to 6 hours" (IIb, C) and titration to residual heparin (IIa, B). GuidelineCentral reproduces the 2.6 mg/100 U text independently.

### 02-9
STS 2018: "It is reasonable to maintain activated clotting time above 480 seconds during CPB" (IIa, C). The threshold is approximate and instrument-dependent: for maximal-activation or microcuvette devices, "values above 400 seconds are frequently considered therapeutic". Weight-based bolus dosing is "reasonable" (IIa, C). STS gives no fixed dose range; 300 IU/kg appears as an example. Independent practice sources (snippets) confirm the 300-400 IU/kg range: a 1996 JECT paper ("ACT above 480 seconds ... loading dose of 300-400 units/kg") and a European survey (300 IU/kg most common, ACT targets 400-480 s). The verdict stays CONFIRMED because the guideline values were read in full.

### 02-10
EACTS 2024 full text (PMC copy of BJA 2025;134:917-1008; also EJCTS 67(2):ezae354) has two relevant tables:
- Table 40: "It is recommended that the MAP be maintained between 50 and 80 mmHg ..." (I, A); "The use of vasopressors to increase the MAP to values above 80 mmHg during CPB is not recommended" (III, B).
- Table 41: "It is recommended that a minimal value of DO2 of 280 ml/min/m2 be used to reduce the risk of AKI stage 1" (I, A).

The flow statement is narrative text: "most perfusionists usually set the pump flow rate between 2.2 and 2.8 L/min/m2". It is not a graded recommendation.

### 02-11
CALS-ANZ (Karcher et al., Crit Care Resusc 2022;24:218-23):
- Shocks: "up to three stacked shocks are delivered".
- Internal shocks: "defibrillated with 20 joules using internal defibrillator pads".
- Resternotomy: "Chest reopening should be completed within 5 minutes", for patients "within 10 days of their last operation".
- Compressions: external massage "may be delayed by up to 60 seconds".
- Pacing: DOO mode.
- Adrenaline: "only small doses of adrenaline (eg, 50–100 micrograms i.v.)". The erratum (PMC10692630) fixes a printed "50-100 mg" to 50-100 µg.

Independent sources:
- STS 2017 expert consensus (Ann Thorac Surg 2017;103:1005-20): "three sequential attempts at defibrillation before external cardiac massage", resternotomy within 5 minutes, and "full doses of epinephrine should not be routinely given". Epinephrine "may also be safely used in smaller doses (eg, 50 to 300 µg boluses)".
- ERC 2021 (German edition): "bis zu drei aufeinanderfolgende Schocks (< 1 min)" and "Resternotomie (< 5 min)".

No independent guideline gave a joule value, but a 202-patient study (snippet) found 10-20 J optimal for open-chest defibrillation.

### 02-12
ACCP Antithrombotic Therapy 9th ed., "Parenteral Anticoagulants" (Garcia, Baglin, Weitz, Samama; Chest 2012;141(2 Suppl):e24S-e43S): "the apparent biologic half-life of heparin increases from approximately 30 min after an IV bolus of 25 units/kg, to 60 min with an IV bolus of 100 units/kg, to 150 min with a bolus of 400 units/kg". This replaces the report's secondary, snippet-only source (The Blood Project) with an A-grade one. One secondary site gives 180 min at 400 U/kg, so treat 150 min as the reference value.

### 02-X1
Report §2.7: "Give no faster than 20 mg/min".
- Health Canada product monograph: "Protamine Sulfate Injection USP should be given by very slow intravenous injection in doses not to exceed 50 mg of protamine sulfate in any 10-minute period". It also warns: "Too rapid administration ... can cause severe hypotensive and anaphylactoid reactions".
- NZ Medsafe datasheet: "slow intravenous injection over a period of about 10 minutes. No more than 50mg ... in any one dose".
- OpenAnesthesia's "no more than 20 mg per minute or 10-15 minutes for the entire dose" is a practice teaching value, four times the label rate.

Game hook #7 ("Rate > 20 mg/min raises type I risk", design) can keep 20 mg/min as a gameplay threshold, but it should say the label limit is 5 mg/min.

### 02-X2
NCBI E-utilities abstract of Eleveld et al., Br J Anaesth 2018;120(5):942-959 confirms all seven parameter values for "a 35-yr-old, 170 cm, 70 kg male (without concomitant anaesthetic drugs)". The values match the report exactly. Note the "without concomitant anaesthetic drugs" condition and the erratum in Br J Anaesth 2018;121(2):519. The covariate equations still need the full paper.

### 02-X3
Kane, Kothmann & Giussani, "Detection and response to acute systemic hypoxia", BJA Education 2020 (PMC7807956), gives DO2 = (SaO2/100 × [Hb] × 1.34 + PaO2 × 0.023) × flow. In that formula, "0.023 is the solubility of oxygen (in ml dl−1 kPa−1); 1.34 is Hüfner's constant". Converting to mmHg (1 kPa = 7.5 mmHg) gives 0.0031, about 0.003 mL/dL/mmHg. Recomputed examples: 1.34 × 9 + 0.003 × 250 = 12.81 mL/dL → DO2i = 2.4 × 12.81 × 10 = 307. With Hb 7.5 → 10.80 → 259. Both match the report.

### 02-X4
PhysioNet ECGSYN page: "License (for files): GNU General Public License version 3", version 1.0.0, published 3 Dec 2003. OpenCOR repository `LICENSE.txt` (raw GitHub) begins "GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007". Open Hub also lists OpenCOR as GPL-3.0. A 2015 paper said Apache-2.0, which reflects an older state of the project. Both report statements are correct.

### 02-X5
The AHA 2025 ACLS poster set (JN-2788, "© 2025 American Heart Association", international English edition hosted by the Irish Heart Foundation) was read as PDF text. Cardiac arrest drug box: "Amiodarone IV/IO dose: First dose: 300 mg bolus. Second dose: 150 mg"; "Lidocaine IV/IO dose: First dose: 1-1.5 mg/kg. Second dose: 0.5-0.75 mg/kg"; "Epinephrine every 3-5 min". This replaces the report's snippet-only AHA citation. CALS still overrides the epinephrine dose after cardiac surgery (02-11).

## Resolved open questions

1. **CircAdapt license (report open question 1):** Resolved. The license is a custom academic, non-commercial EULA held by KTF B.V. for Maastricht University and Maastricht UMC+, and it is revocable at will ([license page](https://framework.circadapt.org/latest/license.html)). It is not usable in a distributed game, and a non-academic hobby developer is probably not an eligible licensee. The HumMod license is still unverified.
2. **HTK dose and 180-min claim (open question 2):** Partly resolved. The current label (UK SmPC, rev. 05/2024) gives a 6-8 min perfusion of about 1.5-2 L (1 mL/min/g heart weight). It states no cardioplegic protection time, and it says benefit/risk for procedures under 90 min is not confirmed. 180 min is a brochure claim only. Peer-reviewed data (PMC8384279) show a trend to worse outcomes with single-dose HTK when cross-clamp ≥ 120 min ([SmPC](https://www.medicines.org.uk/emc/product/14445/smpc/print)).
3. **Pulse 4.3.0 vs 4.4.0 labelling (INDEX open question):** Resolved. The page title and heading do not say 4.3.0; that string is a Font Awesome stylesheet version. 4.4.0 (August 2026) is also announced by Kitware's webinar page dated 30 Sep 2026. The GitLab tag could not be checked (HTTP 403), so pin by commit hash or release archive when downloading.
4. **LCOS and NIRS wording in EACTS 2024 (open question 6):** The printed wording is confirmed exactly: "Low cardiac output syndrome is arbitrarily defined as a cardiac index of 2.4 L·min−1·m−2 with evidence of end-organ dysfunction" (no inequality sign). NIRS is printed as "intra- and perioperative decrements (e.g. rScO2 below 15% of baseline)". Independent literature reports CI thresholds of < 2.0-2.5 L/min/m² for LCOS, with no uniform definition ([Schoonen 2022, PMC9558721](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9558721/)). Cerebral desaturation is "often defined as a 20% relative decrease from baseline or an absolute rSO2 value of 50%" ([BMC Anesthesiol 2016](https://bmcanesthesiol.biomedcentral.com/track/pdf/10.1186/s12871-016-0298-7), snippet). For the game: LCOS = CI < 2.2-2.4 plus organ dysfunction; NIRS alarm = relative fall > 15-20% or absolute < 50%. This is an inference: the EACTS phrase is read as a relative fall.

The AHA lidocaine and amiodarone doses (part of open question 7) are also now confirmed: see 02-X5.

## Edits made to the report

All edits are in `research/02-physiology-anesthesia-perfusion.md`.

1. **§0 Summary, "Cardioplegia options" row**
   - Old: "HTK (single dose 20-25 mL/kg, uncertain up to 180 min)."
   - New: "HTK (single dose perfused over 6-8 min, about 1.5-2 L in adults per the UK SmPC; manufacturer brochure 20-25 mL/kg; the label states no protection time, and 120-180 min appears only in manufacturer material) [Step 2 check: corrected, ...#02-6]."
2. **§1.1 table, CircAdapt row, license cell**
   - Old: "**UNVERIFIED.** No license text was found on circadapt.org or the install page."
   - New: "**Custom EULA** (KTF B.V. for Maastricht University and Maastricht UMC+): free, revocable, for educational, non-commercial and research use by academic researchers only; no distribution of the framework or improvements without written permission (license page). [Step 2 check: corrected, ...#02-4]"
3. **§1.1 table, CircAdapt row, "Personal use?" cell**
   - Old: "Probably (uncertain)".
   - New: "Only for academic researchers, non-commercial (EULA)".
4. **§2.7 table, "Protamine reactions" row**
   - Old: "Give no faster than 20 mg/min."
   - New: "Give slowly: the protamine label limit is ≤ 50 mg in any 10-min period (about 5 mg/min); OpenAnesthesia gives ≤ 20 mg/min or the whole dose over 10-15 min [Step 2 check: corrected, ...#02-x1]."
5. **§2.8 table, del Nido row, temperature cell**
   - Old: "4 °C".
   - New: "4 °C at Cleveland; Boston Children's (original protocol) delivers at 8-12 °C [Step 2 check: corrected, ...#02-5]".
6. **§2.8 table, Custodiol HTK row, dose, temperature and duration cells**
   - Old: "Single antegrade dose **20-25 mL/kg over 6-8 min** at 40-60 mmHg root pressure (manufacturer). One trial: about 1-2 L. | Cold | Up to **180 min** claimed by the manufacturer (uncertain)."
   - New: SmPC values (6-8 min, never shorter; 1 mL/min/g; about 1.5-2 L; 80-110 then 40-60 mmHg; brochure 20-25 mL/kg; repeat dose 1-2 min, 200-400 mL), "Cold (SmPC: 6-10 °C)", and "The SmPC states **no** cardioplegic protection time ...; 120-180 min appears only in manufacturer brochures; one perfusion protocol redoses 10 mL/kg before 120 min [Step 2 check: corrected, ...#02-6]."
7. **Key claims #2**
   - Old: "(the page title says 4.3.0, an inconsistency)".
   - New: "(the page heading reads "Version 4.4.0"; the "4.3.0" string on the page is only a Font Awesome 4.3.0 stylesheet path, not a Pulse version) [Step 2 check: corrected, ...#02-1]".
8. **Key claims #10**
   - Old: "CircAdapt license could not be verified | installation.html | A (absence)".
   - New: "CircAdapt is under a custom EULA: free, revocable, educational/non-commercial/research use by academic researchers only [Step 2 check: corrected, ...#02-4] | license.html | A".
9. **Key claims #20**
   - Old: "..., 4 °C, ...".
   - New: "..., 4 °C at Cleveland (8-12 °C at Boston Children's), ... [Step 2 check: corrected, ...#02-5]".
10. **Key claims #23**
    - Old: "HTK single dose 20-25 mL/kg over 6-8 min; protection claimed up to 180 min | NCT01681095 | C".
    - New: "HTK single dose perfused over 6-8 min, about 1.5-2 L in adults (UK SmPC; brochure: 20-25 mL/kg); the label gives no cardioplegic protection time, and 120-180 min is a manufacturer-brochure claim only [Step 2 check: corrected, ...#02-6] | SmPC URL | A".
11. **Summary → Open questions, CircAdapt/HumMod bullet**
    - Old: "CircAdapt and HumMod licenses are unverified. Ask the authors before using them."
    - New: "CircAdapt is under a custom academic, non-commercial EULA [Step 2 check: corrected, ...#02-4]. The HumMod license is unverified. Ask the authors before using it."
12. **Summary → Open questions, HTK bullet**
    - Added: "The UK SmPC (rev. 05/2024) gives a 6-8 min perfusion of about 1.5-2 L and no protection time [Step 2 check: corrected, ...#02-6]."

No "(unverified in Step 2)" markers were needed, because no item stayed UNVERIFIED. No other file was changed.

## Sources

1. Pulse Physiology Engine, version history (read 2026-11-03): https://pulse.kitware.com/version.html
2. Kitware webinar "What's New in the Pulse Physiology Engine 4.4.0" (30 Sep 2026): https://www.kitware.com/webinars/whats-new-in-pulse/
3. Pulse ECMO methodology: https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html
4. Unity Asset Store, Pulse Physiology Engine listing: https://assetstore.unity.com/packages/tools/integration/pulse-physiology-engine-139773
5. Kitware, "Pulse Is Now Available on the Unity Asset Store" (28 Feb 2019): https://www.kitware.com/pulse-is-now-available-on-the-unity-asset-store/
6. CircAdapt Framework End User License Agreement: https://framework.circadapt.org/latest/license.html
7. Matte GS, del Nido PJ. History and use of del Nido cardioplegia solution at Boston Children's Hospital. J Extra Corpor Technol 2012;44:98-103: https://pmc.ncbi.nlm.nih.gov/articles/PMC4557532/
8. Wahba A et al. 2024 EACTS/EACTAIC/EBCP Guidelines on CPB in adult cardiac surgery (BJA 2025;134:917-1008; EJCTS 67(2):ezae354): https://pmc.ncbi.nlm.nih.gov/articles/PMC11947607/
9. Custodiol UK Summary of Product Characteristics (rev. 01/05/2024): https://www.medicines.org.uk/emc/product/14445/smpc/print
10. Perfusion.com, Quick reference: Custodiol cardioplegia: https://perfusion.com/quick-reference-custodiol-cardioplegia/
11. Custodiol-HTK vs cold blood cardioplegia with prolonged cross-clamp (propensity-matched, Arq Bras Cardiol 2020): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8384279/
12. Engelman R et al. STS/SCA/AmSECT temperature management during CPB. Ann Thorac Surg 2015;100:748-57 (STS PDF): https://www.sts.org/sites/default/files/documents/Guidelines_CPB%20Temperature%20Management.pdf
13. Shore-Lesserson L et al. STS/SCA/AmSECT anticoagulation during CPB (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589/
14. GuidelineCentral, Anticoagulation During Cardiopulmonary Bypass: https://guidelinecentral.com/guideline/19856
15. JECT 1996 heparin/ACT paper (snippet): https://ject.edpsciences.org/articles/ject/pdf/1996/02/ject1996282p67.pdf
16. Karcher C et al. CALS-ANZ. Crit Care Resusc 2022;24:218-23: https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/
17. CALS-ANZ erratum (adrenaline unit): https://pmc.ncbi.nlm.nih.gov/articles/PMC10692630/
18. STS Expert Consensus for the Resuscitation of Patients Who Arrest After Cardiac Surgery. Ann Thorac Surg 2017;103:1005-20: https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf
19. ERC Guidelines 2021, Cardiac arrest under special circumstances (German edition, Notfall Rett Med 2021;24:447-523): https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767/
20. Garcia DA et al. Parenteral anticoagulants, ACCP 9th ed. Chest 2012;141(2 Suppl):e24S-e43S: https://pmc.ncbi.nlm.nih.gov/articles/PMC3278070/
21. Health Canada, Protamine Sulfate Injection USP product monograph: https://pdf.hres.ca/dpd_pm/00083834.PDF
22. Medsafe NZ, Protamine sulphate injection datasheet: https://medsafe.govt.nz/profs/Datasheet/p/Protaminesulphateinj.pdf
23. OpenAnesthesia, Protamine reactions: https://www.openanesthesia.org/keywords/protamine-reactions/
24. Eleveld DJ et al. PK-PD model for propofol. Br J Anaesth 2018;120:942-959 (PubMed): https://pubmed.ncbi.nlm.nih.gov/29661412/
25. Kane AD, Kothmann E, Giussani DA. Detection and response to acute systemic hypoxia. BJA Education 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7807956/
26. PhysioNet ECGSYN: https://physionet.org/content/ecgsyn/
27. OpenCOR LICENSE.txt: https://raw.githubusercontent.com/opencor/opencor/master/LICENSE.txt
28. AHA 2025 ACLS posters (JN-2788): https://irishheart.ie/wp-content/uploads/2026/02/JN-2788_ACLS-Posters-International-English.pdf
29. Schoonen A et al. Definitions of low cardiac output syndrome after cardiac surgery. Front Cardiovasc Med 2022: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9558721/
30. Cerebral oximeter comparison, BMC Anesthesiology 2016 (snippet): https://bmcanesthesiol.biomedcentral.com/track/pdf/10.1186/s12871-016-0298-7
