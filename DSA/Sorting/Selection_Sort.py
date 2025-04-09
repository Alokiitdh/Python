ar = [13,46,24,52,20,9,4]


def sorting(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index], array[i]
    return array

print(sorting(ar))



