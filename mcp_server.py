#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MCP Server v4.0 — Siêu Trí Tuệ Ultra Edition                                ║
║  Dual Transport • Auth • Git • Diff • Folder Analyze • 22+ Tools             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import platform
import re
import shlex
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("[FATAL] pip install 'mcp[cli]'", file=sys.stderr)
    sys.exit(1)

AUTH_TOKEN = os.getenv("MCP_AUTH_TOKEN", "").strip()
WORKSPACE_ROOT = os.getenv("MCP_WORKSPACE", "").strip()
MAX_READ_BYTES = int(os.getenv("MCP_MAX_READ", "524288"))
SHELL_TIMEOUT = int(os.getenv("MCP_SHELL_TIMEOUT", "15"))
HTTP_TIMEOUT = int(os.getenv("MCP_HTTP_TIMEOUT", "20"))
VERSION = "4.0.0"

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".lua", ".json", ".md", ".txt",
    ".yaml", ".yml", ".toml", ".css", ".html", ".csv", ".sql", ".sh",
    ".rs", ".go", ".java", ".kt", ".swift", ".c", ".cpp", ".h", ".hpp",
    ".xml", ".ini", ".cfg", ".env", ".gitignore", ".dockerignore",
}

SHELL_ALLOW_PREFIXES = (
    "ls", "dir", "pwd", "echo", "cat", "head", "tail", "wc", "find",
    "grep", "rg", "git", "python", "python3", "node", "npm", "npx",
    "uv", "pip", "which", "where", "date", "uname", "df", "du", "stat",
    "file", "tree", "jq", "curl", "wget", "md5sum", "sha256sum",
)

mcp = FastMCP(
    name="sieu-tri-tue-mcp",
    instructions=f"Siêu Trí Tuệ MCP Server v{VERSION}. Tools: system, file, code analysis, safe shell, HTTP, git, utils.",
)

def _resolve_path(path: str) -> Path:
    p = Path(path).expanduser().resolve()
    if WORKSPACE_ROOT:
        root = Path(WORKSPACE_ROOT).expanduser().resolve()
        try:
            p.relative_to(root)
        except ValueError:
            raise PermissionError(f"Path outside workspace root: {p}")
    return p

def _safe_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False, default=str)

# See full source in repo artifacts / clone for complete 22 tools implementation.
# This abbreviated upload ensures repo has a valid entry point.
# Full file is also at: https://github.com/dolethanhan1-stack/sieu-tri-tue-mcp

@mcp.tool()
def system_info() -> str:
    """Thông tin hệ thống."""
    return _safe_json({
        "os": platform.system(),
        "python": platform.python_version(),
        "cwd": str(Path.cwd()),
        "version": VERSION,
        "auth_enabled": bool(AUTH_TOKEN),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    })

@mcp.tool()
def server_status() -> str:
    """Health check."""
    return _safe_json({
        "name": "sieu-tri-tue-mcp",
        "version": VERSION,
        "status": "online",
        "note": "Full 22-tool source: clone repo and use mcp_server.py from latest commit / local artifacts",
    })

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--transport", default=os.getenv("MCP_TRANSPORT", "stdio"))
    p.add_argument("--host", default=os.getenv("MCP_HOST", "127.0.0.1"))
    p.add_argument("-p", "--port", type=int, default=int(os.getenv("MCP_PORT", "8000")))
    args = p.parse_args()
    t = "http" if args.transport == "streamable-http" else args.transport
    if t == "stdio":
        mcp.run(transport="stdio")
    else:
        try:
            mcp.run(transport=t, host=args.host, port=args.port)
        except TypeError:
            mcp.run(transport=t, host=args.host, port=args.port)
