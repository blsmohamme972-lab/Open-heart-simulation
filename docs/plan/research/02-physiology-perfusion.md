# Research 02 — Physiology, anesthesia and perfusion

> Re-researched: **2026-11-03**. Planning only; no engine or game implementation was tested. Scope: fictional adult elective on-pump CABG. **Verified** means a cited source was inspected; **proposed** means a software design requiring implementation and review. A plausible model is not evidence of clinical accuracy.

## 1. Recommendation and corrections

Use one authoritative physiology backend behind a game-independent interface. Evaluate **Pulse 4.4.0** first, but make the choice conditional on a CPB feasibility experiment. Develop a bounded, custom lumped-parameter CPB model only if the experiment fails and sufficient modeling/review capacity exists. Do not blend two independently evolving patients or replace inconvenient engine values with decorative monitor numbers.

The previous draft overstated certainty. Remove the claims that Pulse is the only maintained validated option, that custom CPB automatically offers “full” fidelity, that performance costs are negligible, and that reproducing published equations removes every licensing concern. Remove drug doses and immediate deterministic outcome rules that were not tied to a specific validated scenario. Current documentation does not support the draft's blanket assertions that drug plasma concentrations are “currently incorrect” or every response takes 30–60 seconds. The present [Pulse drug methodology](https://pulse.kitware.com/_drugs_methodology.html) instead describes qualitative/expert validation, incomplete interactions, and limits for delayed mechanisms. These remain material limitations.

Retain the distinction between ECMO and surgical CPB. Neither a product's validation label nor a realistic waveform demonstrates that its combination of cardioplegic arrest, cross-clamping, reservoir drainage and myocardial recovery is valid.

## 2. Candidate engines: verified capabilities and permission boundaries

