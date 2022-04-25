import pyautogui
import win32gui
import time
TIME_INTERVAL = 5
'''
pip install pywin32
pip install pyautogui
'''
if __name__ == '__main__':
    pyautogui.hotkey('ctrl','alt','w')
    exit(0)
    x = int(input('input the handle(get by spy++)\n'), 16)
    while True:
        # hwnd = win32gui.FindWindow(None,'腾讯会议')
        # print(win32gui.IsWindow(x))
        flag = win32gui.IsWindow(x)
        if flag == 0:
            print("abab")
            break
            
        time.sleep(TIME_INTERVAL)