import random


class GameBoard(object):
    def __init__(self, players, properties):
        self.__current_player_turn = 0
        self.__players = players
        self.properties = properties

    def advance_current_player_turn(self):
        self.__current_player_turn = (self.__current_player_turn + 1) % len(
            self.__players
        )

    def __get_current_player(self):
        return self.__players[self.__current_player_turn]

    def choose_player(self):
        chosen_player = self.__get_current_player()
        return chosen_player["player"]

    def __remove_current_player_properties(self, player):
        for property in self.properties:
            if property.owner == player:
                property.owner = None

    def __update_player_position(self, position, player):
        player["player"].position = position

    def remove_current_player(self):
        current_player = self.__players[self.__current_player_turn]
        self.__remove_current_player_properties(current_player)
        self.__players.pop(self.__current_player_turn)

        if self.__current_player_turn >= len(self.__players):
            self.__current_player_turn = self.__current_player_turn - 1

    def roll_dice(self) -> int:
        return random.randint(1, 6)

    def get_players_in_game(self) -> list:
        return self.__players

    def get_richest_player_in_game(self):
        players_in_game = self.get_players_in_game()
        if not players_in_game:
            return None

        sorted_players = sorted(
            players_in_game, key=lambda x: (x["player"], -x["position"]), reverse=True
        )

        return sorted_players[0]

    def advance_position_in_board(self, current_position: int, position: int) -> int:
        self.__update_player_position(position, self.__get_current_player())
        new_position = (current_position + position) % 20
        if new_position < current_position:
            self.__get_current_player().balance += 100
        return new_position
