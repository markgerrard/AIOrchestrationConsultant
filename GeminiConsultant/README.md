# GeminiConsultant

A lightweight CLI helper that lets Claude Code consult Google Gemini 3 Pro for UI/UX second opinions during coding sessions.

## What This Solves

When you're working on UI and want a specialist opinion, you can say:
- "ask gemini about this UI flow"
- "ask gemini to review the form layout"

…and Claude will run Gemini locally and return:
- The exact question asked
- Gemini's answer (verbatim)
- Claude's interpretation
- Recommended next step
- Then wait for your approval

## When to Use Gemini vs Codex

| Consultant | Use for |
|------------|---------|
| **Codex** (GPT-5.2) | Backend, data models, architecture, correctness, concurrency |
| **Gemini** (3 Pro) | UI/UX, flows, wording, affordances, accessibility |

**Good uses for Gemini:**
- "Does this UI flow make sense?"
- "Are we missing an obvious affordance?"
- "Is this wording confusing?"
- "Does this error state explain what the user should do?"
- "Is this form layout accessible / scannable?"

**Keep with Codex:**
- Backend logic
- Schema design
- Idempotency
- Concurrency
- Performance

## Installation

1. Put the script on PATH:
   ```bash
   mkdir -p "$HOME/bin"
   cp gemini-ask "$HOME/bin/gemini-ask"
   chmod +x "$HOME/bin/gemini-ask"
   ```

2. Ensure `~/bin` is in your PATH:
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Requires [Gemini CLI](https://github.com/google-gemini/gemini-cli) to be installed and configured.

## Usage

```bash
# Direct UX question
gemini-ask "Does this login flow have too many steps?"

# Pipe HTML/component for review
cat resources/views/checkout.blade.php | gemini-ask "Review this checkout form for UX issues and accessibility"

# Use a different model
GEMINI_MODEL=gemini-3-flash gemini-ask "Quick check: is this button label clear?"
```

## Review Patterns

Just tell Claude what you want in natural language:

| You say | Claude runs |
|---------|-------------|
| "ask gemini about this form" | `cat form.html \| gemini-ask "..."` |
| "ask gemini if this flow makes sense" | `gemini-ask "Context: ... Does this flow make sense?"` |
| "get gemini's opinion on the error messages" | `cat errors.blade.php \| gemini-ask "..."` |

### 1. Component Review

**You say:**
> "ask gemini to review the checkout form"

**Claude runs:**
```bash
cat resources/views/checkout.blade.php | gemini-ask "Review this checkout form for UX clarity, accessibility, and missing affordances."
```

### 2. Flow Critique

**You say:**
> "ask gemini if this onboarding flow makes sense"

**Claude runs:**
```bash
gemini-ask "Context: User onboarding flow is: 1) Email signup 2) Verify email 3) Set password 4) Choose plan 5) Add payment. Does this flow make sense? Are we asking too much upfront?"
```

### 3. Copy Review

**You say:**
> "ask gemini if this error message is clear"

**Claude runs:**
```bash
gemini-ask "Review this error message for clarity: 'Your session has expired. Please refresh and try again.' Does it explain what the user should do?"
```

## Important: Keep Gemini Stateless

Just like Codex:
- Don't resume Gemini sessions
- Don't let it accumulate narrative
- Give it artefacts + intent
- Get an unbiased critique

You want: "A designer walking in cold and reacting honestly."

Not: "A designer defending their previous opinions."

## Plan Mode Integration

When Claude is in plan mode with UI/UX changes and finishes drafting a plan, it will ask:

> "Would you like me to have Gemini review the UI/UX aspects of this plan?"

If you say yes, Claude runs:

```bash
cat [plan-file] | gemini-ask "Review the UI/UX aspects of this plan. Check for missing user flows, accessibility concerns, confusing interactions, or UX anti-patterns."
```

You get:
1. Claude's implementation plan
2. Gemini's UX critique (flows, accessibility, interactions)
3. Claude's interpretation of the feedback
4. Your final approval

This catches UX issues before any code is written.

## Gemini-Led UI Planning

When you want Gemini to take the lead on UI/UX planning, just say it however feels natural:

- "gemini ui"
- "gemini to do ui"
- "ask gemini to plan the UI"
- "gemini should handle UX"
- Any variation works — Claude understands intent, or asks for clarification if unclear

**What happens:**

1. Claude gathers relevant UI artefacts (components, routes, copy)
2. Gemini generates a structured UI plan:
   - User goals (3 bullets max)
   - Primary flow (numbered steps)
   - Alternate/error flows
   - Screens/components needed
   - Copy changes (exact strings)
   - Accessibility checklist
   - Open questions / assumptions

3. Claude enforces constraints:
   - Removes out-of-scope items
   - Adds implementation notes
   - Highlights assumptions
   - Writes to `PLAN_UI.md`

4. You approve before implementation

**Why this structure:**

If Gemini runs fully unconstrained, you get:
- Nice-looking flows
- Lots of subjective polish suggestions
- Occasional missed technical constraints
- Scope creep

With Claude as the gate:
- Gemini proposes the UX content
- Claude enforces constraints and makes it executable
- You approve

**Key rule:** Gemini proposes. Claude gates. User decides.

## Caution

Gemini is persuasive. It will confidently suggest "improvements" that are:
- Subjective
- Aesthetic
- Not aligned with your product goals

That's why Claude interpreting Gemini's feedback is critical.

**The invariant holds:**

> Gemini advises. Claude interprets. User decides.

Don't let Gemini directly drive changes.

## Mental Model

- **Claude (Opus)** = engineer who just wrote the code
- **Codex** = backend/architecture reviewer
- **Gemini** = UX/UI specialist you tap on the shoulder
- **You** = product owner who decides what matters

## Integrating with Claude Code

Add the following to your global `~/.claude/CLAUDE.md`:

```markdown
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
3. Run gemini-ask with explicit UX framing

4. After getting Gemini's answer, return to the user with:
   - **Question asked** (what you sent to Gemini)
   - **Gemini's answer** (verbatim)
   - **My interpretation** (agree/disagree, why, context Gemini may have missed)
   - **Recommended action**

5. Wait for user approval before proceeding

**Key rule:** Gemini advises, Claude interprets, user decides.
```
