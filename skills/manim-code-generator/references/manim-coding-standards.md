# Manim Coding Standards

## Scene Structure

- Use one main `Scene` subclass per short video unless the plan explicitly requires multiple scenes.
- Keep `construct()` readable. Extract local helper methods for repeated setup, animation groups, or layout creation.
- Match animation durations to the `scene_plan.md` timeline.
- Use `self.wait()` intentionally. Avoid padding without a pacing reason.

## Layout

- Reserve stable areas for titles, labels, diagrams, and equations.
- Use `VGroup`, `arrange`, `next_to`, `align_to`, and fixed buffers instead of hand-tuned coordinates when possible.
- Check that long labels have enough space on the target frame.
- Keep important content away from frame edges.

## Components

- Import reusable helpers from `components/`.
- Keep spike-only helpers inside the spike's `scene.py` or local files in the same spike folder.
- Move helpers to `components/` only after approval.
- Components should not depend on a single video's script text, asset names, or timing.

## Timing

- Target total runtime: 10 to 40 seconds.
- Use short, legible animation steps.
- Prefer a few meaningful transitions over many decorative movements.
- When the plan's timing is impossible, update the plan before changing the implementation.

## Validation Checklist

- Low-quality render completes.
- Runtime is close to the plan.
- No missing fonts or assets.
- No text overlap.
- No imports from `videos/spikes/`.
- Any new shared helper is in `components/` only if approved.
