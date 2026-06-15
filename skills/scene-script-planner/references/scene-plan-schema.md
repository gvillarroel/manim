# Scene Plan Schema

Use this schema for every `scene_plan.md`.

## Required Fields

- `Status`: `Spike` or `Approved`.
- `Target runtime`: A value from 10 to 40 seconds unless an exception is documented.
- `Audience`: The intended viewer and assumed knowledge.
- `Core idea`: One sentence describing the main point.
- `Learning outcome`: What the viewer should understand after watching.

## Research Summary

Summarize only claims that matter to the scene. Link each important claim to `research.md` when sources exist.

## Visual Language

Describe the recurring visual system: colors, shapes, metaphors, motion style, and how information appears or disappears.

## Timeline

Each timeline row should include:

- Time range, such as `0:00-0:05`.
- Beat, meaning the story function of the moment.
- Visuals, meaning what appears on screen.
- Narration or on-screen text, written in final English copy when known.
- Transition, meaning how the beat enters, changes, or exits.

The timeline should total the target runtime.

## Component Candidates

List reusable ideas without approving them. Use this format:

```markdown
- Candidate: <name>
  Reason:
  Proposed folder: components/<animations|layouts|mobjects|styles>/
  Approval status: Candidate only
```

## Implementation Notes

Include constraints that the Manim code generator must preserve, such as exact formulas, layout priorities, assets, or pacing details.
