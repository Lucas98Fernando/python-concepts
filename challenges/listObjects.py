class users:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


usersList = []

# Inserindo os dados na lista utilizando o retorno da classe
usersList.append(users('Lucas', 'lucas@gmail.com', 23))
usersList.append(users('João', 'joao@hotmail.com', 21))
usersList.append(users('Maria', 'maria@gmail.com', 25))

for key in usersList:
    print(key.name, key.email, key.age)

# É possível acessar através do index
print(usersList[0].name)
print(type(usersList))
