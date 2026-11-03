# 05 — Visual and audio realism: fresh research

**Research date:** 2026-11-03. **Status:** planning recommendations, not implemented or clinically validated. Scope is an adult on-pump CABG game. The highest-value realism is consistency between anatomy, tool contact, physiological state, visible motion, monitors, and team responses. A polished heart that behaves incorrectly fails this goal.

**Evidence notation:** “Evidence” describes the cited source; “Proposal” is a project design choice requiring testing. Sources were searched and opened on the research date. Clinical observations are not universal numerical presets. No reference photographs, videos, recordings, or proprietary alarm files were downloaded for redistribution.

## 1. Anatomy and materials before cinematic effects

**Proposal:** create one approved thorax/heart assembly before patient variety. Preserve physical scale, anatomical orientation, coronary courses, great-vessel connections, pericardial relationships, sternum, and access depth. Keep an inspectable anatomy view beside the operative view; a clinically reviewed visibility mask should determine what the player can actually see through the exposure. Do not expose deep structures merely to make the operation easy. Expert review should include where epicardial fat obscures vessels and how retraction changes the field.

Use a compact material library whose parameters are art controls, not claimed tissue measurements:

| Surface | Proposed visible treatment | Interaction requirements |
|---|---|---|
| Myocardial/epicardial surface | Regional color variation, restrained subsurface scattering, uneven wet highlights; avoid uniform glossy red | Moves with the heart and local tool deformation; lesions are explicit authored variants |
| Epicardial fat | Lobulated pale/yellow geometry with local thickness variation | Obscures underlying anatomy; not a flat color overlay |
| Pericardium and fascia | Thin fibrous sheets, thickness-aware translucency where supported | Separate surfaces with edges and contact response; no penetration during retraction |
| Vessel and graft | Diameter/taper, wall and lumen, distinct cut edge | Visible collapse, clamping and stitch deformation correspond to simulated state |
| Sternum and cut bone | Cortical/cancellous distinction, restrained porosity | Cutting/exposure state controls geometry, debris, and local bleeding cues |
| Drapes, gloves and instruments | Different roughness and scale; brushed steel directionality; cloth folds | Tool tips remain readable under wet highlights and magnification |
| Blood and irrigation | Surface films, pooling, staining and fluid removal | Driven by the fluid accounting model; never decorative unlimited bleeding |

**Evidence:** Unreal's Subsurface Profile is a screen-space scattering approximation developed for skin-like surfaces; its exposed artist controls do not establish organ optical accuracy. **Proposal:** test it as one rendering option, with an opaque fallback for thin surgical layers and difficult silhouettes. Freeze lighting/exposure before tuning tissue color; otherwise material changes can compensate for lighting errors. [Epic: Subsurface Profile Shading Model](https://dev.epicgames.com/documentation/unreal-engine/subsurface-profile-shading-model-in-unreal-engine).

**Proposal:** make wetness a separate state from base tissue color. Track surface film, pooled volume, irrigation dilution, and material changes from tool events separately. Use bounded decals, local pool geometry and sparse droplets first. Match visible accumulation/removal to simulated bleeding, suction and irrigation; a high-fidelity fluid solver is unnecessary for the first slice. Blood color can vary with the modeled source and rendering, but should never be the game's sole oxygenation measurement. Distinguish blood from irrigation in the volume ledger. “Clotted” appearance must follow the coagulation scenario, not merely a cosmetic timer during anticoagulated bypass.

Electrosurgery effects should follow activation, contact and material state: localized marking, brief smoke, sound, and visibility changes. Avoid constant sparks or screen-filling smoke. These are proposed visual proxies, not a thermal-injury solver. Review their appearance and effect on gameplay with clinicians.

## 2. Cardiac motion has several independent causes

**Evidence:** tagged MRI describes spatially varying shortening, radial deformation, base-to-apex motion, and torsion; a uniform scale pulse is a poor representation of ventricular motion. MRI of an intact heart does not directly establish the motion of an exposed, unloaded, manipulated heart. [Moore, McVeigh and Zerhouni, *Quantitative Tagged Magnetic Resonance Imaging of the Normal Human Left Ventricle*, 2000, DOI 10.1097/00002142-200012000-00005; PMID 11153703](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396311/).

**Proposal:** separate five inputs: electrical rhythm, mechanical activation, filling/loading, respiratory/body motion, and external manipulation. Render motion from the authoritative physiology state. Begin with reviewed shape-key/skeletal curves plus local contact deformation; defer full electromechanical FEM. Use distinct atrial, ventricular, basal and apical controls rather than one “heartbeat intensity” slider. Tool contact and sutures must remain attached to the deformed surface.

