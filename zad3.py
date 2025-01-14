import numpy as np

def bisection_method(f, a, b, epsilon, max_iterations):
    if f(a) * f(b) >= 0:
        print("Funkcja nie zmienia znaku w podanym przedziale.")
        return None

    iteration = 0
    while iteration < max_iterations:
        c = (a + b) / 2  # Środek przedziału
        fc = f(c)

        print(f"Iteracja {iteration + 1}: c = {c:.6f}, f(c) = {fc:.6f}")

        # Sprawdzenie, czy znaleziono przybliżone miejsce zerowe
        if abs(fc) < epsilon or (b - a) / 2 < epsilon:
            return round(c, 3)

        # Zawężenie przedziału
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iteration += 1

    # Jeśli nie osiągnięto wymaganego epsilon, zwracamy ostatnie c
    return round(c, 3)

# Definicja funkcji
def func(x):
    return np.sin(x - 1) + np.exp(-(x - 3)**2)

# Parametry
A, B = 10, 14
epsilon = 0.087
max_iterations = 10

# Wywołanie metody bisekcji
root = bisection_method(func, A, B, epsilon, max_iterations)
if root is not None:
    print(f"Miejsce zerowe funkcji: x = {root:.3f}")
else:
    print("None")
