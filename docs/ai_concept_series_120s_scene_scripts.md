# AI Concept Series 120-Second Scene Scripts

Status: Master planning document
Target runtime: 120 seconds per video
Audience: Technical and semi-technical viewers who use AI tools but need clearer mental models for model behavior, cost, orchestration, safety, and product choices.

This document defines the narration and required visual content for eleven 2-minute concept videos. It is a text-only production contract. It says what each video must communicate and what must appear on screen, without specifying Manim implementation details.

## Series Contract

- Language: all narration, labels, captions, and future on-screen text must be in English.
- Background: every video uses a white background.
- Duration: each video is exactly 120 seconds. This is an intentional exception to the repository default of 10 to 40 seconds because this is a master script for 2-minute production cuts.
- Structure: every video uses the same five-beat timing grid: `0:00-0:12` hook, `0:12-0:36` core definition, `0:36-1:06` mechanism, `1:06-1:40` practical implication, and `1:40-2:00` cost, caution, or handoff.
- Explanation style: every scene must explain the same idea in more than one way at the same time. Each beat should combine a primary metaphor, a structural diagram, and a concrete example or meter when possible.
- Screen division: use a consistent layout across the series. The left side carries the main conceptual diagram, the right side carries a compact example or decision checklist, and the bottom edge carries a thin progress, cost, risk, or state meter. Titles and key terms remain in a stable header area.
- Visual rhythm: each video should feel like an evolving whiteboard diagram. New information should attach to the existing structure instead of resetting the screen unless the beat changes the concept.
- Current facts: exact vendor prices, plan names, credit allowances, and product support claims must be rechecked before final recording. The scripts below avoid locking volatile numbers into narration unless the concept depends on the category.

## Shared Color Variables

Future scene code should define colors as reusable variables so the palette can be changed centrally while staying consistent across the series.

| Variable | Hex | Meaning |
| --- | --- | --- |
| `COLOR_BACKGROUND` | `#FFFFFF` | White background |
| `COLOR_TEXT` | `#1F2937` | Primary text and outlines |
| `COLOR_MUTED` | `#6B7280` | Secondary labels and inactive states |
| `COLOR_MODEL` | `#2563EB` | Model, inference, and neural computation |
| `COLOR_TOKEN` | `#F59E0B` | Tokens, prompts, context, and generated text |
| `COLOR_TOOL` | `#059669` | Tools, MCP servers, plugins, and external systems |
| `COLOR_RISK` | `#DC2626` | Risk, blocked actions, failures, unsafe paths |
| `COLOR_GUARDRAIL` | `#7C3AED` | Guardrails, policy gates, hooks, and permission checks |
| `COLOR_COST` | `#0F766E` | Billing, credits, meters, latency, and efficiency |
| `COLOR_SUCCESS` | `#16A34A` | Passing tests, accepted outputs, safe completion |

## Video 1: What Is an LLM?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: An LLM is a text-first foundation model that predicts useful continuations token by token.
Learning outcome: The viewer should understand tokens, context, next-token prediction, scale, and why hardware affects cost and latency.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "A large language model is not a magic database. It is a text-first foundation model that predicts useful continuations one token at a time." | The title "What is an LLM?" appears beside a sentence breaking into token chunks. The same idea is also shown as a model box receiving context and producing one next token. |
| 0:12-0:36 | Core definition | "The input is split into tokens: words, word pieces, punctuation, and spaces. The model reads those tokens as context, then estimates what token should come next." | The left diagram shows text becoming colored token tiles. The right panel shows a short prompt, a context window, and a ranked list of possible next tokens. The bottom meter labels input tokens and output tokens separately. |
| 0:36-1:06 | Mechanism | "After one token is chosen, it is appended to the context. Then the model repeats the same step again. A fluent answer is built from many small predictions." | A loop is visible: context, model, probability list, selected token, expanded context. The same loop is explained through an example sentence completing itself token by token. |
| 1:06-1:40 | Practical implication | "Model size, training, and the amount of context change the quality of those predictions. Larger models can capture richer patterns, but they usually require more computation." | The screen compares a small model and a large model using the same prompt. The large model has more internal parameters, a bigger compute footprint, and a higher latency or cost meter. |
| 1:40-2:00 | Cost and handoff | "That is why LLMs immediately lead to billing questions. Every prompt, every answer, and every retry turns model work into measurable usage." | The token stream feeds into a usage meter. A handoff label points to the next video: "Billing is the meter around model work." |

