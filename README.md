## Gabriel García - 21352
## Sebas Juárez - 21471

# Proyecto ADA - Maximum Subarray Sum

Este proyecto resuelve el problema clásico de encontrar la **suma máxima de un subarreglo contiguo** dentro de un arreglo de enteros, utilizando dos enfoques distintos de diseño de algoritmos:

1. Divide and Conquer
2. Programación Dinámica

---

## Descripción del problema

Dado un arreglo de enteros (positivos, negativos o ceros), el objetivo es encontrar el subarreglo contiguo que tenga la **suma total más alta posible**.

### Entrada
Un archivo `.txt` llamado `entradas.txt`, donde cada línea contiene un arreglo separado por comas:

-2,1,-3,4,-1,2,1,-5,4 4,1,5,-4,-7,6,4,-3,2


### Salida esperada
Para cada arreglo del archivo, se imprime:

- La suma máxima del subarreglo contiguo
- El subarreglo que produce dicha suma
- Los índices de inicio y fin dentro del arreglo original

Ejemplo:

Maximum Subarray Sum del array 1 es: 6 Subarreglo: [4, -1, 2, 1] (índices 3 a 6)
Maximum Subarray Sum del array 2 es: 11 Subarreglo: [6, 4, -3, 2] (índices 5 a 8)


---

## Implementación con Divide and Conquer

Archivo: `Maximum_Subarray_Sum_DaC.py`

Este enfoque sigue la estrategia de:

- **Dividir:** el arreglo en mitades
- **Conquistar:** resolver recursivamente cada mitad
- **Combinar:** calcular la suma máxima que cruza el centro y elegir la mejor de las tres

  Se ve principalmente en la Función: max_subarray_sum_dac(arr, left, right)

### Complejidad:
- Tiempo: **O(n log n)**
- Espacio: **O(log n)** por llamadas recursivas

