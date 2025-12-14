import sys
import pyautogui
import pyperclip
import time

# Small delay to switch focus safely
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1260, 1045)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(452, 153)
pyautogui.dragTo(950, 920, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get text from clipboard and store in variable
copied_text = pyperclip.paste()

# Print to verify
print("Copied Text:")
print(copied_text)
