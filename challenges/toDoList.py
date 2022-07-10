import uuid

option_selected = 0
valid_options = {1, 2, 3, 4}
tasks = []

print('To Do List\n')


class Tasks:
    def __init__(self, name, description):
        self.id = uuid.uuid1()
        self.name = name
        self.description = description


def add_task():
    name = input('\nNome da tarefa: ')
    description = input('Descrição da tarefa: ')

    tasks.append(Tasks(name, description))
    print('\nTarefa adicionada com sucesso!\n')


def view_tasks():
    if len(tasks) > 0:
        print('')
        for task in tasks:
            print(f'ID: {task.id}')
            print(f'Nome: {task.name}')
            print(f'Descrição: {task.description}')
            print('\n------------------------------------------------------\n')
    else:
        print('\nNenhuma tarefa foi adicionada ainda\n')


def delete_task():
    delete_by_id = input('\nInforme o ID da tarefa que você deseja excluir: ')
    index_to_delete = None

    for index, task in enumerate(tasks):
        if str(task.id) == delete_by_id:
            index_to_delete = index

    if index_to_delete != None:
        del tasks[index_to_delete]
        print('\nTarefa excluída com sucesso!\n')
    else:
        print('\nNão foi possível encontrar a tarefa com o ID informado\n')


while option_selected != 4:
    print('1 - Adicionar tarefa')
    print('2 - Visualizar tarefas')
    print('3 - Excluir tarefa')
    print('4 - Sair')

    option_selected = int(input('\nSelecione uma opção: '))

    if option_selected == 1:
        add_task()

    if option_selected == 2:
        view_tasks()

    if option_selected == 3:
        delete_task()

    if option_selected == 4:
        print('\nAté a próxima!')

    if not option_selected in valid_options:
        print('\nSelecione uma opção válida!\n')
