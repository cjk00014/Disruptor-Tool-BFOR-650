import subprocess

# Function to install the keyboard library
def keyboard_install():
    try:
        #The following line will import these three commands to install the keyboard import on a host copmuter
        subprocess.check_call(['pip', 'install', 'keyboard'])
    except Exception as e:
        print(f"Error installing keyboard library: {e}")

try:
    import keyboard
except ImportError:
    keyboard_install()
    import keyboard

import random

# This function creates the disallowed key as well as highlights and deletes the line when the disallowed key is pressed
def disallowed_key(event):
    disallowed_key = random.choice('pwdlsc./~') # Change what you would like within the parentheses to delete different characters
    if event.name == disallowed_key:
        keyboard.send('ctrl+a')
        keyboard.send('delete')
        return False
    # Allow all other key presses
    return True

# This command will track when the disallowed key is pressed and unpressed
keyboard.hook(disallowed_key)

# Cj Kurdi
# ckurdi@albany.edu