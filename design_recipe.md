
<!-- Describe the problem -->

As a user
So that I can `record` my experiences
I want to keep a regular `diary`

As a user
So that I can `reflect` on my experiences
I want to `read my past diary entries`

As a user
So that I can reflect on my experiences in my `busy` day
I want to select diary entries to `read based on how much time I have and my reading speed`

As a user
So that I can keep track of my `tasks`
I want to keep a `todo list` along with my diary

As a user
So that I can keep track of my `contacts`
I want to see a list of all of the `mobile phone numbers` in all my diary entries


<!-- Design the class system -->

``` python

# keeps diary, todo list, and contacts all in one place
class Records():

    def __init__(self):
        self.diary = Diary()
        self.todo_list = ToDo()
        self.contacts = Contacts()

    def add_diary_entry(self):
        self.diary.add("Entry text")

    def reflect_on_diary(self):
        return self.diary.read()
    
    def read_when_busy(self, time, wpm):
        return self.diary.busy(time, wpm)
    
    def add_a_task(self):
        self.todo_list.add("Task text")

    def show_tasks(self):
        self.todo_list.show()

    def mark_as_done():
        self.todo_list.done("Task text")
    
    def add_contact():
        self.contacts.add()

    def show_contacts():
        self.contacts.show()


class Diary():

    def __init__(self):
        self.diary_list = []

    def add(self, entry):
        self.diary_list.append(entry)

    def read(self):
        return self.diary_list
    
    def busy(self, time, wpm):
        pass


class Todo(self):
    
    def __init__():
        self.todo_list = []
    
    def add(self, task):
        self.todo_list.append(task)

    def show_tasks(self):
        return self.todo_list

    def mark_as_done(self, task):
        self.to_do_list.remove(task)


class Contacts(self):

    def __init__():
        self.contacts = []
    
    def add(self, contact):
        self.contacts.append(contact)

    def show(self):
        returns self.contacts

```


<!-- Create examples of integration tests -->


<!-- TEST 1 -->

Given a new Records instance
When the user adds two diary entries
Then reading the diary should return both entries in order

<!-- TEST 3 -->

Given multiple entries of varying lengths
When user specifies available time and reading speed
Then only the suitable entry (or entries) should be returned

<!-- TEST 4 -->

Given a new Records instance
When the user adds tasks and completes one
Then only incomplete tasks remain in the list

<!-- TEST 5 -->

Given a diary containing text with phone numbers
When the user extracts and views contacts
Then all valid numbers should appear in the contact list

<!-- TEST 6 -->

Given the user has not added any diary entries
When they try to read or reflect on the diary
Then an empty list or a clear “no entries yet” message should be returned

<!-- TEST 7 -->

Given the user enters a diary entry with only whitespace or empty text
When it is added to the diary
Then it should be ignored or raise an exception instead of being stored

<!-- TEST 8 -->

Given the user has very limited reading time (e.g., 0 minutes)
When they use the “read when busy” feature
Then no entries should be returned

<!-- TEST 9 -->

Given the user tries to mark a task as done that doesn’t exist
When they call mark_as_done("Nonexistent Task")
Then a clear error or “task not found” message should appear

<!-- TEST 10 -->

Given the user adds duplicate task names
When they view or complete tasks
Then only the specific instance should be affected, or duplicates should be prevented

<!-- TEST 11 -->

Given a diary entry contains malformed or partial phone numbers
When contacts are extracted
Then invalid numbers should be ignored




<!-- Create examples as unit tests  -->


<!-- DIARY -->

Given a new diary, when a user adds an entry, then the diary list should contain that entry.

Given a diary with multiple entries, when the user reads it, then all entries should be returned in order.

Given a diary with entries of varying lengths, when the user uses the busy filter, then only entries that fit the time and speed should be returned.

Given an empty diary, when the user reads it, then an empty list should be returned.

Given a diary entry that is empty or only whitespace, when it’s added, then it should be ignored or raise an error.

<!-- TODO -->

Given an empty todo list, when a task is added, then it should appear in the list.

Given a todo list with tasks, when a task is marked as done, then it should be removed from the list.

Given a todo list, when a user tries to mark a nonexistent task as done, then an appropriate error should occur.

Given duplicate task names, when one is completed, then only that instance should be removed.


<!-- CONTACTS -->

Given an empty contacts list, when a contact is added, then it should appear in the list.

Given multiple contacts, when they are shown, then they should appear in the order added.

Given duplicate contacts, when they are shown, then duplicates should not appear twice.

Given invalid contact data, when it’s added, then it should be ignored or raise an error.


<!-- Implement the behavior -->