| Scenario | Required proposed presentation contract |
|---|---|
| Native beating | Phase-related ECG, contraction and pressure; physiological delays are explicit, not frame coincidence |
| Bypass with unloading | Shape/filling changes independent of native electrical activity; motion does not alone indicate systemic perfusion |
| Cardioplegic arrest | Suppressed coordinated contraction according to the modeled arrest state; passive movement from contact and ventilation remains possible |
| Ventricular fibrillation | Incoherent motion pattern; no normal stroke animation; circulation reflects pump support and native effectiveness separately |
| Reperfusion/recovery | Rhythm, filling and contractility recover according to the scenario, not a guaranteed animation transition after clamp removal |
| Pacing/electrical activity without effective contraction | Electrical marker can exist without a corresponding useful pulse; interface identifies signal source |

These contracts need clinical review; they do not specify treatment. Aortic cross-clamping, pump flow, cardioplegia, ECG and mechanical arrest are separate states. Turning on bypass must not automatically stop all heart animation. Returning an ECG trace must not automatically restore a healthy pressure waveform.

## 3. Operating room, lighting and viewpoint

**Evidence:** AORN's 2024 design toolkit describes lighting for the surgical field and patient monitoring, with control of spot size, shadow, color and placement. **Proposal:** use this as a layout checklist, not a claim that a rendered room meets facility standards. [AORN, *Design in Depth*, lighting section, PDF page 19](https://www.aorn.org/docs/default-source/tool-kit-documents/construction/components/construction_and_design_2.pdf?sfvrsn=9730b9e_5).

Start with one reviewed room arrangement: surgeon and assistant working zones, scrub handoff zone and instrument table, anesthesia access at the head, and perfusion workstation with plausible line routing. Layout varies by team and equipment; do not designate one arrangement as universal. Give tubes, hands, retractors and instruments collision priorities so they do not visibly pass through each other. Use simplified bodies beyond the field rather than expensive photorealistic faces.

Provide a stable operative camera, controlled lean/orbit, and a magnified working view. Label the magnified view as a gameplay aid unless optical characteristics have been reviewed. Do not simulate depth of field so strongly that needle tips become unreadable. Disable gratuitous head bob and camera shake. Maintain anatomical scale and an adjustable operating position for left/right handed controls.

Use field lights plus room fill, stable white balance and constrained exposure. Test light placement with both hands and a retractor present, including partial shadow and instrument glare. Realistic obstruction should matter, but a teammate should have a readable repositioning interaction instead of trapping the player's view. Keep monitor text readable without making every display unrealistically self-illuminating.

## 4. Audio and monitors must describe the same patient

**Evidence:** the ASA monitoring standard, amended October 15, 2025, includes oxygenation, ventilation, circulation and temperature assessment, and audible pulse-oximeter variable-pitch tone and low-threshold alarm. **Proposal:** reproduce the informational relationships with original sounds and explicit monitor-source settings; do not reproduce a manufacturer's interface wholesale. [ASA, *Standards for Basic Anesthetic Monitoring*](https://www.asahq.org/standards-and-practice-parameters/standards-for-basic-anesthetic-monitoring).

**Evidence:** the APSF's June 2024 report and manufacturer response discuss circumstances where pulse-oximeter pulse-rate output and associated tone did not faithfully indicate pulsatile flow, including CPB and motion/low-signal situations. This is device- and circumstance-dependent; it does not establish that all pulse oximeters behave identically. **Proposal:** signal validity, averaging and artifacts belong in a sensor layer separate from physiological truth. [APSF, *Pulse Oximetric Pulse Rate: What Are We Measuring?*](https://www.apsf.org/article/pulse-oximetric-pulse-rate-what-are-we-measuring/).

**Evidence:** the AATS CPB primer describes loss of arterial pulsatility during typical nonpulsatile pump support. **Proposal:** display mean pressure and waveform appropriate to the modeled pump configuration; do not maintain a decorative normal arterial pulse during arrested-heart nonpulsatile bypass. Also avoid depicting an absent pulse as absent oxygenation when the circuit is providing support. [AATS, *Cardiopulmonary Bypass Fundamentals*](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals).

The audio event specification should include:

- Pulse tone: timing from the selected measured pulse source; pitch from valid measured saturation where appropriate. Missing/invalid data has an explicit behavior.
- Alarm: source, priority, trigger, validity condition, acknowledgement and silence/retrigger state; visible explanation and event-log entry accompany it.
- Pump and suction: equipment operation and fluid interaction drive layers; do not infer medically calibrated sound-to-flow mappings without evidence.
- Saw/electrosurgery: activation, contact and release produce distinct layers; no sound when an inactive tool merely touches tissue.
- Instrument handling: limited contact sounds based on metal, tray, glove and tissue surfaces.
- Team dialogue: short requests, acknowledgements and status changes triggered by actual task state. Captions identify speaker and timing; prerecorded or authored lines are safer for consistency than unconstrained generated clinical dialogue.

