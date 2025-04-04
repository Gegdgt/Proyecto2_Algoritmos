import random

def generar_entradas(nombre_archivo, cantidad=30, tam_inicial=10, tam_incremento=10):
    with open(nombre_archivo, 'w') as archivo:
        for i in range(cantidad):
            tam = tam_inicial + i * tam_incremento
            arreglo = [random.randint(-50, 50) for _ in range(tam)]
            linea = ','.join(map(str, arreglo))
            archivo.write(linea + '\n')

generar_entradas("entradas.txt")
