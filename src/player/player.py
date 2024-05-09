class Player(object):
    def __init__(self, type):
        self.__balance = 300
        self.position = 0
        self.type = type

    def __lt__(self, other):
        return self.__balance < other.__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value
