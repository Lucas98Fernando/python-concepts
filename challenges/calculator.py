option = 0


def operation(type):
    numberOne = float(input("Informe o primeiro número: "))
    numberTwo = float(input("Informe o segundo número: "))

    return {
        'sum': numberOne + numberTwo,
        'subtraction': numberOne - numberTwo,
        'multiplication': numberOne * numberTwo
    }[type]


def setDefaultMessage(type):
    return f'A {type} entre os números foi: '


while option != 4:
    print("------------------")
    print("Calculadora")
    print("------------------")
    print("\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Sair")
    print("\n")
    option = int(input("Informe uma opção: "))

    if option == 1:
        result = operation("sum")
        print("\n")
        print(f'{setDefaultMessage("soma")} {result}')
        print("\n")

    if option == 2:
        result = operation("subtraction")
        print("\n")
        print(f'{setDefaultMessage("subtração")} {result}')
        print("\n")

    if option == 3:
        result = operation("multiplication")
        print("\n")
        print(f'{setDefaultMessage("multiplicação")} {result}')
        print("\n")

    if (option == 4):
        print("Até mais!")
        break
