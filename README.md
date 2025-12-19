# AI Orchestration Tools

Tools for orchestrating collaboration between Claude and OpenAI Codex.

## Which Tool Should I Use?

| Use case | Tool |
|----------|------|
| Get second opinions from Codex during Claude Code sessions | [CodexConsultant](./CodexConsultant/) |
| Have Codex orchestrate and delegate implementation to Claude Opus via MCP | [CodexOrchestrator](./CodexOrchestrator/) |

## Tools

### [CodexConsultant](./CodexConsultant/)
Lightweight CLI for getting second opinions from Codex. Say "ask codex to review the changes" in any Claude session.

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

## Quick Start: CodexOrchestrator

See [CodexOrchestrator/README.md](./CodexOrchestrator/README.md) for full setup.

## Requirements

**CodexConsultant:**
- [OpenAI Codex CLI](https://github.com/openai/codex)
- Claude Code

**CodexOrchestrator:**
- [OpenAI Codex CLI](https://github.com/openai/codex)
- Python 3.x + venv
- Claude Code
