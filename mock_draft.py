"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks
import pandas as pd
import fantasy_draft_rank
import random 


class Player():
    def __init__(self, player_name, position, points):
        self.player_name = player_name
        self.position = position
        self.points = points
    
    def __repr__(self):
        return self.player_name

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
    #ranked = fantasy_draft_rank.Rank(player_df).rank()
    
    
    # print(ranked.roster)
    # unsorted_ranks = list()
    rank = ranks.Rank(player_df)
    rank.position_points()
    unsorted_ranks = list()
    
    #For each player
    for i in range(len(player_df)):
        #Create a player instance
        temp_player = Player(player_df['player_name'][i],\
            rank.roster[player_df['player_name'][i]]['position'],\
            rank.roster[player_df['player_name'][i]]['rank_points'])
        #Put it in unsorted list with points
        unsorted_ranks.append((temp_player,temp_player.points))
    
    #Sort list by points descending
    sorted_ranks = sorted(unsorted_ranks, key=second , reverse=True)
    
    player_list = []
    for i in sorted_ranks:
        player_list.append(i[0])
    
    return player_list
    

#Driver: Rachel Navigator: Grant
def mock_draft(df):
    """Simulates an 8 person mock draft. 
    
    Args:
        draft_dict (dict): A dictionary containing the players information. 
        
    """
    
        
    # data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    # df = pd.DataFrame(data)
    
    ranked = fantasy_draft_rank.Rank(df)
    playerName_position = {}
    for j in ranked.roster:
        playerName_position[j]= ranked.roster[j]["position"]
    
    computer = 1
    
    
    particpants = []
    
    draft_players = []
    user = Particpant()
    user.name = "User"
    
    draft_order = {}
    
    new_roster = {}
    
    while computer <= 8:
        participant = Particpant()
        participant.name = f"Computer {computer}"
        draft_players.append(participant)

        computer += 1
    
    players_ranked = draft_round(df)
    draft_pick = random.randint(1,8)
    draft_players[draft_pick] = user
    #print(len(draft_players))
    current_round = 0
    print(draft_pick)
    while current_round < 8:
        current_round += 1 
        for draft_player in draft_players:
            #print(players_ranked)
            iterator = 0
            if draft_player.name == "User":
                selection = input("Make your selection: ")
                for i in range(len(players_ranked)):
                    if selection == players_ranked[i].player_name:
                        temp_player = players_ranked[i]
                        if temp_player.position == "QB":
                            if draft_player.roster["QB"] == None:
                                draft_player.roster["QB"] = temp_player
                                players_ranked.remove(temp_player)
                                
                        elif temp_player.position == "RB":
                            if draft_player.roster["RB1"] == None:
                                draft_player.roster["RB1"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] == None:
                                draft_player.roster["RB2"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = temp_player
                                players_ranked.remove(temp_player)
                        
                            elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex2"] = temp_player
                                players_ranked.remove(temp_player)
                                
                        elif temp_player.position == "WR":
                            if draft_player.roster["WR1"] == None:
                                draft_player.roster["WR1"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] == None:
                                draft_player.roster["WR2"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex2"] = temp_player
                                players_ranked.remove(temp_player)
                                
                        elif temp_player.position == "TE":
                            if draft_player.roster["TE"] == None:
                                draft_player.roster["TE"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] == None:
                                draft_player.roster["Flex1"] = temp_player
                                players_ranked.remove(temp_player)
                                
                            elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                                draft_player.roster["Flex1"] = temp_player
                                players_ranked.remove(temp_player)
            else:
                for i in range(len(players_ranked)):
                    if players_ranked[iterator].position == "QB":
                        if draft_player.roster["QB"] == None:
                            draft_player.roster["QB"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1

                    elif players_ranked[iterator].position == "RB":
                        if draft_player.roster["RB1"] == None:
                            draft_player.roster["RB1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] == None:
                            draft_player.roster["RB2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                    elif players_ranked[iterator].position == "WR":
                        if draft_player.roster["WR1"] == None:
                            draft_player.roster["WR1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] == None:
                            draft_player.roster["WR2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                    elif players_ranked[iterator].position == "TE":
                        if draft_player.roster["TE"] == None:
                            draft_player.roster["TE"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                        elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                iterator += 1
    for participant in draft_players:
        print(participant.roster)


if __name__ == "__main__":
    
    
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    
    mock_draft(df)
    # myRank = fantasy_draft_rank.Rank(df)
    # roster = myRank.position_points()
    # print(roster)
    
