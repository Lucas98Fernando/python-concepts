import requests

print('Pokédex\n')


def fetchPokemons():
    pokemonName = input('Informe o nome do Pokémon => ')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName}')
    data = response.json()

    if response.status_code == 200:
        print(data)
        print(f"\nNome: {data['species']['name']}")
        print(f"Tipo{'s' if len(data['types']) > 1 else ''}: ")
        for key in data['types']:
            print(key['type']['name'])
        searchAgain()
    else:
        print('Não foi possível buscar os dados do pokémon :(')


def searchAgain():
    searchAgain = input('\nPesquisar novo pokémon (s/n)? ')
    if searchAgain == 's':
        fetchPokemons()


fetchPokemons()
