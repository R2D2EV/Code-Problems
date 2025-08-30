def len_number(n):    
    len_num = 0
    while abs(n) > 0:
        n = n // 10
        len_num += 1
    return len_num

def solution(n):
    rever_num = 0
    while n > 0:
        len_num = len_number(n) - 1
        digit = n % 10
        rever_num += (10 ** (len_num))  * digit
        print(rever_num)
        n = n // 10
        len_num -= -1
    

    print(rever_num)
    print(len_num)                

n = 123456
solution(n)