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

#The ids of the pieces go from 1 to 32. This dictionary identifies the piece type based on the id as well as its color
pieces_id = { 1:("king",'w'), 2:("queen", 'w'), 3:("knight", "w"), 4:("knight", "w"), 5:("rook", "w"), 6:("rook", "w"),...
             7:("bishop", "w"), 8:("bishop", "w"), 9:("pawn", "w"), 10:("pawn", "w"), 11:("pawn", "w"), 12:("pawn", "w"),...
             13:("pawn", "w"), 14:("pawn", "w"), 15:("pawn", "w"), 16:("pawn", "w"),...
             17:("king",'b'), 18:("queen", 'b'), 19:("knight", "b"), 20:("knight", "b"), 21:("rook", "b"), 22:("rook", "b"),...
             23:("bishop", "b"), 24:("bishop", "b"), 25:("pawn", "b"), 26:("pawn", "b"), 27:("pawn", "b"), 28:("pawn", "b"),...
             29:("pawn", "b"), 30:("pawn", "b"), 31:("pawn", "b"), 32:("pawn", "b")}


