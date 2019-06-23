import Problem
import DFS
import BFS
import DLS
import IDDFS
import Bidirectional
import UCS


def printSolution(solution):
    counter = 0
    for s in list(reversed(solution)):
        print('{}:'.format(counter))
        s.printNode()
        print('\n')
        counter += 1


def printActions(actions):
    print(list(reversed(actions)))


def printStatistics(algo, actions, solution):
    # printSolution(solution)
    printActions(actions)
    print("\nnumOfExploredNodes: {}".format(algo.numOfExploredNodes))
    print("numOfCreatedNodes: {}".format(algo.numOfCreatedNodes))
    print("maxNodesInMemory: {}".format(algo.maxNodesInMemory))
    print("goalDepth: {}".format(len(actions)))


# p = Problem.Problem([[4, 1, 2],
#              [5, 3, 0],
#              [6, 7, 8]])

# p = Problem.Problem([[1, 2, 3],
#                      [7, 4, 6],
#                      [0, 5, 8]])

p = Problem.Problem([[1, 5, 2],
                     [4, 0, 3],
                     [7, 8, 6]])

print("\n\nBFS")
bfs = BFS.BFS()
result = bfs.run(p)
if result:
    actions, solution = result
    printStatistics(bfs, actions, solution)

# print("\n\nDFS")
# dfs = DFS.DFS()
# result = dfs.run(p)
# if result:
#     actions, solution = result
#     printStatistics(dfs, actions, solution)
#
# print("\n\nDLS")
# dls = DLS.DLS()
# result = dls.run(p, 4)
# if result not in ['cutoff', 'failure']:
#     actions, solution = result
#     printStatistics(dls, actions, solution)
# else:
#     print(result)

# print("\n\nIDDFS")
# iddfs = IDDFS.IDDFS()
# result = iddfs.run(p)
# if result != 'failure':
#     actions, solution = result
#     printStatistics(iddfs, actions, solution)
# else:
#     print(result)

# print("\n\nBidirectional")
# bid = Bidirectional.Bidirectional()
# result = bid.run(p)
# if result:
#     actions, solution = result
#     printStatistics(bid, actions, solution)
# else:
#     print(result)

print("\n\nUCS")
ucs = UCS.UCS()
result = ucs.run(p)
if result:
    actions, solution = result
    printStatistics(ucs, actions, solution)
