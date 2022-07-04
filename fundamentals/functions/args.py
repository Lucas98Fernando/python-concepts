# Definindo argumentos variáveis utilizando o *, ou seja, a quantidade de argumentos que serão passados para a função é indefinido, nesse caso será uma tuple
def sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

# As ** no argumento da função indica que será recebido um dicionário
def calculateAvg(**args):
    avg = (float(args['note1']) + float(args['note2'])) / 2
    return f"O(A) aluno(a) {args['name']} ficou com a média => {avg}"
