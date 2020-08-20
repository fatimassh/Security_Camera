import pyautogui

#location of lock screen button
def lock_screen():
    pyautogui.moveTo(x=27, y=10)
    pyautogui.click()
    pyautogui.moveTo(x=52, y=247)
    pyautogui.click()
