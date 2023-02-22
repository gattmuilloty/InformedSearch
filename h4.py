from game import *

# Start the time
et = time.time()

file1 = open("solution_H4.txt","w")

# Created to allow the heapq functions to work properly.
# This will allow the states to be compared based off their total number of incorrect pieces
def __lt__( self, other ):
    return self.h1h2() < other.h1h2()

# Finds the sum of h1 and h2 heuristic functions
#
# Output:
# total - Integer type of the total number incorrect pieces, along with the total Manhattan Distance
def h1h2( self , goal = goal ):
    
    # Initialize the number of incorrect tiles
    total = 0

    # For each puzzle piece
    for i in range(16):

        if self.currentState[i] != goal[i]:
            total += 1

    # For the range of the slide puzzle
    for i in range(16):

        if self.currentState.index(i) != goal.index(i):
            row1, col1 = divmod( self.currentState.index(i), 4 )
            row2, col2 = divmod( goal.index(i), 4 )

            total += abs( row1 - row2 ) + abs( col1 - col2 )
            
    return total

# Add heuristic functions to the State object for specific algorithm
State.__lt__ = __lt__
State.h1h2 = h1h2

# Heuristic Function #3 ( Combination of Heuristic Functions h1 and h2 )
# Input:
# init - Initial state of the State type
# goal - Goal state of the State type
# file1 - File to write the solution to
# 
# Output:
# solution_H4.txt - Text file containing solution
def h4( init, goal, file1 ):

    # Open and closed lists
    open = [ ( init.h1h2( ), init ) ]
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
        print( 'Removed from Queue:')
        curr.display()
        print('')

        # Find neighbors of the popped node
        neighbors = curr.findNeighbors( closed )

        tempList = []
        
        # For each neighbor
        for i in range( len( neighbors )):
            print('Appended to open and closed list: ')
            neighbor = State( neighbors[i] )
            neighbor.display( )

            print( 'h1 + h2 = ' )
            print( neighbor.h1h2( ) )
            print('')

            neighbor.parent = curr

            new_priority = neighbor.h1h2()

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

    file1.write('Method: h4')
    file1.write('\n\n')

    file1.write('Number of moves in path: ')
    file1.write( str(len(movedList) + 1))
    file1.write('\n\n')

    file1.write('Total Number of iterations performed to reach path: ')
    file1.write( str( totalIt + 1))
    file1.write('\n\n')

    file1.write('Time elapsed: ')
    file1.write( str( round( (ct - et)/ 60 , 2 ) ) )
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

    h4( State( init, goal= goal ), State( goal ), file1)

if __name__ == "__main__":
    main()