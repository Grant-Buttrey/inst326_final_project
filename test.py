"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re
import requests 
import operator
import pandas as pd

class League():
    def __init__(self, df):
        self.player_dict= {}
        stats = df["stats"] 
        counter = 0
        fumble_list = df["fumbles_lost"]
        pos_list = df["position"]

        for i in df["player_name"]:
            self.player_dict[i] = stats[counter]

            self.player_dict[i]["fumbles"] = fumble_list[counter]
            self.player_dict[i]["position"] = pos_list[counter]
            counter+=1
        #print(self.player_dict["Lamar Jackson"])
        
'''
class Player():
    """This class with gather all of the statistics for each player in the api.
    
    Attributes:
        player_name (str): The name of the player.
        position (str): The position of the player.
        pass_td (float): The amount of passing touchdowns in the 2019 season. 
        pass_yds (float): The amount of passing yards in the 2019 season.
        receiving_td (float): The amount of receiving touchdowns in the 2019 season.
        receiving_yd (float): The amount of receiving yards in the 2019 season.
        rushing_td (float): The amount of rushing touchdowns in the 2019 season.
        rushing_yd (float): The amount of rushing yards in the 2019 season.
        fumbles (float): The amount of fumbles lost in the 2019 season.
        

    def __init__(self,player_name, position, pass_yd, pass_td, receiving_td, receiving_yd, rushing_yd, rushing_td, fumbles):     
        self.name = player_name
        self.position = position
        self.pass_td = pass_td
        self.pass_yd = pass_yd
        self.receiving_td = receiving_td
        self.receiving_yd = receiving_yd
        self.rushing_td = rushing_td
        self.rushing_yd = rushing_yd
        self.fumbles = fumbles
        
    def player_stats(self, player_api):
        """Creates a list of player instances and appends players statistics to
        the list.
        
        Args:
            player_api (json): The api being read in the main function. 
            
        Return:
            A list of player instances. 
        
        """
        player_instances = []
    
        for i in player_api:
            player_instances.append(player_api(i["player_name"], i["position"], i['stats']["passing"]["passing_yds"], i['stats']["passing"]["passing_td"], i['stats']["receiving"]["receiving_td"], i['stats']["receiving"]["receiving_yds"]
                                           ,i['stats']["rushing"]["rushing_yds"], i['stats']["rushing"]["rushing_td"], i['fumbles_lost']))
        
        return player_instances
    
    def __repr__(self):
        """Allows the player instance to be returned as the players name. 
        
        Returns:
            The name of the player.
        
        """
        return self.name
'''

