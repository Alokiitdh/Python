#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


## Lets start Coding

PLACEHOLDER = '[name]'

with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\Mail Merge Project Start\Input\Names\invited_names.txt', mode ='r') as name:
    names = name.readlines()# read each line and make it in list
    print(names)


with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\Mail Merge Project Start\Input\Letters\starting_letter.txt', mode = 'r') as para:
    letter_content = para.read() # here i want all content inside letter_content
    for name in names:
        stripeed_name = name.strip()
        new = letter_content.replace(PLACEHOLDER, stripeed_name)
        with open(fr'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripeed_name}.text', mode = 'w') as sending:
            sending.write(new) 







