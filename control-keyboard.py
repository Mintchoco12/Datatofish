# DataToFish: https://datatofish.com/control-keyboard-python/

import os
import pyautogui    # Importeer de volgende packages
import time

os.startfile(r'D:/example_file.txt') # Open een bestand die op een bepaalde locatie staat

time.sleep(3) # Wacht 3 seconden

pyautogui.write('Hello There', interval = 0.1) # Schrijf het volgende met een 0.1s tussentijd
pyautogui.press('enter') # Druk op enter
pyautogui.write('How is the Weather?', interval = 0.1) # Schrijf het volgende met een 0.1s tussentijd
pyautogui.hotkey('alt', 'f4') # Activeer de hotkey
pyautogui.press('enter') # Druk op enter