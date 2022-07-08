import random

chars = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyz123456789!@#$%&*'

print('Gerador de senhas\n')

passwords_amount = int(input('Quantas senhas você deseja gerar? '))
passwords_length = int(input('Qual será o tamanho das senhas? '))

print('\nSenhas geradas: \n')

def generatePasswords():
    for amount in range(passwords_amount):
        passwords = ''
        for length in range(passwords_length):
            passwords += random.choice(chars)
        print(passwords)


generatePasswords()
