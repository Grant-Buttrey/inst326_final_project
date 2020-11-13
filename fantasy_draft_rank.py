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
        
        """
        player_instances = []
    
    for i in players:
        player_instances.append(player_api(i["player_name"], i["position"], i['stats']["passing"]["passing_yds"], i['stats']["passing"]["passing_td"], i['stats']["receiving"]["receiving_td"], i['stats']["receiving"]["receiving_yds"]
                                           ,i['stats']["rushing"]["rushing_yds"], i['stats']["rushing"]["rushing_td"], i['fumbles_lost']))
        
    def __repr__(self):
        """Allows the player instance to be returned as the players name. 
        
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
        """

        
    def last_season_stats(self):
        """This method will categorize the players stats and 
        add or take away points to the players value. 
        
        Args: 
            self (Rank): A player object that contains the attributes of a players.
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points. 
            
        """
        
        
    def rank(self):
        """This method will total all of the points for the player
        and append them to a list of players from most points to
        least points.
        
        Args:
            self (Rank): A player object that contains the attributes of a players.
        
        
        """
    


def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    api = requests.get('https://www.fantasyfootballdatapros.com/api/players/2019/all')
    players = api.json()

if __name__ == "__main__":
    
    
            
    
