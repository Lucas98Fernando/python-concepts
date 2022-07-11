a = 2
b = '3'

print(a + int(b))
print(str(a) + b)

# Observação importante: Para fazer a conversão de tipos sem erro, o valor precisa está no formato aderente a conversão que deseja realizar
# Isso irá gerar um erro, pois 5.2 não é um valor inteiro
# print(3 + int('5.2'))
print(3 + float('5.2'))
