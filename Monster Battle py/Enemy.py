class Enemy:
    def __init__(self, name, ad, hp):
        self.__name = name
        self.ad = ad
        self.hp = hp

    def talk():
        print("**cricket**")
    
    def ultimate(self):
        print(f"{self.__name} has no ultimate.")

    def get_name(self):
        return self.__name