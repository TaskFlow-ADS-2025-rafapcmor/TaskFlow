TaskFlow – Sistema de Gerenciamento de Tarefas

Projeto desenvolvido para a A3 da disciplina Gestão e Qualidade de Software, do curso Análise e Desenvolvimento de Sistemas.
O objetivo é demonstrar boas práticas de desenvolvimento, testes unitários e testes BDD aplicado a um projeto real.

🚀 Descrição do Projeto

O TaskFlow é um sistema simples de gerenciamento de tarefas desenvolvido em Python, focado em organização, qualidade e boas práticas.

O sistema permite:

Criar tarefas

Marcar tarefas como concluídas

Listar tarefas

Filtrar tarefas concluídas e pendentes

🧱 Estrutura do Projeto
taskflow/
│── src/
│   └── taskflow/
│       ├── __init__.py
│       ├── task.py
│       └── task_manager.py
│
│── tests/
│   ├── __init__.py
│   └── test_tasks.py
│
│── features/
│   ├── task_management.feature
│   └── steps/
│       └── steps_task.py
│
│── requirements.txt
│── README.md

🧪 Testes Unitários (Pytest)

Para rodar os testes unitários:

pytest -v


Os testes validam:

Criação de tarefas

Conclusão de tarefa

Listagem

Filtragem

👣 Testes BDD (Behave)

Os cenários estão em:
features/task_management.feature

Para rodar:

behave


O BDD simula o comportamento real do usuário no sistema.

🛠️ Tecnologias Utilizadas

Python

Pytest

Behave

Gherkin

Git + GitHub

📌 Objetivo Acadêmico

Demonstrar:

organização do código

uso de testes

documentação clara

boas práticas de qualidade de software

✨ Autores

Arthur Vitor; Gabriel; João Vittor; João Pedro; Shayene Lorena

Curso: Análise e Desenvolvimento de Sistemas

Disciplina: Gestão e Qualidade de Software
