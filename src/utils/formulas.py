import scipy.stats as stats

from src.constants.variables import (
    AVERAGE_A,
    AVERAGE_F,
    STANDARD_DEVIATION_A,
    STANDARD_DEVIATION_F,
)


def formula(case, r):
    if case == 1:
        return AVERAGE_A + (STANDARD_DEVIATION_A * stats.norm.ppf(r))
    else:
        return AVERAGE_F + (STANDARD_DEVIATION_F * stats.norm.ppf(r))
