#  2. Similar Word Pairs – Pattern Matching
# Ejercicio: Dado un arreglo de palabras, encuentra todos los pares de palabras que tengan el mismo patrón de letras 
# (por ejemplo, "foo" y "app" tienen el mismo patrón: la primera y segunda letra son iguales, la tercera es diferente).

# Input: ["foo", "bar", "app", "egg", "add"]
# Output: [("foo", "app"), ("egg", "add")]
def get_pattern(word):
    pattern = {}
    pattern_code = []
    next_code = 0

    for char in word:
        if char not in pattern:
            pattern[char] = next_code
            next_code += 1
        pattern_code.append(pattern[char])

    return pattern, pattern_code

print(get_pattern("foo"))

def find_similar_word_pairs(words):
    similar_pairs = []

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if get_pattern(words[i]) == get_pattern(words[j]):
                similar_pairs.append((words[i], words[j]))

    return similar_pairs

# Input list of words
words = ["foo", "bar", "app", "egg", "add"]

# Find and print similar word pairs
similar_word_pairs = find_similar_word_pairs(words)
print(similar_word_pairs)



