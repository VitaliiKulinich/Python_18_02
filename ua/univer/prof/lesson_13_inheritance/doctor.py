from ua.univer.prof.lesson_13_inheritance.human import Human


class Doctor(Human):
    def __init__(self, name, age, licence):
        super().__init__(name, age)
        self.licence = licence

    @property
    def licence(self):
        return self.__licence

    @licence.setter
    def licence(self, value):
        self.__licence = value

    def cure(self):
        print("Cure")

    def list_of_fields(self):
        return ["Doctor", self.name, self.age, self.licence]

    def __str__(self):
        return f"{self.name}, {self.age}, {self.licence}"
