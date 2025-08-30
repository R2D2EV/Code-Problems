# CHECKED
def sortByHeight(a):
    i = 1
    while i < len(a):
        if a[i] != -1:
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
        i += 1
    return(a)

def sortByHeight2(a):
    holder = sorted([number for number in a if number != -1])
    i = 0
    j = 0
    while i < len(a):
        if a[i] != -1:
            a[i] = holder[j]
            j += 1
        i += 1
    return a


if __name__ == '__main__':
    try:
        a = [-1, 150, 190, 170, -1, -1, 160, 180]
        print(sortByHeight(a))
        print(sortByHeight2(a))

    except Exception as e:
        print(e)