import csv

from ua.univer.prof.lesson_13_14_inheritance.doctor import Doctor
from ua.univer.prof.lesson_13_14_inheritance.fighter import Fighter
from ua.univer.prof.lesson_13_14_inheritance.student import Student


class Human_factory:
    def get_human_by_key(self, key):
        return self.get_human_by_type(self.get_str_human_type_by_key(key))

    def get_human_type_by_str(self, key):
        human_dict = {
            "Student": Student,
            "Doctor": Doctor,
            "Fighter": Fighter
        }
        if key in human_dict.keys():
            return human_dict[key]
        else:
            return None

    def get_str_human_type_by_key(self, key):
        human_dict = {
            0: "Student",
            1: "Doctor",
            2: "Fighter"
        }
        return human_dict[key]

    def get_human_by_type(self, human_type):
        if human_type == "Student":
            return Student("Petya", 20, 2)
        elif human_type == "Doctor":
            return Doctor("Aybolit", 60, 777)
        elif human_type == "Fighter":
            return Fighter("Cannon", 30, 75, 65)

    def get_human_by_row(self, row):
        human_type = row[0]
        if human_type == "Student":
            name = row[1]
            age = int(row[2])
            group = int(row[3])
            return Student(name, age, group)
        elif human_type == "Doctor":
            name = row[1]
            age = int(row[2])
            licence = int(row[3])
            return Doctor(name, age, licence)
        elif human_type == "Fighter":
            name = row[1]
            age = int(row[2])
            power = int(row[3])
            defence = int(row[4])
            return Fighter(name, age, power, defence)

    def write_to_csv(self, humans, filename):
        with open(filename, "a", newline="") as users_csv:
            csv_w = csv.writer(users_csv)
            for h in humans:
                csv_w.writerow(h.list_of_fields())

    def read_from_csv(self, filename):
        humans = []
        with open(filename, "r", newline="") as users_csv:
            csv_r = csv.reader(users_csv)
            for row in csv_r:
                humans.append(self.get_human_by_row(row))
        return humans
