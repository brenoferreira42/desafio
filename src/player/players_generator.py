import random
from player.player import Player
from player.player_types import (
    ImpulsivePlayer,
    CautiousPlayer,
    DemandingPlayer,
    RandomPlayer,
)


class PlayersGenerator(object):
    def __init__(self):
        self.__player_types = [
            ImpulsivePlayer,
            CautiousPlayer,
            DemandingPlayer,
            RandomPlayer,
        ]
        self.players = []

    def construct_players(self) -> list:
        player_types = random.sample(self.__player_types, len(self.__player_types))
        for i, player_type in enumerate(player_types):
            current_player = Player(player_type)
            self.players.append({"position": i, "player": current_player})

        return self.players
