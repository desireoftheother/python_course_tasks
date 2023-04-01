# READ FILM
from live_code_projects.film_registry.search import search_film_by_one_field_key, search_film_by_id
from live_code_projects.film_registry.main import films_container


def read_film() -> None:
    print('''It's function to search film by some fields:
     Here are the fields:
     -- ID
     -- Name
     -- Year
     -- Director
     -- IMDB
             ''')
    while True:
        field_name = input("Enter the name of the field to search (or 'id'): ")
        if field_name == "id" or field_name in films_container[1]:
            break
        else:
            print("Please enter a valid field name.")

    search_value = input(f"Enter the value for {field_name}: ")
    found_films = list()

    if field_name == "id":
        search_film_by_id(search_value)
    else:
        search_film_by_one_field_key(field_name, search_value)

    if found_films:
        print("Found films:")
        for film in found_films:
            film_id = list(film.keys())[0]
            info = film[film_id]
            print(f"Film ID: {film_id}")
            print(f"Name: {info['name']}")
            print(f"Year: {info['year']}")
            print(f"Director: {info['director']}")
            print(f"IMDB rating: {info['imdb']}")
    else:
        print("No films found.")

read_film()
