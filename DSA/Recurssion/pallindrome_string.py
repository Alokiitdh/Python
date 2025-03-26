str = 'racecar'

# Converting to array
array =[]
for cg in str:
    array.append(cg)
print(array)

p1 = 0
p2 = len(array)-1

while p1<p2:
    array[p1], array[p2] = array[p2], array[p1]
    p1 +=1
    p2 -=1

print(array)

st = ''
for ch in array:
    st+=ch

print(st)

if st == str:
    print('Pallindrome')
else:
    print('Not')