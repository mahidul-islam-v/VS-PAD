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
        p1.ultimate()
        p2.ultimate()
        p1.atk()
        p2.atk()
        p1.hp-= p2.ad
        p2.hp-= p1.ad
        print(f'{p1.get_name()}: {p1.hp}hp')
        print(f'{p2.get_name()}: {p2.hp}hp')
        print('\n')
        
    winner = p1.get_name() if p1.hp>0 else p2.get_name()
    print(f'{winner} wins\n**{winner.lower()} smirks')

p1 = Rimuru(50, 5)
p2 = Veldora(100, 4)