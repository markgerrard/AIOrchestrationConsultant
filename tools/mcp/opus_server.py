#!/usr/bin/env python3
import os
import subprocess
import shutil
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("opus")


def run(cmd, cwd, timeout_sec: int):
    try:
        p = subprocess.run(
            cmd,
            text=True,
            cwd=cwd,
            capture_output=True,
            timeout=timeout_sec,
            stdin=subprocess.DEVNULL,
        )
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError as e:
        return 127, "", str(e)
    except subprocess.TimeoutExpired as e:
        out = e.stdout or ""
        err = e.stderr or ""
        return 124, out, (err + f"\nTimed out after {timeout_sec}s").strip()


@mcp.tool()
def opus_implement(
    instruction: str,
    repo_path: str = ".",
    resume: bool = True,
    continue_session: bool | None = None,
    timeout_sec: int = 1800,
) -> dict:
    repo_path = os.path.abspath(repo_path)

    # Headless mode (-p) so it works without a TTY.
    claude_path = shutil.which("claude") or "claude"
    cmd = [claude_path]
    # Resume/continue support varies by Claude Code version. If it errors, call with resume=false.
    #
    # Back-compat: if callers still pass continue_session, it wins.
    should_resume = continue_session if continue_session is not None else resume

    if should_resume:
        cmd += ["-c"]

    cmd += ["-p", instruction, "--dangerously-skip-permissions", "--permission-mode", "acceptEdits"]

    code, out, err = run(cmd, repo_path, timeout_sec=timeout_sec)
    return {
        "repo_path": repo_path,
        "resume": should_resume,
        "timeout_sec": timeout_sec,
        "cmd": cmd,
        "exit_code": code,
        "stdout": out[-20000:],
        "stderr": err[-20000:],
    }


if __name__ == "__main__":
    mcp.run()
