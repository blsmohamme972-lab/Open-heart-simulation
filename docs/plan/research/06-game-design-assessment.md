# 06 — Gameplay, controls, assessment and benchmarks

Research refreshed: **2026-11-03**. Status: planning evidence and proposed design; no game implementation or clinical validation. Sources were searched and opened during this research pass. Product pages describe vendor offerings, not independent proof of effectiveness. All mechanics below are proposals unless explicitly described as a research finding.

## Recommendation

Build a desktop-first, single-player simulation of **one reviewed adult elective on-pump CABG case**, with the player acting as surgeon and a simulated multidisciplinary team managing its assigned responsibilities. Develop one coronary anastomosis exercise and a short linked perfusion scenario before attempting the whole case. Progress should come from understanding anatomy, controlling instruments, recognizing changing conditions and communicating with the team.

Accuracy has separate dimensions: anatomical structure, task sequence, tissue response, physiology, team behavior and input-device behavior. A successful checklist or realistic image cannot establish all six. The first release can support deliberate practice within a bounded simulation; it cannot claim that mouse performance measures real surgical competence.

## 1. Benchmarks and what their evidence supports

| Benchmark | Verified finding | Design implication and limit |
|---|---|---|
| Ramphal tissue-based cardiac simulator | Ramphal et al., *A high fidelity tissue-based cardiac surgical simulator* (2005), describes a computer-assisted biological-tissue preparation supporting coronary and valve procedures and adverse scenarios. [Primary publication, PMID 15848335](https://pubmed.ncbi.nlm.nih.gov/15848335/) | Include a working operative environment and evolving patient state. Its physical tissue/tool behavior does not establish the fidelity of a digital model. |
| Cardiac anastomosis Boot Camp | Fann et al. report a coronary anastomosis curriculum using component exercises, assessment and practice. [Primary study, full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4146435/) | Build repeatable partial tasks before a full operation. This study is not evidence that an untested consumer control scheme transfers to clinical practice. |
| Touch Surgery cardiac modules | Brewer et al., *Creation and Global Deployment of a Mobile, Application-Based Cognitive Simulator for Cardiac Surgical Procedures* (2016), randomized 16 preclinical medical students to modules or reading. Four modules covered sternotomy, cannulation, decannulation and sternal closure; the outcome was a multiple-choice assessment. [PMID 27568126; DOI 10.1053/j.semtcvs.2016.02.006](https://pubmed.ncbi.nlm.nih.gov/27568126/) | Supports investigating procedural knowledge exercises. It does not establish fine motor skill, tissue mechanics or CABG outcome transfer. Do not combine its cognitive evidence with unrelated haptic evidence to claim a validated full-case simulator. |
| HeartWorks | The manufacturer describes interactive cardiac anatomy and transthoracic, transesophageal and 3D echocardiography learning. [Official product description](https://surgicalscience.com/simulators/heartworks/) | Useful benchmark for anatomy exploration and echo-to-anatomy correspondence. It is not evidence of open-heart cutting or suturing simulation. |
| Osso VR | Its assessment announcement describes workflow and technique assessment with milestone-based progression. [Vendor announcement, 2021](https://www.ossovr.com/post/press-osso-vr-adds-localization-and-first-of-its-kind-assessment-experiences) | Borrow the concept of task-specific feedback and progression. Proprietary metrics, vendor superiority claims and results from other procedures are not validation of this project. |
| Fundamental Surgery haptics | A randomized trial reports improved performance for an orthopedic bone-drilling task after haptic versus non-haptic VR training. [Primary study, PMID 36389184](https://pubmed.ncbi.nlm.nih.gov/36389184/), [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC9661648/) | Justifies a later haptic feasibility study. Bone drilling differs from coronary suturing; neither effect size nor training validity transfers automatically. Full-text access was intermittently blocked during this pass; no detailed numerical claim is adopted. |

Surgeon Simulator and Trauma Center are entertainment references, not clinical validation sources. Their interaction patterns are not adopted as accuracy benchmarks. A broad catalog of laparoscopic, orthopedic and endovascular simulators would add less value than the cardiac and assessment evidence above; Simbionix and VirtaMed capabilities require module-specific investigation if a later feature depends on them.

These products and their illustrations are **reference only**. No license to redistribute their software, clinical cases, scoring forms, videos or assets was verified. Do not copy them into the repository. Reuse original design principles and independently authored content.

## 2. The core loop and modes

Proposed loop: **inspect → form a plan → prepare and communicate → manipulate → observe consequences → reassess → review and repeat**. Every important action should affect a persistent state: anatomy, a tool, a team task, circuit configuration, physiology or an observation. A correct answer in a dialogue cannot substitute for an unfinished physical action.

| Mode | Purpose | Assistance and result |
|---|---|---|
| Anatomy and instrument orientation | Learn landmarks, instrument identity and spatial relationships | Labels, isolation views and demonstrations; no competence score |
| Guided task | Learn one bounded action and its rationale | Ghost trajectory, anatomy highlighting, explicit prerequisite explanations and pausing |
| Practice task | Repeat instrument and decision exercises | Adjustable assistance, stable scenario seeds, immediate or delayed feedback |
| Integrated case | Follow the reviewed CABG workflow with parallel team activity | Limited hints, persistent consequences, pause/save; end-of-case debrief |
| Scenario challenge | Investigate one reviewed deviation | Controlled starting conditions and known causal mechanism; introduced after the normal case passes review |

Separate interface help, motor assistance, clinical hints and patient complexity. Difficulty must not silently change anatomy, physiological laws or safety prerequisites. Increasing complexity should introduce documented patient variants and observable complications, not arbitrary instant-death chances. Do not turn population mortality percentages into random failure probabilities.

Case time and wall-clock time must be recorded separately. Fast-forward may advance reviewed stable waiting periods only; it must not bypass required observations or erase deterioration. Practice-mode rewind creates a new attempt with the earlier record preserved. A full-case save must restore the same pending tasks, tool state, physiological state and random seed.

The first vertical slice should begin with an already exposed, prepared operative field. It should include grasp/retract, needle positioning, bounded tissue passage, suture handling, inspection of the resulting anastomosis, one modeled quality defect and a debrief. Complete entry-to-ICU coverage follows only after this slice establishes useful interaction and credible consequences.

## 3. Desktop precision controls

All mappings are provisional and must be tested with both experienced game users and clinical reviewers. A mouse supplies limited degrees of freedom and no tissue force; the interface must make its constraints legible.

| Action | Proposed mapping | Fidelity boundary |
|---|---|---|
| Position active instrument | Mouse moves in a visible task plane; wheel or dedicated keys adjust depth | Surface projection is assistance, not direct hand tracking |
| Orient instrument | Dedicated rotate mode for pitch/yaw, separate roll keys; persistent orientation cue | Switching modes interrupts natural movement; test accidental rotation rates |
| Open/close jaws | Remappable control with optional toggle rather than sustained hold | Closure position is not a measured surgeon grip force |
| Precision manipulation | User-selectable lower motion gain and anchored camera/loupe view | Scaling improves usability but changes task difficulty; log it |
| Use two tools | Explicit active-hand switching; inactive tool can hold a reviewed constraint | A held retraction constraint substitutes for continuous bimanual control |
| Pass a needle | Acquire and orient needle, choose permitted entry/exit region, follow its curved path | Authored passage paths are a bounded approximation, not arbitrary tissue penetration |
| Handle suture/knot | Explicit grasp points, tension feedback and a constrained tying interaction | Log assisted versus free segments; no claim of physical knot competence |
| Move camera | Separate camera control; moving the camera does not accidentally move a tool | Collision and tool contact remain active unless practice mode is paused |

Assistance presets should disclose exactly what they change: snapping, trajectory guidance, motion damping, automatic instrument orientation, assistant stabilization and knot completion. Retain the settings in every replay. Never compare assisted and unassisted task scores as equivalent.

Prototype three tasks first: target acquisition without unintended contact, curved needle passage, and simultaneous exposure plus manipulation. Record endpoint error, missed selections, unintended tissue contact, mode-switch errors, completion and user discomfort. Set acceptance thresholds after observed pilot distributions and reviewer agreement, rather than inventing millimeter tolerances from screen resolution.

Gamepad can offer an accessible command/navigation path, but fine-manipulation equivalence is unproven. VR controllers, hand tracking and force-feedback devices are later input profiles with separate validation. Tracking loss must suspend the affected tool safely and produce a recorded event, not an uncontrolled cut. Controller vibration is not calibrated tissue resistance.

## 4. The operating-room team

Represent surgeon, assistant, scrub nurse, anesthesiologist and perfusionist as separate task owners. Anesthesia and perfusion should continue their reviewed background responsibilities while the player operates. Requests should contain recipient, action, relevant object and prerequisites; each task moves through requested, acknowledged, active, completed or unable states.

Use closed-loop communication as a design reference: receipt of a request and confirmation of completion are different events. AHRQ describes check-back as verification of exchanged information. [TeamSTEPPS check-back tool](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/checkback.html) Proposed dialogue should be newly written and reviewed for the selected protocol.

For example, requesting a perfusion transition should elicit the team's current readiness and a completion report from the modeled circuit, rather than instantly changing a procedure-stage flag. An unavailable instrument should remain unavailable until the scrub nurse's retrieval task completes. A colleague's concern should expose the relevant observation and require acknowledgement; it should not magically reveal a hidden diagnosis.

Use authored commands and deterministic task logic initially. Optional voice recognition can select those same commands, with visible confirmation for ambiguity. Free-form generative dialogue must not calculate medication, bypass prerequisites or decide patient state. The team should refuse impossible actions and explain the actual failed precondition; clinically plausible errors may remain possible where their consequences are modeled.

## 5. Consequences and assessment

Use a reviewed event graph rather than a single health bar. Example design chains include: excessive modeled traction → local injury state → altered bleeding/visibility → changed observations; an anastomosis defect → altered modeled flow/resistance → graft assessment finding; an unresolved team task → delayed transition → continued exposure to the current physiological condition. These are proposed abstractions; exact mechanisms, thresholds and recovery behavior require the procedure and physiology reviews.

An event needs a timestamp, actor, affected structure, measured input, precondition result, state change, observation availability and source/rule identifier. Record what the player could actually know. An error should be distinguishable from an interface failure and from an unmodeled response.

The original OSATS study compared checklists, global ratings and pass/fail judgments in surgical residents; its global ratings discriminated experience levels better than checklists in that study. [Martin et al., 1997, PMID 9052454; DOI 10.1046/j.1365-2168.1997.02502.x](https://pubmed.ncbi.nlm.nih.gov/9052454/) This supports combining process checks with qualitative review. It does **not** make an automated game score an OSATS assessment. Reproducing any published assessment form requires a separate rights check.

Proposed debrief dimensions:

- **Task completion:** prerequisites, omissions and appropriate response to changes.
- **Tissue handling:** contact location, modeled damage and avoidable repeated manipulation.
- **Technical result:** simulated anastomosis geometry, leak and flow measures within the validated model domain.
- **Situational awareness:** observations obtained, interpretation opportunities and response delays.
- **Team coordination:** request ownership, acknowledgements, completion checks and handoff completeness.
- **Efficiency:** unnecessary instrument travel or repetition, with patient condition and assistance level retained.

Report these separately with evidence clips. Do not average a severe unresolved defect away with speed points. Elapsed time is contextual feedback; a fast unsafe run must not outrank a careful successful run. Simulated blood loss and modeled patient outcome are useful consequences but remain model outputs, not direct skill measurements. Until reviewed thresholds exist, use descriptive feedback rather than clinical pass/fail labels.

## 6. Debrief, replay and accessibility

PEARLS combines learner self-assessment, focused discussion and directive feedback. [Eppich and Cheng, 2015, PMID 25710312; DOI 10.1097/SIH.0000000000000072](https://pubmed.ncbi.nlm.nih.gov/25710312/) Adapt that structure with original text: ask what the player noticed, show a short event timeline with synchronized operative/monitor views, explain the modeled causal chain, and offer one focused repeat exercise. An automated explanation is not a trained facilitator, and it must disclose model uncertainty.

Save scenario version, content and rule versions, assistance configuration, input-device profile, random seed, commands and periodic state snapshots. Scrubbing should reconstruct observations and team messages. Counterfactual replay must be labeled as another simulated run, not a prediction of what a real patient would have experienced.

Provide remappable controls, left-handed layouts, adjustable motion gain, alternatives to holds/repeated presses, scalable labels, contrast options and captions for speech plus meaningful non-speech sounds. Microsoft's caption guideline explicitly treats non-speech cues as information requiring an alternative presentation. [Xbox Accessibility Guideline 104](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104) Captions should identify the speaker/device; monitor warnings must not rely on color or audio alone.

Offer reduced blood intensity, reduced smoke and camera-motion controls, while preserving the observation needed to understand a modeled event. If a visual filter hides a relevant cue, provide an equivalent informational cue and record the setting. Keep accessibility settings separate from clinical knowledge hints. Graphic-content preferences should be available before entering an operative scene.

## 7. Validation gates and remaining decisions

Before calling a task accurate, obtain a structured review from a cardiac surgeon plus the relevant anesthesia/perfusion professional: task coverage, allowable variation, observable cues, input assumptions, consequence chains and misleading omissions. Record disagreements and protocol-specific alternatives. A plausible-looking demo is a face-validity finding at most, not evidence of educational transfer.

Before comparing scores, check whether repeated identical inputs produce consistent results and whether two reviewers interpret the proposed rubric consistently. Test whether expert users are penalized mainly by unfamiliar game controls; offer equivalent familiarization before any experience-group comparison. Investigate knowledge retention and transfer separately only if educational claims become a goal, using a study designed for that claim.

Open decisions are the target hardware, intended audience, available reviewers, acceptable desktop assistance, amount of authored suturing, whether integrated cases allow pausing, and which complications can be supported by verified models. Proposed default: local single-player, assisted desktop interaction, pausing available, one normal case and a small reviewed set of deviations, with no leaderboard or competence certificate.

## Search and verification log

Queries included `Martin Regehr OSATS 1997 PubMed`, `Eppich Cheng PEARLS 2015 PubMed`, `Ramphal cardiac surgery simulator`, `HeartWorks official`, `Touch Surgery simulations clinical literature`, `Osso VR assessment`, `Fundamental Surgery haptic trial`, `TeamSTEPPS check-back`, and `Xbox accessibility captions`. Vendor bibliographies were used to locate primary papers, then identifiers and outcomes were checked against the publication records.

This is a targeted planning review, not a systematic review. The strongest directly relevant cognitive study located was small and measured knowledge; physical cardiac-training studies used different interfaces and materials. The plan therefore adopts supported design ideas while leaving this game's realism, assessment reliability and educational effectiveness explicitly unverified.
