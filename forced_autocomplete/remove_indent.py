import sys
import pyautogui
import pyperclip
from pynput import keyboard

def on_press_power_paste():
    remove_indent = True
    string  = pyperclip.paste()
    if remove_indent:
        string = '\n'.join(list(map(str.strip, string.split('\n'))))
    
    try:
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

