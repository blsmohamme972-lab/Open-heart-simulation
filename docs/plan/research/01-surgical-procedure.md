# Research 01: The real open-heart operation, step by step

> **Purpose.** This is input for the plan's section 2 ("Medical procedure model"). It describes the real operation in enough detail that the game can copy it: the order of steps, who does each step, the instruments, typical times, what success looks like, what goes wrong, and what people say out loud in the operating room (OR).
>
> **Status:** research only, so there is no game design here beyond short "game hooks". Researched 2026-11-03.
>
> **Disclaimer:** this is for a personal, educational game. It is **not** clinical guidance. Practice varies a lot between surgeons and hospitals. Where sources disagree, the range is given. Anything marked **(uncertain)** is the author's best estimate or rests on a weak or secondary source. Check it before treating it as fact.

---

## 0. Summary for the plan

| Decision | Recommendation | Why (short) |
|---|---|---|
| v1 procedure | **On-pump CABG ×3 via median sternotomy**: LIMA→LAD, reversed saphenous vein graft (SVG)→obtuse marginal (OM), SVG→RCA/PDA. Cold blood cardioplegia, antegrade with optional retrograde. | It is the most common adult heart operation, and the steps are standard and well documented. It covers every core mechanic: opening, conduit harvest, bypass, arrest, microsurgery, weaning and closure. Outcome measures are clear. |
| v2 | **Isolated surgical aortic valve replacement (SAVR)** | It reuses about 80% of the CABG pipeline (sternotomy, cannulation, CPB, arrest, weaning, closure) **(uncertain estimate)**. New work is the aortotomy, valve excision, decalcification, pledgeted annular sutures and prosthesis seating. |
| v3 | **Mitral valve repair** (then replacement) | It needs bicaval cannulation, left atriotomy, leaflet and chordal modelling, an annuloplasty ring and a saline test. The anatomy and soft-tissue simulation are the hardest so far. |
| v3/v4 | **Off-pump CABG (OPCAB)** | It needs a beating, moving heart with a tissue stabilizer and shunts. That is the hardest physics, and it is a minority technique (about 17% of US CABG in 2012, falling). |
| Phase model | About 45 ordered steps in 11 phases (A–K below), run as a state machine with team "actors" and a physiology model. | It matches how real OR teams split the work and talk to each other. |
| Timing realism | Skin-to-skin about 3–4 h; bypass time about 100 min; cross-clamp time about 70 min. The game will need time compression (an open question for the design step). | See §6. |

---

## 1. Which procedures to model

### 1.1 Volumes and risk (US, Society of Thoracic Surgeons (STS) Adult Cardiac Surgery Database)

