# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 19:50:46 2019

@author: konta
"""

# This file initialises and keeps the board variable so that it can be transferred between files

import numpy as np

def init_board():
    global board
    board = np.zeros((8,8))

def init_pieces_id():
    
    global pieces_id    
    pieces_id = { 1:'king_b', 3:'queen_b', 5:'knight_1b', 7:'knight_2b', 9:'rook_1b', 11:'rook_2b',
                 13:'bishop_1b', 15:'bishop_2b', 17:'pawn_1b', 19:'pawn_2b', 21:'pawn_3b', 23:'pawn_4b',\
                 25:'pawn_5b', 27:'pawn_6b', 29:'pawn_7b', 31:'pawn_8b',\
                 2:'king_w', 4:'queen_w', 6:'knight_1w', 8:'knight_2w', 10:'rook_1w', 12:'rook_2w',\
                 14:'bishop_1w', 16:'bishop_2w', 18:'pawn_1w', 20:'pawn_2w', 22:'pawn_3w', 24:'pawn_4w',\
                 26:'pawn_5w', 28:'pawn_6w', 30:'pawn_7w', 32:'pawn_8w'}