## Video 2: LLM Billing

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: LLM cost is driven by model work, even when products package that work as subscriptions, credits, or API tokens.
Learning outcome: The viewer should understand input tokens, output tokens, model tiers, retries, caching, tool loops, and local versus hosted costs.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "LLM billing looks confusing because products sell subscriptions, credits, and APIs. Underneath, the meter still follows model work." | Three billing badges appear: subscription, credits, and API tokens. All three connect to the same hidden usage meter. |
| 0:12-0:36 | Core definition | "The bill is shaped by what you send, what the model returns, which model you choose, and how many times the system has to try again." | The left side shows a prompt and response split into input and output tokens. The right side shows model tier, context size, retries, and tools as separate cost drivers. |
| 0:36-1:06 | Mechanism | "An agentic session can add more cost than a single chat turn because tool results, intermediate reasoning, and repeated calls all add more work." | A single-turn path is compared with an agent loop path. The loop path shows prompt, model call, tool call, observation, second model call, and final answer, while the cost meter rises in steps. |
| 1:06-1:40 | Practical implication | "Cost control usually means sending less irrelevant context, choosing the cheapest model that is good enough, caching repeated prefixes, and limiting unnecessary retries." | The same task is shown before and after cost control. The after view has trimmed context, a suitable model tier, cache reuse, and a retry cap. The output quality indicator remains acceptable. |
| 1:40-2:00 | Caution and handoff | "Local models are not free; they move cost into hardware, energy, maintenance, and latency. To predict spend, you also need to understand probability and evaluation." | Hosted billing and local infrastructure are shown as two different cost stacks. A handoff label points to "Probability explains why retries and evaluation matter." |

## Video 3: LLM Probabilities and Evaluation

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: LLM outputs are probabilistic, so evaluation must measure whether the result is good enough for the task.
Learning outcome: The viewer should understand distributions, sampling, context sensitivity, pass rates, programmatic tests, and model-based graders.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "An LLM does not retrieve one guaranteed answer. It chooses from a probability distribution over possible next tokens." | The title appears over probability bars for several candidate tokens. One token is selected while the others remain visible to show uncertainty. |
| 0:12-0:36 | Core definition | "Better context changes the distribution. It can make the useful token more likely, but it does not turn a probabilistic system into a deterministic one." | Two versions of the same prompt are compared. The vague context creates flat probability bars; the precise context creates a stronger leading answer. |
| 0:36-1:06 | Mechanism | "Evaluation wraps the model call with checks. Some checks are objective, like tests. Others are judgment-based, like a grader model or human review." | A model output enters three evaluation lanes: unit test, rubric grader, and human review. Each lane produces pass, fail, or needs review. |
| 1:06-1:40 | Practical implication | "Running multiple attempts can improve the chance of finding a passing answer, but every attempt costs time and money. pass@N is the tradeoff made visible." | Several sampled answers appear as numbered attempts. A pass counter rises, while the cost meter rises at the same time. The right panel shows "more attempts" versus "more cost." |
| 1:40-2:00 | Caution and handoff | "The right evaluation depends on the task. Code can often be tested directly. Open-ended writing needs rubrics. Agents need both, because they take actions." | A decision board maps task types to evaluation types. A handoff label points to "Agents use probabilistic calls inside action loops." |

