from random import randint
from time import sleep
print("Vou pensar em um numero entre 0 e 5. tente adivinhar")
x = int(input("Em que numero eu pensei?"))
y = int(randint(0, 5))
print('PENSANDO...')
sleep(2)
if y == x:
    print('You win!!')
else:
    print('You lost boy! ', y)
