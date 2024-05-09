class PlayerStrategyHandler(object):
    def play(self, property, player):
        player_type = player.strategy()
        player_type.play(property, player)