## Video 4: What Is an Agent?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: An agent is a goal-directed system that uses model calls, context, tools, and observations to pursue an outcome.
Learning outcome: The viewer should distinguish a single prompt from an agent loop and understand autonomy, tools, stop conditions, and risk.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "An agent is not just a smarter chat reply. It is a system that pursues a goal on your behalf." | A one-shot chat bubble is contrasted with a goal card connected to a loop. The title states "Agent = goal-directed system." |
| 0:12-0:36 | Core definition | "An agent needs a goal, context, tools it can use, observations from the world, and a condition for stopping." | The screen shows five stable parts: goal, context, tools, observations, and stop condition. A concrete example task sits beside the abstract diagram. |
| 0:36-1:06 | Mechanism | "The loop is simple: decide the next step, take an action, observe the result, update context, and decide again." | The main diagram cycles through plan, act, observe, update, and stop. The right side shows the same loop as a short checklist for a coding task. |
| 1:06-1:40 | Practical implication | "Agents are useful when the path is not known in advance: research, debugging, migration, triage, and workflows that branch based on results." | Four example tasks appear as branching paths. The bottom meter shows autonomy increasing from "suggest" to "act with permission" to "act automatically." |
| 1:40-2:00 | Caution and handoff | "More autonomy increases the need for evaluation, permissions, guardrails, and observability. The agent loop needs boundaries." | The agent loop is surrounded by evaluation, permission, guardrail, and telemetry controls. A handoff label points to "Guardrails define the boundaries." |

## Video 5: What Is a Guardrail?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A guardrail is an active control that checks AI input, output, or actions against policy before harm occurs.
Learning outcome: The viewer should understand allow, block, redact, transform, ingress checks, egress checks, prompt injection, and tradeoffs.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "A guardrail is a control that blocks, redirects, or sanitizes AI behavior before damage happens." | A risky request approaches a policy gate. The gate shows four possible outcomes: allow, block, redact, and transform. |
| 0:12-0:36 | Core definition | "Guardrails turn policy into executable decisions. They can inspect user input, tool requests, retrieved context, and model output." | The screen shows checkpoints before the model, before tools, after tools, and before final output. Each checkpoint has a policy label and a decision marker. |
| 0:36-1:06 | Mechanism | "The same guardrail idea can catch different problems: prompt injection, secret leakage, unsafe actions, disallowed content, or data leaving the wrong boundary." | Several example flows pass through the same gate: injected instruction, API key, destructive command, and sensitive customer data. Each gets a different policy outcome. |
| 1:06-1:40 | Practical implication | "Good guardrails are specific. They preserve useful work while stopping the parts that violate policy or require permission." | The left side shows a bad broad block that stops everything. The right side shows a precise decision that redacts a secret, asks for permission, and allows the safe part to continue. |
| 1:40-2:00 | Caution and handoff | "Guardrails add latency and design work, but they are usually cheaper than a bad action, leaked secret, or unsafe automation. They need a place to run." | A tradeoff scale compares latency and design effort against incident cost. A handoff label points to "The harness is where controls are wired." |

## Video 6: What Is a Harness?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A harness is the runtime wrapper that turns a model into a usable product or agentic system.
Learning outcome: The viewer should understand prompts, context management, tools, permissions, MCP connections, environment, and orchestration.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "The real product is rarely just the model. It is the model plus the harness around it." | A bare model box is compared with a full stack labeled prompt, context, tools, permissions, environment, and loop. |
| 0:12-0:36 | Core definition | "A harness decides what the model sees, what tools it can call, what permissions it needs, and how the loop continues or stops." | The model sits inside a runtime frame. The frame controls incoming context, tool access, permission checks, and the stop condition. |
| 0:36-1:06 | Mechanism | "In a harness, a user request becomes structured context. The model proposes an action. The harness executes or blocks that action, then returns observations." | The main flow shows request, context builder, model call, permission check, tool execution, observation, and final response. The right panel shows the same steps as a compact state machine. |
| 1:06-1:40 | Practical implication | "The same model can behave very differently in different harnesses because the defaults, tools, memory, and policies are different." | Three harness shells surround the same model: coding assistant, enterprise search assistant, and desktop automation assistant. Each exposes different tools and permissions. |
| 1:40-2:00 | Caution and handoff | "Harness quality affects cost, safety, and reliability. Hooks are the precise interception points inside that runtime." | Cost, safety, and reliability meters attach to the harness frame. A handoff label points to "Hooks intercept specific events." |

