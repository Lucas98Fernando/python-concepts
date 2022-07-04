# A palavra reservada def significa: Defining a function (Definindo uma função)
def salute(name='Lucas', age=20):
    print(f'Hello, {name}! \n Você tem {age} anos')


# É possível sobrescrever a mesma função, porém sem sobrecarregar, gerando algum gargalo
# def salute():
#     print('Olá, sou uma função repetida')

# Se o código for executado a partir desse arquivo, a função salute() será chamada com os argumentos 'Ana' e age=30, essa abordagem serve como se fosse o método main() em outras linguagens, como Java ou Dart, por exemplo...
if __name__ == '__main__':
    salute('Ana', age=30)
