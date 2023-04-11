from val_module import *


def update_film(films_container):
    way_to_update = input("Choose the way to update film\n"
                          "1. if by ID -> input id\n"
                          "2. if by the full combination of values -> combination \n"
                          "method: ").lower().strip()
    if way_to_update == "id":
        inputted_id = int(input("Provide the id: "))
        film_ids = [key for key in films_container.keys()]
        if inputted_id in film_ids:
            chosen_film = films_container[inputted_id]
            print(chosen_film)
            value_to_change = input("What do you want to change\n"
                                     "1. Name\n"
                                     "2. Year\n"
                                     "3. Director\n"
                                     "4. IMDB\n"
                                     "your choice: ").lower().strip()
            new_value = input("Input new value: ")
            if value_to_change in ['name', 'year', 'director', 'imdb']:
                if value_to_change == "name":
                    is_format_valid = False
                    iteration = 1
                    while not is_format_valid:
                        if iteration == 1:
                            if validate_name(new_value):
                                chosen_film["name"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                                iteration += 1
                        else:
                            new_value = input("New name: ")
                            if validate_name(new_value):
                                chosen_film["name"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                elif value_to_change == "year":
                    is_format_valid = False
                    iteration = 1
                    while not is_format_valid:
                        if iteration == 1:
                            if validate_year(new_value):
                                chosen_film["year"] = int(new_value)
                                is_format_valid = True
                            else:
                                print("Wrong format")
                                iteration += 1
                        else:
                            new_value = input("New name: ")
                            if validate_name(new_value):
                                chosen_film["year"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                elif value_to_change == "director":
                    is_format_valid = False
                    iteration = 1
                    while not is_format_valid:
                        if iteration == 1:
                            if validate_director(new_value):
                                chosen_film["director"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                                iteration += 1
                        else:
                            new_value = input("New name: ")
                            if validate_director(new_value):
                                chosen_film["director"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                elif value_to_change == "imdb":
                    is_format_valid = False
                    iteration = 1
                    while not is_format_valid:
                        if iteration == 1:
                            if validate_rank(new_value):
                                new_value = float(new_value)
                                chosen_film["imdb"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
                                iteration += 1
                        else:
                            new_value = input("New name: ")
                            if validate_rank(new_value):
                                new_value = float(new_value)
                                chosen_film["imdb"] = new_value
                                is_format_valid = True
                            else:
                                print("Wrong format")
    elif way_to_update == "combination":
        is_name_valid = False
        while not is_name_valid:
            name = input("Name: ").title()
            if validate_name(name):
                is_name_valid = True
            else:
                print("wrong format")
        is_year_valid = False
        while not is_year_valid:
            year = input("Year: ")
            if validate_year(year):
                is_year_valid = True
                year = int(year)
            else:
                print("wrong format")
        is_director_valid = False
        while not is_director_valid:
            director = input("Director: ").title()
            if validate_director(director):
                is_director_valid = True
            else:
                print("wrong format")
        is_rank_valid = False
        while not is_rank_valid:
            imdb = input("IMDB: ")
            if validate_rank(imdb):
                is_rank_valid = True
                imdb = float(imdb)
            else:
                print("wrong format")
        films_list = [film for film in films_container.values()]

        for film in films_list:
            is_name_found = film["name"] == name
            is_year_found = film["year"] == year
            is_director_found = film["director"] == director
            is_imdb_found = film["imdb"] == imdb
            if is_name_found and is_year_found and is_director_found and is_imdb_found:
                print(film)



example = {
    1: {
    "name": "Film",
    "year": 2023,
    "director": "Tommy",
    "imdb": 9.8
    },
    2: {
    "name": "FilmName",
    "year": 2000,
    "director": "Tommy Wiseau Sr.",
    "imdb": 10
    }
}
update_film(example)
