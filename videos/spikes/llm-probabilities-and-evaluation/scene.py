from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import PURPLE


CONCEPT = {'title': 'LLM Probabilities and Evaluation',
 'subtitle': 'Reliability is measured, not guessed.',
 'hook': 'An LLM does not retrieve one guaranteed answer; it samples likely continuations.',
 'definition': 'LLM output comes from probability distributions, so evaluation checks whether '
               'attempts meet a target.',
 'keywords': ['distribution', 'context', 'sample', 'pass-at-N', 'tests', 'judges'],
 'lenses': [('Plain English', 'The model ranks possible next tokens by probability.'),
            ('Visual model', 'Better context narrows the bars toward useful choices.'),
            ('Practical cue', 'Run checks, then compare quality per dollar and minute.')],
 'mechanism': ['prompt', 'probabilities', 'sample N', 'validator', 'score'],
 'mechanism_note': 'Pass-at-N asks whether at least one of N attempts succeeds.',
 'mechanism_cards': ['Context shifts the probability distribution.',
                     'Programmatic tests are strongest when the target is exact.',
                     'Model judges need calibration against human review.'],
 'contrast': ('Single answer', 'One generated path', 'Evaluation', 'Measured attempts'),
 'practical': ['Use unit tests for code',
               'Use exact validators when possible',
               'Calibrate model graders',
               'Track cost per accepted answer'],
 'use_when': 'Use this when explaining retries, sampling, or model benchmarks.',
 'watch_for': 'Higher pass-at-N can hide higher cost and latency.',
 'control_lever': 'Improve context and validators before increasing retries.',
 'recap': ['context', 'probability', 'samples', 'checks', 'quality'],
 'takeaway': 'Reliability is a distribution plus a measurement process.',
 'footer': 'Distribution + measurement = reliability.',
 'caution': 'More attempts can improve odds while also raising spend.',
 'handoff': 'Next: agents use these uncertain model calls inside longer loops.',
 'accent': 'PURPLE'}
CONCEPT["accent"] = PURPLE


class LLMProbabilitiesAndEvaluation(AIConceptScene):
    concept = CONCEPT
