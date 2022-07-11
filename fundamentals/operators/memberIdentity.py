# Operadores de membro
myList = [3, 5, 'Lucas', 7, 'Fernando']

print('Lucas' in myList)  # True
print('Fernando' not in myList)  # False

x = 3
y = x
z = 3

print(x is y)  # True
print(y is z)  # True
print(x is not z)  # False

# Operadores de identidade

# list_a e list_b apontam para uma lista no mesmo espaço na memória
list_a = [1, 2, 3]
list_b = list_a

# Mesmo tendo o mesmo conteúdo que list_a e list_b, ela aponta para outra lista, em outro espaço na memória
list_c = [1, 2, 3]

print(list_a is list_b)  # True
print(list_b is list_c)  # False
