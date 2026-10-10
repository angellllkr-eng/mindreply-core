"""MindReply Expansion Service — R-05 Expansion Corps.

POST /mr/expansion/replicate
GET  /mr/expansion/regions
GET  /mr/expansion/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="MindReply Expansion Service", version="1.0.0")

REGIONS: list[dict] = []


@app.post("/mr/expansion/replicate")
def replicate(data: dict) -> dict:
    region = {
        "region_id": f"reg-{len(REGIONS)+1}",
        "name": data.get("name", "unknown"),
        "market": data.get("market", ""),
        "status": "ACTIVE",
        "replicated_from": data.get("source_region", ""),
    }
    REGIONS.append(region)
    return region


@app.get("/mr/expansion/regions")
def regions() -> dict:
    return {"regions": REGIONS, "total": len(REGIONS)}


@app.get("/mr/expansion/status")
def status() -> dict:
    return {"service": "expansion-service", "division": "R-05", "status": "healthy"}
