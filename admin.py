from person import *
class Admin(Person):
    def __init__(self, id_, first_name, last_name, age):
        super().__init__(id_, first_name, last_name, age)
        self.staff_members = {}

    def create_staff_account(self, staff_details): 
        staff_id = input("Enter the ataff id: ")
        staff_first_name = input("Enter the staff first name:")
        staff_last_name = input("Enter the staff last name: ")
        staff_age = int(input("Enter the staff age: "))
        staff_role = input("new staff role: ")
        if staff_details.id_ not in self.staff_members:
            self.staff_members[staff_details.staff_id] = staff_details

        

    def remove_staff_member(self, staff_id):
        pass

    def update_staff_role(self, staff_id, new_role):
        pass

    def approve_maintenance_request(self, room_id, maintenance_type):
        pass

    def generate_payroll_report(self):
        pass
    def display_role(self):

        print(f"{self.name} is a admin!")

if __name__ == "__main__":
    a1 = Admin("s400" , "mmd" , "arian" , 21)