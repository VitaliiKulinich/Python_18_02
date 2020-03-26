class Student:
    id = 1

    def __init__(self, name, year, address, phone, faculty, course, group):
        self.group = group
        self.course = course
        self.__faculty = faculty
        self.__marks = [3,3,23,21,]
        self.name = name
        self.year = year
        self.address = address
        self.phone = phone
        self.__id = Student.id
        Student.id += 1


    def __str__(self):
        return f"{self.__id}, {self.name}, " \
               f"{self.year}, {self.address}, " \
               f"{self.phone}, {self.marks}, " \
               f"{self.faculty}, {self.course}, {self.group}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, mark):
        self.__marks.append(mark)

    def average_mark(self):
        sum = 0
        for mark in self.__marks:
            sum += mark
        return sum/self.__marks.__len__()

    @property
    def faculty(self):
        return self.__faculty

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        self.__course = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value
