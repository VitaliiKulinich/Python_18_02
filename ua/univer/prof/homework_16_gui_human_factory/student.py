from ua.univer.prof.lesson_13_14_inheritance.human import Human


class Student(Human):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value

    def study(self):
        print("Study")

    def list_of_fields(self):
        return ["Student", self.name, self.age, self.group]

    def __str__(self):
        return f"{self.name}, {self.age}, {self.group}"
