import random

from src.utils.formulas import formula


def generate_list():
    list_random = []

    for _ in range(20):
        r1 = random.random()
        f1 = formula(1, r1)

        r2 = random.random()
        f2 = formula(2, r2)

        list_random.append([f1, f2])

    return list_random  # [[i, i + 1] for i in range(1, 21)]
