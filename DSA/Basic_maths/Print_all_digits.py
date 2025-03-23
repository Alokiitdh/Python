digits = 7789

ex_digit = []
for dig in str(digits):
    ex_digit.append(dig)

print(ex_digit)
m=0
for max in ex_digit:
    if int(max)>=m:
        m=int(max)

print(m)
