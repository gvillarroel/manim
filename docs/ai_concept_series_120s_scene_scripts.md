# AI Concept Series 120-Second Content Scripts

Status: Master planning document
Target runtime: 120 seconds per video
Audience: Technical and semi-technical viewers who use AI tools but need clearer mental models for model behavior, cost, orchestration, safety, and product choices.

This document is a content-only production reference for eleven 2-minute concept videos. Use it to preserve the information, examples, timing, and source links needed for a later scene-generation pass.

## Series Rules

- Language: all project-facing output must be in English.
- Duration: each video is exactly 120 seconds. This is an intentional exception to the repository default of 10 to 40 seconds because this is a master script for 2-minute production cuts.
- Timing: each video uses the same five-beat content grid: `0:00-0:12` hook, `0:12-0:36` core definition, `0:36-1:06` mechanism, `1:06-1:40` practical implication, and `1:40-2:00` cost, caution, or handoff.
- Current facts: exact vendor prices, plan names, credit allowances, and product support claims must be rechecked before final recording.
- Source handling: when a source contains more detail than can fit in 120 seconds, keep the concise claim in the script and keep the official link in the references.

## Video 1: What Is an LLM?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: An LLM is a text-first foundation model that predicts useful continuations token by token.
Learning outcome: The viewer should understand tokens, context, next-token prediction, scale, and why hardware affects cost and latency.

### Key Facts

- A large language model is a text-first foundation model trained on large datasets.
- Text is processed as tokens, which may be words, word pieces, punctuation, spaces, or characters depending on the tokenizer.
- Generation can be explained as repeated next-token prediction from preceding context.
- Model size is often discussed through parameter counts, but parameter count alone is not the full quality measure.
- Efficient inference at large scale commonly depends on accelerator hardware because the workload is dominated by large numeric operations.
- More context, more output, larger models, and repeated calls all affect latency and cost.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define an LLM as a text-first model that predicts useful continuations one token at a time. | Contrast this with the misconception that an LLM is a perfect database or lookup engine. |
| 0:12-0:36 | Core definition | Explain tokens and context. The input becomes tokens, and those tokens form the context used for prediction. | Use a simple sentence such as "AI tools write code" and break it into possible token pieces. |
| 0:36-1:06 | Mechanism | Explain the repeated generation loop: context enters the model, the model ranks next-token options, one token is chosen, and the context grows. | Use a partial sentence completion example where each new token changes the next prediction. |
| 1:06-1:40 | Practical implication | Explain that training, model size, context quality, and hardware capacity shape usefulness, latency, and cost. | Compare a smaller model and a larger model through the same prompt without claiming size alone guarantees quality. |
| 1:40-2:00 | Cost and handoff | Connect LLM behavior to usage measurement: prompts, answers, retries, and long context all create measurable work. | Handoff idea: billing is the meter around model work. |

### References

- OpenAI Help Center, tokens: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- Google Cloud generative AI glossary: https://docs.cloud.google.com/docs/generative-ai/glossary
- GPT-3 paper, autoregressive language model example: https://papers.nips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
- NVIDIA H100 product page, accelerator reference: https://www.nvidia.com/en-us/data-center/h100/

## Video 2: LLM Billing

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: LLM cost is driven by model work, even when products package that work as subscriptions, credits, or API tokens.
Learning outcome: The viewer should understand input tokens, output tokens, model tiers, retries, caching, tool loops, and local versus hosted costs.

### Key Facts

