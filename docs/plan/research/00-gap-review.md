# Final gap and consistency review

Reviewed: **2026-11-03**. This is the coordinating agent's internal document/evidence review. The separately assigned critic stopped with a workspace credit-limit error, so this is **not an independent review**, a clinical sign-off, a legal opinion, or a runtime evaluation. All seven research reports and six integrated design documents were available for this review.

## High-impact source spot checks

The coordinating review independently reopened the following primary pages after the reports were written:

| Check | Evidence | Disposition |
|---|---|---|
| BodyParts3D archive rights changed | [Official license](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html) | New archive acquisition is the selected route; package provenance remains an import gate |
| Unreal/content compatibility restriction | [Epic EULA §6(c)](https://www.unrealengine.com/eula/unreal) | ShareAlike anatomy and the GPL bridge are excluded from the baseline |
| Pulse extracorporeal scope and limitations | [ECMO methodology](https://pulse.kitware.com/_extracorporeal_membrane_oxygenation_methodology.html) | Retain the CPB experiment; no ready surgical-bypass claim |
| Clinical teaching pages conflict | [AATS fundamentals](https://www.aats.org/tsra-primer-cardiopulmonary-bypass-fundamentals), [troubleshooting](https://www.aats.org/tsra-primer-cpb-troubleshooting) | Conflict in anticoagulation teaching details confirmed; no universal executable dose chosen |
| Touch Surgery cardiac evidence scope | [Brewer et al., PMID 27568126](https://pubmed.ncbi.nlm.nih.gov/27568126/) | Cognitive outcome distinguished from manual surgical performance |
| OSATS study identity and relevance | [Martin et al., PMID 9052454](https://pubmed.ncbi.nlm.nih.gov/9052454/) | Published assessment evidence does not validate this game's automated metrics |

The research reports contain the detailed findings and access limitations. These checks validate citation alignment for selected claims, not every statement in the literature or biological fidelity of a future implementation.

## Contradictions found and resolved

1. **Backend decision:** an early integrated draft called the custom reduced model the baseline, while physiology research recommended evaluating Pulse first. The integrated design now consistently uses Pulse as the first experiment and a custom backend only after an explicit failed-capability/scope decision. Analytical fixtures remain useful verification tools.
2. **Units:** geometry/SI language could conflict with physiology's practical units. Architecture now defines geometry units separately and requires typed physiological quantities with explicit conversions.
3. **Scope versus realism:** the full-case ambition exceeded the first interaction milestone. The plan now separates slice, assisted full-case alpha, reviewed desktop release, and later unrestricted interaction/VR work.
4. **Licenses versus engine:** historical ShareAlike recommendations and the Unreal preference were incompatible without further rights. The baseline uses direct permissive/original candidates, while conflicting or uncertain assets remain blocked.
5. **Schedule:** year-based aspirations and task estimates needed reconciliation. The roadmap provides a summed 47–84-week base estimate and explicit contingency/staffing assumptions rather than promising a full simulator in a few months.
6. **Validation language:** face plausibility, numerical verification, clinical content review and transfer studies are now separate. No external expert review is claimed.
7. **Repository status:** the old skeleton said no code existed. The pre-existing Python example is acknowledged and unchanged. Initial upload failures are recorded as historical and resolved after access restoration.
8. **Research prompts:** the old prompts requested precise dosing/timing without sufficient context. Updated evidence rules supersede those assumptions while retaining the historical topic brief.

## Remaining gaps and assigned gates

| Gap | Owner / gate | Effect on the plan |
|---|---|---|
| Exact fictional patient, graft map and local protocol | Clinical/design roles, M1 | Needed before clinical rules are implemented |
| Specialist reviewer availability | Producer, M1 | No “clinically reviewed” milestone without actual review |
| Source geometry has not been downloaded or inspected | Technical artist, M1–M2 | Asset license eligibility is not anatomy/interaction approval |
| Pulse surgical CPB behavior is untested | Simulation developer + perfusion/anesthesia review, M2 | May require custom modeling cost or smaller scope |
| Tissue mechanics, puncture and knot fidelity | Interaction developer + surgeon review, M2–M3 | First release uses explicitly bounded/assisted interaction |
| Clinical timing and parameter envelopes | Clinical leads, before assessment enabling | No guessed scoring thresholds or dose files |
| Hardware, budget and weekly availability | Owner/producer, before implementation commitments | Performance and dates remain assumptions |
| Assessment reliability and educational effectiveness | Assessment/research lead, later study | Descriptive feedback only; no competence credential |
| Full clinical data, media and measurement rights | Asset/research leads, acquisition gate | Synthetic cases and cleared references remain default |
| Arbitrary surgery, VR and haptics | Separate future feasibility tracks | Not required for initial desktop release |

These gaps do not prevent a concrete planning handoff. They prevent overstating what the future game can support before the evidence exists.

## Documentation verification

The final pass checks relative file links and local heading anchors, Markdown fence balance, CSV shape/unique IDs/acquisition fields, whitespace errors, and changed-file scope. It also compares the existing Python source/tests and ignore file byte-for-byte with starting commit `301466b`. Final results are recorded in [PROGRESS.md](../PROGRESS.md).

No game tests were run because game code was not changed. No software dependencies, game engine, asset package, runtime prototype, medical reviewer or educational study was exercised by this documentation review. External source checks are targeted and cannot guarantee future link availability.

## Handoff conclusion

The plan has a coherent first case, a defensible narrow slice, explicit fidelity limits, candidate assets with rights evidence, a conditional technology decision, task/state interfaces, a dependency roadmap and measurable validation gates. It is ready for the owner to review and for later implementation scoping. Accuracy remains a goal that must be demonstrated subsystem by subsystem.
