
# CHECKED
def transpose_matrix2(matrix):
    return [list(row) for row in zip(*matrix)]

def matrix_elements_sum(matrix):
    transposed_matrix = transpose_matrix2(matrix)
    sum_places = 0
    for row in transposed_matrix:
        for column in row:
            if column == 0: 
                break
            sum_places += column
    return sum_places


if __name__ == '__main__':
    try:
        matrix = [
            [0, 1, 1, 2],
            [0, 5, 0, 0],
            [2, 0, 3, 1]  
        ]
        print(matrix_elements_sum(matrix))
    except Exception as e:
        print(e)