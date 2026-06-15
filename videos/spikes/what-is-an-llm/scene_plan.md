# What is an LLM?

Status: Spike
Target runtime: 39 seconds
Audience: Technical beginners and practitioners who use AI tools but need a durable mental model.
Core idea: An LLM turns text into tokens and predicts useful continuations one token at a time.
Learning outcome: The viewer can explain the concept using a plain definition, a mechanism diagram, and one practical decision rule.

## Research Summary

The scene uses tokenization, next-token prediction, parameter count, and accelerator hardware as the minimum useful mental model for an LLM. The plan uses short claims only and pushes source detail into `research.md`.

## Visual Language

- White background with dark text and shared color variables imported from `components/styles/ai_concept_theme.py`.
- 3Blue1Brown-style motion: a misconception is crossed out, an equation-like mental model assembles, particles travel through a mechanism graph, and the idea resolves into an orbiting recap map.
- Each scene explains the same idea in more than one way at the same time: a plain-language sentence, symbolic equation, moving mechanism, visual contrast, rising pressure curve, and connected recap graph.
- Accent color changes by concept, but the palette, spacing, motion grammar, particle flow, and recap-map structure stay consistent across all videos.
- Avoid slide decks: do not hold static card grids as the main explanation; every beat must show a relationship changing over time.

## Timeline

| Time | Beat | Visuals | Narration or on-screen text | Transition |
| --- | --- | --- | --- | --- |
| 0:00-0:04 | Hook | Misconception text is crossed out while concept keywords gather below it. | "Not a magic database: it is a text prediction system with memory-like context." | Title appears, the misconception is struck through, then keywords pulse into view. |
| 0:04-0:12 | Core definition | Definition becomes an equation-like strip using the recap terms. Three small annotations point to the same concept from different angles. | "An LLM turns text into tokens and predicts useful continuations one token at a time." | The hook transforms into the symbolic model and each term pulses in sequence. |
| 0:12-0:22 | Mechanism | A node graph appears: text -> tokens -> model -> next token -> append. Dots move through the graph to make the causal flow visible. | "Generation is iterative: the output token becomes part of the next input." | Particles traverse the arrows, then input/rule/result callouts appear below the flow. |
| 0:22-0:31 | Practical implication | The weak frame visually transforms into the stronger frame; meters and a pressure curve grow beside it. | "The useful mental model is text -> tokens -> next token -> repeated loop." | The mechanism condenses into a contrast transform and animated consequence meters. |
| 0:31-0:39 | Cost, caution, handoff | A central concept node connects to recap terms in an orbit map while caution and next-step callouts appear. | "Bigger parameter counts do not automatically mean better results for every task. Next: billing explains why those tokens and turns become money." | Recap edges draw outward, terms pulse, then the scene fades. |

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

- Generate one Manim `Scene` subclass named `WhatIsAnLLM` in `scene.py`.
- Use the temporary shared helpers in `components/layouts/ai_concept_scene.py`, `components/mobjects/ai_concept_primitives.py`, and `components/styles/ai_concept_theme.py` because the user explicitly requested cross-video consistency.
- Keep all visible copy in English.
- Preserve a white background and keep all colors defined through shared variables.
- Do not add external assets; use Manim primitives only.
- The rendered scene should feel like a short visual explanation, not a slide deck: prioritize transformations, moving particles, arrows, curves, and object continuity.
