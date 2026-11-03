# Open Heart Surgery Simulation — Master Plan

> Status: **PLANNING — fresh research restarted 2026-11-03**. This task changes planning documents only. The repository already contains a small Python heartbeat example; it is not a validated surgical or physiological simulator.

## Goal

Build a realistic open heart surgery simulation game that stays as close to real practice as possible:
the surgical steps, anatomy, instruments, operating-room team and physiology (vital signs, heart-lung bypass,
cardioplegia, blood) should all behave like the real thing. Free assets licensed for personal / non-commercial
use, Blender and other open tools may be used.

**Disclaimer:** this is a personal, educational game project. It is not a certified medical training device
and must not be used for clinical decisions.

## How this plan is built

Each step is pushed to the repo when it finishes:

| Step | What happens | Output | Status |
|------|--------------|--------|--------|
| 0 | Skeleton + planning process | `PLAN.md` | Done |
| 1 | Research: surgery, physiology, assets and licenses, engine and tech, realism, game design, production | `docs/plan/research/*.md` | Pending |
| 2 | Design: engine decision + detailed plan sections | `docs/plan/*.md` | Pending |
| 3 | Review: medical-accuracy, licensing, feasibility and completeness checks, then fixes | updated `docs/plan/*.md`, final `PLAN.md` | Pending |

## Research restart — 2026-11-03

The owner requested a new search and a complete plan before implementation. The four existing research reports are being checked against fresh primary sources, and the three missing domains will be completed. Historical reports remain available in Git history.

- **Checkpoint A:** repository audit and research restart (this update).
- **Checkpoint B:** seven refreshed research reports, with sources, limitations, and license evidence.
- **Checkpoint C:** integrated scope, simulation architecture, asset pipeline, gameplay, production roadmap, and acceptance criteria.
- **Checkpoint D:** independent gap review, corrections, and final planning handoff.

Each completed checkpoint will be committed and a push attempted to the existing default branch. Any access failure will be recorded in [the progress log](docs/plan/PROGRESS.md); local commits are not represented as uploads.

Working assumptions, pending research: personal/non-commercial use; desktop PC first; adult elective on-pump CABG as the first full procedure; Blender asset preparation; optional PC VR and haptics after the desktop simulation proves viable. These are reversible planning assumptions, not user hardware or budget commitments.

## Plan sections (filled in by Step 2)

1. Vision, scope and target platform
2. Medical procedure model (step-by-step surgical flow)
3. Physiology, anesthesia and perfusion simulation
4. Technical architecture and engine choice
5. Asset pipeline (anatomy, instruments, OR, licenses)
6. Gameplay, controls, scoring and UX
7. Visual and audio realism
8. Roadmap and milestones
9. Risks, validation and testing
