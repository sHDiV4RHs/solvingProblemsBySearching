import Node


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

        child = Node.Node(newState, 0, node, action)
        # print("\nchild in getChild")
        # child.printNode()
        return child
