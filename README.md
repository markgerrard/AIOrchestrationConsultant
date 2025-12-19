# AI Orchestration Tools

Tools for orchestrating collaboration between Claude, OpenAI Codex, and Google Gemini.

## Which Tool Should I Use?

| Use case | Tool |
|----------|------|
| Backend/architecture second opinions | [CodexConsultant](./CodexConsultant/) — "ask codex" |
| UI/UX second opinions | [GeminiConsultant](./GeminiConsultant/) — "ask gemini" |
| Have Codex orchestrate and delegate to Claude Opus via MCP | [CodexOrchestrator](./CodexOrchestrator/) |

## Consultant Specializations

| Consultant | Strengths |
|------------|-----------|
| **Codex** (GPT-5.2) | Backend, data models, architecture, correctness, concurrency, performance |
| **Gemini** | UI/UX, flows, wording, affordances, accessibility, form layout |

## Tools

### [CodexConsultant](./CodexConsultant/)
Lightweight CLI for backend/architecture second opinions. Say "ask codex to review the changes" in any Claude session.

### [GeminiConsultant](./GeminiConsultant/)
Lightweight CLI for UI/UX second opinions. Say "ask gemini about this form" in any Claude session.

### [CodexOrchestrator](./CodexOrchestrator/)
MCP server for Codex-to-Claude orchestration. Codex acts as orchestrator/reviewer and delegates implementation tasks to Claude Opus.

## Quick Start: CodexConsultant

1. Install the script:
   ```bash
   mkdir -p ~/bin
   cp CodexConsultant/codex-ask ~/bin/
   chmod +x ~/bin/codex-ask
   ```

2. Ensure `~/bin` is in your PATH:
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Add to your `~/.claude/CLAUDE.md` (see [CodexConsultant/README.md](./CodexConsultant/README.md) for full example)

4. Test it:
   ```bash
   codex-ask "What are the tradeoffs between Redis and Memcached?"
   ```

## Quick Start: GeminiConsultant

1. Install the script:
   ```bash
   mkdir -p ~/bin
   cp GeminiConsultant/gemini-ask ~/bin/
   chmod +x ~/bin/gemini-ask
   ```

2. Add to your `~/.claude/CLAUDE.md` (see [GeminiConsultant/README.md](./GeminiConsultant/README.md) for full example)

3. Test it:
   ```bash
   gemini-ask "Does a 5-step onboarding flow feel like too much?"
   ```

## Quick Start: CodexOrchestrator

See [CodexOrchestrator/README.md](./CodexOrchestrator/README.md) for full setup.

## Example: Using Both Consultants Together

Here's a prompt that uses both Gemini (UI/UX) and Codex (technical) in plan mode:

```
Create a simple landing page for "Bloom Cosmetics" - a clean beauty brand. The page should have:

- Hero section with tagline and CTA button
- Featured products section (3 products)
- Newsletter signup form
- Footer with social links

Use HTML/CSS (Tailwind if available). Enter plan mode and have both Gemini review
the UI/UX and Codex review the implementation plan before we proceed. Use gemini for UI.
```

**What happens:**

1. Claude enters plan mode
2. Gemini creates UI/UX plan (copy, colors, flow, components, accessibility)
3. Claude writes implementation plan based on Gemini's UI
4. Codex reviews the technical plan (catches missing steps, accessibility gaps)
5. Claude updates plan with Codex's feedback
6. You approve the final plan

**Workflow:**

| AI | Role | What They Do |
|----|------|--------------|
| **Gemini** | UI/UX Planner | Creates copy, colors, flow, components |
| **Codex** | Technical Reviewer | Catches accessibility gaps, missing steps |
| **Claude** | Interpreter/Executor | Combines both, writes final plan |
| **You** | Decision Maker | Approves before implementation |

> **Gemini proposes UX, Codex reviews technical plan, Claude interprets and executes, user approves.**

---

