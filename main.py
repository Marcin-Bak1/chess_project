# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:16:04 2019

@author: Marcin Bak

This is the main file that initialises and continues the game
"""


import numpy as np
import matplotlib.pyplot as plt
import pieces


            
#Initialization of the game


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
pieces_id = { 1:'king_b', 3:'queen_b', 5:'knight_1b', 7:'knight_2b', 9:'rook_1b', 11:'rook_2b',
             13:'bishop_1b', 15:'bishop_2b', 17:'pawn_1b', 19:'pawn_2b', 21:'pawn_3b', 23:'pawn_4b',\
             25:'pawn_5b', 27:'pawn_6b', 29:'pawn_7b', 31:'pawn_8b',\
             2:'king_w', 4:'queen_w', 6:'knight_1w', 8:'knight_2w', 10:'rook_1w', 12:'rook_2w',\
             14:'bishop_1w', 16:'bishop_2w', 18:'pawn_1w', 20:'pawn_2w', 22:'pawn_3w', 24:'pawn_4w',\
             26:'pawn_5w', 28:'pawn_6w', 30:'pawn_7w', 32:'pawn_8w'}



#Here is how the board will look like (need to initialise it properly by using pieces)

# =============================================================================
# board_example = [
#         [9 , 5 , 13, 3 , 1 , 15, 7 , 11]
#         [17, 19, 21, 23, 25, 27, 29, 31]
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#         [18, 20, 22, 24, 26, 28, 30, 32]
#         [10, 6 , 14, 4 , 2 , 16, 8 , 12]
#         ]
# =============================================================================

board = np.zeros((8,8))
# =============================================================================
# =============================================================================
# Here starts a party mode
# =============================================================================
# =============================================================================

rook_1b = pieces.rook(0, 0, 'black', 9)
rook_2b = pieces.rook(0, 7, 'black', 11)
rook_1w = pieces.rook(7, 0, 'white', 10)
rook_2w = pieces.rook(7, 7, 'white', 12)

#Check invalid moves
rook_1b.move((1,1))
print(board)

# =============================================================================
# =============================================================================
# # Here ends the party mode
# =============================================================================
# =============================================================================



# =============================================================================
# game = 1
# 
# while game == 1:
#     
#     #Here goes the main game
#     
#     #put some user "interface here"
# =============================================================================
    