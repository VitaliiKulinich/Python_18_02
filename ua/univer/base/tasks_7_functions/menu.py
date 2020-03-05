from ua.univer.base.tasks_7_functions.tasks import square_perimetr_of_equilateral_triangle, add_right_digit, min_max, \
    sort_numbers, sign, ring_s, degree, factorial_2, palindrom


def menu():
    print("Enter the number of program:")
    print("1 - square, perimetr of equilateral triangle")
    print("2 - add right digit")
    print("3 - min, max")
    print("4 - sort")
    print("5 - sign")
    print("6 - ring")
    print("7 - degree")
    print("8 - factorial")
    print("9 - palindrom")

    print("Your number = ")
    number = int(input())

    if number == 1: square_perimetr_of_equilateral_triangle()
    if number == 2: add_right_digit()
    if number == 3: min_max()
    if number == 4: sort_numbers()
    if number == 5: sign()
    if number == 6: ring_s()
    if number == 7: degree()
    if number == 8: factorial_2()
    if number == 9: palindrom()

