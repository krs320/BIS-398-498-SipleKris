### Exercise 5.20 Two-Dimensional List

def display_table(table, width):

    
#Headers 
    indent = len(str(len(table)))
    print(f'{"":{indent}}', end='')

    for col in range(len(table[0])):
        print(f'{col:>{width}}', end='')
    print()

    for i, row in enumerate(table):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{width}}', end='')
        print()
          
values = [list(range(0, 10)), 
          list(range(10, 20)), 
          list(range(20, 30)), 
          list(range(30, 40)), 
          list(range(40, 50)), 
          list(range(50, 60)), 
          list(range(60, 70)), 
          list(range(70, 80)), 
          list(range(80, 90)), 
          list(range(90, 100)), ]

display_table(values, 5)