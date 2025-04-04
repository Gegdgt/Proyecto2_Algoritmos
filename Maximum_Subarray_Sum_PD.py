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

if __name__ == "__main__":
    nombre_archivo = 'entradas.txt'
    entradas = leer_entradas(nombre_archivo)

    for i, arreglo in enumerate(entradas, start=1):
        resultado = maximum_subarray_sum(arreglo)
        print(f"Caso {i}: Máxima suma de subarreglo = {resultado}")
