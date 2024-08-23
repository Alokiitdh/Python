# middle of the list
my_list = [1,2,3,4,5,6,7,8,9]
new_list = []

def middle_elements(my_list):
    for i in range(len(my_list)):
        if i != 0 and i!= len(my_list)-1:
            new_list.append(my_list[i])
    return new_list

print(middle_elements((my_list)))
