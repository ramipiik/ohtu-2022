class PlayerStats:
    def __init__(self, reader):
        self.reader=reader

    def top_scorers_by_nationality(self, nationality):
        players=self.reader.get_players()
        filtered=[]
        for player in players:
            if player.nationality==nationality:
                filtered.append(player)
        filtered.sort(reverse=True)
        return filtered

