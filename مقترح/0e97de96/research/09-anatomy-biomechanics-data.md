# Research 09: Anatomy and tissue biomechanics data

> **Purpose.** Collect the numbers the open heart surgery simulation game needs so that the heart, vessels, grafts, chest wall and blood *look* the right size and *behave* (stretch, tear, move, bleed) in a believable way. Every value has a source link next to it.
>
> **Researched 2026-11-03 (re-do, fresh searches).** Work was independent of older reports. Note: the shared web-search budget ran out part-way through. After that point only direct page fetches of already-known URLs were used. Gaps that remain are listed in the Summary (open questions).
>
> **Disclaimer.** This is research for a personal, non-commercial, educational game. It is **not clinical guidance**, not a medical device specification, and must not be used to make decisions about real patients. Many numbers come from small studies, animal tissue or cadavers. Values marked "(uncertain)" or "(uncertain - snippet only)" were not read in the full source text.

**Abbreviations (defined once).** LV/RV = left/right ventricle. LA/RA = left/right atrium. LM = left main coronary artery. LAD = left anterior descending artery. LCx = left circumflex artery. RCA = right coronary artery. PDA = posterior descending artery. OM = obtuse marginal branch. LIMA/IMA/ITA = (left) internal mammary/thoracic artery. SVG = saphenous vein graft. EDV/ESV = end-diastolic/end-systolic volume. BSA = body surface area. CT = computed tomography. CMR = cardiovascular magnetic resonance. QCA = quantitative coronary angiography. HO = Holzapfel-Ogden (myocardium material law). FEM = finite element method. XPBD = extended position-based dynamics. UTS = ultimate tensile strength. ACT = activated clotting time. CPB = cardiopulmonary bypass. Hct = hematocrit. EAT = epicardial adipose tissue. OPCAB = off-pump coronary artery bypass.

---

## 0. Summary for the plan

