from direct_keys import *
import time
import ctypes
from pytesseract import image_to_string
from PIL import ImageGrab, Image


class single_player_seasons():
    def __init__(self):
        time.sleep(3)
        self.games = 0
        self.ingame = True
        self.teams = 0
        self.team = team2

    def movetosecondhalf(self):
        ctypes.windll.user32.SetCursorPos(962, 323)
        press_key(0x1C, 2, 3)

    def movetosquadscreen(self):
        self.games += 1
        ctypes.windll.user32.SetCursorPos(287, 327)
        press_key(0x1C, 6, 5)
        time.sleep(5)
        if is_on_screen(bbox=newseason_box, condition='ENTRY REQUIREMENTS') is True:
            ctypes.windll.user32.SetCursorPos(287, 327)
            press_key(0x1C, 2, 5)
            ctypes.windll.user32.SetCursorPos(482, 463)
            time.sleep(2)
            press_key(0x1C, 2, 5)
            time.sleep(2)

    def fixplayerinjuries(self):
        img = ImageGrab.grab(bbox=injuredplayers_box)
        injured_players = (image_to_string(img, lang='eng'))
        injured_players_list = injured_players.split(', ')
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

    def checkfitness(self):
        if (self.games % 3) == 0:
            team_played = 0
            press_key(0xD0, 1, 3, hold_time=0.1)
            press_key(0x1C, 1, 4)
            press_key(0x20, 1, 2)
            press_key(0x1C, 1, 2)
            ctypes.windll.user32.SetCursorPos(755, 510)
            time.sleep(3)
            press_key(0x1C, 1, 10)
            team = teams[teams.index(self.team) - 1]

    def movetonextgame(self):
        press_key(0x39, 1, 3)
        press_key(0x1C, 9, 5)
        time.sleep(10)
        print("ESC")
        press_key(0x01, 1, 4)


def press_key(hex_no, amount, refresh_time, hold_time=0.5):
    for i in range(amount):
        if hex_no == 0x1C:
            print(i)
        PressKey(hex_no)
        time.sleep(hold_time)
        ReleaseKey(hex_no)
        print("a completed")
        time.sleep(refresh_time)


def is_on_screen(bbox, condition):
    screen = ImageGrab.grab()
    if (image_to_string(screen.crop(bbox), lang='eng')) == condition:
        return True
    else:
        return False


halftime_box = (938, 136, 1007, 169)
fulltime_box = (710, 88, 891, 122)
newseason_box = (1157, 259, 1360, 290)
injuredplayers_box = (480, 416, 1028, 449)
team1 = {"Otto": (779, 61), "Mello": (629, 137), "Fraser": (968, 136),
            "Marseiler": (443, 180), "Hansen": (1152, 186),
            "Fujita": (805, 244), "Scott": (447, 376), "Frantsen": (1174, 375),
            "Empereur": (661, 390), "Pask": (953, 388), "Brunst": (800, 489)}
team2 = {"Takagi": (779, 61), "Puri": (629, 137), "Edwards": (968, 136),
            "Ariza": (443, 180), "Hawkridge": (1152, 186),
            "Thorsem": (805, 244), "Bermingham": (447, 376), "Turton": (1174, 375),
            "Han Pengei": (661, 390), "Sowunmi": (953, 388), "Broda": (800, 489)}
team_loyalty = {"Zapata": (779, 61), "Luis Alberto": (629, 137), "Ramirez": (968, 136),
            "Gervinho": (443, 180), "Suso": (1152, 186),
            "Badelj": (805, 244), "Durmisi": (447, 376), "Rafael": (1174, 375),
            "Wauge": (661, 390), "Romagnoli": (953, 388), "Karnezis": (800, 489)}
teams = [team1, team2]
team = team2

# TODO restart process when disconnect occurs
# TODO fix injured players ingame


if __name__ == '__main__':
    game = single_player_seasons()
    while True:
        game.ingame = True
        if is_on_screen(halftime_box, '1.5:lll]') is True:
            game.movetosecondhalf()
            game.ingame = False
        if is_on_screen(fulltime_box, 'PLAYER RATINGS') is True:
            game.movetosquadscreen()
            game.fixplayerinjuries()
            game.checkfitness()
            game.movetonextgame()
            game.ingame = False
        if game.ingame is True:
            press_key(0x26, 1, 1)
