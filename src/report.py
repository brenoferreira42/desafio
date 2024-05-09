class Report(object):
    def __init__(self):
        self.turn_reports = []

    def generate_turn_report(self, winner, turn_duration):
        report = {
            "winner_behaviour": winner.type.__name__,
            "turn_duration": turn_duration,
        }

        self.turn_reports.append(report)

    def generate_complete_report(self):
        total_games = len(self.turn_reports)
        timeouts = sum(
            1 for report in self.turn_reports if report["turn_duration"] == 999
        )
        average_turns = (
            sum(report["turn_duration"] for report in self.turn_reports) / total_games
        )

        wins_by_behaviour = {}
        for report in self.turn_reports:
            behaviour = report["winner_behaviour"]
            wins_by_behaviour[behaviour] = wins_by_behaviour.get(behaviour, 0) + 1

        most_winning_behaviour = max(wins_by_behaviour, key=wins_by_behaviour.get)

        print("Estatísticas dos Turnos:\n")
        print(f"Partidas terminadas por time out (1000 rodadas): {timeouts}")
        print(f"Média de turnos por partida: {average_turns:.2f}")
        print("Porcentagem de vitórias por comportamento dos jogadores:")
        for behaviour, wins in wins_by_behaviour.items():
            win_percentage = (wins / total_games) * 100
            print(f"  {behaviour}: {win_percentage:.2f}%")
        print(f"Comportamento que mais vence: {most_winning_behaviour}")
