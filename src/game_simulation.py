from src.player.players_generator import PlayersGenerator
from src.property.properties_generator import PropertiesGenerator
from src.game_board import GameBoard
from src.player.play_round import PlayRound


class GameSimulation(object):
    def __init__(self, report):
        self.players = PlayersGenerator().construct_players()
        self.properties = PropertiesGenerator().construct_properties()
        self.board = GameBoard(self.players, self.properties)
        self.__play_round = PlayRound()
        self.__report = report

    def play_turn(self):
        selected_player = self.board.choose_player()
        dice_face = self.board.roll_dice()
        board_position = self.board.advance_position_in_board(
            selected_player.position, dice_face
        )

        if selected_player.balance <= 0:
            self.board.remove_current_player(selected_player)
            return {"win": False}
        elif len(self.board.get_players_in_game()) == 1 and selected_player.balance > 0:
            return {"win": True, "winner": selected_player}
        else:
            self.__play_round.play(
                self.board.properties[board_position], selected_player
            )
            self.board.advance_current_player_index()
            return {"win": False}

    def play(self):
        winner = None
        turn_duration = 0
        for i in range(1000):
            if not len(self.players) == 0:
                turn = self.play_turn()
                if i == 999 and turn["win"] is False:
                    winner = self.board.get_richest_player_in_game()["player"]
                    turn_duration = i
                    self.__report.generate_turn_report(winner, turn_duration)
                    break
                elif turn["win"] is True:
                    winner = turn["winner"]
                    turn_duration = i
                    self.__report.generate_turn_report(winner, turn_duration)
                    break
