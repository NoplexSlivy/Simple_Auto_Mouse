from AutoLoclick import locate
import pyautogui as auto
import keyboard as key2
import time as t
copy = True
bigT = input("Enter the time between clicks (in seconds): ")
print("Press q to set the locations that the cursor will click. \nPress e to start the automation. \nHold c to stop")
x = locate(.1)
while copy:
    for i in x:
        auto.click(i)
        t.sleep(float(bigT))
    if key2.is_pressed('c'):
        copy = False
        break
