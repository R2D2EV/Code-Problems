# Complejidad temporal: O(n²) - en el peor y caso promedio, O(n) en el mejor caso
# Complejidad espacial: O(1) - ordenamiento in-place
def insertion_sort(arr):
    """
    Implementación del algoritmo Insertion Sort
    
    Funcionamiento:
    - Divide la lista en una parte ordenada y otra no ordenada
    - Toma elementos de la parte no ordenada y los coloca en su posición correcta
      dentro de la parte ordenada
    
    Args:
        arr: Lista de elementos a ordenar
        
    Returns:
        Lista ordenada
    """
    # Comenzamos desde el segundo elemento
    for i in range(1, len(arr)):
        # Elemento actual a insertar en la parte ordenada
        key = arr[i]
        
        # Mover elementos mayores que key una posición adelante
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insertar el elemento en su posición correcta
        arr[j + 1] = key
        
    return arr