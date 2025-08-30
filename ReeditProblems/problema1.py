# CHECKED
# Enunciado:

# Dado un arreglo de números enteros llamado arr, tu tarea es encontrar y devolver todos los elementos del arreglo que sean estrictamente mayores que sus vecinos inmediatos.

# Un número es considerado mayor que sus vecinos si:
# Es mayor que el número anterior y
# Es mayor que el número siguiente.
# Reglas especiales:

# El primer y el último elemento del arreglo tienen solo un vecino, por lo que no se consideran para esta comparación.
# input: arr = [1, 3, 2, 4, 5, 3, 6, 2]
# output: [3, 5, 6]

arr = [1, 3, 2, 4, 5, 3, 6, 2]


def problema1(arr):
    arr_index = 1
    arr_len = len(arr) - 1
    lista2 = []
    while arr_index < arr_len:
        if arr[arr_index] > arr[arr_index - 1] and arr[arr_index] > arr[arr_index + 1]:
            lista2.append(arr[arr_index])
        arr_index += 1
    print(lista2)

if __name__ == "__main__":
    try:
        problema1(arr)
    except Exception as e:
        print(e)