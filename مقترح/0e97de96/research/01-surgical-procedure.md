# Research 01: The real open heart operation, step by step

> **Purpose.** This report describes how a real open heart operation is done, step by step, so that the game can copy it as closely as possible. It covers which operation to build first, the full ordered step list for that operation, who does each step, instruments and sutures, numbers (doses, pressures, flows, times), the words people say in the room, and what changes for valve operations.
>
> **Researched 2026-11-03 (re-do, fresh searches).** All facts below come from searches and page reads done on this date. Older plan files in the repository were not read.
>
> **Disclaimer.** This is research for a personal, non-commercial, educational game. It is **not clinical guidance**, not a training standard and not a medical device specification. Real practice varies by hospital, surgeon and patient. Numbers are given so the game can feel real, not so anyone can treat a patient.

**Abbreviations used (defined once):** CABG = coronary artery bypass grafting. CPB = cardiopulmonary bypass (the heart-lung machine). OPCAB = off-pump CABG (no heart-lung machine). SAVR = surgical aortic valve replacement. MV = mitral valve. LIMA / LITA = left internal mammary (thoracic) artery. RIMA = right internal mammary artery. ITA = internal thoracic artery. LAD = left anterior descending coronary artery. RCA = right coronary artery. OM = obtuse marginal branch. PDA = posterior descending artery. SVG = saphenous vein graft. RA = radial artery. EVH = endoscopic vein harvest. TEE / TOE = transesophageal echocardiography. PA catheter / PAC = pulmonary artery (Swan-Ganz) catheter. ACT = activated clotting time. MAP = mean arterial pressure. Hb = haemoglobin. HCT = haematocrit. DO2 = oxygen delivery. TTFM = transit-time flow measurement. PI = pulsatility index. DF = diastolic filling. VF = ventricular fibrillation. STS = Society of Thoracic Surgeons. EACTS = European Association for Cardio-Thoracic Surgery. EACTAIC = European Association of Cardiothoracic Anaesthesiology and Intensive Care. EBCP = European Board of Cardiovascular Perfusion. SCA = Society of Cardiovascular Anesthesiologists. AmSECT = American Society of ExtraCorporeal Technology. ACC/AHA = American College of Cardiology / American Heart Association. ESC = European Society of Cardiology. WHO = World Health Organization. OR = operating room. ICU = intensive care unit.

