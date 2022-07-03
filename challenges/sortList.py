numbers = [3, 4, 9, 10, 7, 8, 6]

sortBy = input('Ordernar dados por (asc ou desc)? ')
result = 'Resultado final:'

if sortBy == 'asc':
    numbers.sort()
    print(f'{result} {numbers}')
elif sortBy == 'desc':
    numbers.sort(reverse=True)
    print(f'{result} {numbers}')
else:
    print('Informe uma opção válida e tente novamente.')
