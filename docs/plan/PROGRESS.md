# Planning checkpoints

Task date: 2026-11-03. User instruction: redo searches, build the plan only, and upload the plan after each step.

## A — Repository audit and research restart

- Starting repository commit: `301466b`.
- Existing default branch: `ccr-03f48685-d2o76x`.
- Existing material: master-plan skeleton, reusable research prompts, four research drafts, and a small Python heartbeat demonstration with tests.
- No `AGENTS.md` instructions were present in the checkout.
- Six parallel research tracks cover surgical workflow, physiology/perfusion, assets/licenses, engine/interaction technology, visual/audio realism, and game design/assessment. The coordinating track covers production/validation and integrates all results.
- Research must distinguish verified evidence, proposed simulation abstractions, and unresolved clinical or licensing questions. The task does not certify clinical accuracy.
- GitHub API access returned HTTP 401 with the configured credentials. Public Git clone succeeded. Checkpoint commit `1b2ba1a` was created locally; push failed: Git could not obtain a username/credential for HTTPS. It has not been uploaded.

## B — Fresh research

Complete locally: all seven refreshed reports and an item-level candidate asset register. Sources, access limits, changed claims, licenses, and future validation gates are recorded. Parallel workers reported a credit-limit error after saving their reports; the coordinator recovered the saved files and is completing integration/review. The separate independent gap-review worker did not finish; no independent review is claimed.

Research checkpoint `ce4ed5e` was committed locally; its initial push failed with the same missing HTTPS credential error.

After the owner restored GitHub access, authenticated repository inspection returned ADMIN access and Git push succeeded: remote branch `ccr-03f48685-d2o76x` advanced from `301466b` to `ce4ed5e`. **Checkpoints A and B are now uploaded.** The earlier failure is resolved; no additional connection action is needed.

## C — Integrated design

Complete and uploaded in `04636b8`: six integrated design documents and a rewritten master plan. Scope, backend selection, units, licensing, assistance, roadmap, dependencies and acceptance criteria are reconciled. No engine project, game implementation, purchased assets, or clinical-data collection was added. The remote branch advanced from `ce4ed5e` to `04636b8` successfully.

## D — Review and handoff

Complete: [internal gap review](research/00-gap-review.md), targeted source spot checks, cross-document reconciliation, and final planning handoff. The separate critic did not complete; the coordinating agent performed this review and does not claim independence.

Documentation verification: relative links and referenced local anchors resolve; Markdown fences balance; the 16-row asset-candidate CSV has consistent columns and unique IDs, with no false acquisition/hash claims; `git diff --check` passes. The only changed paths are `PLAN.md` and `docs/plan/`. Existing Python code/tests and `.gitignore` match starting commit `301466b` byte-for-byte.

No game tests were needed for this documents-only change. Clinical validation, geometry inspection, runtime benchmarks and educational studies remain future gates.

This record is included in the final review checkpoint. Delivery verification compares its commit with the remote branch after push; the final chat handoff reports the resulting commit and repository link.

## Checkpoint index

| Checkpoint | Commit / identification | Result |
|---|---|---|
| A — restart | `1b2ba1a` | Uploaded after access restored |
| B — fresh research | `ce4ed5e` | Uploaded after access restored |
| C — integrated plan | `04636b8` | Uploaded successfully |
| D — final review | Commit containing this final review record | Review complete; verify against remote at handoff |

Planning is complete. Implementation has not begun. No unresolved repository-access action remains after the successful authenticated pushes.

## E — Named proposal consolidation

The owner requested a named proposal that other agents can read, compare and improve. [OHS-PROPOSAL-001 — Codex Research & Design Proposal](../proposals/OHS-PROPOSAL-001-CODEX.md) consolidates the master plan, six design sections, seven research reports, the gap review and the complete asset-candidate register from source commit `8b77ee2d5814cbdc3847d825d3201f9b3605efaf`.

The proposal is explicitly provisional. It includes a reusable review prompt, navigation, source provenance and comparison criteria. The root README and PLAN index link to it. Relative links are rebased and citation links preserved; the source documents remain available. A separate read-only review checked the consolidation approach and its scope.

