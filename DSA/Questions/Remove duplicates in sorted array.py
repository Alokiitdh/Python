# Remove Duplicates in sorted array:
def duplicate_sorted_array(sorted_array):
     #initializing a pointer 
     # approach : If the current number is different
     # from the previous it is unique
     pointer = 1
     for i in range(1,len(sorted_array)):
          if sorted_array[i] != sorted_array[i-1]:
               sorted_array[pointer] = sorted_array[i]
               pointer += 1

     return sorted_array[:pointer]
                    
          
array = [0,0,1,1,2,2,3]
result = duplicate_sorted_array(array)
print('output: ', result)