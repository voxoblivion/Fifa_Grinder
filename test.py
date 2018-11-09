from PIL import ImageGrab, Image
from pytesseract import image_to_string
import time
import ctypes
from direct_keys import *
from main import press_key

team1 = {"Otto": (779, 61), "Mello": (629, 137), "Fraser": (968, 136),
            "Marseiler": (443, 180), "Hansen": (1152, 186),
            "Arthur": (805, 244), "Poaty": (447, 376), "Frantsen": (1174, 375),
            "Empereur": (661, 390), "Pask": (953, 388), "Brunst": (800, 489)}
team2 = {"Takagi": (779, 61), "Puri": (629, 137), "Edwards": (968, 136),
            "Ariza": (443, 180), "Hawkridge": (1152, 186),
            "Thorsem": (805, 244), "Bermingham": (447, 376), "Turton": (1174, 375),
            "Han Pengei": (661, 390), "Sowunmi": (953, 388), "Worra": (800, 489)}
team = team1
img = ImageGrab.grab()
entryreqs_box = (1157, 259, 1360, 290)
fulltime_box = (710, 88, 891, 122)
halftime_box = (938, 136, 1007, 169)
injuredplayers_box = (480, 416, 1028, 449)
img1 = img.crop(halftime_box)

time.sleep(5)
img = ImageGrab.grab(bbox=injuredplayers_box)
injured_players = (image_to_string(img, lang='eng'))
injured_players_list = injured_players.split(', ')
print(injured_players_list)
if injured_players_list[0] in team.keys():
    press_key(0x1C, 1, 5)
    time.sleep(2)
    for i in injured_players_list:
        ctypes.windll.user32.SetCursorPos(team[i][0] + 30, team[i][1] + 30)
        time.sleep(2)
        press_key(0x1F, 1, 5)
        press_key(0x1C, 2, 5)
        press_key(0x01, 1, 5)
    press_key(0x01, 1, 5)
    press_key(0x1C, 1, 5)