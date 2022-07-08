import pyautogui
import webbrowser
import time

message = input("message leave blank to use clipboard: ")
duration = input("duration: ")
repeats = input("repeats: ")

isLoaded = input("Press enter when you want me to start spamming")

time.sleep(1)

for i in range (int(repeats)):
    if message !="":
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(int(duration))
    
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(int(duration))

if message !="":
    print(f'Spammed {message} {duration} times in {repeats} seconds\n')

else:
    print(f'Spammed Ctrl + V {duration} times in {repeats} reconds\n')