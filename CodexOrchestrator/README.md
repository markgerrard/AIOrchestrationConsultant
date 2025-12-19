# CodexOrchestration

Portable AI tooling for orchestrating Claude/Codex with an Opus implementation layer.

## Structure

```
tools/
├── codex-opus              # Entrypoint wrapper (policy layer)
└── mcp/
    ├── opus_server.py      # MCP server (execution layer)
    ├── requirements.txt    # Python dependencies
    └── codex.config.example.toml  # Sample config
```

## Installation

1. Clone this repo
2. Create venv and install deps:
   ```bash
   cd tools/mcp
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy example config to `~/.codex/config.toml` and adjust paths
4. Add `tools/codex-opus` to your PATH
5. Run: `codex-opus`

## Usage

- **THINK** (default): Codex orchestrates, plans, reviews - no file modifications
- **IMPLEMENT**: Calls Opus (via MCP) to implement, resumes session
- **IMPLEMENT FRESH**: Calls Opus to implement, fresh session

Codex = orchestrator/reviewer
Opus = implementer (via `opus_implement` MCP tool)

All implementations auto-append to `CHANGELOG.md`.
