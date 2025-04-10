numbers = [1,2,3,4,5,6]
# for i in range(len(numbers)):
#     numbers[i] +=1
# print(numbers)

# new_list = [n+1 for n in numbers]
# print(new_list)

# name = 'Alok'
# new_name = [char for char in name]
# print(new_name)

# new = list(name)
# print(new)


# new_num = [n*2 for n in range(1,5)]
# print(new_num)

# new_sq = [n**2 for n in range(1,10) if n> 4]
# print(new_sq)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n)  for n in list_of_strings ]
print(numbers)
result = [n for n in numbers if n % 2== 0]
print(result)