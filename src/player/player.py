class Player(object):
    def __init__(self, type):
        self.__balance = 300
        self.position = 0
        self.type = type

    @property
    def balance(self):
        return self.__balance
