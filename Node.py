class Node:
    def __init__(self, state, pathCost, parent, lastAction):
        self.state = state
        self.pathCost = pathCost
        self.parent = parent
        self.previousAction = lastAction

    def printNode(self):
        for l in self.state:
            print(l)


class DLSNode(Node):
    def __init__(self, state, pathCost, parent, lastAction):
        super().__init__(state, pathCost, parent, lastAction)
        self.state = state
        self.pathCost = pathCost
        self.parent = parent
        self.previousAction = lastAction

    def printNode(self):
        for l in self.state:
            print(l)
