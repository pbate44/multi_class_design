
class ToDo():
    
    def __init__(self):
        self.todo_list = []
    
    def add(self, task):
        self.todo_list.append(task)

    def show_tasks(self):
        return self.todo_list

    def done(self, task):
        self.todo_list.remove(task)