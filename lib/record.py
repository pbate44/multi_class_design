from lib.Todo import *
from lib.Contacts import *
from lib.Diary import *



class Record():

    def __init__(self):
        self.diary = Diary()
        self.todo = ToDo()
        self.contacts = Contacts()

    def add_diary_entry(self, entry):
        if entry.strip() != "":
            self.diary.add(entry)
        else:
            raise Exception("Empty entries cannot be added!")

    def reflect_on_diary(self):
        if self.diary.diary_list:
            return self.diary.read()
        else:
            raise Exception("This diary is empty!")
    
    def read_when_busy(self, time, wpm):
        if time > 0:
            return self.diary.busy(time, wpm)
        else:
            raise Exception("You don't have time to read right now!")
    
    def add_a_task(self, task):
        if task in self.todo.todo_list:
            raise Exception("Task already exists!")
        else:    
            self.todo.add(task)

    def show_tasks(self):
        self.todo_list.show()

    def mark_as_done(self, task):
        if task in self.todo.todo_list:
            self.todo_list.done(task)
        else:
            raise Exception("Task not found!")
    
    def add_contacts(self):
        self.contacts.add(self.diary.diary_list)

    def show_contacts(self):
        self.contacts.show()