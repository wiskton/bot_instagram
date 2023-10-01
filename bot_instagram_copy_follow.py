import mouse
import keyboard
import time
import csv
import os
import pyautogui
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
FOLLOW_TIME = os.getenv('FOLLOW_TIME')
PERFIL = 'https://instagram.com/wiskton'


def browser():
    # open edge
    os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    time.sleep(5)

    keyboard.write('https://instagram.com')
    keyboard.press("enter")

    time.sleep(5)


def login():
    try:
        img = pyautogui.locateCenterOnScreen("imgs/user.jpg", confidence=0.7)
        pyautogui.click(img.x, img.y)
        keyboard.write(USER)
        keyboard.press("enter")
    except:
        print("Não encontrou o campo de usuário.")

    try:
        img = pyautogui.locateCenterOnScreen("imgs/password.jpg", confidence=0.7)
        pyautogui.click(img.x, img.y)
        keyboard.write(PASSWORD)
        keyboard.press("enter")
    except:
        print("Não encontrou o campo de senha.")

    try:
        img = pyautogui.locateCenterOnScreen("imgs/login.jpg", confidence=0.7)
        pyautogui.click(img.x, img.y)
    except:
        print("Não encontrou o campo de login.")


def open_profile():
    img = pyautogui.locateCenterOnScreen("imgs/link.jpg", confidence=0.8)
    pyautogui.click(img.x, img.y)

    keyboard.write(PERFIL)
    keyboard.press("enter")

    time.sleep(5)

    img = pyautogui.locateCenterOnScreen("imgs/following.jpg", confidence=0.9)
    pyautogui.click(img.x, img.y)

    time.sleep(5)


def copy_followers():
    try:
        img = pyautogui.locateCenterOnScreen("imgs/follow.jpg", confidence=0.9)
        pyautogui.click(img.x, img.y)

        time.sleep(5)
    except:
        img = pyautogui.locateCenterOnScreen("imgs/seta.jpg", confidence=0.9)
        for x in range(0, 2):
            pyautogui.click(img.x, img.y)

        time.sleep(2)


if __name__ == "__main__":
    browser()
    login()
    open_profile()
    while True:
        copy_followers()