- LLM products may expose cost through subscriptions, credits, API token rates, or a mixture of these.
- API-based billing commonly separates input tokens and output tokens.
- Larger context, longer output, more expensive model tiers, retries, and agentic tool loops can increase cost.
- Prompt caching or cache reads can reduce cost when the same context prefix is reused.
- Hosted services make vendor spend visible; local models move cost into hardware, energy, operations, and developer time.
- For production planning, cost per successful task is more useful than cost per single prompt.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Explain why LLM billing feels confusing: subscriptions, credits, and API pricing are different packaging around model usage. | Avoid exact prices unless verified immediately before recording. |
| 0:12-0:36 | Core definition | Define the main cost drivers: input tokens, output tokens, model choice, context length, retries, tool turns, and cache behavior. | Use a short prompt plus a long answer to show why output length matters. |
| 0:36-1:06 | Mechanism | Explain why an agentic session can cost more than one chat turn: each tool call can create additional context and more model calls. | Example flow: user request, model call, tool result, second model call, final answer. |
| 1:06-1:40 | Practical implication | Explain cost controls: reduce irrelevant context, choose the lowest adequate model, cache repeated prefixes, cap retries, and evaluate outputs. | Use a "before and after" task description: noisy prompt versus trimmed prompt. |
| 1:40-2:00 | Caution and handoff | Explain why local is not automatically free and why probability affects cost through retries and evaluation. | Handoff idea: probabilistic outputs explain why repeated attempts and evaluation matter. |

### References

- GitHub Copilot model billing and AI credits: https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
- GitHub Copilot licenses and plans: https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses
- Claude Code costs: https://code.claude.com/docs/en/costs
- Claude pricing: https://claude.com/pricing
- Atlassian Rovo pricing: https://www.atlassian.com/licensing/rovo

## Video 3: LLM Probabilities and Evaluation

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: LLM outputs are probabilistic, so evaluation must measure whether the result is good enough for the task.
Learning outcome: The viewer should understand distributions, sampling, context sensitivity, pass rates, programmatic tests, and model-based graders.

### Key Facts

- LLM generation selects from probability distributions over candidate tokens.
- Prompt and context quality can shift the distribution toward better answers but cannot guarantee correctness.
- Programmatic evaluation is preferred when correct behavior can be checked deterministically.
- Open-ended outputs often need rubric-based grading or human review.
- pass@N describes the chance that at least one of N generated samples solves a task, but it should be estimated carefully.
- More attempts can improve success probability while increasing cost and latency.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Explain that an LLM does not retrieve one guaranteed answer; it chooses from a probability distribution. | Use the phrase "likely next token" rather than "known correct token." |
| 0:12-0:36 | Core definition | Explain how context changes probabilities and why better context can improve the odds of a good answer. | Example: vague prompt versus prompt with constraints, expected format, and relevant data. |
| 0:36-1:06 | Mechanism | Explain evaluation as a wrapper around model output: tests, rubric graders, model-based graders, and human review. | Use coding as the deterministic case and policy-writing as the rubric case. |
| 1:06-1:40 | Practical implication | Explain pass@N and the success-versus-cost tradeoff of multiple attempts. | Include the example from the report: 20 sampled patches, 6 pass tests; pass@5 should use the pass@k estimator, not a naive shortcut. |
| 1:40-2:00 | Caution and handoff | Explain that agents need evaluation because they place probabilistic calls inside action loops. | Handoff idea: an agent is a loop that uses uncertain model calls to decide actions. |

### References

- HumanEval / Codex evaluation paper: https://arxiv.org/pdf/2107.03374
- OpenAI evaluation guidance: https://developers.openai.com/api/docs/guides/evals
- Anthropic evals for agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

## Video 4: What Is an Agent?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: An agent is a goal-directed system that uses model calls, context, tools, and observations to pursue an outcome.
Learning outcome: The viewer should distinguish a single prompt from an agent loop and understand autonomy, tools, stop conditions, and risk.

### Key Facts

