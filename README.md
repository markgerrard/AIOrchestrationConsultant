# AI Orchestration Tools

Tools for orchestrating collaboration between Claude and OpenAI Codex.

## Tools

### [CodexOrchestrator](./CodexOrchestrator/)
MCP server and tooling for Codex-to-Claude orchestration. Codex acts as the orchestrator/reviewer and delegates implementation tasks to Claude Opus via Model Context Protocol.

### [CodexConsultant](./CodexConsultant/)
Lightweight CLI for getting second opinions from Codex. Add to your global `~/.claude/CLAUDE.md` to enable "ask codex" in any Claude session.

## Quick Start

```bash
# Install CodexConsultant
cp CodexConsultant/codex-ask ~/bin/
chmod +x ~/bin/codex-ask

# Add CLAUDE.md integration (see CodexConsultant/README.md for full example)
```

## Requirements

- [OpenAI Codex CLI](https://github.com/openai/codex)
- Claude Code