**Evidence grades:** A = primary/authoritative (guideline, peer-reviewed paper, official document). B = reputable secondary (society education page, review summary, major vendor page). C = weak (blog, forum, sample note, search snippet).

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence [links] |
|---|---|---|
| Primary procedure for v1 | On-pump isolated CABG via median sternotomy, 3 grafts: LIMA to LAD + 2 reversed SVGs (for example to OM and RCA/PDA). | STS: 161,907 isolated CABG in 2023, 88.5% on-pump (off-pump 11.5%) [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/); median 3 grafts per patient in an on-pump series [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/) |
| v2 candidate | SAVR (reuses ~75% of the CABG pipeline: sternotomy, CPB, cross-clamp, cardioplegia, de-airing, weaning, closure). | ~22,000 isolated SAVR per year in STS (178,014 from July 2014 to June 2022) [PMC12617330](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/); step timing study [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) |
| v3 candidate | Mitral valve repair (needs bicaval cannulation, left atriotomy, leaflet and ring mechanics, saline test, TEE grading). | 17,907 isolated primary MV operations in 2016; repair rate 65.6%; 82.5% repair for degenerative prolapse [Gammie 2018, PMID 30032907](https://pubmed.ncbi.nlm.nih.gov/30032907/) |
| Later variant | Off-pump CABG as a "hard mode" of CABG (stabilizer, shunts, haemodynamic instability). | 11.5% of isolated CABG in 2023 [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/) |
| Anticoagulation rule | Heparin ~300 IU/kg; go on bypass only when ACT > 480 s (or > 400 s with maximal-activation devices). | STS/SCA/AmSECT 2018 [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); 2024 EACTS/EACTAIC/EBCP [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Pump targets | Flow 2.2-2.8 L/min/m²; DO2 above ~270-300 mL/min/m²; transfuse if Hb < 6.0 g/dL; HCT 21-24% acceptable if DO2 > 273. | 2024 EACTS/EACTAIC/EBCP [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Temperature rules | Arterial outlet < 37 °C; arterial-venous gradient ≤ 10 °C; rewarm ≤ 0.5 °C/min with gradient ≤ 4 °C once outlet ≥ 30 °C. | STS/SCA/AmSECT 2015 [PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) |
| Cardioplegia model | Offer 2 modes: cold 4:1 blood (Buckberg) every 15-30 min, or single-dose del Nido 20 mL/kg (max 1000 mL) good for ~90 min. | [JECT 2014 PMC4557478](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478); 2024 EACTS [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Graft check | Score grafts with TTFM: mean flow > 15-20 mL/min, PI < 3-5, DF > 50%, backflow < 3-4%. | [Takami 2024 PMC11583563](https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563); ESC/EACTS 2018 IIa B via [EuroIntervention](https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began) |
| Reversal | Protamine-to-heparin ratio ≤ 1.0 (mg per 100 IU); never above 2.6 mg/100 IU. | 2024 EACTS [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/); STS 2018 [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| VF after unclamping | Internal paddles 10-30 J (game default 20 J). | [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868); CALS-ANZ 20 J [PMC10692601](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) |
| Team communication | Build every critical event as a closed-loop call and answer; add perfusion checklists (pre-bypass, weaning, post-bypass). | AmSECT 2023 Guideline 3.2 and Appendix F [AmSECT PDF](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf); [Wadhera 2010](https://pubmed.ncbi.nlm.nih.gov/20106395/) |
| Timings to target | CABG skin-to-skin ~3-4 h; CPB ~75-115 min; cross-clamp ~55-65 min (3 grafts). SAVR cross-clamp ~45-70 min. | [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/); [PMC10903005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903005); [PMC12617330](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/) |

---

## 1. Which procedures to model

### 1.1 Current volume data (United States, STS database)

| Fact | Number | Source | Grade |
|---|---|---|---|
| STS Adult Cardiac Surgery Database size | > 8.3 million procedures, > 1000 institutions, > 97% of US cardiac surgery (data to end of 2023) | [Iribarne 2025, PMID 40127833](https://pubmed.ncbi.nlm.nih.gov/40127833/) | A |
| Database size in 2026 update | > 8.6 million operations | [STS 2026 update, doi 10.1016/j.athoracsur.2026.05.024](https://doi.org/10.1016/j.athoracsur.2026.05.024) | A (abstract only) |
| Isolated CABG, 2023 | 161,907 cases | [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/) citing Iribarne 2025 | A |
| Off-pump share of isolated CABG, 2023 | 11.5% (18,656 of 161,907) | [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/) | A |
| Multi-arterial grafting share, 2023 | 17.9% of isolated CABG (+30% since 2018) | [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/) | A |
| Isolated SAVR | 178,014 patients from July 2014 to June 2022 (~22,000 per year, derived); operative mortality 1.9% | [PMC12617330](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/) | A |
| Isolated AVR trend | Fell ~40% in 2020 vs 2018 with no real rebound (TAVR effect) | [STS 2023 update](https://www.annalsthoracicsurgery.org/article/S0003-4975(23)01219-5/fulltext) (uncertain - snippet only) | A/C |
| Isolated primary MV operations | 14,442 (2011) to 17,907 (2016); repair rate 65.6% overall, 82.5% for degenerative prolapse; operative mortality 1.1% repair, 3.7% replacement | [Gammie 2018, PMID 30032907](https://pubmed.ncbi.nlm.nih.gov/30032907/) | A |
| MV repair trend | Fell ~15% at 2020 low, near 2018 level again by 2022 | [STS 2023 update](https://www.annalsthoracicsurgery.org/article/S0003-4975(23)01219-5/fulltext) (uncertain - snippet only) | A/C |
| Off-pump vs on-pump outcomes (2008-2023, experienced off-pump surgeons) | > 184,000 matched pairs; off-pump had lower short-term morbidity and mortality, similar long-term survival, more incomplete revascularization | [STS press release 31 Jan 2026](https://www.sts.org/press-releases/late-breaking-sts-study-finds-pump-cabg-experienced-surgeons-reduces-perioperative-complications) | B |
| Same study, numbers | Operative mortality 1.9% (off-pump) vs 2.2% (on-pump); incomplete revascularization 14.4% vs 8.1% | [Medscape](https://www.medscape.com/viewarticle/pump-beats-pump-cabg-short-term-outcomes-2026a10006g3) (uncertain - snippet only) | C |

**Conclusion.** Isolated CABG is still the most common adult heart operation in the US by a wide margin: about 162,000 per year versus about 22,000 isolated SAVR and about 18,000 isolated mitral operations. Most CABG (88.5%) is done on-pump. On-pump CABG is also the "parent" of the other operations. It contains every core system the game needs: sternotomy, CPB, cross-clamp, cardioplegia, micro-suturing, de-airing, weaning, protamine and closure.

### 1.2 Recommendation

1. **v1 = on-pump isolated CABG via median sternotomy, 3 grafts.** Graft plan: LIMA to LAD (in situ), reversed SVG to an OM branch, reversed SVG to the RCA or PDA. A real on-pump series had a median of 3 grafts per patient (IQR 2.5-4) [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/). LIMA to LAD remains the preferred graft for the LAD [ACC 2022](https://www.acc.org/Latest-in-Cardiology/Articles/2022/10/31/13/02/Key-Takeaways-From-the-2021-Coronary-Revascularization-Guidelines).
2. **v1 options inside CABG:** radial artery as the second graft (class 1 in the 2021 ACC/AHA/SCAI guideline for the next most important non-LAD target [ACC 2022](https://www.acc.org/Latest-in-Cardiology/Articles/2022/10/31/13/02/Key-Takeaways-From-the-2021-Coronary-Revascularization-Guidelines)); open vs endoscopic vein harvest; pedicled vs skeletonized LIMA.
3. **v2 = SAVR.** Highest reuse, short and well-measured cross-clamp phase (five timed sub-steps) [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387).
4. **v3 = mitral valve repair.** Most complex valve mechanics; needs new anatomy (left atrium, leaflets, chordae) and TEE grading.
5. **Later = OPCAB** as a mode of CABG, and combined operations (CABG + AVR).

### 1.3 How much of the CABG pipeline each later procedure reuses

These percentages are an engineering estimate for planning, not a sourced number.

| System / step block | CABG (v1) | SAVR | Mitral repair | OPCAB |
|---|---|---|---|---|
| Room setup, lines, induction, TEE, prep, time-out | build | reuse | reuse (+ TEE mitral views) | reuse |
| Median sternotomy, retractor, pericardium | build | reuse | reuse | reuse |
| Conduit harvest (LIMA, SVG, RA) | build | not used | not used | reuse |
| Heparin / ACT | build | reuse | reuse | reuse (lower target) |
| Aortic cannulation | build | reuse | reuse | not used |
| Venous cannulation | two-stage atrial | reuse | **new: bicaval + caval snares** | not used |
| CPB physiology model | build | reuse | reuse | standby only |
| Cross-clamp + cardioplegia | build | reuse (+ direct ostial delivery option) | reuse | not used |
| Venting (LV vent) | optional | reuse (usually needed) | reuse | not used |
| Micro-suturing engine | build (7-0/8-0 running) | reuse for pledgeted mattress sutures | reuse for ring sutures, neochords | reuse |
| Valve excision / sizing / prosthesis | - | **new** | **new (ring sizing, leaflet work)** | - |
| De-airing, unclamping, defibrillation | build | reuse | reuse | not used |
| Graft check (TTFM) | build | not used | not used | reuse |
| Weaning, protamine, decannulation | build | reuse | reuse (+ TEE repair check) | reduced |
| Closure, chest tubes, wires | build | reuse | reuse | reuse |
| **Estimated reuse** | 0% (base) | ~75% | ~65% | ~70% |

---

## 2. The team and who does what

| Role | Main jobs in the operation | Evidence |
|---|---|---|
| Surgeon (attending) | Leads the operation; incision, sternotomy, cannulation, cross-clamp, anastomoses, decision to wean; leads the time-out together with others. | Op note sequence [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html); roles [Wahr 2013 AHA statement](https://pubmed.ncbi.nlm.nih.gov/23918255/) |
| First assistant (surgeon, resident, or physician assistant) | Exposure, suction, "following" the running suture, vein or radial harvest, often the endoscopic vein harvest, chest closure. | REGROUP: only EVH harvesters with > 100 cases and < 5% conversion took part [ACC summary](https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018) |
| Scrub nurse | Instruments, sutures, sternal wires; controls free wire ends; counts. | Scrub nurse passes sternal wires and controls the free end with a clamp (patent text, C) |
| Circulating nurse | Time-out documentation, counts, blood products, room logistics, sign-out. | WHO checklist phases [WHO](https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources) |
| Anaesthesiologist | Lines, induction, airway, TEE, heparin and protamine administration, ventilation on/off, drugs, haemodynamics during weaning. | Closed-loop heparin/protamine examples (Stanford, snippet C); weaning checklist studies [Ogden 2016](https://pubmed.ncbi.nlm.nih.gov/27256448/) |
| Perfusionist | Heart-lung machine set-up and checklist, ACT checks, initiating CPB, flow, temperature, cardioplegia delivery, weaning the pump, returning volume. | AmSECT Standard 5.1: perfusionist shall use a checklist for each CPB [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) |

Responsibility for gas exchange moves from the anaesthesiologist to the perfusionist while the patient is on full bypass, because the oxygenator does the work (interoperable alarms paper, snippet only - uncertain) [JECT 2019](https://ject.edpsciences.org/articles/ject/abs/2019/01/ject-51-38/ject-51-38.html).

---

## 3. On-pump CABG: complete ordered step list (patient entry to ICU transfer)

How to read the tables: **Who** = the person who acts. **Tools** = instruments, sutures, devices. **Time** = typical duration. Times marked "(est.)" are game-design estimates anchored to the sourced totals in Section 6; they are not measured values. **OK when** = success criteria. **Errors / complications** = what can go wrong (good game events).

### Phase A. Before the incision

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| A1 | Patient enters OR; **WHO "Sign In"** (before anaesthesia): identity, site, procedure, consent, allergies, airway risk, blood loss risk. | Circulating nurse + anaesthesiologist | WHO checklist has 19 items in 3 phases: Sign In, Time Out, Sign Out [WHO](https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources); [checklist PDF](https://iris.who.int/bitstream/handle/10665/44186/9789241598590_eng_Checklist.pdf?sequence=2&isAllowed=y) | 3-5 min (est.) | All items confirmed aloud | Wrong patient or missing consent (game: hard stop) |
| A2 | Supine positioning; arms tucked; pressure points padded; legs prepared for vein harvest. | Nurses + anaesthesia | Supine is standard [opnote template (C)](https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/) | 5-10 min (est.) | Access to chest and both legs | Pressure injury, nerve injury (late event) |
| A3 | **Arterial line** (radial) before induction; large-bore IV; central line. | Anaesthesiologist | Radial arterial line and Swan-Ganz used in sample note [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html). If the radial artery will be harvested, plan the arterial line on the other arm [Sousa-Uva 2018](https://academic.oup.com/ejcts/article/54/6/971/5146781) | 10-20 min (est.) | Good waveform | Line in the arm planned for radial harvest (planning error) |
| A4 | **PA catheter** (optional, risk-based). | Anaesthesiologist | 2011 ACCF/AHA: Class I (LOE C) in cardiogenic shock, preferably before induction; IIa (LOE B) in acute instability; IIb (LOE B) in stable patients after weighing risk [WikiDoc reproduction](https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_pulmonary_artery_catheterization) | 10-15 min (est.) | PA pressures and cardiac output read | Arrhythmia while floating; PA rupture (rare) |
| A5 | Induction, intubation, ventilation. | Anaesthesiologist | General endotracheal anaesthesia [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html) | 10-15 min (est.) | Stable MAP, saturation | Hypotension at induction in poor LV |
| A6 | **TEE probe** in; baseline exam. | Anaesthesiologist | 2011 ACCF/AHA: TEE is Class I (B) for persistent haemodynamic disturbance and for concomitant valve surgery; IIa (B) for monitoring in CABG [WikiDoc](https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_TEE). Comprehensive exam = 28 views (ASE/SCA 2013) [ASE](https://www.asecho.org/guideline/comprehensive-tee/) (snippet) | 10-15 min (est.) | Baseline LV function, valves, aorta seen | Missed aortic atheroma (stroke risk later) |
| A7 | Bladder catheter, temperature probes (nasopharyngeal, bladder), defibrillator pads. | Nurse / anaesthesia | NP or PA temperature is reasonable for weaning measurement (Class IIa, C) [STS 2015 PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) | 5 min (est.) | Probes reading | - |
| A8 | Skin prep chin to toes; sterile drapes. | Surgeon / assistant / scrub nurse | Betadine prep in sample note [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html) | 10 min (est.) | Field sterile | Contamination (infection risk score) |
| A9 | **WHO "Time Out"** before skin incision; perfusion checklist completion acknowledged here. | Whole team | 2024 EACTS: pre-bypass checklist completion should be acknowledged during the team time-out [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/); perfusionist presents the patient-specific CPB plan (AmSECT Standard 3.1) [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) | 2-3 min (est.) | All roles respond | Skipped time-out (game penalty) |

### Phase B. Opening and conduit harvest

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| B1 | **Skin incision**, midline from sternal notch to below xiphoid; diathermy through fat to the sternum. | Surgeon | Scalpel (No. 10 or 20 blade); electrocautery. Cautery power settings: UNVERIFIED (no authoritative source found) | 3-5 min (est.) | Midline found | Off-midline incision (bad sternal split) |
| B2 | **Median sternotomy.** Ventilation is paused / lungs deflated while the saw runs (standard teaching; uncertain - no A source found). | Surgeon; anaesthesiologist holds ventilation | Powered sternum saw with blade guard. Stryker System 8 IFU: battery heavy-duty saw for the sternum; always use the matching blade guard [IFU](https://bioclinicalservices.com.au/stryker/clinical/system-8-sternum-saw-instructions-for-use-rev-aa-sept-2019) (B). Reciprocating saw is the standard for dividing the sternum (patent text, C) | 1-2 min (est.) | Straight split, bone wax on marrow | Saw injury to heart/lung if ventilating; off-midline split |
| B3 | **LIMA takedown.** IMA retractor lifts the left hemisternum. LIMA dissected from origin to bifurcation; branches clipped; papaverine; heparin given before the distal LIMA is divided. | Surgeon (or assistant) | IMA retractor (e.g., Favaloro / Rultract type); low-power diathermy; small metal clips; papaverine. One study used "low diathermy (15 mA)" and small clips (snippet, uncertain). Order: heparin first, then transect distally [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html) | 20-40 min (est.) | Free flow good; no branch bleeding; no dissection | Diathermy injury to LIMA; spasm; missed branch (steal); pleural tear |
| B3a | Option: **pedicled** vs **skeletonized** LIMA. | Surgeon | 2018 ESC/EACTS: skeletonization recommended to reduce sternal wound infection (Class I, B); bilateral IMA should be considered if sternal infection risk is low (IIa, B) [EuroIntervention](https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began). ART post hoc: skeletonized ITA had higher long-term MACE (HR 1.25), but not among surgeons with ≥ 51 enrolled cases (HR 1.07) [JAMA Cardiol 2021](https://jamanetwork.com/journals/jamacardiology/fullarticle/2784330) (snippet) | Skeletonized takes longer (est.) | - | Skeletonized: more skill-sensitive (game: higher precision demand, lower wound infection) |
| B4 | **Saphenous vein harvest** (parallel with B3, by the assistant). Open, bridged, or endoscopic. Branches tied or clipped; vein flushed and checked for leaks on the back table; reversed for use. | First assistant | REGROUP (1,150 patients, 16 VA centres): EVH vs open, no MACE difference (HR 1.12, 95% CI 0.83-1.51); leg wound infection 3.1% open vs 1.4% EVH [ACC summary](https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018) (B). 2018 ESC/EACTS: EVH in experienced hands IIa (A); no-touch if open IIa (B) [EuroIntervention](https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began) | 30-45 min (est.) | Enough length for planned grafts; no leaks | Vein too short, avulsed branch, over-distension injury; leg wound infection |
| B4a | Option: **no-touch** vein (harvested with surrounding fat). | Assistant | 16-year RCT: SVG patency 83% no-touch vs 64% conventional; LITA 88% [PMC11638440](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11638440/) (snippet); 10-RCT meta-analysis RR occlusion 0.70 but more leg wound problems (snippet) | Longer (est.) | - | More leg wound complications |
| B5 | Option: **radial artery** harvest (non-dominant arm; ulnar collateral checked first). | Assistant | Check hand collateral flow (modified Allen, pulse oximetry, Doppler); contraindications: poor ulnar flow, small size, heavy calcification; do not skeletonize RA; papaverine or milrinone intraluminal; use only on high-grade stenosis (competitive flow "string sign"). Patient-level meta-analysis: adverse cardiac events HR 0.67 vs SVG [Sousa-Uva 2018](https://academic.oup.com/ejcts/article/54/6/971/5146781) | 30-45 min (est.) | Good pulse, no spasm | Hand ischaemia (game: skipped Allen check), spasm, forearm paraesthesia |
| B6 | Open pericardium (inverted T); **pericardial stay sutures** to the wound edges to lift the heart. | Surgeon | Heavy silk or braided stay sutures (uncertain - no A source on size) | 3-5 min (est.) | Heart exposed | Phrenic nerve injury |

### Phase C. Heparin, cannulation, going on bypass

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| C1 | **Heparin** IV. | Anaesthesiologist (surgeon asks; closed loop) | ~300 IU/kg weight-based (STS 2018 Class IIa C; cited bolus 300 IU/kg) [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); 2019 EACTS range 300-500 U/kg [PMC10634377](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377); BJA Education "300-400 IU/kg" (snippet) | 1 min + 3-5 min to circulate (est.) | ACT checked ~3-5 min later | Heparin not given / given into a non-running line (fatal clotting if bypass starts) |
| C2 | **ACT check.** | Perfusionist / anaesthesia | Go when ACT > 480 s (STS IIa C); > 400 s often therapeutic on maximal-activation / microcuvette devices [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589). 2024 EACTS: pre-CPB target 480 s (survey range 400-500) [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). Heparin resistance: 6 of 100 patients given 300 IU/kg had ACT < 350 s [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) | 2 min (est.) | ACT ≥ target, called out | Low ACT (heparin resistance event: more heparin, antithrombin) |
| C3 | **Aortic purse-strings** (usually two concentric) on the distal ascending aorta; epiaortic scan if calcified. | Surgeon | Double purse-string on the arterial side because pressure is higher; venous side single (patent text, C). Pledgeted 2-0/3-0 braided suture typical (uncertain - no A source). 2018 ESC/EACTS: CT or epiaortic ultrasound should be considered (IIa C); minimal aortic manipulation (I B) [EuroIntervention](https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began) | 3-5 min (est.) | Purse-strings snugged with tourniquets (snares) | Too deep a bite (aortic wall injury) |
| C4 | **Aortic cannulation.** Systolic pressure lowered first. Stab incision, cannula in, tourniquets tightened, de-aired, connected to arterial line; pulsatile line pressure checked. | Surgeon asks anaesthesia to lower pressure | Systolic < 100 mmHg during cannulation to lower dissection risk [2024 EACTS PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). Distal ascending aorta is the preferred site [same]. Pressure-dispersion tips advised [same]. Sizes: adult aortic cannulas ~20-24 Fr are typical (uncertain - manufacturer tables not verified); Fr ÷ 3 = mm (24 Fr ≈ 8 mm) [Auckland](https://flexiblelearning.auckland.ac.nz/cyberiv/22.html) (B) | 3-5 min (est.) | Good line pressure, no bubbles | **Aortic dissection** (rare, catastrophic); air in line; malposition |
| C5 | **Venous cannulation** through the right atrial appendage with a **two-stage (cavo-atrial) cannula** into the IVC. | Surgeon | Single purse-string ~5-6 stitches on the venous side (patent text, C); 3-0 purse-string in RA appendage then 2-stage cannula [J Cardiothorac Surg 2008](https://rd.springer.com/content/pdf/10.1186/1749-8090-3-4.pdf) (snippet). 2024 EACTS lists bicaval, single atrial or cavo-atrial (2-stage); size depends on patient size and target flow [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). Example product size 34-46 Fr two-stage (GUDID record for Medtronic MC2, catalog 91246; snippet - uncertain) | 3-5 min (est.) | Good drainage when started | Atrial tear; arrhythmia from manipulation; air lock in venous line |
| C6 | **Antegrade cardioplegia / root vent cannula** in the ascending aorta (proximal to the clamp site); optional **retrograde** coronary sinus cannula through a small RA purse-string. | Surgeon | Antegrade delivery pressure 60-100 mmHg; retrograde flow 200-400 mL/min with coronary sinus pressure 30-50 mmHg (higher harms veins) [2024 EACTS](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) | 3-5 min (est.) | Line de-aired | Coronary sinus perforation (retrograde) |
| C7 | **Pre-bypass checklist** done; "ready for bypass" confirmed. | Perfusionist reads; team answers | AmSECT Appendix F checklist: patient, pump, gas, safety alarms, cardioplegia, anticoagulation "target achieved and results communicated" [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) | 1-2 min (est.) | All items green | Missing item (alarm off, line clamp left on) |
| C8 | **Initiate CPB.** Venous line unclamped; pump flow raised to full; when at full flow anaesthesia stops ventilation. | Surgeon: "go on bypass"; perfusionist confirms and reports "full flow"; anaesthesiologist stops ventilation | One institutional protocol: once arterial flow is full the perfusionist tells surgeon and anaesthetist, which allows the anaesthetist to stop ventilation [AKU protocol](https://www.aku.edu/mcpk/anaes/Documents/Cardiopulmonary%20Bypass%20(CPB)%20lnitiation%20And%20Maintenance.pdf) (snippet - uncertain). Flow target 2.2-2.8 L/min/m² [2024 EACTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | 1-3 min (est.) | Full flow, stable MAP, venous return good | Low venous return; high line pressure; MAP drop at onset (haemodilution) |
| C9 | **Optional LV vent** through the right superior pulmonary vein. | Surgeon | Commonly via right superior pulmonary vein, tip through mitral valve into LV [JA Clin Rep 2023](https://jaclinicalreports.springeropen.com/articles/10.1186/s40981-023-00608-w) (snippet) | 3 min (est.) | LV decompressed | Vent tip in aortic root (steals cardioplegia); air entry at vent site |
| C10 | **Cooling** (mild hypothermia). | Perfusionist | Hypothermia = core < 35 °C [2024 EACTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). Cooling gradient arterial-venous ≤ 10 °C (Class I C) [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211). Practice examples: ~32 °C [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html); 26-28 °C oesophageal in an older series [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/); some teams stay at 36 °C [PMC8357396](https://pmc.ncbi.nlm.nih.gov/articles/PMC8357396) | 5-10 min (est.) | Target temp reached | Gradient > 10 °C (gas emboli risk) |

### Phase D. Cross-clamp and cardiac arrest

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| D1 | Pump flow briefly lowered; **aortic cross-clamp** applied between the aortic cannula and the cardioplegia needle. Cross-clamp time starts. | Surgeon: "clamp on" (asks for flow down first); perfusionist confirms and starts timer | Cross-clamp (e.g., Fogarty / DeBakey type). Aorta palpated with pressure briefly ~30 mmHg in one series to look for plaque [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/) | < 1 min | Clamp across, no leak | Clamping a calcified aorta (stroke); clamp on the cannula |
| D2 | **Cardioplegia induction.** | Perfusionist delivers; surgeon watches the heart | **Mode 1, cold blood (modified Buckberg):** 4:1 blood:crystalloid, 4 °C; induction ~500 mL; maintenance every 15-20 min (~1000 mL total); warm "hot shot" ~500 mL at 37 °C before unclamping [JECT 2014 PMC4557478](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478). 2024 EACTS: cold intermittent every 20-30 min is usual [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). **Mode 2, del Nido:** 1:4 blood:crystalloid, 20 mL/kg, max 1000 mL if > 50 kg, half dose if clamp < 30 min expected, single dose [JECT 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478); single dose up to 90 min of ischaemia [2024 EACTS](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475); adult protocol 1000-1200 mL then 500 mL every 60 min if clamp > 90 min (snippet) [PMC8972223](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8972223/) | 2-4 min (est.) | Diastolic arrest (flat ECG), heart soft and cold | Incomplete arrest (aortic regurgitation steals cardioplegia; vent malposition); LV distension |
| D3 | Topical cooling (optional): iced slush; phrenic nerve protection pad. | Assistant | Slush and phrenic protector in sample note [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html) | 1 min | - | Phrenic nerve cold injury |

### Phase E. Grafting, de-airing and reperfusion

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| E1 | **Target exposure** and **coronary arteriotomy** for each distal. Heart lifted / rotated with laps and stay suture. | Surgeon; assistant exposes | Micro-knife (beaver blade) then **Potts scissors** to extend; coronary probe to size the lumen. Arteriotomy length: 20% shorter than the bevelled graft end, to leave a hood [PMC5147479](https://pmc.ncbi.nlm.nih.gov/articles/PMC5147479) (snippet); small arteriotomies of 3-4 mm are described (patent, C). A 4-6 mm teaching range is common (uncertain) | 2-3 min each (est.) | Clean lumen, no back-wall injury | Back-wall cut; arteriotomy in a diseased segment; wrong vessel |
| E2 | **Distal anastomoses, order.** Usual teaching: vein grafts to the back and side of the heart first, LIMA-LAD last (so the LIMA is not stretched when the heart is lifted). Sample note: SVG-OM, SVG-posterolateral, SVG-RCA, then LIMA-LAD [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html). Cardioplegia re-dosed between grafts (Buckberg mode) or down each vein graft. | Surgeon sews; assistant follows suture and blows/irrigates | **Running polypropylene:** 7-0 for SVG distals; 7-0 or 8-0 for LIMA-LAD [PMC5147479](https://pmc.ncbi.nlm.nih.gov/articles/PMC5147479) (snippet); sample note 7-0 vein, 8-0 LIMA [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html). Typical "about 10 stitches: 5 around heel, 5 around toe" (patent, C). Graft bevel ~30-45° (patent, C). Instruments: Castroviejo needle holder, fine (e.g., DeBakey / Gerald) forceps, coronary probes, blower | 8-15 min each (est.; 3 distals fit in a ~58-65 min clamp, see Section 6) | Probe passes heel and toe; no leak on test injection | Purse-stringing (too much suture tension), catching back wall, intimal flap, twisted or kinked graft, leak |
| E3 | **Proximal anastomoses**, option A: **single cross-clamp** (do proximals while the heart is still arrested). Option B: remove cross-clamp, place **side-biting (partial) clamp**, do proximals on the beating heart. | Surgeon | Aortic punch makes a 4-5 mm hole (patent text, C; punch sizes like 4.0-4.8 mm are typical - uncertain); sample note: 4 mm punch, running 6-0 Prolene [Scribd sample (C)](https://www.scribd.com/document/257599251/CABG-x4); 6-0 in [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html). Stroke: partial clamp 1.73% vs single clamp 1.8% (p = 0.92, n = 2,000) [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/); Mayo 8,497 patients 1.2% vs 1.5% (snippet) [Mayo](https://mayoclinic.elsevierpure.com/en/publications/on-pump-coronary-artery-bypass-graft-operation-is-one-crossclamp-) | 5-8 min each (est.) | Haemostatic, graft lies without kink | Partial clamp on atheroma (stroke), graft too long (kink) or too short (tension), aortic dissection from side clamp |
| E4 | **De-airing.** Root vent on suction; lungs gently inflated; heart allowed to fill; last proximal sutures left loose and aorta allowed to bleed ≥ 10 s before tying [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/). TEE checks for air. | Surgeon; anaesthesia inflates lungs; perfusionist adjusts volume | 2024 EACTS: TEE assesses residual air and adequacy of de-airing before weaning; CO2 insufflation reduces gaseous microemboli but no proven neuro benefit [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | 2-5 min (est.) | No air on TEE | Coronary air embolism (RCA: ST elevation, RV dysfunction) |
| E5 | **Cross-clamp removal** (if not already off). Optional warm "hot shot" just before. Clamp time stops. | Surgeon: "clamp off"; perfusionist records time | Hot shot ~500 mL at 37 °C just before clamp removal [JECT 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478) | < 1 min | Heart pinks up | VF on reperfusion (common) |
| E6 | **Reperfusion and rewarming** on full bypass. | Perfusionist | Arterial outlet < 37 °C (Class I C); gradient ≤ 10 °C; once outlet ≥ 30 °C keep gradient ≤ 4 °C and rate ≤ 0.5 °C/min (IIa B) [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) | 15-30 min (est.; overlaps with proximals) | NP temp near normal | Cerebral hyperthermia if outlet > 37 °C; rewarming too fast (gas emboli) |
| E7 | **Defibrillation** if VF. | Surgeon places internal paddles; anaesthesia or nurse charges and fires | Optimal initial open-chest energy 10-30 J [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868); 20 J internal in CALS-ANZ [PMC10692601](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/); internal paddle devices max 50 J (FDA listing, snippet). Defibrillate after careful de-airing and with core > 30 °C [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868) | < 1 min per shock | Sinus rhythm or paceable rhythm | Refractory VF: check K+, Mg, temperature, graft problem |
| E8 | **Epicardial pacing wires**: atrial on the right atrium (appendage), ventricular on the diaphragmatic surface of the RV; brought out through the skin below the incision. | Surgeon | Placement and practice vary by surgeon [2022 literature review](https://www.springermedizin.de/de/temporary-epicardial-pacing-wires-post-cardiac-surgery-a-literat/23121200) (snippet, B). Output set at twice the capture threshold [LITFL (C)](https://litfl.com/temporary-epicardial-cardiac-pacing/) | 2-3 min (est.) | Capture confirmed | Bleeding at wire site; later tamponade at removal |

### Phase F. Graft check, weaning and reversal

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| F1 | **TTFM graft check** (probe around each graft). | Surgeon | 2018 ESC/EACTS: intraoperative graft flow measurement should be considered (IIa, B) [EuroIntervention](https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began). Values that predict a patent graft: mean flow > 15 mL/min, PI < 5.0, DF > 50%, systolic reverse flow < 4%; stricter consensus: flow > 20 mL/min, PI < 3.0, reverse flow < 3% [Takami 2024 PMC11583563](https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563). One series suspected failure at flow < 20 mL/min and/or PI > 5 [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/). Cut-offs are not standardized [Takami 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563) | 1-2 min per graft (est.) | All grafts pass | Low flow + high PI: revise anastomosis (game: return on bypass / redo) |
| F2 | **Weaning checklist.** Typical items: temperature normal, rhythm/pacing, K+ and Ca2+, Hb, acid-base, lungs re-inflated and **ventilator on**, monitors re-zeroed, de-airing done on TEE, vents off, inotropes ready. | Anaesthesiologist + perfusionist + surgeon | 2024 EACTS recommends a weaning checklist (Recommendation Table 54; sample checklist in its supplement) [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). Delphi: 10 essential items chosen by 90 SCA members [Ogden 2016](https://pubmed.ncbi.nlm.nih.gov/27256448/); checklist raised completion in 5 of 9 tasks in simulation [PMID 25277642](https://pubmed.ncbi.nlm.nih.gov/25277642/). STS 2015: no recommendation on the best weaning temperature [PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211). Practice values often taught: core > 36 °C, K+ about 4-5 mmol/L (Stanford guide and lecture slides; uncertain - C) | 2-3 min (est.) | Every item answered | **Weaning with ventilator off** (hypoxia) - a known error [JECT 2019](https://ject.edpsciences.org/articles/ject/abs/2019/01/ject-51-38/ject-51-38.html) (snippet) |
| F3 | **Come off bypass.** Venous line partly clamped, heart filled, pump flow reduced in steps, then stopped. | Surgeon: "coming off"; perfusionist calls flows; anaesthesia reports pressures | AmSECT weaning items: venous assist off, reservoirs vented, shunts closed, vents clamped/removed; post-bypass: "announce bypass terminated", lines clamped [AmSECT 2023 Appendix F](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) | 3-10 min (est.) | Stable MAP and output without pump | Failed wean (LV/RV failure, vasoplegia) - back on bypass, inotropes, balloon pump |
| F4 | Volume given back from the pump in small boluses. | Perfusionist on request | Arterial circuit must be bubble-free before transfusing perfusate [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) | ongoing | Filling pressures OK | Air from circuit |
| F5 | **Venous cannula out**, purse-string tied. | Surgeon | - | 1-2 min (est.) | Dry | RA tear |
| F6 | **Protamine.** Pump suckers OFF first (so protaminized blood does not clot the circuit). Slow infusion. | Surgeon asks; anaesthesiologist gives and announces; perfusionist stops suckers | 2024 EACTS: protamine-to-heparin ratio should be kept below 1.0 [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). STS 2018: titrate to remaining heparin (IIa B); limit ratio < 2.6 mg per 100 U (IIa C); low-dose infusion 25 mg/h up to 6 h for rebound (IIb C); severe reaction: stop protamine, resuscitate, may need to restart CPB (I C) [PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589). Old practice: 1984 letter describes the protamine announcement and stopping sucker pumps at that moment (snippet) | 5-10 min (est.) | ACT back to baseline | **Protamine reaction** (hypotension, pulmonary hypertension, collapse); suckers left on (circuit clots - cannot go back on bypass) |
| F7 | **Aortic cannula out** (systolic pressure lowered), purse-strings tied, reinforced. | Surgeon | Same low-pressure rule as cannulation (est.) | 1-2 min | Dry | Bleeding, dissection |

### Phase G. Closure and transfer

| # | Step | Who | Tools / numbers | Time | OK when | Errors / complications |
|---|---|---|---|---|---|---|
| G1 | **Haemostasis**: check all anastomoses, cannulation sites, LIMA bed, sternal edges, pacing wire sites. | Surgeon + assistant | Diathermy, clips, extra sutures; blood products per tests | 10-20 min (est.) | Dry field | Missed bleeder (late re-exploration event) |
| G2 | **Chest tubes**: mediastinal (often 2) and left pleural (LIMA harvest opened the left pleura); right pleural if RIMA. | Surgeon | Template: two mediastinal + left pleural [opnote (C)](https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/). 28F mediastinal tube used in an RCT arm [J Cardiothorac Surg 2021](https://link.springer.com/10.1186/s13019-021-01414-0) (snippet). Clogging rate cited at 36% (snippet) | 3-5 min (est.) | Tubes draining | Clogged tube -> tamponade |
| G3 | **Sternal wiring.** Stainless steel wires (peristernal, single or figure-of-eight), twisted. | Surgeon; scrub nurse passes wires and controls ends | 2,672 patients: DSWI 1.5%; risk higher with ≤ 8 paired fixation points vs ≥ 9 (p = 0.002) [Shaikhrezai 2012 PMC3397758](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758); template uses 7 wires [opnote (C)](https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/); stainless steel no. 5 wires in an RCT (snippet) | 10-15 min (est.) | Stable sternum | Wire through IMA graft or RV; unstable sternum (dehiscence later) |
| G4 | Fascia, subcutaneous, skin closure; dressings; leg closure. | Assistant | Layered closure [MT Samples (C)](https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html) | 10-15 min (est.) | Closed | - |
| G5 | **WHO "Sign Out"**: procedure recorded, instrument/swab/needle counts, specimens, key concerns for recovery. Team debrief (AmSECT Standard 3.3: perfusionist joins the debrief). | Circulating nurse leads | [WHO](https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources); [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) | 2-3 min (est.) | Counts correct | Count mismatch (retained item) |
| G6 | **Transfer to ICU** intubated and sedated; handover. | Anaesthesiologist + surgeon | Fast-track extubation target 4-6 h in a template [opnote (C)](https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/); at least 6 h ventilation in an older series [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/) | 10-20 min (est.) | Stable on monitors | Transport disconnection; arrest in ICU (see 11.3) |

---

## 4. Numbers the game engine needs during CPB

| Parameter | Value / range | Source | Grade |
|---|---|---|---|
| Heparin initial dose | 300 IU/kg typical; 300-500 U/kg range; 300-400 IU/kg in teaching | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); [EACTS 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377); BJA Education (snippet) | A / A / C |
| ACT to start CPB | > 480 s (> 400 s for maximal-activation devices) | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| Heparin resistance definition | Not reaching target after 400 or 500 U/kg in most papers | Review (snippet) [iperfusion PDF](https://iperfusion.org/wp-content/uploads/2024/01/PIIS1538783624000072.pdf) | C |
| Off-pump heparin | Often half dose (~150 U/kg); 80% of surgeons keep ACT ≥ 300 s | Survey and RCT (snippets) [PMC3329286](https://pmc.ncbi.nlm.nih.gov/articles/PMC3329286) (uncertain) | C |
| Pump flow | 2.2-2.8 L/min/m² (moderate hypothermia to normothermia) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| Oxygen delivery (DO2) | Keep above ~250-300 mL/min/m²; 270-280 thresholds linked to kidney injury | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| MAP on CPB | 50-80 mmHg (2019 EACTS Class I A); 2024 version cites RCTs with no clear benefit of higher targets (70-80 vs 40-50 mmHg) | [Ranucci editorial on 2019 guideline](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9918189/) (snippet); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | B / A |
| MAP < 50 mmHg | One of the CPB factors linked to 30-day mortality in a perfusion database model | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| Systolic during aortic cannulation | < 100 mmHg | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| Transfusion trigger on CPB | Hb < 6.0 g/dL; HCT 21-24% acceptable if DO2 > 273 mL/min/m² | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| Arterial outlet max temp | < 37 °C | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) | A |
| Cooling / rewarming gradient | ≤ 10 °C; when outlet ≥ 30 °C: ≤ 4 °C and ≤ 0.5 °C/min | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) | A |
| Cardioplegia antegrade pressure | 60-100 mmHg | [EACTS 2024](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) | A |
| Cardioplegia retrograde | 200-400 mL/min; coronary sinus pressure 30-50 mmHg | [EACTS 2024](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) | A |
| Cold blood redose interval | Every 15-20 min (Cleveland Clinic Buckberg); every 20-30 min (guideline text) | [JECT 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| del Nido | 20 mL/kg, max 1000 mL, single dose; up to 90 min | [JECT 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478); [EACTS 2024](https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) | A |
| Protamine | Ratio ≤ 1.0 mg per 100 IU heparin (2024); never > 2.6 mg/100 U (2018) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/); [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) | A |
| Internal defibrillation | 10-30 J start; 20 J common protocol | [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868); [PMC10692601](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/) | A |
| Serious perfusion adverse events | 1 in 1,236 to 1 in 2,500 procedures | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |

---

## 5. Instrument trays (realistic cardiac set)

Exact tray contents differ by hospital. Names below are standard surgical names; the evidence for specific tray lists is weak (catalogues and sample notes), so the list is graded B/C. Cautery power settings could not be verified on any authoritative page: **UNVERIFIED**.

| Group | Instrument | Used for | Evidence |
|---|---|---|---|
| Opening | Scalpel handles (No. 3/4) with No. 10/15/20/11 blades | Skin, stab incisions for cannulas | General surgical practice (C) |
| Opening | Electrocautery pencil (monopolar) | Fat, periosteum, LIMA branches (low power) | Low diathermy used for LIMA [snippet](https://journal.hsforum.com/index.php/HSF/article/download/571/575/577) (C); settings UNVERIFIED |
| Opening | Powered sternum saw + blade guard; oscillating saw for redo sternotomy | Median sternotomy | [Stryker System 8 IFU](https://bioclinicalservices.com.au/stryker/clinical/system-8-sternum-saw-instructions-for-use-rev-aa-sept-2019) (B); reciprocating saw standard (patent, C) |
| Opening | Bone wax | Marrow bleeding | (C) |
| Retraction | Sternal retractor (e.g., Ankeney, Morse, Cooley type) | Spread the sternum | Ankeney adult sternal retractor in catalogues (C) |
| Retraction | IMA retractor (Favaloro, Rultract "skyhook" type) | Lift left hemisternum for LIMA | Modified mammary retractor mentioned in redo paper [PMC12529703](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12529703/) (C) |
| Retraction | Weitlaner / self-retaining leg retractor | Open vein harvest | (C) |
| Vascular | DeBakey atraumatic forceps (various lengths) | General tissue handling | [Issuu instrument guide (C)](https://issuu.com/japacvs/docs/surgical_instruments_csoc) |
| Vascular | Gerald / ring-tip forceps | Handling the mammary artery | Same (C) |
| Micro | Castroviejo needle holders (locking, tungsten carbide tips) | 6-0 to 8-0 suture for anastomoses | Coronary set listings (C) [coronary set](https://www.indianbusinessportal.in/products/coronary-set) |
| Micro | Potts scissors (25°, 45°, 60°, 90°, 125° angles); Diethrich coronary scissors | Extending arteriotomies, trimming grafts | Catalogue listings (C) |
| Micro | Castroviejo micro scissors | Trimming the LIMA end | [Issuu guide (C)](https://issuu.com/japacvs/docs/surgical_instruments_csoc) |
| Micro | Coronary probes / vessel dilators (graduated, e.g., 1.0-2.5 mm) | Sizing the coronary lumen and checking the toe/heel | Scanlan CABG line lists "vessel dilator/probes" (catalogue snippet; exact sizes uncertain) |
| Micro | Beaver micro-knife (arteriotomy blade) | Opening the coronary | (C) |
| Micro | Blower / mister (CO2 or saline) | Clear field during anastomosis | "Mister-blower" in LITA-LAD technique (snippet) (C) |
| Clamps | Aortic cross-clamp (straight / angled) | Isolate the heart from circulation | (C) |
| Clamps | Side-biting / partial occlusion clamp (Satinsky / Cooley type) | Proximal anastomoses on beating heart | [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/) (technique, A) |
| Clamps | Bulldog clamps (DeBakey ring-handle, micro-coronary) | Occlude the LIMA before anastomosis | Catalogue listing (C); bulldog on ITA before trimming (snippet) |
| Clamps | Tubing clamps | CPB lines | AmSECT checklist "tubing clamps available" [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf) (A) |
| Cannulation | Tourniquets (Rumel snares) + snare introducers | Tighten purse-strings around cannulas | (C) |
| Cannulation | Aortic cannula, two-stage venous cannula, cardioplegia/root vent needle, retrograde coronary sinus cannula, LV vent | CPB circuit connections | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) for types |
| Grafts | Aortic punch (about 4-5 mm) | Holes for proximal anastomoses | Patent text (C); 4 mm punch in sample note (C) |
| Grafts | Ligating clips (small/medium) and appliers | LIMA and vein branches | (C) |
| Grafts | Endoscopic vein harvest system | EVH | REGROUP (B) |
| Flow | TTFM console and probes (e.g., Medistim VeriQ) | Graft flow, PI, DF | NICE VeriQ guidance lists mean flow, PI, DF outputs [NICE](https://www.nice.org.uk/guidance/mtg8/documents/veriq-assessment-report-overview2) (B) |
| Rhythm | Internal defibrillator paddles (sterile); temporary pacing box | VF after unclamp; pacing | [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868) (A) |
| Closure | Sternal wires (stainless steel, size 5-7), wire twister, wire cutter, heavy needle holder | Sternal closure | [PMC3397758](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758) (A); no. 5 wire RCT (snippet) |
| Closure | Chest tubes (e.g., 28F) and drainage system | Drain blood | RCT (snippet) |
| Sutures | Polypropylene 8-0 (LIMA-LAD), 7-0 (vein distals), 6-0 (proximals), 4-0/5-0 (repairs, cannulation sites), braided 2-0 pledgeted (valve), ePTFE 4-0 (neochords) | Each anastomosis or repair | See Phases E, 8 and 9 |

---

## 6. Typical total timings

| Operation | Skin-to-skin | CPB time | Cross-clamp time | Source | Grade |
|---|---|---|---|---|---|
| On-pump CABG, n = 51, median 3 grafts | 240 min (IQR 195-275) | 112 min (IQR 82.5-128) | 65 min (IQR 48.5-80) | [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/) | A |
| Isolated primary CABG, REPLICCAR II, n = 3,090 (5 centres) | - | mean 76.8 ± 27.5 min | mean 58.2 ± 23.4 min | [PMC10903005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903005) | A |
| Same study, risk groups | - | CPB > 140 min group: in-hospital mortality OR 4.22-7.33 | - | [PMC10903005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903005) | A |
| On-pump CABG, E-CABG, n = 2,957 | - | - | mean 58 ± 25 min (~38% > 60 min) | (snippet) | C |
| CABG surgeon learning: 16,486 CABGs | new residents ~234 min vs seniors ~180 min | - | - | [RTI](https://www.rti.org/publication/learning-cabg-surgery) (snippet) | C |
| Isolated SAVR, STS, 178,014 patients | - | median 90-96 min | median 68-72 min | [PMC12617330](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/) | A |
| Isolated SAVR, single centre, n = 57 | - | - | 50.5 ± 13.8 min (experienced 44.1, less experienced 60.6) | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) | A |
| Robotic MV repair, n = 200 (degenerative) | - | median 122 min | median 79 min | (snippet) [TUM portal](https://portal.fis.tum.de/en/publications/two-hundred-robotic-mitral-valve-repair-procedures-for-degenerati/) | C |
| Minimally invasive MV repair, n = 1,732 | - | median 99.5 min (single clamp) | median 60 min (single clamp) | (snippet) | C |

**Game default for v1 (3-graft CABG):** skin-to-skin ~240 min real time; CPB ~90 min; cross-clamp ~60 min. Time compression in the game is a design choice, but the internal clock should track these real values so the debrief can show "your clamp time vs real surgeons".

---

## 7. Real OR call-outs and closed-loop communication

### 7.1 What the evidence says

- Closed-loop communication means the receiver repeats the order back and the sender confirms. AmSECT Guideline 3.2: protocol-driven (closed-loop) communication should be used to acknowledge verbal commands, verify content and reduce ambiguity [AmSECT 2023](https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf). (A)
- A structured, unambiguous verbal protocol around **8 critical events during CPB** cut communication breakdowns from 11.5 to 7.3 per case (p = 0.008) [Wadhera 2010](https://pubmed.ncbi.nlm.nih.gov/20106395/). The abstract does not list the 8 events. (A)
- Communication failure and human factors were the two leading root causes of sentinel events (Joint Commission 2014-2015, cited in [Fann 2016](https://www.sts.org/sites/default/files/documents/patient_safety/HumanNatureinCTSurgery.pdf)). (A)
- The AHA statement says preventable errors in the cardiac OR are often cognitive, system or teamwork failures, not technical failures; it recommends briefings, checklists and debriefings [Wahr 2013](https://pubmed.ncbi.nlm.nih.gov/23918255/). (A)
- In a paediatric cardiac study, closed-loop communication was seen only between surgeon and perfusionist; surgeon-anaesthetist talk was ≤ 5% of exchanges [PMC8720321](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720321) (snippet). (C)
- The 2024 EACTS guideline says weaning is a multidisciplinary effort where communication among all team members is crucial, and recommends a checklist before weaning [PMC11826094](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/). (A)

### 7.2 Proposed call-out script for the game

No source gives one universal script; wording varies by hospital (uncertain). The script below is a **game design proposal** built on the closed-loop rule and the critical events above.

| Event | Caller says | Responder says (read-back) | Who responds |
|---|---|---|---|
| Heparin | Surgeon: "Heparin, please, 300 per kilo." | "Giving 300 units per kilo of heparin... heparin is in." | Anaesthesiologist |
| ACT | Perfusionist: "ACT is 520." | "ACT 520, thank you. We are anticoagulated for bypass." | Surgeon |
| Lower pressure for cannulation | Surgeon: "Systolic under 100 for the aortic cannula." | "Bringing systolic under 100... systolic is 95." | Anaesthesiologist |
| Ready | Surgeon: "Are we ready for bypass?" | "Pre-bypass checklist complete. Ready." | Perfusionist |
| Going on | Surgeon: "Go on bypass." | "Going on bypass... on bypass... full flow, 4.8 litres." | Perfusionist |
| Ventilation off | Perfusionist: "Full flow. You can stop ventilating." | "Ventilator off." | Anaesthesiologist |
| Cooling | Surgeon: "Cool to 32." | "Cooling to 32." | Perfusionist |
| Clamp on | Surgeon: "Flow down for the clamp." -> "Clamp on." | "Flow down... clamp on at 09:42, restoring flow." | Perfusionist |
| Cardioplegia | Surgeon: "Cardioplegia, please." | "Cardioplegia going in, root pressure 75... 500 in... heart is arrested." | Perfusionist |
| Redose timer | Perfusionist: "Twenty minutes since last dose." | "Thanks, dose down the vein graft after this anastomosis." | Surgeon |
| Rewarm | Surgeon: "Start rewarming." | "Rewarming, outlet capped at 37." | Perfusionist |
| Hot shot / clamp off | Surgeon: "Hot shot." -> "Clamp off." | "Hot shot in... clamp off at 10:44, clamp time 62 minutes." | Perfusionist |
| Defibrillate | Surgeon: "Paddles in, 20 joules." | "Charging 20... charged... clear... shock delivered." | Anaesthesiologist / nurse |
| Ventilate | Surgeon: "Ventilate, please." | "Ventilating... ventilator on, lungs up." | Anaesthesiologist |
| Weaning checklist | Perfusionist: "Weaning checklist." | Item-by-item answers (temperature, rhythm, K+, ventilator ON, vents off) | Anaesthesiologist + surgeon |
| Coming off | Surgeon: "Coming off." | "Coming down to 2 litres... 1 litre... off bypass." | Perfusionist |
| Protamine | Surgeon: "Start protamine." | "Suckers off... protamine going in, slowly." | Perfusionist (suckers), anaesthesiologist (drug) |
| Decannulate | Surgeon: "Aortic cannula out." | "Arterial line clamped, ready." | Perfusionist |

Mechanic: a missed or wrong read-back increases a "communication breakdown" counter; some errors cause events (for example, going on bypass with low ACT; weaning with ventilator off; protamine with suckers on).

---

## 8. SAVR: what is new compared with CABG

Basic flow is the same as CABG phases A, B (without conduit harvest), C, D, F, G. New or changed steps:

| # | New / changed step | Details and numbers | Source | Grade |
|---|---|---|---|---|
| S1 | No conduit harvest | Shorter opening phase | - | - |
| S2 | LV vent is usual | Via right superior pulmonary vein into the LV | [JA Clin Rep 2023](https://jaclinicalreports.springeropen.com/articles/10.1186/s40981-023-00608-w) (snippet) | B |
| S3 | Cardioplegia delivery | Aortic regurgitation can stop root cardioplegia from reaching the coronaries; combine antegrade (often direct into the coronary ostia after aortotomy) and retrograde | Antegrade + retrograde to reach all myocardium [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) | A |
| S4 | **Exposure** after clamp: transverse (or oblique "hockey-stick") aortotomy above the valve; stay sutures | Measured step 1 "exposure" incl. cardioplegia: 5.2 ± 2.8 min | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) | A |
| S5 | **Leaflet excision and annulus decalcification**, irrigation to remove debris, **sizing** with prosthesis-specific sizers | Measured step 2: 8.2 ± 4.4 min | Same | A |
| S6 | **Annular sutures**: pledgeted, braided 2-0 mattress sutures through annulus and sewing ring | Mean 15.0 ± 2.0 sutures (experienced 14.4 vs 15.9); suturing step 16.4 ± 5.9 min (32.3% of clamp time) | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) | A |
| S6a | Suture detail | 12-15 pledgeted 2-0 Ethibond from ventricular side through annulus then sewing ring (interrupted technique) | [J Cardiothorac Surg 2024](https://link.springer.com/article/10.1186/s13019-024-02754-3) (snippet) | C |
| S7 | **Seat valve and tie** (by hand or automated knot device such as Cor-Knot) | Tying step 9.2 ± 3.0 min (18.5% of clamp time) | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) | A |
| S8 | **Check**: coronary ostia not blocked, leaflets of a mechanical valve move freely | Standard (uncertain - no A source in this search) | - | - |
| S9 | **Aortotomy closure** (two-layer running polypropylene), de-airing, clamp off | "Declamping" step 11.4 ± 3.9 min | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387); two-layer closure [PMC8357396](https://pmc.ncbi.nlm.nih.gov/articles/PMC8357396) | A / B |
| S10 | **TEE**: prosthesis seating, paravalvular leak, gradient | TEE Class I (B) for valve surgery [WikiDoc](https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_TEE) | B |
| S11 | Valve options for the game | Bioprosthesis (e.g., Perimount Magna Ease) or mechanical (e.g., Medtronic AP 360) were used in the timing study | [Swiss Med Wkly 2017](https://smw.ch/index.php/smw/article/download/2329/3539/10387) | A |
| S12 | Outcomes to show | STS SAVR operative mortality 1.9% overall | [PMC12617330](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/) | A |

Specific SAVR complications for events: heart block (pacing), paravalvular leak, coronary ostial obstruction, aortic dissection at aortotomy, retained calcium debris (stroke).

---

## 9. Mitral valve repair: what is new compared with CABG

| # | New / changed step | Details and numbers | Source | Grade |
|---|---|---|---|---|
| M1 | **Bicaval cannulation** (SVC + IVC cannulas) with caval snares if the right atrium is opened; or single two-stage cannula for left atrial approach | Sternotomy series used bicaval or single two-stage cannulation | [Asian Cardiovasc Thorac Ann 2009](https://https-sage-cnpereading-com-443.webvpn1.xju.edu.cn/doi/10.1177/0218492309103330) (snippet, mirror - uncertain) | C |
| M2 | **Left atriotomy** through Sondergaard's (interatrial) groove; alternatives: transseptal, superior septal | Three main left atrial accesses listed | [Tex Heart Inst J editorial](https://thij.kglmeridian.com/view/journals/thij/50/1/article-e217563.xml) (snippet); groove dissection [Nagoya PDF](https://nagoya.repo.nii.ac.jp/record/15589/files/13_Song1.pdf) (snippet) | B |
| M3 | **Atrial retractor**; exposure suture on posterior annulus | Retractor blade ~1 cm above the annulus; 4-0 polypropylene traction stitch | [Perier 2013 PMC3857044](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044) | A |
| M4 | **Valve analysis** (Carpentier segments A1-A3, P1-P3; P1 as reference) | Find prolapsing segment | Same | A |
| M5 | **Leaflet work**: resection (triangular/quadrangular) **or** artificial chords ("respect" approach) | STS: annuloplasty 94.3%, leaflet resection 46.5%, artificial chords 22.7% of repairs; 16.2% of replacements followed a failed repair attempt | [Gammie 2018](https://pubmed.ncbi.nlm.nih.gov/30032907/) | A |
| M5a | Neochord detail | 4-0 ePTFE figure-of-eight through papillary muscle tip; arms ~3 mm apart, 4-5 mm from free edge; knots 10-12 ventricular side, 5 atrial side; deep clefts closed with 5-0 monofilament | [Perier 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044) | A |
| M6 | **Annuloplasty ring sizing** (by anterior leaflet area / height) and ring sutures | 2-0 braided sutures; middle of anterior leaflet matches middle of ring | [Perier 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044) | A |
| M7 | **Saline test**: fill LV with saline before closing the atrium; look for leak and a symmetric closure line | - | [Perier 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044) | A |
| M8 | Close atrium, de-air, clamp off, wean | As CABG | - | - |
| M9 | **TEE repair check** (post-bypass) | Residual MR; mean gradient > 5-6 mmHg suggests stenosis; systolic anterior motion (SAM) after repair 1-16%, coaptation-to-septum distance < ~2.5 cm predicts SAM (snippets) | (snippets) [JTD](https://jtd.amegroups.org/article/view/18369) | C |
| M10 | **Second pump run** if repair fails (re-repair or replace) | Decision tree for the game | Practice (uncertain) | - |
| M11 | Outcomes to show | Operative mortality 1.1% repair vs 3.7% replacement; less invasive approach 23.0% | [Gammie 2018](https://pubmed.ncbi.nlm.nih.gov/30032907/) | A |
| M12 | Minimally invasive variant (later) | Right mini-thoracotomy 3.5-4 cm; femoral venous 21-25 Fr, arterial 18-22 Fr; Chitwood transthoracic clamp; Bretschneider cardioplegia, redose after 100 min | [Perier 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044) | A |

---

## 10. Off-pump CABG (later variant), what changes

| Item | Off-pump detail | Source | Grade |
|---|---|---|---|
| Share of practice | 11.5% of isolated CABG in 2023 | [PMC13555479](https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/) | A |
| Heparin | Often half dose (150 U/kg); 80% keep ACT ≥ 300 s; RCT 300 vs 150 U/kg no better clot control with high dose | (snippets) [PMC3329286](https://pmc.ncbi.nlm.nih.gov/articles/PMC3329286) | C |
| Exposure and stabilization | Deep pericardial stay suture + tissue stabilizer (Octopus / Acrobat type); haemodynamic instability worst during PDA grafting | (snippets) [EKB](https://journals.ekb.eg/article_124682.html); [opnote (C)](https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/) | C |
| Intracoronary shunts | Sizes 1-3 mm by vessel size (Flo-Coil / Flo-Thru) | (snippet) | C |
| Trade-off | Lower short-term morbidity and mortality in expert hands, more incomplete revascularization | [STS press release](https://www.sts.org/press-releases/late-breaking-sts-study-finds-pump-cabg-experienced-surgeons-reduces-perioperative-complications) | B |

---

## 11. Complications and failure modes (event library)

### 11.1 Intraoperative events with sourced numbers

| Event | Trigger in game | Real number | Source |
|---|---|---|---|
| Heparin resistance | ACT below target after standard dose | 6/100 had ACT < 350 s after 300 IU/kg | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Stroke | Clamping atheroma; air | 1.2-1.8% with single vs partial clamp | [Uyar 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/); Mayo (snippet) |
| Serious perfusion accident | Circuit failure, disconnection | 1/1,236 to 1/2,500 procedures | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| VF after reperfusion | Clamp removal | Common; treat 10-30 J internal | [PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868) |
| Graft failure | Bad anastomosis | Low flow / high PI on TTFM; 5 anastomoses revised in 51 patients after ultrasound + TTFM | [PMC6950894](https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/) |
| Protamine reaction | Fast protamine | Severe reaction may need return to CPB (STS Class I C) | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Weaning with ventilator off | Missed checklist item | Known error; electronic alarm proposed | [JECT 2019](https://ject.edpsciences.org/articles/ject/abs/2019/01/ject-51-38/ject-51-38.html) (snippet) |

### 11.2 Postoperative events (for an ICU epilogue)

| Event | Real number | Source |
|---|---|---|
| Deep sternal wound infection | 1.5% (40/2,672); fewer with ≥ 9 paired wire fixation points | [PMC3397758](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758) |
| Leg wound infection | 3.1% open vs 1.4% endoscopic harvest | [ACC REGROUP](https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018) |
| Chest tube clogging | ~36% (single-centre) | (snippet) |
| Operative mortality isolated CABG | ~1.9-2.2% (non-emergency, 2008-2023) | [Medscape](https://www.medscape.com/viewarticle/pump-beats-pump-cabg-short-term-outcomes-2026a10006g3) (snippet) |

### 11.3 Arrest in ICU after cardiac surgery (bonus scenario)

STS expert consensus (Ann Thorac Surg 2017;103:1005-20): at least six team roles; for VF give **three sequential shocks before external compressions**, then **emergency resternotomy within 5 minutes**; for asystole/severe bradycardia pace first via wires (DDD 80-100 bpm, maximal outputs); internal massage is better than external; amiodarone 300 mg after three failed shocks [STS consensus PDF](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf). CALS-ANZ: up to three stacked shocks, internal defibrillation 20 J, DOO pacing [PMC10692601](https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/).

---

## Game hooks

How each finding becomes a mechanic, data value or rule.

| # | Finding | Game mechanic / data value / rule |
|---|---|---|
| H1 | CABG is the most common operation; median 3 grafts | Campaign starts with a 3-graft CABG (LIMA-LAD, SVG-OM, SVG-RCA). Graft count becomes a difficulty setting (1-5). |
| H2 | WHO checklist 3 phases, 19 items | Three mini-dialogues: Sign In, Time Out, Sign Out. Missing an item = score penalty; wrong patient = hard fail. |
| H3 | ACT > 480 s before CPB | Hard gate: "Go on bypass" button disabled until ACT ≥ 480 (or ≥ 400 with a "maximal-activation device" option). If forced, circuit clot event. |
| H4 | 6% heparin resistance | Random event p = 0.06: ACT stays < 350 s; player must give more heparin or antithrombin. |
| H5 | Systolic < 100 mmHg during cannulation | If player cannulates with systolic ≥ 100, dissection risk rises (rare catastrophic event). |
| H6 | Flow 2.2-2.8 L/min/m², DO2 > 270-300, Hb > 6 | Perfusion panel with green zones; time below DO2 270 adds an "AKI risk" score. |
| H7 | Temperature rules (< 37 °C outlet, ≤ 10 °C gradient, ≤ 0.5 °C/min) | Perfusion sliders with hard warnings; breaking rules adds "neuro risk". |
| H8 | Cardioplegia modes and intervals | Player picks Buckberg (redose timer 15-20 min) or del Nido (20 mL/kg up to 1000 mL, ~90 min). Missed redose = "ischaemia meter" climbs; affects VF chance and weaning difficulty. |
| H9 | Retrograde 200-400 mL/min at CS pressure 30-50 | Over-pressure triggers coronary sinus injury event. |
| H10 | Distal technique: 7-0/8-0 running, arteriotomy shorter than graft bevel, probe heel and toe | Suturing mini-game: bite spacing, depth, tension; back-wall catch detection; probe test at the end. |
| H11 | TTFM cut-offs (flow > 15-20, PI < 3-5, DF > 50%, reverse flow < 3-4%) | After unclamp, each graft gets TTFM values computed from anastomosis quality. Fail -> choice: accept, revise (go back on pump), or add graft. |
| H12 | Single clamp vs side-biting clamp | Strategy choice for proximals: single clamp (longer clamp time) vs side clamp (atheroma stroke risk if aorta "calcified" in patient file). |
| H13 | VF on reperfusion, 10-30 J | Defib mini-task with energy selector (default 20 J). Refractory VF prompts checks (K+, temperature, air, graft). |
| H14 | Weaning checklist (ventilator ON) | Checklist UI; skipping "ventilator on" causes falling saturation within seconds after flow reduction. |
| H15 | Protamine ratio ≤ 1.0, suckers off | Dose slider; ratio > 1.0 gives bleeding penalty; > 2.6 adds coagulopathy; giving protamine with suckers on clots the pump (cannot return to bypass). |
| H16 | Protamine reaction | Rare event: hypotension and pulmonary hypertension; correct answer is stop protamine, support, possibly re-heparinize and go back on bypass. |
| H17 | ≥ 9 paired wire fixation points lowers DSWI | Closure mini-game: number and placement of wires change infection and dehiscence risk in the epilogue. |
| H18 | EVH vs open: same MACE, fewer leg infections | Harvest choice affects time and leg infection rate (3.1% vs 1.4%). |
| H19 | Skeletonized vs pedicled LIMA | Skeletonized: lower sternal infection risk, higher precision demand; mistakes cause LIMA injury. |
| H20 | Radial artery needs ulnar collateral check and high-grade target | If player skips Allen/Doppler check: hand ischaemia event. If placed on moderate stenosis: "string sign" late failure. |
| H21 | Closed-loop call-outs (AmSECT 3.2; 11.5 -> 7.3 breakdowns) | Voice/text call-out system with required read-backs; "communication breakdown" counter shown in debrief. |
| H22 | Real timings (CABG clamp ~58-65 min; SAVR 44-61 min by experience) | Debrief compares player clamp time, CPB time and skin-to-skin with real ranges; "senior surgeon" benchmark. |
| H23 | SAVR sub-step times (exposure 5.2, resection 8.2, suturing 16.4, tying 9.2, declamp 11.4 min) | SAVR level timeline and par times for each sub-step. |
| H24 | Mitral repair: saline test, TEE SAM, gradient | Repair puzzle with a saline test view; post-bypass TEE grades MR and SAM; failing triggers second pump run. |
| H25 | STS resuscitation protocol | Optional ICU emergency: 3 shocks, resternotomy within 5 min, pace if wires present. |

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | 161,907 isolated CABG in STS database in 2023; 11.5% off-pump | https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/ | A |
| 2 | STS ACSD has > 8.3 million procedures, > 1000 sites, > 97% of US cardiac surgery | https://pubmed.ncbi.nlm.nih.gov/40127833/ | A |
| 3 | 178,014 isolated SAVR in STS (July 2014-June 2022); median CPB 90-96 min; median clamp 68-72 min; mortality 1.9% | https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/ | A |
| 4 | 17,907 isolated primary MV operations in 2016; repair rate 65.6%; DLP repair 82.5%; mortality 1.1% repair vs 3.7% replacement | https://pubmed.ncbi.nlm.nih.gov/30032907/ | A |
| 5 | ACT > 480 s is reasonable before/during CPB; > 400 s for maximal-activation devices | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | A |
| 6 | Heparin bolus ~300 IU/kg; 6 of 100 had ACT < 350 s after 300 IU/kg | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | A |
| 7 | Protamine:heparin ratio should be kept below 1.0 (2024) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 8 | Protamine ratio limited to < 2.6 mg per 100 U heparin (IIa C) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | A |
| 9 | Pump flow 2.2-2.8 L/min/m²; transfuse if Hb < 6.0 g/dL; HCT 21-24% ok if DO2 > 273 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 10 | Systolic pressure kept < 100 mmHg during aortic cannulation | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 11 | Arterial outlet < 37 °C; gradient ≤ 10 °C; rewarming ≤ 0.5 °C/min with ≤ 4 °C gradient when ≥ 30 °C | https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211 | A |
| 12 | Antegrade cardioplegia 60-100 mmHg; retrograde 200-400 mL/min at CS 30-50 mmHg; cold intermittent every 20-30 min | https://academic.oup.com/ejcts/article/67/2/ezae354/8011475 | A |
| 13 | Buckberg 4:1 at 4 °C, maintenance every 15-20 min, hot shot ~500 mL at 37 °C; del Nido 20 mL/kg max 1000 mL | https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478 | A |
| 14 | TTFM predictors: Qm > 15 mL/min, PI < 5, DF > 50%, SRF < 4%; stricter: Qm > 20, PI < 3, SRF < 3% | https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563 | A |
| 15 | 2018 ESC/EACTS: graft flow measurement IIa B; skeletonization I B; RA over SVG for high-grade stenosis I B; EVH IIa A; no-touch IIa B | https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began | B |
| 16 | 2021 ACC/AHA/SCAI: new class 1 for radial artery over SVG for the next most important non-LAD target | https://www.acc.org/Latest-in-Cardiology/Articles/2022/10/31/13/02/Key-Takeaways-From-the-2021-Coronary-Revascularization-Guidelines | B |
| 17 | REGROUP: EVH vs open no MACE difference (HR 1.12); leg infection 3.1% vs 1.4% | https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018 | B |
| 18 | Partial vs single clamp stroke 1.73% vs 1.8% (p = 0.92) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/ | A |
| 19 | Open-chest defibrillation optimal initial energy 10-30 J | https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868 | A |
| 20 | On-pump CABG medians: skin-to-skin 240 min, CPB 112 min, clamp 65 min, 3 grafts | https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/ | A |
| 21 | Multicentre CABG means: clamp 58.2 min, CPB 76.8 min | https://pmc.ncbi.nlm.nih.gov/articles/PMC10903005 | A |
| 22 | SAVR clamp 50.5 min; suturing 32.3% and tying 18.5% of clamp time; 15 sutures mean | https://smw.ch/index.php/smw/article/download/2329/3539/10387 | A |
| 23 | ≤ 8 paired sternal wire points linked to more DSWI than ≥ 9 (p = 0.002); DSWI 1.5% | https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758 | A |
| 24 | Structured protocol around 8 CPB critical events cut breakdowns 11.5 -> 7.3 per case | https://pubmed.ncbi.nlm.nih.gov/20106395/ | A |
| 25 | Perfusionist shall use a checklist for each CPB; closed-loop communication guideline | https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf | A |
| 26 | Post-cardiac-surgery VF arrest: 3 sequential shocks, then resternotomy within 5 min | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 27 | PAC: Class I in cardiogenic shock, IIa in acute instability, IIb in stable patients (2011 ACCF/AHA) | https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_pulmonary_artery_catheterization | B |
| 28 | Mitral repair techniques in STS: annuloplasty 94.3%, resection 46.5%, artificial chords 22.7% | https://pubmed.ncbi.nlm.nih.gov/30032907/ | A |

---

## Sources

1. Iribarne A, et al. The STS Adult Cardiac Surgery Database: 2024 Update on National Trends and Outcomes. Ann Thorac Surg 2025 - https://pubmed.ncbi.nlm.nih.gov/40127833/ - database size and coverage.
2. STS Adult Cardiac Surgery Database: 2026 Update on Outcomes and Research. Ann Thorac Surg 2026 - https://doi.org/10.1016/j.athoracsur.2026.05.024 - > 8.6 million operations (abstract only).
3. Anaortic off-pump vs conventional CABG (cites STS 2024 update) - https://pmc.ncbi.nlm.nih.gov/articles/PMC13555479/ - 2023 isolated CABG count, off-pump share, multi-arterial share.
4. STS press release, 31 Jan 2026, off-pump CABG study - https://www.sts.org/press-releases/late-breaking-sts-study-finds-pump-cabg-experienced-surgeons-reduces-perioperative-complications - off-pump vs on-pump cohort.
5. Medscape, Off-pump beats on-pump CABG in short-term outcomes (2026) - https://www.medscape.com/viewarticle/pump-beats-pump-cabg-short-term-outcomes-2026a10006g3 - mortality and incomplete revascularization numbers (snippet only).
6. Women and isolated SAVR, 178,014 STS patients. Catheter Cardiovasc Interv 2025 - https://pmc.ncbi.nlm.nih.gov/articles/PMC12617330/ - SAVR volume, CPB and clamp medians, mortality.
7. Gammie JS, et al. Isolated Mitral Valve Surgery: STS ACSD Analysis. Ann Thorac Surg 2018 - https://pubmed.ncbi.nlm.nih.gov/30032907/ - mitral volume, repair rate, techniques, mortality.
8. STS ACSD 2023 Update on Procedure Data and Research - https://www.annalsthoracicsurgery.org/article/S0003-4975(23)01219-5/fulltext - AVR and MV volume trends (snippet only).
9. Wahba A, Kunst G, De Somer F, et al. 2024 EACTS/EACTAIC/EBCP Guidelines on cardiopulmonary bypass in adult cardiac surgery. ICVTS 2025;40(2):ivaf002 - https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ (also EJCTS https://academic.oup.com/ejcts/article/67/2/ezae354/8011475) - ACT, flow, DO2, Hb, cannulation pressure, cardioplegia, protamine, weaning checklist, CO2, adverse events.
10. Puis L, et al. 2019 EACTS/EACTA/EBCP guidelines on CPB. ICVTS 2020 - https://pmc.ncbi.nlm.nih.gov/articles/PMC10634377 - heparin 300-500 U/kg, ACT ranges.
11. Engelman R, et al. STS/SCA/AmSECT Clinical Practice Guidelines for CPB - Temperature Management. 2015 - https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211 - temperature rules.
12. Shore-Lesserson L, et al. STS/SCA/AmSECT Clinical Practice Guidelines: Anticoagulation during CPB. Ann Thorac Surg 2018;105:650-62 - https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 - heparin, ACT, protamine, HIT.
13. AmSECT Standards and Guidelines for Perfusion Practice, 2023 update - https://anzcp.org/wp-content/uploads/2024/06/AmSECT_Perfusion_SG_2023-Ratified-021023_Digital-edition.pdf - communication, checklists, anticoagulation standard, Appendix F checklist.
14. Wadhera RK, et al. Is the "sterile cockpit" concept applicable to cardiovascular surgery? J Thorac Cardiovasc Surg 2010;139:312-9 - https://pubmed.ncbi.nlm.nih.gov/20106395/ - 8 critical events, breakdowns 11.5 -> 7.3.
15. Fann JI, et al. Human Factors and Human Nature in Cardiothoracic Surgery. Ann Thorac Surg 2016 - https://www.sts.org/sites/default/files/documents/patient_safety/HumanNatureinCTSurgery.pdf - communication as root cause, checklists.
16. Wahr JA, et al. Patient Safety in the Cardiac Operating Room: Human Factors and Teamwork. AHA Scientific Statement. Circulation 2013 - https://pubmed.ncbi.nlm.nih.gov/23918255/ - teamwork and briefings.
17. WHO Surgical Safety Checklist (2009) tools page - https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources - 19 items, 3 phases; checklist PDF https://iris.who.int/bitstream/handle/10665/44186/9789241598590_eng_Checklist.pdf
18. Rance G, et al. Ventilator-heart lung machine communication bridge. J Extra Corpor Technol 2019;51:38 - https://ject.edpsciences.org/articles/ject/abs/2019/01/ject-51-38/ject-51-38.html - ventilator-off weaning error (snippet only).
19. Use of del Nido Cardioplegia for Adult Cardiac Surgery at the Cleveland Clinic. J Extra Corpor Technol 2014;46:317-23 - https://pmc.ncbi.nlm.nih.gov/articles/PMC4557478 - Buckberg and del Nido details.
20. Re-dosing of del Nido cardioplegia in adult surgery - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8972223/ - adult fixed-volume protocol (snippet only).
21. Takami Y, et al. FFT analysis of intraoperative TTFM during CABG. J Cardiothorac Surg 2024;19:635 - https://pmc.ncbi.nlm.nih.gov/articles/PMC11583563 - TTFM cut-offs.
22. Peroperative epicardial ultrasonography of distal CABG anastomoses: feasibility study. J Cardiothorac Surg 2020 - https://pmc.ncbi.nlm.nih.gov/articles/PMC6950894/ - CABG skin-to-skin, CPB, clamp, grafts; TTFM suspicion thresholds.
23. Difference Between CPB Time and Cross-Clamp Time (REPLICCAR II). Braz J Cardiovasc Surg 2024 - https://pmc.ncbi.nlm.nih.gov/articles/PMC10903005 - multicentre CABG times and outcomes.
24. Langhammer B, et al. Procedural aspects of SAVR - a process analysis. Swiss Med Wkly 2017;147:w14464 (CC BY-NC-ND 4.0) - https://smw.ch/index.php/smw/article/download/2329/3539/10387 - SAVR sub-step times, suture counts.
25. Uyar IS, et al. Single vs partial aortic clamping and stroke. Cardiovasc J Afr 2013;24:213-7 - https://pmc.ncbi.nlm.nih.gov/articles/PMC3767939/ - stroke rates, technique details.
26. Mayo Clinic: On-pump CABG, one cross-clamp vs two - https://mayoclinic.elsevierpure.com/en/publications/on-pump-coronary-artery-bypass-graft-operation-is-one-crossclamp- - stroke 1.2% vs 1.5% (snippet only).
27. Sousa-Uva M, et al. Radial artery as a conduit for CABG: a state-of-the-art primer. Eur J Cardiothorac Surg 2018;54:971-6 - https://academic.oup.com/ejcts/article/54/6/971/5146781 - RA indications, harvest, meta-analysis, 2018 ESC/EACTS RA class.
28. The 2010-2014-2018 trilogy of ESC/EACTS guidelines (commentary). EuroIntervention - https://eurointervention.pcronline.com/article/the-2010-2014-2018-trilogy-of-esceacts-guidelines-on-myocardial-revascularisation-we-cannot-jump-three-steps-this-way-and-then-return-to-where-we-began - 2018 technical recommendations and classes.
29. ACC: Key Takeaways From the 2021 Coronary Revascularization Guidelines - https://www.acc.org/Latest-in-Cardiology/Articles/2022/10/31/13/02/Key-Takeaways-From-the-2021-Coronary-Revascularization-Guidelines - LIMA-LAD, RA class 1, BIMA 2a.
30. ACC: REGROUP trial summary - https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018 - EVH vs open vein harvest.
31. Gaudino M, et al. Skeletonized vs pedicled ITA, ART post hoc. JAMA Cardiol 2021 - https://jamanetwork.com/journals/jamacardiology/fullarticle/2784330 - MACE HR 1.25; surgeon effect (snippet only).
32. No-touch vein harvest meta-analysis of RCTs - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11638440/ - patency 83% vs 64% at 16 years; RR 0.70 (snippet only).
33. WikiDoc reproductions of 2011 ACCF/AHA CABG guideline: PAC https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_pulmonary_artery_catheterization and TEE https://wikidoc.org/index.php/Coronary_artery_bypass_surgery_TEE - PAC and TEE recommendation classes.
34. ASE comprehensive TEE guideline page - https://www.asecho.org/guideline/comprehensive-tee/ - 28-view exam (snippet only).
35. Combination of internal and external defibrillation during heart surgery. Indian J Thorac Cardiovasc Surg 2019 - https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868 - 10-30 J; paddle 5 cm; timing after de-airing and > 30 °C.
36. STS Expert Consensus for Resuscitation of Patients Who Arrest After Cardiac Surgery. Ann Thorac Surg 2017;103:1005-20 - https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf - 3 shocks, resternotomy within 5 min, pacing.
37. CALS-ANZ guidelines on cardiothoracic advanced life support. Crit Care Resusc 2022 - https://pmc.ncbi.nlm.nih.gov/articles/PMC10692601/ - internal 20 J, DOO pacing.
38. Shaikhrezai K, et al. Number of sternal wires and deep sternal wound infection. ICVTS 2012 - https://pmc.ncbi.nlm.nih.gov/articles/PMC3397758 - DSWI 1.5%; ≥ 9 paired fixation points.
39. Active clearance vs conventional chest tubes RCT. J Cardiothorac Surg 2021 - https://link.springer.com/10.1186/s13019-021-01414-0 - 28F mediastinal device (snippet only).
40. Temporary epicardial pacing wires post-cardiac surgery: literature review (2022) - https://www.springermedizin.de/de/temporary-epicardial-pacing-wires-post-cardiac-surgery-a-literat/23121200 - wire placement (snippet only).
41. LITFL: Temporary epicardial cardiac pacing - https://litfl.com/temporary-epicardial-cardiac-pacing/ - output at 2x threshold (C).
42. Perier P, et al. Minimally invasive repair of posterior leaflet prolapse, "respect" approach. Ann Cardiothorac Surg 2013;2:833-8 - https://pmc.ncbi.nlm.nih.gov/articles/PMC3857044 - neochords, ring, saline test, cannula sizes.
43. Ogden SR, et al. Developing a checklist (separation from CPB) via modified Delphi. J Cardiothorac Vasc Anesth 2016 - https://pubmed.ncbi.nlm.nih.gov/27256448/ - 10-item checklist.
44. Checklist usage decreases critical task omissions when separating from simulated CPB (2014) - https://pubmed.ncbi.nlm.nih.gov/25277642/ - 9-item checklist, 5 of 9 improved.
45. Step-by-Step Minimally Invasive AVR: the RAT Approach. Braz J Cardiovasc Surg 2021 - https://pmc.ncbi.nlm.nih.gov/articles/PMC8357396 - two-layer aortotomy closure, 36 °C, LV vent.
46. Distal anastomosis technique (7-0/8-0, arteriotomy 20% shorter than bevel) - https://pmc.ncbi.nlm.nih.gov/articles/PMC5147479 - (snippet only).
47. MT Samples: Coronary artery bypass grafting sample report - https://mtsamples.blogspot.com/2008/09/14-coronary-artery-bypass-grafting.html - realistic op-note sequence (C).
48. Op note template: CABG - https://opnote-site.pages.dev/cardiac/coronary-artery-bypass/ - template sequence (C).
49. Stryker System 8 Sternum Saw IFU (Sept 2019) - https://bioclinicalservices.com.au/stryker/clinical/system-8-sternum-saw-instructions-for-use-rev-aa-sept-2019 - blade guard rule (snippet, B).
50. NICE MTG8 VeriQ assessment overview - https://www.nice.org.uk/guidance/mtg8/documents/veriq-assessment-report-overview2 - TTFM device outputs (snippet, B).
51. JA Clinical Reports 2023 case: LV vent via right superior pulmonary vein - https://jaclinicalreports.springeropen.com/articles/10.1186/s40981-023-00608-w - vent route and malposition (snippet).
52. Ranucci M, et al. Systemic arterial pressure management on CPB (editorial) - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9918189/ - 2019 guideline MAP 50-80 mmHg Class I A (snippet).
53. Aga Khan University CPB initiation protocol - https://www.aku.edu/mcpk/anaes/Documents/Cardiopulmonary%20Bypass%20(CPB)%20lnitiation%20And%20Maintenance.pdf - full flow then stop ventilation (snippet only; scanned PDF unreadable).
54. Auckland University IV cannulation teaching page - https://flexiblelearning.auckland.ac.nz/cyberiv/22.html - French to mm conversion (B).

Note: one host needed for a Stanford cardiac anaesthesia guide (cvanes.stanford.edu) was not reachable from this session; its claims (K+ > 4 mmol/L, flow index 2.2-2.4) are used only as snippets marked (C).

---

## Summary

**Key findings**

1. On-pump isolated CABG is the right v1. It is by far the most common adult heart operation in the STS database (161,907 in 2023; 88.5% on-pump) and it contains every core system later procedures need.
2. A full, ordered CABG step list from room entry to ICU is now mapped (Phases A-G, about 45 steps) with roles, tools, sutures, success criteria and typical failures.
3. Hard numbers exist for the parts that matter most to realism: heparin ~300 IU/kg and ACT > 480 s; flow 2.2-2.8 L/min/m²; DO2 > ~270-300; Hb trigger 6.0 g/dL; temperature rules (< 37 °C outlet, ≤ 10 °C gradient, ≤ 0.5 °C/min); cardioplegia pressures, flows and intervals; protamine ratio ≤ 1.0; internal defibrillation 10-30 J.
4. Real timings: 3-graft CABG skin-to-skin ~240 min, CPB ~77-112 min, clamp ~58-65 min. SAVR clamp ~44-72 min with a measured sub-step breakdown.
5. Communication is a measurable safety factor: structured call-outs around critical CPB events cut breakdowns by about a third; checklists are a perfusion standard.
6. SAVR reuses most of the pipeline and has excellent timing data. Mitral repair adds new anatomy, bicaval cannulation, neochords/rings, saline test and TEE grading.

**Recommendations**

1. Build v1 as a 3-graft on-pump CABG with two cardioplegia modes, TTFM-based graft scoring, and a closed-loop call-out system.
2. Put hard gates on safety-critical steps (ACT before bypass; ventilator on before weaning; suckers off before protamine).
3. Store all numeric targets in one data file with the source URL next to each value, so they can be tuned and audited.
4. Plan SAVR as v2 (largest reuse), mitral repair as v3, off-pump as a CABG "hard mode".
5. Use the debrief screen to compare the player's clamp time, CPB time and errors with the real ranges in Section 6.

**Open questions**

1. Exact cannula sizes (aortic and two-stage venous) were not verified on manufacturer pages; need IFU or catalogue access.
2. Electrocautery power settings for sternotomy and LIMA takedown are UNVERIFIED.
3. Exact distal arteriotomy length (4-6 mm teaching vs 3-4 mm patent text) and aortic punch sizes (4.0-4.8 mm) lack an A-grade source.
4. Weaning numeric thresholds (core temperature, K+) come from weak sources; the 2024 EACTS supplementary weaning checklist should be read directly.
5. The 2024 ESC chronic coronary syndrome guideline may have replaced some 2018 ESC/EACTS CABG technique recommendations; not confirmed.
6. Current annual counts for isolated SAVR and MV repair (2023-2025) were not found as exact numbers; only derived averages and trends.
7. A sternotomy-based mitral repair timing source (CPB and clamp) was not found; only robotic/minimally invasive figures.
