from ua.univer.prof.lesson_13_inheritance.human import Human


class Fighter(Human):
    def __init__(self, name, age, power, defence):
        super(Fighter, self).__init__(name, age)
        self.defence = defence
        self.power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        self.__power = value

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    def eat(self):
        print("Eat fighter")

    def fight(self, fighter):
        if self.power + self.defence > fighter.power + fighter.defence:
            print(f"{self.name} winner")
        else:
            print(f"{fighter.name} winner")

    def list_of_fields(self):
        return ["Fighter", self.name, self.age, self.power, self.defence]

    def __str__(self):
        return f"{self.name}, {self.age}, {self.power}, {self.defence}"
