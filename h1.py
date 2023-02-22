from game import *

# Start the time
et = time.time()

file1 = open("solution_H1.txt","w")

# Created to allow the heapq functions to work properly.
# This will allow the states to be compared based off their total number of incorrect pieces
def __lt__( self, other ):
    return self.findNumIncorrect() < other.findNumIncorrect()

# Used to find the sum of the number of incorrect pieces on the current state
#
# Output:
# numIncorrect - Integer type of the total number of incorrect pieces  
def findNumIncorrect( self , goal = goal ):
    
    # Initialize the number of incorrect tiles
    numIncorrect = 0

    # For each puzzle piece
    for i in range(16):

        if self.currentState[i] != goal[i]:
            numIncorrect += 1

    return numIncorrect

# Add heuristic functions to the State object for specific algorithm
State.__lt__ = __lt__
State.findNumIncorrect = findNumIncorrect

# Heuristic Function #1 ( Number of Tiles Misplaced )
# Input:
# init - Initial state of the State type
# goal - Goal state of the State type
# file1 - File to write the solution to
# 
# Output:
# solution_H2.txt - Text file containing solution
def h1( init, goal, file1 ):

    # Open and closed lists
    open = [ ( init.findNumIncorrect( ), init ) ]
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

            print( 'Number of Incorrect Pieces:' )
            print( neighbor.findNumIncorrect( ) )
            print('')

            neighbor.parent = curr

            new_priority = neighbor.findNumIncorrect()

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

    file1.write('Method: h1')
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

    h1( State( init, goal= goal ), State( goal ), file1)

if __name__ == "__main__":
    main()