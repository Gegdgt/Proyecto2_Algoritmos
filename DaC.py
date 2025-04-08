import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Función recursiva (Divide and Conquer)
def tiling_dac(n):
    if n == 0 or n == 1:
        return 1
    return tiling_dac(n - 1) + tiling_dac(n - 2)

# Leer entradas desde el archivo
def leer_entradas(archivo):
    with open(archivo, "r") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]

# Medir tiempos de ejecución
def medir_tiempos(entradas):
    tiempos = []
    for n in entradas:
        inicio = time.time()
        tiling_dac(n)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

# Graficar tiempos y regresión lineal
def graficar_resultados(entradas, tiempos):
    X = np.array(entradas).reshape(-1, 1)
    y = np.array(tiempos)

    modelo = LinearRegression()
    modelo.fit(X, y)
    y_pred = modelo.predict(X)

    plt.figure(figsize=(10, 6))
    plt.plot(entradas, tiempos, label="Tiempo real (DaC)", marker='o')
    plt.plot(entradas, y_pred, label="Regresión lineal", linestyle="--")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiling Problem con Divide and Conquer (sin memo)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


archivo = "entradas.txt"
entradas = leer_entradas(archivo)
tiempos = medir_tiempos(entradas)
graficar_resultados(entradas, tiempos)
