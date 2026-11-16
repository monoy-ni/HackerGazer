import json
import logging
import time
from uuid import uuid4
from fastapi.responses import JSONResponse

logger = logging.getLogger("hackergazer.requests")

def register_logging(app):
    @app.middleware("http")
    async def requests(request, call_next):
        request.state.request_id = str(uuid4())
        start = time.monotonic()
        try:
            response = await call_next(request)
        except Exception:
            response = JSONResponse(status_code=500, content={"code": "INTERNAL_ERROR", "field_errors": {},
                                                              "request_id": request.state.request_id})
        response.headers["X-Request-ID"] = request.state.request_id
        response.headers["Cache-Control"] = "no-store"
        logger.info(json.dumps({"request_id": request.state.request_id, "method": request.method,
            "route": getattr(request.scope.get("route"), "path", "<unmatched>"),
            "status": response.status_code, "duration_ms": round((time.monotonic()-start)*1000)}))
        return response
