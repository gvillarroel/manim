# LLM Probabilities and Evaluation

Status: Spike
Target runtime: 39 seconds
Audience: Technical beginners and practitioners who use AI tools but need a durable mental model.
Core idea: LLM output comes from probability distributions, so evaluation checks whether attempts meet a target.
Learning outcome: The viewer can explain the concept using a plain definition, a mechanism diagram, and one practical decision rule.

## Research Summary

The scene turns probabilistic decoding into a practical evaluation story: context changes probabilities, pass-at-N measures attempts, and validators decide success. The plan uses short claims only and pushes source detail into `research.md`.

## Visual Language

- White background with dark text and shared color variables imported from `components/styles/ai_concept_theme.py`.
- 3Blue1Brown-style motion: a misconception is crossed out, an equation-like mental model assembles, particles travel through a mechanism graph, and the idea resolves into an orbiting recap map.
- Each scene explains the same idea in more than one way at the same time: a plain-language sentence, symbolic equation, moving mechanism, visual contrast, rising pressure curve, and connected recap graph.
- Accent color changes by concept, but the palette, spacing, motion grammar, particle flow, and recap-map structure stay consistent across all videos.
- Avoid slide decks: do not hold static card grids as the main explanation; every beat must show a relationship changing over time.

## Timeline

| Time | Beat | Visuals | Narration or on-screen text | Transition |
| --- | --- | --- | --- | --- |
| 0:00-0:04 | Hook | Misconception text is crossed out while concept keywords gather below it. | "An LLM does not retrieve one guaranteed answer; it samples likely continuations." | Title appears, the misconception is struck through, then keywords pulse into view. |
| 0:04-0:12 | Core definition | Definition becomes an equation-like strip using the recap terms. Three small annotations point to the same concept from different angles. | "LLM output comes from probability distributions, so evaluation checks whether attempts meet a target." | The hook transforms into the symbolic model and each term pulses in sequence. |
| 0:12-0:22 | Mechanism | A node graph appears: prompt -> probabilities -> sample N -> validator -> score. Dots move through the graph to make the causal flow visible. | "Pass-at-N asks whether at least one of N attempts succeeds." | Particles traverse the arrows, then input/rule/result callouts appear below the flow. |
| 0:22-0:31 | Practical implication | The weak frame visually transforms into the stronger frame; meters and a pressure curve grow beside it. | "Reliability is a distribution plus a measurement process." | The mechanism condenses into a contrast transform and animated consequence meters. |
| 0:31-0:39 | Cost, caution, handoff | A central concept node connects to recap terms in an orbit map while caution and next-step callouts appear. | "More attempts can improve odds while also raising spend. Next: agents use these uncertain model calls inside longer loops." | Recap edges draw outward, terms pulse, then the scene fades. |

## Component Candidates

- Candidate: title_sting
  Reason: A consistent title and promise entry for each concept.
  Proposed folder: components/animations/
  Approval status: Candidate only

- Candidate: animated_equation_strip
  Reason: A compact equation-like visual model for each concept.
  Proposed folder: components/mobjects/
  Approval status: Candidate only

- Candidate: moving_mechanism_flow
  Reason: A node-and-particle system that shows how the concept works.
  Proposed folder: components/layouts/
  Approval status: Candidate only

- Candidate: contrast_transform
  Reason: A visual replacement from the weak mental model to the stronger one.
  Proposed folder: components/mobjects/
  Approval status: Candidate only

- Candidate: orbit_recap_map
  Reason: A final concept map with connected recap nodes.
  Proposed folder: components/layouts/
  Approval status: Candidate only

## Implementation Notes

- Generate one Manim `Scene` subclass named `LLMProbabilitiesAndEvaluation` in `scene.py`.
- Use the temporary shared helpers in `components/layouts/ai_concept_scene.py`, `components/mobjects/ai_concept_primitives.py`, and `components/styles/ai_concept_theme.py` because the user explicitly requested cross-video consistency.
- Keep all visible copy in English.
- Preserve a white background and keep all colors defined through shared variables.
- Do not add external assets; use Manim primitives only.
- The rendered scene should feel like a short visual explanation, not a slide deck: prioritize transformations, moving particles, arrows, curves, and object continuity.
