import pytest
from lib.Todo import ToDo


# Given an empty todo list, 
# when a task is added, 
# then it should appear in the list.
def test_add_task_to_empty_todo_list():
    todo = ToDo()
    todo.add("Buy milk")
    assert todo.show_tasks() == ["Buy milk"]


# Given a todo list with tasks, 
# when a task is marked as done, 
# then it should be removed from the list.
def test_mark_task_done_removes_it_from_list():
    todo = ToDo()
    todo.add("Buy milk")
    todo.add("Walk dog")
    todo.done("Buy milk")
    assert todo.show_tasks() == ["Walk dog"]


# Given a todo list, 
# when a user tries to mark a nonexistent task as done, 
# then an appropriate error should occur.
def test_mark_nonexistent_task_done_raises_error():
    todo = ToDo()
    todo.add("Buy milk")
    with pytest.raises(ValueError):
        todo.done("Clean car")


# Given duplicate task names, 
# when one is completed, 
# then only that instance should be removed.
def test_mark_one_of_duplicate_tasks_done_removes_one_instance():
    todo = ToDo()
    todo.add("Buy milk")
    todo.add("Buy milk")
    todo.done("Buy milk")
    assert todo.show_tasks() == ["Buy milk"]
