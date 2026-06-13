from Rimuru import Rimuru
from Veldora import Veldora

def battle(e1, e2):
    e1.talk()
    e2.talk()
    print('\n')
    round = 0

    while e1.hp>0 and e2.hp>0:
        round+=1
        print(f'------Round {round}------')
        print(f'-------Fight-------')
        e1.ultimate()
        e2.ultimate()
        e1.atk()
        e2.atk()
        e1.hp-= e2.ad if e2.ad<e1.hp else e1.hp
        e2.hp-= e1.ad if e1.ad<e2.hp else e2.hp
        print(f'{e1.get_name()}: {e1.hp}hp')
        print(f'{e2.get_name()}: {e2.hp}hp')
        print('\n')
        
    winner = e1.get_name() if e1.hp>0 else e2.get_name() if e2.hp>0 else "both"
    print(f'### ⭐ {winner} wins ⭐ ###\n**{winner.lower()} smirks')


p1h = int(input("Enter"))
p1d = int(input())
p2h = int(input())
p2d = int(input())

p1 = Rimuru(5, 50)
p2 = Veldora(3, 100)
battle(p1, p2)