- An agent is a system that pursues a goal, not merely a single model response.
- Agents combine context, tools, environment observations, decisions, and stopping conditions.
- Anthropic distinguishes workflows with predefined paths from agents that dynamically direct tool use.
- More autonomy can improve capability but usually increases latency, cost, and safety requirements.
- The practical boundary is not only model intelligence; it is the harness, tool access, permissions, and evaluation.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define an agent as a goal-directed system acting on a user's behalf. | Contrast one prompt-response turn with a multi-step task. |
| 0:12-0:36 | Core definition | List the required pieces: goal, context, tools, observations, environment, and stop condition. | Example goal: "Find why this test fails and propose a fix." |
| 0:36-1:06 | Mechanism | Explain the loop: decide next step, take action, observe result, update context, repeat or stop. | Include tool examples such as search, file read, test run, issue lookup, or calendar lookup depending on product context. |
| 1:06-1:40 | Practical implication | Explain where agents are useful: tasks with unknown paths, branching workflows, research, debugging, migration, and triage. | Compare "follow a fixed checklist" with "choose the next tool based on observed results." |
| 1:40-2:00 | Caution and handoff | Explain why autonomy requires evaluation, permissions, guardrails, and observability. | Handoff idea: guardrails define boundaries around the agent loop. |

### References

- OpenAI agents announcement and tools: https://openai.com/index/new-tools-for-building-agents/
- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- GitHub Copilot SDK agent loop: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop
- Claude Agent SDK: https://docs.anthropic.com/en/docs/claude-code/sdk

## Video 5: What Is a Guardrail?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A guardrail is an active control that checks AI input, output, or actions against policy before harm occurs.
Learning outcome: The viewer should understand allow, block, redact, transform, ingress checks, egress checks, prompt injection, and tradeoffs.

### Key Facts

- Guardrails are controls that enforce policy around AI behavior.
- They can inspect user input, retrieved context, tool requests, tool results, and final output.
- Typical decisions include allow, block, redact, transform, ask for permission, or route to review.
- Common risks include prompt injection, jailbreaks, secret leakage, destructive actions, and unsafe output.
- Guardrails can be active blocking controls or inspect-only monitoring controls.
- Poorly designed guardrails can over-block useful work or fail to stop harmful actions.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define a guardrail as a control that blocks, redirects, or sanitizes AI behavior before damage happens. | Use action verbs: allow, block, redact, transform, ask. |
| 0:12-0:36 | Core definition | Explain where guardrails can run: before the model, before tools, after tools, and before final output. | Mention ingress and egress controls without overloading the viewer with security terminology. |
| 0:36-1:06 | Mechanism | Explain how different risks map to different policy outcomes. | Examples: prompt injection blocked, API key redacted, destructive shell command requires permission, unsafe final answer refused. |
| 1:06-1:40 | Practical implication | Explain why precise guardrails are better than broad blocks. | A precise policy can preserve safe work while stopping only the dangerous part. |
| 1:40-2:00 | Caution and handoff | Explain that guardrails add latency and design effort, but are usually cheaper than unsafe automation or leaked data. | Handoff idea: guardrails need to be wired into the harness. |

### References

- Google Cloud Model Armor overview: https://docs.cloud.google.com/model-armor/overview
- Gemini Enterprise Agent Platform and Model Armor: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor
- Anthropic guardrail guide for jailbreak mitigation: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks

## Video 6: What Is a Harness?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A harness is the runtime wrapper that turns a model into a usable product or agentic system.
Learning outcome: The viewer should understand prompts, context management, tools, permissions, MCP connections, environment, and orchestration.

### Key Facts

