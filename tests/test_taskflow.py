import pytest
from src.taskflow import TaskFlow

def test_add_task():
    tf = TaskFlow()
    task = tf.add_task("Estudar", "Revisar matéria")
    assert task.title == "Estudar"
    assert task.description == "Revisar matéria"
    assert task.status == "pendente"

def test_list_tasks():
    tf = TaskFlow()
    tf.add_task("Treinar")
    assert len(tf.list_tasks()) == 1

def test_update_status():
    tf = TaskFlow()
    task = tf.add_task("Ler")
    task.update_status("concluída")
    assert task.status == "concluída"

def test_get_task():
    tf = TaskFlow()
    tf.add_task("Acordar cedo")
    task = tf.get_task("Acordar cedo")
    assert task is not None
    assert task.title == "Acordar cedo"

def test_remove_task():
    tf = TaskFlow()
    tf.add_task("Academia")
    result = tf.remove_task("Academia")
    assert result is True
    assert tf.get_task("Academia") is None

