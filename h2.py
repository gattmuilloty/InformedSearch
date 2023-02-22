from game import *

# Start the time
et = time.time()

file1 = open("solution_H2.txt","w")

# Created to allow the heapq functions to work properly.
# This will allow the states to be compared based off their Manhattan Distances
def __lt__( self, other ):
    return self.manhattanDistance() < other.manhattanDistance()

# Used to find the sum of the distances required to solve the puzzle.
#
# Output:
# distance - Integer type of the Manhattan Distance for the current state    
def manhattanDistance( self, goal = goal ):

    # Initialize distance
    distance = 0

    # For the range of the slide puzzle
    for i in range(16):

        if self.currentState.index(i) != goal.index(i):
            row1, col1 = divmod( self.currentState.index(i), 4 )
            row2, col2 = divmod( goal.index(i), 4 )

            distance += abs( row1 - row2 ) + abs( col1 - col2 )
            
    return distance

# Add heuristic functions to the State object for specific algorithm
State.__lt__ = __lt__
State.manhattanDistance = manhattanDistance

# Heuristic Function #2 ( Greedy Best-First Search )
# Input:
# init - Initial state of the State type
# goal - Goal state of the State type
# file1 - File to write the solution to
# 
# Output:
# solution_H2.txt - Text file containing solution
def h2( init, goal, file1 ):

    # Open and closed lists
    open = [ ( init.manhattanDistance( ), init ) ]
    closed = []

    # Initialize iterations
    numit = 0
    totalIt = 0

    # While the queue is not empty
    while open:

        # Remove first value
        _, curr = open.pop( )

        # Track iterations
        numit += 1
        totalIt += 1

        # Set depth limit
        if numit == 15000:
            # Reset iteration for next depth limit
            numit = 0

            _, curr = open.pop( 0 )

        # If the goal state has been found
        if curr.currentState == goal.currentState:
            break

        print('')
        print( 'Iteration:', totalIt )
        print( 'Removed from Stack:')
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

            print( 'Manhattan Distance:' )
            print( neighbor.manhattanDistance( ) )
            print('')

            neighbor.parent = curr

            new_priority = neighbor.manhattanDistance( )

            # Make a priority queue for the new neighbor nodes
            heapq.heappush( tempList, ( new_priority, neighbor ) )

        # For each new neighbor
        for i in range(len(neighbors)):

            # Insert the largest Manhattan Distances to the stack first, so the last value has the smallest value
            bigToSmall = heapq.nlargest( 1,tempList )[0]
            open.append( bigToSmall )

            # Remove from the temporary heap
            tempList.remove( bigToSmall )
        
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

    file1.write('Method: h2')
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

    h2( State( init, goal= goal ), State( goal ), file1)

if __name__ == "__main__":
    main()