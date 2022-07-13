from PIL import Image 
from fastapi import FastAPI, File, UploadFile
import shutil
from typing import List
import os
from fastapi.responses import FileResponse


app = FastAPI()

@app.post("/image")
async def image(image: UploadFile = File(...)):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {"filename": image.filename}


@app.post("/grey_image/")
async def create_grey_img(file:UploadFile):
    filename= await get_image(file)
    img = Image.open(filename)
    img.convert('L').save('grey_img.jpg')
    return FileResponse("grey_img.jpg")


@app.post("/multiimage")
async def image(images: List[UploadFile] = File(...)):
    for image in images:
        with open(image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        return {"filename": image.filename}

@app.post("/grey_image_multiple/")
async def create_grey_img(file:list[UploadFile]):
    files: List[UploadFile] = File(description="Multiple files as UploadFile"):
    return {"filenames": [file.filename for file in files]}
    filename= await get_image(file)
    img = Image.open(filename)
    img.convert('L').save('grey_img.jpg')
    return FileResponse("grey_img.jpg")