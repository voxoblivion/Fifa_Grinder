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
        self.team = team_loyalty
        self.team_list = [team1, team2]
        self.resolution = 0
        self.res_modifier = 0

    def setmousepos(self, x, y):
        ctypes.windll.user32.SetCursorPos(int(x * self.res_modifier), int(y * self.res_modifier))

    def movetosecondhalf(self):
        self.setmousepos(962, 323)
        press_key(0x1C, 2, 3)

    def movetosquadscreen(self):
        self.games += 1
        self.setmousepos(287, 327)
        press_key(0x1C, 6, 10)
        time.sleep(5)
        if is_on_screen(bbox=newseason_box, condition='ENTRY REQUIREMENTS') is True:
            self.setmousepos(287, 327)
            press_key(0x1C, 2, 5)
            self.setmousepos(482, 463)
            time.sleep(2)
            press_key(0x1C, 2, 5)
            time.sleep(2)
        print("SQUAD SCREEN")

    def get_settings(self):
        config = open("Config.txt")
        self.resolution = [int(x) for x in config.readline().split("=")[1].split("x")]
        print(self.resolution)
        config.close()


    def fixplayerinjuries(self):
        img = ImageGrab.grab(bbox=injuredplayers_box)
        injured_players = (image_to_string(img, lang='eng'))
        injured_players_list = injured_players.split(', ')
        if injured_players_list[0] in self.team.keys():
            print(injured_players_list)
            press_key(0x1C, 1, 5)
            time.sleep(2)
            for i in injured_players_list:
                self.setmousepos(self.team[i][0] + 30, self.team[i][1] + 30)
                time.sleep(2)
                press_key(0x1F, 1, 5)
                press_key(0x1C, 2, 5)
                press_key(0x01, 1, 5)
            press_key(0x01, 1, 5)
            press_key(0x1C, 1, 5)
        print("PLAYER INJURERS SORTED")

    def checkfitness(self):
        if (self.games % 2) == 0 and len(self.team_list) > 1:
            press_key(0xD0, 1, 3, hold_time=0.1)
            press_key(0x1C, 1, 4)
            press_key(0x20, 1, 2)
            press_key(0x1C, 1, 2)
            time.sleep(5)
            self.setmousepos(755, 510)
            time.sleep(3)
            press_key(0x1C, 1, 10)
            self.team = self.team_list[self.team_list.index(self.team) - 1]
            print(self.team)
            print("TEAM SWITCHED")

    def movetonextgame(self):
        press_key(0x39, 1, 3)
        press_key(0x1C, 9, 5)
        time.sleep(20)
        press_key(0x01, 1, 4)
        print("GAME STARTED")


def press_key(hex_no, amount, refresh_time, hold_time=0.5):
    for i in range(amount):
        PressKey(hex_no)
        time.sleep(hold_time)
        ReleaseKey(hex_no)
        time.sleep(refresh_time)


def is_on_screen(bbox, condition):
    new_bbox = [int(x * game.res_modifier) for x in bbox]
    screen = ImageGrab.grab()
    screen_text = (image_to_string(screen.crop(new_bbox), lang='eng'))
    if screen_text != "":
        print(screen_text, str(bbox))
        if screen_text == condition:
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
            "Thorsen": (805, 244), "Bermingham": (447, 376), "Turton": (1174, 375),
            "Han Pengfei": (661, 390), "Sowunmi": (953, 388), "Broda": (800, 489)}
team_loyalty = {"Lacazette": (779, 61), "Van De Beek": (629, 137), "Cesc Fabregas": (968, 136),
            "Paulinho": (443, 180), "Pedro": (1152, 186),
            "Gundogan": (805, 244), "Ordagic": (447, 376), "Pacheco": (1174, 375),
            "Laporte": (661, 390), "Sokratis": (953, 388), "Schmeichel": (800, 489)}
teams = [team1, team2]

# TODO restart process when disconnect occurs
# TODO fix injured players ingame
'''
Issue occurs when game has been running for a while and key presses no longer function 
as intended. Could be fixed with a soft reset.
'''

if __name__ == '__main__':
    game = single_player_seasons()
    game.team = team1
    game.get_settings()
    game.res_modifier = game.resolution[0]/1600
    while True:
        game.ingame = True
        if is_on_screen(halftime_box, '43:Ul') is True:
            game.movetosecondhalf()
            game.ingame = False
        if is_on_screen(fulltime_box, 'I’LHIEK lU-ll II‘UJ') is True:
            game.movetosquadscreen()
            game.fixplayerinjuries()
            game.checkfitness()
            game.movetonextgame()
            game.ingame = False
        if game.ingame is True:
            press_key(0x26, 1, 1)
'''
lllllllllllllllllLLLlllllllllll
'''