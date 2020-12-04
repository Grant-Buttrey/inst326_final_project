"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re
import requests 
import operator

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
    def __init__(self,player_name = "", position = "", pass_yd = 0, pass_td = 0, receiving_td = 0, receiving_yd = 0, rushing_yd = 0, rushing_td = 0, fumbles = 0):     
        self.name = player_name
        self.position = position
        self.pass_td = pass_td
        self.pass_yd = pass_yd
        self.receiving_td = receiving_td
        self.receiving_yd = receiving_yd
        self.rushing_td = rushing_td
        self.rushing_yd = rushing_yd
        self.fumbles = fumbles
        
        player_stats = requests.get("https://www.fantasyfootballdatapros.com/api/players/2019/all")
        self.player_data = player_stats.json()
        
        
    def player_stats(self):
        """Creates a list of player instances and appends players statistics to
        the list.
        
        Args:
            player_api (json): The api being read in the main function. 
            
        Return:
            A list of player instances. 
        
        """
        player_instances = {}
        iterator = 0
        
        #RUN REGULARLY
        """
        for i in self.player_data:
            player_instances[self.player_data[iterator]["player_name"]] = Player(self.player_data[iterator]["player_name"], self.player_data[iterator]["position"], self.player_data[iterator]['stats']["passing"]["passing_yds"], self.player_data[iterator]['stats']["passing"]["passing_td"], self.player_data[iterator]['stats']["receiving"]["receiving_td"], self.player_data[iterator]['stats']["receiving"]["receiving_yds"]
                                            ,self.player_data[iterator]['stats']["rushing"]["rushing_yds"], self.player_data[iterator]['stats']["rushing"]["rushing_td"], self.player_data[iterator]['fumbles_lost'])
            iterator += 1
        """
        #COMPACT RUN
        for i in range(16):
            player_instances[self.player_data[iterator]["player_name"]] = Player(self.player_data[iterator]["player_name"], self.player_data[iterator]["position"], self.player_data[iterator]['stats']["passing"]["passing_yds"], self.player_data[iterator]['stats']["passing"]["passing_td"], self.player_data[iterator]['stats']["receiving"]["receiving_td"], self.player_data[iterator]['stats']["receiving"]["receiving_yds"]
                                            ,self.player_data[iterator]['stats']["rushing"]["rushing_yds"], self.player_data[iterator]['stats']["rushing"]["rushing_td"], self.player_data[iterator]['fumbles_lost'])
            iterator += 1
        
        
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
    
    def __init__(self):
        player = Player()
        self.player_stats = player.player_stats()
        self.rank_points = 0
        
    def position_points(self, player):
        """This method will find out what the position is 
        and add or take away points to the players value.
        
        Args:
            self (Rank): A player object that contains the attributes of a players. 
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points.  
            
        Returns:
            The variable rank_points.
        
        """
        if self.player_stats[player].position == "QB":
            self.rank_points += 2
            
        elif self.player_stats[player].position == "RB":
            self.rank_points += 4
            
        elif self.player_stats[player].position == "WR":
            self.rank_points += 3
            
        elif self.player_stats[player].position == "TE":
            self.rank_points += 2
            
        return self.rank_points 
    
    #Driver: Grant Navigator: Sakib
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
        # players = requests.get("https://www.fantasyfootballdatapros.com/api/players/2019/all")
        # player_data = players.json()
        # player_instance = Player(player_data)
        
        player_dictionary = dict()
        

        for player in self.player_stats.keys():
            self.rank_points = 0
            #passing yards
            if self.player_stats[player].pass_yd <=500:
                self.rank_points += 0
            elif self.player_stats[player].pass_yd > 500 and self.player_stats[player].pass_yd <= 1000:
                self.rank_points += 1
            elif self.player_stats[player].pass_yd > 1000 and self.player_stats[player].pass_yd <= 1500:
                self.rank_points += 2
            elif self.player_stats[player].pass_yd > 1500 and self.player_stats[player].pass_yd <= 2000:
                self.rank_points += 3
            elif self.player_stats[player].pass_yd > 2000 and self.player_stats[player].pass_yd <= 2500:
                self.rank_points += 4
            elif self.player_stats[player].pass_yd > 2500 and self.player_stats[player].pass_yd <= 3000:
                self.rank_points += 5
            elif self.player_stats[player].pass_yd > 3000 and self.player_stats[player].pass_yd <= 3500:
                self.rank_points += 6
            elif self.player_stats[player].pass_yd > 3500 and self.player_stats[player].pass_yd <= 4000:
                self.rank_points += 7
            elif self.player_stats[player].pass_yd > 4000 and self.player_stats[player].pass_yd <= 4500:
                self.rank_points += 8
            elif self.player_stats[player].pass_yd > 4500 and self.player_stats[player].pass_yd <= 5000:
                self.rank_points += 9
            elif self.player_stats[player].pass_yd >= 5000:
                self.rank_points += 10

            #passing touchdowns
            if self.player_stats[player].pass_td <= 5:
                self.rank_points += 0
            elif self.player_stats[player].pass_td > 5 and self.player_stats[player].pass_td <= 10:
                self.rank_points += 1
            elif self.player_stats[player].pass_td > 10 and self.player_stats[player].pass_td <= 15:
                self.rank_points += 2
            elif self.player_stats[player].pass_td > 15 and self.player_stats[player].pass_td <= 20:
                self.rank_points += 3
            elif self.player_stats[player].pass_td > 20 and self.player_stats[player].pass_td <= 25:
                self.rank_points += 4
            elif self.player_stats[player].pass_td > 25 and self.player_stats[player].pass_td <= 30:
                self.rank_points += 5
            elif self.player_stats[player].pass_td >= 30:
                self.rank_points += 6
            
            rushing_points = 0
            
            #rushing yards 
            if self.player_stats[player].rushing_yd <= 200:
                rushing_points += 1 
            elif self.player_stats[player].rushing_yd > 200 and self.player_stats[player].rushing_yd <= 400:
                rushing_points += 2
            elif self.player_stats[player].rushing_yd and self.player_stats[player].rushing_yd <= 600:
                rushing_points += 3
            elif self.player_stats[player].rushing_yd > 600 and self.player_stats[player].rushing_yd <= 800:
                rushing_points += 4
            elif self.player_stats[player].rushing_yd > 800 and self.player_stats[player].rushing_yd <= 1000:
                rushing_points += 5
            elif self.player_stats[player].rushing_yd > 1000 and self.player_stats[player].rushing_yd <= 1200:
                rushing_points += 6
            elif self.player_stats[player].rushing_yd > 1200 and self.player_stats[player].rushing_yd <= 1400:
                rushing_points += 7
            elif self.player_stats[player].rushing_yd > 1400 and self.player_stats[player].rushing_yd <= 1600:
                rushing_points += 8
            elif self.player_stats[player].rushing_yd > 1600 and self.player_stats[player].rushing_yd <= 1800:
                rushing_points += 9
            elif self.player_stats[player].rushing_yd > 1800 and self.player_stats[player].rushing_yd <= 2000:
                rushing_points += 10
            
            #extra value for qb rushing yards
            if self.player_stats[player].position == "QB":
                self.rank_points += rushing_points * 1.2
            else:
                self.rank_points += rushing_points
            
            rushing_td = 0
            
            #rushing touchdown
            if self.player_stats[player].rushing_td <= 3:
                rushing_td += 1
            elif self.player_stats[player].rushing_td > 3 and self.player_stats[player].rushing_td <= 6:
                rushing_td += 2
            elif self.player_stats[player].rushing_td > 6 and self.player_stats[player].rushing_td <= 9:
                rushing_td += 3
            elif self.player_stats[player].rushing_td > 9 and self.player_stats[player].rushing_td <= 12:
                rushing_td += 4
            elif self.player_stats[player].rushing_td > 12 and self.player_stats[player].rushing_td <= 15:
                rushing_td += 5
            elif self.player_stats[player].rushing_td >= 16:
                rushing_td += 6
            
            #extra value for qb rushing touchdowns
            if self.player_stats[player].position == "QB":
                self.rank_points += rushing_td * 1.2
            else:
                self.rank_points += rushing_td
            
            recieving_yards = 0
            
            #receiving yards
            if self.player_stats[player].receiving_yd <= 180:
                recieving_yards += 1
            elif self.player_stats[player].receiving_yd > 180 and self.player_stats[player].receiving_yd <= 360:
                recieving_yards += 2
            elif self.player_stats[player].receiving_yd > 360 and self.player_stats[player].receiving_yd <= 540:
                recieving_yards += 3
            elif self.player_stats[player].receiving_yd > 540 and self.player_stats[player].receiving_yd <= 720:
                recieving_yards += 4
            elif self.player_stats[player].receiving_yd > 720 and self.player_stats[player].receiving_yd <= 900:
                recieving_yards += 5
            elif self.player_stats[player].receiving_yd > 900 and self.player_stats[player].receiving_yd <= 1080:
                recieving_yards += 6
            elif self.player_stats[player].receiving_yd > 1080 and self.player_stats[player].receiving_yd <= 1260:
                recieving_yards += 7
            elif self.player_stats[player].receiving_yd > 1260 and self.player_stats[player].receiving_yd <= 1440:
                recieving_yards += 8
            elif self.player_stats[player].receiving_yd > 1440 and self.player_stats[player].receiving_yd <= 1620:
                recieving_yards += 9
            elif self.player_stats[player].receiving_yd > 1620 and self.player_stats[player].receiving_yd <= 1800:
                recieving_yards += 10
            
            #extra value for qb receiving yards
            if self.player_stats[player].position == "RB":
                self.rank_points += recieving_yards * 1.2
            else:
                self.rank_points += recieving_yards
            
            recieving_touchdowns = 0
            
            #receiving touchdowns
            if self.player_stats[player].receiving_td <= 2:
                recieving_touchdowns += 1
            elif self.player_stats[player].receiving_td > 2 and self.player_stats[player].receiving_td <= 4:
                recieving_touchdowns += 2
            elif self.player_stats[player].receiving_td > 4 and self.player_stats[player].receiving_td <= 6:
                recieving_touchdowns += 3
            elif self.player_stats[player].receiving_td > 6 and self.player_stats[player].receiving_td <= 8:
                recieving_touchdowns += 4
            elif self.player_stats[player].receiving_td > 8 and self.player_stats[player].receiving_td <= 10:
                recieving_touchdowns += 5
            elif self.player_stats[player].receiving_td > 10:
                recieving_touchdowns += 6
            
            #extra value for RB receiving yards
            if self.player_stats[player].position == "RB":
                self.rank_points += recieving_touchdowns * 1.2
            else:
                self.rank_points += recieving_touchdowns
            
            #fumbles
            if self.player_stats[player].fumbles <= 3:
                self.rank_points -= 0
            elif self.player_stats[player].fumbles > 3 and self.player_stats[player].fumbles <= 6:
                self.rank_points -= 1
            elif self.player_stats[player].fumbles > 6 and self.player_stats[player].fumbles <= 9:
                self.rank_points -= 2
            elif self.player_stats[player].fumbles > 9 and self.player_stats[player].fumbles <= 12:
                self.rank_points -= 3
            elif self.player_stats[player].fumbles > 12:
                self.rank_points -= 4
            
            self.rank_points += self.position_points(player)
            
            player_dictionary[self.player_stats[player]] = self.rank_points
            
        return player_dictionary


def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    rank = Rank()
    print(rank.last_season_stats())
    
    
if __name__ == "__main__":
    main()
