import pyautogui
import keyboard # pip install keyboard
import time

# Toggle key
toggle_key = 'f4'
clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    print(f"Autoclicker Active: {clicking}")

# Set up the hotkey to turn on/off
keyboard.add_hotkey(toggle_key, toggle_clicking)

print(f"Press {toggle_key} to start/stop. Press 'esc' to exit.")

while True:
    if clicking:
        pyautogui.click()
        # Reduce CPU usage, adjust for faster/slower clicking
        time.sleep(20) 
    
    if keyboard.is_pressed('esc'):
        break
