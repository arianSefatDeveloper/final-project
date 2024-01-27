from abc import ABC, abstractmethod

class Person:
    def __init__(self, id_, first_name, last_name, age):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def update_contact_details(self, new_first_name=None, new_last_name=None, new_age=None):
        self.first_name = new_first_name or self.first_name
        self.last_name = new_last_name or self.last_name
        self.age = int(new_age or self.age)

    def __str__(self):
        return f"First Name is: {self.first_name}, Last Name is: {self.last_name}, Age is: {self.age} !"
    
    @abstractmethod
    def role(self):
        pass
        
if __name__ == "__main__":
    p1 = Person("s400" , "mmd" , "reza" , 21)