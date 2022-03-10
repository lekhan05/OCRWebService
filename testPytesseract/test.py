import pytesseract

imagePath = "test.png"

lang = "eng"

text = pytesseract.image_to_string(imagePath, lang=lang)

print(text)