| Candidate | Evidence and limits for this project | License and disposition |
|---|---|---|
| **Pulse 4.4.0** | The [version history](https://pulse.kitware.com/version.html) identifies 4.4.0 as August 2026; a [release announcement](https://www.kitware.com/pulse-v4-4-0-release/) appeared September 30. C++ core with C, C#, Java and Python interfaces; official Unity and Unreal integrations are linked from the [project home](https://pulse.kitware.com/). Plugin compatibility with our eventual engine/version remains untested. | Apache-2.0; personal/noncommercial use permitted. Preserve license, relevant notices and modification notices; no share-alike requirement. Inspect each pinned plugin and dependency separately. First feasibility candidate. |
| **BioGears** | [Maintainer repository](https://github.com/BioGearsEngine/core) describes a C++ whole-body engine with standalone and integration use. The inspected README calls its latest deployment beta. No verified ready-made CABG/CPB workflow was found in this review; absence from inspected material is not proof that no extension exists. No comparative runtime benchmark was performed. | Apache-2.0 in the repository; preserve applicable license/NOTICE material. Personal/noncommercial use permitted, no share-alike. Alternative evaluation candidate, not a demonstrated CPB replacement. |
| **CircAdapt Framework** | [Official documentation](https://framework.circadapt.org/latest/) targets customizable cardiovascular mechanics and hemodynamics. Attractive for research comparison; whole-body CPB suitability was not established. | [Custom EULA](https://framework.circadapt.org/latest/license.html) defines users as academic researchers, restricts sublicensing and requires permission for redistribution of developer improvements. Hobby use and public game redistribution are not established by “noncommercial.” Exclude from the dependency plan unless the intended use is expressly licensed. |
| **OpenCOR / libOpenCOR** | A modeling environment/library for CellML, not a turnkey cardiac surgery patient. Distinguish products: [legacy OpenCOR](https://opencor.ws/licensing.html) is GPL-3.0; [libOpenCOR](https://github.com/opencor/libopencor) and the separate [new webapp](https://github.com/opencor/webapp) declare Apache-2.0. Each model has its own provenance and rights. | Personal use allowed by these software licenses. GPL distribution obligations differ from Apache notice obligations. Pin exact product and model revision; do not describe all OpenCOR software with one license. Useful for offline model experiments. |
| **HumMod** | Broad integrative physiology, but the [official terms](https://hummod.org/agreement/) expressly distinguish personal experimentation from integration. No ready-made game CPB interface was verified. | XML descriptions: GPL-2.0. Other products/integration: custom permission requirements. Use as a standalone research reference only; do not assume embeddability. |
| **Custom 0-D model** | A closed-loop compartment model can represent the chosen scenario explicitly. [Smith et al., 2004](https://pubmed.ncbi.nlm.nih.gov/15036180/) demonstrates a minimal model of ventricular interaction and valve dynamics; it does not validate our CPB extension. | Original implementation can have our chosen code license. Check any copied model files, code, figures and parameter datasets separately. More controllable scope, substantially greater validation burden. |

**Pulse-specific evidence.** Its [ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html) documents VA/VV connections, gas exchange, fluid administration and clinical-data comparisons for VV gas exchange. The pump is an ideal flow source, some cannulation sites share lumped nodes, and anticoagulation, thrombosis and hemolysis are absent. This supports an extracorporeal starting point, not a CPB claim. Its [cardiovascular methodology](https://pulse.kitware.com/_cardiovascular_methodology.html) uses a lumped circulation and template ECG; the arrhythmia text states later actions do not affect hemodynamics in certain arrested rhythms. This makes externally pumped circulation during arrest a required experiment rather than a presumed incompatibility. Documentation and the pinned implementation may differ.

## 3. Proposed coupled state model

All requirements below are **proposed abstractions**, to be inspected by a cardiac anesthesiologist and perfusionist alongside the surgical reviewer.

Represent native systemic/pulmonary circulation and the extracorporeal circuit in one volume and substance ledger. Suggested components: chambers and vascular compartments; venous drainage; reservoir; pump; oxygenator; heat exchanger; arterial return; surgical vent; cardiotomy suction; blood collection and external loss. Each connection has direction rules, resistance, contents and clamp state. Procedure phases change connections and permissible actions, not an arbitrary “patient health” score.

| Subsystem | Required state and coupling | Explicit boundary |
|---|---|---|
| Circulation | Pressure, volume, flow, resistance, compliance, contractility, preload/afterload; distinguish native cardiac output, pump flow and effective systemic perfusion. | A compartment cannot resolve local jet trauma or coronary wall stresses. |
| Reservoir and pump | Drainage, actual reservoir volume, suction return, pump command versus delivered flow, pressure and low-level/bubble sensor states. | Centrifugal RPM must not equal fixed flow. A pump curve requires selected-device data or a clearly synthetic curve. |
| Oxygen transport | Hemoglobin mass/concentration, arterial and venous oxygen content, saturation, metabolic demand and oxygenator transfer. | Saturation alone cannot represent oxygen delivery. Do not claim regional brain/kidney injury prediction. |
| Temperature | Blood/circuit and patient tissue stores, sensor location and lag, exchanger transfer, temperature-dependent demand. | One scalar temperature cannot represent outlet, core and peripheral measurements. |
| Rhythm and myocardium | Separate electrical rhythm, mechanical contraction, coronary supply, clamp/protection state and recovery state. | An arrested but perfused patient is not automatically dead; no instant full recovery when the clamp is removed. |
| Bleeding and dilution | Site-specific leak linked to source pressure; lost blood, retained field blood, suction destinations, prime and product contents. | Visual blood quantity must reflect this ledger, never generate extra fluid or oxygen capacity. |
| Gas exchange/ventilation | Native lung and oxygenator contributions, sweep gas, delivered oxygen fraction, ventilator state and gas measurement site. | Airway end-tidal CO2 is not an interchangeable reading of oxygenator exhaust CO2 or arterial CO2. |
| Chemistry/coagulation | Model only supported substances mechanistically; separate measured ACT, drug exposure and abstract coagulation state. | ACT is not a complete coagulation model; [Pulse blood chemistry](https://pulse.kitware.com/_blood_chemistry_methodology.html) identifies missing cellular/coagulation mechanisms. |

For the first playable slice, use bounded representations of myocardial protection, anticoagulation and delayed injury. State explicitly in the fidelity register that these are scenario models. Potassium, calcium, lactate, glucose, renal output and acid–base results must either come from a coupled validated subsystem or be labeled scenario-controlled observations. Do not invent precise biochemical trajectories to fill a monitor.

The heart mesh and audio subscribe to physiological snapshots. Sinus contraction, low contractility, fibrillation and arrest require distinct motion; mechanical motion must follow ventricular state rather than ECG artwork alone. Surgical errors enter the backend as documented events, such as a leak area or obstruction, with one owner responsible for converting that event to physiology.

## 4. Medical reference anchors and parameter governance

These are **source-checking anchors**, not universal treatment rules or final game settings. The [2024 EACTS/EACTAIC/EBCP adult CPB guideline](https://doi.org/10.1093/ejcts/ezae354), published in 2025, describes usual indexed flows of 2.2–2.8 L/min/m² under moderate hypothermia-to-normothermia, recommends MAP 50–80 mmHg after ensuring adequate anesthesia/flow, and recommends a minimum indexed oxygen delivery of 280 mL/min/m² to reduce stage-1 AKI risk. It also supports individualized assessment. These recommendations do not establish deterministic organ-damage thresholds.

The [STS/SCA/AmSECT anticoagulation guideline, 2018](https://www.sts.org/sites/default/files/documents/Anticoagulation-During-Cardiopulmonary-Bypass-Guideline-2018.pdf) treats ACT thresholds as method-dependent; commonly cited 480-second and some approximately 400-second thresholds cannot be mixed without identifying the assay/system. The selected fictional protocol must record the device and justification. Heparin response and reversal must not be a universal linear dose-to-ACT equation.

The [2015 temperature guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC4631211/) distinguishes arterial outlet, venous inflow and patient temperature. Examples include outlet blood below 37°C and an outlet–inflow gradient no greater than 10°C; it offers tighter rewarming guidance once outlet temperature is at least 30°C. Record the exact recommendation context instead of penalizing any temperature difference generically.

Every parameter needs this record before it affects assessment:

`id | meaning | unit | compartment/site | population | procedure phase | source URL + section/table | source date | value/range | evidence type | assay/device | uncertainty | reviewer/date | model version | assessment enabled?`

Keep three independent ranges: **reference physiology**, **scenario starting envelope**, and **alert/assessment limits**. A lab reference interval is not automatically an intraoperative target. Coefficients chosen for numerical stability or gameplay carry `synthetic`, never `clinical`.

Use explicit dimensions: volume mL internally; flow mL/s internally with L/min displays; pressures mmHg or a documented SI conversion; concentration g/dL versus g/L; oxygen content mL O2/dL; saturation fraction internally versus percent on screen; temperature °C; ACT seconds; substance amounts with explicit mg/µg/IU distinctions. For a unit test, `1 L/min = 1000/60 mL/s`. Oxygen delivery derived from L/min flow and mL O2/dL content requires the 10 dL/L conversion; indexing divides by m². Validate concentration changes after prime against conserved substance mass.

## 5. Anesthesia and credible monitors

Initial player scope is surgeon with an anesthesia teammate, not an unrestricted drug calculator. Plan reviewed actions for induction/maintenance, ventilation, analgesia, neuromuscular blockade, vasoactive support and anticoagulation/reversal. Each action needs indication context, route, delay, duration, contraindication handling and a measured response. Anesthesia, analgesia and paralysis are separate states. Require a visible request–acknowledgment–effect sequence so an intervention cannot happen instantly because a dialogue line played.

Do not import the old dose table as implementation data. A later expert-approved formulary must cite current product labeling and the chosen institutional-style fictional protocol, reconcile units, then verify the selected engine's actual drug files and response limitations. Pending that review, model teammate decisions within authored scenarios rather than accepting arbitrary dose combinations.

Monitors need values **plus** timestamp, sample source, validity, confidence/status, filtering and delay:

- ECG: electrical rhythm and electrode/cautery artifact; rate may differ from palpable/mechanical pulse.
- Arterial pressure: waveform and time-averaged MAP; damped line, disconnection and transducer offset as independent observation faults.
- CVP and optional pulmonary artery measures: named locations, waveform quality and catheter validity. These are not direct volume meters.
- Pulse oximetry: a measurement model, not exact arterial saturation. [FDA documentation](https://www.fda.gov/medical-devices/products-and-medical-procedures/pulse-oximeters) records accuracy limitations including poor circulation and skin-related factors. Test low-pulsatility dropout without a fabricated universal skin-tone correction.
- Capnography: airway sampling and ventilation/perfusion dependence; show missing data when sampling is invalid.
- Temperature: separate outlet/inflow and selected patient sites.
- Blood gases, hemoglobin/hematocrit, electrolytes, lactate, glucose and ACT: sample time, result delay, site and model/source limitation.
- Urine output and fluid balance: accumulated volume and elapsed time; prevent one frame's low flow from diagnosing injury.

A stale value must look stale. Alarm acknowledgment changes alarm presentation, not patient state. Fault scenarios must retain access to alternate observations so identifying artifact is playable.

## 6. Feasibility experiment and acceptance gates

**Planned experiment; not performed in this planning task.** Budget an initial two-week engineering spike, then re-estimate. Pin Pulse core, plugin, data files, dependencies and target platform. Reproduce upstream scenarios before evaluating the game adapter. Capture results and failures in a versioned matrix.

Test: stabilized adult phenotype → extracorporeal support → reduction of native mechanical function → pump-supported arrest → restoration of native function → weaning. Add independent perturbations to pump flow, venous drainage, oxygenator gas, volume and temperature. Inspect the source paths for any unsupported connection or arrest behavior.

Proceed with Pulse only if the chosen API exposes required state/actions, pump-supported arrest works without patched monitor values, conservation checks pass, transitions can be saved/restored, and a perfusionist accepts the limited scenario behavior. If custom circuit edits are needed, record their maintenance and revalidation cost. If it fails, explicitly choose between funding a custom backend and reducing the initial scenario; do not hide the limitation.

The custom candidate starts with a minimal closed-loop circulation and circuit; add complexity only to satisfy a scenario or observation. Determine integration step and solver through convergence experiments. A higher update rate alone does not make the model more accurate. Keep physiology time independent from rendering, process all elapsed simulation steps, and make pause, acceleration and replay use the same clock.

## 7. Verification and validation plan

| Check | Required evidence before claiming support |
|---|---|
| Conservation | Sum patient, circuit, field, collected and discarded volume; account for every external source/sink. Check hemoglobin and transported substances independently. |
| Numerical stability | Finite values, permitted pressure/volume domain, nonnegative mass, bounded fractions; compare output under smaller timestep with declared tolerances. Never silently clamp large errors. |
| Baseline | Stable synthetic patient and circuit over a defined interval; acceptable drift agreed before testing. |
| Hemorrhage/prime | Lost mass leaves its source; prime dilutes concentration; suction only returns its actual contents to its configured destination. |
| CPB transition | Native and pump contributions reconcile; systemic support during arrest is possible only with a functioning connected circuit. |
| Obstruction/reservoir | Drainage restriction changes reservoir balance and available delivered flow; low-level detection precedes the authored hazardous condition. |
| Oxygenator | Sweep and oxygen-fraction perturbations produce reviewed directional changes without creating gas or blood mass. |
| Protection/recovery | Clamp and protection timers interact; removing a clamp does not erase accumulated scenario injury. |
| Observations | Artifact changes monitor output without silently changing true physiology; sampling delays survive save/load. |
| Reproducibility | Same initial state, parameters, seed and ordered actions reproduce results within declared numeric tolerance; record platform/version. |

Use different data for tuning and evaluation where available. Record reference population, individual traces versus aggregate means, and mismatch limits. Run expert review of both successful and failed cases; separate face plausibility from quantitative validity and educational transfer. An engine-to-engine match is a useful regression comparison, not independent clinical validation.

## 8. Search record and remaining uncertainty

Fresh queries included `Pulse ECMO methodology 4.4 2026`, `CircAdapt academic researcher license`, `OpenCOR libOpenCOR license`, `2024 EACTS EACTAIC EBCP oxygen delivery`, `STS anticoagulation 480 400`, `minimal haemodynamic model Smith Chase 2004`, and `FDA pulse oximeter limitations`. Official source pages above were inspected on **2026-11-03**. The 2024 guideline publisher/PMC HTML intermittently failed; its recommendation tables and relevant text were checked through the [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11947607/fullTextXML). The Smith paper identity was verified as PMID **15036180**, DOI **10.1016/j.medengphy.2003.10.001**; only its abstract was used here.

Unresolved: executable Pulse arrest/ECMO behavior; exact current plugin build compatibility; CPB-specific validation datasets and reuse rights; selected pump/oxygenator characteristics; expert-approved scenario envelopes and formulary; computational cost on the eventual hardware. No compiled integration, clinical expert approval or runtime performance measurement is claimed. These are implementation gates, not missing research disguised as settled facts.
