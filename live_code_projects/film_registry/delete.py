import val_module as val
from live_code_projects.film_registry.search import search_by_full_combination, search_film_by_id
from live_code_projects.film_registry.main import films_container


def delete_full_combination():
    name_inp = input("Введіть назву фільму: ")
    year_inp = input("Введіть рік фільму: ")
    director_inp = input("Введіть режисера фільму: ")
    imdb_inp = input("Введіть рейтинг imdb: ")
    valid_name = val.validate_name(name_inp)
    valid_year = val.validate_year(year_inp)
    valid_director = val.validate_director(director_inp)
    valid_imdb = val.validate_rank(imdb_inp)
    is_combination_valid = valid_name and valid_year and valid_director and valid_imdb
    if is_combination_valid:
        item_to_delete_dict = {
            "name": name_inp,
            "year": int(year_inp),
            "director": director_inp,
            "imdb": float(imdb_inp)
        }
        found_item = search_by_full_combination(item_to_delete_dict)
        if found_item:
            del films_container[list(found_item.keys())[0]]
            return
        else:
            print("Такого фільму не існує. Введіть, будь ласка, дані ще раз.")
            delete_full_combination()
    else:
        print("Значення полів невалідне. Будь ласка, введіть дані ще раз")
        delete_full_combination()

def delete_id(id_input):
   found_item = search_film_by_id(int(id_input))
   if found_item:
       films_container.pop(found_item)
       print(f"Фільм з ID №{id_input} видалений.")
    else:
        print("Цього фільму немає")

def delete_film():
    GREETING_TEXT = """Вітаю в системі для видаленя даних про фільми."""
    print(GREETING_TEXT)
    print("Як бажаєте видалити фільм?", "За ID введіть команду 1", "За комбінацією полів введіть команду 2", sep='\n')
    command = int(input("Введіть команду: "))
    if command == 1:
        id_input = int(input("Введіть ID фільму: "))
        delete_id(id_input)
    elif command == 2:
        delete_full_combination()
    else:
        print("Введена невалідна команда. Введіть, будь ласка, команду ще раз.")
        delete_film()
