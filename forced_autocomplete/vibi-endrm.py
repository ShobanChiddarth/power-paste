"""\
Same as `vibi.py` but removes extra close bracket characters that were injected by the forced autocomplete
"""
import sys
import time
import ctypes
import pyautogui
import pyperclip
from pynput import keyboard

def num_lock_is_on():
    """Check the state of Num Lock | True if ON, False if OFF"""
    return ctypes.windll.user32.GetKeyState(144) != 0

def on_press_power_paste():
    remove_indent = True
    dont_close_brackets = True
    string  = pyperclip.paste()
    try:
        x=0
        if remove_indent:
            string = '\n'.join(list(map(str.strip, string.split('\n'))))
        if dont_close_brackets:
            for i in string:
                x+=1
                if x%4==0:
                    x=0
                    time.sleep(0.039)
                if i in [')', '}', ']']:
                    pyautogui.typewrite(i)
                    time.sleep(0.005)
                else:
                    if(i=='\n'):
                        pyautogui.typewrite(i)
                        time.sleep(0.005)
                    else:
                        pyautogui.typewrite(i)
            
        print("Successfully Power Pasted")
        # For some reason, pyautogui cannot select text if num lock is off
        if num_lock_is_on():
            pyautogui.press("numlock")
        pyautogui.hotkey("shiftleft", "pagedown")
        pyautogui.press("enter")
        
    except pyautogui.FailSafeException as e:
        print("Stopped Power Pasting |", e)

def on_press(key):
    try:
        print(f"alphanumeric key '{key.char}' pressed")
    except AttributeError:
        print(f"special key '{key}' pressed")
def on_release(key):
    print(f"'{key}' released")
    if key == keyboard.Key.delete:
        sys.exit()
    elif key == keyboard.Key.f8:
        on_press_power_paste()
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
