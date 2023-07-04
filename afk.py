import time
import pyautogui
import keyboard

def press_type_enter(message):
    pyautogui.press('t')
    pyautogui.typewrite(message)
    pyautogui.press('enter')

# Set the interval for AFK mode in seconds (15 minutes = 900 seconds)
afk_interval = 900

# Function to check if F2 key is pressed
def check_start_key():
    return keyboard.is_pressed('F2')

# Variable to track if F2 has been pressed
f2_pressed = False

while True:
    # Wait for F2 key to be pressed
    while not check_start_key():
        time.sleep(0.1)

    if not f2_pressed:
        f2_pressed = True
        while True:
            press_type_enter('.afk')
            pyautogui.press('enter')

            # Wait for the AFK interval
            time.sleep(afk_interval)

            press_type_enter('.afk off')
            pyautogui.press('enter')
