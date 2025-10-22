
class Diary():

    def __init__(self):
        self.diary_list = []

    def add(self, entry):
        if not entry.strip():
            raise Exception("Empty entry not allowed!")
        self.diary_list.append(entry)

    def read(self):
        return self.diary_list

    def busy(self, time, wpm):
        busy_list = []
        
        [busy_list.append(entry) 
         for entry in self.diary_list 
         if len(entry.split(" ")) / wpm <= time]
        
        return busy_list