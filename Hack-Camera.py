#!/use/bin/python3.11.5
# Copyright (C) 2016 The Android Open Source Project
# Chanel Telegram: https://t.me/Cyber_Seven
# ID Telegram: https://t.me/name_MR_DARK
# MR - DARK

from os import system
from time import sleep
system("pip install sys")
system("pip install platform")
system("pip install pygame")
system("pip install colorama")

from platform import uname
from colorama import Fore
import sys
import pygame.camera
import pygame.image

if uname()[0] == "Windows":
  system("cls")
else:
  system("clear")

sleep(2)
print("")

pygame.camera.init()
camera = pygame.camera.Camera(pygame.list_cameras()[0])
camera.start()

img = camera.get_image()
img_name = input(Fore.LIGHTGREEN_EX+"Enter a name for your image: ")

pygame.image.save(img, img_name)
print("")
print(Fore.LIGHTGREEN_EX+"Loading.....%10")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%15")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%25")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%40")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%50")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%75")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%86")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%95")
sleep(1)
print(Fore.LIGHTGREEN_EX+"Loading.....%99")
sleep(1)
print("")
sleep(3)
log = Fore.LIGHTGREEN_EX+"Phine saved.... [loading......%100]"

print(log)
pygame.camera.quit()
