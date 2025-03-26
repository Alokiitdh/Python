vowels = ['a','e','i','o','u']
word = input('Enter Word: ')

def vowel_count(word):
    count = 0
    for char in word:
        if char in vowels:
            count+=1
    return count
print(f"Number of vowels in your word: {vowel_count(word)}")
