import pyautogui
import keyboard


def press_type_enter(message):
    pyautogui.press('t')
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def handle_f1():
    press_type_enter('.d all')
    pyautogui.press('enter')

def handle_f2():
    press_type_enter('.w 15000')
    pyautogui.press('enter')

def handle_f3():
    press_type_enter('.load')
    pyautogui.press('enter')
    press_type_enter('.flex')
    pyautogui.press('enter')
    press_type_enter('.money')
    pyautogui.press('enter')

f4_press_count = 0
def handle_f4():
    global f4_press_count
    if f4_press_count % 2 == 0:
        pyautogui.press('t')
        pyautogui.typewrite('.afk')
        pyautogui.press('enter')
    else:
        pyautogui.press('t')
        pyautogui.typewrite('.afk off')
        pyautogui.press('enter')
    f4_press_count += 1

def handle_f5():
    press_type_enter('.drop')
    pyautogui.press('enter')

def handle_f6():
    press_type_enter('.rev')
    pyautogui.press('enter')

def handle_f7():
    press_type_enter('.load 2')
    pyautogui.press('enter')

def handle_f8():
    press_type_enter('.save 2')
    pyautogui.press('enter')

# Keybinding
# F1 .d all
# F2 Quick withdraw 15000cash
# F3 Quick stats 
# F4 Quick in and out afk 
# F5 VIP Drop gun
# F6 VIP revive 
# F7 Load save 2
# F8 Save 2
keyboard.on_press_key('F1', lambda _: handle_f1())
keyboard.on_press_key('F2', lambda _: handle_f2())
keyboard.on_press_key('F3', lambda _: handle_f3())
keyboard.on_press_key('F4', lambda _: handle_f4())
keyboard.on_press_key('F5', lambda _: handle_f5())
keyboard.on_press_key('F6', lambda _: handle_f6())
keyboard.on_press_key('F7', lambda _: handle_f7())
keyboard.on_press_key('F8', lambda _: handle_f8())


# Keep the script running
keyboard.wait('esc')

# !!!!!!!!!!!!!READ ME!!!!!!!!!!!!!!!!!!

#Python version: 3.11.4 
#pip install pyautogui
#pip install  keyboard
#Version 1.1 by Royaxz 



