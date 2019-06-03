import DLS


class IDDFS:
    def __init__(self):
        self.frontier = []
        self.explored = []
        self.numOfCreatedNodes = 0
        self.maxNodesInMemory = 0
        self.numOfExploredNodes = 0

    def solution(self, node):
        solution = []
        actions = []
        while node.parent != 0:
            solution.append(node)
            actions.append(node.previousAction)
            node = node.parent

        solution.append(node)
        self.maxNodesInMemory = self.numOfExploredNodes
        return [actions, solution]

    def isNotVisited(self, node):
        for n in self.frontier:
            if n.state == node.state:
                return False

        for n in self.explored:
            if n.state == node.state:
                return False

        return True

    def run(self, problem):
        depth = 0
        while True:
            dls = DLS.DLS()
            result = dls.run(problem, depth)
            self.numOfExploredNodes += dls.numOfExploredNodes
            self.numOfCreatedNodes += dls.numOfCreatedNodes
            self.maxNodesInMemory = max(self.maxNodesInMemory, dls.maxNodesInMemory)
            if result != 'cutoff':
                return result
            depth += 1
