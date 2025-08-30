# Multiply 2 matrices

matrix1 = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 1]  
    ]

matrix2 = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],  
        [0, 5, 0, 0],
        [0, 5, 0, 0],
    ] 

def multiply2matrices(matrix1, matrix2):
    rows_m1 = len(matrix1)
    rows_m2 = len(matrix2)
    columns_m1 = len(matrix1[0])
    columns_m2 = len(matrix2[0])
# (1, 3, 4) (1)  1 x 3  3 x 1   0 0  0 0   +  0 1 1 0  + 0 2  3 0  
#           (2)
#           (3)
    if columns_m1 != rows_m2:
        return None
    
    zero_matrix = [[0 for _ in range(columns_m2)] for _ in range(rows_m1)]

    for i in range(rows_m1):
        for j in range(columns_m2):
            for k in range(columns_m1):
                zero_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return zero_matrix

print(multiply2matrices(matrix1, matrix2))