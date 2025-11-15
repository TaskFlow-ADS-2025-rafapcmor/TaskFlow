Funcionalidade: Gerenciar tarefas no TaskFlow

  Cenário: Adicionar uma nova tarefa
    Dado que o usuário esteja usando o TaskFlow
    Quando ele adicionar uma tarefa chamada "Comprar pão"
    Então a tarefa "Comprar pão" deve aparecer na lista

  Cenário: Listar tarefas
    Dado que o usuário adicionou a tarefa "Estudar Python"
    Quando ele listar as tarefas
    Então a lista deve conter "Estudar Python"

  Cenário: Atualizar status da tarefa
    Dado que existe uma tarefa chamada "Lavar roupa"
    Quando atualizar o status para "concluída"
    Então o status da tarefa deve ser "concluída"

  Cenário: Buscar tarefa por nome
    Dado que existe uma tarefa chamada "Pagar contas"
    Quando ele buscar a tarefa por nome
    Então deve encontrar a tarefa "Pagar contas"

  Cenário: Remover tarefa
    Dado que existe uma tarefa chamada "Cortar cabelo"
    Quando ele remover essa tarefa
    Então ela não deve aparecer mais na lista

