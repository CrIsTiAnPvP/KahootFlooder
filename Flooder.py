from kahoot import client
import os
import random
from colorama import Fore
from rainbow import *

class Flooder:
    def __init__(self, name, pin):
        self.pin = int(pin)
        self.name = str(f'{name} ')
        self.bot =  client()
        self.bots = self.name

    def flood(self):
        def unido(nombre):
            colores = [Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX]
            elegido = random.choice(colores)
            print(Fore.LIGHTWHITE_EX+'>> '+elegido+nombre, end='')
            print(str(rainbow(' Se está conectando')).replace('None', ''))
        while True:
            self.bots = self.name + str(random.randint(0, 666))
            self.bot.join(self.pin, self.bots)
            self.bot.on('joined', unido(self.bots))