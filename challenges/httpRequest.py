import requests

print('-------')
print('Pokédex')
print('-------')
pokemonName = input('Informe o nome do Pokémon => ')

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName}')
data = response.json()

print(f"Nome: {data['species']['name']}")

print(f"Tipo{'s' if len(data['types']) > 1 else ''}: ")
for key in data['types']:
    print(key['type']['name'])
