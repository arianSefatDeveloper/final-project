from person import *
from staff import *
from guest import *
from room import *
from admin import *

class Hotel:
    def __init__(self, name):
        self.name = name

    def list_available_rooms(self, room_type):
        pass

    def get_guest_details(self, guest_id):
        pass

    def summerize_daily_operations(self):
        pass


if __name__ == "__main__":
    p1 = Hotel("shiraz")