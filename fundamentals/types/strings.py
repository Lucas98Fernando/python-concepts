# Strings são imutáveis, você pode alterar o valor que está contido em uma variável, mas não exatamente a string

name = 'Lucas Fernando'
# A linha abaixo irá gerar um erro, não é possível reatribuir o conteúdo da string
# name[0] = 'M'

# Duas formas de colocar aspas em uma string
print("Luiz D'Avila" == 'Luiz D\'Avila')  # True

multiLines1 = """Texto com mais
de uma linha
"""

multiLines2 = """Texto com mais\n\tde uma linha
"""

multiLines3 = '''Texto com mais de
uma linha com aspas simples
'''

print(multiLines1)
print(multiLines2)
print(multiLines3)

# Acessando partes da string através de um range
print(name[6:])
print(name[-8:])
print(name[:6])
print(name[1:6])
print(name[6:8])

numbers = '123456789'

# Acessa do toda a string
print(numbers[::])

# Acessando o conteúdo da string com um passo de 2
print(numbers[::2])

# Acessando a partir de um indíce inicial
print(numbers[1::2])

# Invertendo o conteúdo da string
print(numbers[::-1])


# Operador de membro em strings

msg = 'Python é uma linguagem muito legal!'

# Vai retornar False porque letras maiúsculas e minúsculas são consideradas
print('py' in msg)

print('gua' in msg)  # True
print('py' not in msg)  # True
print(len(msg))  # 35

# Convertendo o conteúdo da string para minúsculas
print(msg.lower())

# Convertendo o conteúdo da string para maiúsculas
print(msg.upper())

# Dividindo a string
print(msg.split())


# Magic Methods

a = 'contando...'
b = '123'

# Podemos concatenar as duas strings dessa forma
print(a + b)
# Ou podemos concatenar dessa forma tbm :)
print(a.__add__(b))
print(str.__add__(a, b))

# Tamanho da string
print(a.__len__())

# Verificar se uma string contém alguma outra
print(a.__contains__('cont'))
# É a mesma coisa do exemplo acima
print('cont' in a)
