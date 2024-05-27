import sys
import pyautogui
import pyperclip
from pynput import keyboard

def on_press_power_paste():
    remove_indent = True
    dont_close_brackets = False

    string  = pyperclip.paste()
    try:
        if remove_indent:
            string = '\n'.join(list(map(str.strip, string.split('\n'))))
        
        if dont_close_brackets:
            singe_string_count = 0
            double_string_count = 0
            brackets = {'normal':0, 'flower': 0, 'square': 0, 'angular': 0}
            for i in string:
                if i == "'":
                    singe_string_count += 1
                elif i == '"':
                    double_string_count += 1
                elif i == '(':
                    brackets['normal'] += 1
                elif i=='{':
                    brackets['flower'] += 1
                elif i=='[':
                    brackets['square'] += 1
                elif i=='<':
                    brackets['angular'] += 1

                if (i in ['"', "'"]):
                    if i in '"':
                        if double_string_count % 2 != 0:
                            pyautogui.typewrite(i)
                        else:
                            pyautogui.press('right')
                    elif i in "'":
                        if singe_string_count % 2 != 0:
                            pyautogui.typewrite(i)
                        else:
                            pyautogui.press('right')

                elif i in [')', '}', ']', '>']:
                    if brackets['normal'] > 0 and i == ')':
                        brackets['normal'] -= 1
                    elif brackets['flower'] > 0 and i == '}':
                        brackets['flower'] -= 1
                    elif brackets['square'] > 0 and i == ']':
                        brackets['square'] -= 1
                    elif brackets['angular'] > 0 and i == '>':
                        brackets['angular'] -= 1
                    else:
                        pyautogui.typewrite(i)
                    pyautogui.press('right')
                else:
                    pyautogui.typewrite(i)
        else:
            pyautogui.typewrite(string, interval=0.035)
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
