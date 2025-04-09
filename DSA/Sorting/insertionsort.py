def insertion_sort(array):
    n = len(array)
    for i in range(0,n):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] =  array[j], array[j-1]
            j -=1

    return array





arr = [13, 46, 24, 52, 20, 9, 4]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
