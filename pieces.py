# -*- coding: utf-8 -*-
"""
This is a file containing the classes definitions for the individual pieces on the board

"""

############    Remember about the global variable board          #######################

################### Pawn class far more complicated ###########################
# =============================================================================
# class pawn:
#     def __init__(self, x, y, side, id_no):
#         self.posx = x
#         self.posy = y
#         self.color = side
#
# =============================================================================
def general_move(piece, xn, yn):
    global board
    validity = 1
    xo = piece.posx;
    yo = piece.posy;
    if piece.color == 'black' and board[xn][yn] % 2 != 0:
        validity = 0;
    if piece.color == 'white' and board[xn][yn] % 2 == 0:
        validity = 0
        
    if validity == 1:
        self.posx = xn;
        self.posy = yn;
        board[xo][yo] = 0;
        
        
        if board[xn][yn] != 0:
        
            if self.color == 'black' and board[xn][yn] % 2 == 0:
                piece_beat_id = board[xn][yn]
                piece_beat = pieces_id[piece_beat]
                piece_beat.posx = 100;
                piece_beat.posy = 100;
            if self.color == 'white' and board[xn][yn] % 2 != 0:
                piece_beat_id = board[xn][yn]
                piece_beat = pieces_id[piece_beat]
                piece_beat.posx = 100;
                piece_beat.posy = 100;
            board[xn][yn] = piece.id;
    else:
        print("The move is not valid")
        
class rook(object):
    """This class defines properties and functions of the rook piece. This includes movement patterns and exceptions"""
    
    def __init__(self, x, y, side, id_no):
        global board
        self.posx = x
        self.posy = y
        self.color = side
        self.id = id_no
        board[x][y] = id_no
        
    def move(self, newpos):
        """This is a method of the rook class, takes a tuple in a form (x,y) to define a move"""
        
        global board
        global pieces_id
        
        validity = 1;
        xo = self.posx
        yo = self.posy
        xn = newpos[0]
        yn = newpos[1]
        #Expose trivial non movement
        if xn == xo and yn == yo:
            validity = 0
        
        #This is a piece specific validity check
        if xn == xo or yn == yo:
            # Here first criterium is satisfied, now the presence of the other pieces on the way has to be verified
            #Check orientation of the move
            if yn == yo:
                #Check which side of the line needs to be checked
                if xn < xo:
                    for i in range(xn + 1, xo): #Like this due to the nature of the rnage function
                        if board[i][yo] != 0:
                            validity = 0
                if xn > xo:
                    for i in range(xo + 1, xn): #Like this due to the nature of the rnage function
                        if board[i][yo] != 0:
                            validity = 0                            
            if xn == xo:
                #Check which side of the line needs to be checked
                if yn < yo:
                    for j in range(yn + 1, yo): #Like this due to the nature of the rnage function
                        if board[xo][j] != 0:
                            validity = 0
                if yn > yo:
                    for j in range(yo + 1, yn): #Like this due to the nature of the rnage function
                        if board[xo][j] != 0:
                            validity = 0

        if validity == 0:
            print("This move is not valid")
        
        else:
            pieces.general_move(self, xn, yn)
                            
                            
                            
                            