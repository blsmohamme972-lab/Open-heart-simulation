# Research Prompts (reusable)

> **2026-11-03 refresh:** the topic prompts below are retained as the historical research brief. Apply the updated evidence rules here when rerunning them. Do not fill a requested numeric table with guesses or treat the prompt's suggested engine/procedure as a verified conclusion.

## Updated evidence rules

- Open primary sources after searching; record access date, exact source version and any blocked/full-text limitations. Do not invent PMIDs, versions, prices or license terms.
- Distinguish source facts, proposed software behavior, engineering estimates and clinical-review requirements. Numbers need context, units, population, procedure phase and measurement method.
- A request for drug doses or exact timings does not justify a universal clinical protocol. Record conflicts; defer executable parameters to a reviewed case specification.
- Check each asset's exact item/release terms and engine compatibility. Personal/noncommercial intent does not waive public-repository redistribution restrictions. Separate candidate, acquired, inspected and shipping-approved states.
- Verify software capability in documentation; executable support and performance remain untested until experiments run. ECMO is not equivalent to surgical CPB; FEM is not automatically ground truth.
- Assessment studies support only their measured outcomes. Do not turn mortality rates into random failure odds or describe a game score as validated clinical competence.
- End with concrete implementation decisions, evidence gaps and pass/fail experiments. Preserve source URLs and original attribution rather than copying media or assessment forms.

The completed fresh reports are indexed in [the master plan](../../../PLAN.md). These updated rules supersede contradictory assumptions in the historical prompts below.

These are the prompts used in Step 1. You can paste them into any AI agent with web access (Claude, ChatGPT,
Gemini, Perplexity, etc.) to repeat or extend the research. Comparing answers from several agents is a good way
to find mistakes.

**How to use:** paste the **Common instructions** first, then **one** topic prompt. Use one agent (or one chat) per topic.
Save each answer as `docs/plan/research/<number>-<topic>.md`.

---

## Common instructions (paste first, every time)

```
You are a research agent for a PLANNING project: a realistic open heart surgery simulation GAME
(personal, non-commercial, educational; not a certified medical device). The owner wants it
"as close as possible to real life" and is happy to use free assets licensed for personal /
non-commercial use, Blender, and other free tools. No game code is being written yet; your job
is research that will feed the plan.

Rules:
- Use web research. Search and read real sources.
- Prefer primary/authoritative sources (surgical textbooks, society guidelines, peer-reviewed
  papers, official project/license pages, official engine docs). Cite URLs inline next to claims.
- For every asset, library or tool you recommend, state its exact license, whether personal /
  non-commercial use is allowed, and whether attribution or share-alike applies. If you could
  not verify a license, write "UNVERIFIED".
- Be concrete: numbers, ranges, names, versions, step orders. Avoid vague statements.
- Mark anything you are unsure of with "(uncertain)".
- Output a full report in Markdown, then end with a short summary: key findings,
  recommendations, open questions.
```

---

## 01 — Surgical procedure

```
Topic: the REAL open heart surgery procedure, step by step, so the game can replicate it.
Cover:
1. Which procedures to model. Recommend a primary procedure for v1 (likely on-pump CABG via
   median sternotomy) and candidates for later (aortic valve replacement, mitral valve
   repair/replacement, off-pump CABG). Justify.
2. For the primary procedure, a complete ordered step list from patient entry to ICU transfer:
   positioning, prep and draping, time-out/WHO checklist, skin incision, sternotomy, sternal
   retractor, conduit harvest (LIMA takedown, saphenous vein harvest), pericardiotomy and stay
   sutures, heparinization and ACT target, aortic and venous cannulation (order, purse-string
   sutures), initiating cardiopulmonary bypass, cooling, aortic cross-clamp, cardioplegia
   delivery (antegrade/retrograde, intervals), arrest, distal anastomoses, proximal
   anastomoses, de-airing, cross-clamp removal, reperfusion, rewarming, defibrillation if VF,
   epicardial pacing wires, weaning from bypass, protamine reversal, decannulation, hemostasis,
   chest tubes, sternal wiring, closure.
3. For each step: who does it (surgeon, assistant, scrub nurse, anesthesiologist,
   perfusionist), exact instrument names, typical duration, success criteria, and common
   errors and complications.
4. Typical total timings (skin-to-skin, bypass time, cross-clamp time).
5. Real OR call-outs ("on bypass", "cross-clamp on", "cardioplegia in", etc.).
```

## 02 — Physiology, anesthesia and perfusion

```
Topic: PHYSIOLOGY, ANESTHESIA and PERFUSION simulation for the game.
Cover:
1. Open-source physiology engines usable in a game: Kitware Pulse Physiology Engine, BioGears,
   CircAdapt, OpenCOR/CellML models, HumMod, simple Windkessel models. License, APIs,
   Unity/Unreal integration, fidelity, performance, and whether they model cardiopulmonary bypass.
2. Cardiopulmonary bypass circuit: components, typical flows, MAP targets on bypass,
   temperatures, hematocrit, ACT targets, heparin and protamine dosing, cardioplegia types.
3. Normal and abnormal vital sign ranges to display (ECG rhythms, arterial line, CVP, PA
   pressure, SpO2, EtCO2, temperature, urine output, ABG, lactate, potassium, glucose) and how
   each responds to surgical events.
4. Anesthesia: induction and maintenance drugs, vasopressors/inotropes, typical doses and effects.
5. A recommended modelling approach for the game, with justification.
```

