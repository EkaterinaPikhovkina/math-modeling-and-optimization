from math import exp, sin, cos, sqrt
import pandas as pd
import matplotlib.pyplot as plt


def derivative(x, y):
    return y + cos(x/sqrt(5))


def formula(c, x):
    y = c * exp(x) + ((sqrt(5) * sin(sqrt(5) * x / 5)) / 6) - ((sqrt(5) * cos(sqrt(5) * x / 5)) / 6)
    return y


def exact(derivative, x0, y0, h, bottom_limit, upper_limit):

    c = (y0 - ((sqrt(5) * sin(sqrt(5) * x0 / 5)) / 6) + ((sqrt(5) * cos(sqrt(5) * x0 / 5)) / 6)) / exp(x0)
    n = round((upper_limit - bottom_limit) / h + 1)
    x_values = [x0 + i * h for i in range(n)]
    y_values = [y0]

    for x in x_values[1:]:
        y_next = formula(c, x)
        y_values.append(y_next)

    x_values = [round(x, 4) for x in x_values]
    y_values = [round(y, 4) for y in y_values]

    return x_values, y_values


def euler(derivative, x0, y0, h, bottom_limit, upper_limit):

    n = round((upper_limit - bottom_limit) / h + 1)
    x_values = [x0 + i * h for i in range(n)]
    y_values = [y0]

    for i in range(1, n):
        x_prev, y_prev = x_values[i - 1], y_values[-1]
        y_next = y_prev + h * derivative(x_prev, y_prev)
        y_values.append(y_next)

    x_values = [round(x, 4) for x in x_values]
    y_values = [round(y, 4) for y in y_values]

    return x_values, y_values


def euler_cauchy(derivative, x0, y0, h, bottom_limit, upper_limit):

    n = round((upper_limit - bottom_limit) / h + 1)
    x_values = [x0 + i * h for i in range(n)]
    y_values = [y0]

    for i in range(1, n):
        x_prev, y_prev = x_values[i - 1], y_values[-1]
        y_temp = y_prev + h * derivative(x_prev, y_prev)
        y_next = y_prev + h / 2 * (derivative(x_prev, y_prev) + derivative(x_values[i], y_temp))
        y_values.append(y_next)

    x_values = [round(x, 4) for x in x_values]
    y_values = [round(y, 4) for y in y_values]

    return x_values, y_values


def improved_euler(derivative, x0, y0, h, bottom_limit, upper_limit):

    n = round((upper_limit - bottom_limit) / h + 1)
    x_values = [x0 + i * h for i in range(n)]
    y_values = [y0]

    for i in range(1, n):
        temp_y = y_values[i - 1] + h * derivative(x_values[i - 1], y_values[i - 1]) / 2
        y_next = y_values[i - 1] + h * derivative(x_values[i - 1] + h / 2, temp_y)
        y_values.append(y_next)

    x_values = [round(x, 4) for x in x_values]
    y_values = [round(y, 4) for y in y_values]

    return x_values, y_values


def runge_kutt_4(derivative, x0, y0, h, bottom_limit, upper_limit):

    n = round((upper_limit - bottom_limit) / h + 1)
    x_values = [x0 + i * h for i in range(n)]
    y_values = [y0]

    for i in range(1, n):
        k0 = derivative(x_values[i - 1], y_values[i - 1])
        k1 = derivative(x_values[i - 1] + h / 2, y_values[i - 1] + h * k0 / 2)
        k2 = derivative(x_values[i - 1] + h / 2, y_values[i - 1] + h * k1 / 2)
        k3 = derivative(x_values[i - 1] + h, y_values[i - 1] + h * k2)
        y_next = y_values[i - 1] + h * (k0 + 2 * k1 + 2 * k2 + k3) / 6
        y_values.append(y_next)

    x_values = [round(x, 4) for x in x_values]
    y_values = [round(y, 4) for y in y_values]

    return x_values, y_values


x_0, y_0 = 1.8, 2.6
bottom_line, upper_limit = 1.8, 2.8
h = 0.1

exact_results = exact(derivative, x_0, y_0, h, bottom_line, upper_limit)[1]

methods = {
    "Exact result": exact,
    "Euler (obvious)": euler,
    "Euler-Cauchy": euler_cauchy,
    "Improved Euler": improved_euler,
    "Runge-Kutta": runge_kutt_4
}

df = pd.DataFrame({"Xk": [round(x_0 + i * h, 1) for i in range(11)]})

for method_name, method_func in methods.items():
    results = method_func(derivative, x_0, y_0, h, bottom_line, upper_limit)[1]
    errors = [round(exact - result, 4) for exact, result in zip(exact_results, results)]
    df[method_name] = results
    if method_name != "Exact result":
        df[method_name + " Error"] = errors

print(df.to_string(index=False))


# Графік
fig, ax = plt.subplots()

for method_name, method_func in methods.items():
    x_values, y_values = method_func(derivative, x_0, y_0, h, bottom_line, upper_limit)
    ax.plot(x_values, y_values, label=method_name, marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Порівняння однокрокових методів')
ax.legend()

plt.grid(True)
plt.show()
