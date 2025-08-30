# CHECKED
def adjacentElementProduct(numbers):
    i = 0
    max_numbers = []
    len_numbers = len(numbers)
    while i < len_numbers:
        j = i + 1
        while j < len_numbers:
            product = numbers[i] * numbers[j]
            print(str(numbers[i]) + '*' + str(numbers[j]) + "=" +  str(product))
            j += 1
            max_numbers.append(product)
        print(i)
        print(j)

        i += 1
    print(max_numbers)
    return max(max_numbers)

def adjacentElementProduct2(numbers):
    lista = [numbers[i] * numbers[i + 1] for i in range(len(numbers) - 1)]
    # return max(lista)
    return max (
        [numbers[i] * numbers[i + 1] for i in range(0, len(numbers) - 1)]
    )


if __name__ == "__main__":
    try:
        for i in range(3):
            print(i)
        numbers = [3, 6, -2, -5, 7, 3]
        print(adjacentElementProduct(numbers))
        print(adjacentElementProduct2(numbers))
    except Exception as e:
        print(e)