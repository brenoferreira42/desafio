class Property(object):
    def __init__(self, sell_value: int, rent_value: int):
        self.sell_value = sell_value
        self.rent_value = rent_value
        self.owner = None
