from PIL import ImageGrab, Image
from pytesseract import image_to_string
import time
import ctypes
from direct_keys import *
from fifa19 import press_key

time.sleep(3)

team1 = {"Otto": (779, 61), "Mello": (629, 137), "Fraser": (968, 136),
            "Marseiler": (443, 180), "Hansen": (1152, 186),
            "Fujita": (805, 244), "Scott": (447, 376), "Frantsen": (1174, 375),
            "Empereur": (661, 390), "Pask": (953, 388), "Brunst": (800, 489)}
team2 = {"Takagi": (779, 61), "Puri": (629, 137), "Edwards": (968, 136),
            "Ariza": (443, 180), "Hawkridge": (1152, 186),
            "Thorsen": (805, 244), "Bermingham": (447, 376), "Turton": (1174, 375),
            "Han Pengfei": (661, 390), "Sowunmi": (953, 388), "Broda": (800, 489)}
team_loyalty = {"Lacazette": (779, 61), "Van De Beek": (629, 137), "Cesc Fabregas": (968, 136),
            "Paulinho": (443, 180), "Pedro": (1152, 186),
            "Gundogan": (805, 244), "Ordagic": (447, 376), "Pacheco": (1174, 375),
            "Laporte": (661, 390), "Sokratis": (953, 388), "Schmeichel": (800, 489)}
team = team1
res_modifier = 1.2
fulltimebox = (692, 84, 917, 121)
fulltimebox_scaled = [int(x * res_modifier) for x in fulltimebox]


def setmousepos(x, y):

    ctypes.windll.user32.SetCursorPos(int(x * res_modifier), int(y * res_modifier))

def fixplayerinjuries():
    new_injuredplayers_box = [int(x * res_modifier) for x in injuredplayers_box]
    img = ImageGrab.grab(bbox=new_injuredplayers_box)
    img.save(fp="a", format="png")
    injured_players = (image_to_string(img, lang='eng'))
    injured_players_list = injured_players.split(', ')
    if injured_players_list[0] in team.keys():
        print(injured_players_list)
        press_key(0x1C, 1, 5)
        time.sleep(2)
        for i in injured_players_list:
            setmousepos(x=int(team[i][0] + 30), y=int(team[i][1] + 30))
            time.sleep(2)
            press_key(0x1F, 1, 5)
            press_key(0x1C, 2, 5)
            press_key(0x01, 1, 5)
        press_key(0x01, 1, 5)
        press_key(0x1C, 1, 5)
    print("PLAYER INJURERS SORTED")


img = ImageGrab.grab(bbox=(645, 108, 890, 150))
img.save(fp="a", format="png")