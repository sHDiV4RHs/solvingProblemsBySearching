class Node:
    def __init__(self, state, pathCost, parent, lastAction):
        self.state = state
        self.pathCost = pathCost
        self.parent = parent
        self.previousAction = lastAction

    def printNode(self):
        for l in self.state:
            print(l)

    def __gt__(self, other):
        if self.pathCost > other.pathCost:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.pathCost < other.pathCost:
            return True
        else:
            return False

    # def __eq__(self, other):
    #     if self.pathCost == other.pathCost:
    #         return True
    #     else:
    #         return False


# class DLSNode(Node):
#     def __init__(self, state, pathCost, parent, lastAction):
#         super().__init__(state, pathCost, parent, lastAction)
#         self.state = state
#         self.pathCost = pathCost
#         self.parent = parent
#         self.previousAction = lastAction
#
#     def printNode(self):
#         for l in self.state:
#             print(l)


class AStarNode(Node):
    def __init__(self, state, pathCost, parent, lastAction):
        super().__init__(state, pathCost, parent, lastAction)

    def __gt__(self, other):
        if self.pathCost + self.heuristicFunction() > \
                other.pathCost + other.heuristicFunction:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.pathCost + self.heuristicFunction() < \
                other.pathCost + other.heuristicFunction:
            return True
        else:
            return False

    def printNode(self):
        for l in self.state:
            print(l)

    def getGoalPosition(self, num):
        if num == 0:
            return [2, 2]
        if num == 1:
            return [0, 0]
        if num == 2:
            return [0, 1]
        if num == 3:
            return [0, 2]
        if num == 4:
            return [1, 0]
        if num == 5:
            return [1, 1]
        if num == 6:
            return [1, 2]
        if num == 7:
            return [2, 0]
        if num == 8:
            return [2, 1]

    def heuristicFunction(self):
        diff = 0
        for i in range(3):
            for j in range(3):
                [x, y] = self.getGoalPosition(self.state[i][j])
                diff += abs(x - i) + abs(y - j)
        return diff
