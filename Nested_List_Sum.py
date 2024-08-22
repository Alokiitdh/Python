# List
num = []
sum = 0
numbers =[[1,2],[3],[4,5,6]]
for i in range(len(numbers)):
    num = numbers[i]
    for k in range(len(num)):
        sum = sum + num[k]
print(sum)

