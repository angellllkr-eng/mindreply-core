"""MindReply Discovery Service — R-01 Discovery Corps.

ADR-0003: MindReply Owns Value Creation.

POST /mr/discovery/scan
GET  /mr/discovery/opportunities
GET  /mr/discovery/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="MindReply Discovery Service", version="1.0.0")

OPPORTUNITIES: list[dict] = []


@app.post("/mr/discovery/scan")
def scan(data: dict) -> dict:
    opportunity = {
        "title": data.get("title", "untitled"),
        "market": data.get("market", "unknown"),
        "signal": data.get("signal", ""),
        "status": "FOUND",
        "source": data.get("source", "unspecified"),
    }
    OPPORTUNITIES.append(opportunity)
    return opportunity


@app.get("/mr/discovery/opportunities")
def list_opportunities() -> dict:
    return {"opportunities": OPPORTUNITIES, "total": len(OPPORTUNITIES)}


@app.get("/mr/discovery/status")
def status() -> dict:
    return {"service": "discovery-service", "division": "R-01", "status": "healthy"}
