# file = open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\my_file.txt', mode = 'r')
# content = file.read()
# print(content)
# file.close()

#####33
# Alternate wau to open File



######### READING A FILE
with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\my_file.txt', mode = 'r') as file:
    content =file.read()
    print(content)

########## WRITING A FILE

with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\my_file.txt', mode = 'a') as file:
    file.write('\nSomething new added')

with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\my_file.txt', mode = 'r') as file:
    content =file.read()
    print(content)