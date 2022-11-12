# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest states in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    s = util.Stack() # stack of states to explore
    explored = set() #set of explored states

    start = problem.getStartState() #define starting state as start

    s.push((start,[],0)) #push start state to stack

    #begin graph traversal & loop until stack is empty
    while s:
        current, actions, cost = s.pop() #pop current state
        if current[0] in explored: #ensure current state is not already explored
            continue
        explored.add(current[0]) # add current state to explored list
        if problem.isGoalState(current): # check if goal is reached
            return actions #return states expanded when goal is reached
        children = problem.getSuccessors(current) # find successors of current
        for child, child_actions, child_cost in children: #iterate over children of current
            if child in explored: # ensure not already explored
                continue
            s.push((child, actions + [child_actions], child_cost)) #push children with associated data to stack
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest states in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue() #define main data stucture for bfs
    start = problem.getStartState() # get starting state 
    start = (start, []) #cost is not necessary to store for bfs
    queue.push(start) #push the first element to the queue
    explored = set() #set which contains explored elements

    #add the start node to explored since it is our first expansion
    explored.add(start[0])
    while queue: #we continue while there are elements in the queue - goal state breaks loop
        state = queue.pop()
        if problem.isGoalState(state[0]): #once reached, we return actions
            return state[1] #return list of actions
        successors = problem.getSuccessors(state[0]) # get successors of current state
        for successor in successors:
            if successor[0] in explored: #check if child exists in explored queue
                continue #if so, we break and go to next iteration
            explored.add(successor[0]) #add unexplored child to the explored set
            queue.push((successor[0], state[1] + [successor[1]])) #push relevant successor info to queue

    return None


def uniformCostSearch(problem):
    """Search the state of least total cost first."""
    "*** YOUR CODE HERE ***"

    #define data structures
    pq = util.PriorityQueue()
    explored = set()

    #define starting state
    start = problem.getStartState()
    
    #push initial state to pq
    pq.push((start,[],0),0)

    while pq:
        current, parent_actions, parent_cost = pq.pop() #pop top prior item
        if current[0] in explored:
            continue
        explored.add(current[0]) #explored state 

        #check if we reach goal in current state
        if problem.isGoalState(current):
            return parent_actions

        #now iterate over children & add to stack
        children = problem.getSuccessors(current)
        for child, child_actions, child_cost in children:
            total_actions = parent_actions + [child_actions]
            total_cost = parent_cost + child_cost
            pq.push((child, total_actions, total_cost), total_cost)

    return [] #goal not found

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #define data structures
    pq = util.PriorityQueue()
    explored = set() 

    #define starting node
    start = problem.getStartState()
    
    #push initial node to pq
    pq.push((start,[],0),0)

    while pq:
        current, parent_actions, parent_cost = pq.pop() #pop top prior item
        if current in explored:
            continue
        explored.add(current) #explored node 

        #check if we reach goal in current state
        if problem.isGoalState(current):
            return parent_actions

        #now iterate over children & add to stack
        for child, child_actions, child_cost in problem.getSuccessors(current):
            if child in explored:
                continue

            total_actions = parent_actions + [child_actions]
            state_cost = child_cost + parent_cost
            #add heuristic cost to optimize prioirty value
            heuristic_cost = parent_cost + child_cost + heuristic(child, problem) 
            pq.push((child, total_actions, state_cost), heuristic_cost)

    util.raiseNotDefined()
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
