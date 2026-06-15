---
name: manim-code-generator
description: Generate or refine Python Manim code from an existing text scene plan while reusing approved components, enforcing project structure, and validating short video runtime. Use when Codex needs to create or update `scene.py`, Manim classes, video-specific assets, or approved reusable components after a `scene_plan.md` exists.
---

# Manim Code Generator

## Overview

Turn an existing text scene plan into Manim Python code. Preserve the plan's story and timing while making implementation choices that are reusable, readable, and easy to promote.

## Workflow

1. Read `AGENTS.md` and the target `scene_plan.md`.
2. Confirm the plan has a target runtime from 10 to 40 seconds or documents an exception.
3. Search `components/` for reusable approved helpers before creating new visual code.
4. Implement the scene in `videos/spikes/<slug>/scene.py` or `videos/examples/<slug>/scene.py` based on the script approval status.
5. Keep spike-specific helpers local to the spike folder.
6. Extract reusable helpers into `components/` only when the source video is approved or the user explicitly asks for an approved component.
7. Render a low-quality preview when Manim is available.

## Code Rules

- Write Python, comments, class names, variables, labels, captions, and narration text in English.
- Prefer Manim primitives and existing `components/` helpers over one-off abstractions.
- Use stable dimensions and positions so text and shapes do not overlap.
- Keep scene methods readable by extracting local helper methods when a block has a clear single purpose.
- Do not import from `videos/spikes/`.
- Do not treat approved video folders as libraries. Extract shared behavior to `components/`.
- Keep visual constants close to the scene until they prove reusable, then move approved constants to `components/styles/`.

## Validation

Run the strongest practical validation without asking for confirmation.

Prefer:

```powershell
manim -ql videos/spikes/<slug>/scene.py SceneName
```

or the matching example path for an approved script. If rendering is unavailable, report the exact missing dependency or command failure.

Check the output for:

- Runtime close to the plan.
- No text overlap or unreadable labels.
- Assets load correctly.
- Transitions match the plan.
- No accidental dependency on spike-only code.

## References

- Read `references/manim-coding-standards.md` before implementing or reviewing Manim code.
