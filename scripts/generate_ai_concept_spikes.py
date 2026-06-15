"""Generate AI concept spike plans, research notes, and Manim scenes."""

from __future__ import annotations

from pathlib import Path
from pprint import pformat


ROOT = Path(__file__).resolve().parents[1]
SPIKES = ROOT / "videos" / "spikes"


COMMON_COMPONENTS = [
    ("title_sting", "A consistent title and promise entry for each concept."),
    ("animated_equation_strip", "A compact equation-like visual model for each concept."),
    ("moving_mechanism_flow", "A node-and-particle system that shows how the concept works."),
    ("contrast_transform", "A visual replacement from the weak mental model to the stronger one."),
    ("orbit_recap_map", "A final concept map with connected recap nodes."),
]


CONCEPTS = [
    {
        "slug": "what-is-an-llm",
        "class_name": "WhatIsAnLLM",
        "title": "What is an LLM?",
        "subtitle": "Text becomes tokens; tokens drive next-token prediction.",
        "accent": "BLUE",
        "hook": "Not a magic database: it is a text prediction system with memory-like context.",
        "definition": "An LLM turns text into tokens and predicts useful continuations one token at a time.",
        "keywords": ["text", "tokens", "context", "parameters", "next token", "accelerators"],
        "lenses": [
            ("Plain English", "A model trained on text that continues text."),
            ("Visual model", "Context flows in; one token comes out; the context grows."),
            ("Practical cue", "Token count and model size shape speed and cost."),
        ],
        "mechanism": ["text", "tokens", "model", "next token", "append"],
        "mechanism_note": "Generation is iterative: the output token becomes part of the next input.",
        "mechanism_cards": [
            "The model sees token IDs, not human paragraphs directly.",
            "Parameters shape which continuation is most likely.",
            "Accelerators make repeated matrix math fast enough to use.",
        ],
        "contrast": ("Human word", "Readable meaning", "Model token", "Implementation chunk"),
        "practical": ["Shorter context can be cheaper", "Bigger models often need more hardware", "Latency comes from repeated token steps"],
        "use_when": "Use the term when explaining the base model itself.",
        "watch_for": "Do not imply it stores facts like a database table.",
        "control_lever": "Control context length, model size, and output length.",
        "recap": ["text", "tokens", "probabilities", "parameters", "hardware"],
        "takeaway": "The useful mental model is text -> tokens -> next token -> repeated loop.",
        "footer": "Text -> tokens -> next token -> loop.",
        "caution": "Bigger parameter counts do not automatically mean better results for every task.",
        "handoff": "Next: billing explains why those tokens and turns become money.",
        "summary": "The scene uses tokenization, next-token prediction, parameter count, and accelerator hardware as the minimum useful mental model for an LLM.",
        "key_points": "LLM definition; tokenization; autoregressive generation; parameters as learned weights; accelerator hardware.",
        "claims": [
            ("Language models process text as tokens, which can be characters, word pieces, words, spaces, or punctuation.", "OpenAI Help Center", "High"),
            ("Generation can be explained as predicting a sequence of tokens from preceding context.", "OpenAI Help Center and language-model documentation", "High"),
            ("Modern LLM inference commonly relies on accelerator hardware for large parallel numeric workloads.", "NVIDIA and Google Cloud hardware documentation", "High"),
        ],
        "sources": [
            ("OpenAI Help: What are tokens and how to count them?", "https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them", "Token definition and billing categories."),
            ("Google Cloud Generative AI glossary", "https://docs.cloud.google.com/docs/generative-ai/glossary", "Official LLM definition reference."),
            ("GPT-3 paper", "https://papers.nips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html", "Autoregressive large model example."),
            ("NVIDIA H100 Tensor Core GPU", "https://www.nvidia.com/en-us/data-center/h100/", "Accelerator hardware reference."),
        ],
    },
    {
        "slug": "llm-billing",
        "class_name": "LLMBilling",
        "title": "LLM Billing",
        "subtitle": "Subscriptions hide the meter; model work still drives cost.",
        "accent": "AMBER",
        "hook": "The invoice is not just a subscription: usage still follows tokens, model choice, and retries.",
        "definition": "LLM cost is shaped by tokens, model tier, context size, retries, caching, and local hardware.",
        "keywords": ["tokens", "credits", "context", "model tier", "retries", "cache"],
        "lenses": [
            ("Plain English", "You pay for useful model work, directly or indirectly."),
            ("Visual model", "Input tokens plus output tokens roll into a usage meter."),
            ("Practical cue", "Cost per solved task matters more than sticker price."),
        ],
        "mechanism": ["input", "model", "tools", "output", "meter"],
        "mechanism_note": "More context, stronger models, tool turns, and retries usually increase the bill.",
        "mechanism_cards": [
            "GitHub converts token-priced model use into AI credits.",
            "Claude Code documents API token consumption and cost controls.",
            "Local runs trade vendor invoices for hardware capacity and upkeep.",
        ],
        "contrast": ("Sticker price", "Plan or seat cost", "Real cost", "Useful task cost"),
        "practical": ["Use smaller context", "Pick the cheapest sufficient model", "Reduce retries", "Cache repeated context"],
        "use_when": "Use this view when comparing tools or planning budgets.",
        "watch_for": "Exact public prices change; verify live pages before final voiceover.",
        "control_lever": "Cut wasted turns before switching tools.",
        "recap": ["tokens", "model", "turns", "cache", "cost"],
        "takeaway": "The fastest cost win is fewer wasted tokens and fewer bad turns.",
        "footer": "Fewer wasted tokens. Fewer bad turns.",
        "caution": "Local models are not free; hardware time and maintenance still count.",
        "handoff": "Next: probabilities explain why retries can help and why they cost more.",
        "summary": "The scene avoids brittle price tables and teaches the durable billing model: tokens, model tier, context, retries, caching, and hardware.",
        "key_points": "Token billing; AI credits; subscription plus overage; prompt caching; local-vs-hosted economics.",
        "claims": [
            ("GitHub Copilot model interactions consume tokens and convert cost into AI credits.", "GitHub Docs", "High"),
            ("Claude Code costs are driven by API token consumption and can be reduced through context, model, hooks, and skills.", "Claude Code Docs", "High"),
            ("Rovo Dev Standard is listed at a monthly developer price with included credits and overage pricing.", "Atlassian Rovo pricing", "High as of 2026-06-15."),
        ],
        "sources": [
            ("GitHub Copilot models and pricing", "https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing", "AI credits and token-priced model work."),
            ("GitHub Copilot licenses", "https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses", "Plan and license billing reference."),
            ("Claude Code costs", "https://code.claude.com/docs/en/costs", "Token consumption and cost reduction guidance."),
            ("Atlassian Rovo pricing", "https://www.atlassian.com/licensing/rovo", "Rovo Dev credit and overage pricing."),
        ],
    },
    {
        "slug": "llm-probabilities-and-evaluation",
        "class_name": "LLMProbabilitiesAndEvaluation",
        "title": "LLM Probabilities and Evaluation",
        "subtitle": "Reliability is measured, not guessed.",
        "accent": "PURPLE",
        "hook": "An LLM does not retrieve one guaranteed answer; it samples likely continuations.",
        "definition": "LLM output comes from probability distributions, so evaluation checks whether attempts meet a target.",
        "keywords": ["distribution", "context", "sample", "pass-at-N", "tests", "judges"],
        "lenses": [
            ("Plain English", "The model ranks possible next tokens by probability."),
            ("Visual model", "Better context narrows the bars toward useful choices."),
            ("Practical cue", "Run checks, then compare quality per dollar and minute."),
        ],
        "mechanism": ["prompt", "probabilities", "sample N", "validator", "score"],
        "mechanism_note": "Pass-at-N asks whether at least one of N attempts succeeds.",
        "mechanism_cards": [
            "Context shifts the probability distribution.",
            "Programmatic tests are strongest when the target is exact.",
            "Model judges need calibration against human review.",
        ],
        "contrast": ("Single answer", "One generated path", "Evaluation", "Measured attempts"),
        "practical": ["Use unit tests for code", "Use exact validators when possible", "Calibrate model graders", "Track cost per accepted answer"],
        "use_when": "Use this when explaining retries, sampling, or model benchmarks.",
        "watch_for": "Higher pass-at-N can hide higher cost and latency.",
        "control_lever": "Improve context and validators before increasing retries.",
        "recap": ["context", "probability", "samples", "checks", "quality"],
        "takeaway": "Reliability is a distribution plus a measurement process.",
        "footer": "Distribution + measurement = reliability.",
        "caution": "More attempts can improve odds while also raising spend.",
        "handoff": "Next: agents use these uncertain model calls inside longer loops.",
        "summary": "The scene turns probabilistic decoding into a practical evaluation story: context changes probabilities, pass-at-N measures attempts, and validators decide success.",
        "key_points": "Probabilistic decoding; context quality; pass-at-N intuition; unit tests; model-based graders.",
        "claims": [
            ("Code model evaluations often use pass-at-k style metrics to measure whether sampled outputs solve a task.", "HumanEval / Codex evaluation paper", "High"),
            ("Programmatic evals are preferred when a task has deterministic expected behavior.", "OpenAI evaluation guidance", "High"),
            ("Agent evals may need model-based grading calibrated with human judgment for open-ended outcomes.", "Anthropic eval guidance", "High"),
        ],
        "sources": [
            ("Evaluating Large Language Models Trained on Code", "https://arxiv.org/pdf/2107.03374", "Pass-at-k evaluation basis."),
            ("OpenAI Evals guide", "https://developers.openai.com/api/docs/guides/evals", "Programmatic and model-graded evaluation guidance."),
            ("Anthropic evals for agents", "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents", "Agent evaluation framing."),
        ],
    },
    {
        "slug": "what-is-an-agent",
        "class_name": "WhatIsAnAgent",
        "title": "What is an Agent?",
        "subtitle": "A goal-directed loop with context, tools, and decisions.",
        "accent": "TEAL",
        "hook": "An agent is not just a model response; it pursues a goal through repeated decisions.",
        "definition": "An agent is a system that uses a model to choose actions, use tools, observe results, and continue toward a goal.",
        "keywords": ["goal", "context", "tools", "actions", "observations", "loop"],
        "lenses": [
            ("Plain English", "It keeps working until it has enough evidence to stop."),
            ("Visual model", "Goal, context, action, observation, and memory form a loop."),
            ("Practical cue", "Autonomy increases usefulness and risk at the same time."),
        ],
        "mechanism": ["goal", "context", "choose", "act", "observe"],
        "mechanism_note": "Each turn decides whether to use another tool or produce the final answer.",
        "mechanism_cards": [
            "The model decides the next move.",
            "The harness executes tools and returns observations.",
            "The loop stops when the task is complete enough.",
        ],
        "contrast": ("Workflow", "Fixed path", "Agent", "Dynamic path"),
        "practical": ["Great for open-ended tasks", "Risky with broad permissions", "Cost rises with long loops"],
        "use_when": "Use agents when the path cannot be fully scripted.",
        "watch_for": "Do not give tools or permissions that the task does not need.",
        "control_lever": "Constrain goal, tools, budget, and stop condition.",
        "recap": ["goal", "loop", "tools", "observe", "stop"],
        "takeaway": "An agent is the loop around model decisions, tool use, and observations.",
        "footer": "Agents loop through decisions, tools, and observations.",
        "caution": "Long-horizon autonomy can trade latency and cost for task performance.",
        "handoff": "Next: guardrails show how to constrain that loop.",
        "summary": "The scene distinguishes a single model response from an agentic system that uses tools, observations, and stop conditions.",
        "key_points": "Goal-directed behavior; context; environment; tool actions; workflow-vs-agent distinction.",
        "claims": [
            ("Anthropic distinguishes workflows with predefined code paths from agents that dynamically direct tool use.", "Anthropic Building effective agents", "High"),
            ("GitHub documents the CLI as an orchestrator around an agentic tool-use loop.", "GitHub Copilot SDK agent loop", "High"),
            ("Agentic systems often trade latency and cost for better task performance.", "Anthropic Building effective agents", "High"),
        ],
        "sources": [
            ("Anthropic: Building effective agents", "https://www.anthropic.com/engineering/building-effective-agents", "Workflow-vs-agent distinction and cost tradeoff."),
            ("GitHub Copilot SDK: Agent loop", "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop", "Tool-use loop architecture."),
            ("OpenAI tools for building agents", "https://openai.com/index/new-tools-for-building-agents/", "Product-level agent framing."),
        ],
    },
    {
        "slug": "what-is-a-guardrail",
        "class_name": "WhatIsAGuardrail",
        "title": "What is a Guardrail?",
        "subtitle": "Active controls around inputs, tools, and outputs.",
        "accent": "RED",
        "hook": "A guardrail is not a warning label; it blocks, redirects, or sanitizes behavior before damage happens.",
        "definition": "A guardrail is an active control that inspects agent behavior and decides whether to allow, block, redact, or transform it.",
        "keywords": ["allow", "block", "redact", "sanitize", "policy", "audit"],
        "lenses": [
            ("Plain English", "It is a checkpoint between intent and action."),
            ("Visual model", "Requests pass through gates before tools or outputs."),
            ("Practical cue", "Use separate checks for input, tool use, and output."),
        ],
        "mechanism": ["request", "inspect", "decide", "tool/model", "audit"],
        "mechanism_note": "Guardrails can run before the model, before a tool, or before an answer leaves the system.",
        "mechanism_cards": [
            "Ingress checks catch malicious or sensitive prompts.",
            "Tool checks enforce permissions before side effects.",
            "Egress checks redact unsafe or sensitive outputs.",
        ],
        "contrast": ("Policy doc", "Passive rule", "Guardrail", "Active gate"),
        "practical": ["Block destructive commands", "Redact secrets", "Detect prompt injection", "Log decisions"],
        "use_when": "Use guardrails anywhere model output can trigger real-world action.",
        "watch_for": "Fail-open designs can silently skip protection.",
        "control_lever": "Choose inspect-only, block, redact, or transform by risk level.",
        "recap": ["input", "policy", "decision", "action", "log"],
        "takeaway": "A guardrail is policy made executable at the right checkpoint.",
        "footer": "Policy becomes an executable checkpoint.",
        "caution": "Strict filters reduce risk but can increase false positives.",
        "handoff": "Next: harnesses are where those controls are wired in.",
        "summary": "The scene teaches guardrails as executable controls that sit around prompts, tool calls, responses, and audit logs.",
        "key_points": "Ingress and egress controls; prompt injection; sensitive-data filters; allow/block/redact decisions.",
        "claims": [
            ("Google Model Armor screens prompts and responses to protect against malicious or sensitive content.", "Google Cloud Model Armor", "High"),
            ("Model Armor supports inspect-only and inspect-and-block enforcement styles.", "Google Cloud Model Armor", "High"),
            ("Prompt injection and jailbreak detection can block malicious prompts or responses when enabled.", "Google Cloud Model Armor", "High"),
        ],
        "sources": [
            ("Google Cloud Model Armor overview", "https://docs.cloud.google.com/model-armor/overview", "Guardrail screening and enforcement reference."),
            ("Anthropic guardrail guide", "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks", "Guardrail mitigation reference."),
            ("Google Agent Gateway and Model Armor", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor", "Agent gateway integration reference."),
        ],
    },
    {
        "slug": "what-is-a-harness",
        "class_name": "WhatIsAHarness",
        "title": "What is a Harness?",
        "subtitle": "The runtime wrapper where the agent actually lives.",
        "accent": "SLATE",
        "hook": "The real product is not just the model; the harness controls the loop around it.",
        "definition": "A harness is the runtime wrapper that manages prompts, context, tools, permissions, environment, and the agent loop.",
        "keywords": ["model", "context", "tools", "permissions", "environment", "loop"],
        "lenses": [
            ("Plain English", "It is the operating frame around the model."),
            ("Visual model", "Model plus tools plus policy plus memory becomes the product."),
            ("Practical cue", "Harness defaults decide cost, safety, and behavior."),
        ],
        "mechanism": ["prompt", "context", "model", "tools", "policy"],
        "mechanism_note": "The harness decides what the model sees, what it can do, and when to call it again.",
        "mechanism_cards": [
            "Context management changes what the model knows.",
            "Tool routing changes what the agent can affect.",
            "Permissions decide which actions are allowed.",
        ],
        "contrast": ("Model", "Predicts text", "Harness", "Runs the system"),
        "practical": ["Fewer bad turns", "Safer permissions", "Reusable defaults", "Clearer observability"],
        "use_when": "Use this term when comparing Copilot, Claude Code, OpenCode, or custom runtimes.",
        "watch_for": "Two tools using the same model can behave very differently.",
        "control_lever": "Tune context, tools, permissions, hooks, and stop conditions.",
        "recap": ["prompt", "context", "tools", "policy", "loop"],
        "takeaway": "The harness turns a model into a usable agent system.",
        "footer": "The wrapper shapes the agent.",
        "caution": "Poor harness design wastes calls and hides failure modes.",
        "handoff": "Next: hooks are interception points inside the harness.",
        "summary": "The scene centers the harness as the product wrapper around a model, emphasizing context, tools, permissions, and loop control.",
        "key_points": "Harness as orchestration wrapper; loop; context management; tools; MCP; permissions; environment.",
        "claims": [
            ("GitHub describes Copilot CLI as the orchestrator that runs an agentic tool-use loop.", "GitHub Copilot SDK", "High"),
            ("The model sees conversation history and tool results across loop turns.", "GitHub Copilot SDK", "High"),
            ("Harness design affects cost because each loop iteration may involve additional model calls.", "GitHub Copilot SDK and Anthropic cost guidance", "High"),
        ],
        "sources": [
            ("GitHub Copilot SDK: Agent loop", "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop", "Harness loop and CLI orchestrator."),
            ("Anthropic: Managed agents", "https://www.anthropic.com/engineering/managed-agents", "Harness and managed-agent framing."),
            ("OpenAI Agents SDK evolution", "https://openai.com/index/the-next-evolution-of-the-agents-sdk/", "Modern agent runtime framing."),
        ],
    },
    {
        "slug": "what-is-a-harness-hook",
        "class_name": "WhatIsAHarnessHook",
        "title": "What is a Harness Hook?",
        "subtitle": "An event-driven control point in the agent lifecycle.",
        "accent": "ORANGE",
        "hook": "A hook is not just logging; it can intercept behavior at lifecycle events.",
        "definition": "A harness hook is an event-triggered interception point that can log, validate, approve, deny, or transform behavior.",
        "keywords": ["event", "payload", "script", "approve", "deny", "log"],
        "lenses": [
            ("Plain English", "When this event happens, run this check."),
            ("Visual model", "Event bus sends structured payloads to hook commands."),
            ("Practical cue", "Pre-tool hooks are useful for safety gates."),
        ],
        "mechanism": ["event", "payload", "hook", "decision", "continue"],
        "mechanism_note": "Hooks attach to points such as session start, prompt submitted, pre-tool use, post-tool use, and session end.",
        "mechanism_cards": [
            "The event names where intervention is allowed.",
            "The payload gives context about the agent action.",
            "The command returns a decision or produces side effects.",
        ],
        "contrast": ("After log", "Only observes", "Pre-hook", "Can block"),
        "practical": ["Block risky tools", "Scan for secrets", "Write audit trails", "Collect timing metrics"],
        "use_when": "Use hooks when a repeatable policy must run automatically.",
        "watch_for": "Slow hooks block the agent and can degrade the workflow.",
        "control_lever": "Prefer short, deterministic checks with clear fail behavior.",
        "recap": ["event", "context", "check", "decision", "trace"],
        "takeaway": "Hooks make harness policy executable at lifecycle boundaries.",
        "footer": "Events trigger automatic checks.",
        "caution": "A hook that fails open can create false confidence.",
        "handoff": "Next: plugins package hooks and other customizations.",
        "summary": "The scene explains hooks as lifecycle interception points that receive structured context and can enforce policy.",
        "key_points": "Event interception; pre-tool checks; permission checks; lifecycle coverage; fail-open versus fail-closed.",
        "claims": [
            ("GitHub Copilot hooks run custom shell commands at strategic points in an agent workflow.", "GitHub Docs", "High"),
            ("The preToolUse hook can approve or deny tool executions.", "GitHub Docs", "High"),
            ("Hook performance and security matter because hooks run synchronously and process untrusted input.", "GitHub Docs", "High"),
        ],
        "sources": [
            ("GitHub Copilot hooks concept", "https://docs.github.com/en/copilot/concepts/agents/hooks", "Hook purpose, event types, and cautions."),
            ("GitHub hooks reference", "https://docs.github.com/en/copilot/reference/hooks-reference", "Reference for hook events."),
            ("Claude Code hooks", "https://code.claude.com/docs/en/hooks", "Claude hook lifecycle reference."),
            ("OpenCode plugins", "https://opencode.ai/docs/plugins/", "OpenCode event and plugin hook reference."),
        ],
    },
    {
        "slug": "what-is-a-harness-plugin",
        "class_name": "WhatIsAHarnessPlugin",
        "title": "What is a Harness Plugin?",
        "subtitle": "A distributable package for harness customization.",
        "accent": "GREEN",
        "hook": "A plugin is the packaging layer, not the model itself.",
        "definition": "A harness plugin is an installable package that bundles reusable agents, skills, hooks, integrations, or MCP configuration.",
        "keywords": ["package", "install", "agents", "skills", "hooks", "MCP"],
        "lenses": [
            ("Plain English", "It ships a repeatable setup instead of copy-paste configuration."),
            ("Visual model", "One package unpacks into skills, hooks, agents, and connectors."),
            ("Practical cue", "Plugins standardize team behavior across projects."),
        ],
        "mechanism": ["package", "install", "unpack", "configure", "reuse"],
        "mechanism_note": "A plugin turns customization into a shareable, versioned unit.",
        "mechanism_cards": [
            "It can contain skill folders or custom agents.",
            "It can ship hook definitions and integration setup.",
            "It can configure MCP servers or other tool surfaces.",
        ],
        "contrast": ("Manual setup", "One repo at a time", "Plugin", "Reusable package"),
        "practical": ["Share domain expertise", "Standardize defaults", "Bundle complex MCP setup", "Version behavior"],
        "use_when": "Use plugins when setup should travel across repositories or teams.",
        "watch_for": "Plugins can hide runtime cost if they inject work every session.",
        "control_lever": "Review plugin contents and permissions before standardizing.",
        "recap": ["package", "agents", "skills", "hooks", "MCP"],
        "takeaway": "Plugins distribute harness behavior as a repeatable package.",
        "footer": "Package behavior once; reuse it.",
        "caution": "Installable convenience still needs governance and review.",
        "handoff": "Next: skills are the reusable procedures inside many plugins.",
        "summary": "The scene explains a plugin as a shareable installable customization unit for harness behavior.",
        "key_points": "Plugins as packaging; vendor-specific scope; marketplaces; governance; hidden runtime cost.",
        "claims": [
            ("GitHub Copilot CLI plugins are installable packages that extend the CLI with reusable agents, skills, hooks, and integrations.", "GitHub Docs", "High"),
            ("Plugins can include custom agents, skills, hooks, MCP server configurations, and LSP configurations.", "GitHub Docs", "High"),
            ("Plugins provide reusability, team standardization, and encapsulated setup.", "GitHub Docs", "High"),
        ],
        "sources": [
            ("GitHub Copilot CLI plugins", "https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins", "Plugin definition and package contents."),
            ("Claude Code plugins", "https://code.claude.com/docs/en/plugins", "Claude plugin packaging reference."),
            ("Claude plugin marketplaces", "https://code.claude.com/docs/en/plugin-marketplaces", "Marketplace reference."),
            ("OpenCode plugins", "https://opencode.ai/docs/plugins/", "OpenCode plugin reference."),
        ],
    },
    {
        "slug": "what-is-a-skill",
        "class_name": "WhatIsASkill",
        "title": "What is a Skill?",
        "subtitle": "A reusable procedure loaded when the task calls for it.",
        "accent": "TEAL",
        "hook": "A skill is not a long prompt pasted forever; it is an on-demand capability bundle.",
        "definition": "A skill is a reusable folder of instructions, scripts, and resources that an AI system can load for a specialized task.",
        "keywords": ["trigger", "instructions", "scripts", "resources", "task", "reuse"],
        "lenses": [
            ("Plain English", "Teach the assistant how to do a repeatable job."),
            ("Visual model", "A drawer opens only when the current task matches."),
            ("Practical cue", "Move repeated instructions into skills to reduce clutter."),
        ],
        "mechanism": ["task", "trigger", "load", "execute", "finish"],
        "mechanism_note": "Skills keep specialized procedure out of the main context until it is useful.",
        "mechanism_cards": [
            "The description decides when the skill is relevant.",
            "The body provides task-specific workflow and constraints.",
            "Scripts and assets keep complex work reproducible.",
        ],
        "contrast": ("Pasted prompt", "Always in context", "Skill", "Loaded on demand"),
        "practical": ["Codify repeated workflows", "Keep prompts shorter", "Bundle scripts", "Share domain procedure"],
        "use_when": "Use a skill when the same procedure repeats across tasks.",
        "watch_for": "A vague trigger can load the skill at the wrong time.",
        "control_lever": "Write narrow descriptions and concise instructions.",
        "recap": ["description", "instructions", "scripts", "assets", "result"],
        "takeaway": "A skill is reusable know-how with a trigger and supporting files.",
        "footer": "Reusable know-how, loaded on demand.",
        "caution": "Bad skills can amplify bad process across many tasks.",
        "handoff": "Next: MCP connects skills and agents to external systems.",
        "summary": "The scene defines skills as reusable on-demand procedure bundles with instructions and supporting files.",
        "key_points": "Progressive disclosure; reusable procedures; on-demand loading; triggerable workflows.",
        "claims": [
            ("GitHub describes agent skills as folders of instructions, scripts, and resources loaded when relevant.", "GitHub Docs", "High"),
            ("Skills are supported across several Copilot surfaces.", "GitHub Docs", "High"),
            ("Skills can be project-local or personal depending on storage location.", "GitHub Docs", "High"),
        ],
        "sources": [
            ("GitHub agent skills", "https://docs.github.com/en/copilot/concepts/agents/about-agent-skills", "Skill definition and storage modes."),
            ("Claude Code skills", "https://code.claude.com/docs/en/skills", "Claude skill loading reference."),
            ("OpenCode skills", "https://opencode.ai/docs/skills/", "OpenCode skill reference."),
        ],
    },
    {
        "slug": "what-is-an-mcp",
        "class_name": "WhatIsAnMCP",
        "title": "What is an MCP?",
        "subtitle": "A standard connector layer for AI apps, data, and tools.",
        "accent": "BLUE",
        "hook": "MCP is not one tool; it is a standard way for AI apps to connect to many tools.",
        "definition": "MCP is an open standard that lets AI hosts connect to external data sources, tools, and workflows through clients and servers.",
        "keywords": ["host", "client", "server", "tools", "data", "JSON-RPC"],
        "lenses": [
            ("Plain English", "It is a connector standard for AI applications."),
            ("Visual model", "Host talks through a client to servers that expose tools and data."),
            ("Practical cue", "Build one server, then reuse it across compatible clients."),
        ],
        "mechanism": ["host", "client", "protocol", "server", "tool/data"],
        "mechanism_note": "The protocol separates the AI app from the external system it wants to use.",
        "mechanism_cards": [
            "Hosts are AI applications or agents.",
            "Clients manage connections to servers.",
            "Servers expose tools, data, prompts, or workflows.",
        ],
        "contrast": ("One-off API", "Custom per app", "MCP", "Standard connector"),
        "practical": ["Connect files and databases", "Expose tools safely", "Reuse integrations", "Track consent and auth"],
        "use_when": "Use MCP when a tool or data source should work across AI clients.",
        "watch_for": "Auth, consent, and allowed tools must be explicit.",
        "control_lever": "Document auth mode, allowed tools, audit logs, and fallback behavior.",
        "recap": ["host", "client", "server", "tools", "policy"],
        "takeaway": "MCP standardizes how AI applications reach external systems.",
        "footer": "A standard connection layer for AI tools.",
        "caution": "A standard connector still needs permissions and monitoring.",
        "handoff": "Next: alternatives show why product fit still matters.",
        "summary": "The scene teaches MCP as a connector architecture with hosts, clients, servers, tools, data, and auth considerations.",
        "key_points": "Open standard; host/client/server roles; JSON-RPC transport model; auth and adoption across harnesses.",
        "claims": [
            ("MCP is an open-source standard for connecting AI applications to external systems.", "Model Context Protocol docs", "High"),
            ("MCP lets AI applications connect to data sources, tools, and workflows.", "Model Context Protocol docs", "High"),
            ("MCP is supported across a broad ecosystem of clients and servers.", "Model Context Protocol docs", "High"),
        ],
        "sources": [
            ("MCP introduction", "https://modelcontextprotocol.io/docs/getting-started/intro", "Official MCP purpose and ecosystem framing."),
            ("MCP specification", "https://modelcontextprotocol.io/specification/2025-11-25", "Protocol specification reference."),
            ("MCP authorization", "https://modelcontextprotocol.io/docs/tutorials/security/authorization", "Authorization reference."),
            ("GitHub Copilot MCP", "https://docs.github.com/en/copilot/concepts/context/mcp", "GitHub MCP support reference."),
        ],
    },
    {
        "slug": "ai-alternatives",
        "class_name": "AIAlternatives",
        "title": "AI Alternatives",
        "subtitle": "Choose by context gravity, workflow, controls, and billing.",
        "accent": "ORANGE",
        "hook": "The question is not only which model is best; it is which product fits the job.",
        "definition": "AI products differ by where your context lives, which workflow they optimize, what controls they expose, and how billing behaves.",
        "keywords": ["context", "workflow", "controls", "billing", "governance", "fit"],
        "lenses": [
            ("Plain English", "Pick the tool whose defaults match the work."),
            ("Visual model", "Context gravity pulls each product toward different daily jobs."),
            ("Practical cue", "Compare the full wrapper, not just the model name."),
        ],
        "mechanism": ["job", "context", "surface", "controls", "billing"],
        "mechanism_note": "Rovo, Gemini, Copilot, and Claude differ mainly in product context and harness defaults.",
        "mechanism_cards": [
            "Rovo leans toward Atlassian organizational knowledge.",
            "Gemini leans toward Google productivity and research.",
            "Copilot and Claude Code lean toward coding workflows with different harness choices.",
        ],
        "contrast": ("Best model", "Abstract leaderboard", "Best fit", "Daily workflow match"),
        "practical": ["Map where context lives", "Check tool permissions", "Estimate cost per task", "Pilot with real work"],
        "use_when": "Use this frame when selecting an AI assistant for a team.",
        "watch_for": "Feature lists hide whether the tool fits the actual workflow.",
        "control_lever": "Score options by context, workflow, governance, and cost.",
        "recap": ["context", "workflow", "tools", "policy", "cost"],
        "takeaway": "The right AI product is the one whose harness fits the job.",
        "footer": "Fit beats leaderboard ranking.",
        "caution": "Exact plan pricing changes; verify vendor pages before recording.",
        "handoff": "End of pack: use the same frame to evaluate new AI products.",
        "summary": "The scene compares alternatives through product fit rather than a single best-model ranking.",
        "key_points": "Product-context fit; Rovo for organizational knowledge; Gemini for productivity; Copilot for GitHub-native coding; Claude for customizable coding-agent workflows.",
        "claims": [
            ("Rovo Dev has a published standard plan with developer credits and overage pricing.", "Atlassian Rovo pricing", "High as of 2026-06-15."),
            ("GitHub Copilot spans multiple coding surfaces and uses AI credit allowances for usage-shaped billing.", "GitHub Docs", "High"),
            ("Claude Code documents cost controls through context, model choice, hooks, skills, and usage tracking.", "Claude Code Docs", "High"),
        ],
        "sources": [
            ("Atlassian Rovo", "https://www.atlassian.com/software/rovo", "Rovo product positioning."),
            ("Atlassian Rovo pricing", "https://www.atlassian.com/licensing/rovo", "Rovo Dev pricing and credits."),
            ("Google AI plans", "https://one.google.com/about/google-ai-plans/", "Gemini consumer plan reference."),
            ("GitHub Copilot features", "https://docs.github.com/en/copilot/get-started/features", "Copilot surface and feature reference."),
            ("Claude Code", "https://claude.com/product/claude-code", "Claude coding product reference."),
        ],
    },
]


def component_candidates() -> str:
    lines = []
    for name, reason in COMMON_COMPONENTS:
        folder = "components/layouts/" if name in {"moving_mechanism_flow", "orbit_recap_map"} else "components/mobjects/"
        if name == "title_sting":
            folder = "components/animations/"
        lines.extend(
            [
                f"- Candidate: {name}",
                f"  Reason: {reason}",
                f"  Proposed folder: {folder}",
                "  Approval status: Candidate only",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def render_scene_plan(data: dict) -> str:
    return f"""# {data["title"]}

Status: Spike
Target runtime: 39 seconds
Audience: Technical beginners and practitioners who use AI tools but need a durable mental model.
Core idea: {data["definition"]}
Learning outcome: The viewer can explain the concept using a plain definition, a mechanism diagram, and one practical decision rule.

## Research Summary

{data["summary"]} The plan uses short claims only and pushes source detail into `research.md`.

## Visual Language

- White background with dark text and shared color variables imported from `components/styles/ai_concept_theme.py`.
- 3Blue1Brown-style motion: a misconception is crossed out, an equation-like mental model assembles, particles travel through a mechanism graph, and the idea resolves into an orbiting recap map.
- Each scene explains the same idea in more than one way at the same time: a plain-language sentence, symbolic equation, moving mechanism, visual contrast, rising pressure curve, and connected recap graph.
- Accent color changes by concept, but the palette, spacing, motion grammar, particle flow, and recap-map structure stay consistent across all videos.
- Avoid slide decks: do not hold static card grids as the main explanation; every beat must show a relationship changing over time.

## Timeline

| Time | Beat | Visuals | Narration or on-screen text | Transition |
| --- | --- | --- | --- | --- |
| 0:00-0:04 | Hook | Misconception text is crossed out while concept keywords gather below it. | "{data["hook"]}" | Title appears, the misconception is struck through, then keywords pulse into view. |
| 0:04-0:12 | Core definition | Definition becomes an equation-like strip using the recap terms. Three small annotations point to the same concept from different angles. | "{data["definition"]}" | The hook transforms into the symbolic model and each term pulses in sequence. |
| 0:12-0:22 | Mechanism | A node graph appears: {" -> ".join(data["mechanism"])}. Dots move through the graph to make the causal flow visible. | "{data["mechanism_note"]}" | Particles traverse the arrows, then input/rule/result callouts appear below the flow. |
| 0:22-0:31 | Practical implication | The weak frame visually transforms into the stronger frame; meters and a pressure curve grow beside it. | "{data["takeaway"]}" | The mechanism condenses into a contrast transform and animated consequence meters. |
| 0:31-0:39 | Cost, caution, handoff | A central concept node connects to recap terms in an orbit map while caution and next-step callouts appear. | "{data["caution"]} {data["handoff"]}" | Recap edges draw outward, terms pulse, then the scene fades. |

## Component Candidates

{component_candidates()}

## Implementation Notes

- Generate one Manim `Scene` subclass named `{data["class_name"]}` in `scene.py`.
- Use the temporary shared helpers in `components/layouts/ai_concept_scene.py`, `components/mobjects/ai_concept_primitives.py`, and `components/styles/ai_concept_theme.py` because the user explicitly requested cross-video consistency.
- Keep all visible copy in English.
- Preserve a white background and keep all colors defined through shared variables.
- Do not add external assets; use Manim primitives only.
- The rendered scene should feel like a short visual explanation, not a slide deck: prioritize transformations, moving particles, arrows, curves, and object continuity.
"""


def render_research(data: dict) -> str:
    claim_lines = []
    for claim, source, confidence in data["claims"]:
        claim_lines.extend(
            [
                f"- Claim: {claim}",
                f"  Source: {source}",
                f"  Confidence: {confidence}.",
                "  Notes: Used to keep the scene focused on one durable mental model.",
                "",
            ]
        )
    source_lines = []
    for title, url, why in data["sources"]:
        source_lines.extend(
            [
                f"- Title: {title}",
                f"  URL: {url}",
                f"  Why it matters: {why}",
                "",
            ]
        )
    return f"""# Research Notes

## Claims Used

{''.join(line + chr(10) for line in claim_lines).rstrip()}

## Sources Checked

{''.join(line + chr(10) for line in source_lines).rstrip()}

## Source Handling Notes

- Current pricing and product capability claims should be rechecked on the linked vendor pages before final narrated publication.
- The rendered spike avoids dense price tables and emphasizes durable mechanisms unless an exact figure is essential to the concept.
- Report source: `data/Final English Report for AI Concept Video Series.docx.md`.
"""


def render_scene_py(data: dict) -> str:
    concept = {key: value for key, value in data.items() if key not in {"claims", "sources", "summary", "key_points", "class_name", "slug", "accent"}}
    concept["accent"] = data["accent"]
    return f"""from components.layouts.ai_concept_scene import AIConceptScene
from components.styles.ai_concept_theme import {data["accent"]}


CONCEPT = {pformat(concept, width=100, sort_dicts=False)}
CONCEPT["accent"] = {data["accent"]}


class {data["class_name"]}(AIConceptScene):
    concept = CONCEPT
"""


def main() -> None:
    for data in CONCEPTS:
        folder = SPIKES / data["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene_plan.md").write_text(render_scene_plan(data), encoding="utf-8")
        (folder / "research.md").write_text(render_research(data), encoding="utf-8")
        (folder / "scene.py").write_text(render_scene_py(data), encoding="utf-8")


if __name__ == "__main__":
    main()
