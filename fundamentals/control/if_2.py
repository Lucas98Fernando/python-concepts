value = 'Lucas'  # True

# O valor zero o Python avalia como False
value = 0

# Qualquer número diferente de zero, independentemente de ser negativo ou não, o Python considera como um valor True
value = -0.001

value = ''  # False
value = ' '  # Com um espaço em branco ele considera True
value = []  # False
value = {} # False

if value:
    print("Existe!")
else:
    print("Não existe, é um valor zero ou vazio...")
