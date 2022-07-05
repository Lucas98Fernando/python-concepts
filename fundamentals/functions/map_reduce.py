from functools import reduce

notes = [5.8, 7.7, 8.2, 6.1, 8.5]

# Adicionar 1.5 a cada nota

# Solução 1
# for i, note in enumerate(notes):
#     notes[i] += 1.5

# Solução 2
# for i in range(len(notes)):
#     notes[i] += 1.5


def add_points(points):
    def calc(note):
        return note + points
    return calc


def sum(a, b):
    return a + b


# Solução 3 com o map() - Recomendado
final_result = list(map(add_points(1.5), notes))
print(final_result)

# Somar todas as médias

# Solução 1
# total = 0
# for n in notes:
#     total += n
# print(total)

# Solução 2 com o reduce() - Recomendado
total = reduce(sum, notes, 0)
print(total)
