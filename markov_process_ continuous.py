def generate_equations(matrix1, matrix2):
    equations = []
    for i in range(len(matrix1)):
        equation = ' + '.join([f'{matrix1[i][j]}p_{j+1}' for j in range(len(matrix1[i]))])
        equation += f' = {matrix2[i]}'
        equations.append(equation)
    return equations


def determinant(matrix):
    # Якщо матриця є 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        det += (-1) ** i * matrix[0][i] * determinant(sub_matrix)
    return det


def solve_system(coefficients, constants):
    n = len(coefficients)
    det_A = determinant(coefficients)

    # Перевірка на виродженість системи
    if det_A == 0:
        return None  # Система не має єдиного розв'язку

    solutions = []
    for i in range(n):
        # Створюємо копію матриці коефіцієнтів та замінюємо i-тий стовпчик на стовпчик вільних членів
        matrix_copy = [row[:] for row in coefficients]
        for j in range(n):
            matrix_copy[j][i] = constants[j]

        # Знаходимо детермінант заміщеної матриці та обчислюємо розв'язок
        det_i = determinant(matrix_copy)
        solutions.append(det_i / det_A)

    return solutions


coefficients = [
    [-3.2, 1.8, 1.2, 0.4],
    [2.2, -1.81, 0, 0.05],
    [1, 0, -1.22, 0.05],
    [1, 1, 1, 1]
]
constants = [0, 0, 0, 1]


print("Система лінійних алгебраїчних рівнянь:")
equations = generate_equations(coefficients, constants)
for equation in equations:
    print(equation)
print("\n")

solutions = solve_system(coefficients, constants)
if solutions is None:
    print("Система не має єдиного розв'язку.")
else:
    print("Розв'язки системи:")
    for i, solution in enumerate(solutions, start=1):
        print(f"p_{i} = {solution}")
