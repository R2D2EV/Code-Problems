# CHECKED
# 1. Alternating Parity (Paridad Alternante) – Sliding Window
# Ejercicio: Dado un arreglo de enteros, encuentra la longitud máxima de una subcadena continua donde 
# los números alternan entre pares e impares.
# Input: [4, 3, 6, 7, 8, 1, 2]
# Output: 5  # Subarreglo: [3, 6, 7, 8, 1]

def alternating_parity(numbers):
    i = 1
    length_of_alternating = 1
    max_lenght = 1
    len_numbers = len(numbers)
    while i < len_numbers:
        if numbers[i] % 2 != numbers[i - 1] % 2:
            length_of_alternating += 1
            max_lenght = max(max_lenght, length_of_alternating)
        else:
            length_of_alternating = 1
            
        i += 1
    return max_lenght



if __name__ == "__main__":
    try:
        numbers = [4, 3, 6, 7, 8, 1, 2, 8, 1, 2]
        print(alternating_parity(numbers))
    except Exception as e:
        print(e)
        




# Input: [4, 3, 6, 7, 8, 1, 2]
# Output: 5  # Subarreglo: [3, 6, 7, 8, 1]

