from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.responses import JSONResponse

def register_errors(app):
    @app.exception_handler(HTTPException)
    async def http_error(request, exc):
        detail = exc.detail if isinstance(exc.detail, dict) else {}
        return JSONResponse(status_code=exc.status_code, headers=exc.headers,
            content={"code": detail.get("code", "HTTP_ERROR"), "field_errors": detail.get("field_errors", {}),
                     "request_id": request.state.request_id})
    @app.exception_handler(RequestValidationError)
    async def validation_error(request, exc):
        return JSONResponse(status_code=422, content={"code": "FIELD_INVALID",
            "field_errors": {".".join(map(str, e["loc"])): {"code": e["type"]} for e in exc.errors()},
            "request_id": request.state.request_id})
