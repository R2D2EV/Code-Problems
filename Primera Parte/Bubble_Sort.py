def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # se empieza en i=0 y se va incrementando
        # si no hubo intercambios, la lista ya está ordenada
        intercambio = False
        print("este es el indice i range(n): " + str(i))
        print(arr)
        
        # Última i posiciones ya están ordenadas
        for j in range(0, n - i - 1):
            print("este es el indice j range(0, n - i - 1): " + str(j))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
                print(intercambio)
                print("lista dentro del bucle for j: ")
                print(arr)

        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not intercambio:
            break
            
    return arr

if __name__ == "__main__":
    # Ejemplo de uso
    lista = [5, 4, 3]
    print("Lista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)