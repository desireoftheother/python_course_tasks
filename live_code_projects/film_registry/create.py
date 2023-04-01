from val_module import *

# CREATE FILM

films_container = {
    1: {
        "name": "Avatar",
        "year": 2023,
        "director": "Tommy Wiseau",
        "imdb": 9.8
    },
    2: {
        "name": "Avatar 2",
        "year": 2000,
        "director": "Tommy Wiseau Sr.",
        "imdb": 10
    },
    3: {
        "name": "Pulp fiction",
        "year": 1678,
        "director": "Bruce willis.",
        "imdb": 1
    }
}


def create_film():
    """Ця функція створює dict з даними про фільм за наступним принципом:
    1. Дивиться у набір обов'язкових полів
    2. Запитує у користувача значення для цього поля
    3. Валідує це поле згідно оговорених правил
    4. Якщо поле не валідно, повторити запит допоки не введено правильне значення
    5. Створити dict з цих полів
    6. Якщо фільма з таким самим набором полів не існує в films_container - зберегти його в цю змінну
    Інакше - видати повідомлення (не робити raise exception)

    Hint 1: При збереженні в films_container треба створити унікальний ID у вигляді ключа, не забудьте про це

    Hint 2: зробіть валідатори для полів окремими функціями."""

    mandatory_fields_dict = {
        "name": validate_name,
        "year": validate_year,
        "director": validate_director,
        "imdb": validate_rank
    }

    mandatory_fields_types_dict = {
        "name": str,
        "year": int,
        "director": str,
        "imdb": float
    }

    mandatory_fields_final_dict = dict()

    for field_name, field_validator in mandatory_fields_dict.items():
        is_field_valid = False
        while not is_field_valid:
            field_value = input(f"Введить значення для поля {field_name} ")
            is_field_valid = field_validator(field_value)
            if not is_field_valid:
                print("Це поле не є валідним!")
        mandatory_fields_final_dict[field_name] = mandatory_fields_types_dict[field_name](field_value)

    # Наступна частина перевіряє, чи є в базі фільм з введеними даними
    # Тут я виходжу з того, що дані про фільм зберігаються у вигляді словника, де ключі - це айдішки фільмів,
    # а значення - вкладений словник з даними. Тобто наш films_container виглядає наступним чином:

    is_film_in_container = False

    for film in films_container.values():   # Перебираємо films_container, беручи по черзі словники з даними про окремий фільм
        for film_field_name, film_field_value in film.items():  # Перебираємо поля даних про фільм у films_container і порівнюємо їх з полями нашого mandatory_fields_final_dict
            if mandatory_fields_final_dict[film_field_name] != film_field_value:
                # Якщо значення у якомусь з полів не співпадають - виходимо з циклу, далі нема сенсу перевіряти
                break
        else:   # Якщо не було викликано break, значить всі значення співпали - піднімаємо прапорець, що такий фільм вже є у базі
            is_film_in_container = True

    if not is_film_in_container:    # Власне, якщо is_film_in_container = False - додаємо фільм до бази
        films_container[len(films_container)+1] = mandatory_fields_final_dict
    else:
        print('Такий фільм вже є у базі')
