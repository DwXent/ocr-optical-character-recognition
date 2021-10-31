import cv2
import numpy as np
import pytesseract

import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



path=r"C:\Users\oceanaTech\Desktop\img.PNG"
img = cv2.imread(path)
text = pytesseract.image_to_string(img)
print(text)


cv2.imshow("Img",img)
#cv2.waitKey(0)


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
engine.stop()
cv2.waitKey(0)

