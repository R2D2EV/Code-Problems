# Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should convert to 'a', and 'a' should convert to '1'.

# You need to return a new string with the converted words, rejoined with hyphens.

# Ensure you maintain the original order of the words from the input string in your output string.

# The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.

# Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

# Example

# For the input string "1-a-3-c-5", the output should be "a-1-c-3-e".
def solution(s):
    partes = s.split('-')
    resultado = []

    for parte in partes:
        if parte.isdigit():
            numero = int(parte)
            if 1 <= numero <= 26:
                resultado.append(chr(ord('a') + numero - 1))
            else:
                resultado.append(parte)  # Si está fuera del rango, se deja igual
        elif parte.isalpha() and len(parte) == 1:
            resultado.append(str(ord(parte) - ord('a') + 1))
        else:
            resultado.append(parte)  # Si no es válido, se deja igual

    return '-'.join(resultado)

# Ejemplo de uso
entrada = "1-a-3-c-5"
print(solution(entrada))  # Salida esperada: "a-1-c-3-e"
