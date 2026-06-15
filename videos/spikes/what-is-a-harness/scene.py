from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import SLATE


CONCEPT = {'title': 'What is a Harness?',
 'subtitle': 'The runtime wrapper where the agent actually lives.',
 'hook': 'The real product is not just the model; the harness controls the loop around it.',
 'definition': 'A harness is the runtime wrapper that manages prompts, context, tools, '
               'permissions, environment, and the agent loop.',
 'keywords': ['model', 'context', 'tools', 'permissions', 'environment', 'loop'],
 'lenses': [('Plain English', 'It is the operating frame around the model.'),
            ('Visual model', 'Model plus tools plus policy plus memory becomes the product.'),
            ('Practical cue', 'Harness defaults decide cost, safety, and behavior.')],
 'mechanism': ['prompt', 'context', 'model', 'tools', 'policy'],
 'mechanism_note': 'The harness decides what the model sees, what it can do, and when to call it '
                   'again.',
 'mechanism_cards': ['Context management changes what the model knows.',
                     'Tool routing changes what the agent can affect.',
                     'Permissions decide which actions are allowed.'],
 'contrast': ('Model', 'Predicts text', 'Harness', 'Runs the system'),
 'practical': ['Fewer bad turns',
               'Safer permissions',
               'Reusable defaults',
               'Clearer observability'],
 'use_when': 'Use this term when comparing Copilot, Claude Code, OpenCode, or custom runtimes.',
 'watch_for': 'Two tools using the same model can behave very differently.',
 'control_lever': 'Tune context, tools, permissions, hooks, and stop conditions.',
 'recap': ['prompt', 'context', 'tools', 'policy', 'loop'],
 'takeaway': 'The harness turns a model into a usable agent system.',
 'footer': 'The wrapper shapes the agent.',
 'caution': 'Poor harness design wastes calls and hides failure modes.',
 'handoff': 'Next: hooks are interception points inside the harness.',
 'accent': 'SLATE'}
CONCEPT["accent"] = SLATE


class WhatIsAHarness(AIConceptScene):
    concept = CONCEPT
