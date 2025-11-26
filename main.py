from src.task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n=== TASKFLOW - GERENCIADOR DE TAREFAS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            manager.add_task(titulo, descricao)
            print("✔ Tarefa adicionada com sucesso!")

        elif opcao == "2":
            tarefas = manager.list_tasks()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\n--- TAREFAS ---")
                for t in tarefas:
                    status = "Concluída" if t.completed else "Pendente"
                    print(f"[{t.id}] {t.title} - {status}")

        elif opcao == "3":
            task_id = input("ID da tarefa a concluir: ")
            if manager.complete_task(task_id):
                print("✔ Tarefa concluída!")
            else:
                print("❌ Tarefa não encontrada.")

        elif opcao == "4":
            task_id = input("ID da tarefa a remover: ")
            if manager.remove_task(task_id):
                print("✔ Tarefa removida!")
            else:
                print("❌ Tarefa não encontrada.")

        elif opcao == "5":
            print("Encerrando o TaskFlow...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
