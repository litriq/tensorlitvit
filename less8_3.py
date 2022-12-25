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
    
    def __lt__(self, other):
        self_homeworks = self.homeworks
        other_homeworks = other.homeworks
        return self_homeworks < other_homeworks
    
    def __eq__(self, other):
        self_homeworks = self.homeworks
        other_homeworks = other.homeworks
        return self_homeworks == other_homeworks

    def __gt__(self, other):
        self_homeworks = self.homeworks
        other_homeworks = other.homeworks
        return self_homeworks > other_homeworks

Yuri = Student('Yuri', 'Nechaev', 21, 74, 172, 10)
Gleb = Student('Gleb', 'Toropyko', 20, 61, 175, 6)
print (Yuri)
print (Gleb)
if Yuri<Gleb:
    print(f'{Yuri.name} сдал меньше домшних заданий, чем {Gleb.name}')
if Yuri==Gleb:
    print(f'{Yuri.name} сдал столько же домшних заданий, сколько сдал {Gleb.name}')
if Yuri>Gleb:
    print(f'{Yuri.name} сдал больше домшних заданий, чем {Gleb.name}')
