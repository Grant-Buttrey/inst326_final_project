"""
This Program will run an 8 man mock draft. 
"""

import fantasy_draft_rank as ranks
import pandas as pd
import fantasy_draft_rank
import random 


class Player():
    """
    Creates obects that contains the player's information
    Attributes:
        player_name (string): the NFL player's name
        position (string): the NFL player's position
        points (float or int): the NFL player's points from the ranking system
    """
    #Driver: Grant Navigator: Willaim
    def __init__(self, player_name, position, points):
        """An initializer method that initializes the attributes of Player
        Arguments:
            player_name (string): the NFL player's name
            position (string): the NFL player's position
            points (float or int): the NFL player's points from the ranking system
        """
        
        self.player_name = player_name
        self.position = position
        self.points = points
    #Driver: Sakib Navigator: Rachel
    def __repr__(self):
        """A repr method that displays the NFL player's name
        Returns:
            player_name (String): The NFL player's name
        """
        return self.player_name

class Particpant():
    """
    A class that is the object for each participant in the mock draft
    Attributes:
        name (String): The type of participant
        roster (dictionary): A dictionary to be filled with the participant's fantasy roster
    """
    #Driver: William Navigator: Rachel
    def __init__(self):
        """
        assigns an empty string to name and creates a dictionary for the roster
        """
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
    
#Driver: William Navigator: Sakib
def draft_round(player_df):
    """Sorts the players into draft rounds based on their ranks. 
    
    Args:
        player_dict (dict): A dictionary containing the players information. 
        
    Returns:
        The dictionary draft_dict. 
    
    """

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
    

#Driver: Grant Navigator: Rachel
def mock_draft(df):
    """Simulates an 8 person mock draft. 
    
    Args:
        draft_dict (dict): A dictionary containing the players information.
    Side effects:
        Modifies the values or roster of the Participant objects
        Prints the particpants roster in progress
        Prints every roster from the mock draft simulation
        
    """
    
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
    draft_pick = random.randint(0,7)
    draft_players[draft_pick] = user
    
    current_round = 0
    #iterates through each round of the draft (8).
    while current_round < 8:
        print("\n\n")
        print(f"Round: {current_round + 1}")
        print("Recomendations:\n", players_ranked[0:16])
        print("\n")
        current_round += 1 
        #itterates each perticipant for each round
        for draft_player in draft_players:
            iterator = 0
            if draft_player.name == "User":  
                complete = 0
                while complete == 0:
                    selection = input("Make your selection: ") 
                    #Cannot be a player already taken
                    #Must be correct spelling, case sensitive
                    #Must be a player in the list of players
                    #Must have position open for the selection
                    if selection in [player.player_name for player in players_ranked]:
                        complete = 1
                for i in range(len(players_ranked)):

                    if selection == players_ranked[iterator].player_name:
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
            else:
                iterator = 0
                for i in range(len(players_ranked)):
                    if players_ranked[iterator].position == "QB":
                        if draft_player.roster["QB"] == None:
                            draft_player.roster["QB"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                    elif players_ranked[iterator].position == "RB":
                        if draft_player.roster["RB1"] == None:
                            draft_player.roster["RB1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] == None:
                            draft_player.roster["RB2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["RB1"] != None and draft_player.roster["RB2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                    elif players_ranked[iterator].position == "WR":
                        if draft_player.roster["WR1"] == None:
                            draft_player.roster["WR1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] == None:
                            draft_player.roster["WR2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["WR1"] != None and draft_player.roster["WR2"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex2"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                    elif players_ranked[iterator].position == "TE":
                        if draft_player.roster["TE"] == None:
                            draft_player.roster["TE"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                        elif draft_player.roster["TE"] != None and draft_player.roster["Flex1"] != None and draft_player.roster["Flex2"] == None:
                            draft_player.roster["Flex1"] = players_ranked[iterator]
                            players_ranked.remove(players_ranked[iterator])
                            iterator -= 1
                            break
                
                    iterator += 1
            print(draft_player.roster)
    print("\n\nFinal Rosters:")
    for participant in draft_players:
        print(participant.name)
        print(participant.roster)


if __name__ == "__main__":
    
    
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    
    mock_draft(df)

    
