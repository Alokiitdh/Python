#Tuples
str = 'alok'
my_list = [1,2,3,4]

zip(str, my_list)
print(zip) # The result is ZIP obect
 
new = []
for pair in zip(str, my_list):
    print(pair)
    new.append(tuple(pair))

print(new)
for letter, number in new:
    print(letter, number)