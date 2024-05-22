import numpy as np


A = np.array([[3, 20, -2, 0],
              [5, -4, 0, 20],
              [0, 5, 32, -3],
              [12, 0, 0, 3]])

b = np.array([41, -19, 34, 29])

accuracy = 0.0001
iterations = 1000
x0 = np.zeros(4)


def generate_equations(matrix1, matrix2):
    equations = []
    for i in range(len(matrix1)):
        equation = ' + '.join([f'{matrix1[i][j]}x_{j+1}' for j in range(len(matrix1[i]))])
        equation += f' = {matrix2[i]}'
        equations.append(equation)
    return equations


def rearrange_matrices(matrix1, matrix2):
    new_matrix1 = []
    new_matrix2 = []

    for col in range(matrix1.shape[1]):
        max_row = np.argmax(np.abs(matrix1[:, col]))

        new_matrix1.append(matrix1[max_row])
        new_matrix2.append(matrix2[max_row])

        matrix1 = np.delete(matrix1, max_row, axis=0)
        matrix2 = np.delete(matrix2, max_row, axis=0)

    return np.array(new_matrix1), new_matrix2


def gauss_seidel(itr, acr, matrix1, matrix2, x_0):
    n = len(matrix1)
    x_i = np.zeros(n)

    for k in range(itr):

        x_i = np.zeros(n)
        for i in range(n):
            s1 = np.dot(matrix1[i, :i], x_i[:i])
            s2 = np.dot(matrix1[i, i + 1:], x_0[i + 1:])
            x_i[i] = 1 / matrix1[i][i] * (matrix2[i] - s1 - s2)

        print(f"Ітерація: {k}\n"
              f"Наближені значення:")
        for i in range(n):
            print(f"x{i+1} = {x_i[i]:.10f}")
        print(f"Похибка: {np.linalg.norm(x_i - x_0):.10f}\n")

        if np.linalg.norm(x_i - x_0) < acr:
            break

        x_0 = x_i

    return x_i


print("Система рівнянь:")
equations = generate_equations(A, b)
for equation in equations:
    print(equation)
print("\n")

A_new, b_new = rearrange_matrices(A, b)
solution = gauss_seidel(iterations, accuracy, A_new, b_new, x0)

print("Розв'язок системи:")
for i, sol in enumerate(solution, start=1):
    print(f"x{i} = {sol:.10f}")
