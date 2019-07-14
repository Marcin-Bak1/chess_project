# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:16:04 2019

@author: Marcin Bak

This is the main file that initialises and continues the game
"""


import numpy as np
import matplotlib.pyplot as plt
#Initialization of the game

board = np.zeors((8, 8)) #This variable will store the positions of the pieces on the board
pieces_out = [] #This variable will store ids of pieces which were taken out

#This is an old version of the database
#The ids of the pieces go from 1 to 32. This dictionary identifies the piece type based on the id as well as its color
# =============================================================================
# pieces_id = { 1:("king",'w'), 2:("queen", 'w'), 3:("knight", "w"), 4:("knight", "w"), 5:("rook", "w"), 6:("rook", "w"),...
#              7:("bishop", "w"), 8:("bishop", "w"), 9:("pawn", "w"), 10:("pawn", "w"), 11:("pawn", "w"), 12:("pawn", "w"),...
#              13:("pawn", "w"), 14:("pawn", "w"), 15:("pawn", "w"), 16:("pawn", "w"),...
#              17:("king",'b'), 18:("queen", 'b'), 19:("knight", "b"), 20:("knight", "b"), 21:("rook", "b"), 22:("rook", "b"),...
#              23:("bishop", "b"), 24:("bishop", "b"), 25:("pawn", "b"), 26:("pawn", "b"), 27:("pawn", "b"), 28:("pawn", "b"),...
#              29:("pawn", "b"), 30:("pawn", "b"), 31:("pawn", "b"), 32:("pawn", "b")}
# =============================================================================

#New version of the pieces dictionary. To contain less information if the number is odd it is black, if the number is even the piece is white
pieces_id = { 1:"king", 3:"queen", 5:"knight", 7:"knight", 9:"rook", 11:"rook",...
             13:"bishop", 15:"bishop", 17:"pawn", 19:"pawn", 21:"pawn", 23:"pawn",...
             25:"pawn", 27:"pawn", 29:"pawn", 31:"pawn",...
             2:"king", 4:"queen", 6:"knight", 8:"knight", 10:"rook", 12:"rook",...
             14:"bishop", 16:"bishop", 18:"pawn", 20:"pawn", 22:"pawn", 24:"pawn",...
             26:"pawn", 28:"pawn", 30:"pawn", 32:"pawn"}



#Here the board is initialised before the game

board = [
        [9 , 5 , 13, 3 , 1 , 15, 7 , 11]
        [17, 19, 21, 23, 25, 27, 29, 31]
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
        [18, 20, 22, 24, 26, 28, 30, 32]
        [10, 6 , 14, 4 , 2 , 16, 8 , 12]
        ]

game = 1

while game == 1:
    
    #Here goes the main game
    
    #put some user "interface here"
    