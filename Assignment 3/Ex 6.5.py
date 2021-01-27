### Exercise 6.5 Counting Duplicate Words

text = input('Write a sentance to evaluate for duplicates: ')

word_occur = {}

# Count Occurance of Each Word
for word in text.split():
    if word in word_occur: 
        word_occur[word] += 1  
    else:
        word_occur[word] = 1  

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_occur.items()):
    if count > 1:
        print(f'{word:<12}{count}')

