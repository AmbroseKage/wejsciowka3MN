import numpy as np

# Funkcja, jej pierwsza i druga pochodna
def f(x):
    return np.cos(np.exp(x / 5))

def f_prime(x):
    return -(np.exp(x / 5) * np.sin(np.exp(x / 5))) / 5

def f_double_prime(x):
    return -(np.exp(x / 5) * (np.sin(np.exp(x / 5)) + np.exp(x / 5) * np.cos(np.exp(x / 5)))) / 25

# Parametry metody Newtona
x0 = 33  # Punkt początkowy
epsilon = 0.026
max_iterations = 10

# Algorytm Newtona z uwzględnieniem pochodnych
def newton_method(f, f_prime, f_double_prime, x0, epsilon, max_iterations):
    x = x0
    for iteration in range(max_iterations):
        f_x = f(x)
        f_prime_x = f_prime(x)

        # Sprawdzanie warunku zbieżności (pochodna bliska zeru)
        if abs(f_prime_x) < epsilon:
            print("Pochodna bliska zeru, metoda Newtona nie zbiega.")
            return None

        # Obliczanie kolejnego przybliżenia
        x_new = x - f_x / f_prime_x
        print(f"Iteracja {iteration + 1}: x = {x_new}, f(x) = {f(x_new)}")

        # Sprawdzanie warunku zbieżności
        if abs(x_new - x) < epsilon:
            return round(x_new, 3)

        x = x_new

    return round(x, 3)  # Zwracamy wynik po maksymalnej liczbie iteracji

# Obliczenie miejsca zerowego
result = newton_method(f, f_prime, f_double_prime, x0, epsilon, max_iterations)
print(f"Miejsce zerowe: {result}")
