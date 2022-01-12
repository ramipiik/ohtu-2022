import statistics
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_team_Lemieux_in_PIT(self):
        pit_players=self.statistics.team("PIT")
        self.assertEqual(pit_players[0].name,"Lemieux")
    
    def test_team_three_players_in_EDM(self):
        edm_players=self.statistics.team("EDM")
        self.assertEqual(len(edm_players),3)

    def test_search_non_existing_player_returns_none(self):
        nobody=self.statistics.search("ERKKI")
        self.assertIsNone(nobody)

    def test_search_Kurri_found(self):
        kurri=self.statistics.search("Kurri")
        self.assertEqual(kurri.team, "EDM")
    
    def test_top_scorers_returns_5_players(self):
        top=self.statistics.top_scorers(4)
        self.assertEqual(len(top), 5)

    def test_top_scorers_Gretzky_has_most_points(self):
        top=self.statistics.top_scorers(4)
        self.assertEqual(top[0].name, "Gretzky")