import random
class Magic:
    def __init__(self,name,cost,dmg,type):
        self.name=name
        self.cost=cost
        self.dmg=dmg
        self.type=type

    def generate_dmg(self):
        low=self.dmg-10
        high=self.dmg+10
        return random.randrange(low,high)
