def len_number(n):
    len_num = 0
    while abs(n) > 0:
        n = n // 10
        len_num += 1
    return len_num


def solution(n):
    len_num = len_number(n)
    counter = 0
    i = 1
    while i < len_num:
        digit1 = (n % (10 ** i)) % (10 ** i) // 10 ** (i - 1)
        digit2 = (n % (10 ** (i + 1))) % (10 ** (i + 1)) // 10 ** i
        if digit1 == digit2:
            counter += 1
        i += 1
    return counter


if __name__ == '__main__':
    try:
        n = 112322444
        solution(112322444)
    except Exception as e:
        print(e)