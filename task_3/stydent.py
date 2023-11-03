class Student:
    profession = 'Developer'

#     def check_profission(self):
#         print(self.profession)
#
# new_student = Student()

    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def check_profession(self):
        print(self.profession)

# new_student = Student ('Иван', 'Иванов', 22)
#
# new_student.check_profession()
#
# print(new_student.age)
# print(new_student.first_name)
# print(new_student.last_name)

    @staticmethod
    def print_location():
        print ('Санкт-Петербург')

Student.print_location()

new_student = Student ('Иван', 'Иванов', 22)
# new_student.print_location()
# print(new_student.age)
# print(new_student.first_name)
# print(new_student.last_name)