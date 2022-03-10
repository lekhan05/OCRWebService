import shutil
import os

def saveFileToServer(uploadedFile, path=".", saveAs="default"):
    fileOnServer = os.path.join(path, saveAs)

    with open(fileOnServer, "wb") as buffer:
        shutil.copyfileobj(uploadedFile.file, buffer)
    
    return fileOnServer