There was no open pull request to merge; the earlier plan was already on the default branch. This checkpoint consolidates and publishes that plan as a named proposal. It does not merge unrelated branches or select a winning proposal. No fresh research or game implementation was added.

## F — Android animation, assets and instrument review

The owner corrected the platform to Android and requested a precise review focused on heart animation, assets, rendering engine and realistic tools. [OHS-PROPOSAL-002](../proposals/OHS-PROPOSAL-002-ANDROID-REALISM.md) supersedes the desktop assumptions for this scope while preserving proposal 001 for comparison.

Stage A corrected scope and was uploaded in `00150f4`. Stage B added four focused reports and a structural inspection record for two licensed coronary-motion samples, uploaded in `6e37271`. Stage C integrates decisions, mobile controls, sustained-performance tests and realism gates; its final commit is the handoff checkpoint. [Review log](android-review/00-REVIEW-STATUS.md).

The native Android app, shaders, animation rig and tool physics remain unbuilt. Temporary source-sample inspection did not constitute clinical or rendered validation, and no third-party binary was committed. Existing game demonstration code remains unchanged.

## G — Requested second verification

The owner requested another check of the Android proposal. Baseline `f7e57e5` is reviewed in [OHS-ANDROID-RECHECK-002](android-review/05-REVERIFICATION.md). Two read-only source reviewers assisted; the coordinator rechecked all ten coronary STL phases and the instrument APIs. All ten source MD5 checks pass, and the original two SHA256 hashes match the earlier inspection.

Stage G1 records evidence and concrete corrections: 16 KB native packaging, pinned platform/toolchain requirements, renderer/pacing defaults, temporal contact synchronization and asset-readiness limits. Audit and ten-file structural evidence were uploaded in `6278268`.

Stage G2 reconciles proposal 002 revision 2, all four supporting reports and repository navigation. Both additional reviewers checked the corrections; a two-sample connectivity-scope ambiguity was clarified. The current commit is the revision checkpoint, with remote delivery checked at handoff. No app implementation or phone benchmark is claimed.

Verification passed for 26 Markdown files and 156 local links/anchors, code-fence balance, JSON/hash consistency and `git diff --check`. Existing example/test code, `.gitignore` and proposal 001 are unchanged from `f7e57e5`.

## H — Heart-only appearance experiment

The owner requested a small experiment showing the heart's appearance. [OHS-HEART-APPEARANCE-001](../concepts/heart-appearance-001/README.md) records the generated 2D concept and its provenance. The original PNG is copied unchanged to the repository; no third-party model, animation, engine project or app implementation was added. Anatomical acceptance and feasibility of matching this look on Android remain untested. This checkpoint publishes the visual experiment for review without changing the engine decision.

## I — Cannulation animation storyboard

On 2026-11-04 the owner requested an example of how cannulation animation could look. [OHS-CANNULATION-ANIMATION-001](../concepts/cannulation-animation-001/README.md) contains a four-panel generated storyboard based on the earlier heart appearance concept. It specifies small local contact deformation, an explicit seated attachment and compliant external tubing. A brief read-only concept review checked these intended motion relationships. The delivered image is static; no video, animation rig, procedural guidance, clinical validation or runtime result is claimed. The checkpoint publishes the unchanged image and its limitations.

## J — Owner rejection and reference-based motion correction

The owner rejected storyboard 001 and confirmed that both appearance and motion need improvement. [Reference review 002](../concepts/cannulation-realism-002/REFERENCE-REVIEW.md) records the rejected features, an exact manufacturer reference family, inspected operative imagery and the limits of the requested 99% resemblance claim. The first checkpoint records this evidence and rejection before an actual Blender motion experiment. Manufacturer/reference images remain outside the repo; no realism score is asserted.

The reference checkpoint was uploaded in `4f59390`. The next checkpoint adds an unchanged, newly generated appearance target based on inspected references, with source credit and explicit limits. The separate Blender motion prototype is being rendered and does not yet match the synthetic target's appearance; neither artifact is accepted as 99% realistic.
