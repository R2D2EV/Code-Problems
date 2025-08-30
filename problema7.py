# 4. Perfect X – Matrix Pattern Recognition
# Ejercicio: Dada una matriz cuadrada de 1s y 0s, encuentra las coordenadas centrales de todas las “X perfectas”. 
# Una “X perfecta” tiene 1s en
# ambas diagonales que se cruzan en el centro, y 0s en las demás posiciones de la submatriz 3x3.


# Input:
# [
#  [0, 1],
#  [1, 1],
# ]

# Input:
# [
#  [0, 1, 0],
#  [1, 1, 1],
#  [0, 1, 0]
# ]
# 3 X 3    1 1  3 - 2

# Input:
# [
#  [0, 0, 1, 0, 0],
#  [0, 0, 1, 0, 0],
#  [1, 1, 1, 1, 1],
#  [0, 0, 1, 0, 0],
#  [0, 0, 1, 0, 0],
# 5 X 5    2 2  5 - 3

# Input:
# [
#  [0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0],
#  [1, 1, 1, 1, 1, 1, 1],
#  [0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0],
# ]
# 7 X 7   3 3  7 - 4

# Output: [(1, 1)]  # Centro de la X

import math

def perfect_x(matrix):
    rows_m = len(matrix)
    cols_m = len(matrix[0])
    if rows_m != cols_m or rows_m % 2 == 0:
        return "No es posible con matrices no cuadadras y/o matrices cuadradas  no impares"
    coor1 = rows_m - math.ceil(rows_m / 2)
    return (coor1, coor1)
matrix = [
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [1, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
]

print(perfect_x(matrix))
    




