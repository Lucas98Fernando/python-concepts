value = float(input('Informe o valor do produto: '))
discount = float(input('Informe o valor do desconto (%): '))

valueWithDiscount = value - (value * (discount / 100))

print(
    f'O valor final do produto com {discount}% desconto foi: {valueWithDiscount}')
