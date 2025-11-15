from behave import given, when, then
from src.taskflow import TaskFlow

@given("que o usuário esteja usando o TaskFlow")
def step_impl(context):
    context.tf = TaskFlow()

@when('ele adicionar uma tarefa chamada "Comprar pão"')
def step_impl(context):
    context.tf.add_task("Comprar pão")

@then('a tarefa "Comprar pão" deve aparecer na lista')
def step_impl(context):
    titles = [task.title for task in context.tf.list_tasks()]
    assert "Comprar pão" in titles


@given('que o usuário adicionou a tarefa "Estudar Python"')
def step_impl(context):
    context.tf = TaskFlow()
    context.tf.add_task("Estudar Python")

@when("ele listar as tarefas")
def step_impl(context):
    context.tasks = context.tf.list_tasks()

@then('a lista deve conter "Estudar Python"')
def step_impl(context):
    titles = [task.title for task in context.tasks]
    assert "Estudar Python" in titles


@given('que existe uma tarefa chamada "Lavar roupa"')
def step_impl(context):
    context.tf = TaskFlow()
    context.task = context.tf.add_task("Lavar roupa")

@when('atualizar o status para "concluída"')
def step_impl(context):
    context.task.update_status("concluída")

@then('o status da tarefa deve ser "concluída"')
def step_impl(context):
    assert context.task.status == "concluída"


@given('que existe uma tarefa chamada "Pagar contas"')
def step_impl(context):
    context.tf = TaskFlow()
    context.tf.add_task("Pagar contas")

@when("ele buscar a tarefa por nome")
def step_impl(context):
    context.task = context.tf.get_task("Pagar contas")

@then('deve encontrar a tarefa "Pagar contas"')
def step_impl(context):
    assert context.task.title == "Pagar contas"


@given('que existe uma tarefa chamada "Cortar cabelo"')
def step_impl(context):
    context.tf = TaskFlow()
    context.tf.add_task("Cortar cabelo")

@when("ele remover essa tarefa")
def step_impl(context):
    context.tf.remove_task("Cortar cabelo")

@then("ela não deve aparecer mais na lista")
def step_impl(context):
    task = context.tf.get_task("Cortar cabelo")
    assert task is None