## 03 — Assets and licensing

```
Topic: FREE 3D/2D/AUDIO ASSETS and their LICENSES for the game (personal / non-commercial use
is acceptable, but record exact terms).
Cover, with URLs and exact licenses:
1. Anatomy: BodyParts3D, Z-Anatomy, Open Anatomy Project, NIH 3D heart models, Human Reference
   Atlas 3D organs, Visible Human Project, Embodi3D, specific high-quality Sketchfab CC heart /
   thorax / coronary / sternum models (author + license), segmentation datasets convertible to
   meshes.
2. Surgical instruments and OR equipment models; Poly Haven and ambientCG materials/HDRIs.
3. Tissue textures/materials and photo references.
4. Audio: freesound.org licenses, OR ambience, monitor beeps, bypass machine, saw, suction, cautery.
5. Humans/characters: MakeHuman/MPFB2, Mixamo, Character Creator, MetaHuman (terms).
6. A Blender pipeline: clean, retopologize, UV, bake, rig (heartbeat blend shapes), export.
7. A license compliance approach: an ASSET_LICENSES.md register format and which licenses
   (CC BY-NC, CC BY-SA, ND) carry constraints even for personal use.
```

## 04 — Engine and simulation tech

```
Topic: GAME ENGINE and SIMULATION TECHNOLOGY for a realistic surgical simulation.
Cover:
1. Engine comparison: Unreal Engine 5, Unity 6, Godot 4 — licensing, soft bodies, fluids,
   rendering, VR (OpenXR, Quest 3, PC VR).
2. Soft-tissue simulation: SOFA Framework (+ Unity/Unreal integrations), XPBD, FEM, PhysX 5 FEM,
   NVIDIA Warp, mass-spring; what surgical simulator research uses.
3. Hard problems and techniques: mesh cutting, tearing, suturing and knot tying, tool-tissue
   collision, retraction, clamping vessels, blood (SPH, screen-space fluids, decals), the
   beating heart (blend shapes vs physics vs FEM driven by physiology), cannulation.
4. Haptic devices and SDKs (OpenHaptics, CHAI3D — licenses) and VR hand tracking.
5. Performance budgets for 90 Hz VR vs 60 Hz desktop.
6. A recommended stack and a fallback stack, with reasoning.
```

## 05 — Visual and audio realism

```
Topic: VISUAL and AUDIO REALISM for a surgical simulation.
Cover:
1. Realistic tissue rendering: subsurface scattering, wet surfaces, epicardial fat,
   pericardium, blood (fresh, clotted, pooling, staining), cautery char and smoke.
2. Beating heart realism: correct motion pattern and torsion, ECG-driven timing, cardioplegic
   arrest, ventricular fibrillation, reperfusion.
3. OR realism: surgical lighting, sterile field layout, team positions, camera views, loupe
   magnification.
4. Audio: monitor tones (SpO2 pitch), IEC 60601-1-8 alarms, bypass machine, saw, cautery,
   suction, staff call-outs, spatial audio.
5. Legitimate educational reference sources (reference only, do not ship).
6. Practical ways for a solo developer to reach high realism without AAA budgets.
```

## 06 — Game design and benchmarks

```
Topic: GAME DESIGN and BENCHMARKS from existing surgical simulators and games.
Cover:
1. Existing products (Surgeon Simulator, Trauma Center, Touch Surgery, Osso VR, FundamentalVR,
   Simbionix, VirtaMed, Heartworks, cardiac surgery simulators, academic VR projects): what they
   do well, mechanics, assessment.
2. Scoring grounded in real assessment: OSATS, procedure checklists, error tracking, economy of
   motion, time, tissue damage, blood loss, patient outcome, team communication.
3. Game structure: modes, difficulty, patient variants, progression, debrief/replay.
4. Controls: mouse/keyboard, gamepad, VR, hand tracking, haptics — mapping fine motor tasks.
5. Player role(s) and AI teammates.
6. Recommended core loop and MVP feature set.
```

## 07 — Production, tools and validation

```
Topic: PRODUCTION PLANNING, TOOLS and VALIDATION for a solo/small-team realistic surgery game.
Cover:
1. Realistic scope for 3, 6, 12, 24 months; vertical-slice strategy.
2. Tooling: Git LFS and alternatives, project management, CI builds for Unity/Unreal,
   automated testing (engine tests, physiology regression tests, deterministic replays).
3. Free AI-assisted asset tools, procedural tools, photogrammetry — with licenses.
4. Medical validation: consulting surgeons/perfusionists, face/content validity, documenting sources.
5. Legal/ethical: disclaimers, not a medical device, ESRB/PEGI gore ratings, de-identified data only.
6. Risk register: top technical, content and scope risks with mitigations.
```

---

## 00 — Gap critic (run after all 7 reports exist)

```
You are a completeness critic for the planning of a realistic open heart surgery simulation
game. I will paste 7 research reports below. Read all of them, then produce:
1. Contradictions between reports.
2. Important topics missing or too thin for an "as close as possible to real life" goal.
3. Claims that look wrong or unsourced (especially medical numbers and licenses) — verify the
   5 most important ones with web search.
4. A consolidated list of decisions the design step must make.

<paste reports 01–07 here>
```
