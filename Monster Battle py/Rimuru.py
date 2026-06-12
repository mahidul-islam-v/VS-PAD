from Enemy import *
import random

class Rimuru(Enemy):
    def __init__(self, ad, hp):
        super().__init__(name="Rimuru", ad=ad, hp=hp)

    def talk():
        print(f'Fight me!!')
    
    def ultimate(self):
        did_ult = random.random() < 0.35
        if did_ult:
            self.hp+= 3
            print('Rimuru regenerated 3 hp!')