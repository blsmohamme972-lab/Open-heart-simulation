# Research 08: Patient cases, complications and crisis management

> **Purpose.** Give the plan an evidence base for four things: (1) a library of realistic CABG patients and anatomical variants, (2) intraoperative complications that can run as game events, (3) crisis protocols, checklists and team communication, and (4) a post-operative outcome model that turns what happened in the operating room into a plausible result.
>
> **Researched 2026-11-03 (re-do, fresh searches).** Older plan reports were not read. Every number has a link next to it. Claims marked "(uncertain)" or "(uncertain - snippet only)" could not be confirmed on the full source text. Values marked "(design)" are game-tuning suggestions, not clinical facts.
>
> **Disclaimer.** This is research for a personal, non-commercial, educational game. It is **not clinical guidance**, not a certified medical device, and must never be used to treat a patient. Doses and thresholds are quoted only so the simulation behaves plausibly. Real practice differs between hospitals and changes over time.

**Abbreviations (defined once).** ACT = activated clotting time. AT = antithrombin (AT III). CABG = coronary artery bypass grafting. CALS = Cardiac (Surgical) Advanced Life Support. CPB = cardiopulmonary bypass. CLD = chronic lung disease. DO2 = oxygen delivery. DSWI = deep sternal wound infection. ECLS = extracorporeal life support. ECMO = extracorporeal membrane oxygenation. EF = left ventricular ejection fraction. HCT = haematocrit. HIT = heparin-induced thrombocytopenia. IABP = intra-aortic balloon pump. IMLAD = intramyocardial left anterior descending artery. LIMA = left internal mammary artery. MAP = mean arterial pressure. MCS = mechanical circulatory support. NIRS = near-infrared spectroscopy (cerebral oximetry). PCI = percutaneous coronary intervention. PC-ECLS = post-cardiotomy ECLS. PROM = predicted risk of mortality. RBC = red blood cells. RRT = renal replacement therapy. RV/LV = right/left ventricle. SVR = systemic vascular resistance. TEE (TOE) = transoesophageal echocardiography. TTFM = transit-time flow measurement. VAD = ventricular assist device. VF/VT = ventricular fibrillation/tachycardia.

