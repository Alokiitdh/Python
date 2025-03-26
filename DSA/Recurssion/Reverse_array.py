array = [2,4,2,6,7]

pointer1 =0
pointer2 = len(array)-1

## Swapping logic in arrays

while pointer1 < pointer2:
    array[pointer1], array[pointer2] = array[pointer2],array[pointer1]
    pointer1+=1
    pointer2-=1

print(array)