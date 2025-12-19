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
| **Gemini** (3 Pro) | UI/UX, flows, wording, affordances, accessibility, form layout |

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
