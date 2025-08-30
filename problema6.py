# 3. Cyclical T-Shifts – Array Transformation
# Ejercicio: Dado dos arreglos de igual longitud, crea un nuevo arreglo donde cada
# elemento es la suma del elemento actual del primer arreglo y el elemento del segundo arreglo desplazado cíclicamente a la derecha por 1 posición.


def cyclic_array(arr):
    ShiftedB = []
    i = 1
    while i < len(arr):
        if i == 1:
            ShiftedB.append(arr[i - 2 + len(arr)])
        ShiftedB.append(arr[i - 1])
        i += 1
    return ShiftedB

def array_sum(arr1, arr2):
    array_sum = []
    shift_array = cyclic_array(arr2)
    for i in range(len(arr1)):
        array_sum.append(arr1[i] + shift_array[i])

    return print(f"Sum of the two arrays: {array_sum}")

A = [1, 2, 3]
B = [4, 5, 6]  # Shifted B = [6, 4, 5]

array_sum(A, B)

    
# A = [1, 2, 3]
# B = [4, 5, 6]  # Shifted B = [6, 4, 5]
# Output: [1+6, 2+4, 3+5] = [7, 6, 8]
