def generar_entradas_tiling(nombre_archivo, cantidad=30, max_n=30):
    with open(nombre_archivo, 'w') as archivo:
        for n in range(1, min(cantidad + 1, max_n + 1)):
            archivo.write(f"{n}\n")

# Genera el archivo entradas.txt con valores de 1 a 30
generar_entradas_tiling("entradas.txt")
