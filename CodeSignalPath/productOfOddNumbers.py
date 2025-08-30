# CHECKED
def solution(n):
    product = 1
    counter = 0
    while abs(n) > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            counter += 1
        n = n // 10
    if counter == 0:
        return 0
    else:
        return product


if __name__ == '__main__':
    try:
        n = 4721
        print(solution(n))
    except Exception as e:
        print(e)