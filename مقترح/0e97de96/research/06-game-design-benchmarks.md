# Research 06: Game design and benchmarks

> **Purpose:** Give the open heart surgery simulation game plan an evidence base for game design. This covers benchmark products, real assessment tools that scoring can copy, game modes, controls, player roles, AI teammates, and the MVP (minimum viable product) core loop.
>
> **Researched 2026-11-03 (re-do, fresh searches).** Search note: the shared web-search budget for this run was already used up when this agent started, so keyword search was not available. All evidence comes from **direct fetches of known primary pages**: PubMed records read through the Europe PMC article API, official product and society pages, and the TSDA curriculum and assessment PDFs, which were downloaded and converted to text. Every claim below links to the page it came from.
>
> **Disclaimer:** This is game-design research for a personal, non-commercial, educational game. It is **not clinical guidance**. The game is **not a certified medical device**, and nothing here should be used to train for or perform real surgery. Times, scores and thresholds taken from training curricula are educational targets for simulators, not clinical standards.

Abbreviations, defined once: CPB = cardiopulmonary bypass. CABG = coronary artery bypass grafting. AVR = aortic valve replacement. LAD = left anterior descending artery. ACT = activated clotting time. TSDA = Thoracic Surgery Directors Association. JCTSE = Joint Council on Thoracic Surgery Education. OSATS = Objective Structured Assessment of Technical Skill. NOTSS = Non-Technical Skills for Surgeons. ANTS = Anaesthetists' Non-Technical Skills. STS = Society of Thoracic Surgeons. MAE = massive air embolism. AIAD = acute intraoperative aortic dissection. SDCF = sudden deterioration in cardiac function. VR = virtual reality. DOF = degrees of freedom. NTS = non-technical skills. MVP = minimum viable product.

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Curriculum backbone | Base the game's structure on the **TSDA Cardiac Surgery Simulation Curriculum**. It has 6 modules (CPB, CABG, AVR, MAE, AIAD, SDCF) and 29 sessions. Each module goes from component tasks to the full operation, and SDCF ends in "final exams". | [TSDA curriculum PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), [Feins 2017](https://pubmed.ncbi.nlm.nih.gov/27570162/) |
| MVP procedure | **On-pump CABG to the LAD**: a full CPB run using the "7 Steps of CPB", plus one distal end-to-side anastomosis. Add 2 crisis drills (protamine reaction and massive air embolism). | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) (CABG session 3: "minimum of 3 LAD bypasses"; final exams use CABG to LAD or AVR), [Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/) |
| Technical scoring | Score each skill item from 1 to 5 using rubrics modeled on the **TSDA/JCTSE Vessel Anastomosis Assessment Tool** (13 items), **ACAT** (aortic cannulation, 12 items) and **CPBAT** (CPB, 8 items). Compute each item from telemetry. | [VAAT PDF](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf), [TSDA PDF App. A](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Global vs checklist | Use **global-rating style items** (graded 1–5) for technical quality. Use **binary checklists** only for safety steps. | [Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/): global ratings separated training levels but checklists did not |
| Pass rule | A run passes only if **every item scores ≥4** (the TSDA mastery rule) and no "never event" occurs. | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) ("score of 4 or greater on EACH assessment tool") |
| Crisis timers | MAE: retrograde perfusion within **3 min**, back on CPB within **2 min** of root de-airing. AIAD: femoral cannulation within **3 min**, repair within **20 min**. SDCF: CPB re-established within **4 min**. A full CPB run within **30 min**. | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Non-technical scoring | **NOTSS v2.0**: 4 categories and 12 elements, rated 1–4 or N/A. Use it for the surgeon role and add an ANTS-style layer later for the anaesthesia role. | [NOTSS handbook v2.0](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf), [Fletcher 2003](https://pubmed.ncbi.nlm.nih.gov/12697584/) |
| Outcome layer | Simulated outcome flags follow the **STS** definitions: operative mortality plus 5 major morbidities (reoperation, stroke, kidney failure, chest wound infection, prolonged ventilation). The CABG composite has 4 domains. | [STS glossary](https://www.sts.org/public-reporting-glossary), [STS ACSD explanation](https://publicreporting.sts.org/acsd-exp) |
| Motion metrics | Hand path length, time per stitch, needle-loading time, and inter-stitch spacing SD. Published expert vs trainee values serve as "par" values. | [Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/), [Hermsen 2021](https://pubmed.ncbi.nlm.nih.gov/32971063/) |
| Error model | Tag every error as **consequential or inconsequential** (OCHRA). Track errors per minute and "hazard zones". | [Tang 2004 OCHRA](https://pubmed.ncbi.nlm.nih.gov/15545569/), [Seymour 2002](https://pubmed.ncbi.nlm.nih.gov/12368674/), [Tozzi 2022](https://pubmed.ncbi.nlm.nih.gov/34225333/) |
| Modes | Learn (cognitive), Guided practice, Component drills, Full case, Exam (no hints), Crisis drills, Sandbox, Challenge. | [Brewer 2016](https://pubmed.ncbi.nlm.nih.gov/27568126/), [Osso VR health systems](https://www.ossovr.com/health-systems), [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Practice schedule | Use **distributed (spaced) practice**: start each session with a re-test of earlier tasks and set minimum repetition counts. | [Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/), [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Debrief | Timeline replay plus a 3-question debrief ("what went well / what went wrong / questions"), with a PEARLS-style blend of self-assessment and directive feedback. | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), [Eppich & Cheng 2015](https://pubmed.ncbi.nlm.nih.gov/25710312/) |
| Controls | Desktop first: map intent (mouse or gamepad), **not** individual fingers. VR second, using controllers by default. Hand tracking is optional (Unity XR Hands 1.5.1, 26 joints). Haptic stylus (3D Systems Touch, 3.3 N max) is a later option. | [Surgeon Simulator wiki](https://en.wikipedia.org/wiki/Surgeon_Simulator), [XR Hands data model](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html), [3D Systems Touch](https://www.3dsystems.com/haptics-devices/touch), [Rangarajan 2020](https://pubmed.ncbi.nlm.nih.gov/31564519/) |
| Roles | The player is the **surgeon**. The perfusionist, anaesthesiologist, scrub nurse and assistant are **AI teammates** that use closed-loop commands. A playable perfusionist comes later. | [TSDA PDF "About the Simulator"](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), [Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/) |
| Validity honesty | Do **not** claim the game's scores are validated. Cardiac simulator studies rarely validate their assessment tools, and expert checklists vary widely. | [Ribeiro 2018](https://pubmed.ncbi.nlm.nih.gov/29248416/), [Vaporciyan 2017](https://pubmed.ncbi.nlm.nih.gov/29074155/), [Arjomandi Rad 2023](https://pubmed.ncbi.nlm.nih.gov/37220905/) |
| Licensing of tools | The TSDA curriculum says "No part … may be reproduced, distributed or used without permission", so paraphrase it and build our own rubric. The NOTSS v2.0 handbook allows personal / not-for-profit reproduction. The VAAT PDF has no licence (UNVERIFIED). | [TSDA PDF p. iv](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), [NOTSS handbook p. 2](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf) |

---

## 1. Existing products, curricula and research: what each does well

### 1.1 Entertainment games (benchmarks for feel, pacing and UX)

| Product | Facts (with source) | Mechanics worth copying | What to avoid |
|---|---|---|---|
| **Surgeon Simulator (2013)**, Bossa Studios | Built in 48 h at Global Game Jam 2013, then 48 days to a commercial version. Released 19 Apr 2013 on Windows, OS X and Linux. 2 million copies sold by 4 Feb 2015. Franchise sold to tinyBuild on 26 Aug 2022 for $3M, then acquired by Atari SA on 26 Jun 2024 ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)). Steam: 82% positive of 8,498 reviews, Metacritic 71 ([Steam](https://store.steampowered.com/app/233720/Surgeon_Simulator/)). | First-person view of the hands. A heart transplant level shows that cardiac surgery is a viable game theme. Physics props. | Controls: mouse moves the hand, right button rotates it, left button lowers it, and **A, W, E, R and Space control individual fingers** ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)). The store page says the controls are deliberately awkward ([Steam](https://store.steampowered.com/app/233720/Surgeon_Simulator/)). Critics called the controls "difficult", which was "part of the appeal" ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)). A realism-focused game must do the opposite. |
| **Surgeon Simulator 2** (27 Aug 2020) | Adds a controllable character, **4-player co-op**, and a **creation mode** for player-made levels ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)). | Co-op roles. User-made scenarios, which a scenario editor could copy later. | Slapstick physics. |
| **Trauma Center: Under the Knife** (Atlus, Nintendo DS) | Released in Japan 16 Jun 2005, NA 4 Oct 2005, EU 28 Apr 2006. Metacritic 81/100 from 45 reviews ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)). All actions use the stylus. Tools are picked from icons along the screen edge (laser, scalpel, scanner, forceps, syringe, sutures, antibiotic gel, hand). Each operation has a timer. Actions are graded from "Bad" to "Cool", and each operation ends with a rank from C to S. A Challenge mode lets players replay for a higher score. "Healing Touch" (drawing a star) slows time ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)). | A **tool palette**, gesture-based actions, a **visible timer and vitals**, a per-action quality grade, an end rank, and challenge replays. | Fantasy diseases and a "time slow" power. Critics also flagged difficulty spikes and repetitive play ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)). |

**Lesson:** Entertainment games prove that surgical play can be fun. Trauma Center's palette, timer and ranks fit a realistic sim. Surgeon Simulator's finger mapping is a known anti-pattern for precision tasks.

### 1.2 Cognitive (step and decision) simulators

