from Enemy import *
from Rimuru import *
from Veldora import *

def battle(p1, p2):
    p1.talk()
    p2.talk()
    round = 0

    while p1.hp>0 and p2.hp>0:
        print(f'------Round {round}------')
        print(f'-------Fight------')
        p1.ul

p1 = Rimuru(50, 5)
p2 = Veldora(100, 4)