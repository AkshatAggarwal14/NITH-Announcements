import os

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse

import nith

ROOT = os.path.dirname(__file__)

app = FastAPI(title="NITH Announcements API")


async def _announcements():
    try:
        return await nith.get_announcements()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch NITH site: {e}")


@app.get("/")
@app.get("/api/index")
async def root():
    # Legacy behaviour: Deta deployment served the list at "/".
    # /api/index is the Vercel rewrite target for "/" (see vercel.json).
    return await _announcements()


@app.get("/announcements")
@app.get("/api/announcements")
async def announcements():
    return await _announcements()


@app.get("/favicon.ico")
@app.get("/api/favicon")
async def favicon():
    return FileResponse(os.path.join(ROOT, "logo.png"))