| Product | Facts | Mechanics worth copying |
|---|---|---|
| **Touch Surgery** (now Medtronic) | Mobile app with about 400 procedures across 17 specialties as of June 2025. Its page claims "over 30" peer-reviewed validation papers (Wikipedia notes the article reads like a press release) ([Wikipedia](https://en.wikipedia.org/wiki/Touch_Surgery)). | Step-by-step "learn then test" modes for procedure order. |
| **Touch Surgery cardiac modules** (Stanford) | 4 modules: sternotomy, cannulation, decannulation and sternal closure. Over 6 months, 5,368 unique users did 1,971 hours. In an RCT (randomised controlled trial) of 16 preclinical students, the module group scored **75% ± 9% vs 61% ± 7%** for reading (P < 0.05) ([Brewer 2016](https://pubmed.ncbi.nlm.nih.gov/27568126/)). | Proof that a **low-fidelity cognitive mode** for CPB cannulation steps teaches. It is cheap to build first. |
| **CABG puzzle game** (Iran) | A puzzle game on CABG stages and instrument order raised knowledge from 2.68 ± 0.79 to 5.75 ± 1.65 and cognitive scores from 2.00 ± 1.09 to 6.31 ± 2.57 (P < 0.0001). This was a single-group pre/post study of 18 students, with 2 withdrawals ([Khorammakan 2023](https://pubmed.ncbi.nlm.nih.gov/37055824/)). Weak design (grade A source, weak evidence). | An "instrument tray / step order" mini-game. |

### 1.3 VR procedural platforms

| Product | Facts | Mechanics / evidence |
|---|---|---|
| **Osso VR** | Has **Practice Mode** ("virtual preceptor" guidance at each critical step) and **Test Mode** (guidance removed, scored), debrief feedback, educator dashboards, and collaborative multi-user sessions ([Osso health systems](https://www.ossovr.com/health-systems)). Image filenames show a Quest headset and controllers; the text does not name the hardware (uncertain) ([Osso health systems](https://www.ossovr.com/health-systems)). | RCT evidence (orthopaedics, not cardiac). Tibial nailing, n=20: aggregate global score **17.5 vs 7.5** and correct steps **63% vs 25%** for VR vs a standard guide ([Blumstein 2020](https://pubmed.ncbi.nlm.nih.gov/32035854/)). n=25: completion **6/8 and 7/9 vs 2/8** ([Orland 2020](https://pubmed.ncbi.nlm.nih.gov/32769533/)). Knee arthroplasty, n=22: correct steps **33 vs 27**, time **26.7 vs 35.4 min** ([McKinney 2022](https://pubmed.ncbi.nlm.nih.gov/35863958/)). Osso's headline "92% step accuracy / 67% fewer errors / 25% faster" figures are not tied to a stated study (uncertain) ([Osso](https://www.ossovr.com/)). |
| **Fundamental Surgery (FundamentalXR, formerly FundamentalVR)** | Lists VR, MR, AR, AI and haptics, plus an analytics "Insights" platform. Marketing figures ("95% skill retention", "40% faster learning", "500K+ training hours") are given without methods (C-grade, uncertain) ([FundamentalXR](https://www.fundamentalxr.com/)). | Shows that the market pairs haptics with analytics dashboards. Do not cite its numbers as evidence. |

### 1.4 Haptic / mixed-reality commercial simulators

| Product | Facts | What it teaches us |
|---|---|---|
| **Surgical Science (incl. Simbionix)** | simbionix.com redirects to surgicalscience.com. Lines include LAP-Mentor III, ANGIO Mentor Flex Pro and ENDO Mentor Suite. The company claims "400+ validation studies" ([Surgical Science](https://surgicalscience.com/)). The site lists no cardiac-surgery product ([Surgical Science](https://surgicalscience.com/)). | Proficiency-based training with metrics is the industry norm. |
| **VirtaMed** | Its clinical-evidence page lists 43 unique studies. Metrics used include **task time, camera path length, probe trajectory, dominant vs non-dominant hand asymmetry, gaze patterns, and global rating scales** ([VirtaMed evidence](https://www.virtamed.com/en/clinical-evidence)). | A ready list of telemetry metrics shown to separate experts from novices. |
| **Mentice VIST** | VIST G7/G7+ (image-guided procedures, "responsive haptics"), a dual-haptic extension, and a **VIST TEE Trainer** (transoesophageal echo) ([Mentice simulators](https://www.mentice.com/simulators)). Publications cover construct validity for carotid and neuro work ([Mentice publications](https://www.mentice.com/publications)). | The TEE simulator is a precedent for an "anaesthesia echo" sub-game (later). |
| **HeartWorks** (TEE/TTE echo simulator) | **UNVERIFIED.** The official pages could not be fetched (404/503 on 2026-11-03), so its current owner and features are not confirmed here. | Treat as background only. |

### 1.5 Cardiac-surgery physical simulators and wet labs

| Simulator | Facts | Relevance to game |
|---|---|---|
| **Ramphal Cardiac Surgery Simulator** (UWICSS) | A prepared **porcine heart** in a mock chest, with an actuator, pumps and valves, a vital-sign monitor and a computer. It runs in **arrested or beating** modes. CABG (standard and beating-heart), AVR, homograft and pulmonary autograft can be simulated, and adverse scenarios can be added ([Ramphal 2005](https://pubmed.ncbi.nlm.nih.gov/15848335/)). The heart rate can be set **"between arrested and 200 bpm"** or to ventricular fibrillation. An **operator behind the drapes plays perfusionist/anaesthetist** and responds to the trainee's commands. It took "over 20 software updates" ([TSDA PDF, About the Simulator](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). | The closest real model for our game: monitor traces synced to the heart, a scenario operator (our "AI director"), and commands sent to virtual teammates. |
| **The Chamberlain Group** | Cardiothoracic catalogue: 3 mm and 4 mm graft/target vessels, aortas, aortic roots with **19–27 mm annulus** sizes, Beating Heart, **CABG Beating Heart**, and a Cannulatable Larger Beating Heart ([Chamberlain cardiothoracic](https://www.thecgroup.com/specialty/cardiothoracic)). The CABG Beating Heart is programmable "at different speeds and rhythms", measures about 127 × 89 × 76 mm, and supports CABG and off-pump training ([Chamberlain #1339](https://www.thecgroup.com/product/cabg-beating-heart-trainer/)). Its ECMO/perfusion team trainer interfaces with the Califia or Orpheus simulators ([Chamberlain #1502](https://www.thecgroup.com/product/enhanced-ecmo-perfusion-team-trainer-1502/)). TSDA's Vessel Anastomosis module uses the **Chamberlain Pocket Vessel Anastomosis Trainer** ([TSDA VA module](https://tsda.org/the-tsda/tsda-vessel-anastomosis-simulation-module/)). | Difficulty levers: target vessel 3 vs 4 mm, beating vs still, valve sizes. |
| **KindHeart** | **UNVERIFIED.** kindheart.com returned 404 on 2026-11-03, so no product facts could be confirmed. | No claims made. |
| **Califia (Biomed Simulation)** | A perfusion patient simulator for CPB, ECMO and ECLS (extracorporeal life support), with a Califia Lung and a Califia Beating Heart (synthetic or porcine) for cannulation and cardioplegia practice ([Biomed Simulation](https://www.biomedsimulation.com/)). | A model for a later **playable perfusionist** role. All 23 US perfusion programmes use simulation, and 82.6% use high fidelity ([Bienstock 2026](https://pubmed.ncbi.nlm.nih.gov/42319097/)). |
| **Porcine wet lab: Boot Camp** | 33 first-year residents. Each did **10–18 end-to-side anastomoses** in 4-hour sessions. Scores improved (P < .001) ([Fann 2010](https://pubmed.ncbi.nlm.nih.gov/19846125/)). | Sets repetition counts per session. |
| **Porcine: medical students** | 10 students after 4 months of deliberate practice vs 11 senior general surgery residents. Median score 3 vs 4 (P = .102). Time **792.7 s vs 659 s** (P = .118) ([Nesbitt 2013](https://pubmed.ncbi.nlm.nih.gov/23499474/)). | Deliberate practice can reach resident level. This supports a "practice to mastery" design. |
| **Porcine beating heart (IABP-driven)** | 60 trainees were randomised. After 3 months the beating-heart group beat the non-beating group on instrument use, anastomotic quality and speed (P < .05) ([Wu 2021](https://pubmed.ncbi.nlm.nih.gov/32305184/)). | Use beating-heart motion as a higher difficulty tier. It teaches better, not only harder. |
| **Senior Tour review** | 13 senior surgeons reviewed 12 simulators (6 cardiac: small vessel anastomosis, aortic cannulation, CPB, AVR, mitral repair, aortic root). All agreed that simulation "may not be fully immersive" ([Fann 2012](https://pubmed.ncbi.nlm.nih.gov/22075060/)). | Realism gaps are expected. Focus fidelity where it teaches. |

### 1.6 Curricula and programmes (structure we can copy)

**TSDA Cardiac Surgery Simulation Curriculum** ([PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf); [page](https://tsda.org/education/tsda-cardiac-surgery-simulation-curriculum/)):
- 6 modules: 3 procedures (CPB, CABG, AVR) and 3 adverse events (MAE, AIAD, SDCF). There are **29 sessions** in total. Each session takes **2–4 hours**, and each module has **4–7 sessions** ([TSDA PDF, Introduction](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).
- Every session has the same template: overview, prerequisites, objectives, equipment, set-up, conduct, assessment tools ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). This maps directly to a game "level spec" format.
- It was funded by an AHRQ grant, R18HS020451, at 8 institutions. The preface reports **30 residents and >3,600 simulation hours** ([TSDA PDF, Preface](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). The outcome paper reports **27 residents** ([Feins 2017](https://pubmed.ncbi.nlm.nih.gov/27570162/)). The sources disagree (range 27–30), probably because of how residents were counted (uncertain).
- Video recording and review are "strongly advise[d]" ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). This supports a replay feature.
- "Each weekly session will begin with an evaluation of the component tasks covered in previous weeks" ([TSDA PDF, CPB overview](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). This supports a spaced re-test at session start.
- Outcomes: final mean scores on a 5-point scale were CPB **4.80**, CABG **4.41**, AVR **4.51**, AIAD **4.52**, SDCF **4.76**. MAE is reported as **0.68 ± 0.14**, which is probably a typo or a different scale (uncertain). The study also found "a transient negative effect from time away from training" ([Feins 2017](https://pubmed.ncbi.nlm.nih.gov/27570162/)).
- In the survey, 20/27 residents (74%) and 14/18 faculty (78%) responded. 85% of residents and 100% of faculty felt more comfortable with residents' skills ([Mokadam 2017](https://pubmed.ncbi.nlm.nih.gov/27570163/)).

**TSDA Boot Camp** (inaugural Boot Camp held in Chapel Hill; it featured the Ramphal simulator per [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)):
- Coronary anastomosis: 33 residents, 4-hour sessions in groups of 8–9 with 6–7 attendings. A **3-point scale** was used (1 = good, 3 = below average; note the reversed direction) ([Fann 2010](https://pubmed.ncbi.nlm.nih.gov/19846125/)).
- CPB: 32 residents in 4 groups, 4 hours each. Three simulators were used: a perfused non-beating heart, a computer-controlled CPB simulator, and a perfused beating heart. Crises were **massive air embolism (n=8), poor venous drainage, high arterial line pressure, and protamine reaction (n=7)**. "3 did not verify ACT before initiation; 4 had inadequate communication with the perfusionist". MAE "produced the most errors". Economy of time and thought scored 3.83 ± 0.6. The written exam did **not** correlate with the CPB score (r = 0.07) ([Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/)).
- Rater training: 9 less-experienced faculty took 30 min of video-anchored training on 10 anastomosis components. Composite ICC (intraclass correlation coefficient) rose from **0.76 to 0.90**, and pass/fail kappa from **0.20 to 0.78** ([Lou 2014](https://pubmed.ncbi.nlm.nih.gov/25308119/)). Lesson: anchor every score with examples. The game should show "what a 3 vs a 5 looks like".

**"Top Gun" competition** (a gamified curriculum) ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/)):
- 96 residents were invited, 17 submitted a baseline video and 15 a final video. There were 6 weeks of practice and an average of **23 anastomoses (range 10–40)**.
- 3 blinded raters scored **12 components on a 1–5 Likert scale** plus pass/fail.
- Score rose from **3.24 to 4.01**. Time fell from **11:10 to 9:04**. All-rater pass rose from **13% (2/15) to 73% (11/15)**. The bottom half improved most (+1.11 vs +0.43).
- Lesson: competition and leaderboards increase practice volume and narrow the skill gap. This is direct evidence for a Challenge/leaderboard mode.

**EACTS endoscopic mitral course** (an "air-pilot" training concept): 102 participants. Suture accuracy rose from **43% to 99%** and time fell from **87 s to 42 s** ([Sardari Nia 2020](https://pubmed.ncbi.nlm.nih.gov/31968097/)).

### 1.7 Pooled evidence: does simulation training work, and what moves the needle?

| Finding | Number | Source |
|---|---|---|
| Coronary anastomosis simulation improves skill | 12 studies, 274 subjects. Skill SMD (standardised mean difference) **1.68** (95% CI 1.23–2.13). Time −**205.9 s**. Novices gained more (293 s vs 120 s). **Fidelity had no significant effect.** | [O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/) |
| CABG simulation-based training meta-analysis | 11 studies, 372 participants. Technical SMD **2.18**, time SMD **2.00**. Benefit held across simulator types. | [Sidik 2026](https://pubmed.ncbi.nlm.nih.gov/42236427/) |
| Cardiac simulation systematic review | 16 studies, 81.2% used low-fidelity simulators. Effect size **2.2**. "Evidence of assessment tool validation was absent among all studies." | [Ribeiro 2018](https://pubmed.ncbi.nlm.nih.gov/29248416/) |
| Cardiac simulation systematic review | 28 studies (14 animal, 14 non-tissue). Validity testing done for **only 4 models**. | [Arjomandi Rad 2023](https://pubmed.ncbi.nlm.nih.gov/37220905/) |
| VR training transfers to the OR (operating room) | n=16. Dissection was **29% faster**. Errors were **1.19 vs 7.38 per case** (about 6× fewer). Training was to an expert-set criterion. | [Seymour 2002](https://pubmed.ncbi.nlm.nih.gov/12368674/) |
| Video-game skill correlates with laparoscopic skill | n=33. Playing more than 3 h/week in the past: **37% fewer errors, 27% faster**. Cross-sectional, so correlation only. | [Rosser 2007](https://pubmed.ncbi.nlm.nih.gov/17309970/) |
| Haptics in VR | 8 RCTs and 1 survey, 215 participants. **6 of 8 RCTs** favoured haptics, especially for novices. Two showed no difference. Cost is high. | [Rangarajan 2020](https://pubmed.ncbi.nlm.nih.gov/31564519/) |
| Distributed practice beats massed practice | 38 residents. Weekly sessions beat one day of equal total time at 1-month retention and on transfer to a live model (P < 0.05). | [Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/) |
| Task station + beating heart | 8 residents. Task station time fell 351 → 281 s (P = .07). Beating heart (70 bpm) fell 426 → 362 s (P = .03). Home practice of 90–540 min did not correlate with gains. | [Fann 2008](https://pubmed.ncbi.nlm.nih.gov/19114195/) |

**Implication for the plan:** Fidelity is not the main driver of learning ([O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/)). Deliberate, distributed, feedback-rich repetition is ([Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/); [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Realism budgets should go to **visual and haptic cues that drive the scored items** (bite angle, spacing, air in lines, bleeding), not to everything.

---

## 2. Scoring grounded in real assessment

### 2.1 OSATS: the foundation of surgical skill scoring
- OSATS used operation-specific checklists, detailed global rating forms and pass/fail judgements with 20 residents. Live (animal) and bench scores correlated at **0.69–0.72**. Interrater reliability was **0.64–0.72**. **Global ratings discriminated between training levels; checklists did not** ([Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/)).
- An 8-station, 2-hour OSATS with 48 residents had interstation reliability of **0.78 (checklist) and 0.85 (global)** ([Reznick 1997](https://pubmed.ncbi.nlm.nih.gov/9124632/)).
- The OSATS global rating scale items are commonly listed as **7 items scored 1–5**: respect for tissue, time and motion, instrument handling, knowledge of instruments, use of assistants, flow of operation and forward planning, and knowledge of the specific procedure. **(uncertain: from memory. The fetched abstracts of [Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/) and [Reznick 1997](https://pubmed.ncbi.nlm.nih.gov/9124632/) do not list the items. Verify against the full text before use.)**
- **Game rule:** Score technical quality with graded 1–5 items, as in a global rating. Keep binary checklists for critical safety steps only.

### 2.2 TSDA/JCTSE Vessel Anastomosis Assessment Tool (VAAT): 13 items, 1–5, plus pass/fail and time
Source: [VAAT PDF](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf). The same tool is in Appendix A of the [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), labelled "Developed by JCTSE". The form also records "Time to completion" and "Overall Pass/Fail".

General definitions (paraphrased): **1** poor, cannot accomplish the goal, marked hesitation. **2** below average, partly accomplishes it with hesitation. **3** average, accomplishes it with hesitation and discontinuous flow. **4** good, deliberate with minimal hesitation and good flow. **5** excellent, no hesitation and excellent flow ([VAAT PDF](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf)).

The table maps each item to a game telemetry metric. The anchor summaries are paraphrased from the [VAAT PDF](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf). The metrics and thresholds are **design proposals** to calibrate in playtests.

| # | VAAT item | Anchors at 1 → 5 (paraphrase) | Proposed game metric (design) |
|---|---|---|---|
| 1 | Arteriotomy | Off-midline, multiple "tracks", back-wall injury, irregular edge → midline, single thin track, no back-wall injury, smooth edge | Lateral deviation of the cut from the vessel axis (mm). Number of separate blade passes. Back-wall contact (bool). Edge roughness. |
| 2 | Graft orientation | Unable to orient, unsure of start/end → proper heel-toe, consistent start, knows end point | Heel-toe orientation correct (bool). Idle time before the first bite (s). |
| 3 | Bite | Irregular entry/exit, multiple punctures, inconsistent edge distance → consistent single puncture, regular entry/exit, consistent distance | Entry angle vs tissue normal (deg). Punctures per bite. Distance from edge (mm) and its SD. |
| 4 | Spacing | Uneven spacing → consistent even spacing | SD of inter-stitch distance. Benchmark: attendings **1.72 mm** vs trainees **2.14 mm** ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). |
| 5 | Needle holder use | Awkward grip, cannot rotate, inconsistent needle placement → smooth rotation, consistent placement | Needle regrasp count. Rotation smoothness (jerk). Needle-in-jaw position error. |
| 6 | Use of forceps | No traction, cannot expose, rough → consistent traction and exposure, gentle needle stabilisation | Exposure quality (target visible %). Tissue grasp force over a damage threshold (count). |
| 7 | Needle angles | Not aware of angles → consistent correct angles, compensates for depth and plans the next bite | Mean deviation of needle path from its curved arc (deg). |
| 8 | Needle transfer | Marked hesitation mounting the needle → mounts and manipulates easily | Needle-loading time. Benchmark: attendings **1.9 s** vs trainees **2.5 s** ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). |
| 9 | Suture management | No tension, entangled → proper tension, suture never in the way | Tangle events. Slack/over-tension events. |
| 10 | Knot tying | Slow, breakage, loose or "air" knot → consistent, tight, no hesitation | Knot security (throws, tension). Suture-break events. "Air knot" flag. |
| 11 | Hand mechanics | No pronation/supination or wrist motion → smooth, modulated | VR: wrist roll range used per bite. Desktop: rotation input usage. |
| 12 | Use of both hands | Non-dominant hand neglected → full use to assist and expose | Share of the time the non-dominant tool is doing useful work. |
| 13 | Economy of time and motion | Hesitation, discontinuous → smooth, goal-aware | Total time. Idle gaps over 2 s (design). Hand path length. Benchmarks: path **6,714 vs 10,154 mm**, stitch time **4.6 vs 6.4 s**, ring time **252 vs 312 s** (attending vs trainee) ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). |

Notes:
- Expert disagreement is real. A Delphi with 16 experts reached consensus on only **40 of 146 checklist items (27%)**. Agreement was 0% on "management of assistants" and 47% on "testing and final steps" ([Vaporciyan 2017](https://pubmed.ncbi.nlm.nih.gov/29074155/)). So the game must make each rubric threshold **configurable and documented**.
- The anastomosis meta-analysis lists the OSAT sub-steps used across studies. They match the VAAT items plus "configuration of anastomosis" ([O'Dwyer 2022, PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8830760/fullTextXML)).

### 2.3 Aortic Cannulation Assessment Tool (ACAT): 12 items, 1–5
Source: [TSDA PDF, Appendix A, ACAT](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf). Items are paraphrased:

| # | ACAT item | Key anchors (paraphrase) | Game metric (design) |
|---|---|---|---|
| 1 | Aortic site | Palpates and evaluates aorta, spacing for grafts/aortotomy, **BP noted and appropriate** | Palpation action done. Site distance from planned graft sites. BP checked/announced. |
| 2–7 | Needle angles, bite, spacing, needle holder, forceps, needle transfer | Same anchor family as VAAT | Reuse the VAAT metrics on the purse-string sutures. |
| 8 | Scalpel control | Perpendicular, appropriately sized aortotomy, **no leakage** | Blade angle. Incision length vs cannula size. Leak rate. |
| 9 | Cannula placement | Proper orientation, not too deep or shallow | Tip depth and direction vs target. |
| 10 | Securing cannula | Appropriately snug, smooth motion | Tourniquet tension band. |
| 11 | Connecting cannula | **No air in line; tests line, BP and flow** | Air bubbles in the arterial line (count/volume). Line-test command issued. |
| 12 | Decannulation | All conditions met, no bleeding | Preconditions met. Blood loss at the site. |

The conduct steps run **a → o**: heparin and check aortic pressure → purse strings → ACT check → clean the site → re-check root pressure → open with #11 blade → place cannula → secure → fill/de-air → advance the line → connect → check for air → ask the perfusionist to confirm pressure and flow → ... → decannulate. Minimum repetitions: **10** ([TSDA PDF, CPB Session 1](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

### 2.4 CPB Assessment Tool (CPBAT): 8 items, 1–5
Source: [TSDA PDF, Appendix A, CPBAT](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf):
1. **Briefing** (none → complete)
2. **Communication** (timid/none → confident, audible throughout)
3. **Aortic cannulation**, including "No heparin / Heparin given", "Air in line / Line de-aired", and line tested for BP and flow
4. **Venous cannulation** ("RCA injured" → appropriate position, no leak)
5. **Initiating CPB** (ACT checked, communicates **"on bypass"**, confirms circuit function)
6. **Cross-clamp and cardioplegia** ("Clamp placed, flow down", cardioplegia dose appropriate, LV distension checked by palpation)
7. **Terminating CPB** (ventilates, complete de-airing, bleeding/temperature/rhythm/contractility noted)
8. **Decannulation** (protamine, hemodynamics observed, sites secure)

These anchors give **ready-made "never events"** for exam mode:
- cannulating without heparin;
- going on bypass without an ACT check;
- air left in the arterial line;
- cross-clamping without asking for flow down;
- weaning without ventilating;
- decannulating without protamine or with bleeding sites.

All are named failure anchors in the [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf).

### 2.5 The 7 Steps of CPB: a procedural backbone and checklist
From the [TSDA PDF, CPB Session 1 teaching plan](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), paraphrased:
- **a.** Heparin.
- **b.** Expose the heart; check BP and the aorta.
- **c.** ACT; cannulate the aorta; check the aortic cannula.
- **d.** Atrial (venous) cannulation; venous clamp off; on bypass; lungs off.
- **e.** Inspect the heart; place antegrade and/or retrograde cardioplegia; reduce pump flow, cross-clamp, return to normal flow, check line pressure; begin cardioplegia; set patient temperature.
- **f.** Release the cross-clamp after warm cardioplegia; lungs working; no bleeding in accessible areas; good contractility; stable rhythm; temperature at the desired level.
- **g.** Wean off bypass; venous line clamped and removed when stable; remove aortic vent; protamine; follow RAP, PAP and BP; be alert for a hemodynamic reaction; remove the arterial cannula.

The curriculum also has an appendix of **"50 Steps of Cardiopulmonary Bypass"** ([TSDA PDF TOC](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

**Pre-bypass briefing has 8 items:** diagnosis, procedure, incision, significant surgical history, cannulation, cardioplegia, temperature, questions. **Debrief has 3 questions:** what went well, what went wrong, questions ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

A **CPB knowledge test needs a 90% pass** before the full CPB run ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). This is a ready-made gate for the cognitive mode.

### 2.6 Crisis scoring: Summative Exam Assessment Tool (SEAT), 5 items, 1–5
Items: **Recognizes emergency**, **Communication** (clearly establishes urgency), **Stepwise decision-making**, **Leadership** (takes full command), and **Knowledge of protocol** (knew all steps and stated them in a timely fashion). There is an option for "Not applicable – no emergency encountered" ([TSDA PDF, SEAT](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

Time targets from the same curriculum ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)):

| Event | Target |
|---|---|
| Full CPB run (briefing, cannulation, commands) | within **30 min** |
| MAE: convert to retrograde SVC perfusion after air is recognised | within **3 min** |
| MAE: re-institute normal CPB after aortic root de-airing | within **2 min** |
| AIAD: femoral arterial cannulation | within **3 min** (the PDF says "of the time air is recognized", probably a copy error for "dissection recognized" (uncertain)) |
| AIAD: repair the ascending dissection to allow antegrade flow | within **20 min** |
| SDCF: emergently re-establish CPB on a failing heart | within **4 min** |
| MAE background rate | **0.03–0.07 per 1,000 cases**, with death or serious outcome **>50%** (TSDA citing Mejak 2000, secondary citation, uncertain) |

### 2.7 Motion, time and tissue metrics (economy of motion)
- Multimodal CPB assessment combined a cognitive domain (20 items), a technical domain (21 items) and electromagnetic hand-motion sensors. Experts scored higher cognitively (6.7 vs 4.6, P = .03), but **technical scores did not differ** (6.2 vs 5.8). Experts tied a purse string with a Rummel tourniquet in **64 vs 82 s**. Cross-clamp path length was **47.5 vs 91.9 m** ([Hermsen 2021](https://pubmed.ncbi.nlm.nih.gov/32971063/)). Lesson: **cognitive and decision scoring separates skill levels best for CPB**. The game should weight decisions heavily in CPB scenes.
- AI video tracking of suturing (with MediaPipe) separated 10 attendings from 10 trainees. It measured needle loading, stitch time, path length, average acceleration, "vibrational motion" and suture uniformity (68.9% vs 63.1%) ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). Our game can compute all of these exactly from its own telemetry.
- VirtaMed uses camera path length, probe trajectory, dominant/non-dominant asymmetry and gaze ([VirtaMed evidence](https://www.virtamed.com/en/clinical-evidence)).
- Tissue damage: the mitral simulator with integrated supervision defined **critical "dangerous zones"** and flagged out-of-bound actions. It caught **2 stitches in dangerous zones and 1 misplaced stitch** across 7 users ([Tozzi 2022](https://pubmed.ncbi.nlm.nih.gov/34225333/)). Game: mark hazard volumes (for example the RCA near the venous cannulation site, as in CPBAT "RCA injured", and the vessel back wall) and log every contact.
- Blood loss: the ACAT and CPBAT anchors grade bleeding and leakage ("Significant bleeding with loss of control" → "No bleeding") ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Game: track cumulative simulated blood loss (mL) per site. Physiology values come from Research 02, not this report.

### 2.8 Error tracking
- **OCHRA** (Observational Clinical Human Reliability Assessment): 200 operations, 38,062 steps, 2,242 errors. Mean **11.0 ± 8.0 errors per procedure**, of which **4.0 ± 3.0 were consequential**. It identifies "hazard zones" where errors have serious consequences ([Tang 2004](https://pubmed.ncbi.nlm.nih.gov/15545569/)).
- **Errors per minute** against 8 predefined error types (interrater r > 0.80) was the outcome measure in the VR transfer RCT ([Seymour 2002](https://pubmed.ncbi.nlm.nih.gov/12368674/)).
- **Major vs minor events** (from human factors in cardiac surgery): 243 arterial switch operations by 21 surgeons. Major events and the **total number of minor events** were both strongly linked to death (P < .001), and **appropriate compensation reduced the risk of death** (P = .003) ([de Leval 2000](https://pubmed.ncbi.nlm.nih.gov/10733754/)).
- **Game error model (design):** every logged error has a type (procedural omission, wrong order, execution error, communication error), a severity (consequential / inconsequential, after OCHRA), a timestamp and a "recovered?" flag (after de Leval's compensation). The debrief shows minor-event accumulation as a "risk meter", because minor events add up.

### 2.9 Non-technical skills (NTS)

**NOTSS v2.0 (2019)** ([handbook](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf); [RCSEd page](https://www.rcsed.ac.uk/professional-support-development-resources/learning-resources/non-technical-skills-for-surgeons-notss)):

| Category | Elements (verbatim names from Table 1 of the handbook) |
|---|---|
| Situation Awareness | Gathering information; Understanding information; Projecting and anticipating future state |
| Decision Making | Considering options; Selecting and communicating option; Implementing and reviewing decisions |
| Communication & Teamwork | Exchanging information; Establishing a shared understanding; Co-ordinating team activities |
| Leadership | Setting and maintaining standards; Coping with pressure; Supporting others |

- **Scale:** 1 poor, 2 marginal, 3 acceptable, 4 good, plus N/A when the skill was not required ([NOTSS handbook](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)).
- The handbook says NOTSS suits theatre and simulators but is "**not recommended for formal summative assessment**". Its debrief "takes under five minutes" ([NOTSS handbook](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)). So it fits a formative in-game debrief.
- **Licence:** The handbook "may be photocopied or electronically reproduced by downloading from the RCSEd website without further permission for personal, organizational, or 'not for profit' use. No reproduction by, or for, commercial organizations…" ([NOTSS handbook p. 2](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)). This fits this personal, non-commercial project. Attribution to RCSEd is expected (design assumption).
- History: the prototype (v1.1) had 5 categories and 14 elements and was built from interviews with 27 consultant surgeons, including cardiac surgeons ([Yule 2006](https://pubmed.ncbi.nlm.nih.gov/17054619/)). v2.0 has 4 categories and 12 elements ([handbook](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)).

**ANTS** (anaesthetists): the prototype has **4 categories (task management, team working, situation awareness, decision making) and 15 elements**. It was tested with 50 consultant anaesthetists rating 8 simulated videos ([Fletcher 2003](https://pubmed.ncbi.nlm.nih.gov/12697584/)). The current handbook's scale and licence are **UNVERIFIED**, because the University of Aberdeen ANTS page returned 404.

**Team dimensions and outcomes:** surgical situation awareness was strongly associated with surgical technique errors (F = 7.93, P < 0.001) across 48 observed operations ([Catchpole 2008](https://pubmed.ncbi.nlm.nih.gov/18362635/)). Game: low situation awareness, such as not checking vitals or the line pressure after an event, should **raise the technical error probability**. NTS should not be a separate side score only.

**How the game measures NTS (design):**
- Situation awareness: how quickly the player looks at or queries the monitor after a change, and how quickly a crisis is recognised (seconds from onset to first correct action).
- Decision making: correct protocol branch chosen, and how often decisions are reviewed.
- Communication: briefing completeness (8 items), closed-loop commands ("on bypass", "flow down"), and read-back acknowledged.
- Leadership: commands given in a crisis without prompting (SEAT "Leadership"), and assigning tasks to AI teammates.

### 2.10 Patient outcome layer tied to STS measures
- STS publicly rates **isolated CABG, isolated AVR, AVR+CABG, MVRR, and MVRR+CABG** in the Adult Cardiac Surgery Database ([STS public reporting](https://publicreporting.sts.org/)).
- The **CABG composite has 4 domains**: absence of operative mortality, absence of major morbidity, internal mammary artery (IMA) use, and use of all evidence-based perioperative medications. AVR and MVRR composites have 2 domains (mortality and morbidity). Ratings are 1–3 stars with a "credible interval" and use a **3-year (36-month)** window ([STS ACSD explanation](https://publicreporting.sts.org/acsd-exp)).
- **Operative mortality** means death during the hospital stay, at another hospital after transfer without discharge, or within 30 days if discharged home. The **morbidity rate** is the share of patients with at least one of 5 complications: **reoperation, stroke, kidney failure, chest wound infection, prolonged ventilator support** ([STS glossary](https://www.sts.org/public-reporting-glossary)). The exact prolonged-ventilation threshold is not on that page (uncertain; check STS data specifications).
- **Game rule (design):** at the end of each case, roll simulated outcomes from in-game risk drivers:
  - air embolism or a long crisis time → stroke risk;
  - bleeding or a leaking anastomosis → reoperation risk;
  - long CPB or cross-clamp time and low perfusion → kidney failure / prolonged ventilation risk;
  - choosing a LIMA (left internal mammary artery) conduit → the IMA domain.

  Show the result as an **"STS-style outcome card"** with 4 domains. Effect sizes must come from Research 02 and the clinical literature, not from this report. This is a **teaching abstraction, not a risk calculator**.

### 2.11 Proposed composite score (design proposal, not validated)
| Layer | Weight (initial) | Content | Basis |
|---|---|---|---|
| Technical (T) | 40% | Mean of VAAT/ACAT/CPBAT-style items (1–5) | [VAAT](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf), [Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/) |
| Process & safety (P) | 25% | 7 Steps of CPB checklist, order errors, never events | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Non-technical (N) | 20% | NOTSS-style 4 categories (1–4), SEAT for crises | [NOTSS](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf), [TSDA SEAT](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| Outcome (O) | 15% | STS-style 4-domain card | [STS ACSD](https://publicreporting.sts.org/acsd-exp) |

- **Pass rule:** every T item is ≥4, every crisis timer is met, and there are **zero never events**. This mirrors TSDA's "score of 4 or greater on EACH assessment tool" ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).
- Always show the 4 layers separately. The weighted total is only for leaderboards. Weights are a playtest decision (uncertain).

---

## 3. Game structure

### 3.1 Modes

| Mode | What the player does | Real-world precedent |
|---|---|---|
| **Learn (cognitive)** | Step-order, instrument and team-command quizzes, with an anatomy viewer. Must pass a **90%** knowledge gate before the full CPB case. | Touch Surgery cardiac modules ([Brewer 2016](https://pubmed.ncbi.nlm.nih.gov/27568126/)); TSDA CPB test 90% ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)); CABG puzzle game ([Khorammakan 2023](https://pubmed.ncbi.nlm.nih.gov/37055824/)) |
| **Guided practice** | Hints at every critical step, ghost hands, and "why" pop-ups. | Osso Practice Mode "virtual preceptor" ([Osso](https://www.ossovr.com/health-systems)) |
| **Component drills** | Isolated tasks with minimum repetitions: aortic cannulation (10), venous cannulation / cardioplegia (7 each), end-to-side anastomosis (5 per session, 10 as homework). | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| **Full case** | The whole CABG: briefing → CPB → anastomosis → wean → debrief. | TSDA CABG sessions 3–5 on the Ramphal simulator ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) |
| **Exam** | No hints. A scored full case, with possibly **one hidden crisis or none** (the TSDA list includes "No emergency encountered"). | TSDA final exams ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)); Osso Test Mode ([Osso](https://www.ossovr.com/health-systems)) |
| **Crisis drills** | Timed emergency protocols: MAE, AIAD, SDCF, protamine reaction, poor venous drainage, high line pressure. | [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf); [Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/) |
| **Sandbox** | Free practice and tissue play, with no scoring. | Home task station practice ([Fann 2008](https://pubmed.ncbi.nlm.nih.gov/19114195/)) |
| **Challenge** | Leaderboards on drills (time and quality), with a ghost replay of personal bests. | Top Gun ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/)); Trauma Center Challenge mode ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)) |

### 3.2 Difficulty levers (all grounded in real simulators)
- **Heart motion:** arrested → beating at a set rate (the Ramphal range is arrested to 200 bpm; VF is possible) ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Beating-heart training also gave better learning ([Wu 2021](https://pubmed.ncbi.nlm.nih.gov/32305184/)). Fann used 70 bpm for beating-heart anastomosis ([Fann 2008](https://pubmed.ncbi.nlm.nih.gov/19114195/)).
- **Target vessel size:** 4 mm → 3 mm (Chamberlain stocks both) ([Chamberlain](https://www.thecgroup.com/specialty/cardiothoracic)).
- **Guidance level:** guided → hints on request → none (Osso Practice/Test) ([Osso](https://www.ossovr.com/health-systems)). Orland's VR study offered written hints on request ([Orland 2020](https://pubmed.ncbi.nlm.nih.gov/32769533/)).
- **Time pressure:** par times from the published data. Drill pars:
  - task station anastomosis about 281–351 s ([Fann 2008](https://pubmed.ncbi.nlm.nih.gov/19114195/));
  - Top Gun anastomosis 9:04 after training ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/));
  - purse string + tourniquet 64 s for experts ([Hermsen 2021](https://pubmed.ncbi.nlm.nih.gov/32971063/)).

  These are simulator times, so use them only as starting values.
- **Crisis injection:** none → one scripted crisis → a random crisis at a random step (TSDA final exam style) ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).
- **Team reliability:** AI teammates sometimes make latent errors that the player must catch (see §5).

### 3.3 Patient and scenario variants (from the TSDA SDCF protocol lists)
From the [TSDA PDF, SDCF overview](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf):
- **Re-institute CPB:** intracoronary air; unstable atrial fibrillation; VT/VF (ventricular tachycardia / fibrillation).
- **Failure to wean:** protamine reaction; RV failure; LV failure; hypoxia or lung injury; unable to defibrillate.
- **CABG issues:** graft too long (kinked); graft too short (stretched); twisted graft; RCA occluded by AVR; kinked button; circumflex injury after MVR; distal anastomotic bleeding.
- **Valve issues:** stuck mechanical leaflet; looped strut causing central regurgitation; paraprosthetic leak after AVR; broken pledgeted stitch; air knot in a mechanical valve.
- **Final-exam scenario list:** MAE while on CPB with the heart arrested; AIAD; CABG graft revision (too short); unable to defibrillate; RV failure; SDCF immediately post-op; no emergency.

**Additional CPB equipment crises** (for later): cannulation complications (dissection, malposition, gas embolism), heater-cooler failure, oxygenator problems, electrical failure, tubing rupture, circuit thrombosis, medication issues, and awareness during CPB ([Gerstein 2022](https://pubmed.ncbi.nlm.nih.gov/36100499/)).

### 3.4 Progression
- **Mastery gating:** a module unlocks when every rubric item is ≥4 on N consecutive runs. TSDA uses "score of 4 or better" gates throughout ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). N = 2 is a design choice (uncertain).
- **Repetition minimums:** these are shown as a progress bar (10 aortic cannulations, 7 venous, 5 anastomoses) ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).
- **Distributed practice:** suggest one session per day or week, and open each session with a short re-test of earlier skills ([Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/); [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Feins reported a transient drop after time away ([Feins 2017](https://pubmed.ncbi.nlm.nih.gov/27570162/)), so add a "skill decay" nudge after long breaks (design).
- **Progression order** (mirrors TSDA): CPB fundamentals → aortic cannulation → venous cannulation and cardioplegia → full CPB run → anastomosis drills → full CABG → crises (MAE → SDCF → AIAD) → exam ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

### 3.5 Debrief and replay with a timeline
- Record everything: TSDA "strongly advise[s]" video recording and review ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Reliable scoring needs anchored examples ([Lou 2014](https://pubmed.ncbi.nlm.nih.gov/25308119/)).
- **Timeline** (design): a horizontal track of the 7 CPB steps, with event markers (errors coloured by severity), vitals traces, team-communication markers and a crisis-onset marker. Click a marker to jump to the 3D replay. Players can compare the replay to a ghost expert run.
- **Debrief script:** (1) reaction and self-assessment ("what went well / what went wrong"); (2) focused discussion of 1–3 key events; (3) directive teaching for missed safety steps. This blends the 3 PEARLS strategies (learner self-assessment, focused facilitation, directive feedback) ([Eppich & Cheng 2015](https://pubmed.ncbi.nlm.nih.gov/25710312/)) with the TSDA debrief questions ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). The NOTSS debrief target is under 5 minutes ([NOTSS](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)).

---

## 4. Controls: mapping fine motor tasks

### 4.1 Lessons from shipped games and simulators
| Scheme | Example | Lesson |
|---|---|---|
| Mouse + per-finger keys | Surgeon Simulator: mouse moves the hand; A/W/E/R/Space are fingers ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)) | Comedic difficulty. Avoid for a realistic sim. |
| Stylus + tool palette + gestures | Trauma Center: tools from screen-edge icons, gesture actions, a per-action grade ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)) | Great for **desktop/tablet**. Copy the palette and gesture grading. |
| Touch step simulation | Touch Surgery / cardiac modules ([Brewer 2016](https://pubmed.ncbi.nlm.nih.gov/27568126/)) | Good for the cognitive mode, not for motor skill. |
| VR headset + controllers | Osso VR (Quest + controllers suggested by image filenames, uncertain) ([Osso](https://www.ossovr.com/health-systems)) | RCT-backed for procedure learning ([Blumstein 2020](https://pubmed.ncbi.nlm.nih.gov/32035854/); [McKinney 2022](https://pubmed.ncbi.nlm.nih.gov/35863958/)). |
| Haptic stylus | 3D Systems Touch: **6-DOF position sensing, 3-DOF force**, **3.3 N max**, >0.88 N continuous, ~0.055 mm resolution, 1 kHz, USB, **OpenHaptics SDK with Unity/Unreal compatibility** ([3D Systems](https://www.3dsystems.com/haptics-devices/touch)) | Haptics help novices in 6 of 8 RCTs ([Rangarajan 2020](https://pubmed.ncbi.nlm.nih.gov/31564519/)). OpenHaptics licence and device price are **UNVERIFIED**. |
| Hand tracking | Unity **XR Hands 1.5.1**: 26 tracked points per hand, following OpenXR joint naming; needs a provider (OpenXR) ([XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html), [data model](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html)) | Good for natural grasp. No force feedback, so fine needle control is harder. Keep it optional (design judgement, uncertain). XR Hands licence **UNVERIFIED** (check the Unity package licence). |
| Webcam hand tracking | **MediaPipe**, Apache-2.0 per the repo ([GitHub](https://github.com/google-ai-edge/mediapipe)); used for suturing analytics in [Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/) | Possible later "practice with real instruments in front of a webcam" mode. The landmark count (21) is not confirmed on the fetched page (uncertain). |

### 4.2 Proposed mappings (design proposals)

**Desktop (mouse + keyboard), the MVP default:**
- Mouse moves the active instrument tip on a work plane.
- Mouse wheel = depth.
- Right drag = wrist roll. This is needle rotation along its curve, which is the "hand mechanics" item.
- Left button = close jaws / grasp. A hold-time ramp gives grasp force, and the force feeds the tissue-damage metric.
- `Q`/`E` swap dominant and non-dominant hand control. Ghost-hand assist is available in Guided mode.
- A Trauma Center-style **tool palette** (1–9 keys).
- A **command radial menu** (`Tab`) for team commands, such as "Heparin", "ACT please", "Flow down", "On bypass", "Lungs off".
- Precision aids are difficulty options: a motion-scaling slider and tremor smoothing on/off. Exam mode locks them to a set value.

**Gamepad:** left stick = tip in plane; right stick = wrist roll and pitch; triggers = jaw closure (analog = force); bumpers = depth; face buttons = tools; d-pad = command radial.

**VR controllers (phase 2):**
- Grip = hold the instrument; analog trigger = jaw closure.
- Physical wrist rotation = needle drive (natural pronation/supination, matching VAAT items 7 and 11).
- Non-dominant controller = forceps (VAAT item 12).
- Snap-to-instrument handles avoid finger-level emulation.

**Haptics (phase 3):** a 3D Systems Touch stylus as the needle driver. Feed tissue resistance and needle-puncture "pop" forces under the 3.3 N device maximum ([3D Systems](https://www.3dsystems.com/haptics-devices/touch)).

### 4.3 Breaking fine tasks into controllable sub-actions
| Task | Sub-actions (each scored) | Rubric link |
|---|---|---|
| Suturing (one bite) | Load needle (grasp at the right point on the needle) → orient (angle to tissue) → enter perpendicular → follow the curve (wrist roll) → exit → regrasp → pull through with correct tension | VAAT 3, 5, 7, 8, 9 ([VAAT](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf)) |
| Knot tying | Desktop: semi-automated throws with a timing/tension mini-game (each throw sets tension; too loose = "air knot", too tight = break). VR: two-handed gesture loops with assist. | VAAT 10 ([VAAT](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf)) |
| Cutting (arteriotomy / aortotomy) | Blade angle (perpendicular) → depth control (no back wall) → single pass → length matched to graft or cannula | VAAT 1; ACAT 8 ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) |
| Cannulation | Purse strings → tourniquets → incision → insert to the right depth and orientation → snug → de-air and connect → test the line | ACAT 9–12 ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) |

Knot tying in desktop mode is an abstraction. Real knot-tying skill will not transfer from a mouse (design judgement, uncertain). The game should say so in its "what this trains" panel.

---

## 5. Player roles and AI teammates

| Role | MVP? | Why / evidence |
|---|---|---|
| **Surgeon (primary operator)** | Yes | All TSDA modules and tools are surgeon-centred ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). |
| First assistant | AI in MVP; playable later | In TSDA CABG session 3, a "non-operating resident may serve as first assistant" ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). "Management of assistants" got 0% expert consensus, so keep it simple ([Vaporciyan 2017](https://pubmed.ncbi.nlm.nih.gov/29074155/)). |
| Perfusionist | AI in MVP; playable in phase 2 | The Ramphal operator stands in for the perfusionist/anaesthesiologist and responds to commands ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). Perfusion education uses simulation widely ([Bienstock 2026](https://pubmed.ncbi.nlm.nih.gov/42319097/)). Califia-type sims show the role is "playable" ([Biomed Simulation](https://www.biomedsimulation.com/)). |
| Anaesthesiologist | AI in MVP; playable later | ANTS gives a scoring frame ([Fletcher 2003](https://pubmed.ncbi.nlm.nih.gov/12697584/)). A TEE sub-game has a precedent in the VIST TEE Trainer ([Mentice](https://www.mentice.com/simulators)). |
| Scrub nurse | AI | Instrument requests. Nursing leadership and management skills related to procedural problems in [Catchpole 2008](https://pubmed.ncbi.nlm.nih.gov/18362635/). |

**AI teammate rules (design, grounded in sources):**
1. **Closed loop.** The player issues a command → the AI reads it back → the AI executes → the AI confirms ("Flow is down", "ACT 480", "On bypass"). CPBAT scores whether the surgeon "Communicates 'on bypass'" and confirms circuit function ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). (The ACT value shown here is an illustrative placeholder. Real targets come from Research 02.)
2. **Teammates do not do the surgeon's thinking.** A missed ACT check or heparin dose must stay missed unless the AI is set to "prompting" difficulty. Real trainees made exactly these misses ([Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/)).
3. **Latent errors (hard difficulty):** occasional scripted teammate slips, such as a delayed read-back or a wrong line clamped, for the player to catch. This links to the de Leval finding that compensation saves patients ([de Leval 2000](https://pubmed.ncbi.nlm.nih.gov/10733754/)).
4. **AI director:** like the Ramphal operator, a scenario script selects heart rhythm, flows and crisis triggers in response to player actions ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).
5. **Voice (optional):** offline speech recognition with **Vosk** (Apache-2.0 per the repo, "20+ languages", models about 50 MB, C# binding) ([GitHub](https://github.com/alphacep/vosk-api)), with a small fixed command grammar. The radial menu is always available as a fallback. The Vosk version/date is not stated on the fetched page (UNVERIFIED).
6. **Multiplayer later:** Surgeon Simulator 2 shows that 4-player co-op works for the theme ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)), and Osso offers collaborative sessions ([Osso](https://www.ossovr.com/health-systems)). The roles would be surgeon, perfusionist and anaesthesiologist, scored with NOTSS and ANTS layers.

---

## 6. Recommended core loop and MVP feature set

### 6.1 Core loop
```
Case card (patient, diagnosis, plan)        <- TSDA briefing items
   -> Team briefing (8 items, scored)       <- CPBAT item 1
   -> Operate: step loop
        choose tool -> act -> immediate micro-feedback (bite grade, leak, air)
        -> vitals respond -> issue team commands (closed loop)
   -> Event / crisis (optional, timed)      <- SEAT + TSDA timers
   -> Wean, decannulate, close
   -> Outcome card (STS-style 4 domains)
   -> Debrief: scores by layer + timeline replay + 1-3 teaching points
   -> Recommended drill (lowest-scoring item) -> repeat (distributed)
   -> Unlock next module when all items >= 4
```
Sources: [TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf), [STS ACSD](https://publicreporting.sts.org/acsd-exp), [Eppich & Cheng 2015](https://pubmed.ncbi.nlm.nih.gov/25710312/), [Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/).

### 6.2 MVP feature set (priority order) and justification

| # | Feature | Justification |
|---|---|---|
| 1 | **Learn mode**: 7 Steps of CPB, circuit parts, briefing, with a 90% gate | Cheapest feature, with proven value: the cardiac Touch Surgery modules scored 75% vs 61% ([Brewer 2016](https://pubmed.ncbi.nlm.nih.gov/27568126/)). TSDA requires a 90% CPB test ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). |
| 2 | **Aortic cannulation drill** with ACAT-style scoring | It is the first TSDA component task (10 repetitions) and has the most failure anchors (heparin, air, leak) ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). |
| 3 | **End-to-side anastomosis drill** (arrested 4 mm → 3 mm → beating) with VAAT-style scoring | The best-studied cardiac sim task: 12 studies ([O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/)) and 11 studies ([Sidik 2026](https://pubmed.ncbi.nlm.nih.gov/42236427/)), with published par times and motion metrics ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). |
| 4 | **Full CPB run + CABG to the LAD** with AI perfusionist, anaesthetist and nurse | This mirrors TSDA CABG sessions 3–5 and the final exam ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). |
| 5 | **Two crisis drills: protamine reaction (moderate) and MAE (hard)** | Both were used at Boot Camp, and MAE produced the most errors ([Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/)). MAE has explicit timers ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). |
| 6 | **Scoring layers T/P/N/O + never events + pass rule** | Grounded in the VAAT, ACAT, CPBAT, SEAT, NOTSS and STS sources above. |
| 7 | **Debrief with timeline replay** | Recording and review are advised ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)); anchoring improves scoring reliability ([Lou 2014](https://pubmed.ncbi.nlm.nih.gov/25308119/)). |
| 8 | **Desktop controls** (mouse/keyboard and gamepad) | The widest reach. Fidelity matters less than practice ([O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/)). Avoid per-finger mapping ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)). |
| 9 | **Local challenge board** (personal bests, ghost replay) | Competition increased practice and pass rates ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/)). |

**Not in the MVP (later phases):** AVR (valve excision, annular sutures, de-airing), AIAD with femoral cannulation, the full SDCF set, VR, haptics, a playable perfusionist, multiplayer, voice, and a scenario editor. These come later because each needs more physics and content, while the MVP already covers the TSDA "CPB + CABG + crisis" path ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)).

---

## Game hooks

| # | Finding | Game mechanic / data value / rule |
|---|---|---|
| 1 | TSDA's 7 Steps of CPB, a → g ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | The procedure state machine. Each step is a node with entry conditions, and out-of-order actions are logged as errors. |
| 2 | CPBAT failure anchors: no heparin, no ACT, air in line, clamp without flow down ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | `neverEvents[]` causes an exam fail plus a mandatory teaching card. |
| 3 | VAAT 13 items, 1–5 ([VAAT](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf)) | `AnastomosisRubric` with 13 metric functions mapping telemetry to 1–5. Thresholds live in a data file, not in code. |
| 4 | Spacing SD 1.72 vs 2.14 mm; needle load 1.9 vs 2.5 s; stitch 4.6 vs 6.4 s ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)) | Initial "expert" and "trainee" reference values to calibrate scores 5 and 3 (playtest-tuned). |
| 5 | Global rating > checklist for discriminating skill ([Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/)) | Technical layer = graded items; checklist only for safety. |
| 6 | "Score of 4 or greater on EACH assessment tool" ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | Unlock rule: `min(itemScores) >= 4`. |
| 7 | Minimum repetitions of 10 / 7 / 5 ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | Progress bars per drill; the module is not "complete" before the count is reached. |
| 8 | MAE 3 min / 2 min; AIAD 3 min / 20 min; SDCF 4 min; CPB run 30 min ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | Crisis timers on the HUD. Missing a timer caps the SEAT "Knowledge of protocol" score at 3 (design). |
| 9 | SEAT: recognise, communicate, decide, lead, protocol ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | Crisis scorecard. "Recognise" = seconds from onset to the first correct action. |
| 10 | NOTSS 4 categories / 12 elements, 1–4 + N/A ([NOTSS](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)) | NTS layer: element scores computed from event logs, with N/A when not triggered. |
| 11 | Situation awareness linked to technique errors ([Catchpole 2008](https://pubmed.ncbi.nlm.nih.gov/18362635/)) | Low monitor-checking raises the probability of the next technical slip, for example under assist settings (design). |
| 12 | Minor events add up; compensation saves ([de Leval 2000](https://pubmed.ncbi.nlm.nih.gov/10733754/)) | A "risk meter" that accumulates minor events; corrected errors are partly forgiven. |
| 13 | OCHRA consequential vs inconsequential errors ([Tang 2004](https://pubmed.ncbi.nlm.nih.gov/15545569/)) | `error.severity` enum; the debrief shows hazard zones. |
| 14 | Dangerous-zone stitch detection ([Tozzi 2022](https://pubmed.ncbi.nlm.nih.gov/34225333/)) | Hazard volumes (RCA, back wall, conduction tissue later) with contact logging. |
| 15 | STS composite: 4 domains; 5 morbidities; operative mortality definition ([STS ACSD](https://publicreporting.sts.org/acsd-exp), [STS glossary](https://www.sts.org/public-reporting-glossary)) | End-of-case outcome card; LIMA choice credits the IMA domain. |
| 16 | Ramphal: heart rate from arrested to 200 bpm, VF, operator in the anaesthesia role ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | `HeartMotion.rate` range; an AI director plays the "operator". |
| 17 | Beating-heart training is better than non-beating ([Wu 2021](https://pubmed.ncbi.nlm.nih.gov/32305184/)); 70 bpm used ([Fann 2008](https://pubmed.ncbi.nlm.nih.gov/19114195/)) | Difficulty tier: arrested → 60–70 bpm → higher rates. |
| 18 | Top Gun leaderboard effect ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/)) | Challenge mode with ghost replays and weekly "competitions". |
| 19 | Distributed practice ([Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/)); decay after a break ([Feins 2017](https://pubmed.ncbi.nlm.nih.gov/27570162/)) | Session-start re-test; a "skills getting rusty" nudge after N days. |
| 20 | Anchored examples raise rater reliability ([Lou 2014](https://pubmed.ncbi.nlm.nih.gov/25308119/)) | Each rubric item shows a short clip or animation of 1 vs 3 vs 5 performance. |
| 21 | Briefing 8 items; debrief 3 questions ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)) | Briefing UI checklist (scored); debrief UI prompts. |
| 22 | Hicks: ACT not verified (3), poor communication with the perfusionist (4) ([Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/)) | Tutorial "trap" moments that teach these exact misses. |
| 23 | Haptics help novices ([Rangarajan 2020](https://pubmed.ncbi.nlm.nih.gov/31564519/)); Touch device 3.3 N max ([3D Systems](https://www.3dsystems.com/haptics-devices/touch)) | Optional haptic backend; clamp force output ≤ 3.3 N. |
| 24 | XR Hands, 26 joints ([Unity](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html)) | VR hand-tracking input adapter (phase 2). |

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | The TSDA curriculum has 6 modules (CPB, CABG, AVR, MAE, AIAD, SDCF) and 29 sessions of 2–4 h each. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |
| 2 | The 27 residents in the 8-institution study improved on all modules; CPB final mean 4.80, CABG 4.41, AVR 4.51. | https://pubmed.ncbi.nlm.nih.gov/27570162/ | A |
| 3 | The VAAT has 13 items scored 1–5, plus time and pass/fail. | https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf | A |
| 4 | The CPBAT has 8 items, with failure anchors including "No heparin", "Air in line" and "No ACT checked". | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |
| 5 | MAE targets: retrograde perfusion within 3 min; CPB again within 2 min after de-airing. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |
| 6 | AIAD targets: femoral cannulation within 3 min; repair within 20 min. SDCF: CPB re-established within 4 min. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |
| 7 | The Ramphal simulator heart rate ranges from arrested to 200 bpm, and an operator plays perfusion/anaesthesia. | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |
| 8 | OSATS global ratings discriminated training levels but checklists did not; interrater 0.64–0.72. | https://pubmed.ncbi.nlm.nih.gov/9052454/ | A |
| 9 | Coronary anastomosis simulation: skill SMD 1.68; time −205.9 s; fidelity had no significant effect. | https://pubmed.ncbi.nlm.nih.gov/35143631/ | A |
| 10 | None of 16 cardiac simulation studies showed validation evidence for their assessment tools. | https://pubmed.ncbi.nlm.nih.gov/29248416/ | A |
| 11 | Top Gun: 12 components on 1–5; pass 13% → 73%; time 11:10 → 9:04; 23 anastomoses on average. | https://pubmed.ncbi.nlm.nih.gov/25595829/ | A |
| 12 | Boot Camp CPB: 3 residents did not verify ACT, 4 communicated poorly; MAE caused the most errors. | https://pubmed.ncbi.nlm.nih.gov/20451929/ | A |
| 13 | Video-anchored rater training raised composite ICC from 0.76 to 0.90. | https://pubmed.ncbi.nlm.nih.gov/25308119/ | A |
| 14 | NOTSS v2.0: 4 categories, 12 elements, rated 1–4 + N/A; not for summative use; free for personal / not-for-profit use. | https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf | A |
| 15 | ANTS prototype: 4 categories, 15 elements; 50 raters, 8 videos. | https://pubmed.ncbi.nlm.nih.gov/12697584/ | A |
| 16 | STS CABG composite = 4 domains; morbidity = 5 complications; operative mortality definition. | https://publicreporting.sts.org/acsd-exp ; https://www.sts.org/public-reporting-glossary | A |
| 17 | Expert suturing metrics: spacing SD 1.72 vs 2.14 mm; path 6,714 vs 10,154 mm; stitch 4.6 vs 6.4 s. | https://pubmed.ncbi.nlm.nih.gov/42696816/ | A |
| 18 | CPB multimodal assessment: cognitive scores discriminated, technical scores did not; cross-clamp path 47.5 vs 91.9 m. | https://pubmed.ncbi.nlm.nih.gov/32971063/ | A |
| 19 | VR training to criterion: 29% faster and 1.19 vs 7.38 errors per case. | https://pubmed.ncbi.nlm.nih.gov/12368674/ | A |
| 20 | Haptics improved VR training in 6 of 8 RCTs (215 participants). | https://pubmed.ncbi.nlm.nih.gov/31564519/ | A |
| 21 | Distributed practice beat massed practice for retention and transfer. | https://pubmed.ncbi.nlm.nih.gov/16926566/ | A |
| 22 | Beating-heart simulator training beat non-beating training (60 trainees). | https://pubmed.ncbi.nlm.nih.gov/32305184/ | A |
| 23 | Touch Surgery cardiac modules: 5,368 users; RCT 75% vs 61%. | https://pubmed.ncbi.nlm.nih.gov/27568126/ | A |
| 24 | Surgeon Simulator maps fingers to A/W/E/R/Space; the controls are deliberately awkward. | https://en.wikipedia.org/wiki/Surgeon_Simulator ; https://store.steampowered.com/app/233720/Surgeon_Simulator/ | B/C |
| 25 | Trauma Center: stylus, tool icons, timer, C–S ranks, Challenge mode. | https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife | B |
| 26 | 3D Systems Touch: 6-DOF sensing, 3-DOF force, 3.3 N max, 1 kHz, OpenHaptics with Unity/Unreal compatibility. | https://www.3dsystems.com/haptics-devices/touch | A (vendor spec) |
| 27 | Unity XR Hands 1.5.1 exposes 26 points per hand using OpenXR naming. | https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html | A |
| 28 | Expert Delphi agreed on only 40 of 146 anastomosis checklist items (27%). | https://pubmed.ncbi.nlm.nih.gov/29074155/ | A |
| 29 | Osso VR RCT: aggregate global score 17.5 vs 7.5 for VR vs a standard guide (n=20). | https://pubmed.ncbi.nlm.nih.gov/32035854/ | A |
| 30 | The TSDA curriculum forbids reproduction or use without permission (copyright 2015). | https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf | A |

---

## Sources

1. TSDA Cardiac Surgery Simulation Curriculum (PDF, © 2015, uploaded 2016-01) - https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf - Modules, sessions, 7 Steps of CPB, briefing/debrief, ACAT, CPBAT, SEAT, VAAT, crisis timers, Ramphal simulator description, copyright notice.
2. TSDA curriculum web page - https://tsda.org/education/tsda-cardiac-surgery-simulation-curriculum/ - Module list and session template.
3. TSDA Vessel Anastomosis Simulation Module page - https://tsda.org/the-tsda/tsda-vessel-anastomosis-simulation-module/ - Chamberlain Pocket trainer and assessment tool link.
4. TSDA Vessel Anastomosis Assessment (PDF, Oct 2017) - https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf - 13-item 1–5 rubric and general definitions. Licence not stated (UNVERIFIED).
5. Feins RH et al. Simulation-Based Training in Cardiac Surgery. Ann Thorac Surg 2017 - https://pubmed.ncbi.nlm.nih.gov/27570162/ - 27 residents, 6 modules, outcome scores.
6. Mokadam NA et al. Experience With the Cardiac Surgery Simulation Curriculum (survey). Ann Thorac Surg 2017 - https://pubmed.ncbi.nlm.nih.gov/27570163/ - Survey results.
7. Ramphal PS et al. A high fidelity tissue-based cardiac surgical simulator. Eur J Cardiothorac Surg 2005 - https://pubmed.ncbi.nlm.nih.gov/15848335/ - Ramphal simulator design and procedures.
8. Fann JI et al. Boot Camp coronary anastomosis. J Thorac Cardiovasc Surg 2010 - https://pubmed.ncbi.nlm.nih.gov/19846125/ - 33 residents, 10–18 anastomoses, 3-point scale.
9. Fann JI et al. Improvement in coronary anastomosis with cardiac surgery simulation. JTCVS 2008 - https://pubmed.ncbi.nlm.nih.gov/19114195/ - Task station and beating-heart times, 70 bpm.
10. Hicks GL et al. Cardiopulmonary bypass simulation at the Boot Camp. JTCVS 2011 - https://pubmed.ncbi.nlm.nih.gov/20451929/ - CPB crises, typical errors.
11. Fann JI et al. Senior Tour perspective. JTCVS 2012 - https://pubmed.ncbi.nlm.nih.gov/22075060/ - Review of 12 simulators.
12. Enter DH et al. "Top Gun" competition. Ann Thorac Surg 2015 - https://pubmed.ncbi.nlm.nih.gov/25595829/ - Gamified practice results.
13. Lou X et al. Training less-experienced faculty improves reliability. JTCVS 2014 - https://pubmed.ncbi.nlm.nih.gov/25308119/ - ICC and kappa gains with anchored video.
14. Nesbitt JC et al. Tissue-based coronary surgery simulation. JTCVS 2013 - https://pubmed.ncbi.nlm.nih.gov/23499474/ - Students vs residents.
15. Wu S et al. Porcine beating heart simulator. JTCVS 2021 - https://pubmed.ncbi.nlm.nih.gov/32305184/ - Beating vs non-beating RCT.
16. Hermsen JL et al. Multimodal CPB skills assessment. Ann Thorac Surg 2021 - https://pubmed.ncbi.nlm.nih.gov/32971063/ - Cognitive, technical and motion metrics.
17. Burkhart HM et al. Simulation-based training in thoracic surgery residency (CPB). JTCVS 2010 - https://pubmed.ncbi.nlm.nih.gov/20038482/ - Hydraulic CPB simulator; confidence 59% → 92%.
18. O'Dwyer M et al. Coronary anastomosis simulation meta-analysis. BJS Open 2022 (CC BY) - https://pubmed.ncbi.nlm.nih.gov/35143631/ ; full text https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8830760/fullTextXML - Effect sizes, fidelity, scales used.
19. Sidik AI et al. SBT for CABG meta-analysis. J Surg Educ 2026 - https://pubmed.ncbi.nlm.nih.gov/42236427/ - SMD 2.18 / 2.00.
20. Ribeiro IB et al. Simulation-based skill training in cardiac surgery: systematic review. Ann Thorac Surg 2018 - https://pubmed.ncbi.nlm.nih.gov/29248416/ - No tool validation evidence.
21. Arjomandi Rad A et al. SBT in cardiac surgery: systematic review. ICVTS 2023 - https://pubmed.ncbi.nlm.nih.gov/37220905/ - Validity testing in 4 models.
22. Vaporciyan AA et al. Consensus-derived coronary anastomotic checklist. Ann Thorac Surg 2017 - https://pubmed.ncbi.nlm.nih.gov/29074155/ - Expert disagreement.
23. Martin JA et al. OSATS for surgical residents. Br J Surg 1997 - https://pubmed.ncbi.nlm.nih.gov/9052454/ - Global vs checklist.
24. Reznick R et al. Bench station examination. Am J Surg 1997 - https://pubmed.ncbi.nlm.nih.gov/9124632/ - 8 stations; reliability 0.78 / 0.85.
25. Seymour NE et al. VR training improves OR performance. Ann Surg 2002 - https://pubmed.ncbi.nlm.nih.gov/12368674/ - Transfer and error metrics.
26. Rosser JC et al. Impact of video games on training surgeons. Arch Surg 2007 - https://pubmed.ncbi.nlm.nih.gov/17309970/ - Gaming correlation.
27. Rangarajan K et al. Systematic review of virtual haptics. J Surg Educ 2020 - https://pubmed.ncbi.nlm.nih.gov/31564519/ - Haptics evidence.
28. Moulton CA et al. What kind of practice makes perfect? Ann Surg 2006 - https://pubmed.ncbi.nlm.nih.gov/16926566/ - Distributed practice.
29. Blumstein G et al. VR tibial nailing RCT (Osso VR). J Surg Educ 2020 - https://pubmed.ncbi.nlm.nih.gov/32035854/ - VR vs guide.
30. Orland MD et al. VR intramedullary tibial nail RCT. Clin Orthop Relat Res 2020 - https://pubmed.ncbi.nlm.nih.gov/32769533/ - Completion and accuracy.
31. McKinney B et al. VR training in UKA (unicompartmental knee arthroplasty), RCT. J Surg Educ 2022 - https://pubmed.ncbi.nlm.nih.gov/35863958/ - Steps and time.
32. Brewer ZE et al. Mobile cognitive simulator for cardiac surgery (Touch Surgery). Semin Thorac Cardiovasc Surg 2016 - https://pubmed.ncbi.nlm.nih.gov/27568126/ - Cardiac cognitive modules.
33. Khorammakan R et al. Puzzle game-based learning for CABG. BMC Med Educ 2023 - https://pubmed.ncbi.nlm.nih.gov/37055824/ - Serious game example.
34. Tozzi P et al. Heart surgery simulator with integrated supervision (mitral). Simul Healthc 2022 - https://pubmed.ncbi.nlm.nih.gov/34225333/ - Dangerous-zone detection.
35. Wang SX et al. AI-driven suturing simulation for cardiothoracic training. J Surg Educ 2026 - https://pubmed.ncbi.nlm.nih.gov/42696816/ - Motion and suture metrics.
36. Sardari Nia P et al. EACTS endoscopic mitral SBT course. ICVTS 2020 - https://pubmed.ncbi.nlm.nih.gov/31968097/ - Accuracy and time gains.
37. Tang B et al. OCHRA error categorisation. Arch Surg 2004 - https://pubmed.ncbi.nlm.nih.gov/15545569/ - Error model.
38. Catchpole K et al. Teamwork and error in the OR. Ann Surg 2008 - https://pubmed.ncbi.nlm.nih.gov/18362635/ - Situation awareness linked to technique errors.
39. de Leval MR et al. Human factors and cardiac surgery. JTCVS 2000 - https://pubmed.ncbi.nlm.nih.gov/10733754/ - Major and minor events, compensation.
40. Yule S et al. Development of NOTSS. Med Educ 2006 - https://pubmed.ncbi.nlm.nih.gov/17054619/ - NOTSS origin.
41. RCSEd. NOTSS System Handbook v2.0 (2019) - https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf - Taxonomy, scale, licence terms.
42. RCSEd NOTSS page - https://www.rcsed.ac.uk/professional-support-development-resources/learning-resources/non-technical-skills-for-surgeons-notss - Categories, links.
43. Fletcher G et al. ANTS behavioural marker system. Br J Anaesth 2003 - https://pubmed.ncbi.nlm.nih.gov/12697584/ - ANTS structure.
44. Eppich W, Cheng A. PEARLS debriefing. Simul Healthc 2015 - https://pubmed.ncbi.nlm.nih.gov/25710312/ - Blended debrief.
45. Gerstein NS et al. CPB emergencies and intraoperative issues. J Cardiothorac Vasc Anesth 2022 - https://pubmed.ncbi.nlm.nih.gov/36100499/ - Equipment crisis list.
46. Bienstock J et al. Simulation in perfusion education, 2025 survey. J Extra Corpor Technol 2026 - https://pubmed.ncbi.nlm.nih.gov/42319097/ - Perfusion simulation use.
47. STS Public Reporting home - https://publicreporting.sts.org/ - Procedures rated.
48. STS Adult Cardiac star rating explanation - https://publicreporting.sts.org/acsd-exp - Composite domains, 36-month window.
49. STS Public Reporting glossary - https://www.sts.org/public-reporting-glossary - Operative mortality and morbidity definitions.
50. Surgeon Simulator (Wikipedia) - https://en.wikipedia.org/wiki/Surgeon_Simulator - Controls, sales, sequel.
51. Surgeon Simulator (Steam store page) - https://store.steampowered.com/app/233720/Surgeon_Simulator/ - Reviews, deliberate control difficulty.
52. Trauma Center: Under the Knife (Wikipedia) - https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife - Mechanics, ranks, reception.
53. Touch Surgery (Wikipedia) - https://en.wikipedia.org/wiki/Touch_Surgery - Scope, validation claims.
54. Osso VR home - https://www.ossovr.com/ - Marketing claims (flagged).
55. Osso VR health systems - https://www.ossovr.com/health-systems - Practice and Test modes, collaboration.
56. Osso VR research list - https://www.ossovr.com/vr-surgical-training-research - Study list.
57. FundamentalXR - https://www.fundamentalxr.com/ - Haptics and analytics positioning; unverified marketing figures.
58. Surgical Science (incl. Simbionix) - https://surgicalscience.com/ - Product lines, "400+ validation studies" claim.
59. VirtaMed clinical evidence - https://www.virtamed.com/en/clinical-evidence - Metric types.
60. Mentice simulators - https://www.mentice.com/simulators - VIST G7, TEE Trainer.
61. Mentice publications - https://www.mentice.com/publications - VIST validation list.
62. Chamberlain Group cardiothoracic catalogue - https://www.thecgroup.com/specialty/cardiothoracic - Vessel sizes, beating hearts, aortic roots.
63. Chamberlain CABG Beating Heart #1339 - https://www.thecgroup.com/product/cabg-beating-heart-trainer/ - Programmable rate, dimensions.
64. Chamberlain ECMO/Perfusion Team Trainer #1502 - https://www.thecgroup.com/product/enhanced-ecmo-perfusion-team-trainer-1502/ - Califia/Orpheus interface.
65. Biomed Simulation (Califia) - https://www.biomedsimulation.com/ - Perfusion simulator.
66. 3D Systems Touch haptic device - https://www.3dsystems.com/haptics-devices/touch - Haptic specs.
67. Unity XR Hands 1.5 manual - https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html - Version 1.5.1, providers.
68. Unity XR Hands data model - https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/hand-data/xr-hand-data-model.html - 26 joints.
69. MediaPipe (GitHub) - https://github.com/google-ai-edge/mediapipe - Apache-2.0, platforms.
70. Vosk API (GitHub) - https://github.com/alphacep/vosk-api - Apache-2.0, offline, about 50 MB models.

### Licence and version table for tools, data and assets mentioned
| Item | Version / date | Licence | Personal non-commercial use? | Attribution / SA / ND | Source |
|---|---|---|---|---|---|
| TSDA Cardiac Surgery Simulation Curriculum | © 2015; PDF uploaded 2016-01 | All rights reserved: "No part … may be reproduced, distributed or used without permission" | Reading yes; **copying text into the game: no without permission** | Treat as all rights reserved | [TSDA PDF p. iv](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf) |
| TSDA Vessel Anastomosis Assessment PDF | Created Oct 2017 | **UNVERIFIED** (no licence on the document) | Unknown; paraphrase and design our own rubric | Unknown | [VAAT PDF](https://tsda.org/wp-content/uploads/2017/10/Vessel-Anastomosis-Assessment.pdf) |
| NOTSS Handbook | v2.0, 2019 | RCSEd copyright; free reproduction for personal, organisational, not-for-profit use; no commercial reproduction | **Yes** | Credit RCSEd/UoA (assumed good practice); no derivative clause stated (uncertain) | [NOTSS handbook p. 2](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf) |
| ANTS handbook | Unknown | **UNVERIFIED** | Unknown | Unknown | (Aberdeen page 404) |
| OSATS rating items | 1997 papers | **UNVERIFIED** (published research instrument) | Likely fine to reference; reproduce with citation (uncertain) | Cite | [Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/) |
| O'Dwyer 2022 meta-analysis | 2022 | CC BY (open access per record) | Yes | Attribution | [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8830760/fullTextXML) |
| Unity XR Hands | 1.5.1 | **UNVERIFIED** (Unity package licence not fetched) | Likely yes under Unity terms (uncertain) | Unknown | [Unity docs](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html) |
| OpenHaptics SDK (3D Systems) | Not stated | **UNVERIFIED** (proprietary SDK) | Unknown | Unknown | [3D Systems](https://www.3dsystems.com/haptics-devices/touch) |
| MediaPipe | Release not stated on page | Apache-2.0 (repo label) | Yes | Keep the licence and NOTICE; no SA | [GitHub](https://github.com/google-ai-edge/mediapipe) |
| Vosk API | Release not stated on page | Apache-2.0 (repo label); model licences not checked (**UNVERIFIED**) | Yes (code) | Keep the licence; no SA | [GitHub](https://github.com/alphacep/vosk-api) |
| Commercial games and simulators (Surgeon Simulator, Trauma Center, Osso, etc.) | various | Proprietary | Benchmarks only: **no assets, names or UI copied** | n/a | sources 50–65 |

---

## Summary

**Key findings**
1. A complete, published cardiac-surgery simulation curriculum exists: TSDA, with 6 modules and 29 sessions. It has explicit assessment tools (VAAT 13 items, ACAT 12, CPBAT 8, SEAT 5), mastery rules (≥4 on every item), repetition counts (10/7/5) and crisis time targets (3/2/3/20/4/30 min) ([TSDA PDF](https://tsda.org/wp-content/uploads/2016/01/Cardiac-Surgery-Simulation-Curriculum-TSDA.pdf)). It is the best "level design document" available for this game.
2. Coronary anastomosis is the most evidence-rich task: two meta-analyses ([O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/); [Sidik 2026](https://pubmed.ncbi.nlm.nih.gov/42236427/)) and published expert vs trainee motion values ([Wang 2026](https://pubmed.ncbi.nlm.nih.gov/42696816/)). Simulator fidelity did not change learning gains ([O'Dwyer 2022](https://pubmed.ncbi.nlm.nih.gov/35143631/)).
3. For CPB, decisions and communication separate experts from trainees more than hand skill does ([Hermsen 2021](https://pubmed.ncbi.nlm.nih.gov/32971063/)). Typical trainee misses are the ACT check and communication with the perfusionist, and MAE is the hardest crisis ([Hicks 2011](https://pubmed.ncbi.nlm.nih.gov/20451929/)).
4. Global-rating style items beat binary checklists for discriminating skill ([Martin 1997](https://pubmed.ncbi.nlm.nih.gov/9052454/)). Experts disagree on checklist contents ([Vaporciyan 2017](https://pubmed.ncbi.nlm.nih.gov/29074155/)), and cardiac simulation tools are rarely validated ([Ribeiro 2018](https://pubmed.ncbi.nlm.nih.gov/29248416/)).
5. NOTSS v2.0 (4 × 12, scale 1–4 + N/A) is free for personal / not-for-profit use and fits a formative debrief ([NOTSS handbook](https://www.rcsed.ac.uk/media/ypmnkyhn/notss-handbook.pdf)). STS gives a clean outcome vocabulary: operative mortality, 5 morbidities and the 4-domain CABG composite ([STS](https://publicreporting.sts.org/acsd-exp)).
6. Gamification works in this field: the Top Gun leaderboard raised pass rates from 13% to 73% ([Enter 2015](https://pubmed.ncbi.nlm.nih.gov/25595829/)). Distributed practice beats massed practice ([Moulton 2006](https://pubmed.ncbi.nlm.nih.gov/16926566/)).
7. Entertainment games teach UX lessons. Copy Trauma Center's tool palette, timer and ranks ([Wikipedia](https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife)). Avoid Surgeon Simulator's per-finger mapping ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator)).

**Recommendations**
- Build the MVP around **CPB + CABG to the LAD + 2 crises (protamine reaction, MAE)**. Use desktop controls first, with a Learn mode gate at 90%.
- Implement scoring as 4 visible layers (Technical / Process-safety / Non-technical / Outcome). Add never events and the TSDA "all items ≥4" pass rule. Keep all thresholds in data files so experts can tune them.
- Write **our own rubric text**, inspired by but not copied from TSDA tools, because of their copyright. NOTSS terms may be used with credit under its not-for-profit permission.
- Use AI teammates with closed-loop commands and an AI "operator/director" modelled on the Ramphal simulator.
- Ship timeline replay and a PEARLS + TSDA-style debrief from day one.
- Plan VR (controllers, then optional hand tracking through XR Hands) and haptics (3D Systems Touch) as later phases.

**Open questions**
1. The exact OSATS global rating item wording (from memory here) needs the full Martin 1997 text.
2. Is the MAE score of 0.68 in Feins 2017 a typo or a different scale? Full-text check needed.
3. The AIAD "within 3 minutes of the time air is recognized" wording in TSDA is probably a copy error; confirm the intended trigger.
4. Licence status of the TSDA VAAT PDF, the ANTS handbook, Unity XR Hands, OpenHaptics and the Vosk models: all UNVERIFIED.
5. KindHeart and HeartWorks: official pages unreachable on 2026-11-03, so their current status and products are not confirmed.
6. Score thresholds (mm, degrees, seconds) for each rubric level need expert review or playtest calibration. The published expert/trainee values are only anchors.
7. The STS prolonged-ventilation threshold and full morbidity definitions need the STS data specifications (not fetched here).
8. This run could not use keyword web search (the shared budget was exhausted). A follow-up run with search could add academic VR cardiac surgery projects and newer haptic or hand-tracking accuracy studies not reachable by direct fetch.
