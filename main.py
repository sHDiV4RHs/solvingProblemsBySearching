import queue


class Problem:
    def __init__(self, initialState):
        self.initialState = initialState

    def findZero(self, state):
        I0 = -1
        J0 = -1
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    I0 = i
                    J0 = j
        return [I0, J0]

    def goalTest(self, state):
        if state == [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]]:
            return True

        return False

    def actions(self, state):
        IJ0 = self.findZero(state)
        I0 = IJ0[0]
        J0 = IJ0[1]

        actions = []
        if J0 + 1 < 3:
            actions.append('r')
        if J0 - 1 >= 0:
            actions.append('l')
        if I0 + 1 < 3:
            actions.append('d')
        if I0 - 1 >= 0:
            actions.append('u')
        return actions

    def getChild(self, node, action):
        # print("\nin getChild:")
        # print("\nnode.printNode()")
        # node.printNode()
        IJ0 = self.findZero(node.state)
        I0 = IJ0[0]
        J0 = IJ0[1]
        s = node.state
        newState = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                newState[i][j] = s[i][j]

        if action == 'r':
            newState[I0][J0] = newState[I0][J0 + 1]
            newState[I0][J0 + 1] = 0
        elif action == 'l':
            newState[I0][J0] = newState[I0][J0 - 1]
            newState[I0][J0 - 1] = 0
        elif action == 'u':
            newState[I0][J0] = newState[I0 - 1][J0]
            newState[I0 - 1][J0] = 0
        elif action == 'd':
            newState[I0][J0] = newState[I0 + 1][J0]
            newState[I0 + 1][J0] = 0

        child = Node(newState, 0, node, action)
        # print("\nchild in getChild")
        # child.printNode()
        return child


class Node:
    def __init__(self, state, pathCost, parent, lastAction):
        self.state = state
        self.pathCost = pathCost
        self.parent = parent
        self.previousAction = lastAction

    def printNode(self):
        for l in self.state:
            print(l)


class BFS:
    def __init__(self):
        self.frontier = queue.Queue()
        self.explored = queue.Queue()

    def solution(self, node):
        solution = []
        actions = []
        while node.parent != 0:
            solution.append(node)
            actions.append(node.previousAction)
            node = node.parent

        solution.append(node)
        # return solution
        return [actions, solution]

    def isNotVisited(self, node):
        for n in list(self.frontier.queue):
            if n.state == node.state:
                return False

        for n in list(self.explored.queue):
            if n.state == node.state:
                return False

        return True

    def run(self, problem):
        node = Node(problem.initialState, 0, 0, '')
        if problem.goalTest(node.state):
            return self.solution(node)
        self.frontier = queue.Queue()
        self.frontier.put(node)
        self.explored = queue.Queue()

        while True:
            if self.frontier.empty():
                return False
            node = self.frontier.get()
            # print("\nnode.state:")
            # node.printNode()
            self.explored.put(node)

            actions = problem.actions(node.state)
            # print("\nactions:")
            # print(actions)
            for action in actions:
                child = problem.getChild(node, action)
                # print("\nnode.state in actions")
                # node.printNode()
                # print("\nchild")
                # child.printNode()
                if self.isNotVisited(child):
                    # print("\nisNotVisited")
                    if problem.goalTest(child.state):
                        # print("\ngoalTest")
                        return self.solution(child)
                    self.frontier.put(child)


def printSolution(solution):
    counter = 0
    for s in list(reversed(solution)):
        print('{}:'.format(counter))
        s.printNode()
        print('\n')
        counter += 1


def printActions(actions):
    print(list(reversed(actions)))


p = Problem([[1, 5, 2],
             [7, 4, 3],
             [0, 8, 6]])
bfs = BFS()
actions, solution = bfs.run(p)
printSolution(solution)
printActions(actions)
