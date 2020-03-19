from ua.univer.prof.lesson_10_oop.cat import Cat
from ua.univer.prof.lesson_10_oop.cats_controller import get_list_cat_less_than_age, find_fat_cat
from ua.univer.prof.lesson_10_oop.mouse import Mouse

if __name__ == '__main__':
    cat0 = Cat(name="TomLi")
    cat1 = Cat(name="Tomidze", year=2, weight=3.7)

    m1 = Mouse(name="Jerry", weight=0.2)
    cat1.eat_mouse(m1)
    cat1.show()
    m1.show()

    m2 = Mouse("JerrykoFF", 4.5)
    cat1.eat_mouse(m2)
    m2.show()

    cat2 = Cat("Leopold", 9, 6.3)
    cat2.eat(0.5)
    cat2.eat_mouse(m2)
    cat2.show()
    list_cats = [cat0, cat1, cat2]
    list_cats_less_than_age = get_list_cat_less_than_age(list_cats, age=10)

    fat_cat = find_fat_cat(list_cats_less_than_age)
    print("\nFat cat:")
    fat_cat.show()
