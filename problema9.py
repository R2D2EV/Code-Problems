def palindrome_numbers(numbers):
    palindrome_n = []
    for number in numbers:
        if str(number)[::] == str(number)[::-1]:
            palindrome_n.append(number)
    return palindrome_n

print(palindrome_numbers([1, 33, 44, 120, 111]))