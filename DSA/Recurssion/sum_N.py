
def sum_N(n):
    if n<= 0:
        return 0
    else:
        return n+sum_N(n-1)


n = 5
s = sum_N(n)
print(s)

## using for loop
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(sum)
