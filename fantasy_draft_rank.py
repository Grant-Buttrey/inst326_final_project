"""
This is a script for creating an NFL fantasy draft ranking system. 
"""

import re

def players(player_file):
    player_dict = {}
    
    player_stats = player_file.split("}\n")
    
    player_name_pattern = r'player_name":"(\w+\s+\w+)'
    player_position_pattern = r'position":"(\w+)'
    passing_td_pattern = r'passing_td":(\d+.\d+)'
    passing_yd_pattern = r'passing_yds":(\d+.\d+)'
    fumbles_lost_pattern = r'fumbles_lost":(\d+.\d+)'
    receiving_td_pattern = r'receiving_td":(\d+.\d+)'
    receiving_yd_pattern = r'receiving_yds":(\d+.\d+)'
    rushing_td_pattern = r'rushing_td":(\d+.\d+)'
    rushing_yd_pattern = r'rushing_yds":(\d+.\d+)'        

    for player in player_stats:
        
        player_name = re.findall(player_name_pattern, player)
        player_position = re.findall(player_position_pattern, player)
        passing_td = re.findall(passing_td_pattern, player)
        passing_yd = re.findall(passing_yd_pattern, player)
        receiving_td = re.findall(receiving_td_pattern, player)
        receiving_yd = re.findall(receiving_yd_pattern, player)
        rushing_yd = re.findall(rushing_yd_pattern, player)
        rushing_td = re.findall(rushing_td_pattern, player)
        fumbles_lost = re.findall(fumbles_lost_pattern, player)
        
        player_info = (player_position, passing_td, passing_yd, receiving_td, receiving_yd, rushing_td, rushing_yd, fumbles_lost)
        
        player_dict[player_name] = player_info
        
        return player_dict

class Rank():
    pass
    

def second(tup):
    """
    This method is for returning the last member of a tuple
    
    Parameters:
        tup(tuple): A tuple of two elements, the second of which is an integer
    """
    return tup[-1]
    
def draft_round(player_dict):
    unsorted_ranks = list()
    
    for player in player_dict.keys:
        unsorted_ranks.append(player,player_dict[player])
    
    sorted_ranks = sorted(unsorted_ranks, key=second , reverse=True)
    
    draft_dict = dict()
    
<<<<<<< HEAD
class Draft_Round():
    
def main():
    
if __name__ == "__main__":
    
=======
    for index in range(len(sorted_ranks)):
        if((index/8)+1 in draft_dict.keys()):
            draft_dict[(index/8)+1].append(sorted_ranks[index][0])
        else:
            draft_dict[(index/8)+1] = list(sorted_ranks[index][0])
            
    return draft_dict
>>>>>>> 78db6376c0b8346641cadda51e5b183c86867441
