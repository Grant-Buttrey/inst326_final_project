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

 
    
    #print(playerName_position)
    #print(playerName_position["Lamar Jackson"])
    #print(playerName_position.values())
    
            
    return draft_dict

#Driver: Rachel Navigator: Grant
def mock_draft():
    """Simulates an 8 person mock draft. 
    
    Args:
        draft_dict (dict): A dictionary containing the players information. 
        
    """
  
        
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    
    ranked = fantasy_draft_rank.Rank(df)
    playerName_position = {}
    for j in ranked.roster:
        playerName_position[j]= ranked.roster[j]["position"]
    
    current_round = 1
    computer = 1
    
    draft_player = []
    
    draft_order = {}
    
    new_roster = {}
    
    while computer <= 8:
        draft_player.extend([f"Computer {computer}"])
        computer += 1
        
    draft_player.append([f"User1"])
    players_ranked = draft_round(df)
    draft_pick = random.randint(1,8)

    draft_player[draft_pick] = "user 1"

    counter = 1
    
    for i in draft_player:
        draft_order[counter] = i
        counter += 1
   
    roster = {"QB" : None, "RB1" : None, "RB2" : None, "WR1" : None, "WR2" : None, "TE" : None, "Flex1" : None, "Flex2" : None}
    print(draft_order)
  
    
    players_ranked = draft_round(df)
    print("108")
    while current_round <= 14:
        print("110")
        for player in draft_order:
            print("112")
            if player == "[user 1]":
                print("114")
                pick = input("Make your selection!")
                for nfl_player in players_ranked:
                    if nfl_player == pick:
                        for j in playerName_position:
                            if playerName_position[pick] == "QB":
                                roster["QB"] = pick
                            elif playerName_position[pick] == "RB":
                                if roster["RB1"] == None:
                                    roster["RB1"] = pick
                                elif roster["RB2"] == None:
                                    roster["RB2"] = pick
                                elif roster["Flex1"] == None:
                                    roster["Flex1"] = pick
                                elif roster["Flex2"] == None:
                                    roster["Flex2"] = pick
                                else:
                                    print("Position filled")
                                    pick = input("Make a different available selection!")
                            if playerName_position[pick] == "WR":
                                if roster["WR1"] == None:
                                    roster["WR1"] = pick
                                elif roster["WR2"] == None:
                                    roster["WR2"] = pick
                                elif roster["Flex1"] == None:
                                    roster["Flex1"] = pick
                                elif roster["Flex2"] == None:
                                    roster["Flex2"] = pick
                                else:
                                    print("Position filled")
                                    pick = input("Make a different available selection!")
                            if playerName_position[pick] == "TE":
                                if roster["TE"] == None:
                                    roster["TE"] = pick
                                elif roster["Flex1"] == None:
                                    roster["Flex1"] = pick
                                elif roster["Flex2"] == None:
                                    roster["Flex2"] = pick
                                else:
                                    print("Position filled")
                                    pick = input("Make a different available selection!")
            else:
                continue
        current_round += 1

    print(new_roster)

if __name__ == "__main__":
    mock_draft()
    