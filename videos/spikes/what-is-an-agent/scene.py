from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import TEAL


CONCEPT = {'title': 'What is an Agent?',
 'subtitle': 'A goal-directed loop with context, tools, and decisions.',
 'hook': 'An agent is not just a model response; it pursues a goal through repeated decisions.',
 'definition': 'An agent is a system that uses a model to choose actions, use tools, observe '
               'results, and continue toward a goal.',
 'keywords': ['goal', 'context', 'tools', 'actions', 'observations', 'loop'],
 'lenses': [('Plain English', 'It keeps working until it has enough evidence to stop.'),
            ('Visual model', 'Goal, context, action, observation, and memory form a loop.'),
            ('Practical cue', 'Autonomy increases usefulness and risk at the same time.')],
 'mechanism': ['goal', 'context', 'choose', 'act', 'observe'],
 'mechanism_note': 'Each turn decides whether to use another tool or produce the final answer.',
 'mechanism_cards': ['The model decides the next move.',
                     'The harness executes tools and returns observations.',
                     'The loop stops when the task is complete enough.'],
 'contrast': ('Workflow', 'Fixed path', 'Agent', 'Dynamic path'),
 'practical': ['Great for open-ended tasks',
               'Risky with broad permissions',
               'Cost rises with long loops'],
 'use_when': 'Use agents when the path cannot be fully scripted.',
 'watch_for': 'Do not give tools or permissions that the task does not need.',
 'control_lever': 'Constrain goal, tools, budget, and stop condition.',
 'recap': ['goal', 'loop', 'tools', 'observe', 'stop'],
 'takeaway': 'An agent is the loop around model decisions, tool use, and observations.',
 'footer': 'Agents loop through decisions, tools, and observations.',
 'caution': 'Long-horizon autonomy can trade latency and cost for task performance.',
 'handoff': 'Next: guardrails show how to constrain that loop.',
 'accent': 'TEAL'}
CONCEPT["accent"] = TEAL


class WhatIsAnAgent(AIConceptScene):
    concept = CONCEPT
