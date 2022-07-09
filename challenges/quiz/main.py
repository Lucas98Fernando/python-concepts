import json

json_file = open('challenges/quiz/quiz.json')
data = json.load(json_file)
correct_questions_amount = 0

print('Python Quiz\n')

for i in data['questions']:
    print(f'{i["title"]}\n')

    for index, alt in enumerate(i['alternatives']):
        print(f'{index + 1} - {alt}')

    response = int(input('\nSua resposta: '))

    if response == i['answer']:
        print('\nResposta correta!\n')
        correct_questions_amount += 1
    else:
        print('\nResposta incorreta.\n')


questions_amount = len(data["questions"])
hit_percentage = (correct_questions_amount * 100) / questions_amount

print('Resultados:\n')
print(
    f'Você acertou {correct_questions_amount}/{questions_amount} das questões ({hit_percentage}% de aproveitamento)')
