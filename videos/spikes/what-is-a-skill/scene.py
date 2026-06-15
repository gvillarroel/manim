from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import TEAL


CONCEPT = {'title': 'What is a Skill?',
 'subtitle': 'A reusable procedure loaded when the task calls for it.',
 'hook': 'A skill is not a long prompt pasted forever; it is an on-demand capability bundle.',
 'definition': 'A skill is a reusable folder of instructions, scripts, and resources that an AI '
               'system can load for a specialized task.',
 'keywords': ['trigger', 'instructions', 'scripts', 'resources', 'task', 'reuse'],
 'lenses': [('Plain English', 'Teach the assistant how to do a repeatable job.'),
            ('Visual model', 'A drawer opens only when the current task matches.'),
            ('Practical cue', 'Move repeated instructions into skills to reduce clutter.')],
 'mechanism': ['task', 'trigger', 'load', 'execute', 'finish'],
 'mechanism_note': 'Skills keep specialized procedure out of the main context until it is useful.',
 'mechanism_cards': ['The description decides when the skill is relevant.',
                     'The body provides task-specific workflow and constraints.',
                     'Scripts and assets keep complex work reproducible.'],
 'contrast': ('Pasted prompt', 'Always in context', 'Skill', 'Loaded on demand'),
 'practical': ['Codify repeated workflows',
               'Keep prompts shorter',
               'Bundle scripts',
               'Share domain procedure'],
 'use_when': 'Use a skill when the same procedure repeats across tasks.',
 'watch_for': 'A vague trigger can load the skill at the wrong time.',
 'control_lever': 'Write narrow descriptions and concise instructions.',
 'recap': ['description', 'instructions', 'scripts', 'assets', 'result'],
 'takeaway': 'A skill is reusable know-how with a trigger and supporting files.',
 'footer': 'Reusable know-how, loaded on demand.',
 'caution': 'Bad skills can amplify bad process across many tasks.',
 'handoff': 'Next: MCP connects skills and agents to external systems.',
 'accent': 'TEAL'}
CONCEPT["accent"] = TEAL


class WhatIsASkill(AIConceptScene):
    concept = CONCEPT