## Video 7: What Is a Harness Hook?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A hook is an event-driven interception point inside a harness lifecycle.
Learning outcome: The viewer should understand lifecycle events, pre-tool checks, permission checks, post-tool checks, fail-open versus fail-closed behavior, and audit value.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "A hook is where the harness says: before this event continues, run this check or command." | A harness timeline pauses at a marked event. A hook card appears between the event and the next step. |
| 0:12-0:36 | Core definition | "Hooks attach behavior to lifecycle events: session start, prompt handling, tool use, permission requests, tool results, or session end." | The screen shows a horizontal lifecycle with labeled events. Several hook cards snap onto specific points, each with a different purpose. |
| 0:36-1:06 | Mechanism | "A hook receives event context, applies a rule or script, and returns a decision: continue, modify, ask, block, or log." | The same event flows through an input payload, hook logic, and decision output. The right side shows a risky shell command being blocked before execution. |
| 1:06-1:40 | Practical implication | "Hooks are useful for secrets scanning, permission enforcement, audit trails, context shaping, notifications, and team policy." | Six hook use cases appear as small cards connected to the same lifecycle. The bottom meter separates prevention, observability, and workflow automation. |
| 1:40-2:00 | Caution and handoff | "A hook that fails open may let risk pass through. A hook that fails closed may stop useful work. Plugins package hooks so teams can distribute them." | The screen compares fail-open and fail-closed outcomes. A handoff label points to "Plugins package reusable harness behavior." |

## Video 8: What Is a Harness Plugin?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A harness plugin packages reusable harness extensions so they can be installed, shared, governed, and updated.
Learning outcome: The viewer should understand plugins as distribution units for agents, skills, hooks, MCP configuration, integrations, and policy defaults.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "A plugin is a package of harness customization. It turns repeated setup into something installable." | A messy collection of separate setup cards compresses into one plugin package card. The title states "Plugin = packaged extension." |
| 0:12-0:36 | Core definition | "Depending on the harness, a plugin can include skills, agents, hooks, MCP server configuration, custom tools, or environment setup." | The plugin package opens to reveal a consistent set of contents: skill, agent, hook, MCP config, custom tool, and metadata. |
| 0:36-1:06 | Mechanism | "Installing the plugin makes the harness aware of those capabilities, but the harness still decides when to load them, ask permission, or expose tools." | The plugin feeds into a harness registry. From there, selected capabilities become visible to the model, permissions layer, and tool surface. |
| 1:06-1:40 | Practical implication | "Plugins help teams standardize workflows: the same review rules, connection settings, domain skills, and safety checks can travel together." | Two team members install the same package and receive the same configured workflow. The right panel shows version, owner, permissions, and update status. |
| 1:40-2:00 | Caution and handoff | "Plugins increase reuse, but they also need trust, versioning, review, and governance. One important thing they can package is a skill." | A governance checklist appears beside the plugin package: source, permissions, version, review, rollback. A handoff label points to "Skills are reusable procedures." |

## Video 9: What Is a Skill?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: A skill is an on-demand capability bundle that gives an AI system task-specific instructions, resources, and procedures.
Learning outcome: The viewer should understand trigger descriptions, progressive disclosure, reusable procedures, supporting files, and context efficiency.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "A skill is not just a longer prompt. It is a reusable procedure the AI can load when the task needs it." | A large prompt shrinks into a labeled skill card. The title states "Skill = reusable procedure." |
| 0:12-0:36 | Core definition | "A skill usually has a description that tells when to use it, instructions for the workflow, and optional files, scripts, examples, or templates." | The skill card opens into description, instructions, references, scripts, and templates. A task request appears beside it to show why the skill is relevant. |
| 0:36-1:06 | Mechanism | "The system first matches the task to the skill description. Then it loads the detailed instructions only when they are needed." | A task flows through a trigger matcher. Only the matching skill expands into the working context, while unrelated skills remain closed. |
| 1:06-1:40 | Practical implication | "Skills are best for repeatable work: writing a kind of document, using a tool safely, following a team process, or generating a specific artifact." | Four example skills appear as reusable drawers. Each drawer connects to a different task outcome: document, tool workflow, review process, and generated asset. |
| 1:40-2:00 | Caution and handoff | "Good skills lower repetition and improve consistency. Bad skills with vague triggers or bloated instructions can waste context. External systems still need connectors." | The screen compares a focused skill with a vague oversized skill. A handoff label points to "MCP connects AI systems to external tools and data." |

