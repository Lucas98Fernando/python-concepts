"""
List são utilizadas para armazenar múltiplos elementos em uma única variável.
"""

numbers = [0, 1, 2]
print(type(numbers))

# Adiciona novo elemento na lista
numbers.append(300)

# Quantidade de elementos da lista
print(len(numbers))

# Substituindo uma elemento através de seu index na lista
numbers[2] = 10

# Inserindo um elemento na lista e deslocando os outros
numbers.insert(0, -50)

print(numbers)
print(f'O último elemento da lista é: {numbers[-1]}')
