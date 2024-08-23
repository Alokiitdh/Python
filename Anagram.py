#Anagram
str1 = 'Listen'
str2 = 'Silent'

def is_anagram(str1, str2):
    st1 = list(str1).sort()
    st2 = list(str2).sort()
    if st1 == st2:
        return True
    else: return False

print(is_anagram(str1, str2))