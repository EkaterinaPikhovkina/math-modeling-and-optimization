import numpy as np
import matplotlib.pyplot as plt


def polynomial_interpolation(x_values, y_values):
    n = len(x_values)
    polynomial = np.poly1d(0)  # Початкове значення поліному
    for i in range(n):
        term = np.poly1d(y_values[i])  # Створення базового поліному для поточної точки
        for j in range(n):
            if j != i:
                term *= np.poly1d([1, -x_values[j]]) / (x_values[i] - x_values[j])
        polynomial += term  # Додавання базового поліному до загального поліному
    return polynomial


x_data = np.array([-2, -1, 0, 3])
y_data = np.array([-4, 3, 2, 11])

# Інтерполяція поліномом Лагранжа
interpolated_polynomial = polynomial_interpolation(x_data, y_data)
print(f"Формула многочлена Лагранжа:\n{interpolated_polynomial}\n")

# Обчислення значень поліному Лагранжа для певних точок
x_points = np.array([-1.5, -0.5, 1, 2])
y_points = interpolated_polynomial(x_points)
print("Обчислені значення многочлена в заданих точках:")
for x in x_points:
    print(f"x = {x}, L(x) = {np.round(interpolated_polynomial(x), decimals=10)}")

# Графік
x_plot = np.linspace(-5, 5)
y_plot = interpolated_polynomial(x_plot)

plt.plot(x_points, y_points, 'o', x_plot, y_plot)
plt.plot(x_points, y_points, marker='o', markersize=8, linestyle='None')

plt.title('Графік поліному Лагранжа', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('f(x)', fontsize=14)

plt.show()
