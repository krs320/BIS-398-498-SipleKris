### Exercise 3.1 """Validating User Input"""

passes = 0  # number of passes

# Results of 10 students
for student in range(10):
    # get one exam result
    result = int ( input ( 'Enter result ( 1=pass, 2=fail): '))
    
    while result != 1 and result != 2:  
        print( 'Invalid response' )
        result = int ( input( 'Enter result ( 1=pass, 2=fail): '))
        
    if result == 1:
        passes = passes + 1

# termination phase
print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')