- A harness is the runtime around the model: prompts, context, loop, tools, permissions, environment, and policy.
- The same model can behave differently in different harnesses because the wrapper changes inputs, available actions, and defaults.
- GitHub describes Copilot CLI as an orchestrator around an agentic tool-use loop.
- Anthropic describes the harness as the loop that calls the model and routes tool calls.
- Harness design affects cost because each extra loop iteration can add model calls and tool context.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Explain that the product is not just the model; it is the model plus the harness around it. | Use "model plus runtime wrapper" as the simple definition. |
| 0:12-0:36 | Core definition | Explain what a harness controls: system prompt, context rules, tool availability, permissions, MCP connections, environment, loop, and stop condition. | Keep the list complete because later videos explain hooks, plugins, skills, and MCP. |
| 0:36-1:06 | Mechanism | Explain the harness flow: user request becomes context, model proposes action, harness executes or blocks it, observation returns, loop continues or stops. | Example: coding harness reads files, runs tests, asks before risky changes, and returns a patch. |
| 1:06-1:40 | Practical implication | Explain why the same model behaves differently in a coding assistant, enterprise search assistant, and desktop automation assistant. | Difference comes from context sources, tool permissions, memory, and policy defaults. |
| 1:40-2:00 | Caution and handoff | Explain that harness quality affects cost, safety, and reliability. | Handoff idea: hooks are specific interception points inside the harness lifecycle. |

### References

- GitHub Copilot SDK agent loop: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop
- Anthropic managed agents and harness discussion: https://www.anthropic.com/engineering/managed-agents
- OpenAI Agents SDK evolution: https://openai.com/index/the-next-evolution-of-the-agents-sdk/

## Video 7: What Is a Harness Hook?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A hook is an event-driven interception point inside a harness lifecycle.
Learning outcome: The viewer should understand lifecycle events, pre-tool checks, permission checks, post-tool checks, fail-open versus fail-closed behavior, and audit value.

### Key Facts

- Hooks run custom checks or commands at strategic points in a harness workflow.
- Hook events can include session start, prompt handling, pre-tool use, permission request, tool result, subagent events, and session end.
- A hook can approve, deny, modify, ask for permission, log, or notify depending on the harness.
- Security matters because hooks may process untrusted input.
- Performance matters because many hooks run synchronously and can delay the user workflow.
- Fail-open behavior may let risk pass; fail-closed behavior may stop useful work.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define a hook as a point where the harness pauses an event to run a check or command. | Use "event plus check plus decision" as the minimal model. |
| 0:12-0:36 | Core definition | List common lifecycle events: session start, prompt handling, tool use, permission request, tool result, subagent event, and session end. | Keep GitHub, Claude Code, and OpenCode differences as source-backed examples, not universal claims. |
| 0:36-1:06 | Mechanism | Explain input payload, hook logic, decision, downstream effect, and logging. | Example: a pre-tool hook blocks a risky shell command or asks the user for permission. |
| 1:06-1:40 | Practical implication | Explain hook use cases: secret scanning, permission enforcement, audit trails, context shaping, notifications, and team policy. | Verification fields: event_name, decision, elapsed_ms, error_count, downstream_effect. |
| 1:40-2:00 | Caution and handoff | Explain fail-open versus fail-closed tradeoffs and why hooks are often distributed through plugins. | Handoff idea: plugins package reusable harness behavior. |

### References

- GitHub Copilot hooks concept: https://docs.github.com/en/copilot/concepts/agents/hooks
- GitHub hooks reference: https://docs.github.com/en/copilot/reference/hooks-reference
- Claude Code hooks: https://code.claude.com/docs/en/hooks
- OpenCode plugins and event model: https://opencode.ai/docs/plugins/

## Video 8: What Is a Harness Plugin?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A harness plugin packages reusable harness extensions so they can be installed, shared, governed, and updated.
Learning outcome: The viewer should understand plugins as distribution units for agents, skills, hooks, MCP configuration, integrations, and policy defaults.

### Key Facts

