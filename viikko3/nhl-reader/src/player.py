class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality=nationality
        self.assists=assists
        self.goals=goals
        self.points=goals+assists
        self.penalties=penalties
        self.team=team
        self.games=games
    
    def __str__(self):
        return f"{self.name:20} {self.team:5} {str(self.goals):3}+ {str(self.assists):3}= {str(self.points)}"
    
    def __gt__(self, other_player):
        return self.points>other_player.points
