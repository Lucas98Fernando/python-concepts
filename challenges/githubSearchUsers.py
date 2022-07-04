import requests


def fetchUser():
    print('GitHub Users Find\n')
    username = input('Informe o nome do usuário => ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f'\nNome completo: {data["name"]}')
        print(f'Bio: {data["bio"]}')
        print(f'Empresa: {data["company"]}')
        print(f'Localização: {data["location"]}')
        print(f'Seguidores: {data["followers"]}')
        print(f'Seguindo: {data["following"]}')
        print(f'Repositórios públicos: {data["public_repos"]}')

        searchAgain()
    else:
        print('Não foi possível encontrar os dados do usuário')


def searchAgain():
    searchAgain = input('\nPesquisar novo usuário (s/n)? ')
    if searchAgain == 's':
        fetchUser()


fetchUser()
