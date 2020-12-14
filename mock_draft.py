"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks
import pandas as pd
import fantasy_draft_rank
import random 


class Particpant():
    def __init__(self):
        self.name = ""
        self.roster = {"QB" : None, "RB1" : None, "RB2" : None, "WR1" : None, "WR2" : None, "TE" : None, "Flex1" : None, "Flex2" : None}
        
    

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
    ranked = fantasy_draft_rank.Rank(player_df).rank()
    print(ranked)
    # print(ranked.roster)
    # unsorted_ranks = list()
    
    # key_list = list(ranked.roster.keys())
    # for i in range(len(ranked.roster)):
    #     temp_points = ranked.last_season_stats(key_list[i])
    #     unsorted_ranks.append((key_list[i],temp_points))
    #     print(temp_points)
    # sorted_ranks = sorted(unsorted_ranks, key=second , reverse=True)
    
    # draft_dict = dict()

    # for index in range(len(sorted_ranks)):     
    #     if((index//8)+1 in draft_dict.keys()):
    #         draft_dict[((index//8)+1)].append(sorted_ranks[index][0])
    #     else:
    #         draft_dict[((index//8)+1)] = list()
    #         draft_dict[((index//8)+1)].append(sorted_ranks[index][0])

 
    
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
    
    
    computer = 1
    
    
    particpants = []
    
    draft_players = []
    
    draft_order = {}
    
    new_roster = {}
    
    while computer <= 8:
        participant = Particpant()
        participant.name = "computer"
        draft_players.append(participant)
        # print(participant.name)s
        # print(participant.roster)
        # draft_player.extend([f"Computer {computer}"])
        computer += 1
    # print(particpants)
        
    # draft_player.append([f"User1"])
    players_ranked = draft_round(df)
    draft_pick = random.randint(1,8)

    #draft_player[draft_pick] = "user 1"

    counter = 1
    
    for i in draft_players:
        draft_order[counter] = i
        counter += 1
   
    #roster = {"QB" : None, "RB1" : None, "RB2" : None, "WR1" : None, "WR2" : None, "TE" : None, "Flex1" : None, "Flex2" : None}
    #print(draft_order)
  
    # participants_dict = {}
    
    # for i in draft_order:
    #         participants_dict[i] = roster
    #print(participants_dict)
    current_round = 0
    
    while current_round < 14:
        current_round += 1 
        for draft_player in draft_players:
            #print(players_ranked)
            for players_lists in players_ranked.values():
                #print(person)
                # print(players_lists)
                for nfl_player_name in players_lists:
                    #print(nfl_player_name)
                    
                    for nfl_player_position in playerName_position.values():
                        #print(nfl_player_position)
                        
                        if nfl_player_position == "QB":
                            if draft_player.roster["QB"] == None:
                                draft_player.roster["QB"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                            elif draft_player.roster["QB"] != None:
                                continue
                        elif nfl_player_position == "RB":
                            # print("Running Back")
                            print(draft_player.roster["RB1"])
                            if draft_player.roster["RB1"] == None:
                                draft_player.roster["RB1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] == None:
                                draft_player.roster["RB2"] = nfl_player_name
                                players_lists.remove(nfl_player_name)

                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex2"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] != None:
                                continue
                                
                        elif nfl_player_position == "WR":
                            if draft_player.roster["WR1"] == None:
                                draft_player.roster["WR1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] == None:
                                draft_player.roster["WR2"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex2"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] != None:
                                continue
                            
                        elif nfl_player_position == "TE":
                            if draft_player.roster["TE"] == None:
                                draft_player.roster["TE"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex1"] = nfl_player_name
                                players_lists.remove(nfl_player_name)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and participant.roster["Flex2"] != None:
                                continue
                               
    print(participant.roster)
                    
            # if users["position"]
            # print(participants_dict)
    
    # players_ranked = draft_round(df)
    # print("108")
    # while current_round <= 14:
    #     print("110")
    #     for player in draft_order:
    #         print("112" + player)
    #         if player == "[user 1]":
    #             print("114")
    #             pick = input("Make your selection!")
    #             for nfl_player in players_ranked:
    #                 if nfl_player == pick:
    #                     for j in playerName_position:
    #                         if playerName_position[pick] == "QB":
    #                             roster["QB"] = pick
    #                         elif playerName_position[pick] == "RB":
    #                             if roster["RB1"] == None:
    #                                 roster["RB1"] = pick
    #                             elif roster["RB2"] == None:
    #                                 roster["RB2"] = pick
    #                             elif roster["Flex1"] == None:
    #                                 roster["Flex1"] = pick
    #                             elif roster["Flex2"] == None:
    #                                 roster["Flex2"] = pick
    #                             else:
    #                                 print("Position filled")
    #                                 pick = input("Make a different available selection!")
    #                         if playerName_position[pick] == "WR":
    #                             if roster["WR1"] == None:
    #                                 roster["WR1"] = pick
    #                             elif roster["WR2"] == None:
    #                                 roster["WR2"] = pick
    #                             elif roster["Flex1"] == None:
    #                                 roster["Flex1"] = pick
    #                             elif roster["Flex2"] == None:
    #                                 roster["Flex2"] = pick
    #                             else:
    #                                 print("Position filled")
    #                                 pick = input("Make a different available selection!")
    #                         if playerName_position[pick] == "TE":
    #                             if roster["TE"] == None:
    #                                 roster["TE"] = pick
    #                             elif roster["Flex1"] == None:
    #                                 roster["Flex1"] = pick
    #                             elif roster["Flex2"] == None:
    #                                 roster["Flex2"] = pick
    #                             else:
    #                                 print("Position filled")
    #                                 pick = input("Make a different available selection!")
    #         else:
    #             continue
    #     current_round += 1

    
if __name__ == "__main__":
    mock_draft()
    
    myRank = fantasy_draft_rank.Rank()
    roster = myRank.position_points()
    print(roster)
    