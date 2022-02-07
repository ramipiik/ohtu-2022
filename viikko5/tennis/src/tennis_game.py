class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        elif player_name == "player2":
            self.player2_score = self.player2_score + 1
        else:
            raise Exception("Sorry, no such player")

    def even_score(self):
        if self.player1_score>3:
            return "Deuce"
        return self.points_to_text(self.player1_score) + "-All"

    def victory(self):
        if self.player1_score>self.player2_score:
            return "Win for player1"
        return "Win for player2"
    
    def advantage(self):
        if self.player1_score>self.player2_score:
            return "Advantage player1"
        return "Advantage player2"

    def points_to_text(self, points):
        if points == 0:
            return "Love"
        if points == 1:
            return "Fifteen"
        if points == 2:
            return "Thirty"
        if points == 3:
            return "Forty"

    def get_score(self):
        difference = self.player1_score - self. player2_score
        if difference==0:
            return self.even_score()
        if max(self.player1_score, self.player2_score)>=4:
            if abs(difference)==1:
                return self.advantage()
            return self.victory()
        return self.points_to_text(self.player1_score) + "-" + self.points_to_text(self.player2_score)
