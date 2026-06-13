import sys
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


p1d = 1
p1h = 30
p2d = 1
p2h = 100

arg = sys.argv
arglen = len(arg)

if arglen != 1 or arglen != 5 :
    print("\033[1;34mInvalid number of arguments!\033[0m\nRead the documentation on github for further instructions.")
else:
    if len(sys.argv) == 5:
        p1d = int(sys.argv[1])
        p1h = int(sys.argv[2])
        p2d = int(sys.argv[3])
        p2h = int(sys.argv[4])

    p1 = Rimuru(p1d, p1h)
    p2 = Veldora(p2d, p2h)
    battle(p1, p2)

