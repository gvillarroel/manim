# Project Rules

## Language

- Write every repository artifact in English: documentation, file names, code comments, variable names, scene text, captions, narration, commit messages, and review notes.
- The user may communicate in another language. Convert project-facing output to English before writing files.

## Purpose

This repository produces short Manim videos through a two-step workflow:

1. Plan the scene as text, including research, structure, timing, visual beats, and transitions.
2. Generate Python code that implements the approved text plan with Manim.

Keep these stages separate. Do not write Manim code while using the text-planning skill, and do not redesign the story while using the code-generation skill unless the plan is internally inconsistent.

## Directory Structure

```text
components/
  animations/        Reusable approved animation helpers.
  layouts/           Reusable approved layout helpers.
  mobjects/          Reusable approved custom mobjects.
  styles/            Reusable approved color, typography, and timing constants.
docs/
  promotion.md       Process for promoting a spike to an approved example.
skills/
  scene-script-planner/
  manim-code-generator/
videos/
  examples/          Videos generated from approved scripts.
  spikes/            Videos generated from unapproved or exploratory scripts.
```

## Video Folders

Each video folder should use this shape when practical:

```text
videos/<examples|spikes>/<slug>/
  scene_plan.md      Text plan and timing contract.
  research.md        Sources, notes, and claim checks.
  scene.py           Manim scene code.
  assets/            Video-specific assets.
  renders/           Selected rendered outputs, when intentionally tracked.
```

Use lowercase hyphenated slugs, for example `videos/spikes/bayes-intuition/`.

## Development Cycle Routing

- The development cycle must automatically place generated video work based on the script approval state.
- If `scene_plan.md` has `Status: Approved`, generate or maintain the video under `videos/examples/<slug>/`.
- If `scene_plan.md` has `Status: Spike`, `Status: Draft`, any unapproved status, or no status yet, generate or maintain the video under `videos/spikes/<slug>/`.
- Do not ask which folder to use when the status is clear. Infer the destination from the script status.
- When a script changes from unapproved to approved, promote the folder from `videos/spikes/<slug>/` to `videos/examples/<slug>/` before treating it as a reference example.
- Generated renders, assets, and source files should stay inside the selected video folder unless they are promoted into `components/`.

## Duration Rules

- A scene should run from 10 to 40 seconds.
- Prefer one clear idea per scene.
- If a scene must fall outside the range, document the reason in `scene_plan.md` before coding.
- Timing in the text plan should sum to the intended runtime before implementation starts.

## Component Rules

- Search `components/` before creating any new reusable visual element, animation helper, layout helper, or style constant.
- Reuse approved components whenever they fit the scene.
- Do not import, copy, or generalize components from `videos/spikes/` into other work.
- Spike code may contain local helpers, but those helpers are exploratory and not approved for reuse.
- Promote reusable code into `components/` only after the source video is approved.
- Keep components generic, configurable, and independent from a single video's narration.

## Spike Workflow

- New experiments start in `videos/spikes/<slug>/`.
- Spikes may be incomplete, visually rough, or structurally experimental.
- Spikes are not a source of approved components.
- Before generating code for a spike, create or update `scene_plan.md`.
- When a spike reveals a reusable pattern, note it as a candidate in the scene plan instead of adding it directly to `components/`.

## Example Video Workflow

- Approved script examples live in `videos/examples/<slug>/`.
- Example video folders preserve the final `scene_plan.md`, `research.md`, `scene.py`, and any intentionally tracked assets or renders.
- Treat videos in `videos/examples/` as reference examples.
- Treat `components/` as the reusable library.

## Promotion Workflow

- Follow `docs/promotion.md` when promoting a spike.
- Move the full folder from `videos/spikes/<slug>/` to `videos/examples/<slug>/`.
- Extract only stable, general-purpose helpers into `components/`.
- Update imports after extraction so approved video code uses `components/`.
- Leave spike-only experiments behind only when they are intentionally not part of the approved video.

## Skill Usage

- Use `skills/scene-script-planner` to create or refine text-only plans, research notes, scene schemas, transitions, narration, and timing.
- Use `skills/manim-code-generator` to convert a text plan into Python Manim code.
- Before using a local project skill, read its `SKILL.md` and any referenced files that apply to the task.
- The planner skill may identify candidate components, but it does not approve them.
- The code generator must prefer existing approved components and must not reuse code from spikes.

## Validation

- For documentation-only changes, review file structure and links.
- For Manim code changes, render a low-quality preview when the environment supports it, for example `manim -ql videos/spikes/<slug>/scene.py SceneName`.
- Inspect the render for timing, text overlap, missing assets, and transition clarity.
- Run the strongest practical validation without asking for confirmation.
