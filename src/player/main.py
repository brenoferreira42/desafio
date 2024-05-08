from player import Player
from play_round import PlayRound
from player_types import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer

play_round = PlayRound()
player = Player()

play_round.play(player, ImpulsivePlayer())
play_round.play(player, DemandingPlayer())
play_round.play(player, CautiousPlayer())
play_round.play(player, RandomPlayer())
