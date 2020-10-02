import time
#import numpy as np
import sys

#delay printing
def delay_print(s):
    #prints one letter at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    is_knocked_out = False
    def __init__(self, name, level, typing):
        #creates a Pokemon obj; aka makes a pokemon w/ its own stats
        self.name = name
        self.level = level
        self.max_health = level*3
        self.health = self.max_health
        self.typing = typing
        self.speed = 5*level+3

    def lose_health(self, dmg):
        self.health-=dmg
        if self.health <= 0:
            self.health = 0
            self.is_knocked_out = True
            self.fainted()
        else:    
            delay_print ('{} has {} health remaining.\n'.format(self.name, self.health))
            time.sleep(1)

    def fainted(self):
        if self.is_knocked_out:
            delay_print ('{} fainted!\n'.format(self.name))
            time.sleep(1)
        else:
            delay_print('{} is still standing.\n'.format(self.name))
            time.sleep(1)
        
    def gain_health(self, heal):
        
        if(self.health!=0):
            if self.health + heal < self.max_health:
                self.health+=heal
                #delay_print('You healed {}.\n'.format(self.name))
                time.sleep(1)
                delay_print ('{} now has {} health.\n'.format(self.name, self.health))
                time.sleep(1)
            elif self.health + heal >= self.max_health:
                self.health = self.max_health
                delay_print ('{} is fully restored!\n'.format(self.name, self.health))
                time.sleep(1)
        else:
            delay_print ('Use a revive!\n')
   
    def revive(self):
        if self.is_knocked_out:#if pokemon is already knocked out
            self.is_knocked_out = False#revive pokemon and give it half health
            self.health+=(self.max_health/2)
            delay_print ('You revived {}!\n'.format(self.name))
        else:
            #self.is_knocked_out = False
            delay_print ('{} is still standing.\n'.format(self.name))

    def attack(self, opponent):
        #delay_print("{} attacks {}!".format(self.name, self.opponent))
        if(opponent.typing == 'Water'):#attacking opponenet
            if(self.typing == 'Water' or self.typing == 'Fire'):
                delay_print("It's not very effective...\n")
                time.sleep(1)
                damage = 0.5*self.level 
                opponent.lose_health(damage)
            else:
                delay_print("It's super effective!\n")
                time.sleep(1)
                damage = 2*self.level
                opponent.lose_health(damage)
                
        elif(opponent.typing == 'Fire'):
            if(self.typing == 'Fire' or self.typing == 'Grass'):
                delay_print("It's not very effective...\n")
                time.sleep(1)
                damage = 0.5*self.level
                opponent.lose_health(damage)

            else:
                delay_print("It's super effective!\n")
                time.sleep(1)
                damage = 2*self.level
                opponent.lose_health(damage)

        elif(opponent.typing == 'Grass'):
            if(self.typing == 'Grass' or self.typing == 'Water'):
                delay_print("It's not very effective...\n")
                time.sleep(1)
                damage = 0.5*self.level
                opponent.lose_health(damage)

            else:
                delay_print("It's super effective!\n")
                time.sleep(1)
                damage = 0.5*self.level
                opponent.lose_health(damage)


class Trainer:
    def __init__(self, name, pokemons, potions, active):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.active = active

    def call_out(self):#call out Pokemon in the lead
        delay_print('Go {}!\n'.format(self.active.name))

    def switch(self):
        pass

    def use_potion(self, pick):
        #Potion heals 20 HP
        #Super Potion heals 50 HP
        #Hyper Potion heals 100 HP
        
        if pick == str(1):
            delay_print("\n{} used a potion!\n".format(self.name))
            time.sleep(1)
            self.active.gain_health(20)
        elif pick == str(2):
            delay_print("\n{} uses a super potion!\n".format(self.name))
            time.sleep(1)
            self.active.gain_health(50)
        elif pick == str(3):
            delay_print("\n{} uses a hyper potion!\n".format(self.name))
            time.sleep(1)
            self.active.gain_health(100)


pokemon_one = Pokemon("Inteleon", 39, "Water")
pokemon_two = Pokemon("Cinderace", 41, "Fire")
pokemon_three = Pokemon("Rillaboom", 34, "Grass")
pokemon_four = Pokemon("Charizard", 45, "Fire")
pokemon_five = Pokemon("Venusaur", 36, "Grass")
pokemon_six = Pokemon("Blastoise", 34, "Water")

roster_one = [pokemon_one, pokemon_two, pokemon_three]
roster_two = [pokemon_four, pokemon_five, pokemon_six]

trainer_one = Trainer("Patrick", roster_one, 5, roster_one[0])
trainer_two = Trainer("Red", roster_two, 3, roster_two[0])

delay_print("You're challenged by Pokemon Trainer {}.\n".format(trainer_two.name))
time.sleep(1)
delay_print("Pokemon Trainer {} sends out {}.\n".format(trainer_two.name, trainer_two.active.name))
time.sleep(1)
trainer_one.call_out()
time.sleep(1)

while (trainer_one.active.health > 0 and trainer_two.active.health>0):
    delay_print("\n{}, what will you do?\n".format(trainer_one.name))
    print("Fight! (1)\nHeal (2)")
    num1 = input()

    if num1 == str(2):
        delay_print("Potion (1), Super Potion (2), or Hyper Potion (3)")
        choose1 = input("\n")

    delay_print("\n{}, what will you do?\n".format(trainer_two.name))
    print("Fight! (1)\nHeal (2)")
    num2 = input()

    if num2 == str(2):
        delay_print("Potion (1), Super Potion (2), or Hyper Potion (3)")
        choose2 = input("\n")

    if(trainer_one.active.speed>trainer_two.active.speed):
        if num1 == str(2):
            trainer_one.use_potion(choose1)
        
        if num2 == str(2):
            trainer_two.use_potion(choose2)
        
    elif(trainer_one.active.speed<trainer_two.active.speed):
        if num2 == str(2):
            trainer_two.use_potion(choose2)

        if num1 == str(2):
            trainer_one.use_potion(choose1)

    if(trainer_one.active.speed>trainer_two.active.speed):
        if num1 == str(1):
            delay_print("\n{} attacks {}!\n".format(trainer_one.active.name, trainer_two.active.name))
            time.sleep(1)
            trainer_one.active.attack(trainer_two.active)

            if(trainer_two.active.health == 0):
                delay_print("You defeated Pokemon Trainer {}!\n".format(trainer_two.name))
                time.sleep(1)
                break
        
        if num2 == str(1):
            delay_print("\n{} attacks {}!\n".format(trainer_two.active.name, trainer_one.active.name))
            time.sleep(1)
            trainer_two.active.attack(trainer_one.active)
            if(trainer_one.active.health == 0):
                delay_print("{} defeated you.\n".format(trainer_one.name))
                time.sleep(1)
                break

    elif(trainer_one.active.speed<trainer_two.active.speed):
        if num2 == str(1):
            delay_print("\n{} attacks {}!\n".format(trainer_two.active.name, trainer_one.active.name))
            time.sleep(1)
            trainer_two.active.attack(trainer_one.active)

            if(trainer_one.active.health == 0):
                delay_print("\n{} defeated you.\n".format(trainer_one.name))
                time.sleep(1)
                break

        if num1 == str(1):
            delay_print("\n{} attacks {}!\n".format(trainer_one.active.name, trainer_two.active.name))
            time.sleep(1)
            trainer_one.active.attack(trainer_two.active)

            if(trainer_two.active.health == 0):
                delay_print("\nYou defeated Pokemon Trainer {}!\n".format(trainer_two.name))
                time.sleep(1)
                break
