import random


class GameBoard(object):
    def __init__(self, players, properties):
        self.__current_player_index = 0
        self.properties_positions = []
        self.players = players
        self.properties = properties

    def advance_current_player_index(self):
        if self.__current_player_index == len(self.players) - 1:
            self.__current_player_index = 0
        else:
            self.__current_player_index = self.__current_player_index + 1

    def get_current_player(self):
        return self.players[self.__current_player_index]

    def choose_player(self):
        chosen_player = self.get_current_player()
        return chosen_player["player"]

    def __remove_current_player_properties(self, player):
        for property in self.properties:
            if property.owner == player:
                property.owner = None

    def remove_current_player(self, player):
        current_player = self.players[self.__current_player_index]
        self.__remove_current_player_properties(current_player)
        self.players.pop(self.__current_player_index)

        if self.__current_player_index >= len(self.players):
            self.__current_player_index = self.__current_player_index - 1

    def update_player_position(self, position, player):
        player["player"].position = position

    def roll_dice(self):
        return random.randint(1, 6)

    def get_players_in_game(self):
        return self.players

    def get_richest_player_in_game(self):
        players_in_game = self.get_players_in_game()
        if not players_in_game:
            return None

        sorted_players = sorted(
            players_in_game, key=lambda x: (x["player"], -x["position"]), reverse=True
        )

        return sorted_players[0]

    def advance_position_in_board(self, current_position, position):
        self.update_player_position(position, self.get_current_player())
        new_position = (current_position + position) % 20
        if new_position < current_position:
            self.get_current_player().balance += 100
        return new_position
