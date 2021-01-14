### Exercise 4.12 """Tortoise vs the Hare."""

import random
END_RACE = 70  # final position

# Randomly Move Tortoise 
def move_tortoise(tortoise):
    move = random.randrange(1, 11)

    if 1 <= move <= 5:  # fast
        tortoise += 3
    elif move in (6, 7):  # slip
        tortoise -= 6
    else:  # slow
        tortoise += 1
		
# Tortoise stops at END_RACE
    if tortoise < 1:
        tortoise = 1
    elif tortoise > END_RACE: 
        tortoise = END_RACE

    return tortoise

# Randomly move hare
def move_hare(hare):
    move = random.randrange(1, 11)  # randomize move to choose
      
    # determine moves by percent
    if move in (3, 4):  # big hop
        hare += 9
    elif move == 5:  # big slip
        hare -= 12
    elif 6 <= move <= 8:  # small hop
        hare += 1
    elif move > 8:  # small slip
        hare -= 2

# Hare stops at END_RACE
    if hare < 1:
        hare = 1
    elif hare > END_RACE: 
        hare = END_RACE

    return hare

def print_positions(tortoise, hare):
    
    for count in range(1, END_RACE + 1):
        if count == tortoise and count == hare:
            print('Ow!!!', end='')
        elif count == hare:
            print('Hare', end='')
        elif count == tortoise:
            print('Tortoise', end='')
        else:
            print(' ', end='')
        
    print()

# Race 
tortoise = 1
hare = 1
timer = 0

print('On your mark! Get set!')
print('Bang!')
print("And they're off!")

while tortoise < END_RACE and hare < END_RACE: 
    hare = move_hare(hare)
    tortoise = move_tortoise(tortoise)
    print_positions(tortoise, hare)
    timer += 1

# Winner is
if tortoise >= hare:
    print('Tortoise wins!')
else:  # hare beat tortoise
    print('Hare wins...boo')
