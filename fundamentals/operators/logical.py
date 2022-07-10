a1 = True
a2 = False
a3 = True

print(a1 and a2)
print(a1 and a2 and a3)
print(a1 or a2)
print(a1 or a3)
print(a1 or a2 or a3)
print(not a1)
print(not a2)
print(a1 and not a2 and a3)

# Expressão equivalente ao xor ^ (ou exclusivo)
print(a1 != a2)

a = 6
b = 8

print(a1 and not a2 and a < b)

# Cuidado com operações Bit-a-bit, pois ela não deve ser usada quando a operação for utilizando operadores lógicos.

# Corresponde ao AND
True & True

# Corresponde ao OR
False | True

# Corresponde ao XOR
False ^ True

# AND Bit-a-bit
# 3 = 11
# 2 = 10
3 & 2
# Resultado: 10

# OR Bit-a-bit
# 3 = 11
# 2 = 10
3 | 2
# Resultado: 11

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
3 ^ 2
# Resultado: 01

# Exemplo - Verificar se o saldo estiver positivo e o que sobrou no mês for maior que 20%
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)

# Exemplo
trabalho_terca = True
trabalho_quinta = False

"""
Confirmando os dois trabalhos: TV 50' + Sorvete
Confirmando apenas 1 trabalho: TV 32' + Sorvete
Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # XOR
sorvete = trabalho_terca or trabalho_quinta
saudavel = not sorvete

# Com o método format() podemos informar quais variáveis serão associadas a cada par de chaves "{}" definidos em cada posição na string
print('Tv50={} Tv32={} Sorvete={} Saudável={} '.format(
    tv_50, tv_32, sorvete, saudavel))


# O format é indexado e através disso é possível mudar a ordem em que os dados serão inseridos
print('{1} {0}'.format('Lucas', 'Fernando'))
