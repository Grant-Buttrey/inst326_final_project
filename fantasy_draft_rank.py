"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re
import requests 
import operator
<<<<<<< HEAD

=======
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
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
        
<<<<<<< HEAD
        player_stats = requests.get("https://www.fantasyfootballdatapros.com/api/players/2019/all")
        self.player_data = player_stats.json()
        
        
    def player_stats(self):
=======
    def player_stats(self, player_api):
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
        """Creates a list of player instances and appends players statistics to
        the list.
        
        Args:
            player_api (json): The api being read in the main function. 
            
        Return:
            A list of player instances. 
        
        """
<<<<<<< HEAD
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
        for i in range(10):
            player_instances[self.player_data[iterator]["player_name"]] = Player(self.player_data[iterator]["player_name"], self.player_data[iterator]["position"], self.player_data[iterator]['stats']["passing"]["passing_yds"], self.player_data[iterator]['stats']["passing"]["passing_td"], self.player_data[iterator]['stats']["receiving"]["receiving_td"], self.player_data[iterator]['stats']["receiving"]["receiving_yds"]
                                            ,self.player_data[iterator]['stats']["rushing"]["rushing_yds"], self.player_data[iterator]['stats']["rushing"]["rushing_td"], self.player_data[iterator]['fumbles_lost'])
            print(iterator)
            iterator += 1
        
=======
        player_instances = []
    
        for i in player_api:
            player_instances.append(player_api(i["player_name"], i["position"], i['stats']["passing"]["passing_yds"], i['stats']["passing"]["passing_td"], i['stats']["receiving"]["receiving_td"], i['stats']["receiving"]["receiving_yds"]
                                           ,i['stats']["rushing"]["rushing_yds"], i['stats']["rushing"]["rushing_td"], i['fumbles_lost']))
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
        
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
        
<<<<<<< HEAD
    def position_points(self, player):
=======
    #Driver: Sakib Navigator: Grant          
    def position_points(self):
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
        """This method will find out what the position is 
        and add or take away points to the players value.
        
        Args:
            self (Rank): A player object that contains the attributes of a players. 
        
        Side Effects:
            rank_points (int): Modifies the value of rank_points.  
            
        Returns:
            The variable rank_points.
        
        """
<<<<<<< HEAD
        if self.player_stats[player].position == "QB":
            self.rank_points += 2
            
        elif self.player_stats[player].position == "RB":
            self.rank_points += 4
            
        elif self.player_stats[player].position == "WR":
            self.rank_points += 3
            
        elif self.player_stats[player].position == "TE":
=======
        if self.player_stats[1] == "QB":
            self.rank_points += 2
            
        elif self.player_stats[1] == "RB":
            self.rank_points += 4
            
        elif self.player_stats[1] == "WR":
            self.rank_points += 3
            
        elif self.player_stats[1] == "TE":
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
            self.rank_points += 2
            
        return self.rank_points 
    
<<<<<<< HEAD
=======
    #Driver: Grant Navigator: Sakib
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
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
<<<<<<< HEAD
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

