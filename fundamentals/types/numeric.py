from decimal import Decimal, getcontext

print(dir(int))
print(dir(float))

a = 3
b = 5.0

# O valor 5.0 é um inteiro, mas é do tipo float
print(b.is_integer())

# É o mesmo que 2 + 8
print(int.__add__(2, 8))

# Mesmo resultado, porém com implementações diferentes
print((-2).__abs__())  # Função mapeada diretamente no valor
print(abs(-2))  # Função de dentro do builtins

# O pacote Decimal serve para remover as imprecisões que podem ocorrer devido a especificação que a linguagem utiliza para implementar algumas operações numéricas, pois geralmente a linguagem prioriza performance.
print(Decimal(2) / Decimal(7))

# Nível de precisão do valor gerado
getcontext().prec = 4

print(Decimal(2) / Decimal(7))

# Maior valor
print(Decimal.max(Decimal(2), Decimal(7)))
