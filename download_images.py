from urllib import request
import time
import json

pokemon_dict = {}
for i in range (1,807):
    print(i)
    req = request.Request("https://pokeapi.co/api/v2/pokemon/"+str(i), headers={'User-Agent': 'Mozilla/5.0'})
    pokemon = request.urlopen(req)
    pokemon = json.loads(pokemon.read())
    print(pokemon["name"])
    back_url = pokemon["sprites"]["back_default"]
    front_url = pokemon["sprites"]["front_default"]
    request.urlretrieve(back_url, "images/"+str(i)+"_back.png")
    request.urlretrieve(front_url, "images/" + str(i) + "_front.png")
    pokemon_dict[pokemon["name"]] = i
    time.sleep((60*3)/100)

print(pokemon_dict)