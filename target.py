import datetime


class target:
    def __init__(self, filename, how_often_check, first_notes, rating, reason):
        self.filename = filename
        self.init_date = datetime.datetime.now()
        self.how_often_check = how_often_check
        if first_notes != "":
            self.notes = {self.init_date: (first_notes, rating)}
        else:
            self.notes = {}
        self.reason = reason

    def addNote(self, note, rating):
        date = datetime.datetime.now()
        self.notes[date] = (note, rating)
