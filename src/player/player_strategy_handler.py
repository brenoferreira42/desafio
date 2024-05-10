class PlayerStrategyHandler(object):
    def play(self, property, player):
        player.strategy().play(property, player)
