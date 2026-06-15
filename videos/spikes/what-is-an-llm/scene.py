from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import BLUE


CONCEPT = {'title': 'What is an LLM?',
 'subtitle': 'Text becomes tokens; tokens drive next-token prediction.',
 'hook': 'Not a magic database: it is a text prediction system with memory-like context.',
 'definition': 'An LLM turns text into tokens and predicts useful continuations one token at a '
               'time.',
 'keywords': ['text', 'tokens', 'context', 'parameters', 'next token', 'accelerators'],
 'lenses': [('Plain English', 'A model trained on text that continues text.'),
            ('Visual model', 'Context flows in; one token comes out; the context grows.'),
            ('Practical cue', 'Token count and model size shape speed and cost.')],
 'mechanism': ['text', 'tokens', 'model', 'next token', 'append'],
 'mechanism_note': 'Generation is iterative: the output token becomes part of the next input.',
 'mechanism_cards': ['The model sees token IDs, not human paragraphs directly.',
                     'Parameters shape which continuation is most likely.',
                     'Accelerators make repeated matrix math fast enough to use.'],
 'contrast': ('Human word', 'Readable meaning', 'Model token', 'Implementation chunk'),
 'practical': ['Shorter context can be cheaper',
               'Bigger models often need more hardware',
               'Latency comes from repeated token steps'],
 'use_when': 'Use the term when explaining the base model itself.',
 'watch_for': 'Do not imply it stores facts like a database table.',
 'control_lever': 'Control context length, model size, and output length.',
 'recap': ['text', 'tokens', 'probabilities', 'parameters', 'hardware'],
 'takeaway': 'The useful mental model is text -> tokens -> next token -> repeated loop.',
 'footer': 'Text -> tokens -> next token -> loop.',
 'caution': 'Bigger parameter counts do not automatically mean better results for every task.',
 'handoff': 'Next: billing explains why those tokens and turns become money.',
 'accent': 'BLUE'}
CONCEPT["accent"] = BLUE


class WhatIsAnLLM(AIConceptScene):
    concept = CONCEPT
