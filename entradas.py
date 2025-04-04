import random

def generar_entradas(nombre_archivo, cantidad=30, tam_inicial=500, tam_incremento=200):
    with open(nombre_archivo, 'w') as archivo:
        for i in range(cantidad):
            tam = tam_inicial + i * tam_incremento

            # Patrón 1: Muchos negativos seguidos de picos positivos
            arreglo = []
            for _ in range(tam):
                if random.random() < 0.8:
                    arreglo.append(random.randint(-100, -1))  # Negativos frecuentes
                else:
                    arreglo.append(random.randint(50, 150))   # Picos positivos

            # Aleatorizar ligeramente sin romper el patrón
            random.shuffle(arreglo)

            linea = ','.join(map(str, arreglo))
            archivo.write(linea + '\n')

generar_entradas("entradas.txt")
