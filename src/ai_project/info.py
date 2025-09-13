# src/ai_project/info.py
from datetime import UTC, datetime

from fastapi import APIRouter
from fastapi.routing import APIRoute

router = APIRouter()
STARTED_AT = datetime.now(UTC)


@router.get("/info")
def info():
    # 動態列出目前可用路由
    from .main import app  # 延遲匯入避免循環依賴

    routes = [r.path for r in app.router.routes if isinstance(r, APIRoute)]
    return {
        "version": "0.1.0",
        "started_at": STARTED_AT.isoformat(),
        "routes": sorted(routes),
    }
