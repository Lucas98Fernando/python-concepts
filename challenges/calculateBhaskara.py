from math import sqrt


print('Cálculo de Bhaskara\n')

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = pow(b, 2) - ((4 * a) * c)

x1 = (- b + sqrt(delta)) / (2 * a)
x2 = ((- b) - sqrt(delta)) / (2 * a)

print('')
print(f'O valor de x1 é: {x1}')
print(f'O valor de x2 é: {x2}')

input('\nPressione enter para sair :)')
