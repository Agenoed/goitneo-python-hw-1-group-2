from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            birthday_date = today + timedelta(days=delta_days)

            if birthday_date.weekday() >= 5:
                birthday_date += timedelta(days=(7 - birthday_date.weekday()))
            weekday = birthday_date.strftime("%A")
            birthday_dict[weekday].append(name)

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Kouк", "birthday": datetime(1971, 10, 22)},
    {"name": "Kim Kardashian", "birthday": datetime(1982, 10, 21)},
    {"name": "Jim Hox", "birthday": datetime(1976, 11, 30)},
    {"name": "Karoll Belt", "birthday": datetime(1998, 10, 18)},
]

get_birthdays_per_week(users)
