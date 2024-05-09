from player.players_generator import PlayersGenerator
from property.properties_generator import PropertiesGenerator
from game_board import GameBoard
from player.play_round import PlayRound


class GameSimulation(object):
    def __init__(self):
        self.players = PlayersGenerator().construct_players()
        self.properties = PropertiesGenerator().construct_properties()
        self.board = GameBoard(self.players, self.properties)
        self.__play_round = PlayRound()

    def play_turn(self):
        selected_player = self.board.__choose_player()
        movement = self.board.roll_dice()
        self.__update_player_position(movement, selected_player)
        current_movement = self.__advance_in_board(selected_player.position, movement)

        if selected_player.balance == 0:
            self.board.__remove_current_player()
        if (
            len(self.board.get_players_in_game()) == 0
            and self.board.get_current_player().balance > 0
        ):
            # Winner
            return self.board.get_current_player()
        else:
            self.__play_round.play(
                self.board[current_movement]["property"], selected_player
            )

    def play(self):
        for i in range(1000):
            if i == 1000:
                return self.board.get_richest_player_in_game()
            self.play_turn()


if __name__ == "__main__":
    game_simulation = GameSimulation()
    game_simulation.play()