## Video 10: What Is an MCP?

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: MCP is a standard connector layer that lets AI applications access external tools and data through host, client, and server roles.
Learning outcome: The viewer should understand hosts, clients, servers, tools, resources, transports, authorization, reuse, and security responsibility.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "MCP, the Model Context Protocol, is a standard way for AI applications to connect to external systems." | The title appears over a hub-and-spoke diagram. The hub is labeled MCP, and the spokes point to files, databases, apps, and APIs. |
| 0:12-0:36 | Core definition | "The host is the AI application. The client lives inside the host. The server exposes tools, resources, or prompts from an external system." | Three labeled roles appear: host, client, and server. A simple request travels from host to client to server and back with a result. |
| 0:36-1:06 | Mechanism | "Instead of every harness inventing a custom connector, MCP gives them a common protocol shape for discovering capabilities and exchanging tool calls." | A before-and-after comparison shows many custom connectors replaced by one shared protocol pattern. The right panel shows a tool list discovered from a server. |
| 1:06-1:40 | Practical implication | "MCP matters because it makes integrations more reusable across harnesses, but every connection still needs authentication, consent, logging, and fallback behavior." | Several harnesses connect to the same MCP server. A checklist shows auth mode, allowed tools, user consent point, audit log, and fallback if unavailable. |
| 1:40-2:00 | Caution and handoff | "MCP does not remove model cost or security responsibility. It reduces copy-paste context work while adding tool latency and integration governance." | The MCP hub is surrounded by benefit and responsibility meters: less copy-paste, more tool reach, auth, audit, latency, and cost. A handoff label points to "Product choice still depends on workflow fit." |

## Video 11: AI Alternatives

Status: Master 120-second script
Target runtime: 120 seconds
Core idea: The best AI product depends on workflow context, integration surface, control model, and cost structure rather than on one universal ranking.
Learning outcome: The viewer should compare AI alternatives through task fit, context source, tool surface, governance, evaluation, and billing.

| Time | Beat | Narration | What must be shown |
| --- | --- | --- | --- |
| 0:00-0:12 | Hook | "The question is not just, which AI is best? The better question is, which AI fits this workflow, context, and control model?" | A generic trophy ranking breaks apart into four decision lenses: workflow, context, controls, and cost. |
| 0:12-0:36 | Core definition | "Different products pull toward different centers of gravity: enterprise knowledge, productivity suites, GitHub-native coding, or customizable agent harnesses." | Four product-context lanes appear: Atlassian Rovo for org knowledge, Gemini for productivity and research, GitHub Copilot for GitHub-centered coding, and Claude Desktop or Claude Code for customizable workflows. |
| 0:36-1:06 | Mechanism | "Compare alternatives by the same questions every time: where is the context, what actions can it take, how is permission handled, how is quality evaluated, and how is usage billed?" | A reusable comparison matrix fills in columns for context, actions, permissions, evaluation, and billing. The same row structure is applied to each product lane. |
| 1:06-1:40 | Practical implication | "Run pilots on real tasks, not demos. Measure time saved, correction rate, permission friction, integration fit, and cost per useful outcome." | A pilot dashboard shows real task results: completion time, human corrections, blocked actions, integration misses, and cost per accepted result. |
| 1:40-2:00 | Caution and close | "Prices, model access, and product capabilities change quickly. Keep the framework stable, but verify current facts before you buy, deploy, or record." | The comparison matrix remains stable while product facts are marked as time-sensitive. The final frame shows the series model: model, harness, tools, permissions, context, billing, and evaluation. |
