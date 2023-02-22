import numpy as np
import time
import heapq

init = [11,5,2,1,14,8,10,0,15,4,13,6,9,12,3,7]

goal = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

# Determines whether the state has been added to the closed list
#
# Input:
# state - Current state of the puzzle
# seenList - The list containing all of the visited states
#
# Output
# True - If the state has been visited before
# False - If the state has not yet been visited
def seenYet( state, seenList ):
    for seenState in seenList:
        if seenState.currentState == state:
            return True
    return False

# Display list as 4 x 4 numpy array
def display( state ):
    print( np.array( state ).reshape( 4, 4 ))

class State:
    def __init__( self, currentState, parent = None, goal = None ):
        self.currentState = currentState
        self.parent = parent

    # Finds all the possible directions the blank piece can move.
    #
    # Output:
    # moves - List type containing possible moves that can be done, e.g. ['D','R','L]     
    def findMoves( self ):

        # Find index of where the blank piece is
        pos = self.currentState.index( 0 )

        # Possible directions
        moves = []

        # For moving up and down
        if pos + 4 <= 15:
            moves.append( 'D' )
        if pos - 4 >= 0:
            moves.append( 'U' )

        # For moving left and right
        if ( pos + 1 ) % 4 == 0 :
            moves.append( 'L' )
        elif pos % 4 == 0 :
            moves.append( 'R' )
        else:
            moves.append( 'L' )
            moves.append( 'R' )

        return( moves )

    # Makes a move on the puzzle, given a direction
    # 
    # Input:
    # move - Direction to move the blank piece e.g. 'U', 'D'
    # 
    # Output:
    # copy - A list type of the new state created from the move
    def makeMove( self, move ):
        copy = self.currentState.copy()
        # Down
        if move == 'D':
            ind = copy.index( 0 )
            copy[ ind ] = copy[ ind + 4]
            copy[ ind + 4] = 0
            return( copy )
        # Up
        if move == 'U':
            ind = copy.index( 0 )
            copy[ ind ] = copy[ ind - 4]
            copy[ ind - 4] = 0
            return( copy )
        # Left
        if move == 'L':
            ind = copy.index( 0 )
            copy[ ind ] = copy[ ind - 1]
            copy[ ind - 1] = 0
            return( copy )
        # Right
        if move == 'R':
            ind = copy.index( 0 )
            copy[ ind ] = copy[ ind + 1]
            copy[ ind + 1] = 0
            return( copy )

    # Finds all neighbors, considering what has already been seen
    #
    # Input:
    # seenList - The closed list
    # 
    # Output:
    # potentialStates - List of states (lists) that have not been added to the closed list yet. 
    def findNeighbors( self, seenList):
        # Find possible directions
        potentialMoves = self.findMoves( )

        potentialStates = []

        # For each possible direction
        for move in potentialMoves:
            # Find state of the move
            potentialState = self.makeMove( move )
            # If the list type has yet to be appended to the closed list
            if not seenYet( potentialState, seenList ):
                potentialStates.append( potentialState )

        return( potentialStates )
        
    # Show the state of the current node
    def display( self ):
        print( np.array( self.currentState ).reshape( 4, 4 ))