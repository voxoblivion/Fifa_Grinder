from direct_keys import *
import time
import ctypes
from pytesseract import image_to_string
from PIL import ImageGrab, Image
import re

'''
With the removal of single player seasons in fifa 20 a new gamemode had to used the most viable being single player friendlies
the main advantage being is there is no limit on the number of games that can be played however no coin bonus is achieved
If 0-0 by 90 mins the game goes to extra time then penos
Players no longer get injured. decrease in fitness or count towards their contract
Rare occurrence where GK gets red carded - play no rules match
Reset game every 12 hours in order to deal with disconnect 
'''


class single_player_seasons():
    def __init__(self):
        time.sleep(3)
        self.ingame = True
        self.resolution = 0
        self.res_modifier = 0

    def setTeam(self, team):
        self.team = team

    def setmousepos(self, x, y):
        ctypes.windll.user32.SetCursorPos(int(x * self.res_modifier), int(y * self.res_modifier))

    def gotonextstage(self):
        self.setmousepos(962, 323)
        press_key(0x1C, 2, 3)

    def playpenalties(self):
        press_key(0x1C, 2, 3)
        while True:
            if self.is_on_screen(fulltime_box, 'PLAYER RATINGS') is True:
                break
            press_key(0x39, 1, 1)

    def movetosquadscreen(self):
        self.setmousepos(287, 327)
        press_key(0x1C, 5, 7)
        time.sleep(5)
        print("SQUAD SCREEN")

    def get_settings(self):
        config = open("Config.txt")
        self.resolution = [int(x) for x in config.readline().split("=")[1].split("x")]
        print(self.resolution)
        config.close()

    def movetonextgame(self):
        press_key(0x1C, 6, 5)
        time.sleep(10)
        press_key(0x01, 1, 4)
        print("GAME STARTED " + time.strftime("%H:%M:%S"))

    def is_on_screen(self, bbox, conditions):
        new_bbox = [int(x * self.res_modifier) for x in bbox]
        screen = ImageGrab.grab()
        screen_text = (image_to_string(screen.crop(new_bbox), lang='eng'))
        if screen_text != "":
            print(screen_text, str(bbox))
            for condition in conditions:
                if condition in screen_text:
                    return True
        else:
            return False


def press_key(hex_no, amount, refresh_time, hold_time=0.5):
    for i in range(amount):
        PressKey(hex_no)
        time.sleep(hold_time)
        ReleaseKey(hex_no)
        time.sleep(refresh_time)


halftime_box = (645, 108, 890, 150)
fulltime_box = (830, 100, 1100, 145)
injuredplayers_box = (480, 416, 1028, 449)


# TODO restart process when disconnect occurs

if __name__ == '__main__':
    game = single_player_seasons()
    game.get_settings()
    game.res_modifier = game.resolution[0] / 1920
    while True:
        game.ingame = True
        if game.is_on_screen(halftime_box, ['MATCH FACTS']) is True:
            game.gotonextstage()
            game.ingame = False
        if game.is_on_screen(fulltime_box, ['PLAYER RATINGS']) is True:
            game.movetosquadscreen()
            game.movetonextgame()
            game.ingame = False
        if game.ingame is True:
            press_key(0x26, 1, 1)

'''
lllllllllllllllllLLLllllllllllllllllllllllll l
l


  l
'''
'''
time.sleep(3)
game = single_player_seasons()
game.team = team2
game.get_settings()
game.res_modifier = game.resolution[0] / 1600
game.fixplayerinjuries()
game.games = 2
game.checkfitness()l
'''
