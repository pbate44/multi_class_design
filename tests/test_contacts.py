
import pytest
from lib.Contacts import Contacts


# Given an empty contacts list, 
# when a contact is added, 
# then it should appear in the list.
def test_add_contact_to_empty_list():
    contacts = Contacts()
    contacts.add(["Call me on 02871234567"])
    assert contacts.contacts_list == ["02871234567"]


# Given multiple contacts, 
# when they are shown, 
# then they should appear in the order added.
def test_multiple_contacts_show_in_order():
    contacts = Contacts()
    contacts.add(["My number is 02871234567"])
    contacts.add(["Office: 02879546751"])
    contacts.add(["Home: 02879998888"])
    assert contacts.contacts_list == ["02871234567", "02879546751", "02879998888"]


# Given duplicate contacts, 
# when they are shown, 
# then duplicates should not appear twice.
def test_duplicate_contacts_not_added_twice():
    contacts = Contacts()
    contacts.add(["Call 02871234567"])
    contacts.add(["My other note: 02871234567"])
    assert contacts.contacts_list == ["02871234567"]


# Given invalid contact data, 
# when it’s added, 
# then it should be ignored 
def test_invalid_contact_data_ignored():
    contacts = Contacts()
    contacts.add(["No valid numbers here", "Or here"])
    assert contacts.contacts_list == []
