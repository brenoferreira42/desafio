# TODO: Update to HandlePlayerMove?
class PlayRound(object):
    def play(self, property, player):
        player_type = player.type()
        player_type.play(property, player)
