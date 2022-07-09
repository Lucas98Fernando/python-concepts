print('Contador de vogais\n')

word = input('Informe uma palavra: ')
vowels = ['a', 'e', 'i', 'o', 'u']
vowelsCount = 0

if word:
    for letter in word:
        if letter in vowels:
            vowelsCount += 1
    print(f'A quantidade de vogais na palavra {word} é {vowelsCount}')
else:
    print('Informe uma palavra')
