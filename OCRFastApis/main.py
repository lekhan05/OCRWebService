from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import asyncio
from imageReader import imageReader
from utils import utils


app = FastAPI()

@app.get("/")
def home():
    return {"Welcome!":"Use the endpoint /api/extracttext to perform OCR."}

@app.post("/api/extracttext")
async def extractText(images : List[UploadFile] = File(...)):
    response = {}
    start = time.time()
    tasks = []
    for img in images:
        print("uploading image", img.filename)
        uploadedFile = utils.saveFileToServer(img, path="./", saveAs=img.filename)
        tasks.append(asyncio.create_task(imageReader.readImage(uploadedFile)))

    ocrResults = await asyncio.gather(*tasks)
    for i in range(len(ocrResults)):
        response[images[i].filename] = ocrResults[i]
    end = time.time()
    response["elapsedTime"] = round((end - start), 2)

    return response

