def selection_sort(arr):
    """
    Implementación del algoritmo Selection Sort
    
    Funcionamiento:
    - Encuentra repetidamente el elemento mínimo en la parte no ordenada
    - Lo intercambia con el elemento en la posición actual
    
    Args:
        arr: Lista de elementos a ordenar
        
    Returns:
        Lista ordenada
    """
    n = len(arr)
    
    for i in range(n):
        # Encontrar el índice del mínimo en el subarreglo no ordenado
        min_idx = i
        # for i + 1 es el primer elemento no ordenado
        # for j = i + 1; arr[j] = 25
        for j in range(i + 1, n):
            # [64, 25, 12]
            # [25, 64, 12]
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Intercambiar el mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

if __name__ == "__main__":
    print("\nEjemplos para entrevista:")
    test_array = [64, 25, 12, 22, 11]
    print(selection_sort(test_array))
    print(f"Original: {test_array}")