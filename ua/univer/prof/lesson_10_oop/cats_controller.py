def get_list_cat_less_than_age(list_cats, age):
    list_cats_less_age = []
    for cat in list_cats:
        if cat.year < age:
            list_cats_less_age.append(cat)
    return list_cats_less_age

def find_fat_cat(list_cats):
    fat_cat = list_cats[0]
    for cat in list_cats:
        if fat_cat.weight < cat.weight:
            fat_cat = cat
    return fat_cat
