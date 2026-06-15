from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import ORANGE


CONCEPT = {'title': 'What is a Harness Hook?',
 'subtitle': 'An event-driven control point in the agent lifecycle.',
 'hook': 'A hook is not just logging; it can intercept behavior at lifecycle events.',
 'definition': 'A harness hook is an event-triggered interception point that can log, validate, '
               'approve, deny, or transform behavior.',
 'keywords': ['event', 'payload', 'script', 'approve', 'deny', 'log'],
 'lenses': [('Plain English', 'When this event happens, run this check.'),
            ('Visual model', 'Event bus sends structured payloads to hook commands.'),
            ('Practical cue', 'Pre-tool hooks are useful for safety gates.')],
 'mechanism': ['event', 'payload', 'hook', 'decision', 'continue'],
 'mechanism_note': 'Hooks attach to points such as session start, prompt submitted, pre-tool use, '
                   'post-tool use, and session end.',
 'mechanism_cards': ['The event names where intervention is allowed.',
                     'The payload gives context about the agent action.',
                     'The command returns a decision or produces side effects.'],
 'contrast': ('After log', 'Only observes', 'Pre-hook', 'Can block'),
 'practical': ['Block risky tools',
               'Scan for secrets',
               'Write audit trails',
               'Collect timing metrics'],
 'use_when': 'Use hooks when a repeatable policy must run automatically.',
 'watch_for': 'Slow hooks block the agent and can degrade the workflow.',
 'control_lever': 'Prefer short, deterministic checks with clear fail behavior.',
 'recap': ['event', 'context', 'check', 'decision', 'trace'],
 'takeaway': 'Hooks make harness policy executable at lifecycle boundaries.',
 'footer': 'Events trigger automatic checks.',
 'caution': 'A hook that fails open can create false confidence.',
 'handoff': 'Next: plugins package hooks and other customizations.',
 'accent': 'ORANGE'}
CONCEPT["accent"] = ORANGE


class WhatIsAHarnessHook(AIConceptScene):
    concept = CONCEPT
