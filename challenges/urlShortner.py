import os
import requests
from dotenv import load_dotenv

load_dotenv()
cuttly_key = os.environ['CUTTLY_API_KEY']
cuttly_base_url = os.environ['CUTTLY_BASE_URL']

print('URL Shortner')


def status_error_message(status):
    errors = {
        '2': 'A URL informada é inválida',
        '3': 'O nome personalizado informado já está em uso'
    }

    if str(status) in errors:
        print(f'\n{errors[str(status)]}')
        return False
    else:
        return True


def ask_for_new_url():
    choise = input('\nDeseja encurtar outra URL? (s/n) ')
    if choise == 's':
        generate_url()
    else:
        print('\nAté a próxima!')


def generate_url():
    url_target = input('\nInforme a URL que você deseja encurtar: ')
    custom_name = input('Informe o nome personalizado para o link: ')

    url_api = f'{cuttly_base_url}?key={cuttly_key}&short={url_target}&name={custom_name}'

    response = requests.get(url_api)
    data = response.json()

    is_valid_status = status_error_message(data['url']['status'])

    if response.status_code == 200 and is_valid_status:
        print('\nURL gerada com sucesso!')
        print(f'URL => {data["url"]["shortLink"]}')

        ask_for_new_url()
    else:
        print('Não foi possível gerar a URL')


generate_url()
