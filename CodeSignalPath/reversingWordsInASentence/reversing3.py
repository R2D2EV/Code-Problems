# Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

# Here's what you need to consider:

# The input string will include between 1 and 100 words.
# Each word consists of characters separated by white space.
# A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
# The given string will not start or end with a space, and there will be no occurrence of double spaces.
# After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.
# Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The mapping is case-sensitive.

# Example

# For the input string "CapitaL letters", the output should be "ovggvih XzkrgzO".

def opposite_char(c):
    if 'a' <= c <= 'z':
        return chr(ord('z') - (ord(c) - ord('a')))
    elif 'A' <= c <= 'Z':
        return chr(ord('Z') - (ord(c) - ord('A')))
    else:
        return c  # Por si acaso, aunque no debería haber otros caracteres

def transform_string(s):
    words = s.split()
    
    # Transformar cada carácter de cada palabra
    transformed_words = []
    for word in words:
        transformed = ''.join(opposite_char(c) for c in word)
        transformed_words.append(transformed)
    
    # Reorganizar: último primero, luego los demás en orden
    if len(transformed_words) > 1:
        result = [transformed_words[-1]] + transformed_words[:-1]
    else:
        result = transformed_words
    
    return ' '.join(result)

input_str = "CapitaL letters"
output = transform_string(input_str)
print(output)  # Salida esperada: "ovggvih XzkrgzO"
