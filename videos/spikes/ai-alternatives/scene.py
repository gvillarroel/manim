from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import ORANGE


CONCEPT = {'title': 'AI Alternatives',
 'subtitle': 'Choose by context gravity, workflow, controls, and billing.',
 'hook': 'The question is not only which model is best; it is which product fits the job.',
 'definition': 'AI products differ by where your context lives, which workflow they optimize, what '
               'controls they expose, and how billing behaves.',
 'keywords': ['context', 'workflow', 'controls', 'billing', 'governance', 'fit'],
 'lenses': [('Plain English', 'Pick the tool whose defaults match the work.'),
            ('Visual model', 'Context gravity pulls each product toward different daily jobs.'),
            ('Practical cue', 'Compare the full wrapper, not just the model name.')],
 'mechanism': ['job', 'context', 'surface', 'controls', 'billing'],
 'mechanism_note': 'Rovo, Gemini, Copilot, and Claude differ mainly in product context and harness '
                   'defaults.',
 'mechanism_cards': ['Rovo leans toward Atlassian organizational knowledge.',
                     'Gemini leans toward Google productivity and research.',
                     'Copilot and Claude Code lean toward coding workflows with different harness '
                     'choices.'],
 'contrast': ('Best model', 'Abstract leaderboard', 'Best fit', 'Daily workflow match'),
 'practical': ['Map where context lives',
               'Check tool permissions',
               'Estimate cost per task',
               'Pilot with real work'],
 'use_when': 'Use this frame when selecting an AI assistant for a team.',
 'watch_for': 'Feature lists hide whether the tool fits the actual workflow.',
 'control_lever': 'Score options by context, workflow, governance, and cost.',
 'recap': ['context', 'workflow', 'tools', 'policy', 'cost'],
 'takeaway': 'The right AI product is the one whose harness fits the job.',
 'footer': 'Fit beats leaderboard ranking.',
 'caution': 'Exact plan pricing changes; verify vendor pages before recording.',
 'handoff': 'End of pack: use the same frame to evaluate new AI products.',
 'accent': 'ORANGE'}
CONCEPT["accent"] = ORANGE


class AIAlternatives(AIConceptScene):
    concept = CONCEPT
