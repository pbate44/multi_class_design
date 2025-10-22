import pytest
from lib.Diary import Diary


# Given a new diary, 
# when a user adds an entry, 
# then the diary list should contain that entry.
def test_adds_entry_to_diary():
    diary = Diary()
    diary.add("Today I went for a run.")
    assert diary.read() == ["Today I went for a run."]


# Given a diary with multiple entries, 
# when the user reads it, 
# then all entries should be returned in order.
def test_reads_multiple_entries_in_order():
    diary = Diary()
    diary.add("Entry one.")
    diary.add("Entry two.")
    diary.add("Entry three.")
    assert diary.read() == ["Entry one.", "Entry two.", "Entry three."]


# Given a diary with entries of varying lengths, 
# when the user uses the busy filter, 
# then only entries that fit the time and speed should be returned.
def test_busy_filter_returns_only_entries_that_fit_time_and_speed():
    diary = Diary()
    diary.add("Short entry.")
    diary.add("This entry is slightly longer than the first one.")
    diary.add("This is a much longer diary entry with plenty of words to test the reading time filter.")

    result = diary.busy(time=1, wpm=5)
    assert result == ["Short entry."]


# Given an empty diary, 
# when the user reads it, 
# then an empty list should be returned.
def test_read_empty_diary_returns_empty_list():
    diary = Diary()
    assert diary.read() == []


# Given a diary entry that is empty or only whitespace, 
# when it’s added, 
# then it should be ignored or raise an error.
def test_add_empty_or_whitespace_entry_raises_error():
    diary = Diary()
    with pytest.raises(Exception):
        diary.add("   ")