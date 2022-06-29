import random

test_seed = int(input('crear un numero semilla :'))
random.seed(test_seed)


cara_cruz = random.randint(0, 1)
if cara_cruz == 1:
    print('Cara')
else:
    print('Cruz')

