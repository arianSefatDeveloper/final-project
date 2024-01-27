from person import *

class Guest(Person):
    def __init__(self, id_, first_name, last_name, age):
        super().__init__(id_, first_name, last_name, age)
    def request_room_booking(self, room_type, dates):
        pass

    def amend_booking(self, booking_id, new_dates):
        pass

    def cancel_booking(self, booking_id):
        pass

    def give_feedback(self, feedback_text):
        pass

if __name__ == "__main__":
    p1 = Guest("s400" , "mmd" , "reza" , 21)