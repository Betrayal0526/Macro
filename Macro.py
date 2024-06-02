import pyautogui
import time
import pyperclip
import keyboard
import sys

def safe_sleep(total_sleep_time, check_interval=0.1):
    end_time = time.time() + total_sleep_time
    while time.time() < end_time:
        if keyboard.is_pressed('f10'):
            sys.exit()
        time.sleep(check_interval)

while True:
    if keyboard.is_pressed('f10'):
        sys.exit()
    elif keyboard.is_pressed('f9'):
        pyautogui.moveTo(949, 1061, 0.3)
        pyautogui.click()
        pyautogui.moveTo(538, 977, 0.5)
        pyautogui.click()

        for i in range(10):
            pyperclip.copy("Enter the text")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(['enter'])
            safe_sleep(60)
