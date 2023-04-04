#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code is to simulate a game of the card game war, based on what is used in "Zero to Hero in Python" Bootcamp course.
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit 
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck():
    
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player():
    
    def __init__(self,name):
        self.name=name 
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
        
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return "Player {} has {} cards.".format(self.name,len(self.all_cards))
    
if __name__=="__main__":
    player_one=Player("One")
    player_two=Player("Two")
    new_deck=Deck()
    new_deck.shuffle()
    
    for x in range(int(len(new_deck.all_cards)/2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
        
    round_num=0
    while True:
        round_num+=1
        print(f"Round {round_num}")
        
        if len(player_one.all_cards)==0:
            print("Player Two Wins! Player One out.")
            break 
        
        if len(player_two.all_cards)==0:
            print("Player One Wins! Player Two out.")
            break 
        
        play_one_play=[]
        play_one_play.append(player_one.remove_one())
        
        play_two_play=[]
        play_two_play.append(player_two.remove_one())
        
        at_war=True
        
        while at_war:
            if play_one_play[-1].value>play_two_play[-1].value:
                player_one.add_cards(play_one_play)
                player_one.add_cards(play_two_play)
                at_war=False
                break 
            
            elif play_one_play[-1].value<play_two_play[-1].value:
                player_two.add_cards(play_one_play)
                player_two.add_cards(play_two_play)
                at_war=False
                break 
            
            else:
                print("WAR!")
                for count in range(3):
                    try:
                        play_one_play.append(player_one.remove_one())
                    except: 
                        player_one.all_cards=[]
                        at_war=False
                    finally:
                        try:
                            play_one_play.append(player_two.remove_one())
                        except:
                            player_two.all_cards=[]
                            at_war=False
                        else:
                            at_war=True  
            
            
            