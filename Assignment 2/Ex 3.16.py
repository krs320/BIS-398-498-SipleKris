### Exercise 3.16 """Larger of two integers"""

largest = int ( input( 'Enter number: '))
number = int ( input( 'Enter number: '))

if number > largest:
    next_largest = largest
    largest = number
else:
    next_largest = number

for counter in range(2, 10):
    number = int ( input ( 'Enter number: '))

    if number > largest:
        next_largest = largest
        largest = number
    elif number > next_largest:
        next_largest = number

print(f'Largest # is {largest}, Second largest # is {next_largest}')