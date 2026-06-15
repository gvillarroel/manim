from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import RED


CONCEPT = {'title': 'What is a Guardrail?',
 'subtitle': 'Active controls around inputs, tools, and outputs.',
 'hook': 'A guardrail is not a warning label; it blocks, redirects, or sanitizes behavior before '
         'damage happens.',
 'definition': 'A guardrail is an active control that inspects agent behavior and decides whether '
               'to allow, block, redact, or transform it.',
 'keywords': ['allow', 'block', 'redact', 'sanitize', 'policy', 'audit'],
 'lenses': [('Plain English', 'It is a checkpoint between intent and action.'),
            ('Visual model', 'Requests pass through gates before tools or outputs.'),
            ('Practical cue', 'Use separate checks for input, tool use, and output.')],
 'mechanism': ['request', 'inspect', 'decide', 'tool/model', 'audit'],
 'mechanism_note': 'Guardrails can run before the model, before a tool, or before an answer leaves '
                   'the system.',
 'mechanism_cards': ['Ingress checks catch malicious or sensitive prompts.',
                     'Tool checks enforce permissions before side effects.',
                     'Egress checks redact unsafe or sensitive outputs.'],
 'contrast': ('Policy doc', 'Passive rule', 'Guardrail', 'Active gate'),
 'practical': ['Block destructive commands',
               'Redact secrets',
               'Detect prompt injection',
               'Log decisions'],
 'use_when': 'Use guardrails anywhere model output can trigger real-world action.',
 'watch_for': 'Fail-open designs can silently skip protection.',
 'control_lever': 'Choose inspect-only, block, redact, or transform by risk level.',
 'recap': ['input', 'policy', 'decision', 'action', 'log'],
 'takeaway': 'A guardrail is policy made executable at the right checkpoint.',
 'footer': 'Policy becomes an executable checkpoint.',
 'caution': 'Strict filters reduce risk but can increase false positives.',
 'handoff': 'Next: harnesses are where those controls are wired in.',
 'accent': 'RED'}
CONCEPT["accent"] = RED


class WhatIsAGuardrail(AIConceptScene):
    concept = CONCEPT
