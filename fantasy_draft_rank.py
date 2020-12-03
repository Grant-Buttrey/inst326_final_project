"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re
import requests 
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
        
    """
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
        
    def player_stats(player_api):
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
    
class Rank():
    """This class will rank the players from best to worst based on their 
    statistics from the 2019 season.
    
    """
    
    def __init__(self, player_instance):
        self.player_stats = Player.player_stats(player_instance)
        self.rank_points = 0
               
    def position_points(self):
        """This method will find out what the position is 
        and add or take away points to the players value.
        
        Args:
            self (Rank): A player object that contains the attributes of a players. 
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points.  
            
        Returns:
            The variable rank_points.
        
        """
        if self.player_stats[1] == "QB":
            self.rank_points += 2
            
        elif self.player_stats[1] == "RB":
            self.rank_points += 4
            
        elif self.player_stats[1] == "WR":
            self.rank_points += 3
            
        elif self.player_stats[1] == "TE":
            self.rank_points += 2
            
        return self.rank_points 
    
    def last_season_stats(self):
        """This method will categorize the players stats and 
        add or take away points to the players value. 
        
        Args: 
            self (Rank): A player object that contains the attributes of a players.
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points. 
            
        Returns:
            The variable rank_points.
            
        """
        
        
        #passing yards
        if self.player_stats[2] <=500:
            self.rank_points += 0
        elif self.player_stats[2] > 500 and self.player_stats[2] <= 1000:
            self.rank_points += 1
        elif self.player_stats[2] > 1000 and self.player_stats[2] <= 1500:
            self.rank_points += 2
        elif self.player_stats[2] > 1500 and self.player_stats[2] <= 2000:
            self.rank_points += 3
        elif self.player_stats[2] > 2000 and self.player_stats[2] <= 2500:
            self.rank_points += 4
        elif self.player_stats[2] > 2500 and self.player_stats[2] <= 3000:
            self.rank_points += 5
        elif self.player_stats[2] > 3000 and self.player_stats[2] <= 3500:
            self.rank_points += 6
        elif self.player_stats[2] > 3500 and self.player_stats[2] <= 4000:
            self.rank_points += 7
        elif self.player_stats[2] > 4000 and self.player_stats[2] <= 4500:
            self.rank_points += 8
        elif self.player_stats[2] > 4500 and self.player_stats[2] <= 5000:
            self.rank_points += 9
        elif self.player_stats[2] >= 5000:
            self.rank_points += 10

        #passing touchdowns
        if self.player_stats[3] <= 5:
            self.rank_points += 0
        elif self.player_stats[3] > 5 and self.player_stats[3] <= 10:
            self.rank_points += 1
        elif self.player_stats[3] > 10 and self.player_stats[3] <= 15:
            self.rank_points += 2
        elif self.player_stats[3] > 15 and self.player_stats[3] <= 20:
            self.rank_points += 3
        elif self.player_stats[3] > 20 and self.player_stats[3] <= 25:
            self.rank_points += 4
        elif self.player_stats[3] > 25 and self.player_stats[3] <= 30:
            self.rank_points += 5
        elif self.player_stats[3] >= 30:
            self.rank_points += 6
        
        rushing_points = 0
        
        #rushing yards 
        if self.player_stats[6] <= 200:
            rushing_points += 1 
        elif self.player_stats[6] > 200 and self.player_stats[4] <= 400:
            rushing_points += 2
        elif self.player_stats[6] > 400 and self.player_stats[4] <= 600:
            rushing_points += 3
        elif self.player_stats[6] > 600 and self.player_stats[4] <= 800:
            rushing_points += 4
        elif self.player_stats[6] > 800 and self.player_stats[4] <= 1000:
            rushing_points += 5
        elif self.player_stats[6] > 1000 and self.player_stats[4] <= 1200:
            rushing_points += 6
        elif self.player_stats[6] > 1200 and self.player_stats[4] <= 1400:
            rushing_points += 7
        elif self.player_stats[6] > 1400 and self.player_stats[4] <= 1600:
            rushing_points += 8
        elif self.player_stats[6] > 1600 and self.player_stats[4] <= 1800:
            rushing_points += 9
        elif self.player_stats[6] > 1800 and self.player_stats[4] <= 2000:
            rushing_points += 10
        
        #extra value for qb rushing yards
        if self.player_stats[1] == "QB":
            self.rank_points += rushing_points * 1.2
        else:
            self.rank_points += rushing_points
        
        rushing_td = 0
        
        #rushing touchdown
        if self.player_stats[7] <= 3:
            rushing_td += 1
        elif self.player_stats[7] > 3 and self.player_stats[7] <= 6:
            rushing_td += 2
        elif self.player_stats[7] > 6 and self.player_stats[7] <= 9:
            rushing_td += 3
        elif self.player_stats[7] > 9 and self.player_stats[7] <= 12:
            rushing_td += 4
        elif self.player_stats[7] > 12 and self.player_stats[7] <= 15:
            rushing_td += 5
        elif self.player_stats[7] >= 16:
            rushing_td += 6
        
        #extra value for qb rushing touchdowns
        if self.player_stats[1] == "QB":
            self.rank_points += rushing_td * 1.2
        else:
            self.rank_points += rushing_td
        
        recieving_yards = 0
        
        #receiving yards
        if self.player_stats[5] <= 180:
            recieving_yards += 1
        elif self.player_stats[5] > 180 and self.player_stats[5] <= 360:
            recieving_yards += 2
        elif self.player_stats[5] > 360 and self.player_stats[5] <= 540:
            recieving_yards += 3
        elif self.player_stats[5] > 540 and self.player_stats[5] <= 720:
            recieving_yards += 4
        elif self.player_stats[5] > 720 and self.player_stats[5] <= 900:
            recieving_yards += 5
        elif self.player_stats[5] > 900 and self.player_stats[5] <= 1080:
            recieving_yards += 6
        elif self.player_stats[5] > 1080 and self.player_stats[5] <= 1260:
            recieving_yards += 7
        elif self.player_stats[5] > 1260 and self.player_stats[5] <= 1440:
            recieving_yards += 8
        elif self.player_stats[5] > 1440 and self.player_stats[5] <= 1620:
            recieving_yards += 9
        elif self.player_stats[5] > 1620 and self.player_stats[5] <= 1800:
            recieving_yards += 10
        
        #extra value for qb receiving yards
        if self.player_stats[1] == "RB":
            self.rank_points += recieving_yards * 1.2
        else:
            self.rank_points += recieving_yards
        
        recieving_touchdowns = 0
        
        #receiving touchdowns
        if self.player_stats[4] <= 2:
            recieving_touchdowns += 1
        elif self.player_stats[4] > 2 and self.player_stats[4] <= 4:
            recieving_touchdowns += 2
        elif self.player_stats[4] > 4 and self.player_stats[4] <= 6:
            recieving_touchdowns += 3
        elif self.player_stats[4] > 6 and self.player_stats[4] <= 8:
            recieving_touchdowns += 4
        elif self.player_stats[4] > 8 and self.player_stats[4] <= 10:
            recieving_touchdowns += 5
        elif self.player_stats[4] > 10:
            recieving_touchdowns += 6
        
        #extra value for RB receiving yards
        if self.player_stats[1] == "RB":
            self.rank_points += recieving_touchdowns * 1.2
        else:
            self.rank_points += recieving_touchdowns
        
        #fumbles
        if self.player_stats[8] <= 3:
            self.rank_points -= 0
        elif self.player_stats[8] > 3 and self.player_stats[8] <= 6:
            self.rank_points -= 1
        elif self.player_stats[8] > 6 and self.player_stats[8] <= 9:
            self.rank_points -= 2
        elif self.player_stats[8] > 9 and self.player_stats[8] <= 12:
            self.rank_points -= 3
        elif self.rank_points[8] > 12:
            self.rank_points -= 4
        
        return self.rank_points
        
    def rank(self):
        """Append the players to a list of players from most points to
        least points.
        
        Args:
            self (Rank): A player object that contains the attributes of a players.
        
        Returns:
            The variable rank_points.
            A dictionary containing the players name and their rank points.
    
        """
        player_rankings = {}
        
        


def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    api = requests.get('https://www.fantasyfootballdatapros.com/api/players/2019/all')
    players = api.json()

if __name__ == "__main__":
