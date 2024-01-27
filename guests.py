from person import *

class Guest(Person):
    def __init__(self, id_, first_name, last_name, age):
        super().__init__(id_, first_name, last_name, age)