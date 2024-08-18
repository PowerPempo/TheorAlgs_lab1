def polynomial_value(coefficients, x):
    result = 0
    n = len(coefficients) - 1
    k = 0

    while k <= n:
        result += coefficients[k] * (x ** (n - k))
        k += 1

    return result

print('Увага! Якщо ви вводите "n=3", то ваш поліном має виглядати як ax^2 + bx + c, [a, b, c]')
n = int(input('Введіть кількість коефіцієнтів (n): '))
coefficients = []

k = 0
while k < n:
    coef = float(input(f"Введіть коефіцієнт для x^{n - 1 - k}: "))
    coefficients.append(coef)
    k += 1

x_input = input('Введіть значення "x", для якого ви хочете обчислити поліном: ')
x = float(x_input) if '.' in x_input else int(x_input)


result = polynomial_value(coefficients, x)

# Виведення результату
if isinstance(x, int):
    print(f"Значення полінома при x = {x}: {int(result)}")
else:
    print(f"Значення полінома при x = {x}: {result}")
