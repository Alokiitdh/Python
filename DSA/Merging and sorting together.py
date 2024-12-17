
def merging_sorting(array1, array2, m ,n):
    # define pointers
    i = m-1
    j=n-1
    k=m+n-1

    while i>=0 and j>=0:
      if array1[i] > array2[j]:
        array1[k] = array1[i]
        i -= 1

      else:
        array1[k] = array2[j]
        j-=1
      k-=1

    return array1  


        

arrayy1 = [1,2,3,0,0,0]
arrayy2 = [2,5,8]
m = 3
n= 3
result = merging_sorting(arrayy1, arrayy2, m, n)
print('Output:', result)