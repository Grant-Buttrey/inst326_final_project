"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re
import requests
import operator
import pandas as pd
import pprint

class League():
    #Driver: Sakib Navigator: Grant
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
        

class Rank():
    """This class will rank the players from best to worst based on their 
    statistics from the 2019 season.
    """
    
    def __init__(self, df):
        #Driver: Rachel Navigator: William
        self.ranked_league = League(df)
        self.roster = self.ranked_league.player_dict
        self.frame = df
        
        for i in df["player_name"]:
            self.roster[i]["rank_points"] = 0
        #self.rank_points = ranked_league.player_dict[i]["rank_points"]
               
    def position_points(self):                                 #TAKES POSITION AS ARG
        #Driver: William Navigator: Grant
        """This method will find out what the position is 
        and add or take away points to the players value.
        
        Args:
            self (Rank): A player object that contains the attributes of a players. 
        
        Side Effects:
            self.rank_points (int): Modifies the value of self.rank_points.  
            
        Returns:
            The variable self.rank_points.
        
        """
        #self.ranked_league.player_dict[self.player]["rank_points"] = 0
        
        
        for i in self.frame["player_name"]:
            
        
            if self.roster[i]["position"] == "QB":
                self.roster[i]["rank_points"] += 2
                
            elif self.roster[i]["position"] == "RB":
                self.roster[i]["rank_points"] += 9.5
                
            elif self.roster[i]["position"] == "WR":
                self.roster[i]["rank_points"] += 8
                
            elif self.roster[i]["position"] == "TE":
                self.roster[i]["rank_points"] += 5
                
               
        #passing yards
            if self.roster[i]["passing"]["passing_yds"] <=500:
                self.roster[i]["rank_points"] += 0
            
            elif self.roster[i]["passing"]["passing_yds"] > 500 and self.roster[i]["passing"]["passing_yds"] <= 1000:
                self.roster[i]["rank_points"] += 0
            
            elif self.roster[i]["passing"]["passing_yds"] > 1000 and self.roster[i]["passing"]["passing_yds"] <= 1500:
                self.roster[i]["rank_points"] += 0
            
            elif self.roster[i]["passing"]["passing_yds"] > 1500 and self.roster[i]["passing"]["passing_yds"] <= 2000:
                self.roster[i]["rank_points"] += 0
            
            elif self.roster[i]["passing"]["passing_yds"] > 2000 and self.roster[i]["passing"]["passing_yds"] <= 2500:
                self.roster[i]["rank_points"] += 4
            
            elif self.roster[i]["passing"]["passing_yds"] > 2500 and self.roster[i]["passing"]["passing_yds"] <= 3000:
                self.roster[i]["rank_points"] += 5
            
            elif self.roster[i]["passing"]["passing_yds"] > 3000 and self.roster[i]["passing"]["passing_yds"] <= 3500:
                self.roster[i]["rank_points"] += 6
            
            elif self.roster[i]["passing"]["passing_yds"] > 3500 and self.roster[i]["passing"]["passing_yds"] <= 4000:
                self.roster[i]["rank_points"] += 6
            
            elif self.roster[i]["passing"]["passing_yds"] > 4000 and self.roster[i]["passing"]["passing_yds"] <= 4500:
                self.roster[i]["rank_points"] += 7
            
            elif self.roster[i]["passing"]["passing_yds"] > 4500 and self.roster[i]["passing"]["passing_yds"]<= 5000:
                self.roster[i]["rank_points"] += 8
            
            elif self.roster[i]["passing"]["passing_yds"] >= 5000:
                self.roster[i]["rank_points"] += 9
                
                #passing touchdowns
            if self.roster[i]["passing"]["passing_td"] <= 5:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["passing"]["passing_td"] > 5 and self.roster[i]["passing"]["passing_td"] <= 10:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["passing"]["passing_td"] > 10 and self.roster[i]["passing"]["passing_td"] <= 15:
                self.roster[i]["rank_points"] += 3
            elif self.roster[i]["passing"]["passing_td"] > 15 and self.roster[i]["passing"]["passing_td"] <= 20:
                self.roster[i]["rank_points"] += 4
            elif self.roster[i]["passing"]["passing_td"] > 20 and self.roster[i]["passing"]["passing_td"] <= 25:
                self.roster[i]["rank_points"] += 5
            elif self.roster[i]["passing"]["passing_td"] > 25 and self.roster[i]["passing"]["passing_td"] <= 30:
                self.roster[i]["rank_points"] += 6
            elif self.roster[i]["passing"]["passing_td"] >= 30:
                self.roster[i]["rank_points"] += 7
            
                #rushing yards 
            if self.roster[i]["rushing"]["rushing_yds"] <= 200:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["rushing"]["rushing_yds"] > 200 and self.roster[i]["rushing"]["rushing_yds"] <= 400:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["rushing"]["rushing_yds"] > 400 and self.roster[i]["rushing"]["rushing_yds"] <= 600:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["rushing"]["rushing_yds"] > 600 and self.roster[i]["rushing"]["rushing_yds"] <= 800:
                self.roster[i]["rank_points"] += 4
            elif self.roster[i]["rushing"]["rushing_yds"] > 800 and self.roster[i]["rushing"]["rushing_yds"] <= 1000:
                self.roster[i]["rank_points"] += 5
            elif self.roster[i]["rushing"]["rushing_yds"] > 1000 and self.roster[i]["rushing"]["rushing_yds"] <= 1200:
                self.roster[i]["rank_points"] += 6
            elif self.roster[i]["rushing"]["rushing_yds"] > 1200 and self.roster[i]["rushing"]["rushing_yds"] <= 1400:
                self.roster[i]["rank_points"] += 7
            elif self.roster[i]["rushing"]["rushing_yds"] > 1400 and self.roster[i]["rushing"]["rushing_yds"] <= 1600:
                self.roster[i]["rank_points"] += 8
            elif self.roster[i]["rushing"]["rushing_yds"] > 1600 and self.roster[i]["rushing"]["rushing_yds"] <= 1800:
                self.roster[i]["rank_points"] += 9
            elif self.roster[i]["rushing"]["rushing_yds"] > 1800 and self.roster[i]["rushing"]["rushing_yds"] <= 2000:
                self.roster[i]["rank_points"] += 10

            if self.roster[i]["rushing"]["rushing_td"] <= 3:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["rushing"]["rushing_td"] > 3 and self.roster[i]["rushing"]["rushing_td"] <= 6:
                self.roster[i]["rank_points"] += 0
            elif self.roster[i]["rushing"]["rushing_td"] > 6 and self.roster[i]["rushing"]["rushing_td"] <= 9:
                self.roster[i]["rank_points"] += 3
            elif self.roster[i]["rushing"]["rushing_td"] > 9 and self.roster[i]["rushing"]["rushing_td"] <= 12:
                self.roster[i]["rank_points"] += 4
            elif self.roster[i]["rushing"]["rushing_td"] > 12 and self.roster[i]["rushing"]["rushing_td"] <= 15:
                self.roster[i]["rank_points"] += 5
            elif self.roster[i]["rushing"]["rushing_td"] >= 16:
                self.roster[i]["rank_points"] += 6
                
            receiving_yards = 0
                #receiving yards
            if self.roster[i]["receiving"]["receiving_yds"] <= 180:
                receiving_yards += 0
            elif self.roster[i]["receiving"]["receiving_yds"] > 180 and self.roster[i]["receiving"]["receiving_yds"] <= 360:
                receiving_yards += 0
            elif self.roster[i]["receiving"]["receiving_yds"] > 360 and self.roster[i]["receiving"]["receiving_yds"] <= 540:
                receiving_yards += 0
            elif self.roster[i]["receiving"]["receiving_yds"] > 540 and self.roster[i]["receiving"]["receiving_yds"] <= 720:
                receiving_yards += 0
            elif self.roster[i]["receiving"]["receiving_yds"] > 720 and self.roster[i]["receiving"]["receiving_yds"] <= 900:
                receiving_yards += 6
            elif self.roster[i]["receiving"]["receiving_yds"] > 900 and self.roster[i]["receiving"]["receiving_yds"] <= 1080:
                receiving_yards += 7
            elif self.roster[i]["receiving"]["receiving_yds"] > 1080 and self.roster[i]["receiving"]["receiving_yds"] <= 1260:
                receiving_yards += 8
            elif self.roster[i]["receiving"]["receiving_yds"] > 1260 and self.roster[i]["receiving"]["receiving_yds"] <= 1440:
                receiving_yards += 9
            elif self.roster[i]["receiving"]["receiving_yds"] > 1440 and self.roster[i]["receiving"]["receiving_yds"] <= 1620:
                receiving_yards += 10
            elif self.roster[i]["receiving"]["receiving_yds"] > 1620 and self.roster[i]["receiving"]["receiving_yds"] <= 1800:
                receiving_yards += 11
    
            if self.roster[i]["position"] == "TE":
                self.roster[i]["rank_points"] += receiving_yards * 1.2
            else:
                self.roster[i]["rank_points"] += receiving_yards
            
            receiving_touchdowns = 0
                #receiving touchdowns
            if self.roster[i]["receiving"]["receiving_td"] <= 2:
                receiving_touchdowns += 0
            elif self.roster[i]["receiving"]["receiving_td"] > 2 and self.roster[i]["receiving"]["receiving_td"] <= 4:
                receiving_touchdowns += 0
            elif self.roster[i]["receiving"]["receiving_td"] > 4 and self.roster[i]["receiving"]["receiving_td"] <= 6:
                receiving_touchdowns += 4
            elif self.roster[i]["receiving"]["receiving_td"] > 6 and self.roster[i]["receiving"]["receiving_td"] <= 8:
                receiving_touchdowns += 5
            elif self.roster[i]["receiving"]["receiving_td"] > 8 and self.roster[i]["receiving"]["receiving_td"] <= 10:
                receiving_touchdowns += 6
            elif self.roster[i]["receiving"]["receiving_td"] > 10:
                receiving_touchdowns += 7
                
            #extra value for RB receiving yards
            if self.roster[i]["position"] == "TE":
                self.roster[i]["rank_points"] += receiving_touchdowns * 1.2
            else:
                self.roster[i]["rank_points"] += receiving_touchdowns
            
            #fumbles
            if self.roster[i]["fumbles"] <= 3:
                self.roster[i]["rank_points"] -= 0
            elif self.roster[i]["fumbles"] > 3 and self.roster[i]["fumbles"] <= 6:
                self.roster[i]["rank_points"] -= 1
            elif self.roster[i]["fumbles"] > 6 and self.roster[i]["fumbles"] <= 9:
                self.roster[i]["rank_points"] -= 2
            elif self.roster[i]["fumbles"] > 9 and self.roster[i]["fumbles"] <= 12:
                self.roster[i]["rank_points"] -= 3
            elif self.roster[i]["fumbles"] > 12:
                self.roster[i]["rank_points"] -= 4
                
            if self.roster[i]["passing"]["int"] <= 5:
                self.roster[i]["rank_points"] -= 0
            elif self.roster[i]["passing"]["int"] > 5 and self.roster[i]["passing"]["int"] <= 10:
                self.roster[i]["rank_points"] -= 2
            elif self.roster[i]["passing"]["int"] > 10 and self.roster[i]["passing"]["int"] <= 15:
                self.roster[i]["rank_points"] -= 4
            elif self.roster[i]["passing"]["int"] > 15 and self.roster[i]["passing"]["int"] <= 20:
                self.roster[i]["rank_points"] -= 6
            elif self.roster[i]["passing"]["int"] > 20 and self.roster[i]["passing"]["int"] <= 25:
                self.roster[i]["rank_points"] -= 8
            elif self.roster[i]["passing"]["int"] > 25 and self.roster[i]["passing"]["int"] <= 30:
                self.roster[i]["rank_points"] -= 10
            elif self.roster[i]["passing"]["int"] > 30:
                self.roster[i]["rank_points"] -= 12

def main():
    """Reads in the API and sets it equal to a variable called players.
    
    """
    data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
    df = pd.DataFrame(data)
    rank = Rank(df)
    rank.position_points()
    pprint.pprint(rank.roster)
    

if __name__ == "__main__":
    main()

