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

    while len(list_random) < limit:
        f1 = formula(average=average_a, variance=variance_a, distribution=distribution)
        f2 = formula(average=average_f, variance=variance_f, distribution=distribution)

        list_random.append([f1, f2])

        if f1 > f2:
            interferences += 1
            if (f1 - f2) > 0.1:
                count += 1

    return {"list_random": list_random, "interferences": interferences, "case_b": count}


def generate_list_b(
    options: dict = {},
    security_level: float = 0.1,
    interference_probability: float = 0.95,
):
    distribution, average_a, average_f, variance_a, variance_f = (
        options["distribution"],
        options["average_a"],
        options["average_f"],
        options["variance_a"],
        options["variance_f"],
    )

    case_b = 0
    interferences = 0
    list_random = []

    # crear una condicion donde entre al while almenos 10 veces y un maximo de 1000 veces, si no se cumple la condicion
    # condition =

    count = 0

    while count < 5000:
        count += 1

        f1 = formula(average=average_a, variance=variance_a, distribution=distribution)
        f2 = formula(average=average_f, variance=variance_f, distribution=distribution)

        list_random.append([f1, f2])

        if f1 > f2:
            interferences += 1
            if (f1 - f2) > security_level:
                case_b += 1

        if not (case_b / len(list_random)) < interference_probability:
            break

    return {
        "list_random": list_random,
        "interferences": interferences,
        "case_b": count,
        "is_break": count == 5000,
    }
