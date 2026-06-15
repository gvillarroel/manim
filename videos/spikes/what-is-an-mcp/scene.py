from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import BLUE


CONCEPT = {'title': 'What is an MCP?',
 'subtitle': 'A standard connector layer for AI apps, data, and tools.',
 'hook': 'MCP is not one tool; it is a standard way for AI apps to connect to many tools.',
 'definition': 'MCP is an open standard that lets AI hosts connect to external data sources, '
               'tools, and workflows through clients and servers.',
 'keywords': ['host', 'client', 'server', 'tools', 'data', 'JSON-RPC'],
 'lenses': [('Plain English', 'It is a connector standard for AI applications.'),
            ('Visual model', 'Host talks through a client to servers that expose tools and data.'),
            ('Practical cue', 'Build one server, then reuse it across compatible clients.')],
 'mechanism': ['host', 'client', 'protocol', 'server', 'tool/data'],
 'mechanism_note': 'The protocol separates the AI app from the external system it wants to use.',
 'mechanism_cards': ['Hosts are AI applications or agents.',
                     'Clients manage connections to servers.',
                     'Servers expose tools, data, prompts, or workflows.'],
 'contrast': ('One-off API', 'Custom per app', 'MCP', 'Standard connector'),
 'practical': ['Connect files and databases',
               'Expose tools safely',
               'Reuse integrations',
               'Track consent and auth'],
 'use_when': 'Use MCP when a tool or data source should work across AI clients.',
 'watch_for': 'Auth, consent, and allowed tools must be explicit.',
 'control_lever': 'Document auth mode, allowed tools, audit logs, and fallback behavior.',
 'recap': ['host', 'client', 'server', 'tools', 'policy'],
 'takeaway': 'MCP standardizes how AI applications reach external systems.',
 'footer': 'A standard connection layer for AI tools.',
 'caution': 'A standard connector still needs permissions and monitoring.',
 'handoff': 'Next: alternatives show why product fit still matters.',
 'accent': 'BLUE'}
CONCEPT["accent"] = BLUE


class WhatIsAnMCP(AIConceptScene):
    concept = CONCEPT
