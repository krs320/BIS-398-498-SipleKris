### Exercise 5.28 Class Survey

import numpy as np
import statistics as stats

results = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 2, 2, 3, 3, 2, 5]

values, counts = np.unique(results, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses & frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Min response: {values[counts.index(min(counts))]} , {min(counts)} times')

print(f'Max response: {values[counts.index(max(counts))]} , {max(counts)} times')

print(f'Range of response: ({min(counts)}-{max(counts)})')

print(f'Mean response: {stats.mean(counts)}')

print(f'Median response: {stats.mean(counts)}')

print(f'Mode response: {stats.mode(counts)}')

print(f'Variance: {stats.pvariance(counts)}')

print(f'Standard deviation: {stats.pstdev(counts)}')