Evidence grades: **A** = guideline, peer-reviewed paper, official docs/licence page. **B** = reputable secondary (review summary, society education page, vendor page). **C** = weak (blog, forum, snippet).

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Outcome baselines | Use the STS 2018 isolated-CABG development-sample rates as the "average patient" baseline: operative mortality 2.4%, stroke 1.3%, renal failure 2.2%, prolonged ventilation 9.3%, reoperation 2.4%, DSWI 0.3%, composite morbidity/mortality 15.0%, prolonged stay 5.0%. | [STS 2018 Part 2, Table 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf) (A) |
| Patient generator | Build patients from the STS candidate predictor list (age, sex, BMI, BSA, EF, dialysis/creatinine, diabetes and control method, CLD, status, PCI history/timing, previous CABG, shock/ECMO, IABP, left main, etc.). Age and sex are the only required inputs; blanks are imputed. Calibrate each authored profile by hand with the official STS calculator. | [STS 2018 Part 2, Table 3](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf) (A); [STS calculator guide](https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf) (A) |
| Anatomy variants | Roll variants with published frequencies: right dominance 72-90%, left 8-33%, co-dominance 3-7%; IMLAD 11.5-21.7%; porcelain aorta 2-9.3% of elective CABG; major re-entry injury at redo sternotomy 2.8%. | see Section 1.4 |
| Event library | Ship 20 intraoperative events (Section 2). Each event has cause, incidence, monitor/field signs, ordered steps, a clock, and a mishandling outcome. | Sections 2.1-2.20 |
| Arrest protocol (ICU or after chest closure) | Follow STS 2017 / ERC 2021: up to 3 shocks within about 1 minute, pacing DDD 80-100/min at max output, no routine epinephrine, amiodarone 300 mg after 3 failed shocks, emergency resternotomy within 5 minutes, six team roles. | [STS 2017 consensus](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf) (A); [ERC 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767) (A) |
| Anticoagulation rules | ACT above 480 s on CPB (above 400 s with maximally activated tests). Heparin resistance = more than 500 U/kg needed to reach ACT 480 s. HIT: delay elective surgery; urgent case uses bivalirudin 1 mg/kg + 2.5 mg/kg/h + 50 mg in prime, ACT about 2.5x baseline (>300 s). | [STS/SCA/AmSECT 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf) (A); [Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/) (B); [EACTS 2024 CPB](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| Temperature rules | Arterial outlet below 37 °C; outlet-venous gradient at most 10 °C, at most 4 °C when outlet is 30 °C or more; rewarm at most 0.5 °C/min above 30 °C. | [STS/SCA/AmSECT 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/) (A) |
| Perfusion targets | DO2 at least 280 mL/min/m2 (Class I, A); transfuse on CPB if HCT below 18% (Hb 6.0 g/dL); not if HCT above 24% with adequate DO2; keep systolic below 100 mmHg during aortic cannulation. | [EACTS 2024 CPB](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| Checklists | Pre-CPB checklist (Class I) and pre-weaning checklist (Class I, C) are guideline-backed. Use five cardiac crisis checklists as event cards: CPB failure, systemic air embolism, venous air lock, protamine reaction, heparin resistance. | [EACTS 2024 CPB](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A); [Tarola 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745) (A) |
| Failure to wean | Forcing weaning with high-dose drugs is Class III (harm). Short-term MCS is Class IIa. Start ECLS before lactate reaches 4 mmol/L. PC-ECLS use 0.3-3.6%; survival to discharge about 34%. | [EACTS 2024 CPB](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A); [PC-ECLS consensus 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf) (A) |
| Outcome model | Logistic model: patient baseline log-odds + intraoperative modifiers (CPB time OR 1.57 per 30 min for death; RBC OR 1.77 mortality, 2.06 renal failure; post-CPB MAP below 65 mmHg OR 1.12 per 10 min for RRT; reoperation for bleeding doubles 30-day mortality 2.2% to 4.8%) with a shrinkage factor to avoid double counting. | Section 5 |
| Licences | Re-author all protocol text in your own words. EACTS 2024 CPB guideline is CC BY-NC-ND 4.0 (no derivatives). Stanford Emergency Manual is CC BY-NC-ND (version UNVERIFIED). Ariadne crisis checklists CC BY-NC-SA 4.0 is UNVERIFIED. STS documents carry no open licence. Pulse Physiology Engine 4.4.0 is Apache-2.0. | Section 3.6 |

---

## 1. Patient case library

### 1.1 Baseline outcome rates for isolated CABG (STS)

The STS 2018 models were built on 439,092 isolated CABG records from 2011-2014 and validated on 2014-2016 data ([STS 2018 Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf); [Part 1 summary](https://dihi.org/outcome/the-society-of-thoracic-surgeons-2018-adult-cardiac-surgery-risk-models-part-1-background-design-considerations-and-model-development/)). The table gives the observed event rates in the CABG development sample ([Part 2, Table 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf)).

| Endpoint (STS definition) | Isolated CABG rate | C-statistic of 2018 model |
|---|---|---|
| Operative mortality (in-hospital, or within 30 days) | 2.4% (8,852 / 373,683) | 0.804 |
| Stroke (neurologic deficit more than 24 h) | 1.3% | 0.697 |
| Renal failure (new dialysis or RIFLE criteria) | 2.2% | 0.826 |
| Prolonged ventilation or reintubation (more than 24 h) | 9.3% | 0.772 |
| Reoperation (bleeding, tamponade or any cardiac reason) | 2.4% | 0.621 |
| Composite major morbidity or mortality | 15.0% | 0.738 |
| Prolonged length of stay (more than 14 days) | 5.0% | 0.777 |
| Short length of stay (less than 6 days, alive) | 48.3% | 0.716 |
| DSWI / mediastinitis | 0.3% | 0.681 |

Source for all rows: [STS 2018 Part 2, Tables 2 and 4 and endpoint definitions](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf) (A).

- More recent STS harvest tables list isolated CABG operative mortality of about 2.1-2.2% for 2024, and values shift between harvests ([ACSD 24H3](https://sts.org/sites/default/files/2024-11/ACSD%2024H3%20Multipliers%20and%20Annual%20Rates.pdf), [ACSD 24H4](https://sts.org/sites/default/files/2025-03/ACSD%2024H4%20Multipliers%20and%20Annual%20Rates.pdf)) (uncertain - snippet only).
- The STS Adult Cardiac Surgery Database holds more than 8.3 million procedures from more than 1,000 institutions and covers more than 97% of US cardiac surgery ([STS ACSD 2024 update, PubMed 40127833](https://pubmed.ncbi.nlm.nih.gov/40127833/)) (A).
- Discrimination for reoperation (c = 0.621) and stroke (c = 0.697) is weak ([Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf)). **Game rule (design):** these two endpoints should depend mostly on intraoperative events (bleeding control, aortic handling), not on the patient profile.

### 1.2 STS risk-model variables the generator should carry

The 2018 models started from about 65 candidate predictors and added about 40 new variables compared with the 2008 models ([Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf); [calculator guide](https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf)). Only age and sex are required; blank fields are imputed ([calculator guide](https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf)). BMI has a U-shaped relation with mortality, so the model uses linear and quadratic BMI terms plus BSA ([Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf)).

Candidate predictors from [Part 2, Table 3](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf), grouped for a game data schema:

| Group | Variables |
|---|---|
| Demographics | Age, sex, race/ethnicity, BMI, BSA, payer |
| Kidney / labs | Dialysis or creatinine, haematocrit, white cell count, platelet count |
| Metabolic / lifestyle | Diabetes and control method, hypertension, recent smoker, alcohol, illicit drugs, family history of CAD, sleep apnoea, home oxygen, liver disease, cancer within 5 years |
| Lung | Chronic lung disease (severity), recent pneumonia, mediastinal radiation |
| Cardiac state | EF, heart failure class and timing, MI history and timing, cardiac presentation, arrhythmia type, syncope, shock/ECMO/catheter assist device, preoperative IABP, inotropes within 48 h |
| Coronary anatomy | Number of diseased vessels, left main disease, proximal LAD disease |
| Valves | Aortic/mitral stenosis, aortic/mitral/tricuspid insufficiency, endocarditis |
| Vascular / neuro | PAD, cerebrovascular disease/CVA/TIA, carotid stenosis, previous carotid surgery, unresponsive neurologic state |
| Drugs | ADP-receptor inhibitor and stop timing, GP IIb/IIIa within 24 h, steroids within 24 h, immunosuppression within 30 days, ACE/ARB within 48 h in non-elective cases |
| History | Previous CABG, previous valve procedures, number of previous cardiovascular operations, previous ICD, PCI history and timing |
| Urgency | Status (elective, urgent, emergent, emergent salvage - categories as used by STS; exact definitions not re-checked here (uncertain)) |

**Calibration note.** The official isolated-CABG calculator host (cabgshortandlongtermcalc.research.sts.org) could not be reached from this research session because of network restrictions. The owner should enter each profile by hand and store the returned values. STS asks users to accept terms and conditions before use ([calculator guide](https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf)); those terms were not read (UNVERIFIED). Do not scrape the calculator (design).

**Alternative open formula.** EuroSCORE II publishes logistic coefficients (Nashef et al., Eur J Cardiothorac Surg 2012;41:734-45) ([Wikipedia summary](https://en.wikipedia.org/wiki/EuroSCORE)) (B). The coefficients themselves were **not** verified in this pass (UNVERIFIED). Verify them against the original paper before coding.

### 1.3 Authored profile library (12 cases)

"Target band" is a **design target** for difficulty, not an STS output. Bands: very low below 1%, low 1-2%, moderate 2-4%, high 4-8%, very high above 8% (design). Published risk bands differ by study (for example, one AVR study used below 4% as "low" ([2015 recalibration study](https://scholars.duke.edu/individual/pub1082804)) (uncertain - snippet only)), so the owner must replace bands with real calculator values.

| ID | Profile (age/sex, BMI, EF) | Key STS variables | Status | Target band (design) | What it teaches |
|---|---|---|---|---|---|
| P01 | 58 M, BMI 27, EF 60% | 3-vessel incl. proximal LAD, no diabetes, creatinine normal, no CLD, no PCI | Elective | Very low | Clean standard case; tutorial |
| P02 | 66 M, BMI 31, EF 50% | Diabetes on oral drugs, hypertension, PCI more than 1 year ago, left main | Elective | Low | Typical patient; diabetes raises reoperation-for-bleeding odds (OR 1.35, [Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)) |
| P03 | 76 F, BMI 24, EF 45% | Insulin-treated diabetes, creatinine about 1.6 mg/dL (CKD), small diffuse targets, poor saphenous veins | Elective | Moderate | Conduit choice; AKI risk; haemodilution |
| P04 | 70 M, BMI 29, EF 35% | NSTEMI 3 days ago, moderate CLD, current smoker, ADP inhibitor stopped 2 days ago | Urgent | Moderate to high | Bleeding risk; prolonged ventilation |
| P05 | 63 M, BMI 28, EF 40% | Dialysis, insulin diabetes, PAD | Urgent | High | Hyperkalaemia after cardioplegia; fluid limits |
| P06 | 68 M, BMI 26, EF 20-25% | Cardiogenic shock, preoperative IABP, inotropes within 48 h, left main | Emergent | Very high | Failure to wean; ECLS decision |
| P07 | 72 M, BMI 28, EF 40% | Previous CABG with patent LIMA-LAD, prior PCI | Elective | High | Redo sternotomy, re-entry injury |
| P08 | 79 F, BMI 23, EF 55% | Prior TIA, carotid stenosis, porcelain aorta on CT | Elective | Moderate | No-touch / alternative cannulation; stroke |
| P09 | 55 F, BMI 42, EF 55% | Insulin diabetes, sleep apnoea, mild CLD | Elective | Low | DSWI and ventilation risk; the multi-arterial survival advantage was not seen at BMI 40 or more ([Sabik, STS 2024 news](https://cardiovascularnews.com/multi-arterial-grafting-sts-2024)) (uncertain - snippet only) |
| P10 | 47 M, BMI 25, EF 55% | Familial hypercholesterolaemia, left-dominant system, IMLAD | Elective | Very low | Target finding; RV-entry hazard |
| P11 | 64 M, BMI 30, EF 45% | Heparin infusion for ACS, platelet fall more than 50% on day 6 | Urgent | Moderate | Suspected HIT pathway |
| P12 | 69 M, BMI 27, EF 25% | Pulmonary hypertension, moderate TR, NYHA III | Elective | High | RV failure at weaning |

### 1.4 Anatomical and technical variants

| Variant | Frequency | Game effect | Source |
|---|---|---|---|
| Coronary dominance | Right 72-90%, left 8-33%, co-dominant 3-7% (pooled range); CT series of 1,000: right 84.9%, left 11.3%, co-dominant 3.8% | Changes which territory the circumflex or RCA graft supplies; left dominance makes circumflex grafts more critical (design) | [Review, PMC4505791](https://pmc.ncbi.nlm.nih.gov/articles/PMC4505791) (B, uncertain - snippet only); [PAFMJ CT study](https://www.pafmj.org/PAFMJ/article/view/4311) (B) |
| Intramyocardial LAD | 21.7% of 1,349 CABG reports (3.8% of these ran into the septum); 11.5% in a 349-patient series | Exposure takes longer; hazards are injury to diagonals, LAD, and entry into the RV cavity | [Vanker 2014, S Afr J Surg](https://ajol.info/index.php/sajs/article/view/106808) (B); [Alagha 2023](https://turkiyeklinikleri.com/article/en-the-intramyocardial-left-anterior-descending-artery-prevalence-early-and-mid-term-surgical-outcomes-after-coronary-artery-bypass-procedures-a-retrospective-single-center-study-105593.html) (B); [CTSNet technique](https://www.ctsnet.org/article-video/surgical-technique-exposing-intramyocardial-left-anterior-descending-artery/) (B) |
| Porcelain / unclampable aorta | 2-9.3% of elective CABG (one review); 0.4-5.4% (another); ascending calcification about 14% | Blocks standard cannulation and clamping; offers no-touch strategy. Partial clamping stroke 2.2% vs no-touch 0.2% in one series; meta-analysis RR 0.41 for stroke with no-touch | [WJC 2021 review](https://www.wjgnet.com/1949-8462/full/v13/i8/309.htm) (B, uncertain - snippet only); [PMC4693948](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4693948/) (B) |
| Ascending aortic atheroma | Moderate-severe atheroma on palpation raised stroke 4-fold (2,108 elective CABG) | Raises stroke odds if clamped at a diseased site (design) | [WJC 2021 review](https://www.wjgnet.com/1949-8462/full/v13/i8/309.htm) (uncertain - snippet only) |
| Redo sternotomy | Major re-entry/dissection injury 2.8% and operative mortality 3.5% in 6,627 re-sternotomies (Cleveland Clinic); older series 5-10% injury, with mortality 18.6-26% after injury vs 6.5-9% without | Requires CT review, slower opening, possible peripheral cannulation first (design) | [Modern reoperative practice, PubMed 33757681](https://pubmed.ncbi.nlm.nih.gov/33757681/) (A, snippet); [MDPI review](https://www.mdpi.com/2077-0383/14/4/1251) (B) |
| Patent LIMA graft at redo | No incidence found in this pass | Injury causes acute anterior ischaemia (design) | (uncertain) |
| Small / diffusely diseased targets | No frequency found in this pass | Lower TTFM flows; higher graft-failure probability (design) | (uncertain) |
| Poor veins (varicose, stripped, small) | No frequency found in this pass | Forces radial artery or other conduit; longer harvest time (design) | (uncertain) |
| LIMA injury during harvest | No frequency found in this pass | Loss of best conduit; vein to LAD (design) | (uncertain) |

---

## 2. Intraoperative complications as game events

### 2.0 Event schema

Each event in game data should have: `id`, `trigger` (random roll and/or player error), `incidence` (per case, with source), `phase` (pre-CPB, on CPB, cross-clamp, weaning, post-CPB, ICU), `signs` (monitor values, field visuals, perfusion console alarms, TEE findings), `correctSteps` (ordered list with role owner), `clock` (seconds until harm escalates), `outcomeIfMishandled` (modifier for the Section 5 model), and `debrief` text. Overall, CPB-related adverse events are reported at 1 per 138 perfusions (US), 1 per 198 (France) and 1 per 15 (Netherlands); serious injury or death 1:2,500 to 1:1,236; death from CPB incidents 1 in 4,446-4,864 ([EACTS 2024 CPB, sections 4.2 and 12](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A). The most frequently reported events were inadequate ACT, allergic reactions, aortic dissection at the cannulation site, heat-exchanger problems and clot in the circuit ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)).

### 2.1 Surgical bleeding, coagulopathy and reoperation

| Field | Content |
|---|---|
| Cause | Surgical site (85% of documented reoperations: multiple sites 30%, sternum 17%, anastomosis 13%), coagulopathy 16% ([Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)) (A) |
| Incidence | Reoperation for bleeding commonly quoted as 2-6% (Ranucci 2008 abstract, seen only as a search snippet; [PubMed record, identity not confirmed](https://www.pubmed.gov/21640602/)) (uncertain - snippet only); 5.3% of 11,813 elective patients ([Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)); STS "reoperation" 2.4% ([STS Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf)) |
| Risk factors | Diabetes OR 1.35, BMI OR 0.96 per unit, CPB time OR 1.005 per minute ([Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)); CPB time OR 1.1 per 30 min for reoperation for bleeding ([Salis 2008](https://db.cngb.org/search/literature/18948034)) (uncertain - snippet only) |
| Signs | Pooling blood in field, rising suction return, falling HCT and CVP, rising chest-drain output after closure (design values in Section "Game hooks") |
| Correct steps | 1) Find and fix surgical bleeding first. 2) Confirm heparin reversal: protamine-to-heparin ratio below 1.0 ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)), never above 2.6 mg per 100 U ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)). 3) Stop cardiotomy suction when protamine starts ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). 4) Targeted blood products. 5) If ongoing in ICU: re-explore |
| Clock | Bleeding rate drives volume loss each second (design) |
| If mishandled | 30-day mortality 4.8% vs 2.2% without reoperation; 1-year 10.4% vs 4.9%; RBC mean 8.0 vs 1.3 units ([Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)) (A). Other studies: OR 2.62 in 7,381 patients; pooled incidence 4.6% and mortality RR 3.30 in a 2018 meta-analysis ([search record](https://pesquisa.bvsalud.org/bvseps/resource/pt/mdl-28826154)) (uncertain - snippet only). Low-risk CABG needing reoperation OR 4.4 (Moulton, cited by [Qazi](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)) |

**Transfusion rules on CPB** ([EACTS 2024 CPB, Recommendation Table 45](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A): transfuse RBC if HCT is below 18% (Hb 6.0 g/dL) (recommended); do not transfuse if HCT is above 24% and DO2/extraction are adequate. A 2021 STS/SCA/AmSECT/SABM patient blood management update exists (Tibi et al., Ann Thorac Surg 2021;112:981-1004) ([summary](https://medicaldialogues.in/surgery/guidelines/2021-guideline-on-patient-blood-management-in-cardiac-surgery-83469)) (uncertain - snippet only). The 2024 EACTS/EACTAIC patient blood management guideline exists ([EACTS page](https://www.eacts.org/clinical-practice-guideline/2024-eacts-eactaic-guidelines-on-patient-blood-management-in-adult-cardiac-surgery-in-collaboration-with-ebcp)) but its massive-bleeding algorithm (fibrinogen, PCC, viscoelastic thresholds) was **not** read in this pass (UNVERIFIED). A cardiac-specific massive transfusion ratio was not found (UNVERIFIED).

### 2.2 Iatrogenic aortic dissection at cannulation or clamp

| Field | Content |
|---|---|
| Cause | Arterial inflow cannula about 33%, cross-clamp or partial clamp about 29%, proximal vein anastomosis site 14% ([review, Thieme 2019](https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0039-1695729)) (uncertain - snippet only). Cannulating an aneurysmal aorta is a risk factor ([Columbia series](https://vivo.weill.cornell.edu/display/pubid31770775)) (uncertain - snippet only) |
| Incidence | 0.06-0.6% depending on cannulation site ([EACTS 2024 CPB](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A): about 0.06% ascending aorta, 0.6% femoral/iliac, 0.5% axillary/subclavian ([review](https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0039-1695729)) (uncertain - snippet only) |
| Prevention | Keep systolic pressure below 100 mmHg during cannulation ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A) |
| Signs | Sudden loss of radial pressure, sudden drop in NIRS, EEG change; none is specific ([search summary, likely this chapter](https://springerlink.bibliotecabuap.elogim.com/chapter/10.1007/978-3-030-79721-8_9)) (uncertain - snippet only; exact source not confirmed). High arterial line pressure (a correctly sized cannula should stay below 200 mmHg at full flow, [JECT 1982](https://ject.edpsciences.org/articles/ject/pdf/1982/01/ject1982141p309.pdf)) (uncertain - snippet only). TEE: dissection flap and entry tear ([ASE 2020](https://www.asecho.org/wp-content/uploads/2023/03/PIIS0894731720301334.pdf)) (A) |
| Correct steps | Columbia approach: 1) immediate repair, 2) call a second attending surgeon, 3) monitor malperfusion aggressively, 4) secure true-lumen arterial access with systemic cooling, 5) hemiarch or total arch replacement guided by suspected brain malperfusion ([Columbia, 15 cases 2000-2016](https://vivo.weill.cornell.edu/display/pubid31770775)) (uncertain - snippet only) |
| Clock | Seconds to minutes: pumping into a false lumen causes malperfusion (design: 60-120 s before organ damage accrues) |
| If mishandled | Mortality about 30% when found early, more than double if missed until after surgery ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/); [review](https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0039-1695729)). Columbia in-hospital mortality 6.7% with a standard approach (uncertain - snippet only) |

### 2.3 Massive arterial air embolism on CPB

| Field | Content |
|---|---|
| Cause | Empty reservoir (inattention), reversed pump-head tubing or rotation, heart ejecting unexpectedly, inadequate de-airing, deep high-flow suction, defective or detached oxygenator, pressurised cardiotomy reservoir ([Mills & Ochsner 1980](https://pubmed.ncbi.nlm.nih.gov/7431967/)) (A); pulled aortic cannula, cracked circuit ([AmSECT protocol](https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf)) (A); vacuum-assisted venous drainage over-pressure ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| Incidence | 8 in 3,620 CPB operations (about 0.22%) in 1971-1979 ([Mills & Ochsner](https://pubmed.ncbi.nlm.nih.gov/7431967/)); modern rate is lower but not quantified in this pass (uncertain) |
| Signs | Visible air slug in arterial line, bubble detector alarm, sudden NIRS drop; TEE confirms ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| Correct steps (circuit) | 1) Alert surgeon. 2) Stop pump, clamp all lines and shunts, announce "off bypass" loudly, ventilate. 3) Find source (cardioplegia lines, oxygenator exhaust port, arterial filter port, cracked connector). 4) Remove air ("walk out", forward-flush), re-prime, restart with bubble detector on ([AmSECT protocol](https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf)) (A) |
| Correct steps (air reached patient) | 1) Trendelenburg. 2) Someone compresses carotids. 3) Surgeon moves venous cannula into SVC (clamp IVC line if bicaval); de-air venous line. 4) Reconfigure for retrograde perfusion up the SVC. 5) Cool. 6) Retrograde cerebral perfusion 1-2 L/min for 1-2 min with aortic root vent on, or until air stops leaving the aorta. 7) FiO2 100%, normal pCO2. 8) Restore normal circuit and restart CPB with higher flow and pressure. 9) Consider hypothermia for about 45 min, rewarm slowly (gradient below 8 °C), consider mannitol 25 g; hyperbaric oxygen if available ([AmSECT protocol](https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf)) (A) |
| Disagreement | Another quick reference suggests SVC retrograde flow of 300-500 mL/min for about 3 min with CVP below 25 mmHg ([Perfusion.com](https://perfusion.com/quick-reference-massive-air-embolism/)) (C). A 1995 case used 1.5 L/min for 5 min ([PubMed 7561320](https://pubmed.ncbi.nlm.nih.gov/7561320/)) (uncertain - snippet only). Game range: 0.3-2.0 L/min (design) |
| Clock | Countermeasures work only if deployed quickly ([ICVTS 2014](https://academic.oup.com/icvts/article/19/5/875/648359)) (uncertain - snippet only). Design: 30 s to stop pump, 3-5 min to start retrograde flow |
| If mishandled | 13 patients: 4 instant deaths, 3 transient cerebral injury (resolved within 2 months), 6 without sequelae ([Mills & Ochsner](https://pubmed.ncbi.nlm.nih.gov/7431967/)) (A) |

### 2.4 Oxygenator failure

| Field | Content |
|---|---|
| Cause | Gas supply problems (e.g. mis-seated vaporiser) are common; true device failure, plasma leak, clotting, high-pressure excursions ([Willcox 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10487349/)) (B); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Incidence | UK/Ireland emergency changeover 1 per 4,055 cases (1993) and 1 per 4,634 (1997); US surveys 1:56,000 (1980), 1:13,600 (1986), 1:2,700 (1999) ([ANZCP PIRS 2021](https://anzcp.org/wp-content/uploads/reports/2021/PIRS-2021-Coagulation_2_Oxygenator_Changeout.pdf)) (uncertain - snippet only). High-pressure excursions 1.14% (Myers) and 1.8% (37 of 2,024, Hjärpe) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A) |
| Signs | Post-oxygenator PO2 below target despite FiO2 increase; dark arterial blood; rising oxygenator inlet pressure; gas-outlet monitoring helps detect it early ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| Correct steps | 1) Rule out non-device causes: sweep gas source, blender, connections, vaporiser seating; switch to 100% O2 ([Willcox 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10487349/); [JECT 2024 algorithm](https://ject.edpsciences.org/10.1051/ject/2024026)) (uncertain - snippet only for the 2024 table). 2) For high-pressure excursion: heparin, AT, epoprostenol, haemodilution ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). 3) Second perfusionist primes replacement. 4) Change out: classic method interrupts CPB; PRONTO parallel method avoids stopping CPB, estimated under 90 s ([PRONTO via search](https://www.scribd.com/document/701000242/PRONTO-PROCEDURE)) (uncertain - snippet only) |
| Clock | Hypoxaemia every second; design: 2-4 min tolerance at reduced flow and cooling |
| If mishandled | Hypoxic brain injury; or finishing the case with a faulty oxygenator ([Willcox 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10487349/)) |

### 2.5 Pump or power failure

| Field | Content |
|---|---|
| Cause | Pump failure, electrical failure, tubing disconnection ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A) |
| Incidence | Not quantified in this pass (uncertain). Treat as very rare (design: 1 in 5,000 cases) |
| Signs | Arterial flow reads zero, roller stops, console dark, MAP falls to zero on CPB |
| Correct steps | 1) Announce. 2) Hand-crank the arterial pump (hand cranks must be available per checklist). 3) Switch to battery / backup console. 4) Use emergency lighting and backup oxygen cylinder if gas also lost ([AmSECT Perfusion Checklist, "Backup" section](https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf)) (A). A crisis checklist for "CPB failure" exists ([Tarola 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745)) but its steps are not published in the text |
| Clock | Design: hand-crank within 15-30 s |
| If mishandled | Global ischaemia; outcome via Section 5 "low-flow minutes" (design) |

### 2.6 Heparin resistance (AT deficiency)

| Field | Content |
|---|---|
| Definition | More than 500 U/kg heparin needed to reach ACT 480 s; heparin sensitivity index below 1 s/U/kg suggests it ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)) (B) |
| Incidence | 4-26% depending on bolus and ACT target; 30.7% of 287 in one study ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)) |
| Causes | AT deficiency (congenital about 1 in 3,000; acquired from preoperative heparin, liver disease, sepsis, ECMO/IABP), high platelet count, albumin 3.5 g/dL or less (OR 3.17), endocarditis (OR 4.57) ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)) |
| Signs | ACT stays below target after standard bolus of 300-500 U/kg ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)) |
| Correct steps | 1) Extra heparin. 2) AT concentrate (500 IU vials, usually 1-2 vials; mean 1,029 IU or 14.1 IU/kg; formula dose IU = (target % - current %) x kg / 1.4). 3) FFP if AT not available (2 units about 500 IU AT). 4) Rarely accept sub-target ACT ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)). If ACT still inadequate, consider off-pump or MiECC ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). AT concentrate is rated Class I, Level A to reduce plasma use ([2021 PBM update via search](https://medicaldialogues.in/surgery/guidelines/2021-guideline-on-patient-blood-management-in-cardiac-surgery-83469)) (uncertain - snippet only) |
| Targets | ACT above 480 s reasonable on CPB; above 400 s with maximally activated or microcuvette tests (Class IIa, C) ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)) (A) |
| Clock | Blocks "go on bypass" until solved; delay grows in urgent cases (design) |
| If mishandled | Going on CPB with low ACT: circuit clot, thromboembolism ([Butt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/)) |

