'''
In order to complete this project, you should have completed the Python lessons and project about Classes. 
You can find those lessons in the Learn Python 3 Course.
This includes the Classes lesson and the Inheritance lesson.
'''

'''
Create a Pokémon class. 
The __init__() method of our Pokémon class created variables to keep track of the 
Pokémon’s name, level, type (for example "Fire" or "Water"), maximum health, current health, and whether or not 
the Pokémon was knocked out. In our implementation, the maximum health was determined by the Pokémon’s level.

Hint:
Our instance variables were named 
self.name, self.level, self.health, self.max_health, self.type, and self.is_knocked_out.
'''

'''
Give your Pokémon class some functionality. 
Our Pokémon class had a variety of methods that changed the variables associated with a Pokémon. 
For example, it had a method the decreased the Pokémon’s health (we called this lose_health) and 
a method for regaining health. We also created a method that would officially “knock out” a Pokémon 
(when its health became 0) and another method to revive a knocked out Pokémon.

All of these methods had print statements to let the user know what was happening. 
For example, we might print something like "Charmander now has 30 health" when healing.

Hint:
The lose_health and gain_health methods each had an argument that determined how much health was lost or gained.
'''

'''
One of the trickier methods we created in the Pokémon class was the attack method. 
This method takes another Pokémon as an argument and deals damage to that Pokémon.

The amount of damage dealt depends on the types of the attacking Pokémon and the Pokémon being attacked. 
If the attacking Pokémon has advantage over the other Pokémon 
(for example, a "Fire" Pokémon attacking a "Grass" Pokémon), 
we dealt damage equal to twice the attacking Pokémon’s level. 
If the attacking Pokémon was at a disadvantage (for example, a "Grass" Pokémon attacking a "Fire" Pokémon), 
we dealt damage equal to half the attacking Pokémon’s level.

There are a huge number of types with advantages and disadvantages, but we only coded Fire, Water, and Grass.

Make sure to put in appropriate print statements to let the user know what is happening 
when one Pokémon attacks another.

Hint:
Our attack method had an argument named other_pokemon.

We compared the attacking Pokémon’s type (self.type) to the other Pokémon’s type (other_pokemon.type).

We then calculated how much damage should be dealt based on those types and stored it in a variable named damage.

We finally damaged the other Pokémon by calling other_pokemon.lose_health(damage)
'''

'''
Make a Trainer class. A Trainer can have up to 6 Pokémon, which we stored in a list. 
A trainer also has a name, and a number of potions they can use to heal their Pokémon. 
A trainer also has a “currently active Pokémon”, which we represented as a number.

Hint:
Our Trainer class had the instance variables self.pokemons, self.potions, self.current_pokemon, and self.name`.
'''

'''
Give your Trainer class some functionality through methods. 
Our trainer is able to use a potion and attack another trainer. 
When a potion is used, it heals the trainer’s currently active Pokémon. 
Similarly, when a trainer attacks another trainer, the currently active Pokémon deals damage to the other 
trainer’s current Pokémon. Finally, the trainer is able to switch which Pokémon is currently active.

Again, make sure to include print statements with all of these 
methods so the user can understand what is happening.

Hint:
The attack_other_trainer method had an argument named other_trainer. 
We would then find the other trainer’s active Pokemon by looking in their pokemons list like this:
their_pokemon=other_trainer.pokemons[other_trainer.current_pokemon]
'''

'''
Create some Pokémon and Trainers and test your methods. 
Can you create Pokémon that can attack each other and deal the correct amount of damage? 
Can you create trainers that have multiple Pokémon and can switch between them?

Hint:
This is one trainer that we made:
trainer_one = Trainer([a,b,c], 3, "Alex")

a, b, and c were each different Pokemon. We gave this trainer 3 potions and named them "Alex".
'''

'''
After experimenting with your Classes, go back to your methods and add some logic to deal with edge cases that you might not have thought about. 
Here are a couple of examples that you could try to implement:

A potion should not be able to heal a Pokémon past its maximum health.
A Pokémon that is knocked out should not be able to attack another Pokémon.
A trainer should not be able to switch their active Pokémon to one that is knocked out

As you continue to test your Classes, there may be other edge cases you encounter that you might want to fix.
'''

'''
Add more functionality that we haven’t implemented yet. Here is a list of ideas that you might want to try:
Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
Let your Pokémon evolve once they hit a certain level.
Have more stats associated with a Pokémon. 
In the real game, every Pokémon has stats like Speed, Attack, Defense. 
All of those stats effect the way Pokemon battle with each other. 
For example, the Pokémon with the larger Speed stat will go first in the battle.
'''