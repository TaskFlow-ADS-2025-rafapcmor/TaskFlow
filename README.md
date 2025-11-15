# 🗂️ TaskFlow  
Um projeto simples de gerenciamento de tarefas desenvolvido para a disciplina **Gestão e Qualidade de Software** utilizando **Python**, **Testes Unitários**, **BDD (Behavior Driven Development)** e boas práticas de documentação.

---

## 📌 Sobre o Projeto
O **TaskFlow** é um sistema que permite criar, listar, buscar, atualizar e remover tarefas.  
O objetivo principal é demonstrar na prática:

- Desenvolvimento orientado a testes (TDD)  
- Criação e execução de testes unitários  
- Aplicação de BDD utilizando Gherkin + Behave  
- Organização de projeto seguindo boas práticas  
- Estrutura e documentação de software  

---

## 🎯 Objetivos do Trabalho

- Criar um projeto funcional utilizando Python  
- Implementar testes unitários com pytest  
- Criar cenários BDD em Gherkin  
- Automatizar cenários BDD usando Behave  
- Documentar todo o projeto  
- Criar apresentação final  
- Utilizar GitHub Projects para gerenciamento  

---

## 📁 Estrutura do Projeto
taskflow/
├── src/
│ ├── taskflow.py
│ └── init.py
├── tests/
│ └── test_taskflow.py
├── features/
│ ├── taskflow.feature
│ └── steps/
│ └── taskflow_steps.py
├── requirements.txt
├── TEST_REGISTRY.md
├── slides/
│ └── (arquivo de apresentação)
└── README.md

---

## ⚙️ Como Instalar e Rodar

### 1️⃣ Criar ambiente virtual  
**Windows:**
```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1

## Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

## Instalar Dependências
pip install -r requirements.txt

## Como Executar os Testes
pytest -v

## Testes BDD(Behave)
behave

