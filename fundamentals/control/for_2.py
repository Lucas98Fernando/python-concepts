people = ['Lucas', 'Maria']
quality = ['Legal', 'Inteligente']

for p in people:
    for q in quality:
        print(f'{p} é {q}')

# Exemplo de laço vazio utilizando a palavra reservada: pass
for i in [1, 2, 3]:
    pass

# Imprime somente valores par, o continue serve para seguir o fluxo
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

print('\n')

# Com o break é possível interromper o laço/bloco de execução
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('Fim!')
