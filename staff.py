from person import *
class Staff(Person):
    def __init__(self, id_, first_name, last_name, age, role):
        super().__init__(id_, first_name, last_name, age)
        self.role = role