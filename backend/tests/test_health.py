import logging
from app.api import health

def test_liveness_has_request_id(client):
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"
    assert r.headers["X-Request-ID"] and r.headers["Cache-Control"] == "no-store"

def test_readiness_success_and_failure(client, monkeypatch):
    monkeypatch.setattr(health, "readiness_checks", lambda: {"database": "ok", "schema": "ok"})
    assert client.get("/ready").status_code == 200
    monkeypatch.setattr(health, "readiness_checks", lambda: {"database": "unavailable", "schema": "unavailable"})
    assert client.get("/ready").status_code == 503

def test_no_placeholder_business_routes(client):
    r = client.get("/apps")
    assert r.status_code == 404 and r.json()["code"] == "HTTP_ERROR"
    assert r.json()["request_id"] == r.headers["X-Request-ID"]

def test_request_logs_exclude_query(client, caplog):
    caplog.set_level(logging.INFO, logger="hackergazer.requests")
    client.get("/health?token=secret-test-value")
    assert "secret-test-value" not in caplog.text

def test_cors(client):
    r = client.options("/health", headers={"Origin": "http://localhost:5173", "Access-Control-Request-Method": "GET"})
    assert r.headers["access-control-allow-origin"] == "http://localhost:5173"


def test_frontend_loopback_origin(client):
    r = client.options("/health", headers={"Origin": "http://127.0.0.1:5173", "Access-Control-Request-Method": "GET"})
    assert r.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"
