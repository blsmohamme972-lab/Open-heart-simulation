# Research 07: Production, tools, validation and legal

> **Purpose.** Give the plan an evidence-backed basis for scope, schedule, tooling (version control, CI, tests), free and AI-assisted asset tools, medical validation, legal and ethical limits, and a risk register for a solo / small-team, non-commercial, "as close as possible to real life" open heart surgery simulation game.
>
> **Researched 2026-11-03 (re-do, fresh searches).** Prices, quotas and licenses change often. Every number below carries the URL it came from. Re-check the marked items before you commit money or ship.
>
> **Disclaimer.** This is planning research for a game. It is **not clinical guidance**, not legal advice, and not a regulatory opinion. Physiological numbers quoted here are for simulation design and testing only.

**Abbreviations (defined once).** CPB = cardiopulmonary bypass. HLM = heart-lung machine. CABG = coronary artery bypass grafting. AVR = aortic valve replacement. MAP = mean arterial pressure. CVP = central venous pressure. SVR = systemic vascular resistance. CI = continuous integration. LFS = Git Large File Storage. VCS = version control system. UVCS = Unity Version Control. SME = subject-matter expert. MDSW = medical device software. MDR = EU Medical Device Regulation 2017/745. PHI = protected health information. SA = ShareAlike. NC = NonCommercial. ND = NoDerivatives. VS = vertical slice.

