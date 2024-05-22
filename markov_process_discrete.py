import numpy as np

# Задані перехідні імовірності
transition_probabilities = {
    (1, 2): 0.3, (1, 3): 0.2, (1, 4): 0.15, (1, 5): 0.1,
    (2, 3): 0.35, (2, 4): 0.2, (2, 5): 0.15,
    (3, 4): 0.35, (3, 5): 0.15,
    (4, 5): 0.5
}

# Складання матриці переходів
num_states = 5
transition_matrix = np.zeros((num_states, num_states))

for i in range(num_states):
    for j in range(num_states):
        if (i + 1, j + 1) in transition_probabilities:
            transition_matrix[i, j] = transition_probabilities[(i + 1, j + 1)]
        elif i == j:
            sum_except_diagonal = sum(transition_probabilities.get((i + 1, k + 1), 0) for k in range(num_states) if k != i)
            transition_matrix[i, j] = 1 - sum_except_diagonal

# Визначення початкових імовірностей перебування системи в станах
initial_probabilities = np.array([1, 0, 0, 0, 0])

# Виведення матриці переходів
print("Матриця перехідних імовірностей:")
print(transition_matrix)

# Виведення початкових імовірностей станів у зазначеному форматі
print("\nПочаткові імовірності станів:")
for i, p in enumerate(initial_probabilities):
    print(f"p{i + 1}(0)={p};", end="\n")

# Розрахунок імовірностей після кожного кроку
current_probabilities = initial_probabilities
for i in range(5):
    current_probabilities = np.dot(current_probabilities, transition_matrix)
    print(f"\nІмовірності після {i + 1}-го кроку:")
    for j, p in enumerate(current_probabilities):
        print(f"p{j + 1}({i + 1})={p:.4f};", end="\n")

# Перевірка результатів після 5-го тесту за формулою p(5) = p(0) * P^5
prob = np.dot(initial_probabilities, np.linalg.matrix_power(transition_matrix, num_states))
print("\nПеревірка результатів після 5-го тесту за формулою p(5) = p(0) * P^5:")
for j, p in enumerate(prob):
    print(f"p{j + 1}(5)={p:.4f};", end="\n")
