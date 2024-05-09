from src.game_simulation import GameSimulation
from src.report import Report


if __name__ == "__main__":
    report = Report()
    for _ in range(300):
        game_simulation = GameSimulation(report)
        turn_report = game_simulation.play()

    report.generate_complete_report()
