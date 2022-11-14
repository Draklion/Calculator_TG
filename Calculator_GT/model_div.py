def Division(divisible1, divider1, key):
    dictionary = {
        "R": f"Результат вычисления: {divisible1/divider1}"
    }
    return dictionary[key]

def Division_remain(divisible1, divider1, key):
    dictionary = {
        "R": f"Результат вычисления: {divisible1%divider1}"
    }
    return dictionary[key]
