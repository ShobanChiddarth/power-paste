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
3. `python main.py`
4. Place curson on text field and press f8 (it will start typing what you have copied earlier)
7. Press delete if you want to stop the program while it is not typing anything
8. Move the mouse to any corner (don't click anything) while it is typing to stop typing.
9. Do not click on anything while the program is typing

### About websites that have forced code autocomplete
Check the folder [forced_autocomplete](./forced_autocomplete/). There are different files for different types of forced autocomplete.