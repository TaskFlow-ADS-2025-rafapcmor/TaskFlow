from src.taskflow import TaskFlow

def menu():
    print("\n===== TASKFLOW - GERENCIADOR DE TAREFAS =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def main():
    taskflow = TaskFlow()  # cria o gerenciador de tarefas

    while True:
        menu()
        opc = input("\nEscolha uma opção: ")

        if opc == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            taskflow.add_task(titulo, descricao)
            print("Tarefa adicionada com sucesso!")

        elif opc == "2":
            tarefas = taskflow.list_tasks()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\n--- TAREFAS ---")
                for i, task in enumerate(tarefas):
                    print(f"{i+1}. {task['title']} - {task['description']}")

        elif opc == "3":
            index = int(input("Número da tarefa para remover: ")) - 1
            if taskflow.remove_task(index):
                print("Tarefa removida!")
            else:
                print("Índice inválido.")

        elif opc == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
