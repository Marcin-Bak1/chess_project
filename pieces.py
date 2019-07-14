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
    

class rook:
    """This class defines properties and functions of the rook piece. This includes movement patterns and exceptions"""
    
    def ___init___(self, x, y, side, id_no):
        self.posx = x
        self.posy = y
        self.color = side
        board[x][y] = id_no
        
    def move(self, newpos):
        """This is a method of the rook class, takes a tuple in a form (x,y) to define a move"""
        
        validity = 1;
        xo = self.posx
        yo = self.posy
        xn = newpos[0]
        yn = newpos[1]
        #Expose trivial non movement
        if xn == xo and yn == yo:
            validity = 0
        
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
            #Now that the move has been checked to be valid
                            
                            
                            
                            
                            
                            
                            
                            