- The STS database covers more than 8.3 million procedures from more than 1,000 sites, which is more than 97% of US cardiac surgery ([STS 2024 update, Ann Thorac Surg 2025](https://pubmed.ncbi.nlm.nih.gov/40127833/)).
- An STS composite-measure study (July 2016–June 2019) reported **448,569 CABG** cases against **72,067 isolated AVR**. CABG is by far the largest category ([STS multiprocedural composite measure, index record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_2560059683); number taken from a search snippet, so **(uncertain)** until checked against the full text).
- One large-centre example from 2024: isolated CABG 994 cases, isolated AVR 382, AVR+CABG 171 ([Cleveland Clinic 2024 outcomes](https://my.clevelandclinic.org/-/scassets/files/org/heart/outcomes/matrix-data-set/final-neoh-e15-jan-dec-2024.pdf?la=en)). Isolated mitral repair was 460, which is unusually high because it is a mitral referral centre.

**Observed STS national event rates (%), from [STS ACSD 25H4 "Multipliers and Annual Rates"](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf):**

| Procedure / outcome | 2023 | 2024 | 2025 |
|---|---|---|---|
| **Isolated CABG**: operative mortality | 2.197 | 2.082 | 2.047 |
| permanent stroke | 1.276 | 1.296 | 1.223 |
| renal failure | 1.963 | 1.985 | 1.946 |
| prolonged ventilation | 5.764 | 5.478 | 5.164 |
| deep sternal wound infection | 0.260 | 0.245 | 0.245 |
| any re-operation | 2.537 | 2.581 | 2.697 |
| combined morbidity/mortality | 9.462 | 9.192 | 8.906 |
| post-op length of stay < 6 days | 47.1 | 46.6 | 46.7 |
| post-op length of stay > 14 days | 5.40 | 5.49 | 5.30 |
| **Isolated AVR**: operative mortality | 2.083 | 1.939 | 2.179 |
| **Isolated MV repair**: operative mortality | 0.997 | 0.946 | 0.879 |
| **Isolated MV replacement**: operative mortality | 4.916 | 4.924 | 4.868 |
| **AVR + CABG**: operative mortality | 3.846 | 3.610 | 3.671 |
| **MV repair + CABG**: operative mortality | 5.243 | 4.187 | 4.931 |

Game use: these rates can set the baseline odds in an "outcome" or "consequence" model. A flawless player should see roughly these rates or lower. A sloppy player should see higher rates.

### 1.2 Recommendation and justification

1. **v1 = on-pump CABG through a median sternotomy.**
   - It is the most common operation (see above), so it is the most "real".
   - Its steps are the most standard. Teaching material lays out the same sequence: sternotomy → conduit harvest → heparin → cannulation → CPB → cross-clamp → cardioplegia → distals → proximals → de-air → unclamp → wean → protamine → decannulate → close ([AATS TSRA Primer: CPB Fundamentals](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [Cardiac Outlines: CABG outline](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)).
   - It contains every mechanic the later procedures need: opening, CPB, arrest, fine suturing, weaning and closure.
   - Grafting can be scored clearly: correct target, anastomosis quality, graft length and lie, flow, and ischemic time.
   - Guideline support for the default graft plan: the internal mammary artery (IMA) to the LAD is the preferred graft, and in the 2021 guideline the radial artery was preferred over the saphenous vein for the second most important target (Class 1) ([ACC key takeaways, 2021 ACC/AHA/SCAI revascularization guideline](https://www.acc.org/latest-in-cardiology/articles/2022/10/31/13/02/key-takeaways-from-the-2021-coronary-revascularization-guidelines)). For v1 a reversed SVG is still the realistic and simpler second conduit. A radial artery could be an optional upgrade.
2. **v2 = SAVR.** It is the second most common isolated operation. It reuses most of the CABG systems and adds one well-defined new "repair" task (§9.1).
3. **v3 = mitral valve repair, then replacement.** Repair has the best results (operative mortality about 0.9%), but it needs complex valve analysis and leaflet, chordal and ring work. The soft-tissue simulation is the hardest (§9.2).
4. **OPCAB, later or optional.** Its use peaked at about 23% of US CABG in 2002 and fell to about 17% by 2012 ([STS-based analysis via Duke Scholars](https://scholars.duke.edu/publication/1040209) **(uncertain: link taken from a search snippet)**). Within the VA, it fell to 8.6% in 2018–2021 ([VA on- vs off-pump volume study](https://bohrium.dp.tech/paper/arxiv/ceab112d7b14ca0d77c6169f766870181546f8f71b5cfadf0f4080ee92cee799)). The trial evidence is neutral to slightly unfavourable:
   - CORONARY (n = 4,752): 5-year composite 23.1% vs 23.6%, HR 0.98 ([ACC CORONARY summary](https://www.acc.org/Latest-in-Cardiology/Clinical-Trials/2014/06/08/17/13/CORONARY); [NEJM 2016, PMID 27771985](https://pubmed.ncbi.nlm.nih.gov/27771985/)).
   - VA ROOBY 5-year: mortality 15.2% off-pump vs 11.9% on-pump ([CTSNet JANS summary of ROOBY-FS](https://spb-cts.freelock.com/print/jans/five-year-outcomes-after-pump-and-pump-coronary-artery-bypass)).

   For the game, OPCAB means a moving target and a stabilizer, which is a big physics cost for a minority technique.

---

## 2. The team and where they stand

| Role | Typical position | Main jobs in a CABG |
|---|---|---|
| **Attending surgeon** | Patient's right side | Sternotomy, LIMA takedown, cannulation, anastomoses, decisions, and directing the team's verbal communication. |
| **First assistant** (fellow, resident or PA) | Patient's left side, across from the surgeon | Exposure, suction, holding conduits, snaring Rumel tourniquets, tying cannulas, sometimes opening and closing. |
| **Second assistant / vein harvester** (often a PA) | At the legs | Saphenous vein harvest (open or endoscopic) at the same time as the LIMA harvest, then leg closure. |
| **Scrub nurse / surgical technologist** | Beside the surgeon, at the instrument table | Hands instruments and sutures, loads needles, prepares the sterile ends of cannulas, keeps counts. |
| **Circulating nurse** | Not sterile, moves around the room | Runs the time-out and sign-out, gets supplies and blood, does documentation and counts. |
| **Anesthesiologist** (with TEE) | At the head | Induction, lines, TEE, drugs (heparin, protamine, inotropes, vasopressors), ventilation on and off, blood products, haemodynamics before and after bypass. |
| **Perfusionist** | At the heart-lung machine, usually near the head or on the left | Primes and checks the circuit, runs CPB (flow, pressure, temperature, gases), delivers cardioplegia, monitors ACT, calls out status. |

Sources: roles as described across the [TSRA primer](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) and [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Aortic+Cannulation). Exact standing positions vary by institution **(uncertain)**.

---

## 3. Master timeline for v1 (on-pump CABG ×3)

Wall-clock times are typical for a planned, uncomplicated case with an experienced surgeon. Ranges overlap because harvests run in parallel.

| Phase | Steps | Typical duration | Elapsed (approx.) |
|---|---|---|---|
| A. Room entry → incision | Sign-in, induction, lines, TEE, positioning, prep and drape, time-out | 45–90 min **(uncertain)** | 0:00 → about 1:00 |
| B. Opening | Skin incision, sternotomy, IMA retractor | 10–15 min **(uncertain)** | → about 1:15 |
| C. Conduit harvest (parallel) | LIMA (surgeon) and SVG (PA, legs) | LIMA 20–29 min (RCT means); SVG 30–60 min **(uncertain)** | → about 1:45 |
| D. Exposure + cannulation | Pericardial well, heparin, purse-strings, cannulas | 15–25 min **(uncertain)** | → about 2:05 |
| E. Bypass + arrest | Go on pump, cool, cross-clamp, cardioplegia | 5–10 min **(uncertain)** | → about 2:15 |
| F. Grafting (clamp on) | 3 distal anastomoses (± proximals under a single clamp) | Cross-clamp about 60–75 min (STS means) | → about 3:25 |
| G. Reperfusion | Hot shot, de-air, unclamp, defibrillate, pacing wires, (proximals with a side-biting clamp) | 10–30 min **(uncertain)** | → about 3:45 |
| H. Weaning | Checklist, separation | 5–15 min **(uncertain)** | CPB total about 100 min |
| I. Reversal + decannulation | Protamine, remove cannulas | 10–20 min **(uncertain)** | → about 4:00 |
| J. Hemostasis + closure | Hemostasis, chest tubes, wires, layers, sign-out | 30–60 min **(uncertain)** | → about 4:45 |
| K. Transfer to ICU | Monitor and pacing-box transfer, handoff | 15–30 min **(uncertain)** | → about 5:00 |

Measured anchors are in §6.

---

## 4. The primary procedure, step by step

Format for each step: **Who**, **Instruments/supplies**, **Real sequence**, **Duration**, **Success**, **Errors/complications**, and, where useful, **Game hooks**. "S" = surgeon, "A1" = first assistant, "A2" = second assistant/harvester, "SN" = scrub nurse, "CN" = circulating nurse, "AN" = anesthesiologist, "P" = perfusionist.

### Phase A: patient entry to incision

**A1. Patient entry + WHO Sign-In**
- **Who:** CN leads; AN and the patient (if awake) take part.
- **Real sequence:** The patient confirms identity, site, procedure and consent. The team confirms the site marking, the anaesthesia machine and medication check, that the pulse oximeter is on and working, allergies, airway or aspiration risk, and blood-loss risk above 500 mL. These items come from the WHO Surgical Safety Checklist ([summary of the WHO checklist items](https://en.wikipedia.org/wiki/WHO_Surgical_Safety_Checklist)).
- **Cardiac adaptations:** STS and EACTS adapted the checklist *without removing items*. They added cardiac-specific checks such as preparation for heavy bleeding, perfusion arrangements and the ICU bed ([EACTS checklist guideline, doi:10.1093/ejcts/ezs009](https://researchportal.northumbria.ac.uk/en/publications/eacts-guidelines-for-the-use-of-patient-safety-checklists/); [review of checklist adaptations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9491475/)).
- **Duration:** 2–5 min **(uncertain)**.
- **Success:** every item confirmed out loud and documented.
- **Errors:** skipped items, or blood not cross-matched or available. In the game, a skipped check could trigger a later delay event.

**A2. Anesthesia induction, monitoring and lines**
- **Who:** AN, with the anesthesia tech and CN.
- **Real setup:**
  - ECG, pulse oximetry, end-tidal CO₂, EEG-derived depth monitor (BIS), **radial arterial line**, blood-pressure cuff on the other arm, and **central venous access ± pulmonary artery catheter** ([AATS TSRA Primer: Setting Up](https://www.aats.org/tsra-primer-setting-up)).
  - Lines usually go in after intubation: "arterial line, cordis, and Swan-Ganz" ([Cardiac Outlines: Positioning](https://publish.obsidian.md/cardiacoutlines/Textbook/Positioning+for+Cardiac+Case)).
  - **TEE probe**, **Foley catheter** ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Positioning+for+Cardiac+Case)), temperature probes (nasopharyngeal and bladder) and cerebral oximetry **(uncertain: common practice, not individually sourced)**.
  - External defibrillator pads are placed when internal defibrillation will not be possible ([TSRA Setting Up](https://www.aats.org/tsra-primer-setting-up)).
  - Baseline ACT is drawn **(uncertain)**.
- **Antibiotic:** cefazolin is given **within 60 min before skin incision** ([STS antibiotic prophylaxis guideline Part II, via Guideline Central](https://guidelinecentral.com/guideline/19852)). Redosing is due about 4 h later or after CPB, depending on the protocol ([MPOG measure spec ~4 h 15 min](https://spec.mpog.org/Spec/Public/89)).
- **Duration:** 30–60 min **(uncertain)**.
- **Success:** stable induction, all lines working, TEE baseline exam done (EF, valves, aorta).
- **Errors:** induction hypotension, line complications (arterial or carotid puncture), unexpected TEE findings that change the plan (for example significant aortic regurgitation, which changes the cardioplegia route).

**A3. Positioning**
- **Who:** S or A1, CN, AN.
- **Real setup:**
  - Supine, arms tucked and padded, shoulder roll or donut pad behind the scapulae, knee pads ([TSRA Setting Up](https://www.aats.org/tsra-primer-setting-up)).
  - Legs lifted with rolled blankets under the knees to expose the saphenous harvest sites ([Cardiac Outlines: Positioning](https://publish.obsidian.md/cardiacoutlines/Textbook/Positioning+for+Cardiac+Case)).
  - Electrosurgery (Bovie) return pads on the lateral thighs ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Positioning+for+Cardiac+Case)).
  - Lights: one at the head looking into the chest, one behind the right shoulder, one on the legs (same source).
- **Duration:** 5–10 min **(uncertain)**.
- **Errors:** pressure injury, nerve injury (brachial plexus from over-abducted arms) **(uncertain)**, and a wet Bovie pad that causes burns.

**A4. Skin prep and draping**
- **Who:** A1/A2 and SN.
- **Real sequence:** Prep **from chin to knees, with both legs prepped for CABG vein harvest** ([TSRA Setting Up](https://www.aats.org/tsra-primer-setting-up)). Some surgeons prep down to the ankles **(uncertain)**. Optional ultrasound mapping of the saphenous vein before draping ([Cardiac Outlines CABG outline](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)). Chlorhexidine-alcohol is the usual agent **(uncertain: not separately sourced)**.
- **Duration:** 10–15 min **(uncertain)**.
- **Success:** sterile field over the sternum and both legs.

**A5. Time-out (before incision)**
- **Who:** the whole team. CN reads; S, AN, SN and P answer.
- **WHO items:** team introductions by name and role; patient, procedure and incision site; **antibiotic given within the last 60 min**; surgeon states critical or unusual steps, expected duration and expected blood loss; anaesthesia states patient-specific concerns; nursing confirms sterility indicators and equipment issues; essential imaging displayed ([WHO checklist items](https://en.wikipedia.org/wiki/WHO_Surgical_Safety_Checklist)).
- **Cardiac additions:** the perfusionist confirms the cannulation plan, minimum temperature, cardioplegia type and route, and whether circulatory arrest is planned ([pediatric adaptation, SciELO RBCCV](https://scielo.br/j/rbccv/a/MXkdGjQTMgF6nhK3Mqc4Lkk/?lang=en)). The perfusion pre-bypass checklist must be complete. A validated 41-item CPB checklist covers patient, equipment, machine, centrifugal pump, gas supply, materials, circuit, cardioplegia, vacuum, and "before starting CPB" (heparin dose, ACT, arterial line test) ([dos Reis Filho et al., JECT 2025, CC BY 4.0](https://doi.org/10.1051/ject/2024030)).
- **Duration:** 1–3 min **(uncertain)**.
- **Game hooks:** an interactive time-out dialogue. A missed item can carry a penalty.

### Phase B: opening

**B1. Skin incision**
- **Who:** S.
- **Instruments:** skin marker, **#10 blade** "held like a violin bow", **electrocautery (Bovie)** ([TSRA Setting Up](https://www.aats.org/tsra-primer-setting-up)).
- **Real sequence:**
  1. Feel for the sternal notch and xiphoid, draw the midline and check it against the sternal edges.
  2. Cut from just below or just above the sternal notch to below the xiphoid tip.
  3. Deepen with cautery to the periosteum, **staying midline between the origins of the two pectoralis muscles**, and score a straight line on the periosteum to follow with the saw ([VUMC Open Manual of Surgery: Sternotomy, CC BY-SA 3.0](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf); [TSRA](https://www.aats.org/tsra-primer-setting-up)).
- **Duration:** 2–5 min **(uncertain)**.
- **Success:** a straight midline line on the periosteum.
- **Errors:** going off midline ("if cutting through muscle, you are off midline": [TSRA](https://www.aats.org/tsra-primer-setting-up)), which leads to an asymmetric sternotomy and a higher risk of sternal instability.

**B2. Median sternotomy**
- **Who:** S, with A1 assisting. AN holds ventilation.
- **Instruments:** cautery, hemostat or right-angle clamp, **sternal saw (reciprocating, with a guard foot)**, Lebsche sternal knife and mallet as backup, Army-Navy retractors, **bone wax** (or Gelfoam or vancomycin paste) ([VUMC Sternotomy](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)).
- **Real sequence:**
  1. Divide the **interclavicular ligament** above the notch with cautery, taking care because the **innominate vein may be right underneath** (VUMC).
  2. Free the xiphoid. Bluntly finger-dissect behind the sternum from above and below (VUMC).
  3. **Ask anaesthesia to hold respirations** (lungs down) while sawing. Angle the saw blade **slightly upward** to protect the innominate vein. Resume ventilation when done ([TSRA Setting Up](https://www.aats.org/tsra-primer-setting-up)).
  4. Keep the guard pulled up against the back of the sternum. A plain oscillating saw is dangerous for a first-time sternotomy because depth cannot be controlled. Oscillating saws are used for **redo** sternotomy ([VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf); [MMCTS tutorial](https://mmcts.org/tutorial/80)).
  5. Control periosteal and marrow bleeding with cautery and a thin layer of bone wax. Use **wax sparingly**, because it is a suspected infection risk and should be avoided in fragile, elderly sterna ([MMCTS tutorial](https://mmcts.org/tutorial/80)).
  6. Insert the sternal retractor and open it **gradually**, a little at a time ([VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)).
- **Duration:** 3–8 min **(uncertain)**.
- **Success:** a midline split with even halves, no pleural or pericardial injury, dry edges.
- **Errors/complications:** off-midline cut, which leads to fracture and later sternal non-union (VUMC); innominate vein injury; pleural entry; RV or graft injury in a redo; sawing while the lungs are inflated, which injures the lung **(uncertain)**.
- **Game hooks:** the saw follows the scored line, and deviation is measured. Mistiming the "hold ventilation" call costs points.

**B3. IMA retractor deployment**
- **Who:** S/A1.
- **Instruments:** asymmetric IMA retractor, for example a **Rultract "Skyhook"** or **Delacroix-Chevalier IMA Couëtil retractor** ([TSRA: Mammary takedown](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)). The table is raised and rotated away from the surgeon **(uncertain)**.
- **Duration:** 1–3 min **(uncertain)**.

### Phase C: conduit harvest (two teams in parallel)

**C1. LIMA takedown (surgeon)**
- **Who:** S, with A1 suctioning and retracting.
- **Instruments:** Bovie at **about 50% of normal power** to avoid thermal injury ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)); small and medium hemoclips with a clip applier; DeBakey forceps; **papaverine** (topical and/or sub-adventitial); **bulldog clamp**; **Potts scissors** to make the oblique cuff ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets); [CTSNet LIMA video note on papaverine](https://www.ctsnet.org/print/article/left-mammary-artery-harvesting-through-left-minithoracotomy-thoracoscopic-assistance)).
- **Real sequence:**
  1. Pedicled harvest (with its veins and fascia) or skeletonized harvest (artery alone).
  2. Extend proximally to the **first intercostal branch** (identify and divide it to avoid "steal") and distally just beyond the **bifurcation into the superior epigastric and musculophrenic arteries**.
  3. **Clip and cauterize away from the vessel.** Never use cautery on a metal clip, because heat conducts to the IMA.
  4. Avoid opening the pleura cephalad to the 4th rib.
  5. Check hemostasis, **ask for heparin, and divide the IMA distally only after heparin is in**.
  6. Check the flow, use papaverine for spasm, and place a bulldog on the end ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)).
- **Duration (RCT data):** pedicled **20.2 ± 5.4 min**; surgical skeletonized **28.6 ± 8.7 min** ([Interact CV Thorac Surg 2024 RCT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11139514/)).
- **Success:** a long enough IMA (no tension with the lungs inflated and the heart filled), good free flow, no spasm or hematoma, dry bed.
- **Errors:**
  - Grabbing the IMA itself, or excess traction, causing spasm, intimal dissection or hematoma.
  - Cautery near clips.
  - Dissecting too far cephalad.
  - IMA too short.
  - Missed side branches causing steal or bleeding.
  - Pleural entry, which means a pleural chest tube is needed.
  - Skipping the bed recheck after protamine.

  (All from [TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets).) Skeletonized grafts had higher flow in one 200-patient RCT ([CTSNet / RCT summary](https://www.iris.unina.it/retrieve/e268a72f-65d9-4c8f-e053-1705fe0a812c/REPRINT%20definitivo.pdf)).

**C2. Greater saphenous vein harvest (second team, same time)**
- **Who:** A2 (PA). SN supports both teams.
- **Instruments (open):** #10/#15 blade, **Metzenbaum scissors**, small hemoclips, vessel loop, a vein cannula (20 G short IV catheter held with a soft bulldog: [Cardiac Outlines anastomosis primer](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)), syringe with heparinized blood or crystalloid, **7-0 Prolene** for repairs.
- **Real sequence (open technique):**
  1. Incise 0.5–1 cm anterior and superior to the **medial malleolus**.
  2. Tunnel over the vein with scissors and divide the skin bridges every few centimetres.
  3. Clip the side branches.
  4. Distend gently (no high pressure) to find leaks.
  5. Repair holes with 7-0 Prolene using longitudinal bites.
  6. Keep the valves in place and **reverse the vein** when grafting.
  7. Store it in heparinized solution.

  Source: [TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets). Endoscopic vein harvest (EVH) is common in the US ([Cardiac Outlines outline lists EVH](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)).
- **Duration:** about 30–60 min **(uncertain)**.
- **Success:** enough length for 2 grafts (about 40–50 cm **(uncertain)**), no leaks, no varicose segments.
- **Errors:** handling the vein directly, over-distension (endothelial damage), using a varicose segment, forgetting to reverse it (valves then block flow) ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)). Leg-wound infection: **3.1% open vs 1.4% endoscopic** in REGROUP (n = 1,150), with no difference in major adverse cardiac events ([ACC REGROUP summary](https://www.acc.org/Latest-in-Cardiology/Articles/2018/11/07/16/03/sun-630-REGROUP-endoscopic-vein-harvest-aha-2018)).

### Phase D: exposure and cannulation

**D1. Pericardiotomy and pericardial well**
- **Who:** S, A1.
- **Instruments:** cautery, Metzenbaum scissors, forceps, **0 silk stay sutures** ("pop-off" stitches) ([Cardiac Outlines: Pericardial well](https://publish.obsidian.md/cardiacoutlines/Textbook/Creation+of+the+Pericardial+Well)).
- **Real sequence:**
  1. Make an **inverted-T** pericardiotomy.
  2. For CABG, place **three pairs of stays**: at the level where the right atrial appendage touches the aorta, at the inner corners of the inverted T, and at the pericardial reflection over the aorta.
  3. Secure them to the skin or over the retractor. On the side of an in-situ mammary, attach them to a drape with a Kelly clamp so the pleura can still be reached (same source).
- **Duration:** 3–5 min **(uncertain)**.
- **Errors:** injury to the innominate vein or RV, and stays pulled too tight, which tear the pericardium (same source).

**D2. Heparinization**
- **Who:** AN gives it, on the surgeon's request. In some practices S injects it into the right atrium ([Cardiac Outlines: heparin timing](https://publish.obsidian.md/cardiacoutlines/Textbook/Philosophies+in+the+Timing+of+Heparin+Administration)). P is told so that pump suction can be used.
- **Dose:** **300–400 U/kg** unfractionated heparin.
  - The TSRA primer uses **400 U/kg before cannulation** ([TSRA CPB](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
  - The STS/SCA/AmSECT 2018 guideline: weight-based bolus is reasonable (IIa, C) ([PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).
  - A European survey found most centres give 300 IU/kg ([iPerfusion 2026 survey summary](https://iperfusion.org/2026/03/10/) **(uncertain)**).
- **ACT target:**
  - **> 480 s** during CPB (IIa, C). With maximal-activation or microcuvette ACT devices, **> 400 s** is often considered therapeutic (IIa, C) ([STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).
  - The TSRA primer: ACT **> 450 before cannulation** and > 480 for bypass ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
  - The EACTS/EACTAIC/EBCP 2024 guideline: > 480 s is "considered an appropriate threshold" for uncoated circuits with cardiotomy suction ([EACTS 2024 CPB guideline §9.3.1](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
- **Duration:** bolus about 1 min, then ACT check at about 3–5 min **(uncertain)**.
- **Heparin resistance:** give an extra **100 U/kg**, then antithrombin III (concentrate, for example Thrombate III, or FFP) ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)). A proposed definition is failing to reach ACT ≥ 480 after 500 U/kg ([iPerfusion / JTH 2024](https://iperfusion.org/wp-content/uploads/2024/01/PIIS1538783624000072.pdf)). Doses above 400 IU/kg can cause heparin rebound ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).
- **Errors:** **going on pump without an adequate ACT** (catastrophic circuit thrombosis), using pump suction before heparin, a heparin reaction (0.2–5%) ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)), and giving heparin without telling the perfusionist (a reported incident type: [closed-loop incident report summary](https://perfusion.com/?p=37177)).

**D3. Aortic purse-strings**
- **Who:** S, with A1 snaring tourniquets.
- **Instruments:** **2-0 Ethibond** (braided polyester) double-armed sutures (the inner one pledgeted, the outer one not), **Rumel tourniquets** (red rubber Robinson catheter + snare), Kelly clamps, tonsil clamp for traction, **Metzenbaum scissors**, DeBakey forceps ([Cardiac Outlines: aortic purse-string](https://publish.obsidian.md/cardiacoutlines/Textbook/Aortic+Cannulation+Pursestring)).
- **Real sequence:**
  1. Feel the aorta for calcium. Use **epiaortic ultrasound** at a low threshold.
  2. The site is the distal ascending aorta, inner curve near the innominate take-off ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)), leaving room for the cross-clamp.
  3. Place two concentric diamond-shaped purse-strings. Bites go **into the media, not through the full wall**, with about 2 mm between the entry and exit of each bite. The whole site should be no wider than the span of relaxed DeBakey forceps tips.
  4. Incise the adventitia in the centre until the white media shows.

  Source: [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Aortic+Cannulation+Pursestring); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals). A box-shaped pattern made from two pledgeted mattress sutures is an accepted alternative (TSRA).
- **Duration:** 3–5 min **(uncertain)**.
- **Errors:** a full-thickness bite, which causes bleeding, air entry or a hematoma (if it happens: early adventitial incision and pressure). Stitching through calcium or plaque risks embolism or dissection.

**D4. Aortic cannulation**
- **Who:** S cannulates. A1 tightens the Rumels and ties. P connects the line and does the test. AN keeps BP low.
- **Instruments:** **#11 blade** ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)) or **#15 blade** ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Aortic+Cannulation)); arterial cannula (adult sizes **about 18–24 Fr**: [LivaNova conventional cannulae brochure](https://d2wzb2yxq0vcns.cloudfront.net/wp-content/uploads/2021/12/LN_BROCHURE_CONVENTIONAL_CANNUALAE_09295-179-A.pdf)); 0 silk tie; tubing clamps.
- **Real sequence:**
  1. **Systolic BP < 100 mmHg** and **ACT adequate (TSRA: > 450)** before the aortotomy ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [EACTS 2024 §5.1](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  2. Stab incision. **Insert the cannula tip-down at almost the same moment**, with the black orientation line along the direction of flow.
  3. Cinch the Rumels. Tie 0 silk around the cannula and both tourniquets.
  4. De-air the cannula: back-bleed by quick release and reclamp, and tap out bubbles.
  5. Make a "wet-to-wet" connection to the arterial line. The surgeon says **"Bump the pump"**, then **"Off"** when the air is cleared, and confirms with **"Test the line"** ([TSRA, verbatim](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
  6. Check the line pressure and that it shows a pulsatile swing **(uncertain detail)**.
  7. Secure the cannula to the drapes.

  Aortic cannulation **comes before venous** so that volume can be given quickly if the patient becomes unstable ([JOVS review](https://jovs.amegroups.org/article/view/23160/html); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Duration:** 2–5 min **(uncertain)**.
- **Success:** the cannula sits in the true lumen, the line pressure is appropriate, there is no bleeding and no air.
- **Errors/complications:**
  - **Iatrogenic aortic dissection**, incidence about **0.03–0.35%** ([case report literature review, J Cardiothorac Surg 2009](https://cardiothoracicsurgery.biomedcentral.com/articles/10.1186/1749-8090-4-2) **(uncertain: figure taken from a search snippet)**). Signs: sudden high arterial line pressure with low flow, falling systemic pressure, lower venous return, the aorta darkening and enlarging. Response: stop CPB, clamp the lines, confirm on TEE, re-cannulate at another site (femoral or axillary), cool for deep hypothermic circulatory arrest (DHCA) and repair ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).
  - Cannula malposition (against the wall or into an arch vessel), bleeding, air in the line, posterior-wall injury.

**D5. Venous cannulation (dual-stage, right atrium → IVC)**
- **Who:** S makes the atriotomy. A1 inserts or holds the cannula.
- **Instruments:** **single** purse-string (sources vary: 3-0/4-0 Prolene or 2-0 Ethibond **(uncertain)**); regular DeBakey forceps; Metzenbaum scissors; dual-stage cannula with stylet (sizes vary by maker, for example 29/37 or 36/50 Fr: [LivaNova brochure](https://d2wzb2yxq0vcns.cloudfront.net/wp-content/uploads/2021/12/LN_BROCHURE_CONVENTIONAL_CANNUALAE_09295-179-A.pdf)); Rumel; 0 silk.
- **Real sequence:**
  1. Grab the right atrial appendage. Make a small atriotomy "just big enough".
  2. Insert the cannula toward the **IVC** up to its "double line" mark.
  3. Cinch the Rumel and tie it to the cannula ([Cardiac Outlines: venous cannulation](https://publish.obsidian.md/cardiacoutlines/Textbook/Venous+Cannulation)).
  4. The distal basket sits in the IVC and the proximal basket drains the RA and SVC. Drainage is by gravity, with vacuum assist if needed ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Duration:** 2–4 min **(uncertain)**.
- **Errors:** bleeding from the atrium, **air lock** (air in the venous line stops drainage), poor drainage from IVC-dominant positioning, a purse-string so wide that it narrows the cava after decannulation ([CTSNet note](https://www.ctsnet.org/node/54084)), and blockage by the Eustachian valve.

**D6. Antegrade cardioplegia / root-vent cannula**
- **Who:** S, with A1. P flushes the line.
- **Instruments:** **pledgeted 2-0 Ethibond U-stitch** (horizontal mattress), Rumel; **Cooley antegrade catheter ("pigsticker")**; Y-connector to the root vent and the cardioplegia line ([Cardiac Outlines: antegrade](https://publish.obsidian.md/cardiacoutlines/Textbook/Antegrade+Pursetring+and+Insertion+of+Antegrade+Cannula)). Adult root cannulae come in about 5–9 Fr (12–16 Ga) ([LivaNova AR-11112, 9 Fr](https://livanova.com/cannulae/en-gb/adult/cardioplegia-cannulae/antegrade-aortic-root/with-and-whitout-vent-line/ar-11112)).
- **Real sequence:**
  1. **For CABG, place it as low as possible** on the ascending aorta without hitting the RCA ostium, and keep the planned proximal anastomosis sites in mind. For valve cases place it high.
  2. Insert the catheter and attach the Y.
  3. Call **"Root vent on"**, then **"Flush and suck"** to clear air (Cardiac Outlines, verbatim).
- **Duration:** 2–3 min **(uncertain)**.

**D7. Retrograde cardioplegia cannula (coronary sinus) (optional, surgeon preference)**
- **Who:** S.
- **Instruments:** **4-0 Prolene** diamond purse-string on the low RA near the AV groove; retrograde catheter with stylet ([Cardiac Outlines: retrograde](https://publish.obsidian.md/cardiacoutlines/Textbook/Retrograde+Pursetring+and+Insertion+of+Retrograde+Cannula)). Adult balloon catheters are about **14 Fr** with a self- or manually-inflating balloon ([LivaNova RCS-13314](https://www.livanova.com/cannulae/en-us/adult/cardioplegia-cannulae/retrograde/self-inflating-pvc-balloon/rcs-13314)).
- **Real sequence:**
  1. Steer the catheter into the coronary sinus. The tip should point toward the left atrial appendage. A "waggle test" catches malposition into the IVC, RV or posterior vein (Cardiac Outlines).
  2. Confirm the position by palpation or TEE, plus the coronary sinus pressure trace **(uncertain)**.
  3. **Never reinsert the stylet while the catheter is inside the heart** (Cardiac Outlines).
- **Duration:** 2–4 min **(uncertain)**.
- **When used:** especially with LV hypertrophy, **aortic regurgitation** (antegrade cardioplegia leaks into the LV), tight stenoses and significant right coronary disease ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [TSRA Aortic Valve](https://www.aats.org/tsra-primer-aortic-valve)).
- **Errors:** coronary sinus perforation or rupture (from the stylet or from pressure above 40–50 mmHg), malposition leading to poor protection, venous air lock from a sinus injury ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).

### Phase E: bypass and arrest

**E1. Initiate cardiopulmonary bypass**
- **Who:** S orders it. P starts the pump and opens venous drainage. AN stops ventilation and drugs once the heart is empty.
- **Call-outs:** S: **"Go on pump."** P: **"We're at full flow."** Then the team is "ready to stop ventilation" ([Cardiac Outlines: initiate CPB](https://publish.obsidian.md/cardiacoutlines/Textbook/Initiate+Cardiopulmonary+Bypass), verbatim quotes).
- **Targets:**
  - Flow: TSRA gives **2.1–2.5 L/min** ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)). The units read as per m² **(uncertain)**. EACTS says most perfusionists use **2.2–2.8 L/min/m²** under moderate hypothermia to normothermia ([EACTS 2024 §9.5](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  - **MAP 50–80 mmHg** (rule of thumb "MAP ≈ age"). **CVP < 10 mmHg**. Pump-to-cannula gradient **< 100 mmHg**. Non-pulsatile arterial trace ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
  - **DO₂ ≥ 250–300 mL/min/m²** (one analysis suggests about 270). **SvO₂ > 75%** ([EACTS 2024 §9.5](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
- **Duration:** 1–3 min to reach full flow **(uncertain)**.
- **Success:** good venous drainage (stable reservoir level), target flow and pressure reached, good oxygenation, heart decompressed and empty, ventilator off.
- **Errors/complications:**
  - Inadequate drainage: signs are a distended RV, a falling reservoir and high CVP. Causes are a kink, an air lock or a clamp. Fixes: vacuum assist, reposition ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).
  - **High arterial line pressure** is "an ominous sign" (kink, clamp, malposition or dissection).
  - Low MAP from vasoplegia or malposition: give vasopressin or noradrenaline, rarely methylene blue. Vasoplegia occurs after CPB in about 20% (range 2.5–66% depending on the definition) ([vasoplegia meta-analysis, Leiden repository](https://scholarlypublications.universiteitleiden.nl/handle/1887/4253678) **(uncertain: link taken from a search snippet)**).
  - **Reservoir run dry**, which causes massive air embolism. Prevalence of arterial gas embolism during bypass is about 0.003–0.007% ([StatPearls: Arterial Gas Embolism](https://www.statpearls.com/articlelibrary/viewarticle/32891/)).

**E2. Temperature management (cooling)**
- **Who:** P, on the surgeon's instruction.
- **Practice:** CABG is usually done at **mild hypothermia (32–34 °C) or "tepid" or normothermic CPB**. This is surgeon- and centre-dependent **(uncertain)**. Hypothermia is defined as core temperature below 35 °C ([EACTS 2024 §7.6](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
- **Rules:**
  - Heat exchanger to arterial inflow gradient must not exceed **10 °C** ([EACTS 2024 §10.2](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  - The arterial outlet temperature is used as the surrogate for brain temperature (Class I) ([STS/SCA/AmSECT 2015 temperature guideline, JECT](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211)).
  - Alpha-stat (uncorrected) vs pH-stat blood-gas management ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).

**E3. Aortic cross-clamp**
- **Who:** S applies it. P lowers flow briefly while it goes on **(common practice, uncertain)**. Everyone notes the time.
- **Instruments:** aortic cross-clamp (straight or angled, for example Cooley/DeBakey/Fogarty-type **(uncertain eponyms; tray contents vary)**).
- **Real sequence:**
  1. Apply after stable full-flow bypass, between the aortic cannula and the root cardioplegia cannula ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [patent background describing clamp position](https://patents.google.com/patent/US5911728)).
  2. The clamp may cross a little of the main PA as long as **the aorta is fully occluded**. Use two fingers to judge the depth ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Initiate+Cardiopulmonary+Bypass)).
  3. **Ischemic time starts at clamp application** ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Errors:** incomplete clamping (cardioplegia runs off and arrest fails), clamping a calcified segment (embolism or dissection), a clamp that slips.

**E4. Cardioplegic arrest (induction)**
- **Who:** P delivers on the surgeon's order. S checks root pressure and LV distension (by finger and TEE). AN watches the ECG and TEE.
- **Solution:**
  - Classic **4:1 blood:crystalloid (Buckberg) high-potassium cold blood cardioplegia**.
  - **del Nido** (1:4 blood:crystalloid) given as a single dose that lasts **up to 90 min of ischaemia** ([EACTS 2024 §7.5.1](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  - For longer clamp times, del Nido is often redosed at about **60 min** ([del Nido redosing study, PMC8972223](https://pmc.ncbi.nlm.nih.gov/articles/PMC8972223)).
- **Antegrade:** root pressure **60–100 mmHg** ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)). **Arrest within 30–60 s** (TSRA; EACTS: antegrade induction takes 30–60 s).
- **Retrograde:** flow **200–400 mL/min**, **coronary sinus pressure 30–50 mmHg**, avoid higher. Retrograde induction takes 2–4 min ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094)). TSRA gives ≤ 40 mmHg.
- **Volume (one surgeon's rule):** about **1,200 mL antegrade alone**, or **about 1,000 mL antegrade + 500 mL retrograde**. Note the volume at which electrical and mechanical silence is reached, add 100–200 mL, and use that as the maintenance dose ([Cardiac Outlines: cardiac arrest](https://publish.obsidian.md/cardiacoutlines/Textbook/Cardiac+Arrest)).
- **Topical slush** on the RV is an adjunct ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Cardiac+Arrest); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Success:** a flat ECG (asystole), a still heart, a soft and non-distended LV, a full and pressurized root.
- **Errors:**
  - Failure to arrest: check the clamp, give more cardioplegia, cool further ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Cardiac+Arrest)).
  - LV distension from unrecognized aortic regurgitation or from handling the heart in a way that makes the valve leak.
  - Poor distribution beyond tight stenoses, which is why retrograde or down-the-graft doses are used.

### Phase F: grafting (heart arrested, clamp on)

**F1. Target identification and exposure**
- **Who:** S, with A1 positioning the heart.
- **Real technique:**
  - LAD and diagonals: a cold wet sponge behind the heart.
  - Circumflex and OMs: lift the apex toward the midline and rotate counter-clockwise. The left atrial appendage marks the circumflex course.
  - RCA and PDA: Trendelenburg, apex toward the right shoulder ([TSRA targets](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)).
  - Pick a soft, disease-free segment of good calibre beyond the stenosis, ideally marked out before cardioplegia (same source).
- **Instruments:** laparotomy sponges, heart holder or "jock", **Parsonnet (eyelash) epicardial retractor** ([Cardiac Outlines primer](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)).

**F2. Distal anastomoses: SVG→RCA/PDA and SVG→OM**
- **Who:** S sews. A1 holds the conduit, follows the suture and runs the blower. SN loads sutures. P gives maintenance cardioplegia on request.
- **Instruments:**
  - **Castroviejo needle holder** (round handles for distals).
  - **Coronary DeBakey**, **Gerald** and **Mills** forceps; Gold forceps for the needle.
  - **Beaver (Wechsler) blade** or #11/#15 blade.
  - **Potts / Diethrich coronary scissors**, forward and reverse angles.
  - **Coronary probes**, nerve hook, **blower/mister** (humidified CO₂), Frazier suction.
  - **7-0 Prolene double-armed** suture.

  Sources: [Cardiac Outlines anastomosis primer](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer); [TSRA anastomoses](https://www.aats.org/tsra-primer-coronary-artery-anastomoses); [Scanlan A/V-access catalog listing Gerald forceps and micro needle holders](https://www.scanlaninternational.com/wp-content/uploads/2023/11/mk-b-avAccess_revB.pdf). Some surgeons use **8-0** for small targets (< 1.2 mm) ([PMC5147479](https://pmc.ncbi.nlm.nih.gov/articles/PMC5147479)).
- **Real sequence:**
  1. Turn the root vent off.
  2. Arteriotomy: "stroker" blade through the epicardium, a "poker" blade at about 30°, then extend with Potts scissors to about **1.5× the coronary diameter**, sized to the conduit ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)).
  3. Probe beyond the arteriotomy to confirm there is no further stenosis downstream.
  4. Bevel the conduit to about **30–45°** ([TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses); [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)).
  5. Sew with the **parachute technique**: start at the heel, place several loops, then lower the graft. Run around the toe. Usually about **12 passes** in all ("along each hour of the clock") ([TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses)).
  6. Flush the graft to de-air and check for leaks before tying. Repair leaks with an interrupted 7-0 stitch (TSRA).
  7. Give cardioplegia down the vein graft after the distal is done, and/or into the root or retrograde ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)).
- **Order:** commonly **right-sided and circumflex targets first, LAD last** ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)). This puts the LIMA on last, so the heart is not lifted again and the pedicle is not stretched **(rationale uncertain)**.
- **Maintenance cardioplegia:** every **20–30 min** ([EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094)) or about every **20 min**, aiming for root pressure about 70 mmHg during antegrade dosing ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Duration:** about 8–15 min per hand-sewn distal **(uncertain)**. A beating-heart LIMA–LAD series measured a mean of **8.6 min (range 5–14)** ([HSF U-CLIP series](https://journal.hsforum.com/index.php/HSF/article/view/6019) **(uncertain: link taken from a search snippet)**).
- **Success:** a patent, leak-free anastomosis without narrowing, a good-sized "hood", a graft with no twist or kink, the right length, and no back-wall bite.
- **Errors:**
  - **Catching the back wall** (narrowing or occlusion), partial-thickness "skiving" bites, purse-stringing (too few or too tight stitches), "seagulling" at sequential sites, an oversized arteriotomy.
  - Grabbing the needle by its tip; lifting the whole hand and tearing the wall.
  - Too much blower or suction, which dries or damages the endothelium.
  - Leaving valves in a vein that was not reversed; wrong graft length; twisted conduit.

  (From [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer) and [TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses).) Clinical result: graft failure, which shows as perioperative MI, ST changes, regional wall-motion abnormality on TEE or failure to wean.

**F3. LIMA→LAD distal anastomosis**
- Same as F2, plus the following:
  - Take the bulldog off and check pulsatile flow. Trim to a hooded oblique cuff with Potts scissors ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets)).
  - Sew with **7-0 Prolene**, parachute technique. Tack the pedicle wings to the epicardium with **6-0 Prolene**, avoiding coronary branches ([TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses)).
  - Release the bulldog, check for leaks and watch the ECG and wall motion once flow returns **(uncertain)**.
  - Check the length with the lungs inflated and the heart filled ("have the perfusionist fill the heart" to size grafts: TSRA).
- **Errors:** LIMA under tension (avulsion or kinking when the lung inflates), spasm, intimal flap, wrong target (for example a diagonal mistaken for the LAD) **(uncertain example)**.

**F4. Start rewarming**
- **Who:** S tells P, usually during the last distal or at the proximals **(uncertain timing)**.
- **Rules:** rewarming rate **≤ 0.5 °C/min**. Arterial outlet to venous inflow gradient **≤ 4 °C** at the separation temperature, and a maximum of **10 °C** when the outlet is below 30 °C ([STS/SCA/AmSECT 2015 temperature guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211)). Avoid cerebral hyperthermia above 37 °C. Slow rewarming is associated with less postoperative cognitive dysfunction ([EACTS 2024 §7.6](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).

**F5. Proximal anastomoses (vein grafts to the ascending aorta)**
- **Who:** S, A1. P adjusts pressure or flow on request.
- **Instruments:** #11 blade, **aortic punch** (common sizes about 4.0–4.8 mm **(uncertain)**), **6-0 Prolene**, side-biting (partial-occlusion, Satinsky-type) clamp if used, radio-opaque marker rings (optional) ([TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses); [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)).
- **Two strategies:**
  1. **Single cross-clamp:** sew the proximals while the aorta is still clamped and the heart arrested.
  2. **Clamp off, then side-biting clamp:** lower the pressure while the partial clamp goes on, then sew on the beating, reperfused heart.
- **Evidence:**
  - Mayo cohort (about 8,500 patients): stroke **1.2% single vs 1.5% partial clamp**, not significant ([Mayo study](https://mayoclinic.elsevierpure.com/en/publications/on-pump-coronary-artery-bypass-graft-operation-is-one-crossclamp-)).
  - An Emory case-control study suggested fewer strokes with a single clamp (OR 0.385) ([Emory ETD](https://etd.library.emory.edu/concern/etds/n296x0120)).
  - Partial clamping did not raise stroke rates in patients without aortic plaque ([CVJA 2013, PMC3767939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3767939/)).

  The game could offer both strategies.
- **Real sequence:**
  1. Feel for a soft, calcium-free spot.
  2. Make a 3–4 mm stab with the #11 blade, then punch a round hole. **Remove the punched-out disc** so it cannot embolize.
  3. Cut the graft end as a wide hood at about 30° to the aorta, with an opening about 20% larger than the aortotomy.
  4. Sew with 6-0 Prolene, parachute technique, taking large full-thickness aortic bites (to lower the dissection risk) ([TSRA](https://www.aats.org/tsra-primer-coronary-artery-anastomoses)).
  5. Right-sided grafts leave the right side of the aorta at about 90°. Left-sided grafts angle toward the left shoulder. Avoid a "proud" graft that stands up and can kink ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)).
  6. De-air each graft before tying (with a fine needle, or by back-bleeding) **(uncertain detail)**.
- **Duration:** about 5–10 min each **(uncertain)**.
- **Errors:** aortic dissection from a stitch or the side clamp; embolism from calcium or the punched disc; graft kink, twist or tension; length errors ("a thousand too long before one too short": [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer)); air left in the graft.

### Phase G: reperfusion

**G1. Terminal warm cardioplegia ("hot shot") (optional)**
- Warm (37 °C) blood cardioplegia just before unclamping. One RCT gave **500 mL at 37 °C over 2 min into the root at 50 mmHg** ([Suleiman et al., Eur J Cardiothorac Surg 1998](https://academic.oup.com/ejcts/article/13/5/559/418042) **(uncertain: link taken from a search snippet)**). Small trials suggest less need for inotropes and fewer ventricular arrhythmias ([Brieflands trial](https://brieflands.com/articles/mca-8723)).

**G2. De-airing**
- **Who:** S directs. AN inflates the lungs and checks TEE. P adjusts venous drainage and vent suction.
- **Technique:**
  1. **Trendelenburg (head down)**.
  2. **Root vent suction on** before and after the clamp comes off.
  3. Inflate the lungs to push air out of the pulmonary veins **(uncertain: common practice; not found in the sources reached)**.
  4. TEE target: **no air visible in the left heart** ([CO₂ vs Lund de-airing trial, NCT00934596](https://clinicaltrials.gov/study/NCT00934596); [Trendelenburg + root vent report](https://www.redalyc.org/journal/3989/398975126015/)).
- CO₂ flooding of the field lowers gaseous microemboli (risk difference −0.94) ([EACTS 2024 §4.4](https://pmc.ncbi.nlm.nih.gov/articles/11826094)). A root-vent rate of about 300 mL/min is commonly used, but evidence for it is thin ([AACP abstract](https://www.theaacp.com/wp-content/uploads/2020/03/Trafford-Abstract.docx)).
- **Errors:** **air embolism**. Coronary air (often into the RCA because it sits uppermost) causes inferior ST elevation and RV dysfunction **(uncertain)**. Cerebral air causes stroke. Response for massive air embolism: stop CPB, steep head-down, de-air the lines, **retrograde cerebral perfusion at 20 °C, 1–2 L/min for 2–3 min**, then cool; consider hyperbaric O₂ after surgery ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).

**G3. Cross-clamp removal**
- **Who:** S removes it. P briefly lowers flow or pressure while it comes off **(uncertain)**. The cross-clamp time is announced and recorded.
- **Real sequence (TSRA):** de-air, lower flows briefly, release the cross-clamp, then return to full support ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Success:** the heart reperfuses, colour comes back, and electrical activity resumes.

**G4. Rhythm recovery and defibrillation**
- **Who:** S uses the internal paddles. AN or CN charges the defibrillator. AN gives antiarrhythmics.
- **Facts:**
  - **Reperfusion VF is common after cold cardioplegia.** Older series cite 70–96% in CABG ([IRCMJ 2010 RCT background](https://search.bvsalud.org/gim/resource/en/emr-105553) **(uncertain)**).
  - Magnesium or lidocaine before unclamping lowers the incidence. In one 76-patient RCT, VF was 12% with magnesium vs 26.9% with lidocaine vs 44% with saline (same source).
  - **Internal defibrillation 10–20 J** as the first shock. In an RCT of 202 patients, 10 J succeeded more often than 5 J (93% vs 81%) ([Klein et al., indexed record](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....25e8b45ca57efa79780420d38511ccfe) **(uncertain: link taken from a search snippet)**).
  - Success also depends on temperature, oxygenation and electrolytes ([PMC7525868](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525868)).
- **Errors:** repeated shocks (myocardial injury), shocking a cold heart, uncorrected low potassium.

**G5. Temporary epicardial pacing wires**
- **Who:** S or A1.
- **Real sequence:**
  - **Atrial wires on the right atrium (appendage); ventricular wires on the diaphragmatic surface of the RV.** Bring them out through the skin below the incision ([Reade / PMC2840753 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC2840753)).
  - Connect to an external pacing box. Typical teaching settings are **DDD/AAI/VVI, lower rate 80/min, output 10 mA, sensitivity 2–5 mV**, or twice the capture threshold ([LITFL temporary epicardial pacing](https://litfl.com/temporary-epicardial-cardiac-pacing/)).
- **Duration:** 2–5 min **(uncertain)**.
- **Errors:** bleeding from the RV, failure to capture or sense, later tamponade when the wires are pulled.

**G6. Inspect grafts and posterior anastomoses**
- Check the graft lie, length and flow. Check for hemostasis at the back of the heart **while still on bypass**, because lifting the heart after weaning is poorly tolerated ([Cardiac Outlines outline: "check anastomoses for hemostasis"](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)).

### Phase H: weaning from CPB

**H1. Pre-separation checklist**
- **Who:** AN, P and S together.
- **TSRA "BBB/WWW":** **Breathing** (ventilator back on), **Beating** (heart ejecting), **Bleeding** (acceptable), **Warm** (normothermic), **Working** (good haemodynamics), **Wires** (native rhythm checked; A and/or V wires if there is heart block) ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Typical numeric targets (mostly teaching sources):**
  - Core (bladder) temperature **> 36 °C** ([lecture/flashcard sources](https://brainscape.com/flashcards/seperation-from-cbp-4728992/packs/6940444), low-quality, **(uncertain)**).
  - **K⁺ 4–5 mmol/L**; ionized Ca²⁺ **> 1.0 mmol/L** **(uncertain)**.
  - Paced or sinus rate **80–90/min** **(uncertain)**.
  - Haemoglobin and acid–base corrected; TEE shows the heart is de-aired, ventricular function and valves are OK, and there are no new wall-motion defects.
  - An alternative mnemonic is "C-V-P" (Cold/Conduction/Calcium/Cardiac output; Ventilation/Volatile/Volume/Visualize; Predictors/Protamine/Pressors/Pacer/Potassium) ([same flashcards](https://brainscape.com/flashcards/seperation-from-cbp-4728992/packs/6940444)).
- **Remove the cardioplegia catheters** (retrograde first) before the final wean ([Cardiac Outlines outline](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)).

**H2. Separation**
- **Who:** S calls it. P does it. AN manages drugs and volume.
- **Real sequence:**
  1. P **partly occludes the venous line** so blood volume moves into the patient, and **lowers arterial flow stepwise**, for example full → 2 → 1 → off **(illustrative values)**. TSRA: "Reduce arterial outflow and venous return stepwise, then clamp the venous line and stop the pump" ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
  2. Lungs are re-inflated and ventilated before support ends ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).
  3. AN titrates inotropes and vasopressors, assessed by TEE.
  4. After separation, P can **give volume through the still-inserted aortic cannula** in small boluses ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Duration:** 2–10 min **(uncertain)**.
- **Success:** stable MAP (for example 65–80 mmHg **(uncertain)**), adequate cardiac index, stable rhythm, no new regional wall-motion abnormality, reasonable filling pressures.
- **Errors/complications:**
  - **Failure to wean**: LV or RV failure, graft problem, vasoplegia, air, hyperkalaemia or arrhythmia. Response: **go back on bypass**, rest the heart, correct the cause, add inotropes, consider an IABP. Also re-check the grafts.
  - Low cardiac output syndrome is defined as CI below 2.4 L/min/m² with end-organ dysfunction ([EACTS 2024 §9.11.6](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  - Expert review notes "a sizable number" of patients are difficult to wean ([Licker et al. 2012 review, via DOAJ](https://doaj.org/article/1bad10d7212348eb808263c7099b3b86)).

### Phase I: reversal and decannulation

**I1. Venous decannulation**
- **Who:** S removes the cannula. A1 ties.
- **Order:** **venous first, then the root vent and cardioplegia cannulae, then the arterial cannula last**. Keep the venous purse-string ready, because the patient may need to go back on bypass ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).

**I2. Protamine**
- **Who:** AN gives it, after telling S and P. P **turns off the pump suckers** once protamine starts, so protamine-bound blood does not enter the circuit (standard practice; exact timing varies, for example after the test dose or after a third of the dose) ([Egyptian study on test dose and sucker timing](https://ejhm.journals.ekb.eg/article_441844_87c72efd1459b122c741f74b3a1101ff.pdf) **(uncertain)**).
- **Dose:**
  - Conventionally **1 mg per 100 U of heparin** (1:1 with the initial dose) ([NCT07477977](https://clinicaltrials.gov/study/NCT07477977)).
  - Titration to the remaining heparin is beneficial (IIa, B). **Keep the ratio below 2.6 mg per 100 U** (IIa, C) ([STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).
  - EACTS 2024 advises a protamine:heparin ratio **< 1.0** ([EACTS 2024 §9.3.2](https://pmc.ncbi.nlm.nih.gov/articles/11826094)).
  - Infuse over **5–10 min** ([NCT07477977](https://clinicaltrials.gov/study/NCT07477977)) after a slow test dose ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)).
- **ACT:** back to baseline, within about ±10%. Give 25–50 mg more if it is not ([trial protocols summarized via iPerfusion/JECT](https://ject.edpsciences.org/10.1051/ject/201345235/pdf) **(uncertain)**).
- **Protamine reactions** ([TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting)):
  - **Type I** (histamine, from giving it too fast): low systemic BP and low PA pressure. Treat with vasoconstrictors and by giving it slower.
  - **Type II** (anaphylactic): stop protamine and give inotropes and vasoconstrictors.
  - **Type III** (catastrophic pulmonary vasoconstriction): **high PA pressure**, RV failure. Give 100% O₂, a pulmonary vasodilator and inotropes. **Resume CPB** if needed, which is "may be lifesaving" (Class I in [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).
- **Heparin rebound:** a protamine infusion of 25 mg/h for up to 6 h may be considered (IIb) ([STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)).

**I3. Aortic decannulation**
- **Who:** S; A1 ties.
- **Real sequence:** give the last volume from the pump through the cannula ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)). Lower systolic BP to about < 100 mmHg **(uncertain, by analogy with cannulation)**. Remove the cannula and tie both purse-strings, adding a pledgeted stitch if it bleeds.
- **Errors:** tearing the aorta or dissection, a bleeding purse-string, sudden hypertension at removal.

### Phase J: hemostasis and closure

**J1. Hemostasis "ritual"**
- **Who:** S and A1. AN gives blood products and factors based on labs.
- **Checklist:** cannulation sites; every proximal and distal anastomosis; graft side branches; **the LIMA bed (re-check after protamine)**; sternal edges and periosteum; thymus remnant; pericardial edges; pacing-wire sites; the left pleura if it was opened ([TSRA](https://www.aats.org/tsra-primer-mammary-takedown-saphenous-vein-harvest-and-targets); [VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)).
- **Duration:** 10–30 min **(uncertain)**.
- **Errors:** missed bleeding leads to **re-exploration**. STS "any re-operation" for isolated CABG is **2.70%** (2025); bleeding is one main cause ([STS rates](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf)). Tamponade causes hypotension after surgery ([VUMC pitfalls](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)).

**J2. Chest tubes**
- **Who:** S or A1.
- **Real setup:**
  - One **anterior mediastinal** tube, often plus one **posterior pericardial** tube, plus a **left pleural** tube if the pleura was opened for the LIMA.
  - Each tube exits through the skin of the upper abdomen below the incision and is sutured in place ([VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf); [rk.md summary listing posterior pericardium, anterior mediastinum and both pleural cavities](https://rk.md/2017/surgical-steps-coronary-artery-bypass-grafting-cabg/)).
  - **28 Fr** is a typical standard size (RCT protocol: [NCT02808897](https://clinicaltrials.gov/study/NCT02808897)). Larger tubes (around 32–36 Fr) have historically been common ([vendor note](https://clearflow.com/is-bigger-better/), low-quality).
- **Errors:** a clogged tube with retained blood, causing tamponade; a misplaced tube.

**J3. Sternal closure**
- **Who:** S or A1. SN counts the wires and needles.
- **Instruments:** **stainless-steel sternal wires about 1 mm (USP #5) on heavy needles**, wire twister or heavy needle holder, wire cutter, Kocher clamps ([VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)).
- **Real sequence (VUMC):**
  1. Pass **2 wires through the manubrium and 4 through the sternum**, either transsternal (through the bone) or peristernal (around it, through the intercostal spaces). Do **not injure the internal mammary vessels**.
  2. Clamp each wire end and cross the wires.
  3. Pull all wires up and apart to bring the halves together, then twist each one.
  4. Tighten by **pulling up, then twisting**, because twisting alone breaks the wire.
  5. Cut and crimp the ends down flush with the bone.

  Many surgeons use 6–8 wires, with figure-of-eight wires for heavier patients **(uncertain)**. Bands or plates are used for high-risk sterna (VUMC; [TSRA Setting Up mentions plating](https://www.aats.org/tsra-primer-setting-up)). A figure-of-eight stitch closes the xiphoid fascia ([Cardiac Outlines outline](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)).
- **Errors:** an off-midline or loose closure leading to non-union or dehiscence. **DSWI is 0.245%** in isolated CABG ([STS rates](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf)). Wire injury to the IMA or graft; wire ends cutting through the skin.

**J4. Soft-tissue closure and dressings**
- **Real sequence:** close the periosteal or fascial layer, then interrupted absorbable subcutaneous sutures, then a **running absorbable subcuticular** skin closure or staples ([VUMC](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf)). The "five-minute rule" check comes before the dermal layer ([Cardiac Outlines outline](https://publish.obsidian.md/cardiacoutlines/Textbook/300+Technical+Outline+of+Coronary+Artery+Bypass+Grafting)). Leg incisions are closed in layers. Chest and leg dressings go on.
- **Duration:** 15–30 min **(uncertain)**.

**J5. WHO Sign-Out**
- **Who:** CN reads; S, AN and SN answer.
- **Items:** procedure name, **instrument, sponge and needle counts correct**, specimen labelling, equipment problems, and the key concerns for recovery ([WHO checklist items](https://en.wikipedia.org/wiki/WHO_Surgical_Safety_Checklist)).

### Phase K: transfer to ICU

- **Who:** AN, S or A1, CN, plus ICU staff.
- **Real sequence:**
  1. The patient is usually still **intubated and sedated** and is moved onto transport monitors (arterial line, ECG, SpO₂).
  2. The **pacing box** and its connections go with the patient, along with the chest-tube drainage system and the infusions (inotropes, vasopressors, sedation).
  3. On arrival, a structured handoff covers the procedure, grafts, clamp and bypass times, drugs, bleeding, products given, rhythm and pacing, and concerns **(uncertain: general practice)**.
- **Outcome anchors (STS 2025, isolated CABG):** prolonged ventilation 5.16%, renal failure 1.95%, stroke 1.22%, operative mortality 2.05%; 46.7% go home in under 6 days ([STS rates](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf)).

---

## 5. Parameter table for the physiology and perfusion model

| Parameter | Target / range | Source |
|---|---|---|
| Heparin bolus | 300–400 U/kg (TSRA: 400) | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) |
| ACT before cannulation / on CPB | > 450 s / > 480 s (> 400 s with some devices) | [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Heparin resistance top-up | +100 U/kg, then AT III / FFP | [TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting) |
| Systolic BP for aortic cannulation | < 100 mmHg | [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Pump flow | 2.2–2.8 L/min/m² (TSRA: 2.1–2.5) | [EACTS 2024 §9.5](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| MAP on CPB | 50–80 mmHg ("≈ age"); ≥ 50–60 | [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals); [TSRA troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting) |
| CVP on CPB | < 10 mmHg | [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) |
| Pump–cannula pressure gradient | < 100 mmHg | [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) |
| DO₂ | ≥ 250–300 mL/min/m² (about 270–273 suggested) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| SvO₂ | > 75% | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Haematocrit / Hb on CPB | Accept Hct 21–24% if DO₂ > 273; transfuse if Hb < 6.0 g/dL | [EACTS 2024 §9.9](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Cooling / rewarming gradient | ≤ 10 °C (heat exchanger vs arterial inflow); ≤ 4 °C outlet–venous at separation temperature | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094); [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) |
| Rewarming rate | ≤ 0.5 °C/min | [STS 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211) |
| CABG CPB temperature | 32–34 °C or tepid/normothermic **(uncertain)** | practice-dependent |
| Separation temperature | core > 36 °C **(uncertain)** | teaching sources |
| Antegrade cardioplegia root pressure | 60–100 mmHg (about 70 during maintenance) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094); [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) |
| Retrograde flow / coronary sinus pressure | 200–400 mL/min / 30–50 mmHg (TSRA ≤ 40) | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Time to arrest | antegrade 30–60 s; retrograde 2–4 min | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Induction volume | about 1,200 mL antegrade, or 1,000 antegrade + 500 retrograde | [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Cardiac+Arrest) |
| Redosing | blood cardioplegia every 20–30 min (TSRA about 20); del Nido single dose up to 90 min, redose about 60 min if long | [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094); [PMC8972223](https://pmc.ncbi.nlm.nih.gov/articles/PMC8972223) |
| Hot shot | 500 mL, 37 °C, over 2 min, at 50 mmHg | [Suleiman 1998](https://academic.oup.com/ejcts/article/13/5/559/418042) **(uncertain)** |
| Internal defibrillation | 10–20 J first shock | [Klein et al.](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....25e8b45ca57efa79780420d38511ccfe) **(uncertain)** |
| Temporary pacing | DDD, 80/min, 10 mA, sensing 2–5 mV (teaching defaults) | [LITFL](https://litfl.com/temporary-epicardial-cardiac-pacing/) |
| Protamine | 1 mg/100 U heparin (ratio ≤ 1; never > 2.6 mg/100 U), over 5–10 min | [STS 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589); [EACTS 2024](https://pmc.ncbi.nlm.nih.gov/articles/11826094); [NCT07477977](https://clinicaltrials.gov/study/NCT07477977) |
| High potassium threshold on CPB | > 6.5–7 mmol/L: treat (ultrafiltration, calcium, insulin) | [EACTS 2024 §10.3.2](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |
| Lactate | > 4 mmol/L hyperlactataemia flag | [EACTS 2024 §10.3](https://pmc.ncbi.nlm.nih.gov/articles/11826094) |

---

## 6. Typical total times (measured anchors)

| Metric | Value | Source |
|---|---|---|
| Aortic cross-clamp time, isolated CABG | **Mean 67–73 min** (STS 2002–2005, about 370k pts: 67.4 non-teaching, 73.1 teaching) | [PMID 17532407](https://pubmed.ncbi.nlm.nih.gov/17532407/) |
| CPB (perfusion) time, isolated CABG | **Mean 98–105 min** (same STS study) | [PMID 17532407](https://pubmed.ncbi.nlm.nih.gov/17532407/) |
| Cross-clamp / CPB (STS-definition registry, Brazil) | 69 ± 26 / 100 ± 35 min | [REPLICCAR II, PMC10389413](https://pmc.ncbi.nlm.nih.gov/articles/PMC10389413/table/T2) |
| Skin-to-skin, on-pump CABG | **Median 240 min (IQR 195–275)** in a 51-patient series | [J Cardiothorac Surg 2020](https://cardiothoracicsurgery.biomedcentral.com/articles/10.1186/s13019-020-1057-x/tables/2) |
| Skin-to-skin by experience | about 180 min (senior) vs about 234 min (new residents), 16,486 cases | search-snippet summary **(uncertain: primary source not reached)** |
| "Duration of surgery", on-pump (MASS III RCT) | about 300 ± 87.5 min (off-pump about 240) | search-snippet summary **(uncertain)** |
| LIMA harvest | 20.2 ± 5.4 min (pedicled), 28.6 ± 8.7 min (skeletonized) | [PMC11139514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11139514/) |
| One distal anastomosis | about 8–15 min (beating-heart LIMA–LAD mean 8.6, range 5–14) | **(uncertain)** |
| Room entry → incision | about 45–90 min | **(uncertain)** |
| Total time in room | about 5–6 h | **(uncertain)** |

Design note: a full-length session would last 4–6 hours. The design step must choose between time compression, skippable or automated phases ("the assistant closes"), and a "key moments" mode.

---

## 7. What people say in the real OR (call-outs)

Real cardiac ORs use **closed-loop communication**. A command is repeated back ("read back") before it is carried out:

- A study of CABG audio and video found **64 items** that clinicians consider critical to say out loud. Most critical-event talk happens in **call-back loops between two sub-teams** (surgical ↔ perfusion ↔ anaesthesia) ([de Lind van Wijngaarden et al., Semin Thorac Cardiovasc Surg 2019, doi:10.1053/j.semtcvs.2018.12.001](https://research.tudelft.nl/en/publications/developing-a-quality-standard-for-verbal-communication-during-cab/)).
- In paediatric open-heart cases, closed-loop talk happened mainly between **surgeon and perfusionist**. That pair made up about 12.4% of all exchanges ([perfusion.com summary](https://perfusion.com/?p=37177)).
- AmSECT standards require protocol-driven, closed-loop communication ([AmSECT Standards & Guidelines 2017](https://www.theaacp.com/wp-content/uploads/2017/11/AmSECT_Perfusion_SG_legal_ICEBP_final_2017.pdf)).
- There is **no single national script**. Wording varies by hospital ([JECT 2025 commentary calls for standard terminology](https://ject.edpsciences.org/articles/ject/pdf/forth/ject250077.pdf) **(uncertain: which commentary)**).

**Call-out script for the game.** "V" = the wording is quoted in a source. "I" = illustrative wording that reflects common practice but is not verbatim from a source **(uncertain)**.

| Moment | Speaker → listener | Call-out | Expected read-back / response | Src |
|---|---|---|---|---|
| Time-out | CN → all | "Time-out. Patient name…, procedure…, antibiotics given at…" | Each role confirms | WHO (I) |
| Sternotomy | S → AN | "Hold ventilation, please." / "Lungs down." | AN: "Ventilation held." … S: "Resume ventilation." | [TSRA](https://www.aats.org/tsra-primer-setting-up) (paraphrased) / I |
| Heparin | S → AN | "Heparin, please: full dose." | AN: "Heparin is in, 32,000 units, at [time]." P: "Pump suckers on after ACT." | [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Philosophies+in+the+Timing+of+Heparin+Administration) (I) |
| ACT | P → S | "ACT is 520." | S: "Thank you, cannulating." | I |
| Cannulation BP | S → AN | "Bring the pressure down for cannulation." | AN: "Systolic is 95." | I (target from TSRA) |
| Aortic line test | S → P | **"Bump the pump."** … **"Off."** … **"Test the line."** | P: line pressure value, "line is good" | **V** [TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals) |
| Root vent | S → P | **"Root vent on."** … **"Flush and suck."** | P: "Root vent on." | **V** [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Antegrade+Pursetring+and+Insertion+of+Antegrade+Cannula) |
| Go on bypass | S → P | **"Go on pump."** | P: "Going on… **We're at full flow.**" | **V** [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Initiate+Cardiopulmonary+Bypass) |
| Stop ventilation | P/S → AN | "Full flow, you can stop ventilating." | AN: "Ventilator off." | V (concept) / I |
| Cooling | S → P | "Let's drift to 34." | P: "Cooling to 34." | I |
| Cross-clamp | S → P | "Come down for the clamp." … "**Clamp on.**" | P: "Flow down." … "Clamp on at [time], back to full flow." | I |
| Cardioplegia | S → P | "Give antegrade cardioplegia." | P: root pressure and volume updates; "**antegrade dose complete, X mL**" | V (concept: [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Cardiac+Arrest)) / I |
| Switch to retrograde | S → P | "Retrograde, 500 please." | P: "Retrograde, coronary sinus pressure 35." | V (concept) / I |
| Maintenance dose | S → P | "Give a dose down the vein graft." / "Root dose." | P: "Cardioplegia in… complete." | I |
| Ischaemic time | P → S | "Twenty minutes since last dose." | S: "Dose after this distal." | I (interval from EACTS/TSRA) |
| Rewarming | S → P | "Start warming." | P: "Rewarming; gradient under 4." | I |
| Hot shot | S → P | "Hot shot, please." | P: "Hot shot going, 500 mL." | I |
| De-air / unclamp | S → AN/P | "Head down, inflate the lungs, root vent up. **Clamp coming off.**" | P: "Clamp off at [time]; clamp time 68 minutes." | I |
| VF | S → CN/AN | "Paddles, 10 joules." … "Clear. Shocking." | CN: "Charged at 10." | I |
| Pacing | S → AN | "Pace DDD at 80." | AN: "Pacing DDD 80, capturing." | I |
| Pre-wean | S → all | "Ventilate. Are we ready to come off?" | AN: "Ventilating, K 4.6, Ca 1.1, temp 36.5." P: "Ready." | V (concept BBB/WWW) / I |
| Weaning | S → P | "Come down to half… one liter… **come off.**" | P: "Half flow… one liter… **off bypass** at [time]." | I (stepwise per TSRA) |
| Volume | S → P | "Give 100 from the pump." | P: "100 in." | I (concept TSRA) |
| Protamine | S → AN/P | "Test dose of protamine." … "Start protamine." | AN: "Protamine started." P: "**Pump suckers off.**" | I |
| Decannulation | S → P | "Venous cannula out." … "Aortic cannula coming out." | P: "Venous line clamped." | I (order from TSRA) |
| Counts | SN/CN → S | "Counts correct." | S: "Thank you." | WHO sign-out (I) |

Game hooks:
- Every critical action needs its command, and the right read-back must follow.
- A missing read-back raises a risk modifier. One example is going on pump without "ACT OK".
- Sources for the event list: the 64-item standard (only its existence and categories were confirmed, not the item text) and the 41-item CPB checklist ([JECT 2025, CC BY 4.0](https://doi.org/10.1051/ject/2024030)).

---

## 8. Complication catalogue for the outcome engine

| Event | Trigger in the game (example) | Real base rate / data | Real response |
|---|---|---|---|
| Iatrogenic aortic dissection | Cannulating with SBP > 100, deep bite, high line pressure, partial clamp on a diseased aorta | about 0.03–0.35% **(uncertain)** | Stop CPB, TEE, femoral/axillary re-cannulation, DHCA repair ([TSRA](https://www.aats.org/tsra-primer-cpb-troubleshooting)) |
| Massive arterial air embolism | Reservoir runs dry, loose connection, poor de-airing | 0.003–0.007% ([StatPearls](https://www.statpearls.com/articlelibrary/viewarticle/32891/)) | Stop CPB, head-down, retrograde cerebral perfusion, re-prime ([TSRA](https://www.aats.org/tsra-primer-cpb-troubleshooting)) |
| Venous air lock / poor drainage | Atrial injury, kinked line | not quantified | Fix the injury, lift the lines, vacuum, reposition |
| Heparin resistance | Random or by profile (AT III deficiency, prior heparin infusion) | common; definition ≥ 480 s not reached after 500 U/kg | +100 U/kg, then AT III/FFP |
| Failure to arrest / LV distension | Incomplete clamp, aortic regurgitation | not quantified | Re-clamp, retrograde cardioplegia, vent |
| Graft failure / poor anastomosis | Back-wall bite, twist, kink, wrong length, poor target | not quantified here (perioperative MI rates **(uncertain)**) | Redo the anastomosis, add a graft, IABP |
| Reperfusion VF | Cold heart, hypokalaemia, no Mg/lidocaine | 70–96% in older CABG series **(uncertain)** | Internal shock 10–20 J |
| Vasoplegia | ACE inhibitor before surgery, long CPB | about 20% (2.5–66%) | Noradrenaline, vasopressin, methylene blue |
| Failure to wean / low output | Poor protection, long clamp, graft issue | "sizable number" | Back on pump, inotropes, IABP |
| Protamine reaction (Type III) | Random, fast infusion | 3 types ([TSRA](https://www.aats.org/tsra-primer-cpb-troubleshooting)) | Stop, pulmonary vasodilator, back on CPB |
| Bleeding → re-exploration | Poor hemostasis, under-reversal | any re-op 2.70% (STS 2025) | Re-explore |
| Stroke | Aortic manipulation, air, clamping | 1.22% (STS 2025) | Outcome only |
| DSWI | Poor closure, obesity, diabetes, bilateral IMA | 0.245% (STS 2025) | Outcome only |
| Operative death | Combination of the above | 2.05% (STS 2025) | Outcome |

STS figures are from [STS ACSD 25H4](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf).

---

## 9. Later procedures: what changes from the CABG pipeline

### 9.1 Surgical aortic valve replacement (v2)

- **Cannulation:** usually a single dual-stage venous cannula plus an **LV vent** through the right superior pulmonary vein ([Trifecta technique paper, PMC3781796](https://pmc.ncbi.nlm.nih.gov/articles/PMC3781796); [TSRA venting](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)). The aortic cannula goes higher, near the arch, to leave room for the aortotomy.
- **Cardioplegia:** **antegrade into the root does not work with significant aortic regurgitation**. Use retrograde, and/or direct coronary ostial cannulation after the aortotomy ([TSRA Aortic Valve](https://www.aats.org/tsra-primer-aortic-valve)).
- **New steps:**
  1. **Transverse or "hockey-stick" aortotomy** about 1–2 cm above the sinotubular junction.
  2. Leaflet excision.
  3. **Annular decalcification**, which prevents paravalvular leak; capture the debris.
  4. **Sizing** with valve-specific sizers ("the largest that fits without force").
  5. **Interrupted pledgeted horizontal-mattress 2-0 Ethibond** sutures placed all around the annulus. Pledgets go on the ventricular side for supra-annular valves. One series used a median of 14 pledgeted sutures (range 11–23) ([PMC search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC3548539) **(uncertain)**).
  6. Seat the valve sinus by sinus (left → right → non-coronary).
  7. Tie without distorting the valve. Check that the coronary ostia are clear.
  8. Close the aortotomy in **two layers of 5-0 polypropylene** ([PMC3781796](https://pmc.ncbi.nlm.nih.gov/articles/PMC3781796)).
  9. De-air through the LV vent and root vent with TEE.
- **New complications:** **complete heart block** (sutures near the conduction system, so pacing wires matter), paravalvular leak, coronary ostial obstruction, patient–prosthesis mismatch, and embolized calcium leading to stroke **(uncertain: names standard, not separately sourced)**.
- **Operative mortality:** 2.18% (STS 2025).

### 9.2 Mitral valve repair / replacement (v3)

- **Cannulation:** **bicaval** (separate SVC and IVC cannulae with caval snares or tourniquets, joined with a Y) ([TSRA](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals)).
- **Access:** **left atriotomy through Sondergaard's groove** (the interatrial groove), from the junction of the left atrium and right superior pulmonary vein, extended under the SVC toward the IVC ([Annals CTS mitral exposure](https://www.annalscts.com/article/view/6421/html) **(uncertain: link taken from a search snippet)**). Transseptal access is an alternative. A self-retaining atrial-lift retractor is used **(uncertain: name not sourced)**.
- **Pericardial well:** a stay at the level of the right superior pulmonary vein ([Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/Textbook/Creation+of+the+Pericardial+Well)).
- **Repair toolkit:**
  - **P2 resection** (triangular or quadrangular) ± **sliding plasty**, where the posterior leaflet is detached 1–2 cm toward each commissure.
  - **Neochords in 5-0 PTFE (Gore-Tex)**.
  - **Annuloplasty ring**.
  - Commissuroplasty.

  (All from [TSRA Mitral Valve](https://www.aats.org/tsra-primer-mitral-valve).)
- **Test:** inject saline under pressure into the LV ("saline test"). After weaning, TEE should show **residual MR < 1+** ([Annals CTS](https://www.annalscts.com/article/view/6421/html)).
- **Replacement:** preserve the subvalvular apparatus where possible ([TSRA](https://www.aats.org/tsra-primer-mitral-valve)).
- **New complications:** **SAM / LVOT obstruction** (treat "slow, tight and full"), **circumflex artery injury** from bites placed beyond the annulus, residual MR ([TSRA](https://www.aats.org/tsra-primer-mitral-valve)), and AV-groove disruption after replacement **(uncertain)**.
- **Operative mortality:** repair 0.88%, replacement 4.87% (STS 2025).

### 9.3 Off-pump CABG (v3/v4, optional)

- **What is removed:** no cannulation, cross-clamp or cardioplegia.
- **What is added:** a **suction or pressure tissue stabilizer** and an apical positioner, **intracoronary shunts** sized by probe, a **blower/mister**, careful haemodynamic management while the heart is lifted, and proximals on a side-biting clamp or a clampless device. Instruments are listed in the [Cardiac Outlines primer: Hercules stabilizer arm, shunts](https://publish.obsidian.md/cardiacoutlines/Textbook/200+A+Coronary+Anastomosis+Primer).
- **Evidence:** CORONARY showed **11.8% incomplete revascularization off-pump vs 10.0% on-pump**, and 3.0 vs 3.2 grafts per patient ([CORONARY summary](https://www.acc.org/Latest-in-Cardiology/Clinical-Trials/2014/06/08/17/13/CORONARY)).
- **Simulation cost:** a moving target with cardiac and respiratory motion, plus haemodynamic collapse when the heart is lifted. This is the highest-effort mode.

---

## 10. Sources and licences

This report mainly uses **sources of facts**, which are fine to use as references. Facts and procedure steps are not copyrightable, but **text, figures and videos are**. Each source's status for re-use *inside the game* (copying text or images) is below.

| Source | Use in plan | Licence | Personal / non-commercial OK? | Attribution / ShareAlike |
|---|---|---|---|---|
| VUMC Open Manual of Surgery: *Sternotomy* (Davis & Bishop), [PDF](https://www.vumc.org/global-surgical-atlas/sites/default/files/public_files/PDF/Sternotomy.pdf) | Steps, photos of sternotomy, Lebsche knife, Finochietto retractor, wiring | **CC BY-SA 3.0** (verified in the PDF footer) | Yes (commercial use is allowed too) | **Attribution + ShareAlike** apply to any adapted images or text |
| dos Reis Filho et al., *CPB checklist*, JECT 2025, [doi:10.1051/ject/2024030](https://doi.org/10.1051/ject/2024030) | 41-item perfusion checklist | **CC BY 4.0** (verified in the PDF) | Yes | Attribution |
| de Lind van Wijngaarden et al. 2019, *Quality standard for verbal communication during CABG* ([portal](https://research.tudelft.nl/en/publications/developing-a-quality-standard-for-verbal-communication-during-cab/)) | Communication model | Portal states **CC BY**. Full text not opened, so **UNVERIFIED** | Likely yes | Attribution |
| AATS TSRA Primer: Adult Cardiac (several chapters, [index](https://www.aats.org/tsra-primer-adult-cardiac)) | Core step order, numbers, troubleshooting | No open licence seen. **UNVERIFIED**, assume © AATS | Use as a reference only; paraphrase | Do not copy text or figures |
| *Outlines of Technique in Cardiac Surgery* (Perez-Tamayo et al., [Cardiac Outlines](https://publish.obsidian.md/cardiacoutlines/)) | Detailed surgeon-level steps, sutures, call-outs | No licence stated (DMCA badge), so **UNVERIFIED**; assume all rights reserved | Reference only | Do not copy text or images |
| STS/SCA/AmSECT 2018 Anticoagulation guideline ([PMC5850589](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)) | Heparin, ACT, protamine | **UNVERIFIED** (journal copyright) | Reference only | Cite |
| STS/SCA/AmSECT 2015 Temperature guideline ([PMC4631211](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211)) | Temperature rules | **UNVERIFIED** | Reference only | Cite |
| 2024 EACTS/EACTAIC/EBCP CPB guideline ([PMC 11826094](https://pmc.ncbi.nlm.nih.gov/articles/11826094)) | Flows, DO₂, cardioplegia, Hb | **UNVERIFIED** (likely open access, licence not confirmed) | Reference only | Cite |
| STS ACSD rates PDF ([25H4](https://www.sts.org/sites/default/files/2026-01/ACSD%2025H4%20Multipliers%20and%20Annual%20Rates.pdf)) | Outcome base rates | © STS, **UNVERIFIED** licence. The numbers are facts. | Use the numbers; do not reproduce the document | Cite |
| WHO Surgical Safety Checklist (2009) | Sign-in / time-out / sign-out items | **UNVERIFIED**. WHO encourages local adaptation; reproduction terms not checked | Paraphrase or adapt; check WHO terms before copying the form | Cite WHO |
| Wikipedia: *WHO Surgical Safety Checklist* | Item list | **CC BY-SA 4.0** (text) | Yes | Attribution + ShareAlike if text is copied |
| LITFL (pacing) | Pacing defaults | **UNVERIFIED** (LITFL has historically used CC BY-NC-SA; not confirmed) | Reference only until verified | Cite |
| Manufacturer pages (LivaNova cannulae, Scanlan instruments) | Device sizes and names | © manufacturers, **UNVERIFIED** | Reference only; do **not** use logos or brand names in the game (trademarks) | — |

**Recommendation:** the game should reproduce *procedures and numbers* (facts) and build its *own* art, text and 3D models. For reference imagery to copy, use only CC BY or CC BY-SA material (for example the VUMC sternotomy chapter), with attribution. Asset licensing is covered in a separate research file.

---

## 11. Open questions and uncertainties

1. **Exact call-out wording** varies by hospital. The 64-item list of critical items was not reached (TU Delft PDF returned 503). A clinician should review the script in §7.
2. **Weaning numeric targets** (K⁺, iCa²⁺, temperature, paced rate) came from low-quality teaching sources. A Stanford CV anesthesia CPB guide was found, but **`cvanes.stanford.edu` is blocked in this session's network settings** and must be allowed before it can be fetched. The full EACTS 2024 weaning section (§9.11) was only partly read.
3. Cooling target for routine CABG (32–34 °C vs tepid/normothermic) is practice-dependent. The game should allow both.
4. Typical durations for prep, distal and proximal anastomoses, weaning and closure are mostly estimates. The game needs a time-compression design anyway.
5. Proximal strategy (single clamp vs side-biting clamp): the evidence is mixed. The design could offer both, with a stroke-risk modifier.
6. Instrument eponyms (Cooley vs Fogarty vs DeBakey cross-clamps; Ankeney vs Morse vs Finochietto sternal retractors; aortic punch sizes) vary by hospital tray and were only partly verified.
7. Several citations come from search-result snippets and are marked **(uncertain)**. These include ROOBY and CORONARY details, the aortic-dissection incidence, defibrillation energy trials, hot-shot dosing and skin-to-skin times. Check them before treating them as facts.
8. Licences for the AATS TSRA Primer, Cardiac Outlines, the WHO checklist and LITFL are **UNVERIFIED**. Treat them as reference-only until confirmed.
