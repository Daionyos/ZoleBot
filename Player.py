class Player:
    counter = 0 # Static counter to track deal order
    def __init__(self):
        self.game_score = 0
        self.hand = []
        self.is_bigGuy = False
        self.id = count(self.__class__.counter,self)
    pass
def count(n,self):
    if n >= 3:
        self.__class__.counter = 0
        return self.__class__.counter
    else:
        self.__class__.counter = self.__class__.counter + 1
        return self.__class__.counter