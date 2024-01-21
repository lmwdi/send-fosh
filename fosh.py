import pyautogui
import keyboard
import time

time.sleep(5)

txt = open('fosh.txt' ,encoding='utf-8')

for i in txt:
    keyboard.write(f'name {i}' )
    time.sleep(0.2)
    pyautogui.press('Enter')