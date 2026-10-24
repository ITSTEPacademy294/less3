# print('hello')
#
# name = 'ltdhj'
# print(name)
#
# age = 15
# print(age)

class Student:
    def __init__(self, name='невідомий', height=160):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} виріс, зріст {self.height}")

    def __str__(self):
        return f"Студент {self.name}, його зріст - {self.height}"

    def __del__(self):
        print(f'студента {self.name} видалено')

Bob = Student('Bob', 150)
Kate = Student('Kate', 160)

Bob.grow(10)

print(Bob.name)