class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Error")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self):
        print("Eat")

    def list_of_fields(self):
        return [self.name, self.age]

    def __str__(self):
        return f"{self.name}, {self.age}"
