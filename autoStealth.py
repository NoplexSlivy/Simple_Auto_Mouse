# This program will click a random location on the screen

from AutoLoclick import locate
import pyautogui as auto
import keyboard as key2
import time as t
import random as rand
copy = True
bigT = input("Enter the time between clicks (in seconds): ")
print("Press q to set the locations that the cursor will click. \nPress e to start the automation. \nHold c to stop")
x = locate(.1)
base = auto.position()
while copy:
    #auto.moveTo(base[0], base[1], duration=0.1)
    num2 = rand.randint(0,len(x))
    z = x[num2-1]
    y = rand.randint(1,3)
    num = rand.randint(float(bigT),(float(bigT)+y)) #anti detection?

    auto.moveTo(z[0], z[1], duration=float(num))
    auto.click(x=None, y=None, clicks=1, interval=0, button='left')
    if key2.is_pressed('c'):
        copy = False
        break
