# Siêu Trí Tuệ MCP Server v4.0

Dual-transport Model Context Protocol server (stdio + Streamable HTTP).

**22 tools**: system, file ops, code analysis, git, safe shell, HTTP fetch, utils.

## Quick start

```bash
pip install "mcp[cli]"
python mcp_server.py                    # stdio
python mcp_server.py -t http --host 0.0.0.0 -p 8000   # HTTP
```

## Grok Build

```bash
grok mcp add sieu-tri-tue -- python /path/to/mcp_server.py
```

## Grok.com (HTTP + tunnel)

```bash
python mcp_server.py -t http --host 0.0.0.0 -p 8000
ngrok http 8000
# Then: grok.com/connectors → Custom → https://xxx.ngrok-free.app/mcp
```

Optional auth:
```bash
export MCP_AUTH_TOKEN="your-secret"
```

## License
MIT
