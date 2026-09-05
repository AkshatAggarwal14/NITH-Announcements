import os
import sys

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse

# Vercel runs this as /api/index.py; make project root importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

ROOT = os.path.dirname(os.path.dirname(__file__))

import nith

app = FastAPI(title="NITH Announcements API")


@app.get("/")
async def root():
    # Legacy behaviour: Deta deployment served the list at "/",
    # so keep that to avoid breaking existing bots.
    return await get_announcements()


@app.get("/api/announcements")
async def get_announcements():
    try:
        return await nith.get_announcements()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch NITH site: {e}")


# Vercel rewrites every path to /api/index (see vercel.json), so in
# production the app always sees this path. Define it explicitly.
@app.get("/api/index")
async def vercel_entrypoint():
    return await get_announcements()


# Alias
@app.get("/announcements")
async def announcements_alias():
    return await get_announcements()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join(ROOT, "logo.png"))
