#this is the ho man tin sumulation code
import time 
import random
import math
import os 

class labubu:
    def __init__(self, name, efficiency, age, gender):
        self.name = name
        self.efficiency = efficiency
        self.age = age
    
    def kill(self):
        print(f'{self.name} has been killed!')
        del self

    def boost(self):
        self.efficiency += 20
        print(f'{self.name} efficiency increased to {self.efficiency}!')
        self.age -= 1

    def combine(self, second_labubu):
        self.efficiency = (self.efficiency + second_labubu.efficiency) * 1.5
        self.age = (self.age + second_labubu.age) / 2 
        print(f'{self.name} and {second_labubu.name} have combined!')
        del second_labubu
    
    def givehead(self, second_labubu):
        if self.gender == second_labubu.gender:
            print("They are not suitable for giving head to each other!")
            print("Unlock gender change tool to perform this act!")
        else:
            if self.gender == "M":
                self.efficiency += 50 
            else:
                second_labubu.efficiency += 50
            print(f'{self.name} and {second_labubu} have given head!')

    def sextransfer(self):
        self.gender = "M" if self.gender == "F" else self.gender = "F"     

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bold(text):
    return f"\033[1m{text}\033[0m"

def rules():
    clear()
    print('''
This is the rules of the Ho Man Tin Simulator game.
In this game, you will cosplay as Ho Man Tin, our beloved teacher.
Your goal in this game, is to farm labubus as much as possible.
The labubus can generate a currency called:
        '''
        )
    print(bold("load"))
    print('''
You will have tools to help you gain load, but you have to buy them!
Good luck!
        '''
        )

def exitgame():
    home()

def home():
    clear()
    print