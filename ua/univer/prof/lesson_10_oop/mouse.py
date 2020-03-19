class Mouse:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.killer = None

    def show(self):
        if self.weight > 0:
            print(f"Mouse {self.name}, {self.weight}")
        else:
            print(f"Mouse {self.name} ...RIP... kill by {self.killer.name}")