- A plugin is an installable package of harness customization.
- Depending on the harness, plugins can contain agents, skills, hooks, MCP server configuration, custom tools, integrations, environment setup, or LSP configuration.
- Plugins help teams standardize repeated setup and workflows.
- Plugins also create governance concerns: source trust, permissions, versioning, review, marketplace policy, and rollback.
- Plugin scope varies by product, so vendor-specific claims must be linked and verified.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define a plugin as packaged harness customization that turns repeated setup into something installable. | Contrast one-off setup with reusable package. |
| 0:12-0:36 | Core definition | Explain typical plugin contents: skills, agents, hooks, MCP configs, custom tools, integrations, metadata, or environment setup. | Make clear that exact contents depend on the harness. |
| 0:36-1:06 | Mechanism | Explain installation and discovery: the harness learns which capabilities exist, then decides when to load or expose them. | Include permissions and capability exposure as separate concerns. |
| 1:06-1:40 | Practical implication | Explain team standardization: same review rules, connection settings, domain skills, and safety checks can travel together. | Example: a company coding plugin packages repo review policy, secret scanning hook, and MCP server config. |
| 1:40-2:00 | Caution and handoff | Explain trust and governance: source, version, permissions, review, updates, rollback. | Handoff idea: one important thing a plugin can package is a skill. |

### References

- GitHub Copilot CLI plugins: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- OpenCode plugins: https://opencode.ai/docs/plugins/

## Video 9: What Is a Skill?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A skill is an on-demand capability bundle that gives an AI system task-specific instructions, resources, and procedures.
Learning outcome: The viewer should understand trigger descriptions, progressive disclosure, reusable procedures, supporting files, and context efficiency.

### Key Facts

- A skill is a reusable capability bundle, not merely a longer prompt.
- Skills commonly include a description, detailed instructions, and optional supporting files such as scripts, examples, references, or templates.
- The description helps decide when the skill should be used.
- Progressive disclosure means detailed instructions are loaded only when needed.
- Skills are useful when the same workflow is repeated often.
- Vague triggers or bloated instructions can waste context or activate the wrong workflow.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define a skill as a reusable procedure the AI can load when a task needs it. | Contrast repeated manual prompting with a named reusable capability. |
| 0:12-0:36 | Core definition | Explain skill anatomy: trigger description, workflow instructions, supporting resources, scripts, examples, and templates. | Mention that GitHub, Claude Code, and OpenCode each expose skills with product-specific details. |
| 0:36-1:06 | Mechanism | Explain progressive disclosure: match the task to the skill description, then load detailed instructions only when relevant. | Example: a document-generation skill loads its template only for document work. |
| 1:06-1:40 | Practical implication | Explain common skill uses: document creation, tool workflow, review process, migration recipe, data cleanup, and artifact generation. | Rule of thumb from the report: instructions pasted into chat more than three times in a month may deserve a skill. |
| 1:40-2:00 | Caution and handoff | Explain why good skills improve consistency and reduce repetition, while poor skills create confusion or context waste. | Handoff idea: external systems still need connectors, which leads to MCP. |

### References

- GitHub agent skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- Claude Code skills: https://code.claude.com/docs/en/skills
- OpenCode skills: https://opencode.ai/docs/skills/

## Video 10: What Is an MCP?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: MCP is a standard connector layer that lets AI applications access external tools and data through host, client, and server roles.
Learning outcome: The viewer should understand hosts, clients, servers, tools, resources, transports, authorization, reuse, and security responsibility.

### Key Facts

- MCP stands for Model Context Protocol.
- MCP is an open standard for connecting AI applications to external systems.
- The host is the AI application, the client lives inside the host, and the server exposes tools, resources, or prompts.
- MCP uses a protocol shape that allows capability discovery and tool or data exchange.
- Remote HTTP-based MCP authorization follows OAuth conventions; local stdio servers commonly rely on environment-provided credentials.
- MCP can reduce copy-paste context work but does not remove model cost, tool latency, authentication, consent, logging, or security responsibility.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Define MCP as a standard way for AI applications to connect to external systems. | Use examples such as files, databases, SaaS apps, ticket systems, and internal APIs. |
| 0:12-0:36 | Core definition | Explain the roles: host, client, server, tools, resources, and prompts. | Keep the role definitions short and exact. |
| 0:36-1:06 | Mechanism | Explain why a common protocol is useful: different harnesses can reuse similar connector patterns instead of every integration being custom. | Include discovery of available tools as a core concept. |
| 1:06-1:40 | Practical implication | Explain governance requirements for every MCP server: auth mode, allowed tools, user consent point, audit log, and fallback if unavailable. | Examples: GitHub issue lookup, database query, document search, local file operation. |
| 1:40-2:00 | Caution and handoff | Explain that MCP reduces integration friction but adds tool latency, external API exposure, and governance work. | Handoff idea: product choice still depends on workflow fit, not just connector availability. |

