from tabulate import tabulate


def f(x):
    return x ** 3 + (-5) * x ** 2 + (-20) * x + 105


def halfing_interval(a, b, e):

    table = []
    iteration = 1
    l = 1
    while l > e:
        x = (a + b) / 2  # середина інтервалу
        fx = f(x)
        y = a + (l/4)
        z = b - (l/4)
        fy = f(y)
        fz = f(z)

        table.append([iteration, round(a, 4), round(b, 4), round(x, 4), round(l, 4)])

        if fy < fx:
            b = x
        else:
            if fz < fx:
                a = x
            else:
                a = y
                b = z

        l = b - a

        iteration += 1

    optimal_x = (a + b) / 2  # оптимальне значення параметра x
    min_value = f(optimal_x)
    print(tabulate(table, headers=["Ітерація k", "ak", "bk", "xk(c)", "|bk-ak|"]))
    return round(optimal_x, 4), round(min_value, 4)


def golden_section(a, b, e):
    table = []
    gr1 = 0.382  # Золотий переріз
    gr2 = 0.618

    # Початкові точки
    y = a + gr1 * (b - a)
    z = a + gr2 * (b - a)

    iteration = 1
    while abs(b - a) > e:

        fy = f(y)
        fz = f(z)

        table.append([iteration, round(a, 4), round(b, 4), round(((a + b) / 2), 4), round(b - a, 4)])

        if fy <= fz:
            b = z
            z = y
            y = a + gr1 * (b - a)
        else:
            a = y
            y = z
            z = a + gr2 * (b - a)

        iteration += 1

    optimal_x = (a + b) / 2
    min_value = f(optimal_x)
    print(tabulate(table, headers=["Ітерація k", "ak", "bk", "xk(c)", "|bk-ak|"]))
    return round(optimal_x, 4), round(min_value, 4)


a_limit, b_limit = 0, 10
accuracy = 0.01
print("\nЦільова функція: f(x) = x^3 - 5x^2 - 20x + 105")
print(f"\nІнтервал: x ∈ [{a_limit};{b_limit}]")
print("\nТочність: ε =", accuracy)

print("\nМетод половинного ділення інтервалу")
print("\nПошук оптимального рішення")
x_1, y_1 = halfing_interval(a_limit, b_limit, accuracy)
print("\nОптимальне значення х =", x_1)
print("Мінімальне значення функції f(x) =", y_1)

print("\nМетод золотого перерізу")
print("\nПошук оптимального рішення")
x_2, y_2 = golden_section(a_limit, b_limit, accuracy)
print("\nОптимальне значення x:", x_2)
print("Мінімальне значення функції:", y_2)
