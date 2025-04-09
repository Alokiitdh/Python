def bubble_sort(arr):
    n = len(arr)

    # Outer loop for number of passes
    for i in range(n):
        # Inner loop for pairwise comparison
        for j in range(0, n - i - 1):  # Last i elements are already in place
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
arr = [13, 46, 24, 52, 20, 9, 4]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
