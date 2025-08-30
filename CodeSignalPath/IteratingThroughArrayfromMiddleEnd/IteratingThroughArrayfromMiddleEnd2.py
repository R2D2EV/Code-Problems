# For example, 
# if the input is numbers = [1, 2, 3, 4, 5], 
# the output should be [(3, 0), (2, 4), (1, 5)]. Similarly, if the input is 
# numbers = [1, 2, 3, 4], the output should be [(2, 3), (1, 4)].

def solution(arr):
    new_arr = []
    numbers_len = len(arr)
    middle = numbers_len // 2
    if numbers_len % 2 == 1:
        left = middle - 1
        right = middle + 1
        new_arr.append((arr[middle], 0))
    else:
        left = middle - 1
        right = middle
    while left >= 0 and right < numbers_len:
        new_arr.append((arr[left], arr[right]))
        left -= 1
        right += 1
    print(new_arr)

numbers = [1, 2, 3, 4, 5]
solution(numbers)