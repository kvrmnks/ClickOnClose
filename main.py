import pyautogui
import win32gui
import time
TIME_INTERVAL = 5 # s
'''
pip install pywin32
pip install pyautogui
'''
hot_key = ['ctrl', 'alt', 'w']
if __name__ == '__main__':

    x = int(input('input the handle(get by spy++)\n'), 16)
    while True:
        # hwnd = win32gui.FindWindow(None,'腾讯会议')
        # print(win32gui.IsWindow(x))
        flag = win32gui.IsWindow(x)
        if flag == 0:
            for x in hot_key:
                pyautogui.keyDown(x)
            for x in hot_key:
                pyautogui.keyUp(x)
            break
            
        time.sleep(TIME_INTERVAL)