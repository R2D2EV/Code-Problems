def reversed_triple_chars(s: str) -> str:
    length = len(s)
    len_div = length // 3
    newstring = ''
    i = 0
    r_range = 0

    if length < 3:
        return s

    while i < len_div:
        l_range = i * 3
        r_range = (i + 1) * 3
        newstring += s[l_range:r_range][::-1]
        i += 1

    newstring += s[r_range:]
    return newstring

print(reversed_triple_chars('abcdef'))    # cbafed
print(reversed_triple_chars('abcdefg'))   # cbafedg
print(reversed_triple_chars('a'))         # a
print(reversed_triple_chars('abcde'))     # cbade
