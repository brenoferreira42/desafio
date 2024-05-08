import random


class Property(object):
    def __init__(self):
        self.sell_value = random.randint(150, 10000)
        self.rent_value = random.randint(150, 5000)
        self.owner = None
