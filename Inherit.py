#single inheritance 
class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def company_details(self):
        print("Company Name:", self.company_name)
        print("Location:", self.location)


class Employee(Company):   # Inheriting Company 
    def __init__(self, company_name, location, emp_name, salary):
        # calling parent constructor
        super().__init__(company_name, location)
        self.emp_name = emp_name
        self.salary = salary

    def employee_details(self):
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)


# Creating object
emp1 = Employee("TCS", "Bangalore", "Naveen", 50000)

# Calling methods
emp1.company_details()
emp1.employee_details()


#multiple inheritance
class Camera:
    def take_photo(self):
        print("Taking a photo")

    def record_video(self):
        print("Recording a video")


class Music:
    def play_music(self):
        print("Playing music")

    def stop_music(self):
        print("Stopping music")


class Smartphone(Camera, Music):   # Multiple Inheritance
    def make_call(self):
        print("doing call ")



phone = Smartphone()

phone.take_photo()     
phone.record_video()   
phone.play_music()     
phone.stop_music()     
phone.make_call()     


#multilevel inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):   # Level 1 Inheritance
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student(self):
        print("Student ID:", self.student_id)


class Graduate(Student):   # Level 2 Inheritance
    def __init__(self, name, age, student_id, degree):
        super().__init__(name, age, student_id)
        self.degree = degree

    def show_graduate(self):
        print("Degree:", self.degree)


g1 = Graduate("Naveen", 22, "S101", "MCA")
g1.show_person()
g1.show_student()
g1.show_graduate()


#hierarchical inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):   # Child 1
    def car_type(self):
        print("This is Car ")


class Bike(Vehicle):  # Child 2
    def bike_type(self):
        print("This is Bike ")


class Truck(Vehicle): # Child 3
    def truck_type(self):
        print("This is Truck")


c = Car("Toyota")
b = Bike("Yamaha")
t = Truck("Tata")

c.show_brand()
c.car_type()

b.show_brand()
b.bike_type()

t.show_brand()
t.truck_type()


#hybrid 