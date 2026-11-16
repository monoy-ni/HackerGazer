from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text
from alembic.config import Config
from alembic.script import ScriptDirectory
from app.db.session import get_engine

router = APIRouter(tags=["Health"])

@router.get("/health")
def health():
    return {"status": "ok", "service": "HackerGazer", "version": "0.1.0"}

def readiness_checks():
    checks = {"database": "unavailable", "schema": "unavailable"}
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
            checks["database"] = "ok"
            versions = set(connection.execute(text("SELECT version_num FROM alembic_version")).scalars())
            root = Path(__file__).resolve().parents[2]
            cfg = Config(str(root / "alembic.ini"))
            cfg.set_main_option("script_location", str(root / "migrations"))
            head = ScriptDirectory.from_config(cfg).get_current_head()
            checks["schema"] = "ok" if versions == {head} else "outdated"
    except Exception:
        pass
    return checks

@router.get("/ready")
def ready():
    checks = readiness_checks()
    ok = all(value == "ok" for value in checks.values())
    return JSONResponse(status_code=200 if ok else 503, headers={"Cache-Control": "no-store"},
                        content={"status": "ready" if ok else "not_ready", "checks": checks})
