from PIL import ImageGrab, Image
from pytesseract import image_to_string
import time
import ctypes
from direct_keys import *

team1 = {"Otto": (779, 61), "Mello": (629, 137), "Fraser": (968, 136),
            "Marseiler": (443, 180), "Hansen": (1152, 186),
            "Fujita": (805, 244), "Poaty": (447, 376), "Frantsen": (1174, 375),
            "Empereur": (661, 390), "Pask": (953, 388), "Brunst": (800, 489)}
team2 = {"Takagi": (779, 61), "Puri": (629, 137), "Edwards": (968, 136),
            "Ariza": (443, 180), "Hawkridge": (1152, 186),
            "Thorsem": (805, 244), "Bermingham": (447, 376), "Turton": (1174, 375),
            "Han Pengei": (661, 390), "Sowunmi": (953, 388), "Worra": (800, 489)}
img = ImageGrab.grab()
entryreqs_box = (1157, 259, 1360, 290)
img3 = img.crop(entryreqs_box)
print(image_to_string(img3, lang='eng'))
d