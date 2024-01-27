from abc import ABC, abstractmethod

class Person:
    def __init__(self, id_, first_name, last_name, age):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