Use spatial placement for room equipment and voices, with an optional accessible mix. Separate mechanical ambience, informative signals and dialogue buses. Prevent masking of task-critical cues without continuous dramatic music. Provide captions and a visual equivalent for every audio-only gameplay signal.

**Evidence:** IEC 60601-1-8:2006+AMD1:2012+AMD2:2020 addresses alarm priorities, signals, control states and tests for medical equipment. Only the official public description was accessed; the complete paid standard was not reviewed. **Proposal:** label the game's alarms as original simulated alarms. Do not claim IEC compliance, exact standard reproduction, or clinically validated recognition training. [IEC official consolidated edition 2.2](https://webstore.iec.ch/en/publication/67388).

## 5. Reference use and content controls

CTSNet's authored sternotomy demonstration is a useful candidate for observing exposure, instrument scale and tissue appearance. Its page and description were read; the embedded video was not frame-reviewed in this research pass. Annotated video review with a surgeon remains a production task. [Jayakumar et al., *CTSNet Step-by-Step Series: Midline Sternotomy*, 2017, DOI 10.25373/ctsnet.5345287](https://www.ctsnet.org/article-video/ctsnet-step-step-series-midline-sternotomy/).

Reference access is not asset permission. Record source URL, author, observation, review date, and reviewer in a reference index; obtain rights separately before shipping frames, textures, audio or derivatives that reproduce protected material. Use original materials and synthesized/recorded sounds with documented ownership. No patient-identifying imagery or live clinical recordings enter the repository without an appropriate permission and de-identification process.

Offer full, reduced and schematic tissue presentation, with explicit labeling. Reduced intensity may suppress splashes, graphic closeups and smoke while preserving blood-volume consequences, occlusion information and alerts. A schematic view is an accessibility/learning aid, not a claim of identical visual realism. Provide configurable camera motion, subtitle size, contrast, and non-color cues.

## 6. Acceptance rubric and staged delivery

**Proposal:** prioritize one exposed-heart interaction scene with five states: native beat, unloaded bypass, arrest, fibrillation, and supported recovery. Add one controlled leak/suction scenario and one sensor-artifact scenario. Proposed checks below are production gates, not validated medical assessment instruments.

| Domain | Evidence required before the scene passes |
|---|---|
| Anatomy | Surgeon-reviewed landmarks, scale, exposure and tool access; no unresolved major anatomical error |
| Motion | Clinician review of each state and transition; no uniform balloon-like contraction or detached coronary/suture geometry |
| Tissue interaction | Retraction/contact visible at the collision location; no persistent tool penetration or apparent grasp without contact |
| Fluids | Visible pools and removal reconcile with the simulation ledger; blood and irrigation are separately accounted |
| Monitor/audio consistency | Recorded scenario timeline aligns motion, pressure, ECG, sensor quality, tones and team calls; deliberate artifacts are identified |
| Readability | Needle tips, vessel edges and alarms remain identifiable at supported resolution and magnification |
| Performance | Measured scene timings meet the chosen engine budget with wet materials, hands, tools and monitors active |
| Accessibility | Critical information survives audio mute, color differences and reduced-intensity presentation |

Review stills, short synchronized captures and raw event traces together. A visually convincing screenshot is insufficient. Track reviewer role, feedback, defects and revisions; seek cardiac surgeon, anesthesia and perfusion input for their respective cues. Face/content review does not establish learning transfer or clinical competence.

## 7. Search log, limitations and recommendations

Searches included: `ASA standards basic anesthetic monitoring`, `APSF cardiopulmonary bypass pulse oximetry nonpulsatile waveform`, `IEC 60601-1-8 alarm systems`, `Epic subsurface profile shading model`, `MRI tagging left ventricular torsion`, `CTSNet sternotomy video`, and `AORN surgical lighting`. Primary organization pages and the linked research manuscript were opened; search snippets alone were not treated as sufficient for exact standards claims.

Blender manual shape-key and Principled-material URLs failed to load through the web tool (402); no version-specific Blender capability claim depends on those fetches. MRI evidence does not validate exposed-heart motion, the IEC text was not obtained, and no real OR sound library or anatomical reference has been cleared for redistribution.

Recommendation: spend the first realism effort on geometry, working visibility, synchronized physiological cues and original audio. Add subtle wetness, subsurface scattering, local blood and smoke after those contracts pass. Unresolved work is expert reference review, precise material calibration, target-display testing and acquisition of any separately licensed references.
