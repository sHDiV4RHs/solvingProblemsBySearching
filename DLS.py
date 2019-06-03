import Node


class DLS:
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
        # return solution
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

    def run(self, problem, limit):
        node = Node.Node(problem.initialState, 0, 0, '')
        self.numOfCreatedNodes += 1
        return self.recursiveDLS(node, problem, limit)

    def recursiveDLS(self, node, problem, limit):
        if problem.goalTest(node.state):
            return self.solution(node)
        elif limit == 0:
            return 'cutoff'
        else:
            cutoffOccurred = False
            actions = problem.actions(node.state)
            self.numOfExploredNodes += 1
            for action in actions:
                child = problem.getChild(node, action)
                self.numOfCreatedNodes += 1
                result = self.recursiveDLS(child, problem, limit-1)
                if result == 'cutoff':
                    cutoffOccurred = True
                elif result != 'failure':
                    return result
            if cutoffOccurred:
                return 'cutoff'
            else:
                return 'failure'
