from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import AMBER


CONCEPT = {'title': 'LLM Billing',
 'subtitle': 'Subscriptions hide the meter; model work still drives cost.',
 'hook': 'The invoice is not just a subscription: usage still follows tokens, model choice, and '
         'retries.',
 'definition': 'LLM cost is shaped by tokens, model tier, context size, retries, caching, and '
               'local hardware.',
 'keywords': ['tokens', 'credits', 'context', 'model tier', 'retries', 'cache'],
 'lenses': [('Plain English', 'You pay for useful model work, directly or indirectly.'),
            ('Visual model', 'Input tokens plus output tokens roll into a usage meter.'),
            ('Practical cue', 'Cost per solved task matters more than sticker price.')],
 'mechanism': ['input', 'model', 'tools', 'output', 'meter'],
 'mechanism_note': 'More context, stronger models, tool turns, and retries usually increase the '
                   'bill.',
 'mechanism_cards': ['GitHub converts token-priced model use into AI credits.',
                     'Claude Code documents API token consumption and cost controls.',
                     'Local runs trade vendor invoices for hardware capacity and upkeep.'],
 'contrast': ('Sticker price', 'Plan or seat cost', 'Real cost', 'Useful task cost'),
 'practical': ['Use smaller context',
               'Pick the cheapest sufficient model',
               'Reduce retries',
               'Cache repeated context'],
 'use_when': 'Use this view when comparing tools or planning budgets.',
 'watch_for': 'Exact public prices change; verify live pages before final voiceover.',
 'control_lever': 'Cut wasted turns before switching tools.',
 'recap': ['tokens', 'model', 'turns', 'cache', 'cost'],
 'takeaway': 'The fastest cost win is fewer wasted tokens and fewer bad turns.',
 'footer': 'Fewer wasted tokens. Fewer bad turns.',
 'caution': 'Local models are not free; hardware time and maintenance still count.',
 'handoff': 'Next: probabilities explain why retries can help and why they cost more.',
 'accent': 'AMBER'}
CONCEPT["accent"] = AMBER


class LLMBilling(AIConceptScene):
    concept = CONCEPT
