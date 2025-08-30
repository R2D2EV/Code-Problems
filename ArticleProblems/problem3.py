# Tetris Problem

def solution(field, figure):
    # Get the height and width of the field
    height = len(field)
    width = len(field[0])
    # Iterate through the columns of the field
    for col in range(width - 2):
        # Iterate through the rows of the field from the bottom up
        for row in range(height - 1, -1, -1):
        # Check if the current cell is occupied
        if field[row][col] == 1:
            # If the cell is occupied, stop checking this column
            break
        # If the figure fits in the current position, check if a full row is formed
        elif all(field[row + i][col + j] + figure[i][j] <= 1 for i in range(3) for j in range(3)):
            # If a full row is formed, return the current column
            if any(all(field[row + i][col + j] == 1 for j in range(3)) for i in range(3)):
                return col
    # If no full rows are formed, return -1
    return -1