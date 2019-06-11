import numpy as np

dice1 = np.random.randint(1,7)
dice2 = np.random.randint(1,7)

print('Dice 1 is {0}'.format(dice1))
print('Dice 2 is {0}'.format(dice2))

if (dice1+dice2)%2 == 0:
    print('Sum is even number.')
else:
    print('Sum is odd number.')