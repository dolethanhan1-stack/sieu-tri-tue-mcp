# Siêu Trí Tuệ MCP Server v4.0

**22 tools** · Dual transport (stdio + Streamable HTTP) · Git · File · Code analysis · Safe shell

**Repo:** https://github.com/dolethanhan1-stack/sieu-tri-tue-mcp

## Install

```bash
git clone https://github.com/dolethanhan1-stack/sieu-tri-tue-mcp.git
cd sieu-tri-tue-mcp
pip install "mcp[cli]"
```

Full `mcp_server.py` (1560 lines) — nếu trên GitHub còn stub, copy file đầy đủ từ máy rồi:

```bash
git add mcp_server.py && git commit -m "Full MCP v4.0" && git push
```

## Run

```bash
# Stdio
python mcp_server.py

# HTTP
export MCP_AUTH_TOKEN="optional-secret"
python mcp_server.py -t http --host 0.0.0.0 -p 8000
# → http://localhost:8000/mcp
```

## Gắn vào Grok

### A) Grok Build (CLI) — stdio, khuyến nghị

```bash
grok mcp add sieu-tri-tue -- python /absolute/path/to/mcp_server.py
grok mcp list
grok mcp doctor sieu-tri-tue
```

Hoặc `~/.grok/config.toml`:

```toml
[mcp_servers.sieu-tri-tue]
command = "python"
args = ["/absolute/path/to/mcp_server.py"]
```

### B) grok.com Connectors (HTTP)

```bash
python mcp_server.py -t http --host 0.0.0.0 -p 8000
ngrok http 8000
```

1. https://grok.com/connectors  
2. New Connector → Custom  
3. URL: `https://xxxx.ngrok-free.app/mcp`  
4. Auth (nếu có): `Authorization: Bearer <token>`

### C) Grok API

```python
from xai_sdk import Client
from xai_sdk.tools import mcp
client = Client(api_key="YOUR_XAI_KEY")
chat = client.chat.create(
    model="grok-4",
    tools=[mcp(server_url="https://your-public-url/mcp", server_label="sieu-tri-tue")],
)
```

## 22 Tools

| Group | Tools |
|-------|-------|
| System | system_info, server_status, current_time |
| File | list_directory, directory_tree, find_files, read_file_safe, write_file_safe, search_in_files, diff_files |
| Code | analyze_code_structure, analyze_folder |
| Git | git_status, git_log, git_diff, git_branch |
| Shell/Net | run_command_safe, http_fetch |
| Utils | calc, hash_text, base64_tool, uuid_gen |

## Env

- `MCP_AUTH_TOKEN` — Bearer (HTTP)
- `MCP_WORKSPACE` — chroot path
- `MCP_TRANSPORT` / `MCP_HOST` / `MCP_PORT`

MIT
