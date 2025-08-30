def solution(inputString):
    result = ''
    length = len(inputString)
    for i in range(length // 2 + length % 2):
        result += inputString[i]
        if length - 1 - i != i:
            result += inputString[length - 1 - i]
    return result

# "abcdefg", the function should return "gfedabc".

def solution2(inputString):
    result = ''
    length = len(inputString)
    for i in range(length // 2 + length % 2):
        # a b c d e f g  0  1  2  3
        result += inputString[- i - 1]

    for i in range(length // 2):
        # a b c d e f g  0  1  2  3
        result += inputString[i]
        
    return result


inputString = "abcdefg"
print(solution2(inputString))