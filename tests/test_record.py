from lib.record import *
import pytest


# Given a new Records instance
# When the user adds two diary entries
# Then reading the diary should return both entries in order

def test_add_two_entries_and_read_diary():
    record = Record()
    record.diary.add("Entry 1")
    record.diary.add("Entry 2")
    result = record.reflect_on_diary()
    assert result == ["Entry 1", "Entry 2"]


# Given multiple entries of varying lengths
# When user specifies available time and reading speed
# Then only the suitable entry (or entries) should be returned

def test_suitable_entries_are_returned():
    record = Record()
    record.diary.add("Entry Entry Entry Entry Entry Entry Entry One")
    record.diary.add("Entry Entry")
    record.diary.add("Entry Entry Entry Entry Two")
    result = record.read_when_busy(1, 5)
    assert result == ["Entry Entry", "Entry Entry Entry Entry Two"]


# Given a new Records instance
# When the user adds tasks and completes one
# Then only incomplete tasks remain in the list

def test_mark_complete_removes_tasks_from_list():
    record = Record()
    record.todo.add("task one")
    record.todo.add("task two")
    record.todo.add("task three")
    record.todo.add("task four")
    record.todo.add("task five")
    record.todo.done("task three")
    result = record.todo.todo_list
    assert result == ["task one", "task two", "task four", "task five"]



# Given a diary containing text with phone numbers
# When the user extracts and views contacts
# Then all valid numbers should appear in the contact list


def test_extract_and_view_all_phone_numbers():
    record = Record()
    record.diary.add("The old café on the corner still served the best flat " \
                        "white in town, and its chalkboard menu changed every week. " \
                        "If anyone wanted to reserve the back room they often left a " \
                        "note with a contact number: 02879546751.")
    record.diary.add("07719134942. Walking along the river, " \
                    "she found a blue envelope tucked under a bench with " \
                    "a single line of writing and a phone number: 02871234567. " \
                    "It felt like the start of an odd and promising mystery.")
    record.diary.add("He kept a small notebook of things to fix around the house " \
                    "— a leaky tap, a loose tile, and the electrician’s number " \
                    "written beside them: 02879998888. It was the sort of list " \
                    "that made weekends feel productive.")
    record.diary.add("The garden had gone wild while they were away, roses " \
                    "tumbling over the path and the lawn in desperate need of " \
                    "a trim. Neighbours dropped by with offers of help and a " \
                    "friendly smile, which made the chore seem less daunting.")
    record.diary.add("At dusk the market lights blinked on and the smell of " \
                    "roasting chestnuts filled the air; people chatted, " \
                    "children darted between stalls, and someone started playing " \
                    "a familiar tune that made everyone slow down and listen.")
    record.add_contacts()
    result = record.contacts.contacts_list
    assert result == ["02879546751", "07719134942", "02871234567", "02879998888"]


# Given the user has not added any diary entries
# When they try to read or reflect on the diary
# Then an empty list or a clear “no entries yet” message should be returned


def test_empty_diary_cant_be_read():
    record = Record()
    with pytest.raises(Exception) as e:
        record.reflect_on_diary()
    assert str(e.value) == "This diary is empty!"


# Given the user enters a diary entry with only whitespace or empty text
# When it is added to the diary
# Then it should be ignored or raise an exception instead of being stored

def test_empty_diary_record_cant_be_added():
    record = Record()
    with pytest.raises(Exception) as e:
        record.add_diary_entry("  ")
    assert str(e.value) == "Empty entries cannot be added!"


# Given the user has very limited reading time (e.g., 0 minutes)
# When they use the “read when busy” feature
# Then no entries should be returned

def test_limited_reading_time():
    record = Record()
    with pytest.raises(Exception) as e:
        record.read_when_busy(0, 20)
    assert str(e.value) == "You don't have time to read right now!"


# Given the user tries to mark a task as done that doesn’t exist
# When they call mark_as_done("Nonexistent Task")
# Then a clear error or “task not found” message should appear

def test_cant_mark_non_existent_task():
    record = Record()
    with pytest.raises(Exception) as e:
        record.mark_as_done("task1")
    assert str(e.value) == "Task not found!"


# Given the user adds duplicate task names
# When they view or complete tasks
# Then only the specific instance should be affected, or duplicates should be prevented

def test_cant_mark_non_existent_task():
    record = Record()
    record.add_a_task("task1")
    with pytest.raises(Exception) as e:
        record.add_a_task("task1")
    assert str(e.value) == "Task already exists!"


# Given a diary entry contains malformed or partial phone numbers
# When contacts are extracted
# Then invalid numbers should be ignored

def test_invalid_phone_numbers_are_not_added():
    record = Record()
    record.add_diary_entry("02879328509")
    record.add_diary_entry("356291-2")
    record.add_diary_entry("07719134942")
    record.add_diary_entry("hello07615456201")
    record.add_contacts()
    assert record.contacts.contacts_list == ["02879328509", "07719134942"]