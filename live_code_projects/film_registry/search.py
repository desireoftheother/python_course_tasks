from live_code_projects.film_registry.main import films_container

def search_by_full_combination(item_dict):
    item_in_db = dict()
    for key, value in films_container.items():
        if value['name'] == item_dict["name"] and value['year'] == item_dict["year"]  and \
                value['director'] == item_dict["director"] and value['imdb'] == item_dict["imdb"]:
            item_in_db = {key: value}
            break
    return item_in_db


def search_film_by_one_field_key(field_name, search_value):
    found_films = list()
    for film_id, film in films_container.items():
        if field_name in film and search_value == str(film[field_name]):
            found_films.append({film_id: film})
    return found_films


def search_film_by_id(id_value):
    found_value = films_container.get(id_value, None)
    if found_value is not None:
        found_film = {id_value: found_value}
    else:
        found_film = dict()
    return found_film
