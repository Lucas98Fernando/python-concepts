num1 = 10
num2 = 2

print(num1 + num2)

name = "Lucas"
age = 23

print('Meu nome é: ' + name)
# Converter valores númericos para string dessa forma não é legal
# print('Eu tenho ' + str(age) + 'anos de idade')

# Uma alternativa legal é utilizar a sintaxe => f'{}', tudo que estiver dentro das aspas será interpretado como código Python, é semelhante ao Template Literals do JS
print(f'Eu tenho {age} anos de idade')

gretting = "Olá usuário "
print(2 * gretting)

# Detalhe importante: Em Python não existe constantes, mas existe uma convenção, toda variável com letras maiúsculas são para mostrar que esse valor não deve ter reatribuições, mas não garate que isso não irá acontecer.
PI = 3.14
radius = float(input('Qual o valor da circunferência? '))
# Potência, nesse exemplo é o valor de raio elevado a 2
area = PI * pow(radius, 2)

print(f"O valor da circunferência é: {area}")
