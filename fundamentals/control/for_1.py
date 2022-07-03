print("De 0 até 9")
for i in range(10):
    print(i)

print("\n")

print("De 1 até 10")
for i in range(1, 11):
    print(i)

print("\n")

print("De 1 até 100 saltando 7 valores")
for i in range(1, 100, 7):
    print(i)

print("\n")

print("De 20 até 0 voltando 5 valores")
for i in range(20, 0, -5):
    print(i)

print("\n")

numbers = [1, 2, 3, 4]

print("Percorrendo uma lista e exibindo os valores na mesma linha")
for i in numbers:
    print(i, end=' ')

print("\n")

message = "Python é massa!"

print("Percorrendo uma string")
for letter in message:
    print(letter, end=' ')

print("\n")

print("Percorrendo um Set (conjunto)")
# Mesmo que o Set não seja indexado, é possível percorrer seus valores e as repetições serão ignoradas.
for set in {1, 2, 3, 4, 4, 4}:
    print(set, end=' ')

print("\n")

print("Percorrendo um dicionário")
product = {
    'name': 'Xbox One',
    'price': 1899,
    'discount': 0.2
}

print("Exemplo 1 - Pegando as chaves")
# Exibindo chave / valor
for key in product:
    print(key, '=>', product[key])

print("\n")

print("Exemplo 2 - Pegando chave / valor")
# Mesmo resultado, porém com uma implementação diferente do exemplo 1
for key, value in product.items():
    print(key, '=>', value)

print("\n")

print("Exemplo 3 - Pegando somente os valores")
for value in product.values():
    print(value, end=' ')

print("\n")

print("Exemplo 4 - Pegando somente as chaves")
for key in product.keys():
    print(key, end=' ')