class Rank():
    """This class will rank the players from best to worst based on their 
    statistics from the 2019 season.
    """
    
    def __init__(self, df):
        ranked_league = League(df)
        self.roster = ranked_league.player_dict

               
    def position_points(self, position):
        """This method will find out what the position is 
        and add or take away points to the players value.
        
        Args:
            self (Rank): A player object that contains the attributes of a players. 
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points.  
            
        Returns:
            The variable rank_points.
        
        """
        rank_points = 0
        if position == "QB":
            rank_points += 2
            
        elif position == "RB":
            rank_points += 4
            
        elif position == "WR":
            rank_points += 3
            
        elif position == "TE":
            rank_points += 2
            
        return rank_points 
    
    def last_season_stats(self, player_name):
        """This method will categorize the players stats and 
        add or take away points to the players value. 
        
        Args: 
            self (Rank): A player object that contains the attributes of a players.
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points. 
            
        Returns:
            The variable rank_points.
            
        """
        rank_points = 0
        player = self.roster[player_name]
        #passing yards
        if player["passing"]["passing_yds"] <=500:
            rank_points += 0
        elif player["passing"]["passing_yds"] > 500 and player["passing"]["passing_yds"] <= 1000:
            rank_points += 1
        elif player["passing"]["passing_yds"] > 1000 and player["passing"]["passing_yds"] <= 1500:
            rank_points += 2
        elif player["passing"]["passing_yds"] > 1500 and player["passing"]["passing_yds"] <= 2000:
            rank_points += 3
        elif player["passing"]["passing_yds"] > 2000 and player["passing"]["passing_yds"] <= 2500:
            rank_points += 4
        elif player["passing"]["passing_yds"] > 2500 and player["passing"]["passing_yds"] <= 3000:
            rank_points += 5
        elif player["passing"]["passing_yds"] > 3000 and player["passing"]["passing_yds"] <= 3500:
            rank_points += 6
        elif player["passing"]["passing_yds"] > 3500 and player["passing"]["passing_yds"] <= 4000:
            rank_points += 7
        elif player["passing"]["passing_yds"] > 4000 and player["passing"]["passing_yds"] <= 4500:
            rank_points += 8
        elif player["passing"]["passing_yds"] > 4500 and player["passing"]["passing_yds"]<= 5000:
            rank_points += 9
        elif player["passing"]["passing_yds"] >= 5000:
            rank_points += 10

        #passing touchdowns
        if player["passing"]["passing_td"] <= 5:
            rank_points += 0
        elif player["passing"]["passing_td"] > 5 and player["passing"]["passing_td"] <= 10:
            rank_points += 1
        elif player["passing"]["passing_td"] > 10 and player["passing"]["passing_td"] <= 15:
            rank_points += 2
        elif player["passing"]["passing_td"] > 15 and player["passing"]["passing_td"] <= 20:
            rank_points += 3
        elif player["passing"]["passing_td"] > 20 and player["passing"]["passing_td"] <= 25:
            rank_points += 4
        elif player["passing"]["passing_td"] > 25 and player["passing"]["passing_td"] <= 30:
            rank_points += 5
        elif player["passing"]["passing_td"] >= 30:
            rank_points += 6
        
        rushing_points = 0
        
        #rushing yards 
        if player["rushing"]["rushing_yds"] <= 200:
            rushing_points += 1 
        elif player["rushing"]["rushing_yds"] > 200 and player["rushing"]["rushing_yds"] <= 400:
            rushing_points += 2
        elif player["rushing"]["rushing_yds"] > 400 and player["rushing"]["rushing_yds"] <= 600:
            rushing_points += 3
        elif player["rushing"]["rushing_yds"] > 600 and player["rushing"]["rushing_yds"] <= 800:
            rushing_points += 4
        elif player["rushing"]["rushing_yds"] > 800 and player["rushing"]["rushing_yds"]<= 1000:
            rushing_points += 5
        elif player["rushing"]["rushing_yds"] > 1000 and player["rushing"]["rushing_yds"] <= 1200:
            rushing_points += 6
        elif player["rushing"]["rushing_yds"] > 1200 and player["rushing"]["rushing_yds"] <= 1400:
            rushing_points += 7
        elif player["rushing"]["rushing_yds"] > 1400 and player["rushing"]["rushing_yds"] <= 1600:
            rushing_points += 8
        elif player["rushing"]["rushing_yds"] > 1600 and player["rushing"]["rushing_yds"] <= 1800:
            rushing_points += 9
        elif player["rushing"]["rushing_yds"] > 1800 and player["rushing"]["rushing_yds"] <= 2000:
            rushing_points += 10
        
        #extra value for qb rushing yards
        if player["position"] == "QB":
            rank_points += rushing_points * 1.2
        else:
            rank_points += rushing_points
        
        rushing_td = 0
        
        #rushing touchdown
        if player["rushing"]["rushing_td"] <= 3:
            rushing_td += 1
        elif player["rushing"]["rushing_td"] > 3 and player["rushing"]["rushing_td"] <= 6:
            rushing_td += 2
        elif player["rushing"]["rushing_td"] > 6 and player["rushing"]["rushing_td"] <= 9:
            rushing_td += 3
        elif player["rushing"]["rushing_td"] > 9 and player["rushing"]["rushing_td"] <= 12:
            rushing_td += 4
        elif player["rushing"]["rushing_td"] > 12 and player["rushing"]["rushing_td"] <= 15:
            rushing_td += 5
        elif player["rushing"]["rushing_td"] >= 16:
            rushing_td += 6
        
        #extra value for qb rushing touchdowns
        if player["position"] == "QB":
            rank_points += rushing_td * 1.2
        else:
            rank_points += rushing_td
        
        recieving_yards = 0
        
        #receiving yards
        if player["receiving"]["receiving_yds"] <= 180:
            recieving_yards += 1
        elif player["receiving"]["receiving_yds"] > 180 and player["receiving"]["receiving_yds"] <= 360:
            recieving_yards += 2
        elif player["receiving"]["receiving_yds"] > 360 and player["receiving"]["receiving_yds"] <= 540:
            recieving_yards += 3
        elif player["receiving"]["receiving_yds"] > 540 and player["receiving"]["receiving_yds"] <= 720:
            recieving_yards += 4
        elif player["receiving"]["receiving_yds"] > 720 and player["receiving"]["receiving_yds"] <= 900:
            recieving_yards += 5
        elif player["receiving"]["receiving_yds"] > 900 and player["receiving"]["receiving_yds"] <= 1080:
            recieving_yards += 6
        elif player["receiving"]["receiving_yds"] > 1080 and player["receiving"]["receiving_yds"] <= 1260:
            recieving_yards += 7
        elif player["receiving"]["receiving_yds"] > 1260 and player["receiving"]["receiving_yds"] <= 1440:
            recieving_yards += 8
        elif player["receiving"]["receiving_yds"] > 1440 and player["receiving"]["receiving_yds"] <= 1620:
            recieving_yards += 9
        elif player["receiving"]["receiving_yds"] > 1620 and player["receiving"]["receiving_yds"] <= 1800:
            recieving_yards += 10
        
        #extra value for qb receiving yards
        if player["position"] == "RB":
            rank_points += recieving_yards * 1.2
        else:
            rank_points += recieving_yards
        
        recieving_touchdowns = 0
        
        #receiving touchdowns
        if player["receiving"]["receiving_td"] <= 2:
            recieving_touchdowns += 1
        elif player["receiving"]["receiving_td"] > 2 and player["receiving"]["receiving_td"] <= 4:
            recieving_touchdowns += 2
        elif player["receiving"]["receiving_td"] > 4 and player["receiving"]["receiving_td"] <= 6:
            recieving_touchdowns += 3
        elif player["receiving"]["receiving_td"] > 6 and player["receiving"]["receiving_td"] <= 8:
            recieving_touchdowns += 4
        elif player["receiving"]["receiving_td"] > 8 and player["receiving"]["receiving_td"] <= 10:
            recieving_touchdowns += 5
        elif player["receiving"]["receiving_td"] > 10:
            recieving_touchdowns += 6
        
        #extra value for RB receiving yards
        if player["position"] == "RB":
            rank_points += recieving_touchdowns * 1.2
        else:
            rank_points += recieving_touchdowns
        
        #fumbles
        if player["fumbles"] <= 3:
            rank_points -= 0
        elif player["fumbles"] > 3 and player["fumbles"] <= 6:
            rank_points -= 1
        elif player["fumbles"] > 6 and player["fumbles"] <= 9:
            rank_points -= 2
        elif player["fumbles"] > 9 and player["fumbles"] <= 12:
            rank_points -= 3
        elif player["fumbles"] > 12:
            rank_points -= 4
            

        interception_points = 0 

        if player["passing"]["int"] <= 5:
            interception_points += 0
        elif player["passing"]["int"] > 5 and player["passing"]["int"] <= 10:
            interception_points += 2
        elif player["passing"]["int"] > 10 and player["passing"]["int"] <= 15:
            interception_points += 4
        elif player["passing"]["int"] > 15 and player["passing"]["int"] <= 20:
            interception_points += 6
        elif player["passing"]["int"] > 20 and player["passing"]["int"] <= 25:
            interception_points += 8
        elif player["passing"]["int"] > 25 and player["passing"]["int"] <= 30:
            interception_points += 50
        elif player["passing"]["int"] > 30:
            interception_points += 50

        rank_points -= interception_points
        rank_points += self.position_points(player["position"])
        
        return rank_points        

        
    #Navigator: Rachel Driver: Sakib 
    def rank(self):
        """Append the players to a list of players from most points to
        least points.
        
        Args:
            self (Rank): A player object that contains the attributes of a players.
        
        Returns:
            The variable rank_points.
            A dictionary containing the players name and their rank points.
    
        """
        ranked_dictionary = last_season_stats(self)
        
        sorted_dictionary = dict(sorted(ranked_dictionary.items(), key=operator.itemgetter(1),reverse=True))
        
        return sorted_dictionary

def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    rank = Rank(df)
    print(rank.roster)

if __name__ == "__main__":
    main()

