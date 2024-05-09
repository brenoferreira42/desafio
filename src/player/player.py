class Player(object):
    def __init__(self, type):
        self.balance = 300
        self.position = 0
        self.type = type

    def __lt__(self, other):
        return self.balance < other.balance
