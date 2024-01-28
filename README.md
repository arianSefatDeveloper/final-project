# **This is aAdvanced Hotel Management System with Enhanced OOP in Python**




This project is a Hotel Management System implemented in Python, utilizing Object-Oriented Programming (OOP). The system manages various aspects of a hotel, such as staff, guests, and room bookings.

## Table of Contents

- [Classes](#classes)
  - [Person](#person)
  - [Admin](#admin)
  - [Staff](#staff)
  - [Guest](#guest)
  - [Rooms](#rooms)
  - [Hotel](#hotel)
- [Usage](#usage)

## Classes

### Person

- Attributes:

  - unique_id
  - name
  - contact_info

- Methods:
  - `__init__(self, unique_id, name, contact_info)`
  - `update_contact_details(self, new_contact_info)` 
  - `__str__(self)`

### Admin

- Inherits from `Person`.

- Additional Methods:
  - `create_staff_account(self, staff_details, hotel)` 
  - `remove_staff_member(self, staff_id)` 
  - `update_staff_role(self, staff_id, new_role)` 
  - `approve_maintenance_request(self, room_id, maintenance_type)`

### Staff

- Inherits from `Person`.

- Additional Methods:
  - `generate_payroll_report(self)`

#### Receptionist

.

- Additional Methods:
  - `book_guest(self, guest_id, room_id)`
  - `check_out_guest(self, guest_id)`

#### Housekeeping


- Additional Methods:
  - `mark_room_cleaned(self, room_id)`
  - `request_cleaning_supplies(self)`

#### Maintenance



- Additional Methods:
  - `report_repair_done(self, room_id)`: 
  - `order_repair_materials(self, material_list)`  

### Guest

- Inherits from `Person`.

- Additional Methods:
  - `request_room_booking(self, room_type, dates)` 
  - `amend_booking(self, booking_id, new_dates)` 
  - `cancel_booking(self, booking_id)` 
  - `give_feedback(self, feedback_text)`

### Rooms

- Methods:
  - `set_room_status(self, new_status)`
  - `schedule_room_maintenance(self, maintenance_type)`: 
  - `__str__(self)`

### Hotel

- Methods:
  - `__init__(self)`:  
  - `add_staff(self, staff)`: 
  - `list_available_rooms(self, room_type)` 
  - `get_guest_details(self, guest_id)` 
  - `summarize_daily_operations(self)`

## Usage

To use the Hotel Management System, you can instantiate the classes and call the methods based on your requirements. Below is a basic example:

```python
if __name__ == "__main__":
    h1 = Hotel()
    a1 = Admin(12 , "mmd" , "info)
    a1.create_staff_account()
    a1.remove_staff_member()
   

```



  
