### Exercise 4.9

def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f'Fahrenheit{"Celsius":>10}')

for celsius in range(101):
    print(f'{celsius:10}{fahrenheit(celsius):10.1f}')