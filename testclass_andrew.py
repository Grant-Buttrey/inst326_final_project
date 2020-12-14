import fantasy_draft_rank as fdr
import pprint






class Player:
    
    def __init__(self, player):
        
        self.player_name = player
        self.fumbles = roster[player]["fumbles"]
        self.passing = roster[player]["passing"]
        self.rank_points = roster[player]["rank_points"]

if __name__ == "__main__":
    roster = fdr.main()
    player_objects = []
    for player_name in roster:
        my_player = Player(player_name)
        player_objects.append(my_player)
        
    for item in player_objects:
        print(item.rank_points)
    
    
    
            