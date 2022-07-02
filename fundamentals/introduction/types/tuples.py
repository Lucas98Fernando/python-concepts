"""
As Tuplas funcionam de forma semelhante as listas, contudo, possui uma característica muito importante que é a sua imutabilidade.
"""

users = ('Lucas', 'Fernando', 'Maria', 'Lucas', 'João', 'Pedro')

print(type(users))

# Case-sensitive
print('Lucas' in users)  # True
print('lucas' in users)  # False

print(users)
print(users[2])

# Exibindo os elementos da tupla dentro de um intervalo, baseado no index
print(users[1:3])
# É possível fazer um intervalo ignorando os últimos elementos utilizando o sinal de (-)
print(users[2:-1])
# Listando todos os elementos a partir de um index
print(users[2:])
print(users[:-2])

# Tupla com apenas um elemento
bestTeam = ('Liverpool',)
print(type(bestTeam))