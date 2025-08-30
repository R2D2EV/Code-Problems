# CHECKED
import math
def solution(numbers):
    len_num = len(numbers)
    sum_opp_sumber = [numbers[i] + numbers[len_num - 1 - i] for i in range(math.ceil(len_num/2))]
    return sum_opp_sumber


numbers = [1, 2, 3, 4, 5]
print(solution(numbers))

def solution(numbers):
    i = 0
    len_numbers = len(numbers)
    ord_num = []
    while i < len_numbers:
        second_num = round((numbers[i] * numbers[len_numbers - i - 1]) ** 0.5, 2)
        ord_num.append((numbers[i], second_num)) 
        i += 1
    return ord_num
                                                            

numbers = [1, 2, 3, 4, 5]
print(solution(numbers))