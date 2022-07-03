# Exemplo com uma quantidade de repetições indeterminada
note = 0
qtd = 0
total = 0

while note != -1:
    note = float(input("Informe uma nota ou -1 para sair: "))
    if note != -1:
        qtd += 1
        total += note

print(f'A média da turma é: {total / qtd}')

# Exemplo com uma quantidade pré-determinada, nesse caso, é melhor utilizar o for
# x = 10

# while x:
#     print(x)
#     x -= 1

# print("Fim")
