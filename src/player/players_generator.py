import random
from src.player.player import Player
from src.player.player_strategies import (
    ImpulsivePlayerStrategy,
    CautiousPlayerStrategy,
    DemandingPlayerStrategy,
    RandomPlayerStrategy,
)


class PlayersGenerator(object):
    def __init__(self):
        self.__player_strategies = [
            ImpulsivePlayerStrategy,
            CautiousPlayerStrategy,
            DemandingPlayerStrategy,
            RandomPlayerStrategy,
        ]
        self.players = []

    def construct_players(self) -> list:
        player_strategies = random.sample(
            self.__player_strategies, len(self.__player_strategies)
        )
        for i, player_strategy in enumerate(player_strategies):
            current_player = Player(player_strategy)
            self.players.append({"position": i, "player": current_player})

        return self.players
