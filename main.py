from fastapi import FastAPI
from starlette.responses import FileResponse
import nith
# from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Announcement API")
# app = FastAPI(title="Announcement API", redoc_url="/")

URL = 'https://nith.ac.in/'


@app.get("/")
async def get_announcements():
    resp = await nith.get_announcements(URL)
    return resp


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("nith_announcements/logo.png")


# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Announcement API",
#         version="1.0",
#         description="",
#         routes=app.routes,
#     )
#     print(openapi_schema["info"])
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://i.ibb.co/zhW9Q8c/logo.png"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


# app.openapi = custom_openapi
