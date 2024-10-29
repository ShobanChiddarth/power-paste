"""\
- Can remove indent (optional)
- `dont_close_brackets` variable is used to determine to implement time intervals on closing brackets or not, close bracket characters are typed no matter what
- Has time intervals for every 4th character, space, or bracket close only if `dont_close_brackets` is True
"""
import sys
import time
import pyautogui
import pyperclip
from pynput import keyboard

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
        # added an else case to `dont_close_brackets`
        # now it will type the whole thing without any time intervals, in case `dont_close_brackets` is False
        else:
            pyautogui.typewrite(string)
            
        print("Successfully Power Pasted")
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
