import abc
import random
from problems import ArithmeticProblemGenerator
import time

class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


print('Mewtwo Gx, you need addition to win this battle!')

#pokemon_list = [Pokemon("Bulbasaur", 100), Pokemon("Charmander", 100), Pokemon("Squirtle", 100)]
pokemon_list = [Pokemon("Zekrom", 80)]

active_pokemon = random.choice(pokemon_list)

print("Your opponent sent out " + active_pokemon.name)

ps = ArithmeticProblemGenerator(1, 1000)

start_time = time.time()

while active_pokemon.hp > 0:

    p = ps.get_problem()
    print("Your opponent's " + active_pokemon.name + " has " + str(active_pokemon.hp) + " health left")
    print(p.display_problem())

    x = 'answer'
    while not x.isnumeric():
        x = input("Your answer: ")
    if p.check_answer(int(x)):
        print("Awesome, that's right!")
        print("Your opponent's " + active_pokemon.name + " takes 10 damage.")
        active_pokemon.hp -= 10
    else:
        print("Whoops... the right answer was: " + p.display_answer())
        print("Mewtwo, you take 10 damage.")
    print("")

print("Your opponent's " + active_pokemon.name + " fainted!")
print("You win!")
print("--- %s seconds ---" % (time.time() - start_time))