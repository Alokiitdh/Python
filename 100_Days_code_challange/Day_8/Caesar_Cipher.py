print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def index(element,listt):
    count = 0
    if element in listt:
        for char in listt:
            if char == element:
                #print(f"Index: {count}")
                return count
            else:
                count+=1
    else:
        print('Letter is not there')




### Encryption and Decryption 
def encrypt(original_text, shift):
    encrypt_word = ''
    for char in original_text:
        if char in alphabet:
            i = index(char,alphabet)
            new_i = i+shift
            if new_i >25:
                new_i = new_i - 26
                encrypt_word += alphabet[new_i]
            else:
                encrypt_word += alphabet[new_i]


    return encrypt_word

def decrypt(encrypted_word, shift):
    decrypt_word = ''
    for char in encrypted_word:
        if char in alphabet:
            i = index(char, alphabet)
            prev_index = i-shift
            if prev_index < 0:
                prev_index = 26 + prev_index
                decrypt_word += alphabet[prev_index]
            else:
                decrypt_word += alphabet[prev_index]
    
    return decrypt_word

cont = 'y'
count = 2
original_text = input('Enter Message to code: ').lower()
while(cont == 'y' ):
    
    ecodeco = input('Encode(e)/Decode(d):').lower()

    if ecodeco == 'e':
        # Do Encryption
        shift = int(input('How much shift: '))
        en_word = encrypt(original_text,shift)
        print('Encrypted word:', en_word)

    elif ecodeco == 'd':
        sft = int(input('How much was shifted: '))
        encrypted_word = en_word
        dec_word = decrypt(encrypted_word, sft)
        print('Decrypted word:', dec_word) 
    else:
        print('Invalid choice ')
    
    cont = input('Wanna Continue(y/n): ').lower()


    




