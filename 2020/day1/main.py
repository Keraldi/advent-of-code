import numba
import numpy as np

file = open('accounting', mode="r")
inp = file.read().splitlines()
lines = np.array(inp).astype(np.int32)


@numba.njit
def expense_report1(int_lines: 'np.array'):
    for a in int_lines:
        for b in int_lines:
            if a != b and a + b == 2020:
                return a * b


@numba.njit
def expense_report2(int_lines: 'np.array'):
    for a in int_lines:
        for b in int_lines:
            if a != b:
                k = a + b
                if k < 2020:
                    for c in int_lines:
                        if b != c != a and k + c == 2020:
                            return a * b * c


print(expense_report2(lines))
