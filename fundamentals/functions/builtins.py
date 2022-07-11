# O Builtins é o módulo que fornece alguns métodos e tipos que estão inseridos no Python

# Isso é o mesmo que => print(type('Olá pessoal!'))
print(__builtins__.type('Olá pessoal!'))

# O método dir() serve para visualizar o escopo global do Python, exibindo variáveis, módulos, etc... que foram criados ou importados
print(dir())

# Visualizar tudo o que está presente dentro do escopo do builtins
print(dir(__builtins__))
