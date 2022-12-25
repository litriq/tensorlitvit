class Human:
    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height

class Student(Human):
    def __init__(self, name, surname, age, weight, height, homeworks):
        super().__init__(name, surname, age, weight, height)
        self.homeworks = homeworks
    def __str__(self):
        return "Студент {0} сдал {1} домашних заданий".format(self.name, self.homeworks)

Yuri = Student('Yuri', 'Nechaev', 21, 74, 172, 3)
print(Yuri)