from ua.univer.prof.lesson_13_14_inheritance.doctor import Doctor
from ua.univer.prof.lesson_13_14_inheritance.fighter import Fighter
from ua.univer.prof.lesson_13_14_inheritance.human_factory import Human_factory
from ua.univer.prof.lesson_13_14_inheritance.student import Student


def cafe(human):
    human.eat()


def print_list_of_human_type(humans, human_type):
    count_h = 0
    list_h = []
    for h in humans:
        if isinstance(h, human_type):
            count_h += 1
            list_h.append(h)
    print(human_type.__name__, "count find =", count_h)
    for h in list_h:
        print(h)


def print_10_human_from_factory():
    humans = []
    for i in range(10):
        humans.append(humans_factory.get_human_by_key(i % 3))
    for h in humans:
        print(h.list_of_fields())


if __name__ == '__main__':

    humans_factory = Human_factory()
    #print_10_human_from_factory()
    humans = humans_factory.read_from_csv("humans.csv")

    print("What kind of human find?")
    human_str = input("Input : ")

    human_type = humans_factory.get_human_type_by_str(human_str)
    if human_type != None:
        print_list_of_human_type(humans, human_type)
    else:
        print("No such people")