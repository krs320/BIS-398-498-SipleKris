### Exercise 6.8 Writing Out Check Amount

numbers = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 
    14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 
    18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 
    40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 
    80: 'EIGHTY', 90: 'NINETY'}

amount = input('Enter a dollar amount less than 1000: ')
dollars, cents = amount.split('.')
dollars = int(dollars)
cents = int(cents)

number_words = []

if dollars == 0:
    number_words.append(numbers[dollars])
	
elif dollars >= 100:
    number_words.append(numbers[dollars // 100] + ' HUNDRED')


dollars %= 100 


if dollars in range(10, 20):
    number_words.append(numbers[dollars])
elif dollars in range(20, 100):
    number_words.append(numbers[dollars // 10 * 10])
    dollars %= 10 


if dollars in range(1,10):
    number_words.append(numbers[dollars])

print(f'{" ".join(number_words)} AND {cents}/100')