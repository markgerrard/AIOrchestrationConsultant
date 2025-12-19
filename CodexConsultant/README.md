# CodexConsultant

A lightweight CLI tool that allows Claude Code to consult OpenAI's Codex (GPT-5.2) for second opinions during coding sessions.

## Installation

1. Copy the script to your bin directory:
   ```bash
   cp codex-ask /home/forge/bin/
   chmod +x /home/forge/bin/codex-ask
   ```

2. Ensure `/home/forge/bin` is in your PATH:
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Requires [OpenAI Codex CLI](https://github.com/openai/codex) to be installed and configured.

## Usage

```bash
# Direct question
codex-ask "What are the tradeoffs between Redis and Memcached for session storage?"

# Pipe code for review
cat src/auth.py | codex-ask "Review this for security vulnerabilities"

# Detailed review with specific focus areas
cat app/Services/CallAiRunService.php | codex-ask "Review this file after recent changes. Focus on idempotency, input_hash usage, and backfill safety."

# Use a different model (e.g., gpt-5.2-codex, gpt-5.1-codex-max)
CODEX_MODEL=gpt-5.2-codex codex-ask "Explain this error"
```

## Integrating with Claude Code

Add the following to your global `~/.claude/CLAUDE.md` to enable any Claude session to consult Codex:

```markdown
## Consulting Codex (GPT-5.2)

When the user says "ask codex [question]" or wants a second opinion from another AI:

**Command:** `/home/forge/bin/codex-ask`

**How to use it properly:**
1. Always provide context - vague questions get wrong-for-the-situation answers
2. Either include context in the question, or pipe relevant code:
   ```bash
   # With inline context
   codex-ask "We need X for purpose Y. Should we do A or B? Tradeoffs?"

   # With piped code
   cat app/Services/SomeService.php | codex-ask "Review this for [specific concern]"
   ```

3. After getting Codex's answer, return to the user with:
   - **Question asked** (what you sent to Codex)
   - **Codex's answer** (verbatim)
   - **My interpretation** (agree/disagree, why, context Codex may have missed)
   - **Recommended action**

4. Wait for user approval before proceeding

**Key rule:** Codex advises, Claude interprets, user decides.
```

## How It Works

1. User tells Claude "ask codex about X"
2. Claude runs `codex-ask` with a well-formed question including context
3. Codex provides its analysis
4. Claude interprets the response, noting any disagreements or missing context
5. User makes the final decision

This creates a collaborative workflow where two AI models provide complementary perspectives.
