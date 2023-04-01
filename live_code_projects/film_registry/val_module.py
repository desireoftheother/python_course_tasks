import re

# Валідатори полів

DEFAULT_NAME_LEN_THRESHOLD = 200
LOW_YEAR_THRESHOLD = 1895
def validate_name(value, len_threshold=DEFAULT_NAME_LEN_THRESHOLD):
    # Перевіряємо довжину назви фільма, порожність назви фільма і щоб не було тільки пробілів і табуляцій
    len_value = len(value)
    is_len_appropriate = len_value < len_threshold
    is_only_spaces_or_tabs = value.count(" ") + value.count("\t") == len_value
    return is_len_appropriate and not is_only_spaces_or_tabs


def validate_year(value):
    is_digit = value.isdigit()
    if is_digit:
        value = int(value)
        if value >= 1895:
            return True
    else:
        return False


def validate_director(value):
    # Alphabet chars, spaces, dots, hyphens are allowed
    is_dir_valid = value.replace(" ", "").replace("-", "").replace(".", "").isalpha()
    return is_dir_valid


def validate_rank(value):
    pattern_for_floats = "^[0-9]+\.[0-9]+|\d+$"
    try:
        is_rank_valid_re = re.match(pattern_for_floats, value).string == value
    except AttributeError:
        is_rank_valid_re = None
    return is_rank_valid_re
