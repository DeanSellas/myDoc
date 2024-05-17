import io

from typing import Annotated, Union

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles

from PyPDF2 import PdfReader

app = FastAPI(title="Homepage")
appAPI = FastAPI(title="API")

app.mount("/api", appAPI)
app.mount("/", StaticFiles(directory="../www", html=True), name="www")

@appAPI.post("/file/")
async def readFile(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail={"message": "bad file type"})
    reader = PdfReader(io.BytesIO(file.file.read()))
    pdfContent = ""

    for page in reader.pages:
        pdfContent += f"{page.extract_text()}"

    return {"file_name": f"{file.filename}", "pages": len(reader.pages), "content": f"{pdfContent}"}