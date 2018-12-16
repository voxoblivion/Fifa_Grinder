from PIL import ImageGrab, Image
from pytesseract import image_to_string
import time
import ctypes
from direct_keys import *
from main import press_key

config = open("Config.txt")
resolution = [int(x) for x in config.readline().split("=")[1].split("x")]
print(resolution)
