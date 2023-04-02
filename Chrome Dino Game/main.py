import pyautogui 
from PIL import ImageGrab 
import time


def isCollision(data):
    for i in range(530,560):
        for j in range(80, 127):
            if data[i, j] < 171:
                pyautogui.press("down")
                return 

    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] < 100:
                pyautogui.press("space")
                return 
    return


time.sleep(5)
pyautogui.press('up') 
t=30

while t:
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    isCollision(data)
    t-=1
        