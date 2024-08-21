# string manipulations

'''
fruit = 'Banana'
index = 0
while index < len(fruit):
    print(fruit[index])
    index+=1
'''
# Using FOR loop
'''
fruit = 'Banana'
for i in fruit:
    print(i)
'''
# Slicing
'''
fruit = 'banana'
print(fruit[:])
print(fruit[:3])
print(fruit[2:4])
'''
# Opposite Letter 

'''
fruit = 'ALok'
word = fruit
def opp_letter(word):
    for i in range(len(word)):
        print(word[len(word)-i-1:len(word)-i])

opp_letter(word)
'''
