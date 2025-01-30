class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def eat(self):
        print(f"{self.name} is eating.")
        
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Do_study(self):
        print(f"{self.name} is studying.")

    def Do_attend_class(self):
        print(f"{self.name} is attending class.")

    def Do_take_exam(self):
        print(f"{self.name} is taking an exam.")

# Example usage:
dog = Animal("Dog")
dog.make_sound()
dog.sleep()
dog.eat()

car = Vehicle("Toyota")
car.start_engine()
car.honk()
car.stop_engine()

student = Student("Joel", 22)
student.study()
student.attend_class()
student.take_exam()

#Hii All im making the changes to the whole code 