## Full CLAUDE.md Example (Both Tools)

Add this to `~/.claude/CLAUDE.md` to enable both consultants:

```markdown
## Consulting Codex (GPT-5.2)

When the user says "ask codex [question]" or wants a second opinion from another AI:

**Command:** `~/bin/codex-ask`

**Common patterns:**

| User says | You run |
|-----------|---------|
| "ask codex to review the changes" | `git diff \| codex-ask "Review for correctness, edge cases, side effects..."` |
| "ask codex to review [file]" | `cat [file] \| codex-ask "Review this for [concern]..."` |
| "ask codex about [approach]" | `codex-ask "Context: [what we're doing]. Should we do X or Y? Tradeoffs?"` |

**How to use it properly:**
1. Always provide context - vague questions get wrong-for-the-situation answers
2. Include the user's stated goal or risk in your prompt to Codex
3. Either include context in the question, or pipe relevant code

4. After getting Codex's answer, return to the user with:
   - **Question asked** (what you sent to Codex)
   - **Codex's answer** (verbatim)
   - **My interpretation** (agree/disagree, why, context Codex may have missed)
   - **Recommended action**

5. Wait for user approval before proceeding

**Key rule:** Codex advises, Claude interprets, user decides.

**Plan mode:** When in plan mode and ready to present a plan, ask the user: "Would you like me to have Codex review this plan before we proceed?"

---

## Consulting Gemini (UI/UX)

When the user says "ask gemini [question]" or wants a UI/UX opinion:

**Command:** `~/bin/gemini-ask`

**Use Gemini for:** UI flows, UX clarity, wording, affordances, accessibility, form layout, error messages, copy.

**Do NOT use Gemini for:** Backend logic, schema design, performance, concurrency (use Codex instead).

**Common patterns:**

| User says | You run |
|-----------|---------|
| "ask gemini about this form" | `cat [component] \| gemini-ask "Review for UX issues..."` |
| "ask gemini if this flow makes sense" | `gemini-ask "Context: [flow description]. Does this make sense?"` |
| "ask gemini about the error messages" | `cat [file] \| gemini-ask "Review error messages for clarity..."` |

**How to use it properly:**
1. Gather relevant UI artefacts (HTML, component code, copy text)
2. Frame the question around UX, not code correctness
3. Either include artefacts in the question, or pipe them

4. After getting Gemini's answer, return to the user with:
   - **Question asked** (what you sent to Gemini)
   - **Gemini's answer** (verbatim)
   - **My interpretation** (agree/disagree, why, context Gemini may have missed)
   - **Recommended action**

5. Wait for user approval before proceeding

**Key rule:** Gemini advises, Claude interprets, user decides.

**Plan mode:** When in plan mode with UI/UX changes, ask: "Would you like me to have Gemini review the UI/UX aspects?"

**Caution:** Gemini is persuasive and will suggest subjective aesthetic "improvements". Always interpret through the lens of actual product goals.

---

## Gemini-Led UI Planning

When the user indicates Gemini should handle UI/UX planning (any variation — "gemini to do ui", "gemini ui", "ask gemini to plan the UI", "gemini should handle UX", etc.):

1. Gather relevant UI artefacts (components, routes, copy, constraints)
2. Call gemini-ask with structured planning prompt
3. Claude receives Gemini's plan and:
   - Enforces structure
   - Removes out-of-scope items
   - Adds implementation notes
   - Highlights assumptions
4. Present the plan + assumptions to user and wait for approval

**Key rule:** Gemini proposes the UX content. Claude enforces constraints and makes it executable. User approves.
```

---

## Requirements

**CodexConsultant:**
- [OpenAI Codex CLI](https://github.com/openai/codex)
- Claude Code

**GeminiConsultant:**
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- Claude Code

**CodexOrchestrator:**
- [OpenAI Codex CLI](https://github.com/openai/codex)
- Python 3.x + venv
- Claude Code
