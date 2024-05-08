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
        self.__current_player_move_index = 0
        self.__properties_sell_values = []
        self.__properties_rent_values = []
        self.__player_types = [
            ImpulsivePlayer,
            CautiousPlayer,
            DemandingPlayer,
            RandomPlayer,
        ]
        self.__generate_property_values()
        self.__generate_rent_values()
        self.__build_board()
        self.__build_players()

    def __build_players(self):
        player_types = random.sample(self.__player_types, len(self.__player_types))
        for i, player_type in enumerate(player_types):
            current_player = Player(player_type)
            self.players.append({"position": i, "player": current_player})

    def __build_board(self):
        for i in range(20):
            current_property = Property(
                self.__properties_sell_values[i], self.__properties_rent_values[i]
            )
            self.board.append({"position": i + 1, "property": current_property})

    # TODO: Also generate rent values
    def __generate_property_values(self):
        min_property_value = 150
        max_property_value = 800
        # initial_balance = [300] * 4

        # total_earned_per_lap = 100 * len(initial_balance)

        self.__properties_sell_values = []
        total_property_values = 0
        for _ in range(20):
            property_value = random.randint(min_property_value, max_property_value)
            self.__properties_sell_values.append(property_value)
            total_property_values += property_value

        average_property_value = total_property_values / len(
            self.__properties_sell_values
        )

        self.__properties_sell_values = [
            int(value * (average_property_value / property_value))
            for value in self.__properties_sell_values
        ]

    def __generate_rent_values(self):
        for property_value in self.__properties_sell_values:
            rent_value = int(property_value * random.uniform(0.05, 0.1))
            self.__properties_rent_values.append(rent_value)

    def __roll_dice(self):
        return random.randint(1, 6)

    def __advance_in_board(self, current_position, position):
        return (current_position + position) % 20

    def __update_player_position(self, position, player):
        player.position = position

    def __update_player_move_index(self):
        if self.__current_player_move_index == len(self.players) - 1:
            self.__current_player_move_index = 0
        else:
            self.__current_player_move_index += 1

    def __choose_player(self):
        chosen_player = self.players[self.__current_player_move_index]
        self.__update_player_move_index()

        return chosen_player["player"]

    def __remove_current_player(self):
        deleted_player = self.players[self.__current_player_move_index]
        for property in self.board:
            if property["property"].owner == deleted_player:
                property["property"].owner = None

        self.players.pop(self.__current_player_move_index)
        for i in range(len(self.players)):
            self.players[i]["position"] = i

    def play_turn(self):
        selected_player = self.__choose_player()
        movement = self.__roll_dice()
        self.__update_player_position(movement, selected_player)
        current_movement = self.__advance_in_board(selected_player.position, movement)

        if selected_player.balance == 0:
            self.__remove_current_player()
        else:
            self.__play_round.play(
                self.board[current_movement]["property"], selected_player
            )


sim = Simulation()
sim.play_turn()
