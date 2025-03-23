def meging_two_sorted_list(array1, array2):
    m = len(array1)
    n = len(array2)
    # define pointers
    i = m-1
    j = n-1
    k = m+n-1
   
    for _ in range(n):
        array1.append(0) 

    while i>=0 and j >= 0:
        if array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1
        k-=1

    return array1






list1 = [1,2,4]
list2 = [1,3,4]
result = meging_two_sorted_list(list1,list2)
print(result)
