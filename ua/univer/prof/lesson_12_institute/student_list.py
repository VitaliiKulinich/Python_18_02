from ua.univer.prof.lesson_12_institute.student import Student


class Student_List:
    def __init__(self):
        self.students = []

    def init_5_students(self):
        self.students = [
            Student("Vasya", 2000, "Kyiv", "+3801112233", "MMF", 1, "k11"),
            Student("Basya", 2001, "Kyiv", "+3801112233", "BBB", 2, "k13"),
            Student("Tasya", 2003, "Kyiv", "+3801112233", "AAA", 1, "k12"),
            Student("Masya", 2002, "Kyiv", "+3801112233", "MMF", 2, "k21"),
            Student("Dasya", 2004, "Kyiv", "+3801112233", "MMF", 1, "k11")
        ]

    def print_students_by_faculty_and_course(self, students):
        st_dict = students.get_students_by_faculty_and_course()
        for faculty in st_dict:
            print(faculty)
            for group in st_dict[faculty]:
                print("", group)
                for st in st_dict[faculty][group]:
                    print("    ", st)

    def get_students_by_faculty(self, faculty):
        st_list = []
        for st in self.students:
            if st.faculty == faculty:
                st_list.append(st)
                print(st)
        return st_list

    def get_students_with_average_mark_greater_than(self, mark):
        st_list = []
        for st in self.students:
            if st.average_mark() > mark:
                st_list.append(st)
                print(st)
        return st_list

    def get_students_after_year(self, year):
        st_list = []
        for st in self.students:
            if st.year > year:
                st_list.append(st)
                print(st)
        return st_list

    def get_students_by_faculty_and_course(self):
        st_dict = {}
        for st in self.students:
            if st.faculty not in st_dict.keys():
                st_dict[st.faculty] = {}
            if st.group not in st_dict[st.faculty].keys():
                st_dict[st.faculty][st.group] = []
            st_dict[st.faculty][st.group].append(st)
        return st_dict

    def print(self):
        for st in self.students:
            print(st)

