"""Aggregation: A team has players that can exist without the team."""
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players  # Existing Player objects are shared.

    def show_players(self):
        print(f"{self.name}: {', '.join(p.name for p in self.players)}")

if __name__ == '__main__':
    alex = Player('Alex')
    sam = Player('Sam')
    team = Team('Tigers', [alex, sam])
    team.show_players()
    print(f"Player still exists independently: {alex.name}")