=======
        player_dictionary = {}
        
        for player in self.player_stats:
            #passing yards
            if player[2] <=500:
                self.rank_points += 0
            elif player[2] > 500 and player[2] <= 1000:
                self.rank_points += 1
            elif player[2] > 1000 and player[2] <= 1500:
                self.rank_points += 2
            elif player[2] > 1500 and player[2] <= 2000:
                self.rank_points += 3
            elif player[2] > 2000 and player[2] <= 2500:
                self.rank_points += 4
            elif player[2] > 2500 and player[2] <= 3000:
                self.rank_points += 5
            elif player[2] > 3000 and player[2] <= 3500:
                self.rank_points += 6
            elif player[2] > 3500 and player[2] <= 4000:
                self.rank_points += 7
            elif player[2] > 4000 and player[2] <= 4500:
                self.rank_points += 8
            elif player[2] > 4500 and player[2] <= 5000:
                self.rank_points += 9
            elif player[2] >= 5000:
                self.rank_points += 10

            #passing touchdowns
            if player[3] <= 5:
                self.rank_points += 0
            elif player[3] > 5 and player[3] <= 10:
                self.rank_points += 1
            elif player[3] > 10 and player[3] <= 15:
                self.rank_points += 2
            elif player[3] > 15 and player[3] <= 20:
                self.rank_points += 3
            elif player[3] > 20 and player[3] <= 25:
                self.rank_points += 4
            elif player[3] > 25 and player[3] <= 30:
                self.rank_points += 5
            elif player[3] >= 30:
                self.rank_points += 6
            
            rushing_points = 0
            
            #rushing yards 
            if player[6] <= 200:
                rushing_points += 1 
            elif player[6] > 200 and player[4] <= 400:
                rushing_points += 2
            elif player[6] > 400 and player[4] <= 600:
                rushing_points += 3
            elif player[6] > 600 and player[4] <= 800:
                rushing_points += 4
            elif player[6] > 800 and player[4] <= 1000:
                rushing_points += 5
            elif player[6] > 1000 and player[4] <= 1200:
                rushing_points += 6
            elif player[6] > 1200 and player[4] <= 1400:
                rushing_points += 7
            elif player[6] > 1400 and player[4] <= 1600:
                rushing_points += 8
            elif player[6] > 1600 and player[4] <= 1800:
                rushing_points += 9
            elif player[6] > 1800 and player[4] <= 2000:
                rushing_points += 10
            
            #extra value for qb rushing yards
            if player[1] == "QB":
                self.rank_points += rushing_points * 1.2
            else:
                self.rank_points += rushing_points
            
            rushing_td = 0
            
            #rushing touchdown
            if player[7] <= 3:
                rushing_td += 1
            elif player[7] > 3 and player[7] <= 6:
                rushing_td += 2
            elif player[7] > 6 and player[7] <= 9:
                rushing_td += 3
            elif player[7] > 9 and player[7] <= 12:
                rushing_td += 4
            elif player[7] > 12 and player[7] <= 15:
                rushing_td += 5
            elif player[7] >= 16:
                rushing_td += 6
            
            #extra value for qb rushing touchdowns
            if player[1] == "QB":
                self.rank_points += rushing_td * 1.2
            else:
                self.rank_points += rushing_td
            
            recieving_yards = 0
            
            #receiving yards
            if player[5] <= 180:
                recieving_yards += 1
            elif player[5] > 180 and player[5] <= 360:
                recieving_yards += 2
            elif player[5] > 360 and player[5] <= 540:
                recieving_yards += 3
            elif player[5] > 540 and player[5] <= 720:
                recieving_yards += 4
            elif player[5] > 720 and player[5] <= 900:
                recieving_yards += 5
            elif player[5] > 900 and player[5] <= 1080:
                recieving_yards += 6
            elif player[5] > 1080 and player[5] <= 1260:
                recieving_yards += 7
            elif player[5] > 1260 and player[5] <= 1440:
                recieving_yards += 8
            elif player[5] > 1440 and player[5] <= 1620:
                recieving_yards += 9
            elif player[5] > 1620 and player[5] <= 1800:
                recieving_yards += 10
            
            #extra value for qb receiving yards
            if player[1] == "RB":
                self.rank_points += recieving_yards * 1.2
            else:
                self.rank_points += recieving_yards
            
            recieving_touchdowns = 0
            
            #receiving touchdowns
            if player[4] <= 2:
                recieving_touchdowns += 1
            elif player[4] > 2 and self.player_stats[4] <= 4:
                recieving_touchdowns += 2
            elif player[4] > 4 and self.player_stats[4] <= 6:
                recieving_touchdowns += 3
            elif player[4] > 6 and self.player_stats[4] <= 8:
                recieving_touchdowns += 4
            elif player[4] > 8 and self.player_stats[4] <= 10:
                recieving_touchdowns += 5
            elif player[4] > 10:
                recieving_touchdowns += 6
            
            #extra value for RB receiving yards
            if player[1] == "RB":
                self.rank_points += recieving_touchdowns * 1.2
            else:
                self.rank_points += recieving_touchdowns
            
            #fumbles
            if player[8] <= 3:
                self.rank_points -= 0
            elif player[8] > 3 and player[8] <= 6:
                self.rank_points -= 1
            elif player[8] > 6 and player[8] <= 9:
                self.rank_points -= 2
            elif player[8] > 9 and player[8] <= 12:
                self.rank_points -= 3
            elif player[8] > 12:
                self.rank_points -= 4
            
            player_dictionary[player[1]] = self.rank_points
            
        return player_dictionary
        
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
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595

def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    rank = Rank()
    #print(rank.last_season_stats())
    
    
if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    rank = Rank()
>>>>>>> c6f75dae20732850e0228fea94a1a1415e231595