| Decision / Topic | Recommendation | Key evidence |
|---|---|---|
| Reference patient body | Build one "default adult male" (BSA about 1.9 m²) and one "default adult female" (BSA about 1.6 m²); scale chamber, valve and vessel sizes by sex. Women's coronaries about 9% smaller. | [Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570), [Lang 2015 ASE/EACVI](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) |
| Heart mass | Whole heart 330 g default for a young man (95% range 233-383 g). LV myocardium alone 121 ± 28 g (men) and 83 ± 21 g (women) by CMR. | [Molina & DiMaio 2012](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983), [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) |
| Wall thickness | LV 6-10 mm (men), 6-9 mm (women); RV 3 ± 1 mm (>5 mm abnormal). | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086), [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) |
| Coronary sizes | LM 4.5 mm, proximal LAD 3.7 mm, distal LAD 1.9 mm (Dodge). Typical bypass target about 2.1 mm; flag vessels <1.5 mm as "poor target". | [Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570), [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) |
| Coronary dominance | Randomise: right 85%, left 10%, co-dominant 5%. | [Folia Morphol n=4000](https://journals.viamedica.pl/folia_morphologica/article/view/86546) |
| Conduits | IMA 1.9-2.6 mm wide, wall 180-430 µm; SVG 3.1-8.5 mm wide, wall 180-650 µm. | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) |
| Myocardium material | Use HO law with the averaged literature parameter set for "offline/FEM truth"; derive simpler XPBD stiffness from it (fibre-direction small-strain modulus about 10-75 kPa, strongly strain-stiffening). | [PMC6096751](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751), [PMC6647490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/) |
| Active contraction | Fibre active stress 60 kPa is a published benchmark value; good default peak. | [Land 2015 benchmark](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf) |
| Vessel failure | Burst pressure: IMA about 3,200 mmHg, SVG about 1,600-2,100 mmHg. Coronary adventitia UTS about 1.3-1.4 MPa (uncertain). | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094), [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) |
| Needle force | Needle puncture of porcine heart wall 0.9-1.4 N, lower at faster insertion. | [PMC3051196](https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196) |
| Sternal retractor | Total spreading force about 220 N mean, 349 N max at 10 cm spread (range 159-494 N). | [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560), [Saggio 2017](https://www.scitepress.org/Papers/2017/61113/61113.pdf) |
| Heart motion | LAD moves about 10 mm per beat at up to about 48 mm/s; RCA mid-segment about 26 mm at up to about 131 mm/s. Breathing adds about 5-6 mm. | [Shechter 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264), [Shechter 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710) |
| LV torsion | Peak twist 10-19° (rises with age); apex counter-clockwise, base clockwise. | [Tavakoli 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236) |
| Blood | Viscosity about 4 cP at Hct 40%; about -25% at Hct 30%; about +2% per °C of cooling. | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) |
| Anticoagulation | ACT target >480 s (>400 s on maximally activated devices); protamine ≤2.6 mg per 100 U heparin. | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Bleeding model | Orifice-flow equation driven by local pressure, plus a coagulation state; calibrate needle-hole leaks to measured 20-57 mL/min per test anastomosis (uncertain). | Section 4 |
| Mesh source data | Best free path: TotalSegmentator dataset v3.0.0 (CC BY 4.0) + TotalSegmentator code (Apache-2.0) + 3D Slicer (BSD-style) + Blender. Heart chamber and coronary sub-models need a free non-commercial licence. | [Zenodo](https://zenodo.org/records/6802613), [GitHub](https://github.com/wasserth/TotalSegmentator) |

---

## 1. Anatomy dimensions

### 1.1 Heart size and mass

| Quantity | Value | Source | Grade |
|---|---|---|---|
| Whole heart weight, healthy men 18-35 y (n=232) | Mean 331 g, SD 56.7 g, observed range 188-575 g; proposed 95% reference range 233-383 g | [Molina & DiMaio 2012](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983) | A |
| Body weight / BMI as predictor of heart weight in that cohort | Too weak to predict | [Molina & DiMaio 2012](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983) | A |
| Whole heart weight, "non-disease reference group" of a 1,410-case autopsy cohort | 426 g (men), 351 g (women) (uncertain - snippet only) | [search hit, core.ac.uk](https://core.ac.uk/download/77167029.pdf) | C |
| Best body-size predictor of heart weight | BSA (Lausanne, n=288) | [Vanhaebost 2014](https://serval.unil.ch/notice/serval:BIB_85AA3C49A5A5) (uncertain - snippet only) | C |
| LV myocardial mass, CMR, papillary muscles counted as mass | 121 ± 28 g (66-176) men; 83 ± 21 g (41-125) women | [Kawel-Boehm 2020, Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LV mass index, CMR | 62 ± 11 g/m² (men), 49 ± 10 g/m² (women) | [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LV mass index, echo (linear method) normal range | 49-115 g/m² (men), 43-95 g/m² (women) | [Lang 2015, Table 6](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |

**Game default.** Male heart 330 g, female heart about 270 g (female value = 330 g × the women/men ratio 351/426 ≈ 0.82 from the snippet-only autopsy cohort above; the CMR LV-mass ratio 83/121 ≈ 0.69 would give about 226 g, so treat 226-272 g as the plausible band; **uncertain**). Scale the mesh so that LV mass matches 121 g (male) when myocardium density 1.05 g/mL is used (density value **UNVERIFIED** in this round).

### 1.2 Wall thickness

| Wall | Value | Source | Grade |
|---|---|---|---|
| LV septum, echo normal | 0.6-1.0 cm (men), 0.6-0.9 cm (women) | [Lang 2015, Table 6](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV posterior wall, echo normal | 0.6-1.0 cm (men), 0.6-0.9 cm (women) | [Lang 2015, Table 6](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV basal anteroseptal, CMR end-diastole | 9.0 ± 1.4 mm (men), 7.6 ± 1.2 mm (women) | [Kawel-Boehm 2020, Table 26](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LV basal inferolateral, CMR | 7.7 ± 1.2 mm (men), 6.3 ± 1.1 mm (women) | [Kawel-Boehm 2020, Table 26](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| RV free wall | 3 ± 1 mm (range 1-5 mm) | [Lang 2015, Table 8](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| RV wall "abnormal" cut-off | >5 mm | [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) | A |
| Relative wall thickness (concentric) cut-off | RWT >0.42 | [open-exam-prep summary of ASE 2015](https://open-exam-prep.com/study-guides/rdcs-adult/quantification-doppler/chamber-quantification) | C |
| Atrial wall thickness | **Not verified in this round** (gap) | - | - |

### 1.3 Chamber dimensions and volumes

| Chamber / measure | Men | Women | Source | Grade |
|---|---|---|---|---|
| LV end-diastolic diameter (echo) | 50.2 ± 4.1 mm (42.0-58.4) | 45.0 ± 3.6 mm (37.8-52.2) | [Lang 2015, Table 2](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV end-systolic diameter (echo) | 32.4 ± 3.7 mm | 28.2 ± 3.3 mm | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV EDV, echo biplane | 106 ± 22 mL (62-150) | 76 ± 15 mL (46-106) | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV ESV, echo biplane | 41 ± 10 mL (21-61) | 28 ± 7 mL (14-42) | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| LV EDV, CMR (papillary in mass) | 155 ± 30 mL (95-215) | 123 ± 22 mL (78-167) | [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LV ESV, CMR | 55 ± 15 mL | 43 ± 11 mL | [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LV ejection fraction, echo normal | 52-72% | 54-74% | [Lang 2015, Table 4](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| RV EDV, CMR | 166 ± 39 mL (87-244) | 122 ± 27 mL (68-176) | [Kawel-Boehm 2020, Table 10](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| RV ESV, CMR | 73 ± 22 mL | 50 ± 15 mL | [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| RV basal diameter, echo | 33 ± 4 mm (25-41); >41 mm abnormal | same | [Lang 2015, Table 8](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086), [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) | A |
| LA maximal volume, CMR biplane | 72 ± 20 mL | 64 ± 18 mL | [Kawel-Boehm 2020, Table 14](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| LA volume index, echo normal | 16-34 mL/m² | 16-34 mL/m² | [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) | A |
| LA anteroposterior diameter | 3.0-4.0 cm | 2.7-3.8 cm | [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) | A |
| RA maximal volume, CMR biplane | 65 ± 20 mL | 53 ± 14 mL | [Kawel-Boehm 2020, Table 17](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) | A |
| RA area, echo normal | ≤18 cm² | ≤18 cm² | [ASE summary](https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf) | A |
| Pericardial fluid, normal | 20-25 mL | 20-25 mL | [PMC4929280](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280) | B |

Note: CMR volumes are larger than echo volumes for the same heart. Use CMR values for the 3D model (CMR sees the whole cavity). Use echo values only for any in-game "TEE readout" (transoesophageal echo) so the displayed numbers match what clinicians expect.

### 1.4 Valve annuli and aortic root

| Structure | Men | Women | Source | Grade |
|---|---|---|---|---|
| Aortic annulus | 26 ± 3 mm | 23 ± 2 mm | [Lang 2015, Table 14](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| Sinuses of Valsalva | 34 ± 3 mm | 30 ± 3 mm | [Lang 2015, Table 14](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| Sinotubular junction | 29 ± 3 mm | 26 ± 3 mm | [Lang 2015, Table 14](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| Proximal ascending aorta (echo) | 30 ± 4 mm | 27 ± 4 mm | [Lang 2015, Table 14](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) | A |
| Ascending aorta, non-contrast gated CT, n about 2,952 | mean 33 ± 4 mm, upper limit 41 mm | - | [Wolak et al. via search](https://cris.bgu.ac.il/en/publications/aortic-size-assessment-by-noncontrast-cardiac-computed-tomography-2/) (uncertain - snippet only) | C |
| Ascending aorta, contrast CT, n=1,442 | 33.6 ± 4.1 mm | 31.1 ± 3.9 mm | [PMC3766427 search hit](https://pmc.ncbi.nlm.nih.gov/articles/PMC3766427) (uncertain - snippet only) | C |
| Aortic annulus mean diameter indexed to BSA, CT, n=1,286 (Chinese cohort) | about 12.6-13.1 mm/m² across age groups | about 13.0-13.7 mm/m² | [Zhang et al., IJGM 2021](https://doi.org/10.2147/IJGM.S312439) | A |
| Coronary ostium height above annulus, indexed, same CT cohort | left about 8.3-9.3 mm/m²; right about 8.9-10.2 mm/m² | left about 8.7-9.7; right about 9.0-9.7 mm/m² | [Zhang et al., IJGM 2021](https://doi.org/10.2147/IJGM.S312439) | A |
| Mitral annulus, 3D echo | anteroposterior 28.5 ± 3.7 mm; intercommissural 33.0 ± 5.3 mm | - | [search hit, Frontiers 2022](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.1011931/epub) (uncertain - snippet only) | C |
| Mitral annulus AP, CMR (UK Biobank) | 29 ± 4 mm | 26 ± 4 mm | same search (uncertain - snippet only) | C |
| Tricuspid annulus, 3D echo end-diastole, n=254 | major 38 ± 4 mm, minor 31 ± 4 mm | - | [Houston Methodist record](https://scholars.houstonmethodist.org/en/publications/reference-ranges-of-tricuspid-annulus-geometry-in-healthy-adults-/) (uncertain - snippet only) | C |

Derived (uncertain): with BSA 1.87 m² (men) and 1.61 m² (women) from the same CT cohort ([IJGM 2021](https://doi.org/10.2147/IJGM.S312439)), the indexed ostium heights give absolute left-ostium heights of roughly 15-17 mm (men) and 14-16 mm (women). This is a modelling estimate, not a measured absolute value.

### 1.5 Coronary arteries: diameters, lengths, dominance, variants

**Diameters (lumen, angiography).**

| Segment | Dodge 1992 (n=83 normal, from 9,160 studies) | Indian QCA (n=229) | Nepal QCA (n=100) |
|---|---|---|---|
| LM | 4.5 ± 0.5 mm | 4.08 ± 0.44 mm | 4.06 ± 0.68 mm |
| Proximal LAD | 3.7 ± 0.4 mm | 3.27 ± 0.23 mm | 3.26 ± 0.48 mm |
| Mid LAD | - | - | 2.67 ± 0.49 mm |
| Distal LAD | 1.9 ± 0.4 mm | - | 2.01 ± 0.44 mm |
| Proximal LCx | 3.4 ± 0.5 to 4.2 ± 0.6 mm (depends on dominance) | 2.97 ± 0.37 mm | 2.91 ± 0.48 mm |
| Distal LCx | - | - | 2.38 ± 0.44 mm |
| Proximal RCA | 2.8 ± 0.5 to 3.9 ± 0.6 mm (depends on dominance) | 3.20 ± 0.37 mm | 3.2 ± 0.51 mm |
| Source | [Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570) (A) | [PMC5560873](https://pmc.ncbi.nlm.nih.gov/articles/PMC5560873) (A) | [JIOM Nepal](https://jiomnepal.edu.np/index.php/jiomnepal/article/view/1276) (uncertain - snippet only, C) |

Other Dodge findings ([Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570)):
- Women's epicardial arteries are about 9% smaller than men's, even after BSA normalisation.
- Lumen diameter is not affected by age or tortuosity.
- Lumen is about 17% larger with LV hypertrophy and about 12% larger with dilated cardiomyopathy (men).
- LAD diameter does not depend on dominance.
- Measurement repeat error was 0.12 mm.

**Branch vessels (diagonals, OM, PDA).** Exact normal diameters for these branches were **not verified** in this round. The best usable proxy: grafted target coronaries measured 2.14 ± 0.52 mm (range 1-5 mm) in a long-term SVG follow-up ([PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415)). Game default for diagonal, OM and PDA: 1.5-2.5 mm (**uncertain**, chosen to bracket that proxy).

**Lengths (cadaver, n=60 hearts, India).** ([Asar et al. 2023](https://journals.innovareacademics.in/index.php/ajpcr/article/download/48400/29246), grade B)
- LM trunk: 12.6 ± 3.74 mm (range 3.4-19 mm). Other cited series: 7.5-20 mm means (same paper).
- LAD: 105.3 ± 27 mm (33.4-154.4 mm).
- LCx: 79.2 ± 26.2 mm (31.9-144.5 mm).
- RCA segment I (origin to right border): 81.5 ± 18.1 mm; segment II (right border to crux): 20.3 ± 9.9 mm; segment III (beyond crux): 38.2 ± 18.7 mm.
- Caution: segment end-points differ between studies, so lengths are not directly comparable.

**Dominance.**

| Population / source | Right | Left | Co-dominant | Grade |
|---|---|---|---|---|
| 4,000 angiograms, India ([Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546)) | 85.5% | 9.7% | 4.8% | A |
| Textbook estimate cited in same paper ([Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546)) | 80-85% | 7-13% | 2-5% | B |
| About 1,200 patients, CT ([Weill Cornell record](https://vivo.weill.cornell.edu/display/pubid34171741)) | 91.7% | 8% | 1.3% | C (snippet only) |
| 102 patients, India ([DOAJ](https://doaj.org/article/0acf800055a0450f9d71e045d7886d7b)) | 60.8% | 24.5% | 14.7% | C (snippet only) |

Game default: right 85%, left 10%, co-dominant 5% ([Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546)). When the left system is dominant, make the proximal LCx larger (up to about 4.2 mm) and the RCA smaller (down to about 2.8 mm), as Dodge found ([Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570)).

**Common variants.** Prevalence of myocardial bridging, ramus intermedius and anomalous origins was **not verified** in this round (the n=4,000 paper did not report them ([Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546))). Treat these as optional "variant" scenario flags until sourced.

### 1.6 Bypass targets and conduits

| Item | Value | Source | Grade |
|---|---|---|---|
| Target coronary diameter (patent SVG cases) | 2.14 ± 0.52 mm (1-5 mm) | [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) | A |
| Target vessel <1.5 mm | "significant risk factor for occlusion" of vein and arterial grafts | [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) | A |
| SVG patency vs target size (VA cooperative study) | 88% in targets >2.0 mm vs 55% in targets ≤2.0 mm | [Arizona record](https://experts.arizona.edu/en/publications/long-term-patency-of-saphenous-vein-and-left-internal-mammary-art/) (uncertain - snippet only) | C |
| 10-year patency (VA study) | SVG 61%, IMA 85% | same (uncertain - snippet only) | C |
| IMA diameter, adult | 1.9-2.6 mm | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) | A |
| IMA wall thickness | 180-430 µm; 7-11 elastic lamellae | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) | A |
| SVG diameter | 3.1-8.5 mm | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) | A |
| SVG wall thickness | 180-650 µm | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) | A |
| Patent SVG diameter at about 11.6 years | 3.55 ± 0.76 mm (1.8-6 mm) | [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) | A |
| SVG harvest site | 91% below the knee in one cohort | [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) | A |
| LIMA length, pedicled vs skeletonised (n=52, same conduits) | 16.8 ± 0.7 cm vs 18.9 ± 0.5 cm | [TGKDC abstract](https://tgkdc.dergisi.org/abstract.php?id=884) (uncertain - snippet only) | C |
| Skeletonisation length gain (systematic review) | about +3 cm | [ICVTS best evidence topic](https://academic.oup.com/icvts/article/4/6/577/745846) (uncertain - snippet only) | C |
| LIMA angiographic diameter near anastomosis | 1.57 ± 0.17 mm pedicled vs 1.77 ± 0.28 mm skeletonised | [ICVTS best evidence topic](https://academic.oup.com/icvts/article/4/6/577/745846) (uncertain - snippet only) | C |
| Total SVG harvest length needed | **UNVERIFIED** (gap) | - | - |

### 1.7 Chest wall, pericardium, epicardial fat

**Sternum (multidetector CT, n=200 adults, Turkey)** ([Ateşoğlu 2018](https://journals.viamedica.pl/folia_morphologica/article/download/FM.a2018.0002/42756), grade A):

| Measure | Women | Men |
|---|---|---|
| Manubrium length | 46.7 ± 5.1 mm | 51.2 ± 6 mm |
| Body (corpus) length | 86.6 ± 9.7 mm | 102.4 ± 13.3 mm |
| Total sternum length | 133.1 ± 11 mm | 154.1 ± 13.1 mm |
| Manubrium thickness | 8 ± 1.6 mm | 9.2 ± 1.5 mm |
| Body thickness (sternebrae 2-3) | 8.1 ± 1.3 mm | 9.2 ± 1.5 mm |
| Body thickness (sternebrae 4-5) | 7.9 ± 1.5 mm | 8.5 ± 1.5 mm |
| Manubrium width | 54.6 ± 5.2 mm | 64.4 ± 7 mm |
| Body width (sternebrae 2-3 / 3-4 / 4-5) | 23.8 / 25.8 / 27.8 mm | 27.7 / 30 / 32.4 mm |
| Xiphoid length | 29 ± 10 mm | 39.1 ± 11.3 mm |
| Sternal foramen prevalence | 3.5% (both sexes) | |

**Pericardium.**
- Fibrous and visceral layers are each 0.5-1.0 mm thick ([PMC4929280](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280), B).
- On CT the normal pericardium is a line <2 mm thick; >4 mm on MRI is abnormal ([PMC4929280](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280), B).
- CT measurement study: 1.8 ± 0.5 mm over the RV (n=50) (uncertain - snippet only; [Applied Radiology](https://www.appliedradiology.com/doi/10.37549/AR2187)).

**Epicardial adipose tissue (EAT)** ([Iacobellis review, PMC5779180](https://pmc.ncbi.nlm.nih.gov/articles/PMC5779180), B):
- No agreed "normal" thickness exists.
- Echo over the RV free wall, end-systole: range 1-22.6 mm; mean 7 mm (men), 6.5 mm (women).
- End-diastole: 4.7 ± 1.5 mm (n=356 asymptomatic); 6.38 mm mean (range 1.1-16.6) in angiography patients.
- Cut-offs used: >5 mm (increased EAT); ≥5.2-7.6 mm linked to coronary disease.
- Distribution: concentrated in the atrioventricular and interventricular grooves, along the lateral RV wall and around the coronary arteries.

Game rule: make fat thickest in the AV and interventricular grooves (where the LAD runs), so that the player must dissect fat to expose the LAD. Use 2-8 mm over the LAD as a per-patient random value (**uncertain**, extrapolated from the RV free-wall values above).

---

## 2. Tissue mechanical properties

### 2.1 Myocardium: passive (HO law)

The HO law is the field's standard orthotropic model for passive myocardium ([PMC6647490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/)). The strain energy is:

W = a/(2b)·[exp(b(I1−3))−1] + Σ(i=f,s) a_i/(2b_i)·[exp(b_i(I4i−1)²)−1] + a_fs/(2b_fs)·[exp(b_fs·I8fs²)−1], with incompressibility J = 1 ([PMC6647490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/)).

**Published parameter sets** (a-type in kPa; b-type dimensionless) ([PMC6096751, Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751), A):

| Source | a | b | a_f | b_f | a_s | b_s | a_fs | b_fs |
|---|---|---|---|---|---|---|---|---|
| Holzapfel & Ogden 2009 (porcine shear data) | 0.059 | 8.023 | 18.472 | 16.026 | 2.481 | 11.120 | 0.216 | 11.436 |
| Göktepe 2011 | 0.496 | 7.209 | 15.193 | 20.147 | 3.283 | 11.176 | 0.662 | 9.466 |
| Wang 2013a | 0.236 | 10.81 | 20.037 | 14.154 | 3.724 | 5.164 | 0.411 | 11.3 |
| Eriksson 2013 | 0.333 | 9.242 | 18.535 | 15.972 | 2.564 | 10.446 | 0.417 | 11.602 |
| **Average (recommended default)** | **0.28** | **8.82** | **18.1** | **16.5** | **3.0** | **9.5** | **0.4** | **10.9** |

**Human tissue fit.** Sommer et al. 2015 tested human LV myocardium with biaxial extension and triaxial shear ([Sommer 2015 DOI](https://doi.org/10.1016/j.actbio.2015.06.031)). A reduced HO model fitted to those human data gave a = 0.809 kPa, b = 7.474, a_f = 1.911 kPa, b_f = 22.063, a_n = 0.227 kPa, b_n = 34.802, a_fs = 0.547 kPa, b_fs = 5.691 ([PMC6647490, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/), A). The human fit is much softer in the fibre direction at small strain but stiffens faster (higher b_f).

**Derived simple stiffness for real-time use (uncertain, my derivation).** For small strain ε, the fibre term behaves like a linear spring with modulus about 4·a_f and the ground matrix shear modulus is about a. So:
- Fibre-direction small-strain modulus: about 74 kPa (HO 2009 a_f = 18.47 kPa) or about 8 kPa (human fit a_f = 1.91 kPa).
- Cross-fibre: about 10 kPa (4·a_s with a_s = 2.5 kPa).
- Strain-stiffening: with b_f ≈ 16, the exponential factor exp(b_f·(2ε)²) is about 1.9 at 10% fibre strain and about 13 at 20% fibre strain. This is why heart tissue feels soft when touched lightly but resists strong stretch.

**In vivo stiffness (elastography).**
- Human cardiac MR elastography: shear stiffness about 6.5-8.7 kPa across cardiac phases, lowest at end-diastole (uncertain - snippet only; [ISMRM 2009](https://archive.ismrm.org/2009/0711.html)).
- Pig cardiac MRE: shear stiffness 5.1-9.89 kPa over the cycle; stiffer in systole (uncertain - snippet only; same search).

### 2.2 Myocardium: active tension

- A community benchmark used a constant fibre active stress (second Piola-Kirchhoff) of **Ta = 60 kPa**, with 15 kPa (about 112 mmHg) cavity pressure, passive Guccione law C = 2 kPa, b_f = 8, b_t = 2, b_fs = 4 ([Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf), A).
- The same paper's LV test geometry is a truncated ellipsoid: endocardium r_s = 7 mm, r_l = 17 mm; epicardium r_s = 10 mm, r_l = 20 mm; fibre angle from −90° (epicardium) to +90° (endocardium) ([Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf)). This is a small, idealised test shape, not a real-size heart, but it is a perfect unit test for the game's solver.
- The often-quoted Guccione active model value Tmax = 135.7 kPa was **not verified** in this round (uncertain).
- Whole-heart FE models using cell-level tension values can give unphysiological stresses or too little deformation unless re-scaled ([search summary, Frontiers 2018](https://www.frontiersin.org/articles/10.3389/fphys.2018.00425/full), uncertain - snippet only). Game approach: treat peak active tension as a tuning knob (30-120 kPa) and tune it until EF and wall thickening match section 1.3.

### 2.3 Arteries, veins and grafts

| Tissue | Property | Value | Source | Grade |
|---|---|---|---|---|
| Native IMA (from CABG patients) | Burst pressure | 3,196 ± 1,264 mmHg (n=16) | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094) | A |
| Native SV | Burst pressure | 1,599 ± 877 mmHg (n=7) | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094) | A |
| Native IMA | Suture retention (5-0 Prolene, 2 mm bite, 120 mm/min, ISO 7198) | 138 ± 50 gf (about 1.35 N) | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094) | A |
| ITA (compiled) | Burst / suture retention / compliance | 3,073 mmHg / 1.72 N / 11.5% per 100 mmHg | [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) | B |
| SV (compiled) | Burst / suture retention / compliance | 2,134 (± 284) mmHg / 1.92 N / 25.6% per 100 mmHg | [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) | B |
| Human LAD, layer-specific (n=13, autopsy) | Adventitia UTS | about 1,430 ± 604 kPa (circumferential), 1,300 ± 692 kPa (axial); about 3× media/intima | [Holzapfel 2005 via scite](https://scite.ai/authors/gerhard-holzapfel-wmX1ny), [DOI](https://doi.org/10.1152/ajpheart.00934.2004) (uncertain - snippet only) | C |
| Human LAD | Stiffest layer | Intima; media softest axially | same (uncertain - snippet only) | C |
| Aorta (general) | Uniaxial strength | "a few tenths of MPa to a few MPa" between individuals | [Duprey 2016](https://hal.archives-ouvertes.fr/hal-01380216/file/2016_actabio_duprey_auteur.pdf) (uncertain - snippet only) | C |
| Aneurysmal ascending aorta | Elastic modulus | 9.19 MPa circumferential vs 3.13 MPa longitudinal (97 samples, 13 patients) | [Khanafer 2011, PubMed](https://pubmed.ncbi.nlm.nih.gov/21616506) (uncertain - snippet only) | C |
| Ascending aorta, modelling | Peak matrix stress in control tissue | 2.4 MPa (circumferential load), 1.6 MPa (longitudinal load); strength data from Pichamuthu 2013 (n=7 control, 13 TAV, 23 BAV) | [Thunes, PMC8059307](https://pmc.ncbi.nlm.nih.gov/articles/PMC8059307) | A (model) |
| Ascending aorta | Direction of greater strength | Circumferential > longitudinal in dilated aorta | [Brečs 2019](https://science.rsu.lv/en/publications/biomechanical-properties-of-human-dilated-ascending-aorta/) (uncertain - snippet only) | C |

**Derived wall moduli (uncertain, my derivation).** Using thin-wall tube theory and the compliance values above:
- Pressure-strain modulus Ep = ΔP / (ΔD/D). ITA: 100 mmHg / 0.115 ≈ 870 mmHg ≈ 116 kPa. SV: 100 / 0.256 ≈ 390 mmHg ≈ 52 kPa.
- Incremental Young's modulus E ≈ Ep · D / (2h) · (1 − ν²). With IMA D = 2.2 mm, h = 0.3 mm ([Otsuka 2013](https://annalscts.com/article/view/2416/pdf)): E ≈ 0.3 MPa. With SV D = 4 mm, h = 0.4 mm: E ≈ 0.2 MPa.
- These are physiological-pressure values. At high strain (near failure) arteries stiffen to several MPa, consistent with the aneurysm moduli above.

### 2.4 Pericardium, skin, fat, bone

| Tissue | Property | Value | Source | Grade |
|---|---|---|---|---|
| Fresh human pericardium (18 strips, 3.5 × 25 mm) | UTS | 3.14 ± 0.70 MPa | [De Gruyter BMT 2013](https://www.degruyterbrill.com/document/doi/10.1515/bmt-2013-4095/pdf) (uncertain - snippet only) | C |
| Same | Tangent modulus at 30% strain | 98.7 ± 20.8 MPa | same (uncertain - snippet only) | C |
| Glutaraldehyde-treated human pericardium | UTS | 6.20 ± 1.47 MPa | same | C |
| Other untreated pericardium study | UTS | 22.17 ± 8.30 MPa (protocol differs; conflicts with 3.14 MPa) | same search | C |
| Skin (all test types) | Young's modulus | 5 kPa to 140 MPa (depends on in vivo vs ex vivo, indentation vs tension) | [Kalra review](https://www.researchgate.net/profile/Anubha-Kalra/publication/307522356_Mechanical_Behaviour_of_Skin_A_Review/links/5850b5b808aecb6bd8d21795/Mechanical-Behaviour-of-Skin-A-Review.pdf) (uncertain - snippet only) | C |
| Skin, in vivo dermis (thigh, crawling waves, 200 Hz) | Young's modulus | 18.35 ± 1.04 kPa | [PUCP record](https://laboratorio-imagenes-medicas.pucp.edu.pe/publicaciones/in-vivo-estimation-of-the-youngs-modulus-in-normal-human-dermis) (uncertain - snippet only) | C |
| Human subcutaneous fat (tension) | Initial / 30%-strain tangent modulus | 1.6 ± 0.8 kPa / 11.7 ± 6.4 kPa | [Alkhouli 2013 via search](https://pmc.ncbi.nlm.nih.gov/articles/PMC9005403) (uncertain - snippet only) | C |
| Porcine subcutaneous fat (shear, 10 rad/s, 37 °C) | Shear modulus | 7.5 kPa | [Geerligs 2008](https://research.tue.nl/en/publications/linear-viscoelastic-behavior-of-subcutaneous-adipose-tissue/) (uncertain - snippet only) | C |
| Rib cortical bone (proxy for sternum), tension coupons | E / UTS / ultimate strain | 13.9 GPa / 124.2 MPa / 2.7% | [Kemper thesis](https://vtechworks.lib.vt.edu/bitstream/10919/43709/1/KemperThesis.pdf) (uncertain - snippet only) | C |
| Rib cortical bone, 3-point bending, by region | E / UTS | anterior 7.51 GPa / 116.7 MPa; lateral 11.9 GPa / 153.5 MPa | same search (uncertain - snippet only) | C |
| Sternum-specific bone properties | - | **Not found** (gap). Use rib cortical values as a proxy. | - | - |

### 2.5 Sutures, needles, wires and instrument forces

| Interaction | Value | Source | Grade |
|---|---|---|---|
| Needle puncture of porcine heart wall, 1.1 mm tri-pointed surgical needle | 1.37 ± 0.11 N at 1 mm/s; 1.35 N at 5 mm/s; 1.108 N at 20 mm/s; 0.85 N at 50 mm/s; 0.88 ± 0.08 N at 100 mm/s | [PMC3051196, Table I](https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196) | A |
| Needle tissue deflection before rupture at 100 mm/s | 7 mm (19 G trocar) vs 3.5 mm (18 G bevel) | [PMC3021974](https://pmc.ncbi.nlm.nih.gov/articles/PMC3021974) | A |
| Rupture-force saturation velocity | 70 mm/s (trocar), 35 mm/s (bevel) | [PMC3021974](https://pmc.ncbi.nlm.nih.gov/articles/PMC3021974) | A |
| Static pre-puncture stiffness fit (heart) | f = 0.01δ² + 0.026δ (trocar); f = 0.0115δ² + 0.0114δ (bevel) (units as in paper, likely N and mm) | [PMC3021974](https://pmc.ncbi.nlm.nih.gov/articles/PMC3021974) | A |
| Suture retention, IMA | 1.35 N (138 gf) | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094) | A |
| Suture retention, ITA / SV (compiled) | 1.72 N / 1.92 N | [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) | B |
| 6-0 polypropylene breaking force | 436.9 g (about 4.3 N) unknotted; 316.9 g (about 3.1 N) knotted | [Landymore canine carotid study](https://latam-cl.demo.elsevierpure.com/fr/publications/effect-of-force-on-anastomotic-suture-line-disruption-after-carot) (uncertain - snippet only) | C |
| In vivo axial force on 6-0 suture after carotid repair | about 26 g (0.25 N), falling to 18 g at 6 weeks | same (uncertain - snippet only) | C |
| Grasping 6-0 polypropylene with DeBakey forceps | dose-dependent strength loss; a stray knot cut strength 17% | [Scilit record](https://scilit.net/publications/0b06deed15f3892aaf9953d1c115129e) (uncertain - snippet only) | C |
| USP <881> knot-pull minimums for 7-0 to 4-0 | **Not verified** (gap). Only 8-0 class I ≥0.59 N found. | [USP summary via patent](https://patents.justia.com/patent/20240423611) (uncertain) | C |
| Sternal retractor, total force first retraction (18 cadavers, to 10 cm) | 222.8 ± 52.9 N (straight) vs 226.4 ± 71.9 N (curved) | [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560) | A |
| Sternal retractor, maximum total force for full retraction | 349.4 ± 77.9 N; single highest 493.6 N, lowest maximum 159.0 N | [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560), [Saggio 2017](https://www.scitepress.org/Papers/2017/61113/61113.pdf) | A |
| Retractor force by sex, first retraction | 256.2 ± 43.3 N (men) vs 174.9 ± 52.9 N (women) | [Saggio 2017 citing Aigner](https://www.scitepress.org/Papers/2017/61113/61113.pdf) | B |
| Straight retractor force split cranial / median / caudal | 101.5 / 29.1 / 63.0 N | [Saggio 2017 citing Aigner](https://www.scitepress.org/Papers/2017/61113/61113.pdf) | B |
| Force decay over repeated retractions | 224.6 ± 61.3 N (1st) to 110.8 ± 39.8 N (4th) | [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560) | A |
| Force-controlled retraction (other group, cadaver/sheep) | average 77.88 ± 38.85 N, max 323.99 ± 127.79 N | [Saggio 2017](https://www.scitepress.org/Papers/2017/61113/61113.pdf) | B |
| Sternal wire closure force | 220.5 N (figure-of-eight) vs 182.8 N (simple), 7-gauge 316L | [J Cardiothorac Surg 2009](https://link.springer.com/article/10.1186/1749-8090-4-19) (uncertain - snippet only) | C |
| Wire cut-through (cadaver) | separation by wire cutting through bone at forces <400 N | same search (uncertain - snippet only) | C |
| Forceps grasp force in cardiac/vascular surgery | **Not found** in measured data (gap). One spoken talk cites about 30 N pinch (C, unreliable). | [MedAll transcript](https://app.medall.org/contents/v-bbass-get-a-grip-don-t) | C |

### 2.6 Recommended hyperelastic material defaults for FEM / XPBD

XPBD defines compliance α as inverse stiffness and uses α̃ = α/Δt² in the constraint update, which makes stiffness independent of time step and iteration count ([Macklin, Müller, Chentanez 2016](https://matthias-research.github.io/pages/publications/XPBD.pdf), A). For a Neo-Hookean tetrahedral solver, set the deviatoric compliance from μ and the volume compliance from λ (Lamé constants). Standard conversions: μ = E/(2(1+ν)), λ = Eν/((1+ν)(1−2ν)). The per-constraint mapping α_dev = 1/μ, α_vol = 1/λ is from the stable Neo-Hookean constraint method (uncertain - that paper was not fetched in this round).

| Tissue | Model for game | Small-strain E (kPa) default [range] | ν | Basis |
|---|---|---|---|---|
| Myocardium, diastole | Neo-Hookean + fibre spring, or HO (average set) | 20 [8-75] fibre, 10 cross-fibre | 0.45-0.49 | Derived from [PMC6096751](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751) and [PMC6647490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/) (uncertain) |
| Myocardium, systole | Add active fibre stress | peak Ta 60 [30-120] kPa | - | [Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf) |
| Coronary artery wall | Neo-Hookean shell, stiffening | 300 [100-1,000] | 0.45 | Derived; failure about 1.3 MPa adventitia ([scite snippet](https://scite.ai/authors/gerhard-holzapfel-wmX1ny)) (uncertain) |
| IMA wall | Neo-Hookean shell | 300 [150-600] | 0.45 | Derived from [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) + [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) (uncertain) |
| SVG wall | Neo-Hookean shell | 200 [100-500] | 0.45 | Same derivation (uncertain) |
| Ascending aorta wall | Fibre-reinforced shell | 500 [200-3,000] (stiffens with strain) | 0.45 | [Khanafer](https://pubmed.ncbi.nlm.nih.gov/21616506), [Duprey](https://hal.archives-ouvertes.fr/hal-01380216/file/2016_actabio_duprey_auteur.pdf) (uncertain) |
| Pericardium | Membrane / cloth | 1,000-100,000 (very nonlinear; tangent 98.7 MPa at 30% strain) | 0.45 | [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/bmt-2013-4095/pdf) (uncertain) |
| Skin | Neo-Hookean shell | 20 [5-500] in vivo | 0.45 | [PUCP](https://laboratorio-imagenes-medicas.pucp.edu.pe/publicaciones/in-vivo-estimation-of-the-youngs-modulus-in-normal-human-dermis) (uncertain) |
| Subcutaneous / epicardial fat | Soft Neo-Hookean | 2 [1-12] | 0.49 | [Alkhouli via search](https://pmc.ncbi.nlm.nih.gov/articles/PMC9005403) (uncertain) |
| Sternum | Rigid body + breakable joint | 10 GPa cortical equivalent | 0.3 | [Kemper](https://vtechworks.lib.vt.edu/bitstream/10919/43709/1/KemperThesis.pdf) (uncertain) |

Mooney-Rivlin parameters for these tissues were **not verified** in this round. Recommendation: do not copy Mooney-Rivlin constants from forums; instead fit a two-term model offline to the HO curves above (a short script can sample uniaxial stress-stretch from the HO set and fit C10, C01).

---

## 3. Motion data

### 3.1 Coronary motion during the heartbeat (biplane angiography, 10 patients)

([Shechter 2006, PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264), A)

| Landmark | 3D peak cardiac displacement (mm) | Peak systolic velocity (mm/s) | 3D tidal-breath displacement (mm) |
|---|---|---|---|
| RCA origin | 14.4 ± 1.9 | 69.8 ± 13.8 | 5.0 ± 1.3 |
| RCA mid | 26.3 ± 3.1 | 130.7 ± 19.4 | 6.4 ± 1.9 |
| RCA acute margin | 23.2 ± 1.6 | 101.8 ± 13.4 | 7.2 ± 2.2 |
| LM origin | 7.9 ± 2.2 | 34.5 ± 8.8 | 4.6 ± 1.4 |
| LM bifurcation | 8.5 ± 1.7 | 39.1 ± 5.4 | 5.0 ± 1.6 |
| LAD at 5 cm | 9.6 ± 1.3 | 47.5 ± 9.3 | 5.6 ± 2.1 |
| LCx at 5 cm | 12.1 ± 2.4 | 56.4 ± 10.1 | 6.3 ± 1.6 |

- Earlier in-plane values (Hofman, as cited): RCA 25 ± 5 mm, LM 9 ± 1 mm, LAD 11 ± 4 mm, LCx 12 ± 2 mm ([PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264), A).
- Electron-beam CT, 25 subjects: mean in-plane coronary velocity 46.6 ± 12.5 mm/s; lowest 27.9 mm/s at 48% of the cycle ([Radiology DOI](https://doi.org/10.1148/radiology.216.2.r00au19457), uncertain - snippet only).
- Quiet window: a mid-diastolic period of about 187 ms at 72 ± 5% of the cycle when all three arteries moved little ([Johnson 2004 JCMR](https://scmr.org/wp-content/uploads/2023/12/2004_V6_No_3_663-73.pdf), uncertain - snippet only). Rest periods (<1 mm motion) were 66-333 ms (mean 161 ms) for the left and 66-200 ms (mean 120 ms) for the right coronary ([search summary](https://doi.org/10.1148/radiology.213.3.r99dc41751), uncertain - snippet only).

### 3.2 Off-pump stabiliser effect

- Pig study, 3 stabilisers: anastomosis-site motion reduced by 81.4%, 80.5% and 75.7% ([HSF record](https://journal.hsforum.com/index.php/HSF/article/view/934), uncertain - snippet only).
- Stabiliser changed LAD motion to a monophasic pattern and lowered excursion, maximum and average velocity (swine, sonomicrometry) (same, uncertain - snippet only).
- Derived (uncertain): residual LAD motion under a stabiliser ≈ 9.6 mm × (1 − 0.8) ≈ 2 mm per beat, at about 10 mm/s peak. Mechanical stabilisers "exhibit significant residual motion" ([Cedrat technical page](https://cedrat-technologies.com/produit/cardiolock-an-active-cardiac-stabilizer/), C).

### 3.3 LV torsion (3D tagged MRI, n=52, ages 21-82)

([Tavakoli & Sahba 2014, PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236), A)

| Age | Layer | Apical rotation | Basal rotation | Peak twist |
|---|---|---|---|---|
| 21-35 | Mid-wall | +6.9 ± 1.6° | −4.8 ± 1.6° | 11.3 ± 2.2° |
| 21-35 | Epicardium | +5.5 ± 1.3° | −4.2 ± 1.8° | 10.4 ± 2.6° |
| 51-65 | Mid-wall | +9.8 ± 1.7° | −7.4 ± 1.8° | 15.7 ± 3.6° |
| >65 | Mid-wall | +10.5 ± 1.3° | −8.0 ± 1.7° | 16.2 ± 3.4° |

- Counter-clockwise (seen from the apex) is positive; the base turns clockwise ([PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236)).
- Overall peak twist range 10-19° for ages 21-80 ([PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236)).
- Another tagged MRI study: net twist 12.6 ± 1.5° at 80% systole (n=10) ([Lorenz 2000](https://scmr.org/wp-content/uploads/2023/12/2000_V2No2_97-108.pdf), uncertain - snippet only).
- The epicardium (what the player sees) twists least: about 10° in young adults ([PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236)).

### 3.4 Respiratory motion

- Whole heart superior-inferior translation per breath: 4.9 ± 1.9 mm (range 2.4-8.0 mm); coronary trees 5.9-6.1 mm 3D RMS ([Shechter 2004, PMC2494710](https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710), A).
- Coronary-to-diaphragm motion ratio: 0.57 ± 0.26 ([patent citing MRI study](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7561909), C). Rule of thumb: 10 mm diaphragm motion → about 7 mm LAD motion ([MRIquestions](https://mriquestions.com/heart-navigators.html), C).
- Note: these are spontaneously breathing, closed-chest values. With an open chest and mechanical ventilation the pattern differs (gap; uncertain). Stop the respiratory component entirely when the game state is "on full CPB, ventilator off".

---

## 4. Blood and bleeding

### 4.1 Viscosity

| Condition | Value | Source | Grade |
|---|---|---|---|
| Hct 40%, 37 °C | about 4 cP | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) | B |
| Hct 30% | about 25% lower than at 40% | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) | B |
| Hct 20% | about 45% lower than at 40% | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) | B |
| Temperature | about +2% per 1 °C of cooling (no primary source given in review) | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) | B |
| Hct 30% at moderate hypothermia | net about 20% lower than normal; fully restored at about 22 °C | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) | B |
| Kinematic viscosity, blood Hct 38% | 2.44 cSt (37 °C), 3.50 cSt (25 °C), 6.07 cSt (6 °C) | [Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf) | A |
| Kinematic viscosity, Hct 20% | 1.26 / 1.65 / 2.83 cSt | [Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf) | A |
| Crystalloid (0%) | 0.85 / 1.10 / 1.63 cSt | [Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf) | A |

Conflict note. The +2%/°C rule predicts about +60-70% from 37 to 6 °C, but Stammers measured a 2.49× ratio (+149%) for whole blood ([Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf)). Also, the paper's "249%" is a ratio, not an increase. For the game, use an exponential fit through the Stammers points (about +3%/°C at Hct 38%), and keep the 4 cP anchor at 37 °C (uncertain blend of two sources).

Suggested function (derived, uncertain): μ(Hct, T) = 4.0 cP × f(Hct) × exp(0.029 × (37 − T)), with f(40%) = 1.0, f(30%) = 0.75, f(20%) = 0.55 ([PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/)) and the exponent fitted to 6.07/2.44 over 31 °C ([Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf)).

### 4.2 Heparin, ACT and protamine (for the coagulation state machine)

| Rule | Value | Class / LOE | Source |
|---|---|---|---|
| Weight-based heparin bolus | reasonable | IIa / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Common initial dose | 300 IU/kg in most centres | - | [PMC7018172](https://pmc.ncbi.nlm.nih.gov/articles/PMC7018172), [European survey via iperfusion](https://iperfusion.org/2026/03/10/) (uncertain - snippet only) |
| ACT before and during CPB | must show adequate anticoagulation; check at regular intervals | I / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| ACT target | >480 s | IIa / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| ACT target, maximally activated / microcuvette devices | >400 s often considered therapeutic | IIa / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Protamine titration to residual heparin | can be beneficial | IIa / B | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Protamine maximum ratio | <2.6 mg per 100 U heparin | IIa / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Common clinical protamine ratio | 1 mg per 100 IU heparin | - | [PMC7018172](https://pmc.ncbi.nlm.nih.gov/articles/PMC7018172) |
| Heparin rebound | low-dose protamine 25 mg/h up to 6 h may be considered; heparin >400 IU/kg can cause rebound | IIb / C | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Heparin resistance (proposed definition) | ACT <480 s after 500 U/kg | - | [search summary](https://iperfusion.org/wp-content/uploads/2024/01/PIIS1538783624000072.pdf) (uncertain - snippet only) |
| Heparin half-life | dose-dependent; about 30 min after 25 IU/kg, about 60 min after 100 IU/kg; 1-2 h at higher doses | - | [PMC9947996 search hit](https://pmc.ncbi.nlm.nih.gov/articles/PMC9947996) (uncertain - snippet only) |
| Baseline (pre-heparin) kaolin ACT | 107-160 s arterial (90% CI, n=79); 89-137 s venous volunteers (n=120) | - | [FDA 510(k) summary](https://fda.innolitics.com/submissions/HE/subpart-h-hematology-kits-and-packages/JBP/K023582) (uncertain - snippet only) |

### 4.3 Bleeding sources and rates

**Measured data found:**
- Needle-hole leak in an ex vivo CPB set-up: 19.8 ± 4.5 mL/min (low needle-to-suture ratio suture) to 57.2 ± 7.2 mL/min (polypropylene) per test anastomosis ([HEMO-SEAL study via search](https://doi.org/10.1016%2fj.athoracsur.2005.02.004), uncertain - snippet only).
- Preclinical ePTFE graft anastomoses: 0.63-1.94 mL/min (about 30× lower; different set-up) (same search, uncertain - snippet only).
- Needle-to-suture ratio 1:1 "greatly reduces" needle-hole bleeding (canine, heparinised) (same search, uncertain).
- Sternal edge: bone wax did not change bleeding in a 94 vs 90 patient study ([Ann Thorac Cardiovasc Surg](https://www.jstage.jst.go.jp/article/atcs/20/3/20_oa.12.02186/_article), uncertain - snippet only). In another cohort, 24-h drainage was 615 ± 304 mL with wax vs 639 ± 285 mL without ([search summary](https://search.bvsalud.org/portal/resource/en/wpr-497249), uncertain - snippet only).
- For small injuries, bleeding rate is set mainly by the wound's resistance; for injuries >300 µm, by the supply vessels' resistance ([conference abstract](https://istina.fnkcrr.ru/conferences/presentations/597573037), uncertain - snippet only).

**Post-operative bleeding grading.** The Universal Definition of Perioperative Bleeding (UDPB) grades bleeding as insignificant, mild, moderate, severe or massive from 12-hour chest-tube loss, transfusions, re-exploration, delayed sternal closure and salvage treatment ([Dyke 2014](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24332097), A). The mL thresholds per class are **UNVERIFIED** in this round (abstract does not list them).

**Physics model for the game (derived, uncertain).** Treat a hole in a pressurised wall as a short orifice: Q = C_d · A · √(2ΔP/ρ), with C_d ≈ 0.6 and ρ ≈ 1,060 kg/m³. The "thin-plate orifice" choice is supported over Poiseuille for short holes ([MMD discussion](https://www.mmdigest.com/Archives/Digests/199903/1999.03.09.06.html), C).

| Injury | Hole size | ΔP | Open-hole estimate |
|---|---|---|---|
| Needle hole (no suture), artery | 0.3 mm | 100 mmHg | about 13 mL/min |
| Puncture / small tear, artery | 1 mm | 100 mmHg | about 140 mL/min |
| Puncture, vein or RA | 1 mm | 8 mmHg | about 40 mL/min |
| Arteriotomy, partly open | 2 mm | 80 mmHg | about 510 mL/min |
| Lost aortic cannula purse-string | 4-5 mm | 80 mmHg | about 2-3 L/min (cap by cardiac output / pump flow) |

(All numbers in this table are my calculations from the formula; they are not measured values. Cap any wound at the upstream flow available, per the conference abstract above.)

---

## 5. Imaging datasets and mesh pipeline

### 5.1 Datasets

| Dataset | Content | Licence / terms | Version / date | Personal non-commercial use? | Attribution / SA / ND | Source |
|---|---|---|---|---|---|---|
| **TotalSegmentator dataset** | 1,939 CT images, 117 structures (adds 291 paediatric CT to earlier 1,228); 37.4 GB | **CC BY 4.0** | v3.0.0, published 2026-09-10 | Yes | Attribution required; no SA; no ND | [Zenodo 6802613](https://zenodo.org/records/6802613) (A) |
| **MM-WHS** | 120 images: 60 CT/CTA + 60 MRI; training 20 CT + 20 MRI with 7 labels (LV 500, RV 600, LA 420, RA 550, LV myocardium 205, ascending aorta 820, pulmonary artery 850) | Signed data-access agreement emailed to organisers; licence text **UNVERIFIED**. The challenge *paper* is CC BY-NC-ND 4.0 (not the data). | Challenge 2017; page current 2026 | Probably yes for research (uncertain) | Citation likely required (UNVERIFIED) | [MM-WHS data page](https://zmiclab.github.io/zxh/0/mmwhs/data.html) (A), [paper PMC6839613](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6839613/) |
| **ImageCAS** | about 1,000 3D CTA, Siemens 128-slice dual-source, coronary labels | **UNVERIFIED** (no licence on GitHub README; Kaggle page not readable) | Kaggle deploy noted 2023-11-01 | Unknown | Unknown | [GitHub](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT), [arXiv](https://arxiv.org/abs/2211.01607) (A) |
| **ASOCA** | 40 CTCA (20 normal, 20 diseased) with voxel labels, centrelines, lumen meshes, calcium scores | UK Data Service deposit: **UK Data Service End User Licence, closed access, owner permission required**. Scientific Data metadata reportedly CC BY 4.0 (uncertain - snippet only). Conflict. | Deposit 2022-11-08, modified 2024-10-02 | Only after approval | Attribution | [UKDS record](https://reshare.ukdataservice.ac.uk/855916/) (A), [arXiv](https://arxiv.org/abs/2211.01859) |
| **Visible Human Project (NLM)** | Male: CT 1 mm, 512×512, 12-bit; MRI 4 mm; cryosection 2048×1216 at 1 mm (0.33 mm XY originals; 70 mm film at 4096×2700). Female: cryosection at 0.33 mm, >5,000 images, about 40 GB | Since July 2019 the NLM Data License was replaced by NLM Terms and Conditions; no registration for FTP | 2019 terms | Yes | Must credit "Courtesy of the U.S. National Library of Medicine"; redistributors must keep data current or say it is not current | [NLM getting data](https://www.nlm.nih.gov/research/visible/getting_data.html), [NLM terms](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html), [IDC collection](https://portal.imaging.datacommons.cancer.gov/collections/nlm_visible_human_project) (A) |

### 5.2 Tools

| Tool | Licence | Version / date | Non-commercial personal use | Notes | Source |
|---|---|---|---|---|---|
| **TotalSegmentator** (code) | Apache-2.0 | 2.18.0, 2026-08-12 | Yes | "total" task (open) includes heart, aorta, pulmonary vein, LA appendage, SVC, IVC; "trunk_cavities" includes pericardium | [PyPI](https://pypi.org/project/TotalSegmentator/), [GitHub](https://github.com/wasserth/TotalSegmentator) (A) |
| TotalSegmentator **licensed sub-tasks** | Free licence for non-commercial use; commercial licence from author | same | Yes, after free licence | heartchambers_highres (myocardium, LA, LV, RA, RV, aorta, pulmonary artery), coronary_arteries, aortic_sinuses (LVOT and three cusps) | [GitHub](https://github.com/wasserth/TotalSegmentator) (A) |
| **3D Slicer** | "3D Slicer Contribution and Software License Agreement" v1.0 (2005), BSD-style, no use restriction; keep attributions; research only, not for clinical use | Stable 5.12.4 (r34645, builds 2026-09-09/10); preview 5.13.0 (2026-11-03) | Yes | Segment Editor, model export (STL/OBJ) | [slicer.org](https://www.slicer.org/), [download](https://download.slicer.org/), [License.txt](https://raw.githubusercontent.com/Slicer/Slicer/main/License.txt) (A) |
| **MONAI** | Apache-2.0 | 1.6.1, 2026-09-27 | Yes | Training own segmentation if needed | [PyPI](https://pypi.org/project/monai/), [GitHub](https://github.com/Project-MONAI/MONAI) (A) |
| Blender, MeshLab | Not re-verified in this report (see research 03/07) | - | - | Retopology, UVs, sculpt detail | - |

### 5.3 Recommended pipeline (scan → game mesh)

1. Download 2-4 contrast CT cases from the TotalSegmentator dataset (CC BY 4.0) ([Zenodo](https://zenodo.org/records/6802613)). Pick cases with cardiac contrast.
2. Run TotalSegmentator `total` (open) for heart, aorta, great veins, sternum/ribs, and `heartchambers_highres` + `coronary_arteries` after getting the free non-commercial licence ([GitHub](https://github.com/wasserth/TotalSegmentator)).
3. Load labels in 3D Slicer 5.12.4; fix errors in Segment Editor; smooth; export each structure as a surface (STL/OBJ) ([slicer.org](https://www.slicer.org/)).
4. Check sizes against section 1 tables (e.g., LM 4-4.5 mm, LAD 3.3-3.7 mm proximal, LV wall 6-10 mm). Scale the patient if needed.
5. In Blender: retopologise to game budgets, build a tetrahedral cage for FEM/XPBD, add wall thickness to vessels using section 1.6 values, and paint fat into AV/interventricular grooves (section 1.7).
6. Use Visible Human cryosection colour (credit NLM) as reference for tissue colour and fat texture ([NLM terms](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html)).
7. Avoid ASOCA unless approval is granted; avoid ImageCAS until its licence is confirmed.

---

## 6. Recommended default simulation parameters

| Parameter | Default | Range for randomisation / difficulty | Source |
|---|---|---|---|
| Heart weight (male / female) | 330 g / 270 g | 233-383 g (male) | [Molina 2012](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983); female value derived (uncertain) |
| LV wall thickness | 9 mm (M), 7.5 mm (F) | 6-10 mm (M), 6-9 mm (F) | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086), [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) |
| RV wall thickness | 3 mm | 1-5 mm | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) |
| LV EDV / ESV (3D mesh, CMR) | 155 / 55 mL (M); 123 / 43 mL (F) | ± 2 SD | [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/) |
| LV EF (displayed) | 60% | 52-72% (M), 54-74% (F) | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) |
| Aortic annulus | 26 mm (M), 23 mm (F) | ± 3 mm | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086) |
| Ascending aorta | 30 mm (M), 27 mm (F) | up to 41 mm normal on CT | [Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086), [Wolak (snippet)](https://cris.bgu.ac.il/en/publications/aortic-size-assessment-by-noncontrast-cardiac-computed-tomography-2/) |
| LM / prox LAD / dist LAD diameter | 4.5 / 3.7 / 1.9 mm | women −9% | [Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570) |
| Graft target diameter | 2.0 mm | 1.0-3.0 mm; <1.5 mm = poor target | [PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415) |
| LAD length / LM length | 105 / 12.6 mm | 33-154 / 3.4-19 mm | [Asar 2023](https://journals.innovareacademics.in/index.php/ajpcr/article/download/48400/29246) |
| Dominance | Right | R 85%, L 10%, Co 5% | [Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546) |
| IMA diameter / wall | 2.2 mm / 0.3 mm | 1.9-2.6 mm / 0.18-0.43 mm | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) |
| SVG diameter / wall | 4 mm / 0.4 mm | 3.1-8.5 mm / 0.18-0.65 mm | [Otsuka 2013](https://annalscts.com/article/view/2416/pdf) |
| LIMA usable length | 17 cm pedicled, 19 cm skeletonised | 16-20 cm | [TGKDC (snippet)](https://tgkdc.dergisi.org/abstract.php?id=884) |
| Sternum length / thickness | 154 mm / 9 mm (M); 133 / 8 mm (F) | ± 1 SD | [Ateşoğlu 2018](https://journals.viamedica.pl/folia_morphologica/article/download/FM.a2018.0002/42756) |
| Pericardium thickness | 1 mm | 0.5-2 mm | [PMC4929280](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280) |
| EAT over RV / LAD groove | 5 mm | 1-15 mm | [PMC5779180](https://pmc.ncbi.nlm.nih.gov/articles/PMC5779180) |
| Myocardium HO parameters | average set (a 0.28, b 8.82, a_f 18.1, b_f 16.5, a_s 3.0, b_s 9.5, a_fs 0.4, b_fs 10.9) | human fit set as "soft" variant | [PMC6096751](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751), [PMC6647490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/) |
| Peak active fibre stress | 60 kPa | 30-120 kPa (tune to EF) | [Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf) |
| Needle puncture force, heart wall | 1.1 N | 0.85-1.4 N (speed-dependent) | [PMC3051196](https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196) |
| Needle force on vessel wall | 0.3 N (uncertain; thinner wall than myocardium) | 0.1-0.6 N | **UNVERIFIED** (gap) |
| Suture pull-through (tear-out), IMA / SV | 1.4 / 1.9 N | 0.9-2.5 N | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094), [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/) |
| 6-0 polypropylene break | 4.3 N (knotted 3.1 N) | - | [snippet](https://latam-cl.demo.elsevierpure.com/fr/publications/effect-of-force-on-anastomotic-suture-line-disruption-after-carot) (uncertain) |
| Graft burst pressure (failure event) | IMA 3,200 mmHg; SV 1,600 mmHg | ± 1 SD | [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094) |
| Sternal retractor force | 220 N typical, 350 N max | 159-494 N max | [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560) |
| LAD cardiac displacement / peak velocity | 9.6 mm / 47.5 mm/s | ± 1 SD | [PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264) |
| RCA mid displacement / peak velocity | 26.3 mm / 130.7 mm/s | ± 1 SD | [PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264) |
| Stabiliser motion reduction | 80% | 75-81% | [HSF (snippet)](https://journal.hsforum.com/index.php/HSF/article/view/934) |
| Respiratory heart shift (closed chest) | 5 mm SI | 2.4-8 mm | [PMC2494710](https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710) |
| LV peak twist (epicardial) | 10.4° (young) | 10-19° | [PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236) |
| Blood viscosity at 37 °C, Hct 40% | 4 cP | ×0.75 at Hct 30%; ×0.55 at Hct 20% | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/) |
| Viscosity temperature factor | exp(0.029 × (37 − T)) | 2-3% per °C | [PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/), [Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf) (derived) |
| Heparin bolus | 300 IU/kg | 300-400 IU/kg | [PMC7018172](https://pmc.ncbi.nlm.nih.gov/articles/PMC7018172) |
| ACT safe-to-start-CPB threshold | 480 s | 400 s on maximally activated device | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Baseline ACT | 120 s | 89-160 s | [FDA 510(k) (snippet)](https://fda.innolitics.com/submissions/HE/subpart-h-hematology-kits-and-packages/JBP/K023582) |
| Protamine | 1 mg / 100 U | max 2.6 mg / 100 U | [STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589) |
| Bleeding flow law | Q = 0.6·A·√(2ΔP/ρ) | C_d 0.5-0.7 | derived (section 4.3) |

---

## Game hooks

How each finding becomes a mechanic, data value or rule.

1. **Patient generator.** Sample sex, then BSA, then scale all anatomy (section 6). Apply −9% coronary diameter for women ([Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570)). Roll dominance 85/10/5 ([Folia Morphol](https://journals.viamedica.pl/folia_morphologica/article/view/86546)); in left-dominant hearts the PDA comes from the LCx, which changes which targets exist.
2. **Target vessel quality.** Each grafting target gets a diameter (1.0-3.0 mm). Below 1.5 mm, show "poor run-off" and reduce the graft patency score ([PMC6457415](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415)). Above 2.0 mm, give a patency bonus (uncertain VA study data).
3. **Fat dissection mini-task.** The LAD lies under 2-8 mm of groove fat ([PMC5779180](https://pmc.ncbi.nlm.nih.gov/articles/PMC5779180)); obese patients have more. Player must expose the artery before the arteriotomy.
4. **Conduit choice.** IMA (2.2 mm, stiff, high burst pressure) vs SVG (4 mm, compliant, lower burst pressure) ([Otsuka 2013](https://annalscts.com/article/view/2416/pdf), [König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094)). Size mismatch between a 4 mm SVG and a 2 mm target is a visible "hood" design challenge.
5. **LIMA length budget.** Pedicled LIMA reaches about 17 cm; skeletonising adds about 2-3 cm but takes longer ([TGKDC snippet](https://tgkdc.dergisi.org/abstract.php?id=884)). If the chosen target is too far, the game shows "graft under tension".
6. **Needle physics.** Haptic or visual resistance peaks near 1.1 N then drops at puncture ([PMC3051196](https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196)). Slow pushes deflect tissue more before puncture (up to 7 mm at 100 mm/s with a trocar tip ([PMC3021974](https://pmc.ncbi.nlm.nih.gov/articles/PMC3021974))); fast, confident throws are cleaner.
7. **Suture tear-out.** If the player's thread tension at one stitch exceeds about 1.4 N (IMA) or 1.9 N (SVG), the stitch cuts through ([König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094), [PMC4753638](https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/)). If it exceeds about 3 N on 6-0, the thread breaks (uncertain). Grabbing the suture with forceps lowers its strength ([snippet](https://scilit.net/publications/0b06deed15f3892aaf9953d1c115129e)).
8. **Sternal retractor.** Opening speed and width map to force; >350 N risks a "rib fracture / brachial plexus stretch" complication flag ([Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560), [Saggio 2017](https://www.scitepress.org/Papers/2017/61113/61113.pdf)). Women's sterna need less force.
9. **Beating heart difficulty (OPCAB mode).** The LAD target moves about 10 mm per beat at about 48 mm/s ([PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264)). A stabiliser cuts this by about 80% ([HSF snippet](https://journal.hsforum.com/index.php/HSF/article/view/934)). RCA targets move 2-3× more and are the "hard" level. Use the mid-diastolic quiet window (about 70% of the cycle) as the best moment to place a stitch ([Johnson 2004 snippet](https://scmr.org/wp-content/uploads/2023/12/2004_V6_No_3_663-73.pdf)).
10. **Heart twist animation.** Rotate the apex +5-7° and the base −4-5° in systole for a young adult; more for older patients ([PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236)).
11. **Ventilation coupling.** Add 5 mm SI heart shift with each breath while the ventilator runs ([PMC2494710](https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710)); freeze it on full bypass.
12. **Coagulation state machine.** States: baseline (ACT about 120 s) → heparinised (300 IU/kg; target >480 s) → on CPB (recheck ACT periodically) → protamine (1 mg/100 U, cap 2.6) → reversed ([STS/SCA/AmSECT 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589)). Starting CPB below 480 s triggers a clotting-in-circuit risk event. Over-dosing protamine raises bleeding.
13. **Bleeding renderer.** Each wound has size, local pressure and coagulation factor. Flow uses the orifice law (section 4.3), scaled by heparin state and capped by available flow. Needle holes ooze (tens of mL/min per anastomosis, uncertain) until protamine and time seal them.
14. **Cold blood is thicker.** Viscosity rises 2-3% per °C of cooling and falls with haemodilution ([PMC9918189](https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/), [Stammers 2003](https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf)). Use this in the perfusion pressure model and in the visual flow speed of blood.
15. **Graft failure event.** If line pressure in a graft passes its burst pressure (IMA about 3,200 mmHg, SV about 1,600 mmHg ([König 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094))), rupture; this should only happen with a gross error (for example, a flushing syringe), so it works as a "teaching moment" event.
16. **Unit-test the solver.** Reproduce the Land 2015 ellipsoid benchmarks (C = 10 kPa inflation at 10 kPa; active 60 kPa at 15 kPa) before tuning the real heart ([Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf)).

---

## Key claims and evidence

| # | Claim | Source URL | Grade |
|---|---|---|---|
| 1 | Healthy young men: heart weight 331 ± 56.7 g; 95% reference range 233-383 g | https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983 | A |
| 2 | LV mass by CMR 121 ± 28 g (men), 83 ± 21 g (women) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/ | A |
| 3 | Normal LV septal/posterior wall 0.6-1.0 cm (men), 0.6-0.9 cm (women) | https://academic.oup.com/ehjcimaging/article/16/3/233/2400086 | A |
| 4 | RV wall 3 ± 1 mm (1-5 mm); >5 mm abnormal | https://academic.oup.com/ehjcimaging/article/16/3/233/2400086 | A |
| 5 | LV EDV (echo) 106 ± 22 mL men, 76 ± 15 mL women | https://academic.oup.com/ehjcimaging/article/16/3/233/2400086 | A |
| 6 | Aortic annulus 26 ± 3 mm (men), 23 ± 2 mm (women); proximal ascending aorta 30 ± 4 / 27 ± 4 mm | https://academic.oup.com/ehjcimaging/article/16/3/233/2400086 | A |
| 7 | LM 4.5 ± 0.5 mm, proximal LAD 3.7 ± 0.4 mm, distal LAD 1.9 ± 0.4 mm; women -9% | https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570 | A |
| 8 | Dominance: right 85.5%, left 9.7%, co-dominant 4.8% (n=4,000) | https://journals.viamedica.pl/folia_morphologica/article/view/86546 | A |
| 9 | Target coronary diameter 2.14 ± 0.52 mm; target <1.5 mm is an occlusion risk factor | https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415 | A |
| 10 | IMA 1.9-2.6 mm (wall 180-430 µm); SVG 3.1-8.5 mm (wall 180-650 µm) | https://annalscts.com/article/view/2416/pdf | A |
| 11 | Sternum total length 154.1 ± 13.1 mm (M) and 133.1 ± 11 mm (F); body thickness about 8-9 mm | https://journals.viamedica.pl/folia_morphologica/article/download/FM.a2018.0002/42756 | A |
| 12 | Pericardial layers 0.5-1.0 mm; CT normal <2 mm; fluid 20-25 mL | https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280 | B |
| 13 | HO 2009 parameters a=0.059 kPa, b=8.023, a_f=18.472 kPa, b_f=16.026, a_s=2.481 kPa, b_s=11.120, a_fs=0.216 kPa, b_fs=11.436 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751 | A |
| 14 | Benchmark active fibre stress Ta = 60 kPa with 15 kPa endocardial pressure | https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf | A |
| 15 | Burst pressure: IMA 3,196 ± 1,264 mmHg, SV 1,599 ± 877 mmHg | https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094 | A |
| 16 | Suture retention 1.72 N (ITA) and 1.92 N (SV); compliance 11.5 and 25.6%/100 mmHg | https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/ | B |
| 17 | Needle rupture force in porcine heart 1.37 N at 1 mm/s falling to 0.88 N at 100 mm/s | https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196 | A |
| 18 | Sternal retractor max total force 349.4 ± 77.9 N; mean first retraction about 223-226 N | https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560 | A |
| 19 | LAD (5 cm) cardiac displacement 9.6 ± 1.3 mm, peak velocity 47.5 ± 9.3 mm/s; RCA mid 26.3 mm, 130.7 mm/s | https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264 | A |
| 20 | Whole-heart respiratory SI shift 4.9 ± 1.9 mm | https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710 | A |
| 21 | LV peak twist 10-19° (ages 21-80); young epicardial twist 10.4 ± 2.6° | https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236 | A |
| 22 | Blood viscosity about 4 cP at Hct 40%; -25% at Hct 30%; +2% per °C cooling | https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/ | B |
| 23 | Whole blood kinematic viscosity 2.44 cSt (37 °C) → 6.07 cSt (6 °C) | https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf | A |
| 24 | ACT >480 s during CPB is reasonable (IIa); >400 s on maximally activated devices; protamine <2.6 mg/100 U | https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 | A |
| 25 | TotalSegmentator dataset v3.0.0 (2026-09-10) is CC BY 4.0, 1,939 CT, 117 structures | https://zenodo.org/records/6802613 | A |
| 26 | TotalSegmentator code Apache-2.0, v2.18.0 (2026-08-12); heartchambers_highres and coronary_arteries need a (free non-commercial) licence | https://github.com/wasserth/TotalSegmentator | A |
| 27 | ASOCA data on UK Data Service is closed access under the End User Licence | https://reshare.ukdataservice.ac.uk/855916/ | A |
| 28 | Visible Human: licence replaced by NLM Terms (July 2019); credit "Courtesy of the U.S. National Library of Medicine" | https://www.nlm.nih.gov/databases/download/terms_and_conditions.html | A |
| 29 | 3D Slicer 5.12.4 stable; BSD-style licence, research-only, no use restrictions | https://download.slicer.org/ | A |
| 30 | XPBD compliance is inverse stiffness, α̃ = α/Δt² | https://matthias-research.github.io/pages/publications/XPBD.pdf | A |

---

## Sources

1. Lang RM et al. 2015, Recommendations for cardiac chamber quantification (EHJ-CVI) - https://academic.oup.com/ehjcimaging/article/16/3/233/2400086 - LV/RV/LA dimensions, volumes, wall thickness, LV mass, aortic root.
2. ASE "WFTF" chamber quantification summary - https://asecho.org/wp-content/uploads/2018/08/WFTF-Chamber-Quantification-Summary-Doc-Final-July-18.pdf - RV >41 mm and wall >5 mm abnormal; LA volume index 16-34 mL/m²; RA area ≤18 cm².
3. Kawel-Boehm N et al. 2020, CMR reference ranges - https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/ - CMR volumes, LV mass, segmental wall thickness, atrial volumes.
4. Molina DK, DiMaio VJ 2012, Normal organ weights in men: the heart - https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/22182983 (PubMed https://pubmed.ncbi.nlm.nih.gov/22182983/) - heart weight 331 g, range 233-383 g.
5. Heart weight autopsy literature (search hit) - https://core.ac.uk/download/77167029.pdf - 426/351 g reference group (snippet only).
6. Vanhaebost 2014 Lausanne study - https://serval.unil.ch/notice/serval:BIB_85AA3C49A5A5 - BSA best predictor (snippet only).
7. Dodge JT et al. 1992, Lumen diameter of normal human coronary arteries (Circulation) - https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570 - coronary diameters, sex and dominance effects.
8. Indian QCA normal coronary dimensions (n=229) - https://pmc.ncbi.nlm.nih.gov/articles/PMC5560873 - LM/LAD/LCx/RCA diameters.
9. Nepal JIOM normal coronary dimensions (n=100) - https://jiomnepal.edu.np/index.php/jiomnepal/article/view/1276 - mid/distal segment diameters (snippet only).
10. Asar V et al. 2023, Morphometric analysis of coronary arteries (60 hearts) - https://journals.innovareacademics.in/index.php/ajpcr/article/download/48400/29246 - coronary lengths.
11. Folia Morphologica 2023, coronary dominance in 4,000 angiograms - https://journals.viamedica.pl/folia_morphologica/article/view/86546 - dominance percentages.
12. Weill Cornell record, dominance and calcification (CT) - https://vivo.weill.cornell.edu/display/pubid34171741 - 91.7/8/1.3% (snippet only).
13. DOAJ, Indian dominance study (n=102) - https://doaj.org/article/0acf800055a0450f9d71e045d7886d7b - regional variation (snippet only).
14. Zhang et al. 2021, CT aortic root in 1,286 healthy adults (IJGM) - https://doi.org/10.2147/IJGM.S312439 - BSA-indexed annulus, ostium heights.
15. Wolak et al., Aortic size by non-contrast cardiac CT - https://cris.bgu.ac.il/en/publications/aortic-size-assessment-by-noncontrast-cardiac-computed-tomography-2/ - ascending aorta 33 ± 4 mm, ULN 41 mm (snippet only).
16. Contrast cardiac CT aorta norms - https://pmc.ncbi.nlm.nih.gov/articles/PMC3766427 - sex-specific ascending aorta (snippet only).
17. Frontiers Cardiovasc Med 2022 annulus data - https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.1011931/epub - mitral annulus (snippet only).
18. Houston Methodist, tricuspid annulus reference ranges - https://scholars.houstonmethodist.org/en/publications/reference-ranges-of-tricuspid-annulus-geometry-in-healthy-adults-/ - tricuspid annulus (snippet only).
19. Otsuka F et al. 2013, Why is the mammary artery so special (Ann Cardiothorac Surg) - https://annalscts.com/article/view/2416/pdf - IMA/SVG diameters and wall thickness.
20. SVG and target vessel diameter study - https://pmc.ncbi.nlm.nih.gov/articles/PMC6457415 - target 2.14 mm; <1.5 mm risk.
21. VA cooperative study record - https://experts.arizona.edu/en/publications/long-term-patency-of-saphenous-vein-and-left-internal-mammary-art/ - patency by target size (snippet only).
22. LITA skeletonisation length study - https://tgkdc.dergisi.org/abstract.php?id=884 - 16.8 vs 18.9 cm (snippet only).
23. ICVTS best evidence topic on skeletonisation - https://academic.oup.com/icvts/article/4/6/577/745846 - +3 cm length (snippet only).
24. Ateşoğlu S et al. 2018, Sternum by MDCT (Folia Morphol) - https://journals.viamedica.pl/folia_morphologica/article/download/FM.a2018.0002/42756 - sternum dimensions.
25. Pericardium imaging review - https://pmc.ncbi.nlm.nih.gov/articles/PMC4929280 - layer thickness, fluid volume.
26. Iacobellis EAT review - https://pmc.ncbi.nlm.nih.gov/articles/PMC5779180 - epicardial fat thickness and distribution.
27. HO parameter estimation paper (Table 2) - https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751 - HO 2009 and other parameter sets.
28. AIC-based HO model reduction - https://pmc.ncbi.nlm.nih.gov/articles/PMC6647490/ - human (Sommer) fitted parameters; HO law form.
29. Sommer G et al. 2015 human ventricular myocardium (Acta Biomater) - https://doi.org/10.1016/j.actbio.2015.06.031 - source of human test data.
30. Land S et al. 2015, cardiac mechanics benchmark (Proc R Soc A) - https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf - Ta 60 kPa, Guccione parameters, benchmark geometry.
31. Thunes JR et al., ascending aorta failure modelling - https://pmc.ncbi.nlm.nih.gov/articles/PMC8059307 - matrix stress, Pichamuthu cohorts.
32. Duprey A et al. 2016 - https://hal.archives-ouvertes.fr/hal-01380216/file/2016_actabio_duprey_auteur.pdf - aortic strength range (snippet only).
33. Khanafer et al. 2011 (PubMed) - https://pubmed.ncbi.nlm.nih.gov/21616506 - aneurysm moduli (snippet only).
34. König G et al. 2009, tissue-engineered vessel vs native vessels - https://pmc.ncbi.nlm.nih.gov/articles/PMC2758094 - burst pressure, suture retention method.
35. Tissue-engineered vascular graft review 2015 - https://pmc.ncbi.nlm.nih.gov/articles/PMC4753638/ - ITA/SV burst, retention, compliance.
36. Holzapfel GA et al. 2005, layer-specific coronary properties - https://doi.org/10.1152/ajpheart.00934.2004 (via https://scite.ai/authors/gerhard-holzapfel-wmX1ny) - adventitia UTS (snippet only).
37. Needle insertion into porcine heart, rate dependence - https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196 - rupture force vs speed.
38. Needle rupture mechanics in cardiac tissue - https://pmc.ncbi.nlm.nih.gov/articles/PMC3021974 - deflection, stiffness fits, saturation speed.
39. Aigner P et al. 2013, sternal force distribution (JTCVS) - https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560 - retractor forces.
40. Saggio G et al. 2017, instrumented sternal retractor - https://www.scitepress.org/Papers/2017/61113/61113.pdf - retractor force details and literature values.
41. Sternal closure biomechanics (J Cardiothorac Surg 2009) - https://link.springer.com/article/10.1186/1749-8090-4-19 - wire forces (snippet only).
42. Landymore suture line disruption study - https://latam-cl.demo.elsevierpure.com/fr/publications/effect-of-force-on-anastomotic-suture-line-disruption-after-carot - 6-0 suture strength (snippet only).
43. Suture handling study - https://scilit.net/publications/0b06deed15f3892aaf9953d1c115129e - forceps damage to sutures (snippet only).
44. Shechter G et al. 2006, displacement and velocity of coronary arteries - https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264 - cardiac and respiratory coronary motion.
45. Shechter G et al. 2004, respiratory motion of the heart - https://pmc.ncbi.nlm.nih.gov/articles/PMC2494710 - respiratory displacement.
46. Tavakoli V, Sahba N 2014, LV twist by 3D tagged MRI - https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236 - twist by age and layer.
47. Lorenz CH et al. 2000 (JCMR) - https://scmr.org/wp-content/uploads/2023/12/2000_V2No2_97-108.pdf - net twist 12.6° (snippet only).
48. Johnson KR et al. 2004 (JCMR) - https://scmr.org/wp-content/uploads/2023/12/2004_V6_No_3_663-73.pdf - mid-diastolic rest period (snippet only).
49. MRIquestions, heart navigators - https://mriquestions.com/heart-navigators.html - diaphragm-to-coronary ratio (C).
50. Off-pump stabiliser quantification (Heart Surgery Forum) - https://journal.hsforum.com/index.php/HSF/article/view/934 - motion reduction (snippet only).
51. Systemic pressure on CPB review (J Clin Med 2023) - https://pmc.ncbi.nlm.nih.gov/articles/PMC9918189/ - viscosity vs Hct and temperature.
52. Stammers AH et al. 2003 (JECT) - https://ject.edpsciences.org/articles/ject/pdf/2003/01/ject2003351p104.pdf - measured viscosity table.
53. STS/SCA/AmSECT 2018 anticoagulation during CPB guideline - https://pmc.ncbi.nlm.nih.gov/articles/PMC5850589 - ACT, heparin, protamine rules.
54. Heparin dosing by body weight RCT (2018) - https://pmc.ncbi.nlm.nih.gov/articles/PMC7018172 - 300 IU/kg common; 1:1 protamine.
55. Dyke C et al. 2014, Universal definition of perioperative bleeding - https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24332097 - UDPB structure.
56. FDA 510(k) ACT device summary - https://fda.innolitics.com/submissions/HE/subpart-h-hematology-kits-and-packages/JBP/K023582 - baseline ACT ranges (snippet only).
57. Bone wax trial (Ann Thorac Cardiovasc Surg) - https://www.jstage.jst.go.jp/article/atcs/20/3/20_oa.12.02186/_article - sternal bleeding (snippet only).
58. TotalSegmentator GitHub - https://github.com/wasserth/TotalSegmentator - tasks, licences.
59. TotalSegmentator PyPI - https://pypi.org/project/TotalSegmentator/ - version 2.18.0.
60. TotalSegmentator dataset (Zenodo) - https://zenodo.org/records/6802613 - CC BY 4.0, v3.0.0.
61. MM-WHS data page - https://zmiclab.github.io/zxh/0/mmwhs/data.html - image counts, labels, access process.
62. ImageCAS GitHub - https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT - access, no licence stated.
63. ASOCA UK Data Service record - https://reshare.ukdataservice.ac.uk/855916/ - licence, access conditions.
64. NLM Visible Human getting data - https://www.nlm.nih.gov/research/visible/getting_data.html - data specs, 2019 terms change.
65. NLM terms and conditions - https://www.nlm.nih.gov/databases/download/terms_and_conditions.html - acknowledgement wording.
66. 3D Slicer site / download / licence - https://www.slicer.org/ ; https://download.slicer.org/ ; https://raw.githubusercontent.com/Slicer/Slicer/main/License.txt - licence and version.
67. MONAI PyPI - https://pypi.org/project/monai/ - version 1.6.1, Apache-2.0.
68. Macklin M, Müller M, Chentanez N 2016, XPBD - https://matthias-research.github.io/pages/publications/XPBD.pdf - compliance definition.
69. Pericardium tensile tests (Biomed Tech 2013) - https://www.degruyterbrill.com/document/doi/10.1515/bmt-2013-4095/pdf - pericardium UTS (snippet only).
70. Kemper AR thesis, rib cortical bone - https://vtechworks.lib.vt.edu/bitstream/10919/43709/1/KemperThesis.pdf - bone modulus/strength (snippet only).

---

## Summary

### Key findings
- Good primary data exist for chamber sizes, wall thickness, valve/aortic root size, coronary lumen diameters, coronary motion and LV twist. These can be used directly ([Lang 2015](https://academic.oup.com/ehjcimaging/article/16/3/233/2400086), [Kawel-Boehm 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7734766/), [Dodge 1992](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1535570), [PMC2396264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2396264), [PMC3996236](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996236)).
- Myocardium has well-documented HO parameters, and a benchmark active stress of 60 kPa gives a sane starting point ([PMC6096751](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096751), [Land 2015](https://eprints.whiterose.ac.uk/93701/1/20150641.full.pdf)).
- Failure data for grafts (burst pressure, suture retention) are solid; failure data for aorta, coronary layers, pericardium, skin, fat and sternum are mostly from snippets or proxies and need checking.
- Measured surgical interaction forces: needle puncture of heart wall (about 1 N) and sternal retraction (about 220-350 N) are well sourced ([PMC3051196](https://pmc.ncbi.nlm.nih.gov/articles/PMC3051196), [Aigner 2013](https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/24075560)). Forceps grasp forces were not found.
- Blood viscosity and anticoagulation rules are well sourced; bleeding *rates* from specific surgical wounds are poorly documented, so a physics orifice model with calibration is the practical approach.
- The cleanest licence path for meshes is TotalSegmentator dataset (CC BY 4.0) + code (Apache-2.0) + 3D Slicer (BSD-style); ASOCA is closed access and ImageCAS has no stated licence ([Zenodo](https://zenodo.org/records/6802613), [UKDS](https://reshare.ukdataservice.ac.uk/855916/), [ImageCAS GitHub](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT)).

### Recommendations
1. Adopt the section 6 table as the first data file (`anatomy_defaults.json`), with `source` and `grade` fields per value.
2. Build two reference patients (male, female) and a variant generator (dominance, fat, target size).
3. Use HO (average set) offline to generate reference stress-strain curves; fit the real-time XPBD/Neo-Hookean model to those curves, not to single moduli.
4. Unit-test the soft-body solver against the Land 2015 benchmark before tuning gameplay feel.
5. Use TotalSegmentator + 3D Slicer for meshes; request the free non-commercial licence for heart chambers and coronaries; credit NLM for any Visible Human imagery.
6. Implement bleeding as orifice flow × coagulation factor, capped by upstream flow; tune needle-hole ooze to tens of mL/min per anastomosis.
7. Re-check every value graded C (and every "UNVERIFIED") before it drives a scoring rule.

### Open questions (gaps)
- Atrial wall thickness; branch (diagonal, OM, PDA) normal diameters; total SVG harvest length.
- UDPB mL thresholds per bleeding class; measured bleeding rates for cannulation sites and arteriotomies.
- Human ascending aorta UTS in MPa (Pichamuthu 2013 full text); coronary intima/media UTS values.
- Needle insertion force into coronary/vessel wall (only myocardium found); forceps grasp forces; USP knot-pull minimums for 4-0 to 7-0.
- Sternum-specific bone properties and wire cut-through force.
- Open-chest, mechanically ventilated heart motion (all motion data are closed-chest).
- ImageCAS and MM-WHS data licences; ASOCA licence conflict (UKDS End User Licence vs reported CC BY 4.0).
- Mooney-Rivlin parameter sets for cardiac tissues (none verified).
- The web-search budget ran out during this research. More searching could close several of these gaps in a follow-up.
