def polynomial_value(coefficient, x):
    # Обчислюємо значення полінома для заданого x
    result = 0
    max_stepen = len(coefficient) - 1
    # Вираховуємо значення полінома за допомогою циклу

    for i in range(len(coefficient)):
        result += coefficient[i] * (x ** max_stepen)
        max_stepen -= 1

    return result

# Основна частина програми
print('Уважно! Якщо ви наприклад вводите "n=3", то ваш поліном повинен виглядати як - ax^2+bx+c , [a,b,c]')
n = int(input('Введіть кількість коефіцієнтів (n): '))
coefficient = []

for i in range(n):
    coef = float(input(f"Введіть коефіцієнт для x^{n - 1 - i}: "))
    coefficient.append(coef)

# Введення значення x
x_input = input('Введіть значення при якому значенні "x" ви хочете порахувати поліном: ')

# Перевірка на тип введеного значення x
if '.' in x_input:
    x = float(x_input)
else:
    x = int(x_input)

# Обчислення значення полінома
result = polynomial_value(coefficient, x)

# Перевірка на тип введеного значення x та виведення відповідного результату
if isinstance(x, int):
    print(f"Значення полінома при значенні {x}: {int(result)}")
else:
    print(f"Значення полінома при значенні {x}: {result}")
