from src.taskflow import TaskFlow

def main():
    taskflow = TaskFlow()

    while True:
        print("\n=== TaskFlow - Gerenciador de Tarefas ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            title = input("Título da tarefa: ")
            description = input("Descrição da tarefa: ")
            taskflow.add_task(title, description)
            print("Tarefa adicionada com sucesso!")

        elif opc == "2":
            tasks = taskflow.list_tasks()
            if not tasks:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n=== Suas Tarefas ===")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.title} - {task.description}")

        elif opc == "3":
            tasks = taskflow.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.title}")
            
            index = int(input("Número da tarefa a remover: ")) - 1
            taskflow.remove_task(index)
            print("Tarefa removida com sucesso!")

        elif opc == "4":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