### 2.7 Heparin-induced thrombocytopenia (HIT)

| Field | Content |
|---|---|
| Incidence | Anti-PF4/heparin antibodies in nearly 50% after CPB, clinical HIT about 3% ([JPMA 2009 review](https://www.archive.jpma.org.pk/PdfDownload/1711)) (C); prospective 581 patients: 0.5% (95% CI 0.1-1.5%) ([PubMed 19793190](https://www.pubmed.gov/19793190/)) (B, snippet) |
| Signs / scoring | Platelet fall more than 50% or thrombosis 5-14 days after heparin exposure should prompt testing (Class IIa, B); functional test (SRA/HIPA) if antibody result is weak (IIa, C) ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)) (A) |
| Correct steps | Elective: delay until functional or antibody assay negative (IIa, C) ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)), typically after about 100 days ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). Urgent: bivalirudin (IIa, B both guidelines): bolus 1 mg/kg, infusion 2.5 mg/kg/h, 50 mg in pump prime, ACT about 2.5x baseline (typically above 300 s), avoid stagnant blood in circuit; argatroban if renal impairment (bolus 0.1 mg/kg, 5-25 up to 40 µg/kg/min, 4 mg in prime, ACT 450-500 s reported) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A). Renal dysfunction + urgent: plasmapheresis or heparin with antiplatelet agent may be considered (IIb, C) ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)) |
| Clock | Decision at pre-op briefing (design) |
| If mishandled | Giving heparin to acute HIT: thrombosis (graft, limb, stroke); bivalirudin with stasis: circuit clot; no reversal agent exists, so more bleeding ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |

### 2.8 Protamine reaction

| Field | Content |
|---|---|
| Incidence | 0.06-10.6% ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) (B); about 11% in one older study; catastrophic about 0.13% (uncertain - snippet only) |
| Types | I: isolated hypotension. II: anaphylactoid/anaphylactic. III: pulmonary hypertension with RV failure ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) |
| Risk factors | NPH insulin, fish allergy, other drug allergies; a negative test dose does not exclude a reaction ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) |
| Dosing rules | About 1 mg per 100 U heparin; ratio below 1.0 recommended ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)); never above 2.6 mg/100 U ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)); no faster than 20 mg/min or the full dose over 10-15 min ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) |
| Signs | Hypotension, bradycardia, rising PA pressure, RV distension on TEE, bronchospasm / high airway pressure |
| Correct steps | 1) Slow or stop protamine. 2) Volume (IV or via aortic cannula). 3) Vasoactive drugs (phenylephrine, norepinephrine, vasopressin, calcium), inotropes (epinephrine, milrinone). 4) Pulmonary vasodilators (inhaled nitric oxide, epoprostenol). 5) Albuterol for bronchospasm. 6) Severe: re-heparinise and return to CPB or start VA-ECMO. Whether to resume reversal has no consensus ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)) (B) |
| Clock | Type III can arrest within minutes (design: 60-180 s) |
| If mishandled | RV failure and arrest; unplanned return to CPB adds CPB minutes to the outcome model (design) |

### 2.9 Vasoplegia

| Field | Content |
|---|---|
| Definition | MAP below 65 mmHg, cardiac index above 2.2 L/min/m2, SVR below 800 dyn·s/cm5, poor response to vasopressors ([ICVTS 2025 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)) (B) |
| Incidence | 5-45% depending on definition ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)) |
| Risk factors | Age, anaemia, renal impairment, preoperative ACE inhibitors / beta-blockers / loop diuretics, long CPB and clamp times, redo, complex surgery; early hypotension at CPB start ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)) |
| Doses | Norepinephrine 0.01-1.0 µg/kg/min; vasopressin 0.01-0.1 U/min; methylene blue 1-2 mg/kg over 15-30 min then 0.25-2 mg/kg/h; hydroxocobalamin 5 g over 15 min (max 10 g); angiotensin II 2-40 ng/kg/min ([same, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)) (B) |
| Correct steps | 1) Volume check. 2) Norepinephrine. 3) Add vasopressin. 4) Rescue: methylene blue or hydroxocobalamin. No standard stepwise protocol exists ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)) |
| Evidence | Methylene blue was the only non-adrenergic agent with lower mortality (RR 0.12, 95% CI 0.02-0.95) in one meta-analysis; vasopressin RR 0.89, angiotensin II RR 0.98 ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/)). Methylene blue risks: serotonergic interaction, haemolysis in G6PD deficiency ([search summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11863290/)) (uncertain - snippet only) |
| If mishandled | Hypotension minutes feed AKI and composite outcomes (Section 5) |

