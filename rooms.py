class room:
    def __init__(self, room_id, room_is_available, room_type):
        self.room_id = room_id
        self.room_is_available = True
        self.room_type = room_type

    
    def display_room_status(self):
        return self.room_is_available

    def set_room_status(self, new_status):
        if self.room_is_available:
            self.room_is_available = False
        else:
          self.room_is_available = True

    def schedule_room_maintenance(self, maintenance_type):
        pass

    def __str__(self):
        return f"room id: {self.room_id}, type of room: {self.room_type}, room is avalebel:{self.room_is_available}"