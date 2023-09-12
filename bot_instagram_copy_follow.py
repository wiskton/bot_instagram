import mouse
import keyboard
import time
import csv
import os


# utilize a extensão - IG Tools - IG Follower Export Tool
# export todos seguidores 

# quanto tempo espera para seguir o próximo
FOLLOW_TIME = 30
REMOVE_PROFILES = []
NEW_DICT = []

# open edge
os.startfile("msedge")
time.sleep(2)


with open('profiles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # clica na barra de endereço do navegador
        mouse.move(600, 50, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)

        # acessar o novo profile
        keyboard.write(row['profileUrl'])
        keyboard.press("enter")

        # aguarde 5 segundos
        time.sleep(5)

        # clica para seguir a pessoa
        mouse.move(1120, 130, absolute=True, duration=0.1)
        mouse.click('left')

        # # gera um novo dicionário sem as pessoas que acabou de seguir
        # REMOVE_PROFILES.append(row['profileUrl'])
        # for row2 in reader:
        #     if row2['profileUrl'] not in REMOVE_PROFILES:
        #         NEW_DICT.append({
        #             'id': "",
        #             'userName': "",
        #             'fullName': "",
        #             'profileUrl': row2['profileUrl'],
        #             'avatarUrl': "",
        #             'isVerified': "",
        #         })
            
        # # cria um novo csv sem as pessoas que já seguiu
        # with open('profiles2.csv', 'w', newline='') as csvfile:
        #     fieldnames = ['id', 'userName', 'fullName', 'profileUrl', 'avatarUrl', 'isVerified']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writerows(NEW_DICT) 

        time.sleep(FOLLOW_TIME)