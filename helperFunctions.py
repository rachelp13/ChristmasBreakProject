def getGradeString(grade):
    if grade > 90.0:
        if grade > 95:
            return "A+"
        elif grade > 92.5:
            return "A"
        else:
            return "A-"

    elif grade > 80.0:
        if grade > 85:
            return "B+"
        elif grade > 82.5:
            return "B"
        else:
            return "B-"

    elif grade > 70.0:
        if grade > 75:
            return "C+"
        elif grade > 72.5:
            return "C"
        else:
            return "C-"

    elif grade > 60.0:
        if grade > 65:
            return "D+"
        elif grade > 62.5:
            return "D"
        else:
            return "D-"
    else:
        return "F"