"""MindReply Builder Service — R-02 Builder Corps.

POST /mr/build/asset
GET  /mr/build/assets
GET  /mr/build/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="MindReply Builder Service", version="1.0.0")

ASSETS: list[dict] = []


@app.post("/mr/build/asset")
def build_asset(data: dict) -> dict:
    asset = {
        "asset_id": f"ast-{len(ASSETS)+1}",
        "name": data.get("name", "untitled"),
        "type": data.get("type", "product"),
        "status": "CREATED",
        "source_opportunity": data.get("opportunity_id", ""),
    }
    ASSETS.append(asset)
    return asset


@app.post("/mr/build/deploy")
def deploy_asset(data: dict) -> dict:
    for a in ASSETS:
        if a["asset_id"] == data.get("asset_id"):
            a["status"] = "DEPLOYED"
            return a
    return {"error": "asset not found"}


@app.get("/mr/build/assets")
def assets() -> dict:
    return {"assets": ASSETS, "total": len(ASSETS)}


@app.get("/mr/build/status")
def status() -> dict:
    return {"service": "builder-service", "division": "R-02", "status": "healthy"}
