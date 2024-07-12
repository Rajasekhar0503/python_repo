word=input('enter the word to search vowels:')
vowels=('a','e','i','o','u')
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