### References

- MCP introduction: https://modelcontextprotocol.io/docs/getting-started/intro
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25
- MCP authorization: https://modelcontextprotocol.io/docs/tutorials/security/authorization
- GitHub Copilot MCP: https://docs.github.com/en/copilot/concepts/context/mcp
- Claude MCP connector: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- OpenCode MCP servers: https://opencode.ai/docs/mcp-servers/

## Video 11: AI Alternatives

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: The best AI product depends on workflow context, integration surface, control model, and cost structure rather than on one universal ranking.
Learning outcome: The viewer should compare AI alternatives through task fit, context source, tool surface, governance, evaluation, and billing.

### Key Facts

- The right AI product depends on workflow fit, not a universal leaderboard.
- Atlassian Rovo is positioned around organizational knowledge, Jira, Confluence, enterprise search, chat, and agents.
- Gemini is relevant for Google productivity workflows, multimodal help, and research-oriented use cases.
- GitHub Copilot is strongest when the workflow is centered on GitHub, IDEs, CLI work, code review, and agentic coding tasks.
- Claude Desktop and Claude Code are relevant when the user wants a customizable coding-agent workflow with hooks, skills, plugins, and MCP.
- A fair comparison should ask the same questions: where is the context, what actions can it take, how are permissions handled, how is quality evaluated, and how is usage billed?
- Live prices and plan limits are unstable and must be verified immediately before final recording or purchasing decisions.

### Timeline

| Time | Beat | Required content | Examples and notes |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | Reframe the decision from "Which AI is best?" to "Which AI fits this workflow, context, control model, and budget?" | Avoid declaring one universal winner. |
| 0:12-0:36 | Core definition | Explain product centers of gravity: enterprise knowledge, productivity suite, GitHub-native coding, and customizable agent harness. | Examples: Rovo, Gemini, GitHub Copilot, Claude Desktop, Claude Code. |
| 0:36-1:06 | Mechanism | Explain a repeatable comparison checklist: context source, available actions, permission model, evaluation path, billing model, and integration surface. | Use the same criteria for each product so the comparison is fair. |
| 1:06-1:40 | Practical implication | Explain how to pilot products on real tasks: measure time saved, correction rate, permission friction, integration misses, and cost per accepted result. | Example pilot tasks: resolve a GitHub issue, summarize project knowledge, research a policy question, draft a document, migrate code. |
| 1:40-2:00 | Caution and close | Explain that prices, model access, and product capabilities change quickly, so the framework is stable but live facts must be verified. | Close with the shared series model: model, harness, tools, permissions, context, billing, and evaluation. |

### References

- Atlassian Rovo overview: https://www.atlassian.com/software/rovo
- Atlassian Rovo agents: https://support.atlassian.com/rovo/docs/agents/
- Rovo Dev CLI: https://support.atlassian.com/rovo/docs/use-rovo-dev-cli/
- Rovo pricing: https://www.atlassian.com/licensing/rovo
- Google AI plans: https://one.google.com/about/google-ai-plans/
- Gemini app limits: https://support.google.com/gemini/answer/16275805?hl=en
- GitHub Copilot features and plans: https://docs.github.com/en/copilot/get-started/features
- GitHub Copilot licenses: https://docs.github.com/en/billing/concepts/product-billing/github-copilot-licenses
- Claude Desktop installation: https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop
- Claude Code product page: https://claude.com/product/claude-code
