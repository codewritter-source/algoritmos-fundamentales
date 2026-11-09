


"""
Curso: SICI 4036 - Data Structures
Laboratorio 3: Algoritmo de Ordenamiento "Selection Sort"
Estudiante: Guillermo Pacheco Cruz
Descripcion: El programa utiliza un algoritmo de Bubble Sort para organizar solicitudes
    segun la escala de prioridad; donde el valor 1 tiene la prioridad mas alta.
Modificaciones: Agregue a main() una tercera prueba con [5, 4, 3, 2, 1] y una cuarta con [2, 2, 1, 1, 3].
    Etiquete cada caso y confirme que los duplicados se conservan. Imprima junto a los resultados una
    descripción de lo que mide cada contador.
"""


def selection_sort(valores):
    # Ordena una copia; devuelve (lista, comparaciones, cambios).

    datos = valores.copy()
    comparaciones = cambios = 0 # iniciacion de contadores

    for i in range(len(datos) - 1):
        minimo = i
        for j in range(i + 1, len(datos)): # AQUI SE OCACIONA LA COMPLEJIDAD DE ORDEN CUADRATICO
            comparaciones += 1 # Contador de comparaciones realizadas

            if datos[j] < datos[minimo]: # compara datos
                minimo = j

        if minimo != i:
            datos[i], datos[minimo] = datos[minimo], datos[i] # hace intercambio
            cambios += 1 # Contador de cambios realizados

    return datos, comparaciones, cambios


def main():
    prioridades = [4, 1, 3, 5, 2]

    print("PRIMERA PRUEBA \n")
    print("Original:", prioridades)
    print("Ordenado, comparaciones, cambios:", selection_sort(prioridades))

    print("\n SEGUNDA PRUEBA \n")
    print("Ya ordenados:", selection_sort([1, 2, 3, 4, 5]))

    # Modificacione

    tercera = [5, 4, 3, 2, 1]
    cuarta = [2, 2, 1, 1, 3]

    print("\n TERCERA PRUEBA \n")
    print("Original:", tercera)
    print("Ya ordenado, comparaciones y cambios:", selection_sort(tercera))

    print("\n CUARTA PRUEBA \n")
    print("Original:", cuarta)
    print("Ya ordenado, comparaciones y cambios:", selection_sort(cuarta))

if __name__ == "__main__":
    main()


"""
ANALISIS:

La formula n(n-1)/2 representa la suma de las comparaciones por iteracion realizadas por los 
ciclos anidados y Selection Sort mantiene un orden cuadratico O(n^2) incluso en el mejor de los casos
porque a diferencia del Bubble Sort Optimizado con una bandera booleana de control para poder 
detectar orden previo y detenerse. Por esta razon la complejidad temporal se mantiene en
orden cuadratico; incluso en el mejor de los casos.

Hay menos intercambios que comparaciones porque no en todas las iteraciones se realizan cmbios. 
Un intercambio se realiza cuando es necesario, evitanto modificaciones innecesarias y costos computacionales.

Un algoritmo de ordenamiento es estable si preserva el orden relativo de los elementos que se repiten. En Selection
Sort esto no se garantiza debido a la dorma en la que el algoritmo opera; haciendo intercambios saltandose posiciones
se podria alterar el orden relativo original de los elementos repetidos.
"""
