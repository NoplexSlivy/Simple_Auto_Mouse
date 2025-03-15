


def locate(time):
    import pyautogui as auto
    import keyboard as key
    import time as t
    run = True
    location = []
    print("Screen size:", auto.size())  # Print the screen size
    while run:
            if key.is_pressed('q'):
                pos = auto.position()
                print("Mouse position:", auto.position())  # Print the current mouse position
                location.append(pos)
                t.sleep(time)  # Pause
            if key.is_pressed('e'):
                run = False  # Stop the loop if 'e' is pressed
    return location
        