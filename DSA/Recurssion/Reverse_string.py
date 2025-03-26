str = 'alok'

array = list(str)
print(array)

pointer1= 0
pointer2 = len(array)-1

while pointer1 < pointer2:
    array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
    pointer1 +=1
    pointer2 -=1
print(array)


st = ''
for char in array:
    st += char

print(st)