**Evidence grades.** A = primary/authoritative (guideline, peer-reviewed paper, official docs or license page). B = reputable secondary. C = weak (blog, forum, snippet). "(uncertain - snippet only)" = the page could not be opened; only a search snippet was seen.

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| First milestone | Build a **physiology-first vertical slice** of one phase ("go on CPB, cross-clamp, cardioplegia arrest") in ~3 months, not a whole operation. | One-scenario VR perfusion simulator was published as an alpha with a single scenario "initiating cardiopulmonary bypass" ([Babar 2023, PMC10579814](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/)); a vertical slice is a small playable part built to final quality ([Game Developer, C](https://www.gamedeveloper.com/design/why-we-should-stop-saying-vertical-slices-)). |
| Content roadmap | Follow the US cardiac surgery simulation curriculum structure: CPB, CABG, AVR + 3 adverse events. | 6 modules, 39 sessions later cut to 29 ([STS press release](https://www.sts.org/sites/default/files/press-releases/Simulation%20FINAL%2082516.pdf), [Feins et al. PDF](https://core.ac.uk/download/304667056.pdf)). |
| Version control (Unity) | Unity Version Control free tier (no seat fee, 25 GB/month storage, 100 GB egress) **or** Git + LFS with strict budget. | [Unity support](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges); [GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs). |
| Version control (Unreal / large binaries) | Perforce P4 free (5 users, 20 workspaces) self-hosted, or Diversion Indie (5 free users, 100 GB). | [Perforce free](https://www.perforce.com/products/helix-core/free-version-control); [Diversion pricing](https://www.diversion.dev/pricing). |
| GitHub LFS budget | GitHub Free = 10 GiB LFS storage + 10 GiB bandwidth per month; CI downloads count; usage is blocked at quota without payment method. Keep raw scans/source art outside LFS. | [GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs). |
| CI | GitHub Actions + GameCI (`unity-builder@v4`, `unity-test-runner@v4`) for Unity; self-hosted runner for Unreal. | [GameCI builder](https://game.ci/docs/github/builder); [GameCI test runner](https://game.ci/docs/github/test-runner); [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions). |
| Automated tests | Engine-free physiology unit tests + **regression tests against expert reference ranges** + deterministic input replays + screenshot tests for monitors. | Pulse keeps scenario results as a baseline ([Pulse, B](https://pulse.kitware.com/_scenario_file.html)); Orpheus CPB simulator validated against survey ranges ([Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)). |
| Asset licenses | Prefer CC0 (Poly Haven, ambientCG), own Blender work, and own photogrammetry (Meshroom MPL-2.0 / COLMAP BSD). Treat CC BY-SA (Z-Anatomy) and NC assets as "infectious / non-sellable". | [Poly Haven](https://polyhaven.com/license); [ambientCG](https://docs.ambientcg.com/license/); [Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy). |
| AI 3D tools | Usable for props only, after a license check per tool. Hunyuan3D 2.1 is **not licensed in the EU, UK or South Korea**. TRELLIS.2 code is MIT but depends on nvdiffrast (research/evaluation only). | [Hunyuan3D-2.1 LICENSE](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE); [TRELLIS.2](https://github.com/microsoft/TRELLIS.2); [nvdiffrast LICENSE](https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt). |
| Medical validation | Use Messick / Kane framing (not "face validity" alone); run a small modified Delphi (2-3 rounds, a-priori 75% agreement); objective range checks like Orpheus. | [Cook & Hatala 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/); [Nasa 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8299905/); [Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf). |
| Medical device status | Keep it a generic training game: no patient-specific planning, no diagnosis. FDA lists "games that simulate ... cardiac arrest scenarios to train health professionals" as not devices. | [FDA examples](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices); [MDCG 2019-11](https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native). |
| Ratings / store | Expect ESRB T to M and PEGI 16-ish if realistic blood is shown; add a gore/clinical-detail setting; disclose mature content and AI content on Steam. | [ESRB guide](https://www.esrb.org/ratings-guide/); [PEGI labels](https://www.pegi.info/what-do-the-labels-mean); [Steam content survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey). |
| Patient data | Only public, already de-identified, licensed datasets (e.g., TCIA CC BY collections). Never use images obtained privately from a hospital. | [45 CFR 164.514](https://www.law.cornell.edu/cfr/text/45/164.514); [GDPR Recital 26](https://gdpr-info.eu/recitals/no-26/); [TCIA policy (snippet)](https://wiki.cancerimagingarchive.net/x/c4hF). |
| Brands | Use fictional equipment brands; no logos. | Nominative fair use test ([New Kids, snippet](https://caselaw.findlaw.com/us-9th-circuit/1233126.html)); Rogers test limits after Jack Daniel's ([Wikipedia, C](https://en.wikipedia.org/wiki/Jack_Daniel%27s_Properties,_Inc._v._VIP_Products_LLC)). |

---

## 1. Realistic scope and schedule

### 1.1 Benchmarks from real projects

| Project | Team | Time | What shipped | Lesson for this game | Source (grade) |
|---|---|---|---|---|---|
| Surgeon Simulator (2013) | 4 people (Jackson, Good, Williams, Broadley) | 48-hour game jam prototype, then 48 days to the commercial version; Steam release 19 Apr 2013 | Comedic heart transplant in Unity; ~2 million copies by 4 Feb 2015 | A tiny, focused loop can ship fast. It was **not** realistic; realism multiplies the work. | [Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator) (B) |
| Project Hospital (2018) | Planned for "a team of 2-4 people" | Studio formed early 2016; released 30 Oct 2018 (~2.5-3 years) | Realistic hospital management sim in Unity | A medically trained designer plus doctors in a private forum checked terminology and simplifications. Probabilities were tuned "for interesting cases over strict reality". | [J Geek Studies interview](https://jgeekstudies.org/2020/03/08/project-hospital-a-realistic-take-on-hospital-simulation) (B); [Wikipedia](https://en.wikipedia.org/wiki/Project_Hospital) (B) |
| Stardew Valley (2016) | Solo | ~4.5 years (2012-2016) | Full commercial game | Solo full-scope games take years, even without medical accuracy work. | [Stardew wiki](https://stardewvalleywiki.com/Stardew_Valley) (C, uncertain - snippet only) |
| VR perfusion simulator (Erasmus MC, 2023) | Academic team (authors were co-developers) | Not stated | Unreal Engine 4, Meta Quest 2, **one** scenario "initiating cardiopulmonary bypass"; alpha; users could not make mistakes | Even an academic team published only one phase first. | [Babar et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/) (A) |
| US cardiac surgery simulation curriculum | 8 residency programs, AHRQ grant | 39 sessions, later 29 | 6 modules: CPB, CABG, AVR + 3 adverse events | A ready-made, expert-built content order for our roadmap. | [STS press release](https://www.sts.org/sites/default/files/press-releases/Simulation%20FINAL%2082516.pdf) (B); [Feins et al. PDF](https://core.ac.uk/download/304667056.pdf) (A) |

**Why projects slip.** An analysis of 200 game postmortems (1997-2019) found 927 problems in 20 types; most main root causes were about people, not technology ([Politowski et al. 2021, arXiv](https://arxiv.org/abs/2009.02440), A). A secondary summary says the most common problems were scope, feature creep and cutting features (uncertain - snippet only, same paper). The plan should therefore defend scope more than it defends technology.

**Vertical slice.** A vertical slice is a small, fully playable part built to final quality so others can judge the finished game; it is usually a pre-production milestone, and it can itself cause scope creep ([Game Developer essay, C](https://www.gamedeveloper.com/design/why-we-should-stop-saying-vertical-slices-); [bugnet, C](https://bugnet.io/blog/what-is-a-vertical-slice)).

### 1.2 Recommended scope by horizon

Planning assumption (not sourced): one developer, about 20 focused hours per week, plus occasional volunteer SME time. Double the speed for a full-time solo developer; do not assume linear gains for a team of 2-3.

| Horizon | Goal | In scope | Out of scope | Exit criteria (measurable) |
|---|---|---|---|---|
| **0-3 months** | Physiology-first vertical slice | One OR scene with chest already open; one phase: initiate CPB, cross-clamp, antegrade cardioplegia, electrical arrest; live monitor (ECG, arterial line, CVP, SpO2, pump flow, line pressure); 6-10 player verbs; 1 complication (e.g., high arterial line pressure); end-of-case checklist score (10-15 items). Placeholder CC0 art. Medical-fact register v1. CI + tests running. | Sternotomy, grafting, closure, full team AI, VR, voice. | All physiology outputs inside the expert ranges in section 4.4 for 3 patient sizes (50-70, 71-90, 91-110 kg) ([Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)); replay of a recorded session reproduces the same end state hash; one SME walkthrough done. |
| **3-6 months** | One complete operation (abstracted) | On-pump CABG x1 graft **or** AVR: sternotomy (abstracted), cannulation, CPB, cross-clamp, main surgical task, de-airing, weaning, decannulation, closure (abstracted). 3 complications. Tutorial. Debrief screen. | Second procedure; photoreal tissue cutting. | Expert content review round 1 (3-5 SMEs) with every step either "accurate" or "acceptable simplification"; zero open "dangerous inaccuracy" items in the register. |
| **6-12 months** | Content breadth + validation | 2 procedures (CABG + AVR) matching the curriculum modules; 6 complications drawn from a prioritised crisis list; anesthesia and perfusion roles as AI or playable; save/replay; settings for gore level; public demo build. Modified Delphi rounds 1-2. | Pediatric, transplant, aortic dissection. | Delphi consensus (a-priori 75%) on step lists and scoring checklists ([Diamond 2014, snippet](https://doi.org/10.1016/j.jclinepi.2013.12.002)); demo playable start-to-finish in < 45 min (design target). |
| **12-24 months** | 1.0 release quality | 3-4 procedures (add e.g. mitral valve repair); polish, accessibility, localisation; optional small validation study (expert vs novice) and write-up following simulation reporting guidelines. | Certification, accredited CME. | Face/content questionnaire with ~20+ participants, as in the 23-person VR perfusion study ([Babar 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/)); report items per [Cheng et al. 2016](https://dx.doi.org/10.1186/s41077-016-0025-y). |

**Cut-line rule.** If a milestone slips by more than 25% (planning heuristic, not sourced), drop the next-lowest-priority content item rather than extending the date. The postmortem data above says scope is the usual killer ([Politowski 2021](https://arxiv.org/abs/2009.02440)).

---

## 2. Version control and storage

### 2.1 Options compared (checked 2026-11-03)

| Service | Free tier (exact) | Paid starts at | Large-binary handling | Fit for this project | Source (grade) |
|---|---|---|---|---|---|
| **GitHub + Git LFS** | 10 GiB LFS storage + 10 GiB LFS bandwidth per month (Free, Pro, Free orgs); Team 250 GiB each. Max LFS file 2 GB (Free/Pro), 4 GB (Team), 5 GB (Enterprise Cloud). | Metered overage; use GitHub pricing calculator | Without payment method: storage full = pointer files only, no pushes; bandwidth full = LFS disabled until next month. GitHub Actions LFS downloads count against owner bandwidth. | Good for code + small/medium art. 10 GiB fills quickly with 4K textures and scans. | [LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs) (A); [About LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) (A) |
| **GitLab.com Free** | 10 GiB per project for repository + LFS; project goes read-only above it | Extra storage packs | LFS | Similar to GitHub. | [GitLab docs](https://docs.gitlab.com/user/storage_usage_quotas) (uncertain - snippet only) |
| **Azure DevOps** | First 5 users free (Basic); unlimited private Git repos | $6/user/month after 5 users | LFS storage "free unlimited" per third-party pages only | Possibly best free Git+LFS capacity; verify. | [Azure DevOps pricing](https://azure.microsoft.com/en-us/pricing/details/devops/) (uncertain - snippet only); LFS claim UNVERIFIED |
| **Perforce P4 (Helix Core)** | Free for up to 5 users and 20 workspaces; cloud or on-prem; no stated time limit | Contact sales | Native, file locking, built for big binaries | Industry standard for Unreal; you host it (PC/NAS) and back it up. Above limits the server reportedly caps at 1,000 files. | [Perforce free page](https://www.perforce.com/products/helix-core/free-version-control) (A); [Swarm license doc](https://www.perforce.com/perforce/doc.current/manuals/swarm/admin.license.html) (uncertain - snippet only) |
| **Unity Version Control (ex-Plastic SCM)** | Since 1 Mar 2026: no per-seat charge (cloud); 25 GB storage per org per month; 100 GB egress per month free (egress billing started May 2026) | Storage $0.14/GB-month; egress $0.10/GB | Native, file locking | Best free capacity if the engine is Unity. Storage meter is shared with Unity Build Automation artifacts. | [Unity support](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges) (A) |
| **Diversion** | Indie: free for first 5 users (up to 20 total), 100 GB storage, up to 5 repositories; eligibility rules apply | Pro $25/user/month; extra 100 GB = $10/month | Native | Cloud-hosted, engine-agnostic; good for Unreal without self-hosting. | [Diversion pricing](https://www.diversion.dev/pricing) (A) |
| **Anchorpoint** (Git client, not a host) | Personal: free, single user, **non-commercial only**, GitHub only | Team €20/user/month (annual) | Uses Git LFS; file locking only on Team plan | Nice artist UI on top of GitHub; fits a non-commercial solo project. | [Anchorpoint pricing](https://www.anchorpoint.app/pricing) (A) |

### 2.2 Recommendation

1. **If Unity:** UVCS free tier (25 GB) for the whole project, or GitHub for code + UVCS for art. ([Unity support](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges))
2. **If Unreal:** Perforce P4 free on a home server, or Diversion Indie (100 GB). ([Perforce](https://www.perforce.com/products/helix-core/free-version-control); [Diversion](https://www.diversion.dev/pricing))
3. **If Git + LFS anyway:** track only shipping assets in LFS; keep raw photogrammetry photos, high-poly sculpts and CT volumes in a separate backed-up archive (they can be hundreds of GB). Cache LFS objects in CI, because every CI checkout of LFS files burns the monthly 10 GiB bandwidth ([GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)).
4. Keep a second, off-site backup of the repository regardless of host (standard practice; no source checked).

---

## 3. Project management

| Tool | Free plan (exact) | Paid | Notes | Source |
|---|---|---|---|---|
| HacknPlan (game-dev specific) | Personal: unlimited projects, unlimited users per project, 500 MB storage, 5 MB per file, 1 board filter | Personal Plus €5.8/month; Studio €7.5/seat/month (yearly billing) | Has "game design model" (design elements linked to tasks), good for linking medical facts to features. | [HacknPlan pricing](https://hacknplan.com/pricing) (A) |
| GitHub Issues + Projects | Included with GitHub (limits not checked) | - | Keeps tasks, code and medical-fact register in one place. | UNVERIFIED (not fetched) |

**Recommendation.** Use GitHub Issues/Projects (or HacknPlan) with three labels that map to the risk register: `medical-fact`, `license`, `scope-cut`. Store the medical-fact register (section 6.6) and the asset-license register (section 7.6) as CSV/YAML **inside the repo**, so CI can check them.

---

## 4. CI builds and automated testing

### 4.1 GitHub Actions costs (2026)

- Free plan includes **$12 of compute per month**, 500 MB artifact storage and 10 GB cache per repository; Pro and Team include $18 ([GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), A).
- Per-minute rates: Linux 2-core x64 $0.006, Windows 2-core $0.010, macOS 3/4-core $0.062 ([same page](https://docs.github.com/en/billing/concepts/product-billing/github-actions)). Derived: $12 ≈ 2,000 Linux minutes, ≈ 1,200 Windows minutes, or ≈ 190 macOS minutes per month (calculation from the rates above).
- Standard runners in **public** repositories and **self-hosted** runners are free ([same page](https://docs.github.com/en/billing/concepts/product-billing/github-actions)).
- Hosted runner prices were cut by up to 39% on 1 Jan 2026; the planned $0.002/min platform charge for self-hosted runners (originally 1 Mar 2026) was **postponed** with no new date ([GitHub 2026 pricing changes](https://github.com/resources/insights/2026-pricing-changes-for-github-actions), A).

### 4.2 Unity CI with GameCI

- Current actions: `game-ci/unity-builder@v4` and `game-ci/unity-test-runner@v4` ([builder docs](https://game.ci/docs/github/builder); [test-runner docs](https://game.ci/docs/github/test-runner), A).
- Test modes: `EditMode`, `PlayMode`, `Standalone`, `All` (= EditMode + PlayMode); results go to an `artifacts` folder; code coverage is on by default ([test-runner docs](https://game.ci/docs/github/test-runner)).
- Personal license: activate in Unity Hub, copy `Unity_lic.ulf`, add secrets `UNITY_LICENSE`, `UNITY_EMAIL`, `UNITY_PASSWORD` ([activation docs](https://game.ci/docs/github/activation), A). Older forum reports say Unity stopped manual Personal activation; the current GameCI page uses the Hub-generated `.ulf` route ([Unity forum, C](https://discussions.unity.com/t/unity-no-longer-supports-manual-activation-of-personal-licenses/926760)).
- Caching the `Library` folder "could speed up your build by more than 50%" ([builder docs](https://game.ci/docs/github/builder)).
- Alternative: Unity Build Automation free tier = 2 concurrent builds, 200 Windows / 100 Mac / 100 Linux build minutes per month; storage shared with UVCS ([Unity support](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges), A).
- Unity Test Framework is a core package locked to the editor version; Unity 6.2 docs link to `com.unity.test-framework@1.6` (uncertain) ([Unity manual 6000.2](https://docs.unity3d.com/6000.2/Documentation/Manual/com.unity.test-framework.html), A).

### 4.3 Unreal CI

- Official dev and runtime container images exist since UE 4.27 on GitHub Container Registry; access needs a GitHub account linked to an Epic account and a personal access token ([Epic container overview](https://dev.epicgames.com/documentation/unreal-engine/overview-of-containers-in-unreal-engine); [quick start](https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-guide-for-using-container-images-in-unreal-engine), uncertain - snippet only). Dev images fall under the Unreal EULA; third-party guides say never push them to a public registry (C).
- Practical choice for a solo dev: a **self-hosted GitHub runner on the dev PC** (free per [GitHub billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)), because Unreal builds are large and slow on hosted runners.
- Test tools: Automation Test Framework with Automation Spec (BDD style), Functional Testing (level/Blueprint tests), Screenshot Comparison, and Gauntlet for multi-process sessions ([Epic ATF docs](https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine), A). Screenshot tests fail when the new image does not match the approved "ground truth" image ([Epic screenshot tool](https://dev.epicgames.com/documentation/unreal-engine/screenshot-comparison-tool-in-unreal-engine), A).

### 4.4 Test pyramid for a surgery simulator

| Layer | What it checks | Tooling | Pass rule | Evidence |
|---|---|---|---|---|
| 1. Physiology unit tests (engine-free) | Each model function: e.g., pump flow -> MAP for given SVR; cardioplegia flow -> line pressure | Plain C#/C++ test runner (NUnit/GoogleTest) or EditMode tests | Exact or ±1% vs hand-calculated value | Design choice |
| 2. **Physiology regression vs reference** | Whole scenario outputs over time vs stored baseline and vs expert ranges | Headless scenario runner, CSV output, comparison script | Within ±10% of target for set values; "fair" up to 30% error for emergent values; hard fail if outside expert clinical ranges | Pulse keeps scenario results as a baseline for code changes ([Pulse scenario page, snippet](https://pulse.kitware.com/_scenario_file.html)); ±10% tolerance used in Pulse ventilator validation ([Pulse, snippet](https://pulse.kitware.com/md__mechanical_ventilator.html)); "Fair" if error ≤ 30% ([Pulse FairPercentError](https://pulse.kitware.com/group___validation_target_data___fair_percent_error.html), A) |
| 3. Deterministic replay | Recorded inputs + seed + version reproduce the same final state | Input recorder, fixed timestep, state hash | Identical hash on the same build and machine; tolerance-based compare across machines | Floating point is deterministic only "if..." same compiler/instruction set and strict modes; debug vs release can differ ([Gaffer on Games](https://gafferongames.com/post/floating_point_determinism/), B). Unity Physics describes itself as "completely deterministic" ([Unity Physics design](https://docs.unity3d.com/Packages/com.unity.physics@1.3/manual/design.html), A) |
| 4. Scenario "bot surgeon" tests | A scripted player completes the slice; patient survives; checklist score = expected | PlayMode tests / Unreal Functional Tests | Pass/fail + score | [GameCI test runner](https://game.ci/docs/github/test-runner); [Epic ATF](https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine) |
| 5. Visual tests | Monitor layout, waveforms, warning colours | Screenshot comparison | Image diff within threshold | [Epic screenshot tool](https://dev.epicgames.com/documentation/unreal-engine/screenshot-comparison-tool-in-unreal-engine) |
| 6. Data-integrity tests | Every game parameter has a medical-fact ID; every asset has a license row | Script in CI | Fail build on missing IDs | Design choice (section 6.6, 7.6) |

**Example reference ranges for layer 2** (expert survey of 335 perfusionists, used to validate the Orpheus CPB simulator; values are mean ± SD of reported limits) ([Searles et al. 2021, J Extra Corpor Technol 53:263-9](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf), A):

| Parameter | Phase | Low limit | High limit |
|---|---|---|---|
| Arterial pressure (sys/dia, mmHg) | Pre-CPB | 84±12 / 48±10 | 137±21 / 83±13 |
| MAP (mmHg) | During CPB | 54±7 | 82±9 |
| Arterial pressure (sys/dia, mmHg) | Post-CPB | 83±13 / 49±10 | 121±15 / 78±12 |
| CVP (mmHg) | Pre / during / post CPB | 11±4 / 2±2 (uncertain - PDF text extraction) / 12±4 (normal values) | - |
| Arterial line pressure (mmHg) | CPB | 125±44 | 235±77 (median 250) |
| Arterial pump flow index (L/min/m²) | CPB | 2.34±0.35 (target) | - |
| Antegrade cardioplegia flow (mL/min) | Delivery | 214±71 | 359±98 |
| Retrograde cardioplegia flow (mL/min) | Delivery | 123±49 | 236±79 |
| Coronary sinus pressure (mmHg) | Retrograde delivery | 30±21 | 51±31 |

The same paper found valid simulator outputs for patients **50-110 kg**, full-CPB pump flows **3.5-5.5 L/min**, and cardioplegia flows **250-400 mL/min antegrade** and **100-225 mL/min retrograde** ([Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)). Use these as the first regression envelope; the physiology research file should supply the full parameter set.

**Determinism rules for replays** (from [Gaffer on Games](https://gafferongames.com/post/floating_point_determinism/), B): run physiology and gameplay on a fixed timestep; record inputs per tick, RNG seed, build ID and settings; avoid solvers whose iteration count depends on CPU speed; wrap transcendental functions; compare replays on the same build. Treat cross-machine replays as "tolerance" comparisons, not bit-exact.

---

## 5. Free, procedural, photogrammetry and AI-assisted asset tools

### 5.1 Tools and their exact terms

| Tool | Version / date | License | Personal / NC use | Attribution / SA / ND | Who owns the output | Notes | Source (grade) |
|---|---|---|---|---|---|---|---|
| **Blender** | Current version not checked (UNVERIFIED) | GNU GPL v2 or later (source); binaries GPLv3-compatible | Yes | GPL applies to the program, not your art | "What you create with Blender is your sole property", including commercial use | Core DCC, Geometry Nodes for procedural tissue, sculpting | [blender.org license](https://www.blender.org/about/license/) (A) |
| **Meshroom / AliceVision** | 2025.1.0 (18 Aug 2025) | MPL-2.0 | Yes | File-level copyleft for modified source only | Yours (tool output; no claim stated) | Depth maps need NVIDIA CUDA; 2025.1 binaries built with CUDA 12, compute capability ≥ 5.0; CPU "Draft Meshing" fallback; 8 GB RAM min, 32 GB recommended | [Releases](https://github.com/alicevision/Meshroom/releases) (A); [CUDA FAQ](https://meshroom-manual.readthedocs.io/en/latest/faq/needs-cuda/needs-cuda.html) (uncertain - snippet only); [licenses](https://meshroom-manual.readthedocs.io/en/latest/about/licenses/licenses.html) (snippet) |
| **COLMAP** | 3.12.0 (30 Jun 2025, secondary); 3.13.0 listed on conda-forge (uncertain) | New BSD (BSD-3-Clause); dependencies separately licensed | Yes | Keep copyright notice if redistributing the tool | Yours | Structure-from-motion; pair with an open MVS/mesher | [GitHub](https://github.com/colmap/colmap) (A); [conda-forge](https://anaconda.org/conda-forge/colmap) (snippet) |
| **RealityScan 2.0** (formerly RealityCapture) | Released 17 Jun 2025 | RealityScan EULA | Free for students, educators, and individuals/companies with < US$1M revenue in past 12 months; else $1,250/seat/year | Sample datasets non-commercial only | EULA s.6: use "does not grant to Licensor any right, title, or interest in any of the content that you produce" | Requires Epic Games Launcher / Dev Portal; high quality, fast | [License](https://www.realityscan.com/license) (A); [EULA](https://www.realityscan.com/eula) (A); [2.0 news](https://www.realityscan.com/news/realityscan-20-new-release-brings-powerful-new-features-to-a-rebranded-realitycapture) (A) |
| **TRELLIS.2** (Microsoft, image-to-3D) | 4B params; arXiv 2512.14692 (late 2025) | Code and model: MIT | Yes (MIT) **but** see nvdiffrast | MIT notice | Not stated (MIT gives no output claim) | Needs NVIDIA GPU with ≥ 24 GB; outputs GLB with PBR | [GitHub](https://github.com/microsoft/TRELLIS.2) (A) |
| **nvdiffrast** (TRELLIS dependency) | - | NVIDIA Source Code License (1-Way Commercial) | Only "for research or evaluation purposes only and not for any direct or indirect monetary gain" | - | - | A hobby game is arguably neither "research" nor "evaluation" (uncertain); avoid in the shipping pipeline | [LICENSE.txt](https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt) (A) |
| **Hunyuan3D 2.1** (Tencent) | License dated 13 Jun 2025 | Tencent Hunyuan 3D 2.1 Community License | Territory = worldwide **excluding EU, UK and South Korea**; use outside territory "is unlicensed and unauthorized"; >1M MAU needs separate license | Notice requirements | "Tencent claims no rights in Outputs You generate" | Do not use if you live or publish in EU/UK/KR | [HF LICENSE](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE) (A) |
| **Stable Fast 3D** (Stability AI) | Version not checked | Stability AI Community License | Research, non-commercial and commercial use for < US$1M annual revenue | Attribution terms not on summary page (UNVERIFIED) | "you own outputs" (as between you and Stability) | Fast single-image to mesh | [stability.ai/license](https://stability.ai/license) (A) |
| **Meshy** (cloud) | Plan names change | Meshy Terms | Free plan usable | Free plan outputs: you get a **CC BY 4.0 license**, credit Meshy | Paid plans: "full private ownership" if not posted to community | Cloud upload of your prompts/images | [Meshy help](https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models) (A) |
| **Tripo** (cloud) | - | Tripo Terms | Free "Basic" models are public under CC BY 4.0 | Sources conflict on whether free outputs may be used commercially | Paid plans: private models | Treat as UNVERIFIED | [Tripo blog](https://www.tripo3d.ai/blog/commercial-use-ai-3d-models) (uncertain - snippet only) |

### 5.2 Ready-made asset libraries

| Library | License | Attribution | Commercial OK | Notes | Source |
|---|---|---|---|---|---|
| Poly Haven (HDRIs, textures, models) | CC0 | Not required | Yes | Website content (logos, renders) is not CC0 | [polyhaven.com/license](https://polyhaven.com/license) (A) |
| ambientCG (materials, HDRIs) | CC0 1.0 Universal | Not required | Yes ("even for commercial purposes") | Can include raw files in a video game | [docs.ambientcg.com/license](https://docs.ambientcg.com/license/) (A) |
| Z-Anatomy (Blender atlas) | CC BY-SA 4.0; models derived from BodyParts3D (CC BY-SA 2.1 Japan); some parts CC BY-NC 4.0 / CC BY-NC-SA 4.0 | Required strings: "BodyParts3D - The Database Center for Life Science - CC-BY-SA 2.1 Japan" and "Z-Anatomy - The libre 3D atlas of anatomy - CC-BY-SA 4.0" | Mostly yes, but SA forces derivatives under same license; NC parts block sales | Good anatomy reference/base mesh; isolate it in its own folder with license file | [Z-Anatomy GitHub](https://github.com/Z-Anatomy/Models-of-human-anatomy) (A) |
| Sketchfab downloads | Per model: Standard license or CC (BY, BY-SA, BY-NC, BY-ND...) | Depends | CC BY-NC: no; Store "Editorial": no | Check each model page | [Sketchfab licenses](https://sketchfab.com/licenses) (uncertain - snippet only) |
| Fab (Epic) | CC-BY (free) or Standard License (free/paid); Personal tier for buyers with ≤ US$100k revenue in last 12 months | Depends | Yes under Standard | Legacy UE Marketplace license being phased out | [Fab licenses doc](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab) (uncertain - snippet only) |
| 3D Slicer (segment CT to mesh) | BSD-style Slicer license; "no use restrictions"; not FDA approved | Keep notice | Yes | Extensions have own licenses | [slicer.org/commercial-use](https://slicer.org/commercial-use.html) (uncertain - snippet only) |
| TotalSegmentator (auto-segmentation) | Apache-2.0 core; **`heartchambers_highres` is free only for non-commercial use** (license from author otherwise) | Cite paper | Core yes; heart high-res subtask no | Useful for building heart meshes from public CT | [GitHub](https://github.com/wasserth/TotalSegmentator) (uncertain - snippet only) |
| TCIA imaging collections | Mostly CC BY 3.0 / CC BY 4.0; a few CC BY-NC; head/neck collections moved to a limited-access license (Jan 2022) | Cite each collection + TCIA paper | Mostly yes | Users must agree not to re-identify participants | [TCIA policy](https://wiki.cancerimagingarchive.net/x/c4hF) (uncertain - snippet only) |

### 5.3 AI output ownership and disclosure

- **Copyright.** The US Copyright Office published Part 2 "Copyrightability" on 29 Jan 2025 ([copyright.gov/ai](https://www.copyright.gov/ai/), A). Secondary summaries quote it as: "prompts alone do not provide sufficient human control to make users of an AI system the authors of the output"; human-authored material and creative modifications can still be protected (uncertain - snippet only, e.g. [Dykema summary](https://dykema.com/news-insights/the-future-of-creativity-us-copyright-office-clarifies-copyrightability-of-ai-generated-works.html)). Consequence: raw AI meshes may be unprotectable by you; retopologise, re-texture and edit them by hand if ownership matters.
- **Steam disclosure.** The Steam Content Survey asks about **Pre-Generated** AI content ("ships with your game and is consumed by players") and **Live-Generated** content (needs described guardrails) ([Steam content survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey), A). A January 2026 update says efficiency tools used behind the scenes (e.g., code assistants) do not need disclosure; player-facing AI content still does ([PC Gamer](https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/), uncertain - snippet only).
- **Medical accuracy.** AI-generated organ meshes have no anatomical guarantee. Use them only for non-anatomical props (trays, drapes, monitors). Hero anatomy (heart, great vessels, pericardium) should come from segmented public CT, Z-Anatomy reference, or hand sculpting reviewed by an SME.

### 5.4 Photogrammetry of tissue

- Wet-lab cardiac simulators use explanted **porcine hearts** as a model for the human heart ([Ramphal et al. 2005, Eur J Cardiothorac Surg](https://nottingham-repository.worktribe.com/output/1282729), uncertain - snippet only). A butcher-shop pig heart is a legal, ethical photogrammetry subject for **texture and surface detail** (fat, epicardium, coronary course). Note species differences in shape; keep human proportions from human data.
- Capture guidance (planning heuristic, not sourced): cross-polarised light to remove speculars, 100-200 overlapping photos, turntable, colour checker; process in RealityScan (free under $1M revenue) or Meshroom/COLMAP (fully open source).

---

## 6. Medical validation

### 6.1 Who to consult and how to use them

| Role | What they validate | Where they plug in |
|---|---|---|
| Cardiac surgeon | Step order, instrument choice, anatomy, surgical complications, scoring checklists | Procedure graph, checklists, debrief text |
| Clinical perfusionist | CPB circuit, pump flows, pressures, cardioplegia, weaning from CPB | Physiology parameters, HLM UI, alarms |
| Cardiac anesthesiologist | Hemodynamics, drugs and doses, TEE cues, ventilation | Drug table, monitor behaviour |
| OR nurse | Room layout, counts, instrument passing, sterile field | Environment, interaction flow |

All four roles took part in a Dutch national Delphi on cardiac surgical crisis scenarios: 114 experts (26 anesthesiologists, 24 surgeons, 25 perfusionists, 39 OR nurses) from all 16 Dutch cardiac centres ([Kemper et al. 2023, via AHRQ PSNet](https://psnet.ahrq.gov/issue/crisis-scenarios-simulation-based-nontechnical-skills-training-cardiac-surgery-teams-national), uncertain - snippet only). For a hobby project, aim for **at least one of each role** for content review, and 8-15 people for a Delphi (realistic target; smaller than the optimum below, so state it as a limitation).

### 6.2 Validity frameworks: classic vs modern

**Classic (still common in surgical-simulator papers).** Face validity = how realistic the simulator looks; content validity = whether it is suitable for teaching; construct validity = whether it separates experienced from inexperienced surgeons; plus concurrent and predictive validity ([McDougall 2007, J Endourol 21:244-7](https://pubmed.ncbi.nlm.nih.gov/17444766/), uncertain - snippet only).

**Modern (recommended).** Cook & Hatala ([Adv Simul 2016, PMC5806296](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/), A):
- **Messick's five evidence sources:** content, response process, internal structure, relationships with other variables, consequences.
- **Kane's four inferences:** scoring, generalization, extrapolation, implications/decisions.
- They **discourage the term "face validity"** ("superficial appearances that have little merit"), warn against making expert-novice comparisons "the crux of the validity argument", and stress that "Validation is a process, not an endpoint."
- Eight steps: define the construct and interpretation; state the intended decision; define the interpretation-use argument and prioritise evidence; find/adapt instruments; appraise and collect evidence; track practical issues/cost; synthesise the validity argument; judge whether evidence supports the use.

**What this means for a game.** The "construct" is not "surgical skill". It is a narrower claim, e.g., "the player can execute the correct sequence for initiating and weaning CPB and recognise 3 complications". Validate that claim, not general skill.

### 6.3 Delphi panels

| Item | Evidence | Source |
|---|---|---|
| Consensus threshold | Review of 100 Delphi studies: percent agreement most common; **median threshold 75%**; only 42 of 86 studies claiming consensus set the threshold a priori | [Diamond et al. 2014, J Clin Epidemiol](https://doi.org/10.1016/j.jclinepi.2013.12.002) (uncertain - snippet only) |
| Core elements | Anonymity, iteration, controlled feedback, statistical stability of consensus; panel of ~30-50 is considered optimum in concluding rounds of a homogeneous Delphi | [Nasa et al. 2021, World J Methodol](https://pmc.ncbi.nlm.nih.gov/articles/PMC8299905/) (A) |
| Cardiac surgery example 1 | Off-pump CABG: 10 operations videotaped and deconstructed into 6 simulation modules; checklists validated by **11 cardiac surgeons**; consensus = **70% of experts rating ≥ 3.5 on a 5-point scale**; 2 rounds; final checklists 12-23 items | [Cristancho et al. 2012, Surgery 151:785-95](https://doi.org/10.1016/j.surg.2012.03.015) (uncertain - snippet only) |
| Cardiac surgery example 2 | 237 crisis scenarios (round 1) -> 44 scored (round 2) -> **13** with expert consensus > 67% | [Kemper et al. 2023](https://psnet.ahrq.gov/issue/crisis-scenarios-simulation-based-nontechnical-skills-training-cardiac-surgery-teams-national) (uncertain - snippet only) |

**Recommended protocol (modified Delphi, remote, free tools):**
1. Round 0: you draft step lists, decision points, complications and scoring items from textbooks/guidelines, each with a source (medical-fact register).
2. Round 1: experts rate each item 1-5 for "accurate" and "important"; free-text comments.
3. Round 2: show anonymised group median and IQR; experts re-rate.
4. Consensus a priori: ≥ 75% rate ≥ 4 ([Diamond 2014](https://doi.org/10.1016/j.jclinepi.2013.12.002)); items with 50-74% go to round 3; < 50% dropped or marked "simplified".
5. Publish the rule and results in the game's credits/documentation.

### 6.4 Objective validation of the physiology model

- The Orpheus CPB simulator study used Sargent's verification and validation methods: **historical data validation, parameter variability, and face validity**, in two steps: (1) build a benchmark of clinical norms from an expert survey; (2) sweep every user-modifiable variable across its full range and plot outputs against the benchmark; agreement of simulator measurements with clinical monitors was checked with linear regression and **Bland-Altman** plots ([Searles et al. 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf), A). This is directly reusable as an automated test (section 4.4).
- Sargent's paper defines conceptual model validity, verification, operational validity and data validity ([Sargent 2013, J Simulation 7:12-24](https://econpapers.repec.org/RePEc:taf:tjsmxx:v:7:y:2013:i:1:p:12-24), uncertain - snippet only).
- Pulse (open physiology engine, Apache 2.0) validates "using a combination of peer-reviewed publications and subject matter expertise" to establish "an appropriate domain of validity" ([Pulse FAQ](https://pulse.kitware.com/_f_a_q.html), A).
- For a stricter template, FDA's final guidance "Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions" (Nov 2023, docket FDA-2021-D-0980) gives a risk-informed credibility framework based on ASME V&V 40-2018 ([FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions), A). It is **not required** for a game; use its idea of "context of use" to scope claims.

### 6.5 If you ever run a user validation study

- Published model: VR perfusion simulator, **23 participants (12 expert perfusionists, 11 trainees)**, 5-point Likert, USE questionnaire + immersiveness (25 items); 96% (n = 22) agreed it was useful (body text gives slightly different counts); limitations: alpha build, users could not make mistakes, authors were co-developers ([Babar 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/), A).
- Another cardiac example: VR simulator for CPR and emergency resternotomy after cardiac surgery, face and content validity with experts and novices ([Sadeghi et al. 2022, JMIR Serious Games](https://games.jmir.org/2022/1/e30456), uncertain - snippet only).
- Report using the simulation extensions to CONSORT and STROBE (11 CONSORT + 10 STROBE extensions) ([Cheng et al. 2016](https://dx.doi.org/10.1186/s41077-016-0025-y), B - snippet/summary).
- A study with human participants usually needs ethics review or a formal waiver from an institution (uncertain; depends on country and venue).

### 6.6 Medical-fact register (design)

One row per fact. Stored as CSV/YAML in the repo; CI fails if a game parameter has no fact ID.

| Field | Example |
|---|---|
| `fact_id` | `CPB-FLOW-001` |
| `statement` | Target arterial pump flow index on full CPB |
| `value` / `range` / `units` | 2.34 ± 0.35 L/min/m² |
| `phase` | On CPB, normothermic adult |
| `source_url` / `doi` | https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf |
| `grade` | A |
| `game_param_key` | `perfusion.flowIndexTarget` |
| `test_id` | `REG-CPB-03` |
| `simplification` | None / describe |
| `reviewer`, `role`, `date_verified` | (name), perfusionist, 2027-01-15 |
| `status` | draft / SME-approved / Delphi-consensus / disputed |
| `disagreement_note` | Range and both sources when sources disagree |

---

## 7. Legal and ethical

### 7.1 Not a medical device

| Jurisdiction | Rule | What keeps the game outside it | Source |
|---|---|---|---|
| USA (FDA) | FDA lists software that is **not** a medical device, including "Software functions that are intended for health care professionals to use as educational tools for medical training", e.g. "Surgical training videos", "Interactive anatomy diagrams or videos", and "Games that simulate various cardiac arrest scenarios to train health professionals in advanced cardiopulmonary resuscitation" (page current as of 09/29/2022) | Generic training/entertainment, no patient-specific use | [FDA examples page](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices) (A) |
| EU (MDR) | A medical device is software etc. intended "for human beings" for diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease, etc. MDCG 2019-11 decision step 4 asks "is the action for the benefit of individual patients?"; "medical atlases, models and templates" are given as examples that are not | No individual-patient purpose; no planning from a real patient's scan | [MDCG 2019-11 (Oct 2019)](https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native) (A); current revision rev.1, June 2025 ([EC MDCG list](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en), A) |

**Red lines (stay a game):** no import of a real patient's CT to "rehearse that patient's surgery"; no dose calculators presented as clinical tools; no claims like "certified training" or "reduces complications". FDA guidance is nonbinding and intended use is judged from labels and promotion, so wording in the store page matters ([FDA policy page](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/policy-device-software-functions-and-mobile-medical-applications), A; [MDCG 2019-11](https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native), A).

**Suggested disclaimer (splash + store page + credits):** "This is a game and educational simulation. It is not a medical device, not clinical guidance, and not a substitute for supervised training. Values and procedures are simplified. Do not use it to make decisions about real patients."

### 7.2 Age ratings and gore

| System | Relevant definitions | Comparable title | Source |
|---|---|---|---|
| ESRB | T: "minimal blood"; M: "intense violence, blood and gore"; descriptor "Blood and Gore" = "Depictions of blood or the mutilation of body parts" | Surgeon Simulator: **T** (Violence, Blood); Surgeon Simulator 2: **M** (Intense Violence, Blood and Gore) | [ESRB guide](https://www.esrb.org/ratings-guide/) (A); [ESRB Surgeon Simulator](https://www.esrb.org/ratings/10010871/surgeon-simulator/) (A); [Common Sense Media](https://www.commonsensemedia.org/game-reviews/surgeon-simulator-2-access-all-areas) (uncertain - snippet only) |
| PEGI | PEGI 16: depiction "reaches a stage that looks the same as would be expected in real life"; PEGI 18: "gross violence"; Horror descriptor for "disturbing images" at PEGI 12/16. The page says nothing about medical procedures | Realistic open-chest imagery is not violence, but disturbing realistic images may push to 12-16 (uncertain) | [PEGI labels](https://www.pegi.info/what-do-the-labels-mean) (A) |
| IARC | One free questionnaire, instant ratings, accessed only through participating storefront portals (Google Play, Microsoft Store, Nintendo eShop, Oculus/Meta listed in 2017) | Needed only for those stores | [IARC press release 2017](https://www.globalratings.com/news/grac-iarc-pressrelease-171219.pdf) (uncertain - snippet only) |

Design response: a **"clinical detail" setting** (blood volume/visibility, tissue colour saturation, sound) so the default can target T/PEGI 12-16 while "full realism" is opt-in. Whether Steam requires an external rating certificate was not verified (UNVERIFIED).

### 7.3 Steam rules

- "What you shouldn't publish on Steam" includes: "Content that is patently offensive or intended to shock or disgust viewers"; "Content you don't own or have adequate rights to"; "Adult content that isn't appropriately labeled and age-gated" ([Steamworks onboarding](https://partner.steamgames.com/doc/gettingstarted/onboarding), A). A sober, clinical presentation and an honest content survey reduce the "shock or disgust" risk.
- Mature content must be disclosed in the Content Survey; it controls how the game appears relative to customer preferences ([Steam content survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey), A).

### 7.4 Patient data: HIPAA, GDPR, DICOM

- **HIPAA de-identification** (45 CFR 164.514(b)): either Expert Determination (risk "very small", documented) or Safe Harbor (remove 18 identifiers incl. names, geography smaller than a state, all dates except year, ages over 89, device serial numbers, **"Full face photographic images and any comparable images"**, any other unique code) and have no actual knowledge of re-identification ([45 CFR 164.514 via Cornell LII](https://www.law.cornell.edu/cfr/text/45/164.514), A). HIPAA binds covered entities and their associates; a solo developer is usually not one, but any data source you receive from a hospital is.
- **GDPR** (if you or data subjects are in the EU/EEA): Recital 26 says data protection "should therefore not apply to anonymous information"; identifiability is judged on "all the means reasonably likely to be used", cost, time and technology ([GDPR Recital 26](https://gdpr-info.eu/recitals/no-26/), A). Pseudonymised health data remains personal data and special-category data (secondary summary, [noze.it](https://www.noze.it/en/insights/gdpr-health-data-article-9/), C).
- **Imaging-specific.** DICOM PS3.15 "Clean Recognizable Visual Features" option notes that a 3D volume or surface rendering of high-resolution head and neck cross-sections may allow identification ([DICOM PS3.15 E.3.2](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.2.html), uncertain - snippet only). TCIA users agree not to generate facial images or comparable representations that could identify participants ([TCIA policy](https://wiki.cancerimagingarchive.net/x/c4hF), uncertain - snippet only). Chest CT for heart meshes is low risk for faces, but strip all DICOM headers and keep only the mesh.
- **Rule for the plan:** use only public datasets with explicit licenses; never accept scans from friends at hospitals; ship meshes, never source DICOM.

### 7.5 Trademarks of real device brands

- **Nominative fair use** (US, 9th Cir.): allowed only if (1) the product is not readily identifiable without the mark, (2) only as much of the mark as needed is used, (3) nothing suggests sponsorship ([New Kids on the Block v. News America, 971 F.2d 302 (1992)](https://caselaw.findlaw.com/us-9th-circuit/1233126.html), uncertain - snippet only).
- **Games and realism:** in AM General v. Activision (S.D.N.Y., 31 Mar 2020) Humvees in Call of Duty were protected under the Rogers test because they added realism ([Finnegan summary](https://www.finnegan.com/en/insights/blogs/incontestable/in-legal-warfare-over-humvee-trademarks-the-first-amendment-goes-beyond-the-call-of-duty-in-dismissing-am-generals-claims.html), B - snippet). In 2023 the US Supreme Court held Rogers does not apply when a mark is used as a source identifier, and left its wider validity open ([Jack Daniel's v. VIP Products](https://en.wikipedia.org/wiki/Jack_Daniel%27s_Properties,_Inc._v._VIP_Products_LLC), C).
- **Recommendation:** fictional brands for HLM, oxygenator, cannulae, sutures, valves; generic names in UI ("roller pump", "centrifugal pump", "bioprosthetic valve"); no logos, trade dress or product photos. This costs nothing and removes the risk.

### 7.6 License hygiene for assets and code

- Keep an **asset-license register** (path, source URL, author, license, version/date, attribution text, SA/NC/ND flags, modified?).
- **SA (ShareAlike):** derivatives of Z-Anatomy must be shared under CC BY-SA if distributed ([Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy)). Keep SA assets separate so they do not "infect" your own meshes.
- **NC (NonCommercial):** fine for a free personal game, but blocks any future sale or donation-based model; flag them in the register.
- **Engines:** Unity Personal is free for "less than $200K USD of revenue and funds raised in the last 12 months"; splash screen customisable ([Unity Personal](https://unity.com/products/unity-personal), A). Unreal: 5% royalty above US$1M lifetime gross per product ([Unreal license page](https://www.unrealengine.com/en-US/license), uncertain - snippet only). Godot: MIT (uncertain - snippet only). A non-commercial free release stays far below all thresholds.

---

## 8. Risk register

Likelihood (L) and impact (I): H/M/L. Scores are planning judgements, not sourced.

| # | Risk | Category | L | I | Mitigation | Early warning | Evidence |
|---|---|---|---|---|---|---|---|
| R1 | Scope creep: trying to model the whole operation at photoreal quality | Scope | H | H | Phase-based roadmap (section 1.2); cut-line rule; one procedure at a time | Slice not playable end-to-end at month 3 | [Politowski 2021](https://arxiv.org/abs/2009.02440) |
| R2 | Real-time soft-tissue cutting/suturing too hard for a solo dev | Technical | H | H | Abstract cutting/suturing into guided gestures + pre-authored states; physics only where it changes decisions | > 2 weeks on one deformable feature | Design judgement |
| R3 | Physiology model drifts as code changes | Technical / medical | M | H | Baseline regression tests vs reference ranges in CI | Any regression test fails | [Pulse baseline](https://pulse.kitware.com/_scenario_file.html); [Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf) |
| R4 | Non-deterministic replays break debrief/testing | Technical | M | M | Fixed timestep, input recording, same-build replays, tolerance compare | Replay hash mismatch on same machine | [Gaffer](https://gafferongames.com/post/floating_point_determinism/) |
| R5 | Dangerous inaccuracy (wrong step order, wrong dose, wrong values) | Medical accuracy | M | H | Medical-fact register, SME review, Delphi, in-game "simplified" flags | Facts without source or reviewer | [Cook & Hatala 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/) |
| R6 | No SMEs available / SMEs disagree | Medical accuracy | M | M | Recruit across 4 roles; record both positions with ranges; Delphi with a-priori threshold | < 3 reviewers by month 6 | [Nasa 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8299905/); [Diamond 2014](https://doi.org/10.1016/j.jclinepi.2013.12.002) |
| R7 | "Validated" claim without evidence | Medical / legal | M | M | Use Messick/Kane language; never say "validated"; publish what was checked | Marketing copy says "validated" | [Cook & Hatala 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/) |
| R8 | Repo storage/bandwidth quota hits (LFS blocked) | Tooling | H | M | UVCS/P4/Diversion for binaries; LFS cache in CI; raw data outside repo | > 70% of quota used | [GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs) |
| R9 | CI cost or Unity license activation breaks | Tooling | M | L | Self-hosted runner; keep `.ulf` secret current; manual build fallback | CI red for licence errors | [GameCI activation](https://game.ci/docs/github/activation) |
| R10 | Asset under SA/NC/territory-restricted license ends up in build | Licensing | M | H | Asset-license register + CI check; avoid Hunyuan3D in EU/UK/KR; avoid nvdiffrast pipeline | Asset with empty license field | [Hunyuan3D LICENSE](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE); [nvdiffrast](https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt) |
| R11 | AI-generated assets not owned / disclosure missed | Licensing / store | M | M | Human rework of AI assets; Steam AI disclosure; keep prompt logs | AI assets in hero anatomy | [copyright.gov/ai](https://www.copyright.gov/ai/); [Steam survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey) |
| R12 | Patient data / re-identification issue | Legal / ethical | L | H | Public licensed datasets only; meshes not DICOM; no faces | Any non-public scan offered | [45 CFR 164.514](https://www.law.cornell.edu/cfr/text/45/164.514); [GDPR R26](https://gdpr-info.eu/recitals/no-26/) |
| R13 | Drift into medical-device territory | Regulatory | L | H | No patient-specific features; disclaimer; careful store copy | Feature request "load my CT" | [FDA examples](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices); [MDCG 2019-11](https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native) |
| R14 | Store rejection or high age rating due to gore | Content | M | M | Clinical tone; gore setting; honest mature-content disclosure | Store review feedback | [Steam onboarding](https://partner.steamgames.com/doc/gettingstarted/onboarding); [ESRB](https://www.esrb.org/ratings-guide/) |
| R15 | Trademark complaint from device maker | Legal | L | M | Fictional brands, no logos | Real brand names in assets | [New Kids test](https://caselaw.findlaw.com/us-9th-circuit/1233126.html) |
| R16 | Realism vs fun conflict makes the game tedious | Design | M | M | Optional time compression, skippable routine steps, difficulty modes; keep accuracy in decisions | Playtesters quit during routine steps | [Project Hospital interview](https://jgeekstudies.org/2020/03/08/project-hospital-a-realistic-take-on-hospital-simulation) |
| R17 | Tool/pricing change (quotas, licenses) mid-project | Tooling / licensing | M | M | Re-check every 6 months; exportable formats (FBX/GLB, Git/P4) | Vendor pricing email | [Unity 2026 change](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges); [GitHub 2026 change](https://github.com/resources/insights/2026-pricing-changes-for-github-actions) |
| R18 | Developer burnout / long gaps | Scope / people | M | H | Fixed weekly hours; public devlog; small milestones | Two missed milestones | [Politowski 2021](https://arxiv.org/abs/2009.02440) (people root causes) |

---

## Game hooks

How the findings become mechanics, data and rules:

1. **Expert-range alarms.** Orpheus survey limits become alarm thresholds and scoring penalties: MAP on CPB below 54±7 mmHg or above 82±9 mmHg, arterial line pressure above ~235-250 mmHg, antegrade cardioplegia flow outside 250-400 mL/min ([Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)). Difficulty modes can widen or narrow the band (e.g., Novice = mean ± 2 SD, Expert = mean ± 1 SD; design choice).
2. **Patient size presets.** Three adult presets matching the validated domain: small 50-70 kg, medium 71-90 kg, large 91-110 kg, with target pump flows 3.5 / 4.5 / 5.5 L/min ([Searles 2021, Table 3](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)).
3. **Checklist scoring.** Each module gets a 12-23 item checklist built with a Delphi rule, like the off-pump CABG program ([Cristancho 2012](https://doi.org/10.1016/j.surg.2012.03.015)). Debrief shows missed items with the source link from the medical-fact register.
4. **Complication deck.** Complications are drawn from a prioritised crisis-scenario list built with a Delphi (the Dutch panel produced 13) ([Kemper 2023](https://psnet.ahrq.gov/issue/crisis-scenarios-simulation-based-nontechnical-skills-training-cardiac-surgery-teams-national)).
5. **Campaign order.** Chapters follow the curriculum modules: CPB -> CABG -> AVR, each followed by one adverse-event chapter ([STS](https://www.sts.org/sites/default/files/press-releases/Simulation%20FINAL%2082516.pdf)).
6. **Replay and debrief.** Deterministic input replays power a "watch your case" debrief with timeline markers and parameter graphs; the same files are CI regression tests ([Gaffer](https://gafferongames.com/post/floating_point_determinism/)).
7. **Evidence badges.** Each in-game fact tooltip shows status: "SME-approved", "Delphi consensus", or "Simplified for play" (from the register). This makes accuracy visible and avoids "validated" claims ([Cook & Hatala 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/)).
8. **Clinical detail slider.** Blood/tissue realism setting supports ESRB/PEGI targeting and Steam's "shock or disgust" rule ([ESRB](https://www.esrb.org/ratings-guide/); [Steam onboarding](https://partner.steamgames.com/doc/gettingstarted/onboarding)).
9. **Fictional brand system.** All equipment uses an in-game fictional manufacturer set with consistent UI; no real logos ([New Kids test](https://caselaw.findlaw.com/us-9th-circuit/1233126.html)).
10. **Disclaimer gate.** First launch shows the not-a-medical-device disclaimer; store page uses the same text ([FDA examples](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices)).
11. **Team roles.** Surgeon, perfusionist, anesthesiologist, nurse roles map to the four expert groups; each role's actions are validated by that role's SME ([Kemper 2023](https://psnet.ahrq.gov/issue/crisis-scenarios-simulation-based-nontechnical-skills-training-cardiac-surgery-teams-national)).
12. **"Mistakes allowed" rule.** Unlike the alpha VR perfusion simulator where users could not make mistakes, the game must allow wrong actions with physiological consequences ([Babar 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/)).

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | GitHub Free/Pro include 10 GiB LFS storage and 10 GiB LFS bandwidth per month; Team 250 GiB | https://docs.github.com/en/billing/concepts/product-billing/git-lfs | A |
| 2 | Without a payment method, exceeding LFS bandwidth disables LFS until next month; Actions downloads count | https://docs.github.com/en/billing/concepts/product-billing/git-lfs | A |
| 3 | Max LFS file size: 2 GB Free/Pro, 4 GB Team, 5 GB Enterprise Cloud | https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage | A |
| 4 | GitHub Free includes $12/month Actions compute; Linux 2-core $0.006/min; public repos and self-hosted runners free | https://docs.github.com/en/billing/concepts/product-billing/github-actions | A |
| 5 | Self-hosted runner $0.002/min fee (planned 1 Mar 2026) was postponed; hosted prices cut up to 39% from 1 Jan 2026 | https://github.com/resources/insights/2026-pricing-changes-for-github-actions | A |
| 6 | Perforce P4 free for up to 5 users and 20 workspaces | https://www.perforce.com/products/helix-core/free-version-control | A |
| 7 | UVCS since 1 Mar 2026: no seat charge, 25 GB storage, 100 GB egress free; $0.14/GB-month, $0.10/GB | https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges | A |
| 8 | Diversion Indie: 5 free users, 100 GB, 5 repos | https://www.diversion.dev/pricing | A |
| 9 | Anchorpoint free plan is single-user, non-commercial, GitHub only | https://www.anchorpoint.app/pricing | A |
| 10 | GameCI current actions are v4; Personal license needs UNITY_LICENSE/EMAIL/PASSWORD secrets | https://game.ci/docs/github/builder ; https://game.ci/docs/github/activation | A |
| 11 | Meshroom 2025.1.0 released 18 Aug 2025; MPL-2.0 | https://github.com/alicevision/Meshroom/releases | A |
| 12 | RealityScan free under US$1M revenue (past 12 months); $1,250/seat/year above; Epic gets no rights in your content | https://www.realityscan.com/license ; https://www.realityscan.com/eula | A |
| 13 | Hunyuan3D 2.1 license excludes EU, UK and South Korea | https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE | A |
| 14 | TRELLIS.2 is MIT, needs ≥ 24 GB GPU; nvdiffrast is research/evaluation-only | https://github.com/microsoft/TRELLIS.2 ; https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt | A |
| 15 | Meshy free-plan outputs are CC BY 4.0 licensed to the user; paid = private ownership | https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models | A |
| 16 | Z-Anatomy is CC BY-SA 4.0 with BodyParts3D CC BY-SA 2.1 JP attribution | https://github.com/Z-Anatomy/Models-of-human-anatomy | A |
| 17 | Poly Haven and ambientCG assets are CC0, no attribution required | https://polyhaven.com/license ; https://docs.ambientcg.com/license/ | A |
| 18 | Messick's 5 evidence sources; authors discourage "face validity"; validation is a process | https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/ | A |
| 19 | Delphi consensus median threshold 75% across 100 studies | https://doi.org/10.1016/j.jclinepi.2013.12.002 | A (uncertain - snippet only) |
| 20 | Off-pump CABG checklists: 11 surgeons, 70% rating ≥ 3.5/5, 2 rounds | https://doi.org/10.1016/j.surg.2012.03.015 | A (uncertain - snippet only) |
| 21 | Orpheus CPB simulator valid for 50-110 kg, pump flows 3.5-5.5 L/min, cardioplegia 250-400 (antegrade) and 100-225 mL/min (retrograde); 335 survey respondents | https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf | A |
| 22 | VR perfusion simulator study: 23 participants (12/11), UE4, Quest 2, one scenario; 96% found it useful | https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/ | A |
| 23 | US cardiac surgery simulation curriculum: 6 modules, 39 sessions -> 29 | https://www.sts.org/sites/default/files/press-releases/Simulation%20FINAL%2082516.pdf | B |
| 24 | FDA lists training games simulating cardiac arrest scenarios as not medical devices | https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices | A |
| 25 | MDCG 2019-11 step 4: "benefit of individual patients"; atlases/models not; rev.1 June 2025 | https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native ; https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en | A |
| 26 | ESRB "Blood and Gore" = blood or mutilation of body parts; Surgeon Simulator rated T | https://www.esrb.org/ratings-guide/ ; https://www.esrb.org/ratings/10010871/surgeon-simulator/ | A |
| 27 | Steam bans content "patently offensive or intended to shock or disgust viewers" | https://partner.steamgames.com/doc/gettingstarted/onboarding | A |
| 28 | HIPAA Safe Harbor lists 18 identifiers incl. full-face photos and comparable images | https://www.law.cornell.edu/cfr/text/45/164.514 | A |
| 29 | Surgeon Simulator: 48-hour jam + 48 days to commercial release; ~2M copies by Feb 2015 | https://en.wikipedia.org/wiki/Surgeon_Simulator | B |
| 30 | Unity Personal eligibility: < US$200K revenue and funds in last 12 months | https://unity.com/products/unity-personal | A |

---

## Sources

1. GitHub Docs - Git LFS billing - https://docs.github.com/en/billing/concepts/product-billing/git-lfs - LFS quotas, over-quota behaviour, Actions bandwidth.
2. GitHub Docs - About Git Large File Storage - https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage - per-file LFS limits.
3. GitHub Docs - How use of GitHub Actions is measured - https://docs.github.com/en/billing/concepts/product-billing/github-actions - included compute, per-minute rates, free cases.
4. GitHub - 2026 pricing changes for GitHub Actions - https://github.com/resources/insights/2026-pricing-changes-for-github-actions - price cut, postponed self-hosted fee.
5. Perforce - Free version control - https://www.perforce.com/products/helix-core/free-version-control - 5 users / 20 workspaces.
6. Perforce Swarm admin license (snippet) - https://www.perforce.com/perforce/doc.current/manuals/swarm/admin.license.html - over-limit 1,000-file cap (uncertain).
7. Unity Support - Understanding Unity DevOps charges - https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges - UVCS and Build Automation free tiers, 2026 prices.
8. Diversion - Pricing - https://www.diversion.dev/pricing - Indie free tier, paid tiers.
9. Anchorpoint - Pricing - https://www.anchorpoint.app/pricing - free non-commercial plan, Team price.
10. GitLab Docs - Storage usage quotas (snippet) - https://docs.gitlab.com/user/storage_usage_quotas - 10 GiB per project (uncertain).
11. Microsoft - Azure DevOps pricing (snippet) - https://azure.microsoft.com/en-us/pricing/details/devops/ - first 5 users free.
12. HacknPlan - Pricing - https://hacknplan.com/pricing - free plan limits.
13. GameCI - Activation - https://game.ci/docs/github/activation - Unity Personal license secrets.
14. GameCI - Builder - https://game.ci/docs/github/builder - unity-builder@v4, Library caching.
15. GameCI - Test runner - https://game.ci/docs/github/test-runner - unity-test-runner@v4, modes, coverage.
16. Unity Manual 6000.2 - Test Framework package - https://docs.unity3d.com/6000.2/Documentation/Manual/com.unity.test-framework.html - core package version policy.
17. Unity Physics design - https://docs.unity3d.com/Packages/com.unity.physics@1.3/manual/design.html - deterministic, stateless design.
18. Epic - Automation Test Framework - https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine - Unreal test tools.
19. Epic - Screenshot Comparison Tool - https://dev.epicgames.com/documentation/unreal-engine/screenshot-comparison-tool-in-unreal-engine - ground-truth screenshot tests.
20. Epic - Overview of containers (snippet) - https://dev.epicgames.com/documentation/unreal-engine/overview-of-containers-in-unreal-engine - UE container images since 4.27.
21. Gaffer on Games - Floating point determinism - https://gafferongames.com/post/floating_point_determinism/ - replay determinism conditions.
22. Pulse - FAQ - https://pulse.kitware.com/_f_a_q.html - Apache 2.0, validation approach.
23. Pulse - ValidationTargetData FairPercentError - https://pulse.kitware.com/group___validation_target_data___fair_percent_error.html - 30% "fair" threshold.
24. Pulse - Scenario file / mechanical ventilator pages (snippet) - https://pulse.kitware.com/_scenario_file.html ; https://pulse.kitware.com/md__mechanical_ventilator.html - baseline results, ±10% tolerance.
25. Searles BE et al. 2021, J Extra Corpor Technol 53:263-9 - https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf - objective validation of CPB simulator; reference ranges.
26. Sargent RG 2013, J Simulation 7:12-24 (snippet) - https://econpapers.repec.org/RePEc:taf:tjsmxx:v:7:y:2013:i:1:p:12-24 - simulation V&V concepts.
27. FDA - Assessing the Credibility of CM&S (Nov 2023) - https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions - risk-informed credibility framework.
28. Cook DA, Hatala R 2016, Adv Simul - https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/ - Messick/Kane frameworks, validation steps, mistakes.
29. McDougall EM 2007, J Endourol (snippet) - https://pubmed.ncbi.nlm.nih.gov/17444766/ - classic validity definitions.
30. Diamond IR et al. 2014, J Clin Epidemiol (snippet) - https://doi.org/10.1016/j.jclinepi.2013.12.002 - Delphi consensus thresholds.
31. Nasa P et al. 2021, World J Methodol - https://pmc.ncbi.nlm.nih.gov/articles/PMC8299905/ - Delphi quality elements, panel size.
32. Cristancho S et al. 2012, Surgery (snippet) - https://doi.org/10.1016/j.surg.2012.03.015 - off-pump CABG Delphi checklists.
33. Kemper et al. 2023, Simul Healthc, via AHRQ PSNet (snippet) - https://psnet.ahrq.gov/issue/crisis-scenarios-simulation-based-nontechnical-skills-training-cardiac-surgery-teams-national - 13 crisis scenarios, 114 experts.
34. STS press release 2016 - https://www.sts.org/sites/default/files/press-releases/Simulation%20FINAL%2082516.pdf - cardiac surgery simulation curriculum.
35. Feins RH et al. (PDF) - https://core.ac.uk/download/304667056.pdf - curriculum modules and outcomes.
36. Babar ZUD et al. 2023, JTCVS Techniques - https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/ - VR perfusion simulator face/content validity.
37. Sadeghi AH et al. 2022, JMIR Serious Games (snippet) - https://games.jmir.org/2022/1/e30456 - VR resternotomy/CPR simulator validity.
38. Cheng A et al. 2016, Adv Simul - https://dx.doi.org/10.1186/s41077-016-0025-y - simulation research reporting guidelines.
39. Ramphal PS et al. 2005, Eur J Cardiothorac Surg (snippet) - https://nottingham-repository.worktribe.com/output/1282729 - porcine-heart tissue simulator.
40. FDA - Examples of software functions that are not medical devices - https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices - training games not devices.
41. FDA - Policy for Device Software Functions and Mobile Medical Applications - https://www.fda.gov/regulatory-information/search-fda-guidance-documents/policy-device-software-functions-and-mobile-medical-applications - guidance context.
42. MDCG 2019-11 (Oct 2019) - https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native - MDR definition, qualification steps.
43. European Commission - MDCG endorsed documents - https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en - MDCG 2019-11 rev.1 June 2025.
44. ESRB - Ratings guide - https://www.esrb.org/ratings-guide/ - categories and descriptors.
45. ESRB - Surgeon Simulator - https://www.esrb.org/ratings/10010871/surgeon-simulator/ - T rating.
46. Common Sense Media - Surgeon Simulator 2 (snippet) - https://www.commonsensemedia.org/game-reviews/surgeon-simulator-2-access-all-areas - M rating.
47. PEGI - What do the labels mean - https://www.pegi.info/what-do-the-labels-mean - PEGI 16/18 wording.
48. IARC press release 2017 (snippet) - https://www.globalratings.com/news/grac-iarc-pressrelease-171219.pdf - IARC storefronts.
49. Steamworks - Content Survey - https://partner.steamgames.com/doc/gettingstarted/contentsurvey - mature content, AI disclosure.
50. Steamworks - Onboarding - https://partner.steamgames.com/doc/gettingstarted/onboarding - what not to publish.
51. PC Gamer - Steam AI disclosure update (snippet) - https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/ - Jan 2026 change.
52. 45 CFR 164.514 (Cornell LII) - https://www.law.cornell.edu/cfr/text/45/164.514 - HIPAA de-identification.
53. GDPR Recital 26 - https://gdpr-info.eu/recitals/no-26/ - anonymous data.
54. DICOM PS3.15 E.3.2 (snippet) - https://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.2.html - recognizable visual features.
55. TCIA Data Usage Policy (snippet) - https://wiki.cancerimagingarchive.net/x/c4hF - dataset licenses, no re-identification.
56. New Kids on the Block v. News America (snippet) - https://caselaw.findlaw.com/us-9th-circuit/1233126.html - nominative fair use.
57. Finnegan - AM General v. Activision (snippet) - https://www.finnegan.com/en/insights/blogs/incontestable/in-legal-warfare-over-humvee-trademarks-the-first-amendment-goes-beyond-the-call-of-duty-in-dismissing-am-generals-claims.html - realism and Rogers test.
58. Wikipedia - Jack Daniel's v. VIP Products (snippet) - https://en.wikipedia.org/wiki/Jack_Daniel%27s_Properties,_Inc._v._VIP_Products_LLC - Rogers limits.
59. Blender - License - https://www.blender.org/about/license/ - GPL, output ownership.
60. Meshroom - Releases - https://github.com/alicevision/Meshroom/releases - 2025.1.0.
61. Meshroom manual - CUDA FAQ (snippet) - https://meshroom-manual.readthedocs.io/en/latest/faq/needs-cuda/needs-cuda.html - GPU requirement.
62. COLMAP - GitHub - https://github.com/colmap/colmap - BSD license.
63. RealityScan - License - https://www.realityscan.com/license - free threshold, seat price.
64. RealityScan - EULA - https://www.realityscan.com/eula - output ownership, non-commercial definitions.
65. RealityScan 2.0 news - https://www.realityscan.com/news/realityscan-20-new-release-brings-powerful-new-features-to-a-rebranded-realitycapture - 17 Jun 2025 release.
66. Microsoft - TRELLIS.2 - https://github.com/microsoft/TRELLIS.2 - MIT, GPU need.
67. NVIDIA - nvdiffrast LICENSE - https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt - research/evaluation only.
68. Tencent - Hunyuan3D-2.1 LICENSE - https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE - territory exclusion.
69. Stability AI - License - https://stability.ai/license - Community License terms.
70. Meshy - Ownership of generated models - https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models - CC BY 4.0 free plan.
71. Tripo - Commercial use blog (snippet) - https://www.tripo3d.ai/blog/commercial-use-ai-3d-models - free plan CC BY 4.0 (conflicting).
72. US Copyright Office - Copyright and AI - https://www.copyright.gov/ai/ - Part 2 date.
73. Dykema - USCO Part 2 summary (snippet) - https://dykema.com/news-insights/the-future-of-creativity-us-copyright-office-clarifies-copyrightability-of-ai-generated-works.html - prompts alone insufficient.
74. Poly Haven - License - https://polyhaven.com/license - CC0.
75. ambientCG - License - https://docs.ambientcg.com/license/ - CC0 1.0.
76. Sketchfab - Licenses (snippet) - https://sketchfab.com/licenses - license types.
77. Epic - Fab licenses and pricing (snippet) - https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab - Standard/CC-BY, Personal tier.
78. Z-Anatomy - Models of human anatomy - https://github.com/Z-Anatomy/Models-of-human-anatomy - CC BY-SA 4.0, attributions.
79. 3D Slicer - Commercial use (snippet) - https://slicer.org/commercial-use.html - BSD-style license.
80. TotalSegmentator - GitHub (snippet) - https://github.com/wasserth/TotalSegmentator - Apache-2.0, restricted subtasks.
81. Unity - Unity Personal - https://unity.com/products/unity-personal - revenue cap, splash screen.
82. Epic - Unreal license (snippet) - https://www.unrealengine.com/en-US/license - 5% over US$1M.
83. Wikipedia - Surgeon Simulator - https://en.wikipedia.org/wiki/Surgeon_Simulator - dev time, team, sales.
84. Journal of Geek Studies - Project Hospital interview - https://jgeekstudies.org/2020/03/08/project-hospital-a-realistic-take-on-hospital-simulation - team size, realism process.
85. Wikipedia - Project Hospital - https://en.wikipedia.org/wiki/Project_Hospital - release date, engine.
86. Stardew Valley wiki (snippet) - https://stardewvalleywiki.com/Stardew_Valley - solo dev duration.
87. Politowski C et al. 2021 - https://arxiv.org/abs/2009.02440 - 200 postmortems, 927 problems.
88. Game Developer - "Why we should stop saying vertical slices" (snippet) - https://www.gamedeveloper.com/design/why-we-should-stop-saying-vertical-slices- - vertical slice term.
89. bugnet - What is a vertical slice (snippet) - https://bugnet.io/blog/what-is-a-vertical-slice - definition.

---

## Summary

**Key findings**
- Real benchmarks say: a comedic surgery game shipped in 48 days after a jam with 4 people, but a realistic hospital sim took a 2-4 person team ~2.5-3 years, and an academic VR perfusion simulator was first published with a single CPB scenario ([Wikipedia](https://en.wikipedia.org/wiki/Surgeon_Simulator); [JGS](https://jgeekstudies.org/2020/03/08/project-hospital-a-realistic-take-on-hospital-simulation); [Babar 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579814/)). Realism is the cost driver.
- Free storage tiers differ a lot: GitHub LFS 10 GiB, UVCS 25 GB (2026), Diversion Indie 100 GB, Perforce P4 self-hosted with 5 users/20 workspaces ([GitHub](https://docs.github.com/en/billing/concepts/product-billing/git-lfs); [Unity](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges); [Diversion](https://www.diversion.dev/pricing); [Perforce](https://www.perforce.com/products/helix-core/free-version-control)).
- CI is cheap for one developer: $12/month free compute on GitHub, free self-hosted runners, GameCI v4 for Unity ([GitHub](https://docs.github.com/en/billing/concepts/product-billing/github-actions); [GameCI](https://game.ci/docs/github/builder)).
- A published CPB simulator validation gives ready-made, expert-derived reference ranges and a method (parameter sweeps vs benchmark, Bland-Altman) that maps directly to automated regression tests ([Searles 2021](https://ject.edpsciences.org/articles/ject/pdf/2021/04/ject-53-263.pdf)).
- Modern validity thinking (Messick/Kane) replaces "face validity" claims; Delphi with an a-priori ~75% threshold is the standard way to agree content ([Cook & Hatala 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806296/); [Diamond 2014](https://doi.org/10.1016/j.jclinepi.2013.12.002)).
- AI 3D tools carry very different terms: MIT (TRELLIS.2) but with a research-only dependency, territory exclusions (Hunyuan3D 2.1), CC BY outputs on free plans (Meshy), and unclear copyright of raw AI output ([TRELLIS.2](https://github.com/microsoft/TRELLIS.2); [nvdiffrast](https://github.com/NVlabs/nvdiffrast/blob/main/LICENSE.txt); [Hunyuan3D](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/LICENSE); [Meshy](https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models); [USCO](https://www.copyright.gov/ai/)).
- A generic training game is outside FDA device rules (training games are listed as non-devices) and outside MDR if not for individual patients ([FDA](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices); [MDCG 2019-11](https://ec.europa.eu/docsroom/documents/37581/attachments/1/translations/en/renditions/native)).

**Recommendations**
1. Month 0-3: physiology-first vertical slice of one CPB phase, with regression tests against the Orpheus ranges and a medical-fact register from day 1.
2. Choose VCS by engine: UVCS (Unity) or Perforce P4 / Diversion (Unreal); keep raw scans out of Git LFS.
3. CI from week 1: GameCI or a self-hosted runner; tests in 6 layers (section 4.4).
4. Asset policy: CC0 + own work first; SA/NC isolated and flagged; AI only for props, human-edited, disclosed on Steam.
5. Validation path: SME review (4 roles) -> modified Delphi (75% a priori) -> optional small study reported with Cheng 2016 items; never claim "validated".
6. Legal: disclaimer gate, fictional brands, no patient-specific features, only public licensed imaging, gore setting.

**Open questions**
- Which engine? (Affects VCS and CI choice; see research 04.)
- Where does the owner live and plan to publish? (Hunyuan3D territory exclusion; GDPR applicability.)
- Is any future sale or donation model possible? (Decides whether NC assets are acceptable.)
- Can the project recruit at least one perfusionist, surgeon, anesthesiologist and OR nurse?
- Does Steam require an external age-rating certificate for this content? (UNVERIFIED.)
- Azure DevOps LFS "unlimited" storage and GitLab per-project limits need checking on official pages before use.
- Exact attribution terms of the Stability AI Community License and Tripo free-plan commercial terms (UNVERIFIED).
