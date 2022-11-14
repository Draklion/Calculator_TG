def Multiplication(multiplier_1, multiplier_2, multiplier_3, multiplier_4, key):
    dictionary = {
        "R": f"Результат вычисления: {multiplier_1*multiplier_2}",
        "C": f"Результат вычисления: {complex(multiplier_1, multiplier_2)*complex(multiplier_3, multiplier_4)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
