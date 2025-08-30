def solution(arr):
    lenght = len(arr)
    middle = lenght // 2  # 5 // 2 = 2
    new_list = []
    if lenght % 2 == 1:
        left = middle - 1
        right = middle + 1
        new_list.append(arr[middle])
    else:
        left = middle - 1
        right = middle
    while left >= 0 and right < lenght:
        new_list.append(arr[left] * arr[right])
        left -= 1
        right += 1

    return new_list


print(solution([1, 2, 3, 4, 5]))

print(solution([1, 2, 3, 4]))