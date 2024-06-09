import numpy as np
import time


def f(x):
    return 4 / (1 + x**2)


def riemann_integration(f, a, b, N):
    dx = (b - a) / N
    total = 0
    for i in range(N):
        total += f(a + i * dx) * dx
    return total


def rms_error(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


pi_reference = 3.14159265358979323846


N_values = [10, 100, 1000, 10000]


results = []


for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integration(f, 0, 1, N)
    end_time = time.time()
    execution_time = end_time - start_time
    error = rms_error(np.array([pi_reference]), np.array([pi_approx]))
    results.append((N, pi_approx, error, execution_time))


for result in results:
    N, pi_approx, error, execution_time = result
    print(f"N = {N}")
    print(f"Approximated pi: {pi_approx}")
    print(f"RMS error: {error}")
    print(f"Execution time: {execution_time} seconds")
    print()

