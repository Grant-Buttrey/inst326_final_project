"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks
import pandas as pd
import test

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
    ranked = test.Rank(player_df)
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
    
    print(draft_round(df))
    
    #github testing
    

if __name__ == "__main__":
    mock_draft()