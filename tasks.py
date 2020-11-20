import pyautogui
import time

def menu():
    print("What tasks would you like to do?")
    print("[0] Troubleshoot")
    print("[1] Submit Scan")
    print("[2] Download/Upload")
    print("[3] Accept Diverted Power/Stabilize Steering")
    print("[4] Empty Garbage")
    print("[5] Admin Swipe")
    print("[6] Fuel Engines")

    option = int(input("options: "))

    if option == 0:
        troubleshoot()
    if option == 1:
        start_task()
        menu()
    if option == 2:
        start_task()
        download_upload()
        menu()
    if option == 3:
        start_task()
        accept_diverted_stabilize()
        menu()
    if option == 4:
        start_task()
        empty_garbage()
        menu()
    if option == 5:
        start_task()
        admin_swipe()
        menu()
    if option == 6:
        start_task()
        fuel_engines()
        menu()


def troubleshoot():
    while True:
        print(pyautogui.position())

def start_task():
    pyautogui.moveTo(737, 549)
    pyautogui.click()
    time.sleep(0.5)

def download_upload():
    pyautogui.moveTo(414, 397)
    pyautogui.click()

def accept_diverted_stabilize():
    pyautogui.moveTo(401, 335)
    pyautogui.click()

def admin_swipe():
    pyautogui.moveTo(303, 483)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(157, 268)
    pyautogui.drag(600, 0, 0.8, button='left')

def empty_garbage():
    pyautogui.moveTo(576, 268)
    pyautogui.mouseDown()
    pyautogui.moveTo(576, 457)
    time.sleep(3)
    pyautogui.mouseUp()

def fuel_engines():
    pyautogui.moveTo(675, 515)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()
menu()
