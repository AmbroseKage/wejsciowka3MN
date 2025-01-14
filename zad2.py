import numpy as np

coefficients = [320, -344, 126, -19, 1]

roots = np.roots(coefficients)

rounded_roots = np.round(roots, 3)

sorted_roots = np.sort(rounded_roots)

print(sorted_roots)
