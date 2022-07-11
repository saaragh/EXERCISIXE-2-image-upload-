from fastapi import FastAPI, File, UploadFile
import shutil
from typing import List

app = FastAPI()

@app.post("/image")
async def image(image: UploadFile = File(...)):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {"filename": image.filename}

@app.post("/multiimage")
async def image(images: List[UploadFile] = File(...)):
    for image in images:
        with open(image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)