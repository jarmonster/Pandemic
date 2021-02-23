
class Family:
    def __init__(self, nr):
        self.room = []
        self.nr = nr

    def insert(self, Person):
        self.room.append(Person)
    
class Person:
    def __init__(self, Student, nr, S, I, R, infection_date, Inew):
        self.Student = Student
        self.nr = nr
        self.S = S
        self.I = I
        self.R = R
        self.infection_date = infection_date
        self.Inew = Inew

    def studentify(self):
        self.Student = True

    def infectify(self): #only takes place in status update
        if self.S:
            self.S = False
            self.I = True
        elif self.Inew:
            self.Inew = False
            self.I = True
        elif self.I or self.R:
            pass
    
    def sickify(self): #infection
        if self.S:
            self.S = False
            self.Inew = True
        else:
            pass

    def recover(self):
        self.Inew = False
        self.I = False
        self.R = True
        self.S = False
    
    def status(self):
        if self.S:
            return "S"
        if self.I:
            return "I"
        if self.R:
            return "R"
        if self.Inew:
            return "Inew"
        
    def status_update(self, day):
        if self.Inew:
            self.infection_date = day
            self.infectify()
        if (day - self.infection_date) >= 5:
            self.recover()


class Building:
    def __init__(self):
        self.room = []

    def insert(self, Person):
        self.room.append(Person)

    def pop(self, index):
        self.room.pop(index)

