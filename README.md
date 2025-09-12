# AI Project

Minimal API + CLI + Tests
- Start API: `uv run server`
- Health check: `GET /health` → `{"status": "ok"}`
- CLI examples:
  - `uv run ai-cli preprocess`
  - `uv run ai-cli train`
  - `uv run ai-cli infer --x 7`
- Run tests: `uv run pytest -q`

Folder layout

src/ai_project/
main.py # FastAPI app with /health
cli.py # Typer CLI
server.py # uvicorn entry (uv run server)
tests/
test_app.py # API test
test_cli.py # CLI test
