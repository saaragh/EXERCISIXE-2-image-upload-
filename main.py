from fileinput import filename
from fastapi import FastAPI,File,UploadFile
from typing import List 
from PIL import Image 
from fastapi.responses import FileResponse 
import shutil
from werkzeug.utils import secure_filename


app = FastAPI()

@app.post("/image")
async def get_image(image: UploadFile = File("single image uploaded")):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {"filename": image.filename}

@app.post("/uploadfiles/")
async def Multiple_files(files: List[UploadFile] = File(),):
    return {"filenames": [file.filename for file in files]}


@app.post("/grey_image/")
async def create_grey_img(file:UploadFile):
    filename= await get_image(file)
    image = Image.open(filename)
    image.convert('L').save('grey_img.jpg')
    return FileResponse("grey_img.jpg")
            