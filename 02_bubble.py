


"""
Curso: SICI 4036 - Data Structures
Laboratorio 2: Algoritmo de Ordenamiento "Bubble Sort"
Estudiante: Guillermo Pacheco Cruz
Descripcion: El programa utiliza un algoritmo de Bubble Sort para
                organizar latencias en una red.
Modificaciones:Modifique main() para ejecutar dos pruebas adicionales:
                [12, 19, 22, 38, 45] (ordenada) y [45, 38, 22, 19, 12] (orden inverso).
                Etiquete la salida como mejor caso y peor caso. Para cinco datos, la primera
                prueba debe hacer 4 comparaciones y 0 intercambios;
                la segunda, 10 comparaciones y 10 intercambios.
"""

# Laboratorio 2: Bubble Sort con parada temprana.

def bubble_sort(valores):
    # Ordena una copia; devuelve (lista, comparaciones, cambios).
    datos = valores.copy()
    comparaciones = cambios = 0

    for pasada in range(len(datos) - 1):
        hubo_cambio = False

        for j in range(len(datos) - 1 - pasada):
            comparaciones += 1
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                cambios += 1
                hubo_cambio = True

        if not hubo_cambio:
            break

    return datos, comparaciones, cambios

def main():
    latencias = [38, 12, 45, 22, 19]
    print("Original:", latencias)
    # Entrega lista original.
    print("Ordenado, comparaciones, cambios:", bubble_sort(latencias))
    # Entregara una lista con 3 elementos. La lista ordenada, la cantidad
    # de coomparaciones y cantidad de intercambios realizados.
    print("Original sin cambios:", latencias)
    # Entrega lista ordenada.

    print("\n SEGUNDA PRUEBA \n ")

    latencias = [ 12, 19, 22, 38, 45] # Ordenada
    print("Original:", latencias)
    # Entrega lista original.
    print("Ordenado, comparaciones, cambios:", bubble_sort(latencias))
    # Entregara una lista con 3 elementos. La lista ordenada, la cantidad
    # de coomparaciones y cantidad de intercambios realizados.
    print("Original sin cambios:", latencias)
    # Entrega lista ordenada.


    print("\n TERCERA PRUEBA \n ")

    latencias = [45, 38, 22, 19, 12]  # Orden Inverso
    print("Original:", latencias)
    # Entrega lista original.
    print("Ordenado, comparaciones, cambios:", bubble_sort(latencias))
    # Entregara una lista con 3 elementos. La lista ordenada, la cantidad
    # de coomparaciones y cantidad de intercambios realizados.
    print("Original sin cambios:", latencias)
    # Entrega lista ordenada.

if __name__ == "__main__":
    main()

"""
Analisis:

La bandera de control hubo_cambio, permite en el mejor de los casos detectar en la primera,
iteracion si una lista esta ordenada. Esto optimiza el costo computacional requerido. 

Mediante la suma "4 +3 +2 +1" que es la progresion aritmetica de la suma de comparaciones,
por iteracion, de las pruebas realizadas; en las cuales n = 5. La ecuacion general para la 
progresion aritmetica de la suma de comparaciones por iteracion en el peor de los casos 
es: (n-1) + (n-2) + ... + (+1). Lo que equivale a n(n-1)/2, que mantiene una tendencia 
de crecimiento de orden cuadratico O(n^2). 

Las tres listas terminan igualmente ordenadas aunque se realize distinta cantidad de trabajo
porque el algoritmo de Bubble Sort esta diseñado para garantizar que el resultado final siempre
sea una lista ordenada.


"""