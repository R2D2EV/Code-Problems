def len_number(n):    
    len_num = 0
    while abs(n) > 0:
        n = n // 10
        len_num += 1
    return len_num

def solution(n):
    rever_num = 0
    len_num = 0

    while n > 0:
        digit = n % 10
        rever_num += (10 ** (len_num))  * digit + (10 ** (len_num + 1))  * digit
        n = n // 10
        len_num += 2

    return rever_num
    

if __name__ == '__main__':
    try:
        n = 123456
        solution(n)
    except Exception as e:
        print(e)