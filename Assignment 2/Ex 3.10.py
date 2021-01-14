### Exercise 3.10 """7% Investment Return"""


principal = 1000.0
int = 0.07

for year in range(1, 31):
    print(f'Amount after {year} years : $ {principal * (1 + int) ** year:.2f}')
