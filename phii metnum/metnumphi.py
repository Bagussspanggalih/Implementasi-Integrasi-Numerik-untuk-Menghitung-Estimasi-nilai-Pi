import time
import numpy as np
import matplotlib.pyplot as plt

def riemann_integration(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        total += f(a + i * dx) * dx
    return total

def f(x):
    return 4 / (1 + x**2)

pi_reference = 3.14159265358979323846
N_values = [10, 100, 1000, 10000]
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integration(f, 0, 1, N)
    execution_time = time.time() - start_time
    rms_error = np.sqrt((pi_approx - pi_reference)**2)
    results.append((N, pi_approx, rms_error, execution_time))

N_list, pi_list, error_list, time_list = zip(*results)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(N_list, error_list, marker='o')
plt.xscale('log')
plt.xlabel('N (skala log)')
plt.ylabel('Galat RMS')
plt.title('Galat RMS terhadap N')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(N_list, time_list, marker='o', color='r')
plt.xscale('log')
plt.xlabel('N (skala log)')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Waktu Eksekusi terhadap N')
plt.grid(True)

plt.tight_layout()
plt.show()

print("Hasil Perhitungan:")
print("N\tPi Approx\tRMS Error\tExecution Time (seconds)")
for N, pi_approx, rms_error, execution_time in results:
    print(f"{N}\t{pi_approx}\t{rms_error}\t{execution_time:.6f}")
