import pytesseract
import asyncio

async def readImage(imagePath, lang='eng'):
    try:
        text = pytesseract.image_to_string(imagePath, lang= lang)
        return text
    except:
        return "[Error] Unable to process the file: {0}".format(imagePath)