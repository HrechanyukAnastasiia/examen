#10
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)

student1 = Student("Настя", 16)
student1.get_info()