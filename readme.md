# inst326 final project
Contributors:
    Rachel Macairan
    Sakib Sarwar
    Grant Buttrey
    William Giovanini
    
Overview of the project: 

 Our final project is a program that creates a system that tells which round to draft an NFL player in your fantasy league in a draft. The purpose this project serves is to help the people who may not be familiar with fantasy football or are not able to follow football closely enough to know when to draft each player. It can also help those people who may not understand fantasy draft strategies. For example, in fantasy you probably would not draft a defense in the first round. Instead, you should probably draft either a running back or wide receiver. So, for the people who do not know this, our program will be able to tell them that they should not draft a defense in the first round and perhaps they should look into drafting a running back or a wide receiver in the first round instead. We also have a mock draft concept which alows the user to simulate a draft against 7 different computers.

Scope of the Project:

The project uses an API available a https://www.fantasyfootballdatapros.com/api/players/2019/all, which contains statistics for each player in the NFL such as total yards, total touchdowns, and total receptions from the previous season. This program will use those statistics to tell the user when to draft a certain player. The way the program will give value to a player is based on their 2019 statistics. They can gain and lose points based on their statistics and position as well. Using the example from before, a running back like Todd Gurley will gain points from his statistics but will also gain points because he is a running back. But a quaterback like Daniel Jones will lose points or else they will be overvalued. This point system will allow the players like Todd Gurley to be ranked higher than the quarterbacks like Daniel Jones to tell the user to pick Gurley in an earlier round.

How to run the code:

Reach the directory relative to the file mock_draft.py and run the line python mock_draft.py.
Make sure you import the libraries pandas, requests, re, operator 

fantasy_draft_rank.py:
imports: re, requests, operator, pandas, pprint
League class:
            Attributes: player_dict which is an empty dictionary that is later filled with the statistics of the different players in the API.
            __init__: 
                    Arguments: df which is the data frame from the API
Rank class:
            Attributes: ranked_league which is an object of type League
                        roster which is the player_dict attribute of ranked_league
                        frame which is the data frame from the API
            Methods:
                    position_points: This method will find out what the position is 
                                    and add or take away points to the players value.
                                    Args:
                                        self (Rank): A player object that contains the attributes of a players.        
                                    Side Effects:
                                        self.rank_points (int): Modifies the value of self.rank_points.           
                                    Returns:
                                        The variable self.rank_points.
main(): Reads in the API and sets it equal to a variable called players, creates an instance of rank, and passes through the pandas data frame from the API.

mock_draft.py:
imports: fantasy_draft_rank, pandas, random
Player class: 
            Attributes: player_name which is the name of the NFL player
                        position which is the position of the NFL player
                        points which is the points from the ranking system for the respective player
            Methods: __init__:
                            Arguments: player_name which is the name of the NFL player
                                        position which is the position of the NFL player
                                        points which is the points from the ranking system for the respective player
                    __repr__:
                            Returns a string of the player's name
Participant class:
            Attributes: name which is the name of the drafter, i.e. user or computer
                        roster which is the fantasy roster of the drafter
            Methods: __init__:
                        assigns an empty string to name
                        creates a dictionary for the roster
Methods:second:
            This method is for returning the last member of a tuple
            Arguments: tup which is a tuple of the player object and player points
            Returns the last player of the tuple that is passed through
        draft_round:
            Sorts the players into draft rounds based on their ranks.
            Arguments: player_dict which is a dictionary containing the player objects
            Returns: player_list which is a list of the NFL players in a list ordered by the points from the ranking system
        mock_draft:
            Simulates an 8 person mock draft.
            Arguments: df which is a data frame
            Side Effects: Modifies the values or roster of the Participant objects
                          prints the particpants roster in progress
                          prints every roster from the mock draft simulation



