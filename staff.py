from person import *

class Staff(Person):
    def __init__(self, id_, first_name, last_name, age, role):
        super().__init__(id_, first_name, last_name, age)
        self.role = role
    
      # receptionist
    def book_guest(self, guest_id):
        pass
    def check_out_guest(self, guest_id):
        pass

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