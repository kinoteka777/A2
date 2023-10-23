# File: main.py
# Description: the main file for UniSA OOP Assessment 2, Study period 5.
# Author: Casey Faggion
# StudentID: 110398039
# EmailID: fagck001
# This is my own work as defined by the University's Academic Misconduct Policy.

from abc import (ABC, abstractmethod)
from typing import Any 

class Alchemist:
    def __init__(self):
        self.__attack = 0
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__ranged = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes = {}

    def getLab(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe: str):
        pass

    def drinkPotion(self, potion: Potion):
        pass

    def collectReagent(self, reagent: Reagent, amount: int):
        pass

    def refineReagents(self):
        pass

class Laboratory:
    def __init__(self):
        self.__potions = [] #Potion[]
        self.__herbs = [] #Herb[]
        self.__catalysts = [] #Catalyst[]

    def mixPotion(self, name: str, type: str, stat: str, primaryIngredient: str, secondaryIngredient: str):
        pass        

    def addReagent(self, reagent: Reagent, amount: int):
        pass

class Potion(ABC):
    def __init__(self, name: str, stat: str, boost: float):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
    
    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat
    
    def getBoost(self):
        return self.__boost
    
    def setBoost(self, boost: float):
        self.__boost = boost

class Reagent(ABC):
    def __init__(self, name: str, potency: float):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name
    
    def getPotency(self):
        return self.__potency
    
    def setPotency(self, potency: float):
        self.__potency = potency

class SuperPotion(Potion):
    pass

class ExtremePotion(Potion):
    pass

class Herb(Reagent):
    def __init__(self, name: str, potency: float):
        super().__init__(name, potency)
        self.__grimy = True 

    def refine(self):
        self.__grimy = False
        self.__potency *= 2.5
        print(self.__name,'refined!\nGrimy =', self.__grimy,'\nPotency =', self.__potency)

    def getQuality(self):
        pass

class Catalyst(Reagent):
    def __init__(self, name: str, potency: float, quality: float):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(self.__name,'refined!\nQuality is now',self.__quality)
        elif self.__quality >= 8.9:
            self.__quality = 10
            print(self.__name,'refined!\nQuality is now',self.__quality,'\nIt cannot be refined any further!')