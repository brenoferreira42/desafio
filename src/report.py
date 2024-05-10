class Report(object):
    def __init__(self):
        self.__turn_reports = []

    def generate_turn_report(self, winner, turn_duration: int):
        behavior_names = {
            "ImpulsivePlayerStrategy": "Impulsivo",
            "DemandingPlayerStrategy": "Exigente",
            "CautiousPlayerStrategy": "Cauteloso",
            "RandomPlayerStrategy": "Aleatório",
        }

        report = {
            "winner_behavior": behavior_names[winner.strategy.__name__],
            "turn_duration": turn_duration,
        }

        self.__turn_reports.append(report)

    def generate_complete_report(self):
        total_games = len(self.__turn_reports)
        timeouts = sum(
            1 for report in self.__turn_reports if report["turn_duration"] == 999
        )
        average_turns = (
            sum(report["turn_duration"] for report in self.__turn_reports) / total_games
        )

        wins_by_behavior = {}
        for report in self.__turn_reports:
            behavior = report["winner_behavior"]
            wins_by_behavior[behavior] = wins_by_behavior.get(behavior, 0) + 1

        most_winning_behavior = max(wins_by_behavior, key=wins_by_behavior.get)

        print("Estatísticas dos Turnos:\n")
        print(f"Partidas terminadas por time out (1000 rodadas): {timeouts}")
        print(f"Média de turnos por partida: {average_turns:.2f}")
        print("Porcentagem de vitórias por comportamento dos jogadores:")

        sorted_wins_by_behavior = sorted(wins_by_behavior.items(), key=lambda x: x[1])

        for behavior, wins in sorted_wins_by_behavior:
            win_percentage = (wins / total_games) * 100
            print(f"  {behavior}: {win_percentage:.2f}%")

        print(f"Comportamento que mais vence: {most_winning_behavior}")
