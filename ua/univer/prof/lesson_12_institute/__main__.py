from ua.univer.prof.lesson_12_institute.student_list import Student_List


def main_menu():
    print("Menu:")
    print("1. Init 5 students")
    print("2. Get students by faculty")
    print("3. Get students with average mark grater than")
    print("4. Get students after year")
    print("5. Get students by faculty and course")
    print("0. Stop program")
    key = int(input("Enter number: "))
    return key

if __name__ == '__main__':
    students = Student_List()
    while True:
        key = main_menu()

        if key == 0:
            break
        elif key == 1:
            students.init_5_students()
        elif key == 2:
            faculty = input("Faculty: ")
            st_list = students. get_students_by_faculty(faculty)
        elif key == 3:
            st_list = students.get_students_with_average_mark_greater_than(4)
            for st in st_list:
                print(st)
        elif key == 4:
            st_list = students.get_students_after_year(2001)
        elif key == 5:
            students.print_students_by_faculty_and_course()


