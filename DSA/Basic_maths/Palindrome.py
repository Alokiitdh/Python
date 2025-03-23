number = int(input('Enter number to check for palindrome:'))

revrse = 0
num = number

while number>0:
    last_digits = number%10
    revrse = revrse*10 + last_digits
    number = number //10

print(f'Reverse number: {revrse}')
if revrse == num:
    print('Palindrome')
else:
    print('Not a Palindrome')