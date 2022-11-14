def Sum(summand_1, summand_2, summand_3, summand_4, key):
    dictionary = {
        "R": f"Результат вычисления: {summand_1+summand_2}",
        "C": f"Результат вычисления: {complex(summand_1,summand_2)+complex(summand_3, summand_4)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
