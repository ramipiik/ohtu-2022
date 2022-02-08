from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    # matcher = query.build()
    # matcher = query.playsIn("NYR").build()
    # matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals") .build()
    
    matcher = (
      query  
        .playsIn("NYR")  
        .hasAtLeast(5, "goals")  
        .hasFewerThan(10, "goals")  
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
