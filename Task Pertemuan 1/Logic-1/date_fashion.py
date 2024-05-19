def date_fashion(you, date):
    if max(you, date) >= 8:
        if min(you, date) <= 2:
            return 0
        else:
            return 2
    elif min(you, date) <= 2:
        return 0
    else:
        return 1