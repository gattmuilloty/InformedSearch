from game import *

# Start the time
et = time.time()

file1 = open("solution_H3.txt","w")

# Created to allow the heapq functions to work properly.
# This will allow the states to be compared based off their total number of incorrect adjacent pairs
def __lt__( self, other ):
    return self.directTileReversals() < other.directTileReversals()

# Counts the number of direct adjacent tile reversals for a given state
#
# Output:
# pairs - Count of the number of pairs that are in reverse order for a state
def directTileReversals( self ):

    # Calculate the number of pairs
    pairs = 0

    for i in range(15):
        for j in range(i+1, 16):

            # If the adjacent state piece is in a higher state than it is supposed to be in
            if self.currentState[i] != 0 and self.currentState[j] != 0 and self.currentState[i] < self.currentState[j]:
                pairs += 1

    return pairs

# Add heuristic functions to the State object for specific algorithm
State.__lt__ = __lt__
State.directTileReversals = directTileReversals

# Heuristic Function #3 ( Number of Direct Adjacent Tile Reversals )
# Input:
# init - Initial state of the State type
# goal - Goal state of the State type
# file1 - File to write the solution to
# 
# Output:
# solution_H3.txt - Text file containing solution
def h3( init, goal, file1 ):

    # Open and closed lists
    open = [ ( init.directTileReversals( ), init ) ]
    closed = []

    # Initialize iterations
    numit = 0
    totalIt = 0

    # While the queue is not empty
    while open:

        # Remove first value
        _, curr = heapq.heappop( open )

        # Track iterations
        numit += 1
        totalIt += 1

        # If the goal state has been found
        if curr.currentState == goal.currentState:
            break

        print('')
        print( 'Iteration:', totalIt )
        print( 'Removed from Stack:')
        curr.display()

        # Find neighbors of the popped node
        neighbors = curr.findNeighbors( closed )

        tempList = []
        
        # For each neighbor
        for i in range( len( neighbors )):
            print('Appended to open and closed list: ')
            neighbor = State( neighbors[i] )
            neighbor.display( )

            print( 'Total Number of Incorrect Adjacent Pairs:' )
            print( neighbor.directTileReversals( ) )
            print('')
            
            neighbor.parent = curr

            new_priority = neighbor.directTileReversals( )

            # Make a priority queue for the new neighbor nodes
            heapq.heappush( open, ( new_priority, neighbor ) )
        
        # Add the finished node to the closed list
        closed.append( curr )

    print('Solution Found!')

    # End the time
    ct = time.time()

    # Initiate solution list
    movedList = []

    # Parent of the parent
    parent = curr.parent

    while parent != None:
        if parent.parent == None:
            break
        else:
            movedList.append( parent.parent )
            parent = parent.parent

    # Top value is the init, bottom is goal
    movedList.reverse()

    file1.write('Method: h3')
    file1.write('\n\n')

    file1.write('Number of moves in path: ')
    file1.write( str(len(movedList) + 1))
    file1.write('\n\n')

    file1.write('Total Number of iterations performed to reach path: ')
    file1.write( str( totalIt + 1))
    file1.write('\n\n')

    file1.write('Time elapsed: ')
    file1.write( str( round( (ct - et) / 60 , 2) ) )
    file1.write(' minutes')
    file1.write('\n\n')

    for i in movedList:
        file1.write( str( np.array( i.currentState ).reshape(( 4, 4 ))))
        file1.write('\n\n')

    file1.write( str(np.array(curr.parent.currentState).reshape(( 4, 4 ))))
    file1.write('\n\n')
    file1.write( str(np.array(curr.currentState).reshape(( 4, 4 ))))
    file1.write('\n\n')


def main( init = init, goal = goal ):

    h3( State( init, goal= goal ), State( goal ), file1)

if __name__ == "__main__":
    main()