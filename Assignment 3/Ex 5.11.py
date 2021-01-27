### Exercise 5.11 Summarizing Letters of String

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    count = []
    
    for letter in string.lower():
        if letter in alphabet:
            if letter in letters:
                index = letters.index(letter)
                count[index] += 1
            else:
                letters.append(letter)
                count.append(1)
           
    tuples = list(zip(letters, count))
    tuples.sort()
    return tuples

sentence = input('Enter a sentence: ')
summary = summarize_letters(sentence)


# Occurances of Each Letter in Alphabet
for character, count in summary:
    print(f'{character}: {count}')
    
    
# Include full alphabet
all_alphabet = True

if len(summary) == len(alphabet):
    for item in summary:
        if item[0] not in alphabet:
            all_alphabet = False
            break  
else:
    all_alphabet = False
    
if all_alphabet:
    print(f'"{sentence}" includes every letter of the alphabet')
else:
    print(f'"{sentence}" does not include every letter of the alphabet')