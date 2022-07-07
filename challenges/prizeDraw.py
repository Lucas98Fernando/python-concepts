import random
from cli.colors import cliColor

print('Sorteio \n')
qtdUsers = int(input('Quantas pessoas participarão do sorteio? \n'))
usersList = []

print('')


def addUsers():
    userAux = 0
    while(userAux < qtdUsers):
        currentUser = input(f'Nome do {userAux + 1}º usuário: ')
        usersList.append(currentUser)
        userAux += 1


addUsers()


def addMissingUsers():
    missingUserAux = 0
    qtdMissingUsers = int(
        input('\nQuantos novos participantes serão adicionados? \n'))

    print('')

    while(missingUserAux < qtdMissingUsers):
        currentUser = input(
            f'Nome do {missingUserAux + 1}º usuário faltando: ')
        usersList.append(currentUser)
        missingUserAux += 1

    showResult()


def showResult():
    print('')
    listAllParticipants()
    print('')

    choice = input('\nGerar resultado (s/n) ? ')

    if choice == 's':
        print(
            f'\nO vencedor foi: {cliColor(color="GREEN", text=generateWinner())}')
    else:
        print('Nenhum vencedor gerado')


def listAllParticipants():
    for user in usersList:
        print(f'{cliColor(color="YELLOW", text=user)}', end=' | ')


def generateWinner():
    return random.choice(usersList)


print(f'\nParticipantes do sorteio:\n')
listAllParticipants()

print('\n')
choice = input('Algum usuário ficou faltando (s/n) ? ')

if choice == 's':
    addMissingUsers()
elif choice == 'n':
    print(
        f'\nO vencedor foi: {cliColor(color="GREEN", text=generateWinner())}')
