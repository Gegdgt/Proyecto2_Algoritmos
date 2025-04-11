# Reimportar dependencias y volver a ejecutar todo desde cero
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Esta función es la implementación recursiva del Tiling Problem usando Divide and Conquer
def tiling_dac(n):
    if n == 0 or n == 1:
        return 1
    return tiling_dac(n - 1) + tiling_dac(n - 2)

# Esta función genera manualmente entradas del 1 al 30 (simulando "entradas.txt")
def leer_entradas():
    return list(range(1, 31))

# Esta función mide el tiempo de ejecución para cada valor de entrada
def medir_tiempos(entradas):
    tiempos = []
    for n in entradas:
        inicio = time.time()
        tiling_dac(n)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

# Esta función grafica los tiempos reales y las regresiones lineal y exponencial
def graficar_resultados(entradas, tiempos):
    X = np.array(entradas).reshape(-1, 1)
    y = np.array(tiempos)

    # Ajuste de regresión exponencial (y = a * exp(b * x))
    log_y = np.log(y + 1e-9)  # Se suma un valor pequeño para evitar log(0)
    modelo_exp = LinearRegression()
    modelo_exp.fit(X, log_y)
    y_pred_exp = np.exp(modelo_exp.predict(X))

    # Se grafican los resultados
    plt.figure(figsize=(10, 6))
    plt.plot(entradas, tiempos, label="Tiempo real (DaC)", marker='o')
    plt.plot(entradas, y_pred_exp, label="Regresión exponencial", linestyle="-.")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiling Problem con Divide and Conquer (sin memo)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Ejecutar flujo completo
entradas = leer_entradas()
tiempos = medir_tiempos(entradas)
graficar_resultados(entradas, tiempos)
