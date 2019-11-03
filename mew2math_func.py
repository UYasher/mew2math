import abc
import random


class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


print('Mewtwo Gx, you need addition to win this battle!')

#pokemon_list = [Pokemon("Bulbasaur", 100), Pokemon("Charmander", 100), Pokemon("Squirtle", 100)]
pokemon_list = [Pokemon("Zekrom", 300)]

active_pokemon = random.choice(pokemon_list)

print("Your opponent sent out " + active_pokemon.name)

while active_pokemon.hp > 0:

    print("Your opponent's " + active_pokemon.name + " has " + str(active_pokemon.hp) + " health left")

    x1 = random.randint(1, 1000)
    #x2 = random.randint(1, 100)
    x2 = random.randint(1, 1000)

    # eventually this will be a dict to a tuple of (symbol, (f: x, y -> x, y, solution))
    op_char = random.choice(['+','-'])
    operation = {
        '+': lambda x,y: [x, y, x+y],
        '-': lambda x,y: [max(x,y), min(x,y), max(x,y)-min(x,y)]
    }

    x1, x2, result = operation[op_char](x1, x2)

    print(str(x1) + op_char + str(x2) + " = ?")

    x3 = 'placeholder'

    while not x3.isnumeric():
        x3 = input("Your answer: ")
    if int(x3) == result:
        print("Awesome, that's right!")
        print("Your opponent's " + active_pokemon.name + " takes 10 damage.")
        active_pokemon.hp -= 10
    else:
        print("Whoops... the right answer was: " + str(result))
        print("Mewtwo, you take 10 damage.")
    print("")

print("Your opponent's " + active_pokemon.name + " fainted!")
print("You win!")