import time
import matplotlib.pyplot as plt

def maximum_subarray_sum(arr):
    if not arr:
        return 0

    max_actual = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_actual = max(arr[i], max_actual + arr[i])
        max_global = max(max_global, max_actual)

    return max_global

def leer_entradas(archivo):
    casos = []
    with open(archivo, 'r') as file:
        for linea in file:
            numeros = [int(num.strip()) for num in linea.strip().split(',')]
            casos.append(numeros)
    return casos

def generar_grafica_rendimiento(entradas):
    tamaños = []
    tiempos = []

    for entrada in entradas:
        n = len(entrada)
        inicio = time.time()
        maximum_subarray_sum(entrada)
        fin = time.time()
        tamaños.append(n)
        tiempos.append((fin - inicio) * 1000)  # Tiempo en milisegundos

    # Graficar y guardar
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos, marker='o', color='orange')
    plt.title('Tiempo de ejecución de Maximum Subarray Sum (Programación Dinámica)')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (ms)')
    plt.grid(True)
    # plt.ylim(0, 0.5)  # Por ejemplo, hasta 0.05 ms
    plt.tight_layout()
    plt.savefig('grafica_pd.png')
    print("Gráfica guardada como 'grafica_pd.png'.")

if __name__ == "__main__":
    nombre_archivo = 'entradas.txt'
    entradas = leer_entradas(nombre_archivo)

    for i, arreglo in enumerate(entradas, start=1):
        inicio = time.time()
        resultado = maximum_subarray_sum(arreglo)
        fin = time.time()
        tiempo_ms = (fin - inicio) * 1000  # Convertir a milisegundos
        print(f"Caso {i}: Máxima suma de subarreglo = {resultado} | Tiempo = {tiempo_ms:.5f} ms")

    # Generar la gráfica de rendimiento basada en las entradas reales
    generar_grafica_rendimiento(entradas)
