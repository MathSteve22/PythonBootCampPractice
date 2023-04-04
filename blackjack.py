#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Implementation of the game BlackJack as a course project for "Zero to Hero in Python" bootcamp on Udemy

This version assumes player and dealer can only hit and stand
"""

# First import the random library for shuffling
import random


# Global variables for classifying cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Start with a class in order to work with individual cards in the game
class Card:
    
    # initialize with the suit and number/face
    def __init__(self,suit,rank):
        self.suit=suit 
        self.rank=rank
        self.value=values[rank] # value gives us the rank
        
    def __str__(self):
        return self.rank + " of " + self.suit # use for printing

# Next make a class that represents the deck of cards
class Deck:
    
    # initialize with all of the cards not shuffled
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    # function to shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    # function to give one card
    # watch out for error handling
    def deal_one(self):
        return self.all_cards.pop()

# Class to represent the card holder - either player or dealer
class Holder:
    
    # initialized with cards in hand
    def __init__(self,name):
        self.name=name 
        self.cards=[]
        self.value=0 # Particularly concerned on the value, which is the sum
        self.aces=0 # Count the number of aces - may be more technically, but number of "extra" aces
        self.bank=0
    
    # method to adjust for aces from the rules of Blackjack
    def ace_adjust(self):
        while self.aces>0 and self.value>21:
            self.value-=10
            self.aces-=1    
    
    # method to add a card
    def hit(self,new_card,display=False):
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1
        self.ace_adjust()
        if display==True: 
            print(f"Your current hand holds {self.value} with {self.aces} extra aces.")
        
# function to get input of hit or stand
def ask():
    # use list for possible values
    possible=["Hit","hit","Stand","stand"]
    # ask for input
    result=input("Hit or stand? ")
    # deal with improper input
    while True:
        # if did not input correctly
        if result not in possible:
            # error message and ask again
            print("Error in input. Please use Hit or stand (no space)")
            result=input("Hit or stand? ")
            continue 
        # break if input was good
        else:
            break 
    return result

# function to change money in the bank
def add_bank(player,add_amt):
    player.bank+=add_amt
    return player
    
# function to request money in the bank
def req_bank(player):
    # get initial request
    result=input("How much money are you starting with? ")
    while result.isdigit()==False:
        print("Error in input. Please enter a positive whole number or zero.")
        result=input("How much money are you starting with? ")
    player=add_bank(player,int(result))
    return player

# function to get wager based on bank
def get_wager(player):
    
    result=input("How much would you like to wager for this round? Enter zero to end.")
    while result not in [str(num) for num in range(0,player.bank+1)]:
        print("Error in input. Please enter a positive whole number or zero that is smaller than what is in the bank. ")
        result=input("How much would you like to wager for this round? Enter zero to end. ")
    player=add_bank(player,-int(result))
    return player,int(result)

# if you are running this and not importing
if __name__=="__main__":
    
    # Start with the deck shuffled and the dealer and player
    player = Holder("Player")
    dealer = Holder("Dealer")
    deck = Deck()
    deck.shuffle()
    
    # Next welcome player
    print("Welcome Player to Basic BlackJack.")
    print("Throughout the game, the term 'extra ace' will refer to aces whose value is taken to be 11 rather than 1")
    player=req_bank(player) # get initial bank
    
    player,wager = get_wager(player)
    
    while wager>0:
        
    
        # Deal initial hand
        print("Now dealing in the player and dealer.")
        dealer.hit(deck.deal_one())
        dealer.hit(deck.deal_one())
        player.hit(deck.deal_one())
        player.hit(deck.deal_one(),display=True)
    
        # set counter
        lose=False 
    
        # ask for input
        playerInput=ask().lower()
        playContinue=(playerInput=="hit")
    
        # Player's turn
        while playContinue == True:
            player.hit(deck.deal_one(),display=True)
            # see if we went over
            if player.value>21:
                lose=True
                print("Sorry, you lost!")
                break 
            # see if didn't go over
            else:
                lose=False # didn't lose
                print(f"Your score is {player.value}")
                playerInput=ask().lower() # see if they want to continue
                playContinue=(playerInput=="hit")
                continue
    
        # Dealer's turn
        dealLose=False
        # loop with breaking if the dealer goes over or if dealer score is larger
        while lose==False and dealLose==False and player.value>=dealer.value:
            dealer.hit(deck.deal_one()) # deal to dealer
            if dealer.value>21: # if go over, dealer loses
                dealLose=True 
                print("Dealer went over!")
                break 
            else: # if dealer does not go over, continue
                dealLose=False
                print(f"Dealer score is {dealer.value}")
                continue 
    
        # possible cases - incorporate which one is larger and whether one of them failed
        if dealer.value<=player.value and lose==False:
            print("Player won!")
            player=add_bank(player,2*wager)
        elif dealLose:
            print("Player won!")
            player=add_bank(player,2*wager)
        elif lose:
            print("Dealer won!")
        else:
            print("Dealer won!")
        print(f"You have {player.bank} in the bank.")
        player,wager = get_wager(player)
    print("Thank you for playing!")