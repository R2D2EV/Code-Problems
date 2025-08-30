# CHECKED
def commonCharacterCount(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    count = 0

    for char in list1:
        if char in list2:
            list2.remove(char)  # elimina una ocurrencia
            count += 1

    return count

def commonCharacterCount(s1, s2):
    lista = []
    s1_dict = {}
    for letter, i in enumerate(s1):
        s1_dict[letter] = i
    
    common_char = 0
    for letter in s2:
        i = 0
        while i < len(s1_dict):
            if letter == s1_dict[i]:
                print(letter)
                print(s1_dict[i])
                lista.append(letter)
                s1_dict[i] = "1"
                common_char += 1
                print('comom: ' + str(common_char))
                break
            i += 1
    print(s1_dict, common_char)

from collections import Counter

def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    sum_ = 0
    seen = set()
    
    for c in s1:
        if c in c2 and c not in seen:
            # sum_ += c2[c] if c1[c] > c2[c] else c1[c]
            sum_ += min(c1[c], c2[c])
            seen.add(c)
            
    return sum_


if __name__ == '__main__':
    try:
        s1 = "aabccaaad"
        s2 = "adcaa"
        commonCharacterCount(s1, s2)
    except Exception as e:
        print(e)