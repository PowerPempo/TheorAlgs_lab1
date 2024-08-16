"""
Скласти та виконати на ПК програму розкладання довільного натурального числа в добуток ступенів простих чисел
Програма може бути складена на одній з наступних мов: С++, С#, java або Python.
"""

import math


def count(n):
    factors = {}


    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n = n // 2


    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n // i


    if n > 2:
        factors[n] = 1

    return factors


def main():
    n = int(input("Введіть натуральне число: "))
    if n <= 0:
        print("Число повинно бути натуральним (більше 0).")
        return

    factors = count(n)
    factorization = " * ".join([f"{key}^{value}" if value > 1 else f"{key}" for key, value in factors.items()])

    print(f"Розклад числа {n} на прості множники: {factorization}")


if __name__ == "__main__":
    main()
