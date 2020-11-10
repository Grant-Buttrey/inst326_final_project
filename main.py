"""
This is a script for creating the draft rounds for players
"""

import re
import sys
import argparse

import player.py
import rank.py
import draft_round.py

def makePlayer(p_text):
    """
    This is a function for going through the text file's entry on a player
    and taking the information needed to transfer that player's data into
    a Player instance to be used later on.
    
    Parameters:
        p_text(String): The data entry on the player split from the main
        text file about all of the players.
        
    Returns:
        (Player): A newly created instance of player reflecting the data
        on the player that was sent in.
    """
    
    #regex for finding player's name
    reg_name = r"(?<=\"player_name\":\").*(?=\",\"position\")"
    regex = re.compile(reg_name)
    p_name = regex.search(p_text).group(0)
    
    #regex for finding player's position
    reg_pos = r"(?<=\"position\":\").*(?=\",\"stats\")"
    regex = re.compile(reg_pos)
    p_pos = regex.search(p_text).group(0)
    
    return Player(p_name, p_pos)


def main(path):
    player_list = list()
    
    p_stats_file = open(path, encoding='utf-8')
    p_stats = p_stats_file.read().split('},{')
    
    #Creates a list of unranked players as Player objects
    for fplay in p_stats:
        player_list.append(makePlayer(fplay))

    ranked_player_list = list()
    
    #Goes through the players and sends their info to the Rank class to 
    #project the points. This returns a tuple of the player's projected points
    #and their Player object, which can later be organized by points from 
    #highest to lowest.
    for fplay in player_list:
        rank_fplay = Rank(fplay)
        
        ranked_player_list.append(rank_fplay.calculateRank(), fplay)
        
    #Sorted ranked player list is sent in and the DraftRound class returns a 
    #dictionary, which holds an integer as a key to denote the round of the
    #draft these players should be chosen. The value is a set that holds the
    #player objects for that specific round.
    draft = DraftRound(ranked_player_list)
    
    #We can later decide what to do with the "draft" variable which holds the
    #dictionary of ranked players in their specific draft rounds
    



if __name__ == "__main__":
    """
    A main function that will parse the user arguments and run the main
    method of this script.
    """
    

    main(parsed_args.path)