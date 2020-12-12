"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks
import pandas as pd
import fantasy_draft_rank
import random 

#Driver: Grant Navigator: Sakib
def second(tup):
    """
    This method is for returning the last member of a tuple
    
    Parameters:
        tup(tuple): A tuple of two elements, the second of which is an integer
    """
    return tup[-1]
    
#Driver: William Navigator: Rachel
def draft_round(player_df):
    """Sorts the players into draft rounds based on their ranks. 
    
    Args:
        player_dict (dict): A dictionary containing the players information. 
        
    Returns:
        The dictionary draft_dict. 
    
    """
    ranked = fantasy_draft_rank.Rank(player_df)
    unsorted_ranks = list()
    
    key_list = list(ranked.roster.keys())
    for i in range(len(ranked.roster)):
        temp_points = ranked.last_season_stats(key_list[i])
        unsorted_ranks.append((key_list[i],temp_points))
    
    sorted_ranks = sorted(unsorted_ranks, key=second , reverse=True)
    
    draft_dict = dict()

    for index in range(len(sorted_ranks)):     
        if((index//8)+1 in draft_dict.keys()):
            draft_dict[((index//8)+1)].append(sorted_ranks[index][0])
        else:
            draft_dict[((index//8)+1)] = list()
            draft_dict[((index//8)+1)].append(sorted_ranks[index][0])
            
    return draft_dict

#Driver: Rachel Navigator: Grant
def mock_draft():
    """Simulates an 8 person mock draft. 
    
    Args:
        draft_dict (dict): A dictionary containing the players information. 
        
    """
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    
    current_round = 1
    computer = 1
    
    draft_player = []
    
    draft_order = {}
    
    while computer <= 8:
        draft_player.extend([f"Computer {computer}"])
        computer += 1
        
    #draft_player.append([f"User1"])
    
    draft_pick = random.randint(1,8)

    draft_player[draft_pick] = "user 1"

    counter = 1
    
    for i in draft_player:
        draft_order[counter] = i
        counter += 1
        
    roster = {"QB" : None, "RB1" : None, "RB2" : None, "WR1" : None, "WR2" : None, "TE" : None, "Flex1" : None, "Flex2" : None, "Bench1" : None, "Bench2" : None, 
              "Bench3" : None, "Bench4" : None, "Bench5" : None, "Bench6" : None}
    
    players_ranked = draft_round(df)
    
    # while current_round <= 14:
    #     for player in draft_order:
    #         if player == "user 1":
    #                 continue
    #         else:
    #             for nfl_player in players_ranked:
                    
                
                    
    
    # print(draft_round(df))
    
    
    

if __name__ == "__main__":
    mock_draft()