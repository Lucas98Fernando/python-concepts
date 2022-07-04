# Para referenciar uma função localizada em um determinado módulo, é necessário um namespaced, com isso, é possível ter uma função com mesmo nome, porém de módulos diferentes.

# from functions import basic
# basic.salute()
# basic.salute('Fernando')
# # Utilizando parâmetros nomeados
# basic.salute(age=25)

from functions import args
sum = args.sum(2, 4, 1)
print(sum)

result = args.calculateAvg(name='Lucas', note1=7, note2=8.5)
print(result)