### 2.10 VF after unclamping and failure to defibrillate

| Field | Content |
|---|---|
| Incidence | Reperfusion VF after cross-clamp release 74-96% in CABG (abstract; uncertain - snippet only, [Zenodo PDF](https://zenodo.org/records/2908289/files/154.pdf)); 43-56.9% in a Thai procaine vs lidocaine cardioplegia trial ([Thai J Surg](https://he02.tci-thaijo.org/index.php/ThaiJSurg/article/view/266715)) (B, snippet) |
| Prevention | Lidocaine and/or magnesium before clamp release reduce VF in small trials; magnesium more effective than lidocaine in one; lidocaine linked to more transient AV block ([search summary of Iranian/Egyptian trials](https://search.emarefa.net/en/detail/BIM-252862-the-effect-of-lidocaine-and-magnesium-sulfate-on-prevention-)) (C) |
| Signs | VF on ECG after clamp off; heart visibly fibrillating; LV distends if not vented |
| Correct steps | 1) Internal defibrillation (a Thai trial used 10 J shocks; 15.1-24.4% still in VF after the shock) ([Thai J Surg](https://he02.tci-thaijo.org/index.php/ThaiJSurg/article/view/266715)) (uncertain - snippet only). Standard internal energy is not verified here (UNVERIFIED; commonly quoted 10-20 J). 2) Keep heart decompressed (vent), adequate perfusion pressure. 3) Check K+, Mg, temperature, acid-base (general practice, uncertain). 4) Antiarrhythmic: amiodarone 300 mg or lidocaine 1 mg/kg are the arrest-protocol doses ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) |
| Clock | On full CPB the brain is perfused, so pressure is lower; the cost is myocardial (LV distension, oxygen use) (design) |
| If mishandled | Repeated shocks, LV distension, prolonged CPB (design) |

### 2.11 Failure to wean: LV failure

| Field | Content |
|---|---|
| Definition | Difficult separation = rising inotrope/vasoactive doses needed, first weaning attempt fails, or a device is needed ([EACTS 2024, section 11.2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A) |
| Predictors | Low LVEF, mitral/aortic/tricuspid regurgitation, urgent/emergent surgery, long CPB (Denault); female sex, diastolic dysfunction, CPB time (Bernard) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| Signs | Low MAP and cardiac output, rising LA/PA pressure, global hypokinesis or new regional wall-motion abnormality on TEE ([ASE 2020](https://www.asecho.org/wp-content/uploads/2023/03/PIIS0894731720301334.pdf)) |
| Correct steps | 1) Go back on CPB to rest the heart rather than force weaning. 2) Systematic check under TEE: preload, rhythm/pacing, structural problems, graft problems ([EACTS 2024, Fig. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). 3) Inotropes at moderate doses. 4) IABP is the first device approach ([PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf)). 5) If still failing: ECLS/VAD early |
| Rules | Multidisciplinary approach (I, B); forcing weaning with high-dose inotropes/vasoconstrictors not recommended (III, B); short-term MCS should be considered (IIa, B) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). Start PC support before end-organ injury, lactate below 4 mmol/L ([PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf)) (A) |
| Incidence | PC-ECLS used in 0.3-3.6% of cardiac surgery ([PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf)) |
| If mishandled | PC-ECLS survival to discharge 34% (meta-analysis), 25-42% in single centres; age and pre-ECLS lactate predict death; lactate clearance matters more than first value ([PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf)) (A) |

### 2.12 Failure to wean: RV failure

| Field | Content |
|---|---|
| Cause | Pre-existing pulmonary hypertension, RV ischaemia (RCA air or graft problem), protamine type III reaction, inadequate RV protection (general; uncertain) |
| Signs | Rising CVP, falling MAP, dilated hypokinetic RV on TEE, tricuspid regurgitation (uncertain - not verified this pass) |
| Correct steps | EACTS 2024 algorithm includes an RV branch ([EACTS 2024, Fig. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)); drugs named for RV/pulmonary pressure in protamine reactions: milrinone, epinephrine, inhaled nitric oxide, epoprostenol ([OpenAnesthesia](https://www.openanesthesia.org/keywords/protamine-reactions/)). Delayed ECLS with RV dysfunction is linked to worse outcomes ([PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf)) |
| Incidence | Not quantified this pass (uncertain) |
| If mishandled | Same as 2.11 |

### 2.13 Graft failure and myocardial ischaemia

| Field | Content |
|---|---|
| Cause | Technical anastomosis error, kinked or twisted conduit, poor target, competitive flow (general; uncertain) |
| TTFM thresholds | One centre's adequacy criteria: mean flow 20 mL/min or more for RCA grafts and 15 mL/min or more for left grafts, PI below 5, diastolic filling above 50% ([Harahsheh 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3515040)) (B). Other groups: mean flow 10-15 mL/min and PI 3-5 ([review via search](https://pmc.ncbi.nlm.nih.gov/articles/PMC4986749)) (uncertain - snippet only). Tokuda: left-sided grafts at risk with flow 15 mL/min or less, PI 5.1 or more, backward flow 4.1% or more; low positive predictive value ([search summary](https://pure.fujita-hu.ac.jp/en/publications/predicting-early-coronary-artery-bypass-graft-failure-by-intraope/)) (uncertain - snippet only) |
| Signs | ST changes, new regional wall-motion abnormality on TEE ([ASE 2020](https://www.asecho.org/wp-content/uploads/2023/03/PIIS0894731720301334.pdf)), low TTFM flow, high PI, ventricular arrhythmia |
| Correct steps | 1) Re-measure TTFM after checking probe and BP. 2) Inspect graft for kink/twist/length. 3) Revise if poor flow persists. Only about 1% of grafts were revised on flowmetry alone; 5.4% occluded on early angiography despite adequate TTFM ([Harahsheh 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3515040)) |
| If mishandled | Perioperative MI, low output, failure to wean (design link to 2.11) |

### 2.14 Coronary air embolism after unclamping

| Field | Content |
|---|---|
| Cause | Residual air in aortic root or graft; the right coronary ostium is anterior, so the RCA is most often affected ([case report](https://arya.mui.ac.ir/article_31207.html)) (uncertain - snippet only) |
| Signs | Inferior ST elevation, RV dysfunction, bradycardia/heart block shortly after clamp release or de-airing (general; uncertain) |
| Correct steps | Two principles: help nitrogen leave the bubble and push the bubble distally, mainly by raising coronary perfusion pressure ([case report](https://arya.mui.ac.ir/article_31207.html)) (uncertain - snippet only). Animal data: retrograde cardioplegia preserved 90% of baseline LV function after induced coronary air ([search summary](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/6132025)) (C). Going back on CPB is a plausible game option but was not confirmed by a source (uncertain) |
| If mishandled | RV failure at weaning (link to 2.12) |

### 2.15 Arrhythmias (bradycardia, heart block, atrial fibrillation)

| Field | Content |
|---|---|
| Incidence | Postoperative AF 20-40% after CABG ([search summary of reviews](https://rbccv.org.br/article/4423/en-US/atrial-fibrillation-after-coronary-artery-bypass-grafting-and-its-relationship-with-hospital-complications-in-sao-paulo-state)) (uncertain - snippet only); 13.5-28.4% in isolated CABG ([JCPSP](https://www.jcpsp.pk/article-detail/ppostoperative-atrial-fibrillation-following-isolated-coronary-artery-bypass-grafting-incidence-predictors-and-clinical-outcomesorp)) (uncertain - snippet only) |
| Signs | Irregular ECG, loss of atrial kick (falling MAP), pacing failure |
| Correct steps | Epicardial pacing: DDD 80-100/min at maximum outputs for asystole or severe bradycardia; pause the pacemaker to exclude hidden VF if PEA with paced spikes ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A) |
| If mishandled | POAF is associated with acute renal failure (OR 2.74) and higher perioperative mortality and stroke ([JTCVS 2021 meta-analysis](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_2522619935)) (uncertain - snippet only) |

### 2.16 Tamponade (after chest closure / ICU)

| Field | Content |
|---|---|
| Incidence | 2.0% of 510 consecutive cardiac surgery patients ([Chest 1993 via search](https://www.qxmd.com/r/8325120)) (uncertain - snippet only); 0.2-1.8% in the first hours ([PMC2222672](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2222672/)) (B) |
| Signs | Equalisation of pressures in 81%; hypotension only in 40% and pulsus paradoxus in 50% with circumferential effusion; localised clots may be missed on TTE ([search summary of Chuttani 1994 and case report](https://hscrb.harvard.edu/publication/chuttani-k-tischler-md-pandian-ng-lee-rt-mohanty-pk-diagnosis-of-cardiac-tamponade-after-cardiac-surgery-relative-value-of-clinical-echocardiographic-and-hemodynamic-signs-am-heart-j-1994-ap)) (uncertain - snippet only). A sudden fall in drain output is not a validated sign (uncertain) |
| Correct steps | Tamponade requires immediate resternotomy; external massage is ineffective in tamponade or hypovolaemia ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A). See Section 3.1 |
| If mishandled | Arrest; survival after post-cardiac-surgery arrest is about 50% ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) |

### 2.17 Temperature errors (hypothermia and hyperthermia)

| Field | Content |
|---|---|
| Rules | Use arterial outlet temperature as surrogate for brain temperature (I, C); keep outlet below 37 °C (I, C); gradient outlet-venous at most 10 °C during cooling and rewarming (I, C); when outlet is 30 °C or more: gradient at most 4 °C (IIa, B) and rewarming at most 0.5 °C/min (IIa, B); PA or nasopharyngeal temperature reasonable for weaning (IIa, C); no recommended weaning temperature ([STS/SCA/AmSECT 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)) (A). EACTS 2024 rates avoiding systemic hyperthermia by capping outlet at 37 °C as Class I, Level A ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| Evidence | Slow rewarming lowered postoperative cognitive dysfunction in 4 RCTs; brain may be exposed to more than 37 °C during rewarming ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)). Gradient limits exist to avoid gas outgassing ([STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/)) |
| Errors to model | Too-fast rewarming, outlet above 37 °C, weaning while cold, heater-cooler fault (heat-exchange problems are among the most reported CPB events, [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) |
| If mishandled | Neurocognitive penalty and microbubble risk (design); cold weaning raises bleeding and arrhythmia (uncertain) |

### 2.18 Hyperkalaemia from cardioplegia

| Field | Content |
|---|---|
| Cause | Large cumulative cardioplegia volume, especially with pre-existing renal dysfunction ([review PMC3755226](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755226/)) (uncertain - snippet only) |
| Incidence | Not quantified; postoperative hypokalaemia is more common than hyperkalaemia ([same](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755226/)) |
| Signs | Peaked T waves, wide QRS, heart block, slow return of rhythm after clamp release (general; uncertain); K+ on blood gas (design threshold: above 6.0 mmol/L) |
| Correct steps | Limit cardioplegia volume; shift K+ into cells (bicarbonate if acidotic); calcium, epinephrine, furosemide used in a case; intraoperative haemodialysis prevented hyperkalaemia in 33 renal-failure patients ([search summary](https://perfusion.com/?p=38875); [case](https://link.springer.com/content/pdf/10.1007/BF03009322.pdf)) (uncertain - snippet only). Insulin-glucose dosing in this setting: UNVERIFIED |
| If mishandled | Failure to restore rhythm; heart block; delay in weaning (design) |

### 2.19 Cannula malposition

| Field | Content |
|---|---|
| Arterial cannula | Tip in an arch branch (e.g. left subclavian) caused a sharp NIRS drop that recovered above 65% after repositioning ([case report via search](https://doaj.org/article/3815b23349ac4b958c071c2124304eb6)) (uncertain - snippet only). Radial-femoral pressure gap appeared in 16.3% of 92 paediatric patients, mostly during CPB ([Yonsei study](https://ir.ymlib.yonsei.ac.kr/handle/22282913/176942)) (uncertain - snippet only). High line pressure at normal flow |
| Venous cannula | Low venous return; sudden NIRS drop; TEE shows position ([search summary](https://springerlink.bibliotecabuap.elogim.com/chapter/10.1007/978-3-030-79721-8_9)) (uncertain - snippet only). SVC-obstruction facial congestion: not sourced (uncertain) |
| Correct steps | Reduce flow, check line pressure and bilateral NIRS, TEE/epiaortic check, reposition; if dissection is suspected go to 2.2 (design order) |
| If mishandled | Unilateral cerebral hypoperfusion (stroke odds up, design) or dissection |

### 2.20 Low venous return and venous air lock

| Field | Content |
|---|---|
| Cause | Negative pressure in the venous line entrains air at the cannulation site; vacuum-assisted drainage over-pressure; large air volume can overwhelm the reservoir ([search summary of JECT/PIRS reports](https://ject.edpsciences.org/articles/ject/pdf/2011/03/ject-43-115.pdf)) (uncertain - snippet only); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Signs | Falling reservoir level, air column in venous line, low-level alarm |
| Correct steps | A "Venous Air Lock" crisis checklist exists ([Tarola 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745)) but its steps are not in the published text. Plausible order (design, uncertain): 1) reduce arterial flow to protect reservoir level; 2) surgeon finds and closes the air entry (purse string, cannula hole); 3) walk air to reservoir / lift venous line; 4) add volume; 5) restore flow. Never let the reservoir run dry (reservoir inattention causes massive air, [Mills & Ochsner](https://pubmed.ncbi.nlm.nih.gov/7431967/)) |
| Clock | Reservoir volume / (arterial flow - venous return) seconds to empty (design formula) |
| If mishandled | Empty reservoir pumps air: escalate to event 2.3 |

### 2.21 Incidence table for the random event generator (per case, design defaults)

| Event | Default probability per case (design) | Anchor |
|---|---|---|
| Reoperation-level bleeding | 0.024-0.05 | STS 2.4%; Qazi 5.3% |
| Iatrogenic dissection | 0.0006 (ascending cannulation), 0.006 (femoral) | EACTS 2024 / review |
| Massive air embolism | 0.0005 (design; 1980 rate was 0.0022) | Mills & Ochsner |
| Oxygenator change-out | 0.00025 | UK survey 1:4,055 |
| Heparin resistance | 0.04-0.26 (use 0.10) | Butt 2024 |
| Clinical HIT (only if heparin exposure profile) | 0.005-0.03 | 581-patient cohort; JPMA |
| Protamine reaction any type | 0.02 (type III 0.0013) | OpenAnesthesia range 0.06-10.6% |
| Vasoplegia | 0.05-0.45 by risk | ICVTS 2025 |
| Reperfusion VF | 0.4-0.9 | Thai trial; abstract |
| PC-ECLS needed | 0.003-0.036 | PC-ECLS 2020 |
| Tamponade (ICU) | 0.002-0.02 | Chest 1993; PMC2222672 |

---

## 3. Crisis protocols and checklists

### 3.1 Arrest after cardiac surgery (STS 2017, EACTS 2009, ERC 2021, CALS)

Background numbers: arrest after cardiac surgery 0.7-8% and about half survive to discharge ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A); 0.7-2.9% and 17-79% survival in the EACTS 2009 guideline ([Dunning 2009 PDF](https://orbi.uliege.be/bitstream/2268/35860/1/Dunning_Eur%20J%20Cardiothorac%20Surg_2009_36_3.pdf)) (uncertain - snippet only). VF causes 25-50% of arrests; tamponade and bleeding cause many others ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)). Protocol practice halves time to resternotomy ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)). Only 32% of survey respondents followed the guideline in their unit ([Adam et al. survey](https://research.manchester.ac.uk/en/publications/resuscitation-after-cardiac-surgery-results-of-an-international-s/)) (uncertain - snippet only).

**Step order (STS 2017 unless stated)** ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A):

1. Confirm arrest (ECG plus pulseless arterial trace; with an IABP, pause it or look at CVP/oximetry pulsatility). Call for help, start the arrest protocol.
2. **VF / pulseless VT:** three sequential shocks without intervening compressions if a defibrillator is available within 1 minute (Class I, B). Average success falls from 78% (1st shock) to 35% (2nd) to 14% (3rd). Then external massage as a bridge to internal massage.
3. **Asystole / extreme bradycardia:** connect epicardial wires, DDD 80-100/min at maximum atrial and ventricular output (Class I, C). If no output, or pacing delay beyond 1 minute, start compressions. Transcutaneous pacing is lower priority.
4. **PEA:** exclude quickly reversible causes; if paced rhythm, pause the pacer to unmask VF; then prompt resternotomy.
5. **Airway/breathing:** FiO2 100%, remove PEEP, check tube, exclude tension pneumothorax (large-bore cannula if suspected) and haemothorax.
6. **Compressions:** 100-120/min, aim for systolic impulse above 60 mmHg on the arterial line.
7. **Drugs:** stop infusions after initial efforts fail. Amiodarone 300 mg via central line after three failed shocks (IIa, A); 150 mg more for refractory VF; then 900 mg over 24 h; lidocaine 1 mg/kg alternative. **No routine epinephrine or vasopressin** during arrest unless an experienced clinician directs it (Class III harm, C); smaller doses "50 to 300" boluses are acceptable in peri-arrest (the extracted PDF text reads "mg"; micrograms are almost certainly intended - uncertain). Atropine is not part of the protocol.
8. **Emergency resternotomy within 5 minutes** if reversible causes are not found (Class I, C); mandatory if external massage cannot reach systolic 60 mmHg. Rapid ECMO is an acceptable alternative in expert centres. Resternotomy is standard until day 10 after surgery; after that a senior clinician decides.
9. **IABP during arrest:** switch to pressure trigger so inflation follows compressions.
10. **AEDs** are not recommended because they cannot give three rapid shocks.

ERC 2021 matches: up to three consecutive shocks within about 1 minute, pacing within about 1 minute, resternotomy within about 5 minutes, consider MCS and ECPR ([ERC 2021, cardiac surgery section](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767); [PubMed 33773826](https://pubmed.ncbi.nlm.nih.gov/33773826/)) (A). CALS-ANZ also limits routine resternotomy to within 10 days ([search summary](https://www.myamericannurse.com/resuscitation-after-cardiac-surgery-best-practice-recommendations/)) (uncertain - snippet only).

**Six roles** ([STS 2017, Fig 2](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A): (1) external cardiac massage, (2) airway and breathing, (3) defibrillation and pacing (also brings internal paddles to the sterile field), (4) team leader, (5) drugs and syringe drivers, (6) ICU coordinator (prepares resternotomy, calls experts). Plus a resternotomy team that scrubs and gowns.

**Emergency resternotomy set** - five essential items: scalpel, wire cutter, heavy needle holder, single-piece sternal retractor, sucker; scissors and all-in-one drape optional ([STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf)) (A).

### 3.2 Cardiac OR crisis checklists

- **Five cardiac surgery crisis checklists** (Brigham/Harvard group): CPB failure, systemic air embolism, venous air lock, protamine reaction, heparin resistance. Built by 3-round modified Delphi (70% agreement). On activation, a "reader" guides the team and an overhead page calls perfusion, nursing and anaesthesia. In simulation, 89% of 9 participants wanted the checklist used if they were the patient ([Tarola 2018, PMC6364745](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745)) (A). Licence not stated (UNVERIFIED). Individual steps are not in the text (only one figure).
- **EACTS 2024 CPB guideline:** institution-approved CPB checklist before CPB (Class I); acknowledge its completion during the surgical safety checklist; use a perioperative CPB checklist that includes CPB incidents; critical-situation checklists improve time to decision ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A). EBCP provides a checklist on its website (not reviewed here).
- **General OR crisis checklists:** Ariadne Labs (12 checklists, updated May 2017, at projectcheck.org) ([search summary](https://emphatic-hc.squarespace.com/crisis-checklists); [APSF](https://www.apsf.org/article/emergency-manuals-the-time-has-come/)) (B). In the NEJM simulation study, failure to perform life-saving steps fell from 23% to 6% with checklists ([Harvard Gazette](https://news.harvard.edu/gazette/story/newsplus/checklists-in-operating-rooms-improve-performance-during-crises-2/)) (B). Stanford Emergency Manual covers 25 perioperative events ([App Store listing](https://apps.apple.com/app/id6446658508)) (B).
- **SCA-specific crisis checklist:** no SCA-branded cardiac OR crisis checklist was found in this pass (uncertain).

### 3.3 Perfusion emergency protocols (AmSECT)

- **AmSECT Perfusion Checklist** (origination 1990, revision 2004 by AmSECT Quality Committee; PDF file dated 2022) sections: Patient; Sterility; Pump; Electrical; Cardioplegia; Gas supply; Components; Safety mechanisms; Assisted venous return; Monitoring; Anticoagulation; Temperature control; Supplies; Backup (hand cranks, duplicate components, emergency lighting, backup O2 tank, ice); **Emergent restart of bypass** (heparin time and dose confirmed, components de-bubbled, gas flow confirmed, alarms re-engaged, water source connected); **Termination** (venous assist off, reservoirs vented, shunts closed, vents clamped); **Post-bypass** (announce bypass terminated, lines clamped, arterial circuit bubble-free before transfusing, pump suckers off) ([AmSECT PDF](https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf)) (A).
- **AmSECT Standards & Guidelines 2023:** twelve standards, Standard 5 is "Checklist" ([AmSECT S&G page](https://amsect.org/policy-practice/amsects-standards-and-guidelines)) (uncertain - snippet only). A draft change says emergency protocols must be accessible during a case and backup power is required ([AmSECT comparison draft](https://www.amsect.org/Portals/0/Comparison%20of%20S%26G%20Changes%20from%202017%20to%202023%20Final%20Draft.pdf)) (uncertain - snippet only).
- **AmSECT Massive Air Embolism clinical protocol template** - full step list in Section 2.3; recommends an annual drill ([AmSECT PDF](https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf)) (A).

### 3.4 Massive bleeding and transfusion

- On CPB: RBC if HCT below 18%; not if above 24% with adequate DO2; DO2 at least 280 mL/min/m2 (I, A) ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)).
- Reversal: protamine-to-heparin ratio below 1.0 (EACTS 2024); maximum 2.6 mg/100 U (STS 2018); titration-based protamine dosing can be beneficial (IIa, B) ([STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf)).
- Product algorithm (fibrinogen, platelets, PCC, viscoelastic targets): **UNVERIFIED** in this pass; read the 2024 EACTS/EACTAIC PBM guideline (DOI 10.1093/ejcts/ezae352) before coding ([EACTS page](https://www.eacts.org/clinical-practice-guideline/2024-eacts-eactaic-guidelines-on-patient-blood-management-in-adult-cardiac-surgery-in-collaboration-with-ebcp)).

### 3.5 TEE findings the game should show

The ASE/SCA/STS 2020 guideline says TEE should be used in adults without contraindications for all open heart and thoracic aortic procedures and should be considered in CABG; after the procedure, look for unintended consequences such as new wall-motion abnormalities and iatrogenic aortic dissection; TEE helps during de-airing ([ASE 2020, JASE 33:692-734](https://www.asecho.org/wp-content/uploads/2023/03/PIIS0894731720301334.pdf)) (A). A correction was published in November 2020 ([ASE page](https://asecho.org/guideline/guidelines-for-the-use-of-transesophageal-echocardiography-to-assist-with-surgical-decision-making-in-the-operating-room-a-surgery-based-approach-from-the-american-society-of-echocardiography-in-coll)).

| Event | TEE clip to show (design, based on ASE content) |
|---|---|
| Iatrogenic dissection | Flap and entry tear in ascending aorta; note the distal ascending/arch "blind spot" (epiaortic scan helps) |
| Air embolism / de-airing | Bright echoes in LV/LA/aortic root |
| Graft failure | New regional wall-motion abnormality in graft territory |
| LV failure | Global hypokinesis, low fractional area change |
| RV failure / protamine III | Dilated hypokinetic RV, tricuspid regurgitation (uncertain) |
| Tamponade | Effusion or localised clot compressing atria/RV |
| Venous cannula | Cannula position in SVC/IVC, PFO check before cannulation strategy |

### 3.6 Licences of crisis and checklist material

| Resource | Version / date | Licence | Personal NC use | Attribution | Share-alike | No-derivatives | Source |
|---|---|---|---|---|---|---|---|
| 2024 EACTS/EACTAIC/EBCP CPB guidelines (ICVTS 40(2), published 12 Feb 2025) | 2024 | CC BY-NC-ND 4.0 | Yes | Yes | No | **Yes** - cannot ship altered text | [PMC page](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| Vasoplegia review (ICVTS 2025) | 2025 | CC BY 4.0 | Yes | Yes | No | No | [PMC11968317](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/) (A) |
| STS 2017 resuscitation consensus | 2017 | © STS / Elsevier; no open licence stated | Read and cite only (UNVERIFIED reuse) | - | - | - | [STS PDF](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf) |
| ERC 2021 special circumstances | 2021 | © ERC/GRC/ARC; PMC open-access subset under COVID-era permission; specific CC licence not stated | UNVERIFIED | - | - | - | [PMC8190767](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767) |
| Stanford Emergency Manual | Version UNVERIFIED (app © 2025, 25 events) | CC BY-NC-ND (official page); version UNVERIFIED (a 2013 copy cites 3.0) | Yes | Yes (Stanford Anesthesia Cognitive Aid Program) | No | Yes | [Stanford EM FAQ](https://emergencymanual.stanford.edu/?p=2060) (uncertain - snippet only; site returned HTTP 503) |
| Ariadne Labs OR Crisis Checklists | Updated May 2017 | CC BY-NC-SA 4.0 per a third-party copy - **UNVERIFIED** | Probably yes | Yes | Yes | No | [Scribd copy](https://www.scribd.com/document/518857653/Or-Crisis-Checklists-Harvard) (C); projectcheck.org returned no text |
| AmSECT Perfusion Checklist | Orig. 1990, rev. 2004 | No licence stated - UNVERIFIED; text invites perfusionists to modify it | UNVERIFIED | - | - | - | [AmSECT PDF](https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf) |
| AmSECT Massive Air Embolism template | Undated | No licence stated - UNVERIFIED; "template for your perfusion team to edit" | UNVERIFIED | - | - | - | [AmSECT PDF](https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf) |
| Tarola 2018 cardiac crisis checklists | NIH author manuscript 2019 | Not stated - UNVERIFIED | - | - | - | - | [PMC6364745](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745) |
| Pulse Physiology Engine (optional physiology backend) | 4.4.0 | Apache-2.0 | Yes (also commercial) | Keep NOTICE/licence | No | No | [Pulse about page](https://pulse.kitware.com/_about_pulse.html) (A); [NOTICE](https://gitlab.kitware.com/physiology/engine/-/raw/stable/NOTICE) |

**Practical rule (design, not legal advice):** facts, doses and step orders are not copyrightable text, so write all in-game checklists in your own words and cite the source in a credits screen. Do not paste NC-ND text, and never present game checklists as official society documents.

---

## 4. Team communication

### 4.1 Closed-loop communication

- Perfusionists must "efficiently communicate with the cardiac team using closed-loop communication"; surgeon-perfusionist communication is very frequent but not systematised ([Dias et al. 2021, PINTS tool, PMC8720321](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720321)) (A). PINTS has 4 categories and 16 behaviours rated 0.5-4.0; reliability ICC 0.735 overall, lowest for teamwork/communication (0.691) ([same](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720321)).
- In paediatric cardiac surgery observation, closed-loop exchanges occurred only between main surgeon and perfusionist; other exchanges were open ([search summary](https://repository.tudelft.nl/file/File_18958ef7-ef12-4f52-987a-b062183f0d7e)) (uncertain - snippet only).
- A Dutch video study defined essential verbal items for safe communication during CABG on CPB ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)).
- **Game rule (design):** every critical order (pump on/off, flow change, clamp on/off, drug dose) needs call - read-back - confirm within 5 s; missing read-back raises the chance of a wrong execution.

### 4.2 CPB transition checklists

| Transition | Content | Source |
|---|---|---|
| Pre-bypass | AmSECT checklist sections (patient ID, circuit, gas, safety devices, anticoagulation "heparin time and dose confirmed, anticoagulation tested and reported", backup) | [AmSECT](https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf) |
| Going on bypass | ACT above 480 s (or 400 s with maximal-activation tests) before CPB | [STS 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf) |
| Weaning | Checklist before weaning is recommended (I, C); EACTS supplies one in Supplementary Appendix 6; earlier 4-item and 7-item checklists exist; a simulation study showed better completion of 5 of 9 tasks with a checklist; an electronic "ventilator not on" alarm exists | [EACTS 2024, section 11.1](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |
| Termination and post-bypass | Announce bypass terminated, clamp lines, bubble-free arterial line before transfusing, pump suckers off at protamine | [AmSECT](https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) |

The individual items of the EACTS weaning appendix were not read (UNVERIFIED). A plausible game list (design): ventilation on, temperature target reached, rhythm/pacing ready, K+ and acid-base checked, de-airing done, drugs ready, TEE ready, vents off, surgeon ready.

### 4.3 Handover to the ICU

- STS Workforce on Critical Care review: "Handoffs From the Operating Room to the Intensive Care Unit After Cardiothoracic Surgery", Ann Thorac Surg 2019;107:619-630 ([PubMed 30500341](https://pubmed.ncbi.nlm.nih.gov/30500341/)) (A; content not read).
- Standardised protocol after congenital cardiac surgery: technical errors per handover fell from 6.24 to 1.52 and information omissions from 6.33 to 2.38, without longer handovers (79 handovers) ([Joy et al. 2011 via PSNet](https://psnet.ahrq.gov/issue/standardized-multidisciplinary-protocol-improves-handover-cardiac-surgery-patients-intensive)) (B).
- Barriers: time pressure, unclear expectations, confusion about other clinicians' needs ([HATRICC](https://pair.upenn.edu/publication/developing-a-standard-handoff-process-for-operating-room-to-icu-transitions-multidisciplinary-clinician-perspectives-from-the-handoffs-and-transitions-in-critical-care-hatricc-study/)) (B).
- **Game mechanic (design):** an end-of-case handover mini-game: the player picks items for a structured handover (patient, procedure, CPB/clamp times, grafts, events, drugs, pacing settings, bleeding, lines, plan). Each omitted critical item raises the chance of a later ICU event (e.g. unknown pacing dependence).

### 4.4 How errors propagate in the team

- In 31 observed cardiac operations, teamwork and communication failures were the strongest predictor of surgical errors ([Wiegmann 2007 via PSNet](https://psnet.ahrq.gov/issue/disruptions-surgical-flow-and-their-relationship-surgical-errors-exploratory-investigation)) (B); a conference report gives about 8 flow disruptions per hour and 5 errors per case (uncertain - snippet only).
- Flow disruptions are minor one by one but accumulate and raise technical errors and adverse outcomes; most relate to teamwork failures ([Wahr et al. 2013 AHA statement via PSNet](https://psnet.ahrq.gov/issue/patient-safety-cardiac-operating-room-human-factors-and-teamwork-scientific-statement)) (B).
- 10% of 908 potentially preventable deaths in an Australian study involved communication problems; perfusionist stress peaks at start and end of perfusion; fatigue and long hours contribute; teamwork errors are linked to problems during weaning ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/)) (A).
- Simulation design: four emergent CPB scenarios (femoral cannulation for calcified aorta, re-initiation after protamine, conversion for dissection, air removal after dropped cannula), with verbal orders that must be heard, acknowledged and acted on ([White et al. 2015, PMC4730171](https://pmc.ncbi.nlm.nih.gov/articles/PMC4730171)) (B).

**Error-propagation model (design):** each team member has workload and stress (0-1). Stress rises at CPB start/end and during events. Probability that an order is misheard or delayed = base 2% x (1 + 2 x stress) x (no read-back ? 3 : 1). A missed step adds a hidden "latent error" that can trigger a later event (e.g. vent left clamped leads to LV distension at weaning).

---

## 5. Post-operative outcome model

### 5.1 Structure

For each endpoint k (mortality, stroke, renal failure/AKI, prolonged ventilation, reoperation, DSWI):

```
logit(p_k) = logit(p0_k)  +  s * SUM_i [ ln(OR_i,k) * x_i ]
p_k        = 1 / (1 + exp(-logit(p_k)))     (cap at 0.95, design)
```

- `p0_k` = the patient's baseline risk (from the STS calculator for authored profiles, or from STS population rates in Section 1.1 scaled by risk band).
- `x_i` = exposure in units (for example, number of 30-minute CPB blocks above the expected time for that case).
- `s` = shrinkage factor 0.5-0.7 (design). Published odds ratios come from separate studies with overlapping causes (long CPB causes transfusion, which causes ...), so adding them all at full strength double-counts.
- Then sample each endpoint once (Bernoulli) for the debrief, but show the player the probabilities too.

### 5.2 Effect sizes

| Exposure (x unit) | Endpoint: OR (95% CI) | Source / grade |
|---|---|---|
| CPB time, per 30 min | Death 1.57; renal 1.31; neurologic 1.28; pulmonary 1.17; multi-organ failure 1.21; reoperation for bleeding 1.1; multiple transfusions 1.58 (5,006 patients, mean CPB 115 min, in-hospital death 2.6%) | [Salis 2008](https://db.cngb.org/search/literature/18948034); [ScienceOpen](https://www.scienceopen.com/document/vid/27344a7b-f677-41f6-942d-ca767b2e14b9) (A, uncertain - snippet only) |
| CPB time per minute (alt.) | Reoperation for bleeding OR 1.005 | [Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/) (A) |
| Cross-clamp time per minute | OR 1.0148 (low-risk) / 1.0110 (high-risk), outcome probably mortality | [Halle abstract 2025](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0045-1804135) (uncertain - snippet only) |
| RBC transfusion (per unit; per-unit reading uncertain) | Mortality 1.77 (1.67-1.87); renal failure 2.06 (1.87-2.27); prolonged ventilation 1.79 (1.72-1.86); serious infection 1.76 (1.68-1.84); cardiac 1.55 (1.47-1.63); neurologic 1.37 (1.30-1.44) (11,963 isolated CABG) | [Koch 2006, PMID 16607235](https://pubmed.ncbi.nlm.nih.gov/16607235/) (A); Qazi cites "OR 1.77 for a single RBC transfusion" ([PMC8493226](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)) |
| MAP below 65 mmHg after CPB, per 10 min | New RRT OR 1.12 (1.06-1.18) (6,532 patients); no association before/during CPB | [EACTS 2024 citing ref 375](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| MAP below 65 mmHg total, per 10 min | Composite stroke/AKI/death OR 1.05 (1.02-1.08); outside CPB 1.06 (1.03-1.10) (4,984 patients) | [EACTS 2024 citing ref 376](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| DO2 below 280 mL/min/m2 (area over curve) | Linked to ventilation more than 72 h and AKI; DO2 below 300 for more than 15 min with CPB longer than 121 min gave AKI in 50% | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| Reoperation for bleeding (yes) | 30-day mortality 4.8% vs 2.2%; long-term HR 1.21 (1.07-1.37) | [Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/) (A) |
| Partial aortic clamp vs no-touch | Stroke 2.2% vs 0.2%; meta RR 0.41 for no-touch | [WJC review](https://www.wjgnet.com/1949-8462/full/v13/i8/309.htm) (uncertain - snippet only) |
| New postoperative AF | Acute renal failure OR 2.74 (2.42-3.11) | [JTCVS 2021 meta via search](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_2522619935) (uncertain - snippet only) |
| Massive air embolism reaching brain | Death 4/13, transient injury 3/13, none 6/13 | [Mills & Ochsner](https://pubmed.ncbi.nlm.nih.gov/7431967/) (A) |
| Iatrogenic dissection | Mortality about 30% if recognised; more than double if missed | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/) (A) |
| Cardiac arrest after surgery | About 50% survive to discharge | [STS 2017](https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf) (A) |
| PC-ECLS | 34% survive to discharge (meta-analysis) | [PC-ECLS 2020](https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf) (A) |
| Arterial outlet above 37 °C / fast rewarming | No effect size; Class I avoid; slow rewarming lowers cognitive dysfunction (4 RCTs) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/); [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/) - use a small design penalty |

### 5.3 Worked example (design)

Profile P02, baseline mortality 1.5% (design). Case: CPB 150 min where 90 min was expected (2 blocks of 30 min), 2 RBC units, 20 min of MAP below 65 mmHg after CPB.

- Baseline logit = ln(0.015 / 0.985) = -4.185.
- CPB: 2 x ln(1.57) = 2 x 0.451 = 0.902.
- RBC: 2 x ln(1.77) = 2 x 0.571 = 1.142.
- Hypotension: composite OR used as a mortality proxy: 2 x ln(1.05) = 0.098.
- Without shrinkage: logit = -2.043, p = 11.5%. With s = 0.6: logit = -4.185 + 0.6 x 2.142 = -2.900, p = 5.2%.

The unshrunk value is implausibly high for a 2-unit, 150-minute case, which shows why shrinkage is needed. Tune `s` so that a "typical messy case" lands near the STS composite morbidity rate of 15% and mortality stays within 1.5-3x baseline (design).

### 5.4 Caveats

- All odds ratios are observational associations, not causes ([Salis](https://db.cngb.org/search/literature/18948034), [Koch](https://pubmed.ncbi.nlm.nih.gov/16607235/)).
- The STS c-statistic is only 0.62 for reoperation and 0.70 for stroke ([Part 2](https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf)); the game should accept wide randomness for these.
- Long-term survival curves after reoperation for bleeding run parallel, so the harm is mostly early ([Qazi 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/)).

---

## Game hooks

| Finding | Game mechanic / data value / rule |
|---|---|
| STS baseline rates (1.1) | `outcomeBaselines.json`: mortality 0.024, stroke 0.013, renalFailure 0.022, prolongedVent 0.093, reoperation 0.024, dswi 0.003, composite 0.150 |
| STS predictors (1.2) | Patient schema with ~40 fields; generator samples consistent combinations (e.g. dialysis implies high creatinine) |
| Profile library (1.3) | 12 authored cases; campaign order from very low to very high band |
| Dominance / IMLAD / porcelain aorta / redo (1.4) | Random anatomy roll at case creation; IMLAD adds an exposure mini-task with RV-entry risk; porcelain aorta disables standard clamp and offers alternatives; redo adds a re-entry phase with 2.8% major injury base chance |
| CPB adverse event rates (2.0) | Overall event budget: about 1 event per 15-200 cases in "realistic" mode; "training" mode forces 1-3 events per case (design) |
| Massive air protocol (2.3) | 9-step sequence across 3 roles; timer; retrograde flow slider 0.3-2.0 L/min; outcome table from Mills & Ochsner |
| Heparin resistance rules (2.6) | ACT gauge must exceed 480 s (or 400 s with "maximal activation" device setting) before "Go on bypass" unlocks; AT vial = 500 IU; formula shown in debrief |
| HIT rules (2.7) | Pre-op briefing choice: delay vs bivalirudin; bivalirudin raises bleeding and "stasis clot" risk if pump is stopped with blood standing |
| Protamine rules (2.8) | Infusion speed control; above 20 mg/min raises reaction risk (design); ratio meter (target below 1.0, hard stop 2.6 mg/100 U) |
| Vasoplegia doses (2.9) | Drug pump ranges taken directly from the review table |
| Arrest protocol (3.1) | ICU arrest scenario: 3 shocks within 60 s, DDD 80-100 pacing, amiodarone after shock 3, 5-minute resternotomy countdown, six role slots to assign, 5-item resternotomy tray |
| Temperature rules (2.17) | Heater-cooler UI warns when outlet is above 37 °C, gradient above 10 °C (or 4 °C at 30 °C or more), rewarming above 0.5 °C/min |
| DO2 and HCT rules (3.4) | Live DO2 readout; time below 280 mL/min/m2 accumulates AKI risk; transfusion button blocked when HCT is above 24% unless DO2 is low |
| Failure to wean (2.11) | Inotrope "score"; forcing high doses carries a hidden penalty; IABP then ECLS options; ECLS before lactate 4 mmol/L improves survival roll |
| TTFM (2.13) | TTFM probe readout: mean flow, PI, diastolic filling; thresholds 15/20 mL/min, PI 5, DF 50%; 5.4% of "good" grafts still occlude (hidden roll) |
| Checklists (3.2-4.2) | Pre-bypass, weaning and termination checklists as interactive cards; skipping items creates latent errors |
| Closed loop (4.1) | Voice/text orders need read-back; no read-back multiplies error chance |
| Handover (4.3) | End-of-case handover mini-game; omissions raise ICU event risk |
| Outcome model (5) | Logistic model with shrinkage; debrief shows each modifier's contribution |
| Licences (3.6) | Credits screen lists sources; all checklist text re-authored |

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | Isolated CABG (STS 2011-2014): mortality 2.4%, stroke 1.3%, renal failure 2.2%, prolonged ventilation 9.3%, reoperation 2.4%, DSWI 0.3% | https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf | A |
| 2 | STS calculator needs only age and sex; blanks imputed; 2018 models added about 40 variables | https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf | A |
| 3 | After-surgery VF: 3 shocks before compressions; success 78% / 35% / 14% | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 4 | Emergency resternotomy within 5 minutes; mandatory if massage cannot reach systolic 60 mmHg; standard until day 10 | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 5 | Amiodarone 300 mg after 3 failed shocks, then 150 mg, then 900 mg/24 h; lidocaine 1 mg/kg alternative | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 6 | No routine epinephrine during arrest (Class III harm) | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 7 | Pacing DDD 80-100/min at maximum output for asystole/bradycardia | https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf | A |
| 8 | ERC 2021: up to 3 shocks within about 1 min, pacing within 1 min, resternotomy within about 5 min | https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767 | A |
| 9 | ACT above 480 s on CPB is reasonable (above 400 s with maximal-activation tests) | https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf | A |
| 10 | Heparin resistance: more than 500 U/kg to reach ACT 480 s; incidence 4-26%; AT vials 500 IU | https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/ | B |
| 11 | HIT urgent surgery: bivalirudin 1 mg/kg + 2.5 mg/kg/h + 50 mg prime; ACT about 2.5x baseline (>300 s) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 12 | Protamine-to-heparin ratio below 1.0; never above 2.6 mg/100 U | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ ; https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf | A |
| 13 | Arterial outlet below 37 °C; gradient at most 10 °C; at most 4 °C and 0.5 °C/min when outlet is 30 °C or more | https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ | A |
| 14 | DO2 at least 280 mL/min/m2 to reduce AKI (I, A); transfuse on CPB if HCT below 18% | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 15 | Keep systolic below 100 mmHg during aortic cannulation | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 16 | Iatrogenic dissection 0.06-0.6%; about 30% mortality if found early | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 17 | Massive air embolism protocol: stop, clamp, ventilate; Trendelenburg; SVC retrograde perfusion 1-2 L/min for 1-2 min | https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf | A |
| 18 | Mills & Ochsner: 8 of 3,620 CPB cases; of 13 patients, 4 instant deaths | https://pubmed.ncbi.nlm.nih.gov/7431967/ | A |
| 19 | Vasoplegia: MAP below 65, CI above 2.2, SVR below 800; incidence 5-45%; methylene blue 1-2 mg/kg | https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/ | B |
| 20 | Forcing weaning with high-dose inotropes not recommended (III, B); short-term MCS IIa, B | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 21 | PC-ECLS used in 0.3-3.6%; survival to discharge 34%; start before lactate 4 mmol/L | https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf | A |
| 22 | CPB time OR 1.57 per 30 min for death | https://db.cngb.org/search/literature/18948034 | A (snippet) |
| 23 | RBC transfusion OR 1.77 mortality, 2.06 renal failure, 1.79 prolonged ventilation | https://pubmed.ncbi.nlm.nih.gov/16607235/ | A |
| 24 | Post-CPB MAP below 65 mmHg: RRT OR 1.12 per 10 min | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 25 | Reoperation for bleeding: 30-day mortality 4.8% vs 2.2% | https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/ | A |
| 26 | Weaning checklist recommended (I, C); pre-CPB checklist recommended (I) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 27 | Five cardiac crisis checklists: CPB failure, systemic air, venous air lock, protamine reaction, heparin resistance | https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745 | A |
| 28 | Structured handover cut technical errors 6.24 to 1.52 per handover | https://psnet.ahrq.gov/issue/standardized-multidisciplinary-protocol-improves-handover-cardiac-surgery-patients-intensive | B |
| 29 | EACTS 2024 CPB guideline licence CC BY-NC-ND 4.0 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ | A |
| 30 | Pulse Physiology Engine 4.4.0, Apache-2.0 | https://pulse.kitware.com/_about_pulse.html | A |

---

## Sources

1. STS Expert Consensus for the Resuscitation of Patients Who Arrest After Cardiac Surgery (Ann Thorac Surg 2017;103:1005-20) - https://www.sts.org/sites/default/files/documents/ExpertConsensus_ResuscitationAfterCardiacSurgery.pdf - arrest protocol, shocks, pacing, drugs, roles, resternotomy set, survival.
2. Dunning et al., EACTS guideline for resuscitation in cardiac arrest after cardiac surgery (Eur J Cardiothorac Surg 2009;36:3-28) - https://orbi.uliege.be/bitstream/2268/35860/1/Dunning_Eur%20J%20Cardiothorac%20Surg_2009_36_3.pdf - incidence 0.7-2.9%, survival 17-79% (snippet).
3. ERC Guidelines 2021: Cardiac arrest in special circumstances (German PMC version) - https://pmc.ncbi.nlm.nih.gov/articles/PMC8190767 - 3 shocks, pacing, 5-min resternotomy; also https://pubmed.ncbi.nlm.nih.gov/33773826/.
4. 2024 EACTS/EACTAIC/EBCP Guidelines on cardiopulmonary bypass in adult cardiac surgery - https://pmc.ncbi.nlm.nih.gov/articles/PMC11826094/ (PDF: https://cris.unibo.it/retrieve/2e207d71-a608-44f6-968e-3dc328be516b/ivaf002.pdf) - incident rates, dissection, air, checklists, weaning, DO2, HCT, MAP, temperature, bivalirudin, protamine, licence.
5. O'Brien/Shahian et al., STS 2018 Adult Cardiac Surgery Risk Models Part 2 - https://www.sts.org/sites/default/files/documents/Shahian-%202018%20Risk%20Model-Part%202%20of%202.pdf - endpoint rates, definitions, predictors, c-statistics.
6. STS 2018 Risk Model Calculator guide - https://www.sts.org/sites/default/files/STS-2018-Risk-Model-Calculator.pdf - required inputs, imputation, version.
7. STS ACSD 2024 Update on National Trends and Outcomes - https://pubmed.ncbi.nlm.nih.gov/40127833/ - database scale.
8. STS ACSD 24H3 Multipliers and Annual Rates - https://sts.org/sites/default/files/2024-11/ACSD%2024H3%20Multipliers%20and%20Annual%20Rates.pdf - 2024 CABG mortality (snippet).
9. STS 2018 Part 1 summary - https://dihi.org/outcome/the-society-of-thoracic-surgeons-2018-adult-cardiac-surgery-risk-models-part-1-background-design-considerations-and-model-development/ - model development.
10. Shore-Lesserson et al., STS/SCA/AmSECT Anticoagulation During CPB guideline 2018 - https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf - ACT targets, HIT, protamine limits.
11. Butt et al., Heparin resistance management during cardiac surgery (JECT 2024) - https://pmc.ncbi.nlm.nih.gov/articles/PMC11415039/ - HR definition, incidence, AT dosing.
12. Engelman et al., STS/SCA/AmSECT temperature management guideline (JECT 2015) - https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/ - temperature rules.
13. Tarola et al., cardiac surgery crisis checklists (2018) - https://pmc.ncbi.nlm.nih.gov/articles/PMC6364745 - five checklists, Delphi method, simulation.
14. AmSECT Perfusion Checklist - https://www.amsect.org/Portals/0/AmSECT%20Documents/PerfusionChecklist.pdf - checklist sections, emergent restart, termination.
15. AmSECT Massive Air Embolism clinical protocol template - https://amsect.org/Portals/0/Massive%20Air%20Embolism.pdf - air embolism steps.
16. AmSECT Standards and Guidelines page - https://amsect.org/policy-practice/amsects-standards-and-guidelines - 2023 standards (snippet).
17. Mills & Ochsner 1980, Massive air embolism during CPB - https://pubmed.ncbi.nlm.nih.gov/7431967/ - causes, incidence, management, outcomes.
18. Perfusion.com quick reference: massive air embolism - https://perfusion.com/quick-reference-massive-air-embolism/ - alternative retrograde flow values (C).
19. OpenAnesthesia: Protamine reactions - https://www.openanesthesia.org/keywords/protamine-reactions/ - types, incidence, dosing, management.
20. Vasoplegic syndrome in cardiac surgery (ICVTS 2025) - https://pmc.ncbi.nlm.nih.gov/articles/PMC11968317/ - definition, incidence, doses, licence.
21. 2020 EACTS/ELSO/STS/AATS Expert Consensus on Post-Cardiotomy ECLS - https://www.sts.org/sites/default/files/Expert%20Consensus/2020%20Expert%20Consensus%20on%20Post-Cardiotomy%20Extracorporeal%20Life%20Support%20in%20Adult%20Patients.pdf - PC-ECLS incidence, survival, lactate rule.
22. Willcox, Oxygenator failure: are you prepared? (JECT 2023) - https://pmc.ncbi.nlm.nih.gov/articles/PMC10487349/ - oxygenator failure causes, PRONTO.
23. ANZCP PIRS 2021 oxygenator change-out - https://anzcp.org/wp-content/uploads/reports/2021/PIRS-2021-Coagulation_2_Oxygenator_Changeout.pdf - historic change-out rates (snippet).
24. Koch et al. 2006, Crit Care Med 34:1608-16 - https://pubmed.ncbi.nlm.nih.gov/16607235/ - transfusion odds ratios.
25. Salis et al. 2008, CPB duration and outcomes - https://db.cngb.org/search/literature/18948034 - CPB odds ratios (snippet).
26. Qazi et al. 2021, Reoperation for bleeding - https://pmc.ncbi.nlm.nih.gov/articles/PMC8493226/ - reoperation incidence, mortality, causes.
27. Harahsheh 2012, TTFM in CABG - https://pmc.ncbi.nlm.nih.gov/articles/PMC3515040 - TTFM cutoffs and revision rate.
28. ASE/SCA/STS 2020 TEE guideline for surgical decision-making - https://www.asecho.org/wp-content/uploads/2023/03/PIIS0894731720301334.pdf - TEE indications and findings.
29. Coronary dominance review - https://pmc.ncbi.nlm.nih.gov/articles/PMC4505791 - dominance ranges (snippet).
30. PAFMJ CT dominance study (1,000 patients) - https://www.pafmj.org/PAFMJ/article/view/4311 - dominance proportions.
31. Vanker 2014, intramyocardial LAD - https://ajol.info/index.php/sajs/article/view/106808 - IMLAD 21.7%.
32. Alagha 2023, intramyocardial LAD - https://turkiyeklinikleri.com/article/en-the-intramyocardial-left-anterior-descending-artery-prevalence-early-and-mid-term-surgical-outcomes-after-coronary-artery-bypass-procedures-a-retrospective-single-center-study-105593.html - IMLAD 11.5%.
33. WJC 2021 review on porcelain aorta / no-touch - https://www.wjgnet.com/1949-8462/full/v13/i8/309.htm - porcelain aorta incidence, no-touch stroke (snippet).
34. Modern practice and outcomes of reoperative cardiac surgery - https://pubmed.ncbi.nlm.nih.gov/33757681/ - redo injury 2.8%, mortality 3.5% (snippet).
35. MDPI redo review - https://www.mdpi.com/2077-0383/14/4/1251 - older re-entry injury rates (snippet).
36. HIT in 581 cardiac surgery patients - https://www.pubmed.gov/19793190/ - HIT 0.5% (snippet).
37. JPMA HIT study - https://www.archive.jpma.org.pk/PdfDownload/1711 - antibody 50%, clinical 3% (C).
38. Stanford Emergency Manual permissions - https://emergencymanual.stanford.edu/?p=2060 - CC BY-NC-ND (snippet).
39. Ariadne Labs OR crisis checklists (third-party copy) - https://www.scribd.com/document/518857653/Or-Crisis-Checklists-Harvard - CC BY-NC-SA 4.0 claim (C, UNVERIFIED).
40. Harvard Gazette on OR crisis checklists - https://news.harvard.edu/gazette/story/newsplus/checklists-in-operating-rooms-improve-performance-during-crises-2/ - 23% to 6%.
41. APSF, Emergency manuals - https://www.apsf.org/article/emergency-manuals-the-time-has-come/ - projectcheck.org availability.
42. Dias et al. 2021, PINTS tool - https://pmc.ncbi.nlm.nih.gov/articles/PMC8720321 - closed-loop communication, perfusionist non-technical skills.
43. White et al. 2015, Emergent CPB simulation - https://pmc.ncbi.nlm.nih.gov/articles/PMC4730171 - simulation scenarios.
44. Joy et al. 2011 via PSNet - https://psnet.ahrq.gov/issue/standardized-multidisciplinary-protocol-improves-handover-cardiac-surgery-patients-intensive - handover error reduction.
45. STS Workforce on Critical Care, OR-to-ICU handoffs 2019 - https://pubmed.ncbi.nlm.nih.gov/30500341/ - handoff review (not read).
46. HATRICC handoff study - https://pair.upenn.edu/publication/developing-a-standard-handoff-process-for-operating-room-to-icu-transitions-multidisciplinary-clinician-perspectives-from-the-handoffs-and-transitions-in-critical-care-hatricc-study/ - handoff barriers.
47. Wahr et al. 2013 AHA statement via PSNet - https://psnet.ahrq.gov/issue/patient-safety-cardiac-operating-room-human-factors-and-teamwork-scientific-statement - flow disruptions and teamwork.
48. Wiegmann et al. 2007 via PSNet - https://psnet.ahrq.gov/issue/disruptions-surgical-flow-and-their-relationship-surgical-errors-exploratory-investigation - teamwork failures predict errors.
49. Pulse Physiology Engine about page - https://pulse.kitware.com/_about_pulse.html - version 4.4.0, Apache-2.0, ECMO model.
50. Thai J Surg reperfusion VF trial - https://he02.tci-thaijo.org/index.php/ThaiJSurg/article/view/266715 - VF incidence and 10 J shocks (snippet).
51. Tamponade case report PMC2222672 - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2222672/ - early tamponade 0.2-1.8%.
52. Thieme 2019 review on iatrogenic aortic dissection - https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0039-1695729 - site-specific incidence and origin (snippet; page blocked).
53. Columbia iatrogenic dissection series - https://vivo.weill.cornell.edu/display/pubid31770775 - management approach (snippet).
54. Coronary air embolism case report - https://arya.mui.ac.ir/article_31207.html - RCA susceptibility, management principle (snippet).
55. Hyperkalaemic cardioplegia review - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755226/ - potassium problems (snippet).
56. ICVTS 2014 fatal air embolism analysis - https://academic.oup.com/icvts/article/19/5/875/648359 - countermeasures must be fast (snippet).
57. EuroSCORE (Wikipedia) - https://en.wikipedia.org/wiki/EuroSCORE - EuroSCORE II reference (coefficients not verified).

---

## Summary

**Key findings**

- A defensible "average CABG patient" baseline exists: STS 2018 isolated CABG rates (mortality 2.4%, stroke 1.3%, renal failure 2.2%, prolonged ventilation 9.3%, reoperation 2.4%, DSWI 0.3%). STS models predict mortality and renal failure well but reoperation and stroke poorly, so those two should depend on in-game events.
- Arrest after cardiac surgery has a specific, well-documented protocol that differs from standard ACLS: three quick shocks, early pacing, no routine epinephrine, amiodarone after the third failed shock, six team roles and resternotomy within 5 minutes. It is ideal for a timed team mini-game.
- Perfusion crises have concrete published rules: ACT above 480 s, heparin resistance above 500 U/kg, bivalirudin dosing for HIT, protamine ratio below 1.0, outlet temperature below 37 °C, DO2 at least 280 mL/min/m2, transfusion if HCT below 18%. AmSECT gives a step-by-step massive air embolism protocol and a perfusion checklist with emergent restart, termination and post-bypass sections.
- Usable effect sizes exist to link intraoperative events to outcomes (CPB time, transfusion, hypotension minutes, DO2, reoperation for bleeding, air embolism, dissection, ECLS), but they are observational and overlapping, so a shrinkage factor is required.
- Teamwork evidence supports closed-loop communication, checklists and structured handovers as game mechanics (crisis checklists cut missed life-saving steps from 23% to 6%; structured handover cut technical errors from 6.24 to 1.52).

**Recommendations**

1. Build the patient schema from STS predictors; author 12 profiles; calibrate their risks by hand in the official STS calculator (the host was unreachable from this session).
2. Implement the 20 events in Section 2 with the event schema in 2.0 and the default probabilities in 2.21; give each one a role-based ordered step list and a clock.
3. Implement the ICU arrest scenario exactly as Section 3.1 (it has the best evidence and clearest timings).
4. Implement the outcome model in Section 5 with a tunable shrinkage factor (start at 0.6) and show the contributions in the debrief.
5. Re-author all checklist and protocol text; keep a credits page with links; treat NC-ND sources as read-only references.
6. Optionally use Pulse Physiology Engine 4.4.0 (Apache-2.0) for haemodynamics; it includes an ECMO model.

**Open questions**

- Exact STS PROM values for each authored profile (needs manual calculator use; calculator terms not read).
- EuroSCORE II coefficients (not verified) as an open alternative to STS.
- Steps inside the Tarola crisis checklists (only names are published) and the EACTS weaning checklist appendix.
- Massive-bleeding product algorithm (fibrinogen, platelets, PCC, viscoelastic thresholds) from the 2024 EACTS/EACTAIC PBM guideline.
- Internal defibrillation energy for adult open-chest shocks (commonly quoted 10-20 J, UNVERIFIED).
- Incidence data for LIMA injury, poor veins, small/diffuse targets, RV failure at weaning and cardioplegia hyperkalaemia.
- Official licence pages for the Stanford Emergency Manual (site returned HTTP 503) and Ariadne OR crisis checklists (projectcheck.org returned no text).
