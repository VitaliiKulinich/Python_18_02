from ua.univer.prof.lesson_13_inheritance.doctor import Doctor
from ua.univer.prof.lesson_13_inheritance.fighter import Fighter
from ua.univer.prof.lesson_13_inheritance.student import Student


def cafe(human):
    human.eat()


if __name__ == '__main__':
    st1 = Student("Vasya", 10, 1)
    doc1 = Doctor("Haus", -50, 666666)
    f1 = Fighter("BrusLi", 30, 100, 50)

