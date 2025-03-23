number = int(input("Enetr number: "))
num = number

num_list = []

for dig in str(num):
    num_list.append(dig)
print(num_list)

power = len(num_list)
print(power)

sum = 0
for dig in num_list:
    sum = sum + int(dig)**power

print(sum)

if sum == num:
    print('Armstrong number')
else:
    print('Not ')
