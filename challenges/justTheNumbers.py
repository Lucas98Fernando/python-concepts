values = [3, 'Lucas', 0, 9, 'Fernando']
onlyNumbers = []

for v in values:
    if type(v) == int or type(v) == float:
        onlyNumbers.append(v)

print(onlyNumbers)
