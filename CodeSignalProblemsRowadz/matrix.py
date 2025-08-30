# CHECKED
matrix = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 1]  
    ]

matrixb = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 1]  
    ] 
    
def two_matrix_sum(matrix1, matrix2):
    sum_matrix = []
    matrix_len = len(matrix1)
    for row1, row2 in zip(matrix1, matrix2):
        row__sum_matrix = []
        for element1, element2 in zip(row1, row2):
            element3 = element1 + element2
            row__sum_matrix.append(element3)
        sum_matrix.append(row__sum_matrix)
    print(sum_matrix)

two_matrix_sum(matrix, matrixb)

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    print(transposed)
    
transpose_matrix(matrix)

def transpose_matrix2(matrix):
    print([list(row) for row in zip(*matrix)])

transpose_matrix2(matrix)