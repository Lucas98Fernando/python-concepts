numberOne = 10
numberTwo = 2

print(numberOne + numberTwo)
print(numberOne - numberTwo)
print(numberOne * numberTwo)
print(numberOne / numberTwo)
print(numberOne % numberTwo)

value = input('Informe um número: ')
message = f'O número {value} é'

isEvenNumber = float(value) % 2 == 0
isOddNumber = float(value) % 2 == 1

if isEvenNumber:
    print(f'{message} par')
elif isOddNumber:
    print(f'{message} ímpar')
