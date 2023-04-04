#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:22:06 2023

@author: steverl
"""

positions=[' ' for x in range(1,10)]
available=[x for x in range(1,10)]

def display(row1,row2,row3):
    '''
    Displays the board based on the rows 1, 2, and 3
    '''
    print('{}\n{}\n{}'.format(row1,row2,row3))
    
def display_positions():
    '''
    Displays the possible positions
    '''
    display(["1","2","3"],["4","5","6"],["7","8","9"])

def checkWin(available,positions):
    '''
    Checks to see if a tic tac toe win was accomplished
    '''
    wins=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in wins:
        if (win[0] not in available) and (win[1] not in available) and (win[2] not in available) and (positions[win[0]]==positions[win[1]]) and (positions[win[0]]==positions[win[2]]):
            return True 
    return False

def add_to_board(available,positions,posToAdd,shape):
    '''
    Adds the requested position to the board, which was already verified to be free
    '''
    available.remove(int(posToAdd)) 
    positions[int(posToAdd)-1]=shape
    display(positions[0:3],positions[3:6],positions[6:9])
    return available, positions

def ask(available,positions):
    '''
    Asks the user for the next position and which shape
    '''
    if available==None:
        print("Game Ended")
        display(positions[0:3],positions[3:6],positions[6:9])
        return "End","End"
    elif checkWin(available,positions):
        print("Game Ended")
        display(positions[0:3],positions[3:6],positions[6:9])
        return "End","End"
    else:
        accept_str=[str(x) for x in available]
        shapes=["X","O"]
        print("The available positions are {}".format(available))
        userIn=input("Enter a position: ")
        while userIn not in accept_str:
            print("Invalid position.")
            userIn=input("Enter a position: ")
        print("The possible shapes are X or O.")
        shapeIn=input("Input a shape: ")
        while shapeIn not in shapes:
            print("Invalid shape.")
            shapeIn=input("Enter a shape: ")
        return userIn, shapeIn
    
def first_ask(available,positions):
    '''
    Gives the original positions to choose from and gets original input
    '''
    print("Here are the possible positions: ")
    display_positions()
    userIn, shapeIn = ask(available,positions)
    return userIn, shapeIn

pos,shape=first_ask(available,positions)
while pos!="End":
    available,positions=add_to_board(available, positions, pos, shape)
    #print(available)
    #print(positions)
    pos,shape=ask(available,positions)
    
