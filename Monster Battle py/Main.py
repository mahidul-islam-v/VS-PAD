import sys, time
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
        time.sleep(1*s)
        print(f'-------Fight!------')
        time.sleep(0.5*s)
        e1.ultimate()
        e2.ultimate()
        
        time.sleep(0.5*s)
        e1.atk()
        time.sleep(0.5*s)
        e2.atk()
        time.sleep(0.5*s)
        e1.hp = max(0, e1.hp - e2.ad)
        e2.hp = max(0, e2.hp - e1.ad)
        print(f'{e1.get_name()}: \033[32m{e1.hp}\033[0m hp')
        time.sleep(0.5*s)
        print(f'{e2.get_name()}: \033[32m{e2.hp}\033[0m hp')
        time.sleep(2*s)

        
    winner = e1.get_name() if e1.hp>0 else e2.get_name() if e2.hp>0 else "both"
    print(f'\n### ⭐ \033[33m{winner} Wins\033[0m ⭐ ###\n**\033[30m{winner.lower()} smirks\033[0m')


p1d = 5
p1h = 30
p2d = 1
p2h = 50

arg = sys.argv
al = len(arg)
s = int(input("Enter game speed\033[30m (recommended 10\033[0m): "))

if al != 1 and al != 5 :
    print("\033[1;34mInvalid number of arguments!\033[0m\nRead the documentation on github for further instructions.")
else:
    if al == 5:
        p1d = int(arg[1])
        p1h = int(arg[2])
        p2d = int(arg[3])
        p2h = int(arg[4])

    p1 = Rimuru(p1d, p1h)
    p2 = Veldora(p2d, p2h)
    battle(p1, p2)

