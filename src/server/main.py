from typing import Annotated, Union

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Homepage")
appAPI = FastAPI(title="API")

app.mount("/api", appAPI)
app.mount("/", StaticFiles(directory="../www", html=True), name="www")

@appAPI.post("/file/")
async def readFile(file: UploadFile):
    if file.content_type != "application/pdf":
        return {"error": "true"}
    return {"file_name": f"{file.filename}"}