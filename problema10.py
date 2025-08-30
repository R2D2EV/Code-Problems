def orderH(arr):
    order = sorted(arr)
    i = 0
    counter = 0
    while i < len(arr):
        if arr[i] != order[i]:
            counter += 1
        i += 1
    print(counter)

heights = [5,1,2,3,4]
orderH(heights)