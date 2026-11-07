


# Curso: SICI 4036 - Data Structures
# Laboratorio 1: Algoritmos de busqueda Secuencial y Binaria
# Estudiante: Guillermo Pacheco Cruz
# Descripcion: El programa compara algoritmos de busqueda secuencial y binaria.
# Modificaciones:
# a)Cambie los objetivos de búsqueda a (105, 225, 200). Determine el índice obtenido por cada algoritmo y compare
# cuántas inspecciones hizo cada uno.
# b)Reemplace los nueve códigos por list(range(0, 2048, 2)) y pruebe los objetivos (2046, 2047). Antes de ejecutar,
# prediga cuál método necesita menos comparaciones.
# c)Añada un comentario junto a la definición de codigos indicando expresamente la precondición de la búsqueda
# binaria.

"""Laboratorio 1: busqueda secuencial y binaria.
"""

def busqueda_lineal(datos, objetivo):
    """Devuelve (indice, comparaciones); -1 si no existe.
    """

    for i in range(len(datos)):
        if datos[i] == objetivo:

            return i, i + 1
            """
            Si el objetivo se encuentra en los datos
            devuelve una tupla con el indice y la cantidad de iteraciones,
            que al en este caso ser lineal, la canatidad de iteraciones seria
            el indice que ocupa en la lista, +1 para convertir la posicion 0 del
            en una iteracion
            """

    return -1, len(datos)
    """
    Si no encuentra el objetivo en los datos, devolvera -1 pq no es ningun indice
    y la cantidad  de elementos de la lista sera la cantidad de iteraciones realizadas.
    """

def busqueda_binaria(datos, objetivo):
    """Requiere datos ordenados ascendentemente.
    """
    izquierda, derecha = 0, len(datos) - 1
    comparaciones = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if datos[medio] == objetivo:

            return medio, comparaciones
            # devuelve el indice en donde se encuentra el objetivo y la cantidad de iteraciones.

        if objetivo < datos[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1, comparaciones
    # si no encuentra el objetivo, devuelve -1 en lugar de in indice y la cantidad de iteraciones.

def main():

    codigos = list(range(0, 2048, 2))
    """
    codigos representa la entrada que se le pasara a la funcion.
    PARA UNA BUSQUEDA BINARIA LA LISTA TIENE QUE ESTAR ORDENADA.
    """

    print("Codigos:", codigos)
    for objetivo in (2046, 2047):
        # para
        print("Objetivo:", objetivo)
        print(" Lineal:", busqueda_lineal(codigos, objetivo))
        print(" Binaria:", busqueda_binaria(codigos, objetivo))

if __name__ == "__main__":
    main()

"""
Analisis:

En una busqueda lineal, en el peor de los casos, el elemento buscado no se 
encuentra en la lista, y el algoritmo tiene que correr la lista completa para saberlo.

En una busqueda binaria O(log n) en el peor de los casos el algoritmo tiene que realizar 
el numero maximo de divisiones andes de darse cuenta que el elemento buscado no 
se encuentra en la lista.

De la lista no estar ordenada, la busqueda lineal funciona normalmente, pero la busqueda
binaria daria resultados incorrectos, ya que de para que su logica de descartar mitades
para hayar el objetivo, depende de que la lista este ordenada.

En las tuplas que devuelve el programa, el primer elemento representa la posicion en la 
que el objetivo se encuentra en la lista. Si devuelve -1, el objetivo no se encontro en
la lista. El segundo elemento de las tuplas en las salidas, representa la cantidad de
iteraciones realizadas para dar con el objetivo.
"""