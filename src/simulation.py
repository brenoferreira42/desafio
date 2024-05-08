import random
from property import Property
from player.player import Player
from player.play_round import PlayRound
from player.player_types import (
    ImpulsivePlayer,
    CautiousPlayer,
    DemandingPlayer,
    RandomPlayer,
)


class Simulation(object):
    def __init__(self):
        self.board = []
        self.players = []
        self.__play_round = PlayRound()
        self.__player_types = [
            ImpulsivePlayer,
            CautiousPlayer,
            DemandingPlayer,
            RandomPlayer,
        ]
        self.__build_board()
        self.__build_players()

    def __build_players(self):
        player_types = random.sample(self.__player_types, len(self.__player_types))
        for player_type in player_types:
            current_player = Player(player_type)
            self.players.append(current_player)

    def __build_board(self):
        for i in range(20):
            current_property = Property()
            self.board.append({"position": i + 1, "property": current_property})

    def __roll_dice(self):
        return random.randint(1, 6)

    def __advance_in_board(self, current_position, position):
        return (current_position + position) % 20

    def __update_player_position(self, position, player):
        player.position = position

    # TODO: Os jogadores se alteram em rodadas, numa ordem definida aleatoriamente no começo da partida.
    def __choose_player(self):
        return random.choice(self.players)

    def play_turn(self):
        selected_player = self.__choose_player()
        movement = self.__roll_dice()
        self.__update_player_position(movement, selected_player)
        current_movement = self.__advance_in_board(selected_player.position, movement)
        self.__play_round(
            self.board[current_movement]["property"], selected_player.type
        )


sim = Simulation()
sim.play_turn()
