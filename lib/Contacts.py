import re

class Contacts():

    def __init__(self):
        self.contacts_list = []
    
    def add(self, contact):
        numbers = re.findall(r"\b0\d{10}\b", " ".join(contact))
        for number in numbers:
            if number not in self.contacts_list:
                self.contacts_list.append(number)
            
            

    def show(self):
        return self.contacts_list