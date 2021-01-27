### Exercise 5.5 Alphabet Slicing


alphabet = 'abcdefghijklmnopqrstuvwxyz'


# First half using starting & ending indices
print(alphabet [0: len (alphabet) // 2])


# First half using ending index
print(alphabet [: len (alphabet) // 2])


# Second half using starting & ending indices
print(alphabet [len(alphabet) // 2: len(alphabet)])


# Second half using starting index
print(alphabet [len(alphabet) // 2:])


# Every other letter 
print(alphabet [::2])


# Starting with Z
print(alphabet [::-1])


# Every thrid letter in reverse
print(alphabet [::-3])