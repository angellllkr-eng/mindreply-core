"""MindReply Commerce Service — R-03 Commerce Corps.

GET  /mr/commerce/revenue
POST /mr/commerce/offer
GET  /mr/commerce/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="MindReply Commerce Service", version="1.0.0")

STATE = {"revenue": 0.0, "offers": 0, "clients": 0}


@app.get("/mr/commerce/revenue")
def revenue() -> dict:
    return {**STATE}


@app.post("/mr/commerce/offer")
def offer(data: dict) -> dict:
    amount = float(data.get("amount", 0))
    STATE["revenue"] += amount
    STATE["offers"] += 1
    if data.get("new_client"):
        STATE["clients"] += 1
    return {"status": "accepted", "revenue": STATE["revenue"]}


@app.get("/mr/commerce/status")
def status() -> dict:
    return {"service": "commerce-service", "division": "R-03", "status": "healthy"}
