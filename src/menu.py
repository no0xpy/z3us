import fade 
from colorama import Fore
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
version = "1.0"
banner = r"""
 ______     ______     __  __     ______        ______   ______     ______     __        
/\___  \   /\  ___\   /\ \/\ \   /\  ___\      /\__  _\ /\  __ \   /\  __ \   /\ \       
\/_/  /__  \ \  __\   \ \ \_\ \  \ \___  \     \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
  /\_____\  \ \_____\  \ \_____\  \/\_____\       \ \_\  \ \_____\  \ \_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/   \/_____/        \/_/   \/_____/   \/_____/   \/_____/ 
"""

print(fade.water(banner))
print(Fore.YELLOW + f"[I] Vous utilisez la version {version}\n [I] Ce multitool fonctionne uniquement sur windows.")
print(fade.purpleblue(
    "\n 1 - IP Lookup"
    "\n 2 - Status Checker"
    "\n 3 - WHOIS Lookup"
    "\n 4 - Ports Scanner"
    "\n 5 - Identity Generator"
    "\n 6 - Phone Lookup"
    "\n 7 - Password Generator"
    "\n 8 - HTTP Requests Sender"
    "\n 9 - Discord Webhook Remover"
    "\n 10 - Multiple Searcher"
    "\n 11 - MiniFetch"
))

choix = input(Fore.RED + "[?] Que voulez-vous faire ? ")

if choix == "1":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/iplookup.py"')
elif choix == "2":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/statuts.py"')
elif choix == "3":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/whoiss.py"')
elif choix == "4":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/ports.py"')
elif choix == "5":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/id.py"')
elif choix == "6":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/phone.py"')
elif choix == "7":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/password.py"')
elif choix == "8":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/req.py"')
elif choix == "9":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/discordwebhookremove.py"')
elif choix == "10":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/multiplesearch.py"')
elif choix == "11":
    time.sleep(1)
    os.system('cls')
    os.system(f'python "{path}/tools/minifetch.py"')
else:
    print(Fore.RED + "[!] Choix invalide")
    time.sleep(2)
    os.system('cls')
    os.system(f'python "{path}/menu.py"')
