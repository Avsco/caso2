import random
import scipy.stats as stats


def formula(average: float, variance: float, distribution: str):
    r = random.random()

    if distribution == "uniform":
        return average + (variance * stats.uniform.ppf(r))
    elif distribution == "exponential":
        return average + (variance * stats.expon.ppf(r))
    elif distribution == "normal":
        return average + (variance * stats.norm.ppf(r))

    return average + (variance * stats.norm.ppf(r))
