import random
import datetime

today = datetime.datetime.today()
random_boundary_year = random.randint(0, 100)

while True:
    random_year = random.randint(today.year - random_boundary_year, today.year)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 31)
    if random_month == 2 and random_day == 29 and random_year % 4 == 0:
        break
    elif random_month == 2 and random_day > 28 and random_year % 4 != 0:
        continue
    elif random_month in [4, 6, 7, 9, 11] and random_day == 31:
        continue
    else:
        break

random_date = datetime.datetime(random_year, random_month, random_day)

print(f"Випадкова дата: {random_date.date()}")

time_difference = today - random_date

print(f"Різниця між сьогоднішнім днем і випадковою датою: {time_difference}")
