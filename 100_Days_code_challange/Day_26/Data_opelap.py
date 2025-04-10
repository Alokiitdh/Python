with open('Day_26/file1.txt', mode = 'r') as file1:
    file1_list = file1.readlines()
new_1 = [int(n.strip()) for n in file1_list]
print(new_1)

with open('Day_26/file2.txt', mode ='r') as file2:
    file2_list = file2.readlines()

new2 = [ int(n.strip()) for n in file2_list]
print(new2)

result = [n for n in new_1 if n in new2]
print(result)