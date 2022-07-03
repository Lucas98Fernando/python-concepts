option = 0


def operation(type):
    numberOne = float(input("Informe o primeiro número: "))
    numberTwo = float(input("Informe o segundo número: "))

    return {
        'sum': numberOne + numberTwo,
        'subtraction': numberOne - numberTwo,
        'multiplication': numberOne * numberTwo,
        'division': numberOne / numberTwo
    }[type]


def setDefaultMessage(type):
    return f'\nA {type} entre os números foi: '


while option != 5:
    print("------------------")
    print("Calculadora")
    print("------------------")
    print("\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("\n")
    option = int(input("Informe uma opção: "))

    if option == 1:
        result = operation("sum")
        print(f'{setDefaultMessage("soma")} {result} \n')

    if option == 2:
        result = operation("subtraction")
        print(f'{setDefaultMessage("subtração")} {result} \n')

    if option == 3:
        result = operation("multiplication")
        print(f'{setDefaultMessage("multiplicação")} {result} \n')

    if option == 4:
        result = operation("division")
        print(f'{setDefaultMessage("divisão")} {result} \n')
