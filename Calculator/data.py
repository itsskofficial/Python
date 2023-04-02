def add(n1, n2):
    return round((n1 + n2), 2)


def subtract(n1, n2):
    return round((n1 - n2), 2)


def multiply(n1, n2):
    return round((n1 * n2), 2)


def divide(n1, n2):
    return round((n1 / n2), 2)


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
