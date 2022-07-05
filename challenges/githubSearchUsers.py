import requests
from colorama import Fore, Style

print(f'{Fore.LIGHTBLUE_EX}GitHub Users Find{Style.RESET_ALL}\n')


def fetchUser():
    username = input('Informe o nome do usuário => ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f'\nNome completo: {Fore.YELLOW}{data["name"]}{Style.RESET_ALL}')
        print(f'Bio: {Fore.YELLOW}{data["bio"]}{Style.RESET_ALL}')
        print(f'Empresa: {Fore.YELLOW}{data["company"]}{Style.RESET_ALL}')
        print(f'Localização: {Fore.YELLOW}{data["location"]}{Style.RESET_ALL}')
        print(f'Seguidores: {Fore.YELLOW}{data["followers"]}{Style.RESET_ALL}')
        print(f'Seguindo: {Fore.YELLOW}{data["following"]}{Style.RESET_ALL}')
        print(
            f'Repositórios públicos: {Fore.YELLOW}{data["public_repos"]}{Style.RESET_ALL}')

        searchAgain()
    else:
        print('Não foi possível encontrar os dados do usuário')


def searchAgain():
    searchAgain = input('\nPesquisar novo usuário (s/n)? ')
    if searchAgain == 's':
        fetchUser()


fetchUser()
