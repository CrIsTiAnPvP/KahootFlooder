# -*- coding: utf-8 -*-

from rainbow import *
import os
from colorama import *
import time
from Flooder import Flooder

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')    

def main():
    banner = """
 /$$   /$$           /$$                             /$$     /$$$$$$$$ /$$                           /$$                    
| $$  /$$/          | $$                            | $$    | $$_____/| $$                          | $$                    
| $$ /$$/   /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  | $$      | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$$$$/   |____  $$| $$__  $$ /$$__  $$ /$$__  $$|_  $$_/  | $$$$$   | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$    /$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$  | $$    | $$__/   | $$| $$  \ $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
| $$\  $$  /$$__  $$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$      | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/| $$      | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/ \_______/|__/  |__/ \______/  \______/    \___/  |__/      |__/ \______/  \______/  \_______/ \_______/|__/   v 1.0   
                                                                                                                        

    """

    rainbow(banner)
    rainbow('                                       Coded By CrIsTiAn_PvP_YT\n')
    print(f'\n{Fore.LIGHTWHITE_EX}>> ', end='' )
    pin = None
    p = input(str(rainbow("Ingresa el PIN del Kahoot: ")).replace("None", ""))
    if len(p) > 6 or len(p) <= 0 or len(p) < 6:
        print(Fore.LIGHTRED_EX+ 'Error, el pin: '+ Fore.LIGHTCYAN_EX + p + Fore.LIGHTRED_EX+' es incorrecto, prueba de nuevo\n\n')
        print(f'\n{Fore.LIGHTWHITE_EX}>> ', end='' )
        b = input(str(rainbow("Ingresa el PIN del Kahoot: ")).replace("None", ""))
        if len(b) > 6 or len(b) <= 0 or len(b) < 6:
            print(Fore.LIGHTRED_EX+ 'Error, el pin: '+ Fore.LIGHTCYAN_EX + p + Fore.LIGHTRED_EX+' es incorrecto, saliendo de la herramienta\n\n')
            clear()
            exit()
        else:
            pin = int(b)
    else:
        pin = int(p)
    print(f'\n{Fore.LIGHTWHITE_EX}>> ', end='' )
    n = input(str(rainbow("Ingesa el Nombre De Los Bots: ")).replace('None', ''))
    Nombre = None
    if len(n) <= 0:
        print(f'\n{Fore.LIGHTWHITE_EX}>> ', end='' )
        b = input(str(rainbow("Ingresa el Nombre De los Bots: ")).replace("None", ""))
        if len(b) <= 0:
            print(Fore.LIGHTRED_EX+ 'Error, saliendo de la herramienta\n\n')
            clear()
            exit()
        else:
            Nombre = str(b)
    else:
        Nombre = str(n)

    print(f'{Fore.LIGHTCYAN_EX}>> {Fore.LIGHTGREEN_EX}Iniciando el Flooder...\n')
    time.sleep(1.25)
    clear()
    a = Flooder(Nombre, pin)
    a.flood()

clear()
main()
