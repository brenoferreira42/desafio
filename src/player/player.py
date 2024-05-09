class Player(object):
    def __init__(self, strategy):
        self.balance = 300
        self.position = 0
        self.strategy = strategy

    def __lt__(self, other):
        return self.balance < other.balance
