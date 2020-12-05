"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks

#Driver: Grant Navigator: Sakib
def second(tup):
    """
    This method is for returning the last member of a tuple
    
    Parameters:
        tup(tuple): A tuple of two elements, the second of which is an integer
    """
    return tup[-1]
    
#Driver: William Navigator: Rachel
def draft_round(player_dict):
    """Sorts the players into draft rounds based on their ranks. 
    
    Args:
        player_dict (dict): A dictionary containing the players information. 
        
    Returns:
        The dictionary draft_dict. 
    
    """
    unsorted_ranks = list()
    
    for player in player_dict.keys():
        unsorted_ranks.append((player,player_dict[player]))
    
    sorted_ranks = sorted(unsorted_ranks, key=second , reverse=True)
    
    draft_dict = dict()

    for index in range(len(sorted_ranks)):     
        if((index//8)+1 in draft_dict.keys()):
            draft_dict[((index//8)+1)].append(sorted_ranks[index][0].name)
        else:
            draft_dict[((index//8)+1)] = list()
            draft_dict[((index//8)+1)].append(sorted_ranks[index][0].name)
            
    return draft_dict

#Driver: Rachel Navigator: Grant
def mock_draft(draft_dict):
    """Simulates an 8 person mock draft. 
    
    Args:
        draft_dict (dict): A dictionary containing the players information. 
        
    """
    
    #github testing
    

if __name__ == "__main__":
    rank = ranks.Rank()
    player_dict = rank.last_season_stats()
    print(draft_round(player_dict))