---
name: scene-script-planner
description: Plan high-quality text-only Manim video scenes with research notes, concise narrative structure, scene schemas, timing, visual beats, transitions, and reusable component candidates. Use when Codex needs to create or refine `scene_plan.md`, `research.md`, narration, storyboard structure, or transition plans before any Python Manim code is written.
---

# Scene Script Planner

## Overview

Create a text-only contract for a Manim scene before implementation. The output should be specific enough for a separate code-generation pass to implement without redesigning the story.

## Workflow

1. Read `AGENTS.md` before writing project files.
2. Work only in English for project artifacts.
3. Create or update `scene_plan.md` before Manim code exists.
4. Add `research.md` when the scene contains factual, technical, historical, scientific, financial, legal, medical, or current claims.
5. Keep the target runtime between 10 and 40 seconds unless the plan documents a clear exception.
6. Mark reusable visual ideas as component candidates only. Do not approve or create reusable components from a spike.

## Output Contract

Use this structure for `scene_plan.md`:

```markdown
# Title

Status: Spike | Approved
Target runtime: 10-40 seconds
Audience:
Core idea:
Learning outcome:

## Research Summary

## Visual Language

## Timeline

| Time | Beat | Visuals | Narration or on-screen text | Transition |
| --- | --- | --- | --- | --- |

## Component Candidates

## Implementation Notes
```

## Quality Bar

- Design around one primary idea, not a list of facts.
- Keep on-screen text short enough to read comfortably.
- Make every transition explain a relationship, reveal a new state, or reduce visual clutter.
- Ensure timeline rows add up to the stated runtime.
- Prefer concrete visual metaphors that can be implemented with Manim primitives or existing approved components.
- Avoid placing important claims only in narration when they need visual support.
- Record uncertainty and source gaps in `research.md`.

## References

- Read `references/scene-plan-schema.md` when creating or reviewing a scene plan.
- Read `references/research-quality.md` when research, source quality, or factual claims matter.
