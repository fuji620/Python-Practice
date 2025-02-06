class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        print(f"{self.age + 1}年を取る")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id



student1 = Student("太郎", 20, "S12345")
print(student1.name)  # "太郎"
print(student1.age)   # 20
print(student1.get_student_id())  # "S12345"


student1.birthday() 