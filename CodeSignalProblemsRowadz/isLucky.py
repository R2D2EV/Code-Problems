# CHECKED
def is_lucky(number):
    digits = str(number)
    length = len(digits)

    if length % 2 != 0: return False

    half = length // 2
    first_half_sum = sum([int(d) for d in digits[:half]])
    second_half_sum = sum([int(d) for d in digits[half:]])

    return first_half_sum == second_half_sum

if __name__ == '__main__':
    try:
        n = 1230
        print(is_lucky(n))
    except Exception as e:
        print(e)