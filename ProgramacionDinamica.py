import time
import matplotlib.pyplot as plt
import numpy as np

def tiling_problem(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

with open("entradas.txt", "r") as file:
    entradas = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]

tiempos = []
valores_n = []

for n in entradas:
    inicio = time.time()
    resultado = tiling_problem(n)
    fin = time.time()
    
    duracion = fin - inicio
    tiempos.append(duracion)
    valores_n.append(n)

    print(f"n = {n}, formas = {resultado}, tiempo = {duracion:.6f} segundos")

coef = np.polyfit(valores_n, tiempos, deg=1)
linea_ajustada = np.poly1d(coef)

plt.figure(figsize=(10, 6))
plt.plot(valores_n, tiempos, marker='o', label='Tiempos reales')
plt.plot(valores_n, linea_ajustada(valores_n), color='red', linestyle='--', label=f'Regresión lineal: y = {coef[0]:.2e}x + {coef[1]:.2e}')
plt.title("Tiempos de ejecución vs Tamaño del tablero (n)")
plt.xlabel("n (tamaño del tablero 2xn)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
