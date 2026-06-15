from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import GREEN


CONCEPT = {'title': 'What is a Harness Plugin?',
 'subtitle': 'A distributable package for harness customization.',
 'hook': 'A plugin is the packaging layer, not the model itself.',
 'definition': 'A harness plugin is an installable package that bundles reusable agents, skills, '
               'hooks, integrations, or MCP configuration.',
 'keywords': ['package', 'install', 'agents', 'skills', 'hooks', 'MCP'],
 'lenses': [('Plain English', 'It ships a repeatable setup instead of copy-paste configuration.'),
            ('Visual model', 'One package unpacks into skills, hooks, agents, and connectors.'),
            ('Practical cue', 'Plugins standardize team behavior across projects.')],
 'mechanism': ['package', 'install', 'unpack', 'configure', 'reuse'],
 'mechanism_note': 'A plugin turns customization into a shareable, versioned unit.',
 'mechanism_cards': ['It can contain skill folders or custom agents.',
                     'It can ship hook definitions and integration setup.',
                     'It can configure MCP servers or other tool surfaces.'],
 'contrast': ('Manual setup', 'One repo at a time', 'Plugin', 'Reusable package'),
 'practical': ['Share domain expertise',
               'Standardize defaults',
               'Bundle complex MCP setup',
               'Version behavior'],
 'use_when': 'Use plugins when setup should travel across repositories or teams.',
 'watch_for': 'Plugins can hide runtime cost if they inject work every session.',
 'control_lever': 'Review plugin contents and permissions before standardizing.',
 'recap': ['package', 'agents', 'skills', 'hooks', 'MCP'],
 'takeaway': 'Plugins distribute harness behavior as a repeatable package.',
 'footer': 'Package behavior once; reuse it.',
 'caution': 'Installable convenience still needs governance and review.',
 'handoff': 'Next: skills are the reusable procedures inside many plugins.',
 'accent': 'GREEN'}
CONCEPT["accent"] = GREEN


class WhatIsAHarnessPlugin(AIConceptScene):
    concept = CONCEPT
