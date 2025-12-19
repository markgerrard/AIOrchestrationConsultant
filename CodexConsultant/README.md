# CodexConsultant

A lightweight CLI tool that allows Claude Code to consult OpenAI's Codex (GPT-5.2) for second opinions during coding sessions.

## Installation

1. Copy the script to your bin directory:
   ```bash
   mkdir -p ~/bin
   cp codex-ask ~/bin/
   chmod +x ~/bin/codex-ask
   ```

2. Ensure `~/bin` is in your PATH:
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Requires [OpenAI Codex CLI](https://github.com/openai/codex) to be installed and configured.

## Usage

```bash
# Direct question
codex-ask "What are the tradeoffs between Redis and Memcached for session storage?"

# Use a different model (e.g., gpt-5.2-codex, gpt-5.1-codex-max)
CODEX_MODEL=gpt-5.2-codex codex-ask "Explain this error"
```

## Review Patterns

Three practical ways to use "ask codex to review the changes".

Just tell Claude what you want in natural language:

| You say | Claude runs |
|---------|-------------|
| "ask codex to review the changes" | `git diff \| codex-ask "..."` |
| "ask codex about this approach" | `codex-ask "Context: ... Should we do X or Y?"` |
| "get codex's opinion on this file" | `cat file.php \| codex-ask "..."` |

### 1. Quick Diff Review (most common)

**You say:**
> "ask codex to review the changes"

**Claude runs:**
```bash
git diff | codex-ask "Review these changes for correctness, edge cases, and unintended side effects. Bullet points only."
```

What you get:
- Fast second opinion
- Catches obvious mistakes
- No ceremony

This replaces "open ChatGPT, paste diff, explain context".

### 2. Contextual Review Tied to Intent (better)

**You say:**
> "ask codex to review these changes - we're implementing the backfill for extraction, check for race conditions"

**Claude runs:**
```bash
git diff | codex-ask "Context: implementing automated extraction backfill for calls using call_latest_ai_runs as source of truth. Review this diff for schema correctness, race conditions, and scaling issues."
```

This is where Codex shines: same model, but now it understands what the change is trying to achieve.

### 3. Targeted File Review (when diff is noisy)

**You say:**
> "ask codex to review CallAiRunService - focus on the idempotency and input_hash logic"

**Claude runs:**
```bash
cat app/Services/CallAiRunService.php | codex-ask "Review this file after recent changes. Focus on idempotency, input_hash usage, and backfill safety."
```

Avoids Codex getting distracted by unrelated hunks.

## Quality Tips

Always include at least one of:
- **The goal** — what this change is for
- **The risk** — what would be bad if this is wrong

Without context, Codex defaults to generic "best practice" commentary.

## Mental Model

- **Claude (Opus)** = engineer who just wrote the code
- **Codex** = senior reviewer you tap on the shoulder
- **You** = tech lead who decides what matters

## Plan Mode Integration

When Claude is in plan mode and finishes drafting an implementation plan, it will ask:

> "Would you like me to have Codex review this plan before we proceed?"

If you say yes, Claude runs:

```bash
cat [plan-file] | codex-ask "Review this implementation plan. Check for missing steps, wrong order, architectural issues, or potential blockers."
```

You get:
1. Claude's implementation plan
2. Codex's critique (gaps, ordering, blockers)
3. Claude's interpretation of the feedback
4. Your final approval

This catches architectural mistakes before any code is written.

## Integrating with Claude Code

Add the following to your global `~/.claude/CLAUDE.md` to enable any Claude session to consult Codex:

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
3. Either include context in the question, or pipe relevant code:
   ```bash
   # Review recent changes
   git diff | codex-ask "Context: [what the change is for]. Review for correctness, edge cases, and unintended side effects."

   # Review specific file
   cat app/Services/SomeService.php | codex-ask "Review this for [specific concern]"

   # Architecture question
   codex-ask "We need X for purpose Y. Should we do A or B? Tradeoffs?"
   ```

4. After getting Codex's answer, return to the user with:
   - **Question asked** (what you sent to Codex)
   - **Codex's answer** (verbatim)
   - **My interpretation** (agree/disagree, why, context Codex may have missed)
   - **Recommended action**

5. Wait for user approval before proceeding

**Key rule:** Codex advises, Claude interprets, user decides.

**Plan mode:** When in plan mode and ready to present a plan, ask the user: "Would you like me to have Codex review this plan before we proceed?" If yes, run:

    cat [plan-file] | codex-ask "Review this implementation plan. Check for missing steps, wrong order, architectural issues, or potential blockers."

Include Codex's feedback alongside the plan before asking for user approval.
```

## How It Works

1. User tells Claude "ask codex about X"
2. Claude runs `codex-ask` with a well-formed question including context
3. Codex provides its analysis
4. Claude interprets the response, noting any disagreements or missing context
5. User makes the final decision

This creates a collaborative workflow where two AI models provide complementary perspectives.
