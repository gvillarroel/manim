# Final English Report for AI Concept Video Series

## Executive Summary

This report defines a production-ready blueprint for a short-form series of **eleven 2-minute concept videos**, one concept per video, designed to extend the ai-code-assistant-tools → ai-cat-by-concept spikes while maximizing reuse inside efx\_manim. The research basis is intentionally anchored in **official vendor documentation, pricing pages, protocol specifications, and primary papers**, because the most time-sensitive parts of the agenda are product capabilities, hooks/plugins behavior, MCP support, and pricing. Across GitHub Copilot, Claude Code, OpenCode, Atlassian Rovo, Gemini, and MCP, the strongest recurring pattern is that the “real product” is not just the model: it is the **model plus harness plus tools plus permissions plus context plus billing wrapper**. That is the core narrative that should recur across the series. [\[1\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

A second conclusion is financial. The major coding harnesses are converging on **usage-shaped economics** even when they are sold as subscriptions. GitHub Copilot explicitly meters many interactions through **AI credits** and converts token usage into credits; Copilot cloud agent also uses GitHub Actions minutes. Claude Code documentation says costs are driven by **API token consumption**, and Anthropic’s pricing differentiates models materially by per-token rates and cache pricing. Atlassian Rovo Dev uses a credit allowance plus overage pricing. Even “local” runs are not free in an engineering sense, because local operation still consumes accelerator capacity, energy, and developer opportunity cost. [\[2\]](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing)

A third conclusion is architectural. The agenda naturally decomposes into a reusable visual grammar, which makes efx\_manim reuse practical. The same small asset family can cover most of the series: **token ribbons, probability bars, agent-loop flows, tool cards, guardrail gateways, event buses, plugin packages, MCP hub-and-spoke diagrams, and pricing meters**. This reuse fits the official product structures: GitHub documents the agent loop, hooks, plugins, skills, and MCP; Anthropic documents hooks, skills, plugins, MCP, and the harness itself; OpenCode exposes agents, plugins, tools, permissions, skills, and MCP in a similarly modular way. [\[3\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

One important limitation should be explicit. The actual repository contents of ai-code-assistant-tools, ai-cat-by-concept, and efx\_manim were **not directly inspectable in this session**, so the asset taxonomy, naming rules, and reuse strategy below are **recommended standards**, not a verified inventory of what already exists.

## Research Basis and Series Design Principles

The content architecture below is organized around a deliberately narrow rule: **one concept per video, one confusion removed per video**. That matches Anthropic’s recommendation to favor **simple, composable agent patterns** over prematurely complex systems, and it aligns well with Copilot’s, Claude Code’s, and OpenCode’s modular abstractions for skills, tools, hooks, plugins, and MCP. [\[4\]](https://www.anthropic.com/research/building-effective-agents)

The series should consistently distinguish five layers:

| ![Rendered Mermaid diagram 1][image1] |
| :---: |

This abstraction is directly supported by official product descriptions. GitHub describes Copilot CLI as the orchestrator of the agentic tool-use loop; Anthropic describes the harness as the loop that calls the model and routes tool calls; MCP defines standardized host, client, and server roles; and OpenCode exposes agents, tools, plugins, permissions, and MCP as explicit top-level concerns. [\[5\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

For production, the series should standardize around a **five-shot structure** that repeats in every video:

| Time | Function | Purpose |
| :---- | :---- | :---- |
| 0–12s | Hook | Name the concept and define the misconception to remove |
| 12–36s | Core definition | Give the clean mental model |
| 36–66s | Mechanism | Show how it works |
| 66–100s | Practical implication | Connect to coding agents / daily tooling |
| 100–120s | Cost, caution, handoff | Mention tradeoffs and point to the next concept |

That regularity is a production recommendation, not a vendor fact, and it is what makes efx\_manim reuse efficient.

## Cross-Series Production System

The reusable asset pipeline should follow this sequence:

| ![Rendered Mermaid diagram 2][image2] |
| :---: |

The **shared asset library** should include at minimum these parameterized elements: title\_sting, concept\_card, token\_ribbon, next\_token\_loop, parameter\_counter, accelerator\_chip\_card, probability\_bars, judge\_vs\_unit\_test\_split, agent\_loop\_stack, guardrail\_gateway, event\_bus, plugin\_box, skill\_drawer, mcp\_hub, pricing\_meter, and vendor\_compare\_card. This recommendation is driven by the recurring official abstractions across the researched products. [\[6\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

The **intro/outro template** should be fixed across the series. Intro: 4 seconds of a branded concept card plus one-sentence promise. Outro: 4 seconds of “what this concept changes” plus a handoff to the adjacent concept. This is the easiest production win for reuse.

The **metadata and naming convention** for efx\_manim should be deterministic:

* Master scene file: ai-cat\_\_\<concept-slug\>\_\_scene\_\_v1\_0\_0.py

* Shared asset: shared\_\_\<asset-slug\>\_\_v1\_0\_0.py

* Shot file: ai-cat\_\_\<concept-slug\>\_\_shot-\<start\>-\<end\>\_\_v1\_0\_0.py

* Sidecar metadata: ai-cat\_\_\<concept-slug\>\_\_meta\_\_v1\_0\_0.yaml

* Captions: ai-cat\_\_\<concept-slug\>\_\_en-US\_\_captions.vtt

* Narration script: ai-cat\_\_\<concept-slug\>\_\_en-US\_\_narration.md

Recommended YAML fields: concept\_slug, title, duration\_seconds, language, voice\_profile, fps, shared\_assets, source\_urls, last\_reviewed\_utc, qa\_status, caption\_status, localization\_status, owner, semantic\_version.

For **accessibility**, every video should ship with synchronized captions and sufficient text contrast. WCAG requires captions for prerecorded synchronized media, and WCAG contrast guidance sets a 4.5:1 minimum for regular text and 3:1 for large text. Captions should be emitted in WebVTT to keep localization and timing decoupled from animation renders. [\[7\]](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html?utm_source=chatgpt.com)

For **localization**, keep all language-bearing overlays short, avoid baking long sentences into scene geometry, and store captions/subtitles as external text tracks. WebVTT is the relevant open standard here. [\[8\]](https://www.w3.org/TR/webvtt1/?utm_source=chatgpt.com)

For **QA**, each publish package should confirm: exact runtime 120s, no unresolved visual overflow, source-backed claims, captions aligned to frame, narration pace stable, no unexplained acronym on first use, and one explicit “not covered here” handoff to prevent concept overlap.

For **observability and telemetry**, instrument render jobs and agent-assisted content-generation steps with trace spans so that scene generation, caption generation, script edits, and reference checks can be correlated. OpenTelemetry’s trace model is the right neutral default. [\[9\]](https://opentelemetry.io/docs/concepts/signals/traces/?utm_source=chatgpt.com)

## Harness Comparison and AI Alternatives

The matrix below captures the **practical harness layer**, not the underlying models.

| Harness | Core runtime idea | Official shareable unit | What can be shared | Hooks / interception | MCP support | Pricing model and likely cost impact | Source basis |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| GitHub Copilot CLI / cloud agent | Copilot CLI orchestrates the tool-use loop; cloud agent runs autonomously in a GitHub Actions-powered environment | **Plugin**, **agent skill**, **custom agent** | CLI plugins can bundle agents, skills, hooks, and MCP server configs; custom agents define prompts, tools, and MCP servers | Hooks support strategic workflow points such as session start/end, prompt events, preToolUse, permissionRequest, and subagent events | Supported across major Copilot surfaces | Subscription plans plus AI credits; GitHub states 1 AI credit \= $0.01, model/token usage converts to credits; cloud agent also consumes GitHub Actions minutes | [\[10\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) |
| Claude Code | A model-native harness with tools, context management, hook lifecycle, MCP, and desktop/CLI/IDE surfaces | **Plugin**, **skill**, **subagent** | Plugins can package skills, agents, hooks, MCP servers, and LSP servers; skills are prompt-based capability bundles; subagents are specialized agents | Very broad hook lifecycle: session, turn, tool, permission, batch, subagent, compaction, notifications, file changes, and more | First-class via Claude Code MCP and API MCP connector | Subscription seats for Claude apps plus token-priced API/Claude Code consumption; cache reads/writes and model choice materially affect spend | [\[11\]](https://www.anthropic.com/engineering/managed-agents) |
| OpenCode | Configurable coding harness with agents, tools, permissions, skills, plugins, and MCP | **Plugin**, **agent**, **skill** | Plugins can add hooks, integrations, notifications, environment injection, and custom tools; skills are discovered from SKILL.md; agents can be JSON or Markdown-defined | Plugin events cover session, tool, permission, command, file, LSP, TUI, and shell events | First-class via config | Cost depends mainly on the chosen model/provider and number of agentic steps; OpenCode also lets you cap steps, which is a direct cost control | [\[12\]](https://opencode.ai/docs/agents/) |

Two strategic observations matter for the scripts. First, a **harness selection is really a policy decision** about defaults: prompt, toolset, permission model, environment, MCP surface, and orchestration loop. Second, the cheapest harness is often the one that **makes fewer bad turns**, not the one with the lowest nominal subscription price. GitHub explicitly shows costs tied to model and token consumption; Claude Code explicitly recommends cost management through context control, model selection, thinking settings, and preprocessing hooks; OpenCode exposes steps and permission controls that can cap unnecessary agentic iteration. [\[13\]](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing)

For the broader **AI alternatives** requested in the agenda, the product framing is:

| Product | Best fit | Evidence-based positioning | Billing signal |
| :---- | :---- | :---- | :---- |
| Atlassian Rovo | Org knowledge, Jira/Confluence-centered work, enterprise search/agents | Rovo includes Search, Chat, and Agents; Rovo Search respects connected-app permissions; Rovo agents can use plugins and knowledge scoping; Rovo Dev CLI brings those ideas into terminal work | Rovo is included in paid Atlassian cloud subscriptions in many cases; Rovo Dev Standard is $20/developer/month with 2,000 credits and $0.01 per extra credit |
| Gemini App | Consumer/prosumer productivity, deep research, multimodal everyday AI | Google AI plans expose Gemini app features, Deep Research, and compute-based usage limits that refresh on a 5-hour cadence until a weekly cap | Public Google AI plan pages show Plus, Pro, and Ultra tiers; the live page parses incomplete dollar figures in this session, so verify exact Ultra tier pricing at recording time |
| GitHub Copilot | Code-first assistance tightly integrated with GitHub surfaces | Copilot spans IDE/chat/CLI/cloud agent, has MCP support, and now uses AI credits for many agent/chat flows | Personal plans include Pro $10, Pro+ $39, and Max $100 monthly; plans include AI credit allowances |
| Claude Desktop / Claude Code | Deep coding workflows, customizable agent harness, desktop-first coding agent experience | Claude Desktop provides the app surface; Claude Code runs in CLI, desktop, IDEs, and CI, with hooks, skills, plugins, and MCP | Paid Claude plans can continue via usage credits; team seats and model-token pricing are both relevant |

## Concept Video Packets

**What is an LLM**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A large language model is a text-first foundation model trained on massive data. In practice, it is a machine for predicting the next token.” | Title card: *What is an LLM?* Then “LLM \= text-driven foundation model” | title\_sting, concept\_card, foundation\_model\_card |
| 12–36s | “A token is the chunk the model actually sees. Tokens can be full words, parts of words, punctuation, or even short character sequences.” | Sentence breaks into colored token blocks | token\_ribbon, token\_counter |
| 36–66s | “Generation is iterative. The model predicts one token, appends it, then uses the updated text as context for the next step. That loop continues until it stops.” | Autoregressive loop animation | next\_token\_loop, context\_append\_arrow |
| 66–100s | “Model size usually refers to parameter count, the number of learned weights. Bigger often means more capability, but also more training and inference cost.” | Parameter odometer: 1B → 7B → 70B → 175B | parameter\_counter, size\_tradeoff\_scale |
| 100–120s | “To run LLMs efficiently, teams use accelerators such as GPUs and TPUs because the workload is mostly large-scale matrix math. That is why hardware and cost matter immediately.” | GPU, TPU, latency, cost icons | accelerator\_chip\_card, latency\_cost\_footer |

Key technical points: LLM definition; tokenization; autoregressive next-token generation; parameter count as size proxy; accelerator hardware; why scale changes cost and latency.

Verification check: show the same short sentence tokenized in two tokenizers and count the pieces. If the count changes, the audience immediately understands that “token” is an implementation unit, not a human word.

Cost / impact note: larger parameter counts do not automatically mean “better for every task”; they usually mean higher resource demand and often higher price.

Metadata and reuse: concept\_slug=llm, shared\_assets=\[title\_sting,token\_ribbon,next\_token\_loop,parameter\_counter,accelerator\_chip\_card\], visual family tag core-mechanics.

References and visual source candidates: OpenAI tokens — https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them — clean token explanation; Google Cloud glossary — https://docs.cloud.google.com/docs/generative-ai/glossary — official LLM definition; GPT-3 paper — https://papers.nips.cc/paper\_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html — autoregressive exemplar and 175B parameter example; NVIDIA H100 — https://www.nvidia.com/en-us/data-center/h100/ — hardware reference. [\[14\]](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

**LLM Billing**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “LLM billing looks confusing because products sell subscriptions, credits, and APIs. But underneath, usage still tracks model work.” | Title card with three badges: subscription, credits, tokens | title\_sting, billing\_modes\_card |
| 12–36s | “GitHub Copilot makes this explicit: many interactions consume AI credits, and GitHub says one AI credit equals one cent.” | Credit meter increments | pricing\_meter, credit\_counter |
| 36–66s | “Claude Code is also usage-shaped. Anthropic documents token-priced models and recommends managing spend through context control, model choice, and hooks.” | Token price ladder for Haiku, Sonnet, Opus | token\_price\_ladder, context\_trim\_visual |
| 66–100s | “Local models are not free either. You avoid vendor API invoices, but you still pay in GPU capacity, energy, maintenance, and the opportunity cost of hardware tied up running inference.” | GPU clock \+ watt/energy \+ depreciation icons | gpu\_clock\_meter, opportunity\_cost\_card |
| 100–120s | “So the practical lesson is simple: smaller context, cheaper model, fewer retries, more caching, and better prompts usually lower cost faster than tool switching alone.” | Five levers: model, context, retries, cache, prompt quality | cost\_levers\_footer |

Key technical points: token billing; AI credits vs tokens; subscription plus overage; prompt caching; local-vs-hosted economics.

Suggested verification check: maintain a small estimator sheet with input\_tokens, output\_tokens, cache\_reads, turn\_count, tool\_turns, retry\_count, and cost\_per\_successful\_task.

Cost / impact note: GitHub’s paid personal plans run from Pro to Max, with monthly AI credit allowances; GitHub also keeps paid-plan completions and next edit suggestions unlimited. Anthropic’s published model pricing ranges from Haiku 4.5 at lower per-token rates to Opus 4.8 and Fable 5 at materially higher rates, and Claude Code docs note average enterprise usage around $150–250 per developer per month, though real spend varies widely. AWS and GCP pricing pages show that accelerator time itself is not cheap, which is the cleanest public proxy for “local model opportunity cost.” [\[15\]](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses)

Metadata and reuse: concept\_slug=llm-billing, reuse pricing\_meter, credit\_counter, token\_price\_ladder, gpu\_clock\_meter.

References and visual source candidates: GitHub plans — https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses; GitHub AI credits — https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing; Claude pricing — https://claude.com/pricing; Claude Code costs — https://code.claude.com/docs/en/costs; Rovo Dev pricing — https://www.atlassian.com/licensing/rovo. [\[16\]](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses)

**LLM Probabilities and Evaluation**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “An LLM does not retrieve a single guaranteed answer. It selects tokens from a probability distribution.” | Probability bars over candidate tokens | title\_sting, probability\_bars |
| 12–36s | “Better context usually improves results because it narrows the distribution toward the right continuation.” | Same prompt with weak context vs grounded context | context\_quality\_split |
| 36–66s | “For coding, pass-at-N means: if I let the model try N times, how often do I get at least one correct answer?” | Ten sample cards, some red, one green | passn\_grid, success\_counter |
| 66–100s | “The strongest simple checks are programmatic. Run unit tests or exact validators. When outputs are open-ended, use model-based graders, and calibrate them with human review.” | Unit-test path vs judge-model path | judge\_vs\_unit\_test\_split |
| 100–120s | “Higher pass-at-N can be useful, but every extra sample costs more. Reliability is not just model quality, it is quality per dollar and per minute.” | Cost curve rising with retries | retry\_cost\_curve |

Key technical points: probabilistic decoding; context quality; pass@N intuition; programmatic graders; model-based graders; multiple trials.

Suggested code snippet and pass@N example:

import math
import numpy as np

def pass\_at\_k(total\_samples: int, correct\_samples: int, k: int) \-\> float:
    \# HumanEval-style unbiased estimator
    if total\_samples \- correct\_samples \< k:
        return 1.0
    values \= 1.0 \- k / np.arange(total\_samples \- correct\_samples \+ 1, total\_samples \+ 1\)
    return 1.0 \- float(np.prod(values))

def verify\_candidate(run\_tests\_fn, candidate\_code: str) \-\> bool:
    \# Deterministic grader for code tasks
    return bool(run\_tests\_fn(candidate\_code))

Use the snippet visually with a small example: “20 sampled patches, 6 pass tests: empirical pass@1 is 6/20, but pass@5 should be estimated with the pass@k formula, not the naive 1-(1-p)^k shortcut.” That warning comes directly from the HumanEval paper. [\[17\]](https://arxiv.org/pdf/2107.03374)

Metadata and reuse: concept\_slug=llm-probability-evaluation, reuse probability\_bars, passn\_grid, judge\_vs\_unit\_test\_split, retry\_cost\_curve.

References and visual source candidates: HumanEval / Codex eval paper — https://arxiv.org/pdf/2107.03374; OpenAI eval guide — https://developers.openai.com/api/docs/guides/evals; Anthropic evals for agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents. [\[18\]](https://arxiv.org/pdf/2107.03374)

**What is an Agent**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “An agent is a system that pursues a goal on a user’s behalf, not just a model answering one prompt.” | Title card: *Agent \= goal-directed system* | title\_sting, agent\_definition\_card |
| 12–36s | “The minimal mental model is three parts: context, environment, and action.” | Triangle diagram: context, environment, actions | agent\_triangle |
| 36–66s | “The harness runs a loop: send context to the model, get a decision, execute tools, update context, repeat.” | Animated loop | agent\_loop\_stack, tool\_roundtrip |
| 66–100s | “Some agents are tightly scripted workflows. Others are more autonomous and decide which tools to call and when to stop.” | Workflow lane vs autonomous lane | workflow\_vs\_agent\_split |
| 100–120s | “The more autonomy you allow, the more important evaluation, guardrails, and observability become.” | Guardrail, eval, telemetry icons appear | safety\_observe\_footer |

Key technical points: goal-directed behavior; context; environment; actions/tools; loop; workflows vs agents.

Verification check: require every agent demo to log at least goal, tools\_used, files\_touched, stop\_reason, and success\_criterion.

Cost / impact note: an “agent” is expensive mainly when it takes many turns or touches many tools; the conceptual definition itself does not imply high cost, but long-horizon autonomy often does.

Metadata and reuse: concept\_slug=agent, reuse agent\_triangle, agent\_loop\_stack, workflow\_vs\_agent\_split.

References and visual source candidates: OpenAI agent definition — https://openai.com/index/new-tools-for-building-agents/; Anthropic “Building effective agents” — https://www.anthropic.com/engineering/building-effective-agents; Claude Agent SDK — https://docs.anthropic.com/en/docs/claude-code/sdk. [\[19\]](https://openai.com/index/new-tools-for-building-agents/)

**What is a Guardrail**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A guardrail is a control that blocks, redirects, or sanitizes agent behavior before damage happens.” | Title card: *Guardrail \= allow / block / transform* | title\_sting, guardrail\_gateway |
| 12–36s | “Good guardrails can sit on input, output, or tool execution.” | Three gates: input, action, output | three\_gate\_flow |
| 36–66s | “Google Model Armor is a strong concrete example: it can inspect prompts and responses for prompt injection, jailbreak attempts, sensitive data, and harmful content, then allow, block, or redact.” | Packet goes through gateway, verdict appears | model\_armor\_flow, allow\_block\_redact |
| 66–100s | “In coding agents, active guardrails often show up as hooks or permission checks: deny risky shell commands, prevent secret reads, or require extra approvals.” | Bash deny examples and secret file block | tool\_policy\_cards |
| 100–120s | “Guardrails add latency and design effort, but they are usually cheaper than a bad action, leaked secret, or unsafe automation.” | Latency vs incident-cost scales | risk\_tradeoff\_scale |

Key technical points: ingress/egress controls; prompt injection; jailbreaks; sensitive-data filters; allow/block/redact; active vs passive guardrails.

Suggested verification check: seed every harness with a tiny red-team pack: one prompt-injection example, one secret-read example, one destructive shell example, one unsafe-output example.

Suggested code pattern:

def allow\_tool(tool\_name: str, tool\_input: dict) \-\> bool:
    blocked\_patterns \= \[
        ("Bash", "rm \-rf"),
        ("Read", ".env"),
        ("Read", "id\_rsa"),
    \]
    payload \= str(tool\_input)
    return not any(name \== tool\_name and pattern in payload for name, pattern in blocked\_patterns)

References and visual source candidates: Model Armor overview — https://docs.cloud.google.com/model-armor/overview; Agent Gateway integration — https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor; Anthropic guardrail guide — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks. [\[20\]](https://docs.cloud.google.com/model-armor/overview)

**What is a Harness**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A harness is the runtime wrapper around a model. It is where the agent actually lives.” | Title: *Harness \= model wrapper \+ loop \+ tools \+ policy* | title\_sting, harness\_stack\_intro |
| 12–36s | “A harness usually defines the system prompt, context rules, tool availability, MCP connections, permissions, and the model-call loop.” | Layered stack builds from bottom to top | harness\_stack\_layers |
| 36–66s | “GitHub Copilot, Claude Code, and OpenCode all expose this idea differently, but the abstraction is the same: give the model a controlled environment and a repeatable execution loop.” | Three vendor cards snap into one abstract stack | vendor\_compare\_card, abstract\_stack\_merge |
| 66–100s | “Choosing a harness is choosing defaults: what the model can touch, what it remembers, what it can call, and how safely it can fail.” | Default policy toggles flip | defaults\_panel |
| 100–120s | “That is why harness choice affects both quality and cost. A cleaner harness can reduce wasted turns, retries, and bad tool calls.” | Fewer turns \= lower spend | efficiency\_footer |

Key technical points: harness as orchestration wrapper; loop; context management; tools; MCP; permissions; environment.

Cost / impact note: Claude explicitly frames the harness as the loop routing tool calls, GitHub frames CLI as the orchestrator, and OpenAI’s 2026 agents posts also refer to a more capable harness around the loop. The economic implication is direct: sloppy harness design wastes calls. [\[21\]](https://www.anthropic.com/engineering/managed-agents)

Metadata and reuse: concept\_slug=harness, reuse harness\_stack\_layers, vendor\_compare\_card, defaults\_panel.

References and visual source candidates: GitHub agent loop — https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop; Anthropic managed agents / harness — https://www.anthropic.com/engineering/managed-agents; OpenAI Agents SDK evolution — https://openai.com/index/the-next-evolution-of-the-agents-sdk/. [\[22\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

**What is a Harness Hook**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A hook is an active interception point in the harness lifecycle.” | Title: *Hook \= event-driven control point* | title\_sting, event\_bus |
| 12–36s | “GitHub hooks can fire on session lifecycle and tool events like preToolUse and permissionRequest.” | Event chips animate across bus | github\_hook\_bus |
| 36–66s | “Claude Code exposes an even richer lifecycle, including session, turn, tool, permission, subagent, compaction, and async file or config events.” | Claude lifecycle wheel | claude\_hook\_wheel |
| 66–100s | “OpenCode handles similar needs through plugin events like tool.execute.before, tool.execute.after, permission.asked, and session events.” | OpenCode event list scroll | opencode\_event\_stream |
| 100–120s | “Hooks are powerful because they can become your live guardrail layer. But they should be fast, deterministic, and observable, or they become invisible cost multipliers.” | Fast deterministic observable | hook\_quality\_footer |

Key technical points: event interception; pre-tool vs permission checks; lifecycle coverage; guardrail use; fail-open vs fail-closed implications.

Suggested verification check: every hook should log event\_name, decision, elapsed\_ms, error\_count, and downstream\_effect.

Suggested code skeleton:

{
  "hooks": {
    "PreToolUse": \[
      {
        "matcher": "Bash",
        "hooks": \[
          {
            "type": "http",
            "url": "https://policy.example/hooks/pre-tool-use",
            "timeout": 5
          }
        \]
      }
    \]
  }
}

Evidence basis for narration: GitHub documents strategic hook points, including session start/end, preToolUse, permissionRequest, and subagent events; Claude Code documents extensive lifecycle support including PreToolUse, PermissionRequest, SubagentStart, SubagentStop, and prompt/agent/MCP-tool hook types; OpenCode plugins expose session, tool, permission, and shell events. [\[23\]](https://docs.github.com/en/copilot/concepts/agents/hooks)

Metadata and reuse: concept\_slug=harness-hook, reuse event\_bus, claude\_hook\_wheel, opencode\_event\_stream.

References and visual source candidates: GitHub hooks concept — https://docs.github.com/en/copilot/concepts/agents/hooks; GitHub hooks reference — https://docs.github.com/en/copilot/reference/hooks-reference; Claude hooks — https://code.claude.com/docs/en/hooks; OpenCode plugins — https://opencode.ai/docs/plugins/. [\[24\]](https://docs.github.com/en/copilot/concepts/agents/hooks)

**What is a Harness Plugin**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A plugin is the packaging layer for harness customization.” | Title: *Plugin \= distributable customization* | title\_sting, plugin\_box |
| 12–36s | “In GitHub Copilot CLI, plugins are installable packages that extend the CLI with reusable agents, skills, hooks, and integrations.” | GitHub package unpacks into four parts | plugin\_unpack\_cards |
| 36–66s | “In Claude Code, plugins extend Claude Code with skills, agents, hooks, MCP servers, and even LSP support, and they can be distributed through marketplaces.” | Marketplace shelf animation | marketplace\_shelf, plugin\_unpack\_cards |
| 66–100s | “In OpenCode, plugins are local files or npm packages that can subscribe to events, inject environment data, or add custom tools.” | npm box plus local folder | local\_vs\_npm\_plugin |
| 100–120s | “The practical rule is simple: use plugins for shareability, versioning, and governance. But audit them, because plugins can quietly add tools, network calls, and hidden work.” | Audit stamp \+ lock icon | plugin\_audit\_footer |

Key technical points: plugins as packaging/distribution units; vendor-specific plugin scope; marketplaces; governance.

Cost / impact note: plugins can reduce repeat setup time, but they can also increase hidden runtime cost if they inject hooks, LSP servers, or external calls on every session.

Evidence basis for narration: GitHub says CLI plugins extend Copilot with reusable agents, skills, hooks, and integrations, including MCP configs. Claude says plugins extend Claude Code with skills, agents, hooks, and MCP servers and supports plugin marketplaces. OpenCode says plugins extend OpenCode by hooking into events and customizing behavior, and can be loaded locally or from npm. [\[25\]](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins)

Metadata and reuse: concept\_slug=harness-plugin, reuse plugin\_box, plugin\_unpack\_cards, marketplace\_shelf.

References and visual source candidates: GitHub Copilot CLI plugins — https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins; Claude Code plugins — https://code.claude.com/docs/en/plugins; Claude marketplaces — https://code.claude.com/docs/en/plugin-marketplaces; OpenCode plugins — https://opencode.ai/docs/plugins/. [\[26\]](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins)

**What is a Skill**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “A skill is a reusable capability bundle, usually instructions plus supporting files, sometimes with scripts or resources.” | Title: *Skill \= reusable procedure* | title\_sting, skill\_drawer |
| 12–36s | “The best way to think about a skill is progressive disclosure: don’t load a long procedure into every prompt. Load it only when the task needs it.” | Drawer closed, then opens only on trigger | progressive\_disclosure\_drawer |
| 36–66s | “GitHub says agent skills are folders of instructions, scripts, and resources. Claude says skills load only when used. OpenCode discovers SKILL.md content on demand.” | Three vendor examples align | skill\_vendor\_triptych |
| 66–100s | “That makes skills ideal for recurring workflows like code review, migration steps, deployment checklists, or research patterns.” | /deploy, /code-review, /verify cards | workflow\_skill\_cards |
| 100–120s | “Skills improve consistency and often lower cost, because they reduce prompt repetition and keep large instruction bodies out of the working context until needed.” | Smaller context window graphic | context\_savings\_footer |

Key technical points: progressive disclosure; reusable procedures; on-demand loading; triggerable workflows.

Suggested verification check: if the same instructions are pasted into chat more than three times in a month, it should probably become a skill.

Evidence basis for narration: GitHub defines agent skills as folders of instructions, scripts, and resources; Claude Code says a skill body loads only when used, so long material costs almost nothing until needed; OpenCode says skills are loaded on-demand through the native skill tool. [\[27\]](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

Metadata and reuse: concept\_slug=skill, reuse skill\_drawer, progressive\_disclosure\_drawer, workflow\_skill\_cards.

References and visual source candidates: GitHub skills — https://docs.github.com/en/copilot/concepts/agents/about-agent-skills; Claude skills — https://code.claude.com/docs/en/skills; OpenCode skills — https://opencode.ai/docs/skills/. [\[27\]](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

**What is an MCP**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “MCP, the Model Context Protocol, is an open standard for connecting AI applications to external systems.” | Title: *MCP \= standard connector layer* | title\_sting, mcp\_hub |
| 12–36s | “The protocol defines a host, a client, and one or more servers. In practice, that means your AI app can discover tools and context in a predictable format.” | Host → client → server diagram | mcp\_roles\_diagram |
| 36–66s | “For remote HTTP transports, MCP authorization follows OAuth 2.1 conventions. For local stdio servers, credentials usually come from the environment instead.” | Local vs remote auth split | mcp\_auth\_split |
| 66–100s | “MCP matters because major harnesses already support it. GitHub Copilot supports MCP across major surfaces, Claude supports MCP in Claude Code and through the API connector, and OpenCode configures MCP directly.” | Vendor logos connect to same hub | mcp\_adoption\_strip |
| 100–120s | “MCP does not remove model cost. It reduces copy-paste context work, but tool calls can still add latency, external API bills, and security responsibility.” | Time, money, lock icons | mcp\_tradeoff\_footer |

Key technical points: open standard; host/client/server roles; JSON-RPC transport model; OAuth for remote servers; stdio for local; adoption across harnesses.

Suggested config snippet:

{
  "mcp": {
    "jira": {
      "enabled": true
    }
  }
}

Suggested verification check: for each MCP server, record auth\_mode, allowed\_tools, user\_consent\_point, audit\_log\_location, and fallback\_if\_unavailable.

Evidence basis for narration: MCP’s official docs describe it as an open protocol connecting AI applications to external systems; the specification defines hosts, clients, and servers over JSON-RPC; authorization docs recommend OAuth 2.1 for remote HTTP-based transports and environment-based credentials for stdio/local contexts; GitHub, Claude, and OpenCode all document MCP support. [\[28\]](https://modelcontextprotocol.io/docs/getting-started/intro)

Metadata and reuse: concept\_slug=mcp, reuse mcp\_hub, mcp\_roles\_diagram, mcp\_auth\_split, mcp\_adoption\_strip.

References and visual source candidates: MCP intro — https://modelcontextprotocol.io/docs/getting-started/intro; MCP spec — https://modelcontextprotocol.io/specification/2025-11-25; MCP authorization — https://modelcontextprotocol.io/docs/tutorials/security/authorization; GitHub MCP — https://docs.github.com/en/copilot/concepts/context/mcp; Claude MCP connector — https://platform.claude.com/docs/en/agents-and-tools/mcp-connector; OpenCode MCP — https://opencode.ai/docs/mcp-servers/. [\[28\]](https://modelcontextprotocol.io/docs/getting-started/intro)

**AI Alternatives**

| Time | Spoken narration | On-screen text and visual cue | Dynamic storyboard and efx\_manim reuse |
| :---- | :---- | :---- | :---- |
| 0–12s | “Not every AI product solves the same job. The useful comparison is context plus workflow plus billing.” | Title: *Choose by context gravity* | title\_sting, vendor\_compare\_card |
| 12–36s | “Atlassian Rovo is strongest where Jira, Confluence, and connected company knowledge are already the system of record.” | Rovo search and agent cards | rovo\_context\_card |
| 36–66s | “Gemini App is strongest for consumer and prosumer productivity, multimodal work, and Deep Research, but it runs on compute-based usage limits.” | Gemini Deep Research card | gemini\_research\_card |
| 66–100s | “GitHub Copilot is strongest when your workflow is already centered on GitHub code, IDE help, CLI work, and cloud agent tasks. Claude Desktop and Claude Code are strongest when you want a highly customizable coding harness with hooks, skills, plugins, and MCP.” | Split screen: Copilot vs Claude Code | copilot\_vs\_claude\_split |
| 100–120s | “So pick the wrapper that already sits closest to your real context. The right answer is usually the tool that minimizes context transfer, not the one with the loudest model brand.” | Final 2x2 map | context\_gravity\_map |

Key technical points: product-context fit; Rovo for organizational knowledge; Gemini for productivity/deep research; Copilot for GitHub-native coding; Claude Desktop/Code for customizable coding-agent workflows.

Cost / impact note: Rovo Dev Standard is $20 per developer per month with credits and overage pricing; GitHub paid personal plans scale from Pro to Max; Gemini uses subscription plans with compute-based limits; Claude app usage can continue via usage credits on paid plans. Exact public Google Ultra-tier pricing should be rechecked on the live plan page before final voice recording because the parsed plan table in this session did not expose all tier figures consistently. [\[29\]](https://www.atlassian.com/licensing/rovo)

Metadata and reuse: concept\_slug=ai-alternatives, reuse vendor\_compare\_card, context\_gravity\_map, copilot\_vs\_claude\_split.

References and visual source candidates: Rovo overview — https://www.atlassian.com/software/rovo; Rovo agents — https://support.atlassian.com/rovo/docs/agents/; Rovo Dev CLI — https://support.atlassian.com/rovo/docs/use-rovo-dev-cli/; Google AI plans — https://one.google.com/about/google-ai-plans/; Gemini limits — https://support.google.com/gemini/answer/16275805?hl=en; GitHub Copilot features/plans — https://docs.github.com/en/copilot/get-started/features and https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses; Claude Desktop — https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop; Claude Code — https://claude.com/product/claude-code. [\[30\]](https://www.atlassian.com/software/rovo)

## Open Questions and Limitations

The most important limitation is repository visibility. Because the actual efx\_manim tree was not available here, the asset reuse map is a **recommended standard** rather than an audited reuse inventory.

A second limitation is live pricing presentation on some consumer pages. Google’s public AI plan surface clearly shows plan families and usage framing, but the parsed page did not expose all tier dollar figures consistently in this session. Before final recording, the producer should do a **last-mile verification pass** on the live Google plan page and any individual Claude consumer-plan pricing page that will be spoken out loud. [\[31\]](https://one.google.com/about/google-ai-plans/)

A third limitation is scope discipline. Several concepts overlap by design: **guardrails vs hooks**, **plugins vs skills**, **agents vs harnesses**, and **MCP vs tool use**. The handoff lines in each script are therefore essential; otherwise, the series will duplicate explanations and lose the “one concept per video” advantage.

---

[\[1\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) [\[3\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) [\[5\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) [\[6\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) [\[10\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) [\[22\]](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop) https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop

[https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop)

[\[2\]](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing) [\[13\]](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing) https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing

[https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing)

[\[4\]](https://www.anthropic.com/research/building-effective-agents) https://www.anthropic.com/research/building-effective-agents

[https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

[\[7\]](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html?utm_source=chatgpt.com) Understanding SC 1.2.2: Captions (Prerecorded) (Level A)

[https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html?utm\_source=chatgpt.com](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html?utm_source=chatgpt.com)

[\[8\]](https://www.w3.org/TR/webvtt1/?utm_source=chatgpt.com) WebVTT: The Web Video Text Tracks Format

[https://www.w3.org/TR/webvtt1/?utm\_source=chatgpt.com](https://www.w3.org/TR/webvtt1/?utm_source=chatgpt.com)

[\[9\]](https://opentelemetry.io/docs/concepts/signals/traces/?utm_source=chatgpt.com) Traces

[https://opentelemetry.io/docs/concepts/signals/traces/?utm\_source=chatgpt.com](https://opentelemetry.io/docs/concepts/signals/traces/?utm_source=chatgpt.com)

[\[11\]](https://www.anthropic.com/engineering/managed-agents) [\[21\]](https://www.anthropic.com/engineering/managed-agents) https://www.anthropic.com/engineering/managed-agents

[https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)

[\[12\]](https://opencode.ai/docs/agents/) https://opencode.ai/docs/agents/

[https://opencode.ai/docs/agents/](https://opencode.ai/docs/agents/)

[\[14\]](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

[https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

[\[15\]](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses) [\[16\]](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses) https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses

[https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses)

[\[17\]](https://arxiv.org/pdf/2107.03374) [\[18\]](https://arxiv.org/pdf/2107.03374) Evaluating Large Language Models Trained on Code

[https://arxiv.org/pdf/2107.03374](https://arxiv.org/pdf/2107.03374)

[\[19\]](https://openai.com/index/new-tools-for-building-agents/) https://openai.com/index/new-tools-for-building-agents/

[https://openai.com/index/new-tools-for-building-agents/](https://openai.com/index/new-tools-for-building-agents/)

[\[20\]](https://docs.cloud.google.com/model-armor/overview) https://docs.cloud.google.com/model-armor/overview

[https://docs.cloud.google.com/model-armor/overview](https://docs.cloud.google.com/model-armor/overview)

[\[23\]](https://docs.github.com/en/copilot/concepts/agents/hooks) [\[24\]](https://docs.github.com/en/copilot/concepts/agents/hooks) https://docs.github.com/en/copilot/concepts/agents/hooks

[https://docs.github.com/en/copilot/concepts/agents/hooks](https://docs.github.com/en/copilot/concepts/agents/hooks)

[\[25\]](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins) [\[26\]](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins) https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins

[https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins)

[\[27\]](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

[https://docs.github.com/en/copilot/concepts/agents/about-agent-skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

[\[28\]](https://modelcontextprotocol.io/docs/getting-started/intro) https://modelcontextprotocol.io/docs/getting-started/intro

[https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)

[\[29\]](https://www.atlassian.com/licensing/rovo) https://www.atlassian.com/licensing/rovo

[https://www.atlassian.com/licensing/rovo](https://www.atlassian.com/licensing/rovo)

[\[30\]](https://www.atlassian.com/software/rovo) https://www.atlassian.com/software/rovo

[https://www.atlassian.com/software/rovo](https://www.atlassian.com/software/rovo)

[\[31\]](https://one.google.com/about/google-ai-plans/) https://one.google.com/about/google-ai-plans/

[https://one.google.com/about/google-ai-plans/](https://one.google.com/about/google-ai-plans/)

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>