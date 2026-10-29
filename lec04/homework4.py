

def next_birthday(date, birthdays):
    next_date = None

    for birthday_date in birthdays:
        if birthday_date > date:
            if next_date is None or birthday_date < next_date:
                next_date = birthday_date

    if next_date is None:
        next_date = min(birthdays)

    return next_date, birthdays[next_date]
