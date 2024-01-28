from person import *
from room import *
from guest import *
from admin import *
from hotel import *
class Staff(Person):
    def __init__(self, id_, first_name, last_name, age, role):
        super().__init__(id_, first_name, last_name, age)
        self.role = role
        self.guest_room = {}
    
      # receptionist
    def book_guest(self,  room ,room_id,  guest_id):
        if guest_id not in self.guest_room and room.room_is_available:
            self.guest_room[guest_id] = room_id
            room.room_is_available = False
            print(" booking successfully!")
        else:
            print("exists")
    def check_out_guest(self,room ,  guest_id):

        if guest_id in self.guest_room:

            self.guest_room.pop(guest_id)
            room.room_is_available = False
        else:
            print("guest id not exist")

    # housekeeping
    def mark_room_cleaned(self, room_id):
        pass

    def request_cleaning_supplies(self):
        pass

    # maintenance
    def report_repair_done(self, room_id):
        pass

    def order_repair_materials(self, material_list):
        pass  
if __name__ == "__main__":
    s1 = Staff("s400" , "mmd" , "reza" , 21)