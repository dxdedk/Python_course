#1
print ('ЗАДАНИЕ 1')
class reqtangle:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def reqtangle_square(self):
        return self.A*self.B

    def reqtangle_perimetr(self):
        return (self.A+self.B)*2

req = reqtangle (10,20)
print(req.reqtangle_square())
print(req.reqtangle_perimetr(),"\n")

#2
print ('ЗАДАНИЕ 2')
class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, knowledge):
        self.knowledge.append(knowledge)

class Teacher:
    def __init__(self):
        self.number_of_students_taught = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
        self.number_of_students_taught += len(students)

class StudyMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

materials = StudyMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")
T = Teacher()
stud1 = Student()
stud2 = Student()
stud3 = Student()
stud4 = Student()

T.teach(materials.materials[0], stud1, stud2)
T.teach(materials.materials[1], stud1, stud3)
T.teach(materials.materials[2], stud2, stud3, stud4)
T.teach(materials.materials[3], stud4)
T.teach(materials.materials[4], stud1, stud2, stud3, stud4)

print("Stud 1 :", stud1.knowledge)
print("Stud 2 :", stud2.knowledge)
print("Stud 3 :", stud3.knowledge)
print("Stud 4 :", stud4.knowledge,"\n")

#3
print ("Задание 3")
import random
class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

class Student2(Person):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.knowledge = []

    def take(self, knowledge):
        self.knowledge.append(knowledge)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        if len(self.knowledge) > 0:
            random_index = random.randint(0, len(self.knowledge) - 1)
            removed_index = self.knowledge.pop(random_index)
            return removed_index

class Teacher2(Person):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.number_of_students_taught = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
        self.number_of_students_taught += len(students)

class StudyMaterial2:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):
        return len(self.materials)

materials2 = StudyMaterial2("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")
T2 = Teacher2("Петр", 35, "М")
stud21 = Student2("Вася", 18, "М")
stud22 = Student2("Петя", 17, "М")
stud23 = Student2("Аня", 19, "Ж")
stud24 = Student2("Надя", 16, "Ж")

T2.teach(materials2.materials[0], stud21, stud22)
T2.teach(materials2.materials[1], stud21, stud23)
T2.teach(materials2.materials[2], stud22, stud23, stud24)
T2.teach(materials2.materials[3], stud24)
T2.teach(materials2.materials[4], stud21, stud22, stud23, stud24)

print(stud21.full_name, stud21.knowledge)
print(stud22.full_name, stud22.knowledge)
print(stud23.full_name, stud23.knowledge)
print(stud24.full_name, stud24.knowledge,"\n")

print("Количество учебных дисциплин:", len(materials2))
print("Количество усвоенных дисциплин:",stud21.full_name, "-", len(stud21))
print("Количество усвоенных дисциплин:",stud22.full_name, "-", len(stud22))
print("Количество усвоенных дисциплин:",stud23.full_name, "-", len(stud23))
print("Количество усвоенных дисциплин:",stud24.full_name, "-", len(stud24),"\n")

FI = stud21.forget()
print (stud21.full_name, "не усвоил", FI)
print("После 'забывания'", stud21.full_name, "усвоил", len(stud21),"\n")

#4
print ("Задание 4")
class Apple:
    apple_stages = ["цветение", "зеленое", "красное"]

    def __init__(self, index):
        self.index = index
        self.apple_stage = self.apple_stages[0]

    def ripen(self):
        current_stage_index = self.apple_stages.index(self.apple_stage)
        if current_stage_index < len(self.apple_stages) - 1:
            self.apple_stage = self.apple_stages[current_stage_index + 1]

    def is_ripe(self):
        return self.apple_stage == self.apple_stages[-1]

class AppleTree:
    def __init__(self, *apples):
        self.apples = list(apples)

    def grow(self):
        for apple in self.apples:
            apple.ripen()

    def is_harvest_ready(self):
        return all(apple.is_ripe() for apple in self.apples)

    def harvest(self):
        if self.is_harvest_ready():
            self.apples = []
        else:
            print("Нельзя собрать урожай, не все яблоки созрели.")

class Gardener:
    def __init__(self, name, *plants):
        self.name = name
        self.plants = list(plants)

    def take_care_of_plants(self):
        for plant in self.plants:
            if isinstance(plant, AppleTree):
                plant.grow()

    def harvest_all(self):
        for plant in self.plants:
            if isinstance(plant, AppleTree):
                plant.harvest()

# Тестирование
apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)
tree = AppleTree(apple1, apple2, apple3, apple4, apple5)
gardener = Gardener("Петр", tree)

print("Стадии созревания яблок на дереве:")
for apple in tree.apples:
    print(apple.index, apple.apple_stage)

gardener.take_care_of_plants()
print("Стадии созревания яблок после ухода за деревьями:")
for apple in tree.apples:
    print(apple.index, apple.apple_stage)

gardener.harvest_all()

if tree.is_harvest_ready():
    print("Урожай собран.")
else:
    print("Не все яблоки созрели, урожай не может быть собран.")

gardener.take_care_of_plants()
print("Стадии созревания яблок после ухода за деревьями:")
for apple in tree.apples:
    print(apple.index, apple.apple_stage)

gardener.harvest_all()

if tree.is_harvest_ready():
    print("Урожай собран.")
else:
    print("Не все яблоки созрели, урожай не может быть собран.")

