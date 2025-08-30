def repeat_char_jump(inputString, step):
    n = len(inputString)
    result = []
    visited_indices = [False] * n  # To keep track of visited characters
    current_index = 0  # Start at the beginning of the string
    count = 0  # Number of characters added to the result

    while count < n:
        if not visited_indices[current_index]:
            result.append(inputString[current_index])
            visited_indices[current_index] = True
            count += 1
        
        current_index = (current_index + step) % n
        
    return "".join(result)

def repeat_char_jump_alternative(inputString, step):
    n = len(inputString)
    result = [''] * n  # Pre-allocate the list with n empty strings
    current_index = 0
    print(result)
    
    for i in range(n):  # We iterate 'n' times, as we need to add 'n' characters
        result[i] = inputString[current_index]
        current_index = (current_index + step) % n
        
    return "".join(result)

print(repeat_char_jump_alternative("abcdefg", 3))
# Example usage
print(repeat_char_jump("abcdefg", 3))

