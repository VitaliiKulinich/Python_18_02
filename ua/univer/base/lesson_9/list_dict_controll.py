def print_ru_by_eng_key(dict_er):
    for key in dict_er:
        print(f"{key} = {dict_er[key]}")


def find_word(list_dict):
    lang_from = input("Enter language from translate")
    lang_to = input("Enter language to translate")
    word = input("Enter eng word for translate")
    for dict_eruf in list_dict:
        if lang_from in dict_eruf and lang_to in dict_eruf:
            if dict_eruf[lang_from] == word:
                print(dict_eruf[lang_to])
                return
            else:
                print("Word not found")

def add_word(list_dict):
    lang = input("Enter language from translate")
    word = input("Enter word")
    new_dict = {}
    new_dict[lang] = word
    list_dict.append(new_dict)


def find_or_add(list_dict):
    lang_from = input("Enter language from translate")
    lang_to = input("Enter language to translate")
    word = input("Enter word")

    for dict_eruf in list_dict:
        if lang_from in dict_eruf and lang_to in dict_eruf:
            if dict_eruf[lang_from] == word:
                print(dict_eruf[lang_to])
            else:
                print("No word for translate, add new word")
                translate = input("New translate ")
                new_dict = {}
                new_dict[lang_from] = word
                dict[lang_to] = translate
                list_dict.add(new_dict)

