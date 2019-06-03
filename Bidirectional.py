import Node


class Bidirectional:
    def __init__(self):
        self.startFrontier = []
        self.startExplored = []
        self.startNumOfCreatedNodes = 0
        self.startMaxNodesInMemory = 0
        self.startNumOfExploredNodes = 0

        self.endFrontier = []
        self.endExplored = []
        self.endNumOfCreatedNodes = 0
        self.endMaxNodesInMemory = 0
        self.endNumOfExploredNodes = 0

        self.numOfCreatedNodes = 0
        self.maxNodesInMemory = 0
        self.numOfExploredNodes = 0

    def solution(self, startNode, endNode):
        solution = []
        actions = []
        # startNode.printNode()
        # endNode.printNode()
        while startNode != 0:
            solution.append(startNode)
            action = startNode.previousAction
            if action != '':
                actions.append(action)
            startNode = startNode.parent

        while endNode != 0:
            solution.insert(0, endNode)
            action = endNode.previousAction
            if action == 'l':
                actions.insert(0, 'r')
            elif action == 'r':
                actions.insert(0, 'l')
            elif action == 'u':
                actions.insert(0, 'd')
            elif action == 'd':
                actions.insert(0, 'u')

            endNode = endNode.parent

        self.startNumOfExploredNodes = len(self.startExplored)
        self.endNumOfExploredNodes = len(self.endExplored)

        self.numOfCreatedNodes = self.startNumOfCreatedNodes \
                                 + self.endNumOfCreatedNodes
        self.maxNodesInMemory = self.startMaxNodesInMemory \
                                + self.endMaxNodesInMemory
        self.numOfExploredNodes = self.startNumOfExploredNodes \
                                  + self.endNumOfExploredNodes
        return [actions, solution]

    def isNotVisited(self, node, frontier, explored):
        for n in frontier:
            if n.state == node.state:
                return False

        for n in explored:
            if n.state == node.state:
                return False

        return True

    def getIntersection(self, node, frontier):
        for n in frontier:
            if n.state == node.state:
                # n.printNode()
                # print()
                return n
        return False

    def run(self, problem):
        startNode = Node.Node(problem.initialState, 0, 0, '')
        endNode = Node.Node(problem.goalState, 0, 0, '')
        self.startNumOfCreatedNodes += 1
        self.endNumOfCreatedNodes += 1

        # if problem.goalTest(startNode.state):
        #     return self.solution(startNode)

        self.startFrontier = [startNode]
        self.startExplored = []
        self.endFrontier = [endNode]
        self.endExplored = []

        if self.getIntersection(startNode, self.endFrontier):
            return self.solution(startNode, endNode)

        while True:
            if len(self.startFrontier) == 0 or len(self.endFrontier) == 0:
                return False

            # START
            self.startMaxNodesInMemory = max(len(self.startFrontier)
                                             + len(self.startExplored),
                                             self.startMaxNodesInMemory)
            startNode = self.startFrontier.pop(0)
            self.startExplored.append(startNode)
            startActions = problem.actions(startNode.state)
            for action in startActions:
                child = problem.getChild(startNode, action)
                self.startNumOfCreatedNodes += 1
                if self.isNotVisited(child, self.startFrontier,
                                     self.startExplored):
                    intersection = self.getIntersection(child, self.endFrontier)
                    if intersection:
                        return self.solution(child, intersection)
                    self.startFrontier.append(child)

            # END
            self.endMaxNodesInMemory = max(len(self.endFrontier)
                                           + len(self.endExplored),
                                           self.endMaxNodesInMemory)
            endNode = self.endFrontier.pop(0)
            self.endExplored.append(endNode)
            endActions = problem.actions(endNode.state)
            for action in endActions:
                child = problem.getChild(endNode, action)
                self.endNumOfCreatedNodes += 1
                if self.isNotVisited(child, self.endFrontier,
                                     self.endExplored):
                    intersection = self.getIntersection(child, self.startFrontier)
                    if intersection:
                        return self.solution(child, intersection)
                    self.endFrontier.append(child)
