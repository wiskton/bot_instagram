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


# utilize a extensão - IG Tools - IG Follower Export Tool
# export todos seguidores

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
FOLLOW_TIME = os.getenv('FOLLOW_TIME')


def browser():
    # open edge
    os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    time.sleep(5)

    '''
    img = pyautogui.locateCenterOnScreen("imgs/link.jpg", confidence=0.7)
    if not img:
        pyautogui.click(img.x, img.y)
    '''
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

def follow():
    with open("profiles.csv", newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # clica na barra de endereço do navegador
            try:
                img = pyautogui.locateCenterOnScreen("imgs/link.jpg", confidence=0.8)
                pyautogui.click(img.x, img.y)

                # acessar o novo profile
                keyboard.write(row["profileUrl"])
                keyboard.press("enter")

                time.sleep(5)
            except:
                print("Não encontrou a barra de endereço do navegador.")

            # clica para seguir a pessoa
            try:
                img = pyautogui.locateCenterOnScreen("imgs/follow.jpg", confidence=0.9)
                pyautogui.click(img.x, img.y)

                time.sleep(FOLLOW_TIME)
            except:
                print("Você já segue a pessoa.")


if __name__ == "__main__":
    browser()
    login()
    follow()