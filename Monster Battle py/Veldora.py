from Enemy import *
import random

class Veldora(Enemy):
    def __init__(self, ad, hp):
        super().__init__(name="Veldora", ad=ad, hp=hp)

    def talk():
        print('Haha! Come brother, I shall entertain you.')
    
    def ultimate(self):
        did_ult = random.random() < 0.05
        if did_ult:
            self.ap+= 9999999
            print('Veldora goes Super Saiyan!!!!!')