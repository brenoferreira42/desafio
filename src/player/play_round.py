# TODO: Update to HandlePlayerMove?
class PlayRound(object):
    def play(self, property, playerType):
        move = playerType.play(property)
        print(move)
