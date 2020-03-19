class Cat:
    def __init__(self, name="Tom", year=10, weight=5.5):
        self.name = name
        self.year = year
        self.weight = weight

    def show(self):
        if self.weight>0:
            print(self.name, self.year, self.weight)
        else:
            print("Dead cat", self.name)

    def eat(self, food):
        self.weight += food
        print(f"{self.name} eat {food}")

    def eat_mouse(self, mouse):
        if self.weight > 8:
            self.weight = 0
            print("Cat Buuhaaa....")
        if mouse.weight == 0:
            print("Nothing to eat")
            return
        self.weight += mouse.weight
        mouse.weight = 0
        mouse.killer = self
        print(f"Cat {self.name} eat {mouse.name}")