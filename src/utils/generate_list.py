from src.utils.formulas import formula


def generate_list(options: dict = {}, limit: int = 0):
    distribution, average_a, average_f, variance_a, variance_f = (
        options["distribution"],
        options["average_a"],
        options["average_f"],
        options["variance_a"],
        options["variance_f"],
    )

    count = 0
    interferences = 0
    list_random = []

    # que el count tenga un nivel de seguridad de 95% respecto a la lista

    while (
        ((count / len(list_random)) < 0.95)
        if (limit == 0)
        else (len(list_random) < limit)
    ):
        f1 = formula(average=average_a, variance=variance_a, distribution=distribution)
        f2 = formula(average=average_f, variance=variance_f, distribution=distribution)

        list_random.append([f1, f2])

        if f1 > f2:
            interferences += 1
            if (f1 - f2) > 0.1:
                count += 1

    return {"list_random": list_random, "interferences": interferences, "case_b": count}
