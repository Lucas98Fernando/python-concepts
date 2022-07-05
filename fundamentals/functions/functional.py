def sum(a, b):
    return a + b


def subtraction(a, b):
    return a - b


# Atribuindo o resultado de uma função para uma variável
methodSum = sum

print(methodSum(2, 4))


def aritmetic_operation(fn, num1, num2):
    return fn(num1, num2)


# Passando uma função como argumento para uma outra função
result = aritmetic_operation(sum, 4, 6)
print(result)

result = aritmetic_operation(subtraction, 10, 3)
print(result)


# Retornando uma função que está dentro de outra
# Esse tipo de implementação tem como objetivo de melhorar a performance de execução, através de um Lazy Loading (carregamento tardio)
def parcial_sum(a):
    # Imagina que aqui exista um procedimento pesado, se for utilizada a implementação convencional, todo o código que estiver aqui será chamado  cada vez que a função for invocada
    def sum_complete(b):
        return a + b
    return sum_complete


# Caso você armazene o resultado passando os dados relevantes para o primeiro processamento, você pode fazer com que o segundo processamento aguarde sua chamada, isso impacta positivamente na performance
sum_1 = parcial_sum(1)
r1 = sum_1(2)
r2 = sum_1(3)

final_result = parcial_sum(2)(8)
print(final_result, r1, r2)
