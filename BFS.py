import Node


class BFS:
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
        self.numOfExploredNodes = len(self.explored)
        # return solution
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
        node = Node.Node(problem.initialState, 0, 0, '')
        self.numOfCreatedNodes += 1
        if problem.goalTest(node.state):
            return self.solution(node)
        self.frontier = [node]
        self.explored = []

        while True:
            if len(self.frontier) == 0:
                return False
            self.maxNodesInMemory = max(len(self.frontier)
                                        + len(self.explored),
                                        self.maxNodesInMemory)
            node = self.frontier.pop(0)
            # print("\nnode.state:")
            # node.printNode()
            self.explored.append(node)

            actions = problem.actions(node.state)

            # print("\nactions:")
            # print(actions)
            for action in actions:
                child = problem.getChild(node, action)
                self.numOfCreatedNodes += 1
                # print("\nnode.state in actions")
                # node.printNode()
                # print("\nchild")
                # child.printNode()
                if self.isNotVisited(child):
                    # print("\nisNotVisited")
                    if problem.goalTest(child.state):
                        # print("\ngoalTest")
                        return self.solution(child)
                    self.frontier.append(child)
