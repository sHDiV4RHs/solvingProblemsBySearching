import Node
import heapq


class UCS:
    def __init__(self):
        self.frontier = []
        heapq.heapify(self.frontier)
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
        self.numOfExploredNodes = len(self.explored)
        # return solution
        return [actions, solution]

    def isNotVisited(self, node):  # Update the cost if visited
        for n in self.frontier:
            if n.state == node.state:
                if n.pathCost > node.pathCost:
                    self.frontier.remove(n)
                    heapq.heappush(self.frontier, node)
                return False

        for n in self.explored:
            if n.state == node.state:
                return False

        return True

    def run(self, problem):
        node = Node.Node(problem.initialState, 0, 0, '')
        self.numOfCreatedNodes += 1
        heapq.heappush(self.frontier, node)
        self.explored = []

        while True:
            if len(self.frontier) == 0:
                return False
            self.maxNodesInMemory = max(len(self.frontier)
                                        + len(self.explored),
                                        self.maxNodesInMemory)
            node = heapq.heappop(self.frontier)
            if problem.goalTest(node.state):
                return self.solution(node)
            self.explored.append(node)

            actions = problem.actions(node.state)

            for action in actions:
                child = problem.getChild(node, action)
                self.numOfCreatedNodes += 1
                if self.isNotVisited(child):
                    heapq.heappush(self.frontier, child)
