# Power Paste
For pasting on websites that do not allow pasting.

### Specifications
1. Does not need any browser add on
2. This is a local script
3. You should start this script before attempting to paste

### Requirements
1. Python 3 (I used 3.11.7)
2. Modules from [requirements.txt](requirements.txt)


### Steps to get this running
1. Clone this repo
2. `pip install -r requirements.txt`
3. python main.py
4. Place curson on text field and press f8 (it will start typing what you have copied earlier)
5. If your text field does not have autocomplete for bracket open close, quotation mark open close, auto indent,
   you may turn them off at [main.py line 7](./main.py#L7) and [line 8](./main.py#L8) by setting them to `False`
6. If you want it to type faster, you could  set [line 8](./main.py#L8) to `False` but manually remove extra brackets
   after it finishes running
7. Press delete if you want to stop the program while it is not typing anything
8. Move the mouse to any corner (don't click anything) while it is typing to stop typing.
