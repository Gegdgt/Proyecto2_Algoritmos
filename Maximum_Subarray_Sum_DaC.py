import time
import matplotlib.pyplot as plt

def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    current_sum = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right_sum = float('-inf')
    current_sum = 0
    max_right = mid + 1
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i

    return left_sum + right_sum, max_left, max_right

def max_subarray_sum_dac(arr, left, right):
    if left == right:
        return arr[left], left, right

    mid = (left + right) // 2

    left_max, left_start, left_end = max_subarray_sum_dac(arr, left, mid)
    right_max, right_start, right_end = max_subarray_sum_dac(arr, mid + 1, right)
    cross_max, cross_start, cross_end = max_crossing_sum(arr, left, mid, right)

    if left_max >= right_max and left_max >= cross_max:
        return left_max, left_start, left_end
    elif right_max >= left_max and right_max >= cross_max:
        return right_max, right_start, right_end
    else:
        return cross_max, cross_start, cross_end

def find_max_subarray(arr):
    if not arr:
        return 0, [], (0, 0)
    max_sum, start, end = max_subarray_sum_dac(arr, 0, len(arr) - 1)
    return max_sum, arr[start:end + 1], (start, end)

def procesar_archivo_con_tiempos(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    tiempos = []
    tamanos = []

    for i, linea in enumerate(lineas):
        linea = linea.strip()
        if not linea:
            continue
        arreglo = list(map(int, linea.split(',')))
        inicio_tiempo = time.perf_counter()
        suma, subarreglo, (inicio, fin) = find_max_subarray(arreglo)
        fin_tiempo = time.perf_counter()
        duracion = fin_tiempo - inicio_tiempo

        tiempos.append(duracion)
        tamanos.append(len(arreglo))

        print(f"Array {i+1} - Tamaño: {len(arreglo)}")
        print(f"Suma máxima: {suma}")
        print(f"Subarreglo: {subarreglo} (índices {inicio} a {fin})")
        print(f"Tiempo de ejecución: {duracion:.6f} segundos")
        print()

    return tamanos, tiempos

def graficar_resultados(tamanos, tiempos, titulo):
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos, marker='o')
    plt.title(titulo)
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.savefig("grafica_dac.png")
    plt.show()

# Llamada principal
tamanos, tiempos = procesar_archivo_con_tiempos("entradas.txt")
graficar_resultados(tamanos, tiempos, "Tiempo de ejecución - Divide and Conquer (Maximum Subarray Sum)")
