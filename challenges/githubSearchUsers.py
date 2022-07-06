import requests
from colorama import Fore, Style
from cli.colors import cliColor

print(f'{cliColor(color="LIGHTBLUE_EX", text="GitHub Users Find")}\n')


def fetchUser():
    username = input('Informe o nome do usuário => ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(
            f'\nNome completo: {cliColor(color="YELLOW", text=data["name"])}')
        print(f'Bio: {cliColor(color="YELLOW", text=data["bio"])}')
        print(f'Empresa: {cliColor(color="YELLOW", text=data["company"])}')
        print(
            f'Localização: {cliColor(color="YELLOW", text=data["location"])}')
        print(
            f'Seguidores: {cliColor(color="YELLOW", text=data["followers"])}')
        print(
            f'Seguindo: {cliColor(color="YELLOW", text=data["following"])}')
        print(
            f'Repositórios públicos: {cliColor(color="YELLOW", text=data["public_repos"])}')

        searchAgain()
    else:
        print('Não foi possível encontrar os dados do usuário')


def searchAgain():
    searchAgain = input('\nPesquisar novo usuário (s/n)? ')
    if searchAgain == 's':
        fetchUser()
    else:
        print(f'{cliColor(color="LIGHTBLUE_EX", text="Até a próxima!")}')


fetchUser()
