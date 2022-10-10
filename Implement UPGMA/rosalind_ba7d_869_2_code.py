import collections
import numpy as np

nodes = []
graph = {}


with open('rosalind_ba7d.txt', 'r') as f:
    n = int(f.readline())
    matrix = np.zeros(shape=(n, n))
    counter = 0
    for line in f.readlines():
        string = line.split()
        nodes.append(counter)
        graph[counter] = [[counter, 0, 0]]
        for j in range(n):
            matrix[counter][j] = (int(string[j]))
        counter += 1

temp = matrix.copy()


def bfs(s):
    stack = collections.deque([])
    stack.append(s)
    all_nodes = []
    visit = [0] * len(graph)
    if s < n:
        all_nodes.append(s)
    while len(stack) > 0:
        u = stack.popleft()
        for i1 in range(len(graph[u])):
            if visit[graph[u][i1][0]] == 0:
                visit[graph[u][i1][0]] = 1
                if (graph[u][i1][0] not in all_nodes) and (graph[u][i1][0] < n):
                    all_nodes.append(graph[u][i1][0])
                stack.append(graph[u][i1][0])
    return all_nodes


for k in range(n):
    maximum = float('inf')
    minimum = [0, 0]
    for i in range(len(temp)):
        for j in range(i):
            if (i in nodes) and (j in nodes) and (temp[i][j] < maximum):
                minimum[0] = i
                minimum[1] = j
                maximum = temp[i][j]

    replace = (temp[minimum[0]] + temp[minimum[1]])
    nodes.append(nodes[-1] + 1)
    weight = replace[minimum[0]] / 2
    weight1 = weight - graph[minimum[0]][-1][2]
    weight2 = weight - graph[minimum[1]][-1][2]

    graph[nodes[-1]] = []
    graph[nodes[-1]].append([minimum[0], weight1, weight])
    graph[nodes[-1]].append([minimum[1], weight2, weight])

    graph[minimum[0]].append([nodes[-1], weight1, weight])
    graph[minimum[1]].append([nodes[-1], weight2, weight])
    nodes = np.array(nodes)
    nodes = np.delete(nodes, np.where(nodes == minimum[0]))
    nodes = np.delete(nodes, np.where(nodes == minimum[1])).tolist()
    bfsMain = bfs(nodes[-1])
    replace2 = []
    for i in range(len(temp)):
        if i in nodes:
            bfsI = bfs(i)
            firstLen = len(bfsI)
            if firstLen == 0:
                firstLen = 1
            replace2.append(sum([temp[cl1][cl2] for cl1 in bfsI for cl2 in bfsMain]) / (firstLen * len(bfsMain)))
        else:
            replace2.append(0)
    replace2 = np.array(replace2)

    temp = np.vstack([temp, replace2])
    replace2 = np.append(replace2, [0]).reshape(n + k + 1, 1)
    temp = np.hstack([temp, replace2])

    if k == n - 2:
        break

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if i != graph[i][j][0]:
            print(str(i) + '->' + str(graph[i][j][0]) + ':' + "{:.3f}".format(graph[i][j][1]))