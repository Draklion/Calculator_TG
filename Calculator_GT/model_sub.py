def Subtraction(reduced1, deductible1, reduced2, deductible2, key):
    dictionary = {
        "R": f"Результат вычисления: {reduced1-deductible1}",
        "C": f"Результат вычисления: {complex(reduced1,deductible1)-complex(reduced2, deductible2)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
