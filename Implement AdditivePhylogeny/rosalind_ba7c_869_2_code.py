from collections import deque
import numpy as np

with open('rosalind_ba7c.txt', 'r') as f:
    num = int(f.readline())
    matrix = np.zeros(shape=(num, num))
    counter = 0
    for line in f.readlines():
        string = line.split()
        for j in range(num):
            matrix[counter][j] = (int(string[j]))
        counter += 1

graph = {}


def BFS(src, dest, visited, path):
    visited[src] = 1
    path.append(src)
    if src == dest:
        return True
    for neighbor in graph[src]:
        i = neighbor[0]
        if not visited[i]:
            if BFS(i, dest, visited, path):
                return True
    path.pop()
    return False


def AdditivePhylogeny(m, n, N):
    if n == 2:
        graph[0] = [[1, m[0][1]]]
        graph[1] = [[0, m[0][1]]]
        return N
    minimum = float("inf")
    for i in range(n):
        for j in range(n):
            dist = (m[i][n-1] + m[n-1][j] - m[i][j])
            if minimum > dist > 0:
                minimum = dist
    distance = minimum/2
    m[n-1] = m[n-1] - distance
    m[:, n-1] = m[:, n-1] - distance
    m[n-1, n-1] += 2*distance
    flag = True
    for i in range(n-1):
        for j in range(n-1):
            if (i != j) and (m[i][j] == (m[i][n-1] + m[j][n-1])):
                firstNode = i
                secondNode = j
                target = m[firstNode, n-1]
                flag = False
                break
        if not flag:
            break
    temp = m[:n-1, :n-1]
    N = AdditivePhylogeny(temp, n-1, N)
    path = deque()
    visited = [0] * N
    BFS(firstNode, secondNode, visited, path)
    weight = 0
    for i in range(len(path) - 1):
        for j in range(len(graph[path[i]])):
            if graph[path[i]][j][0] == path[i+1]:
                break
        if weight + graph[path[i]][j][1] > target:
            weight2 = weight + graph[path[i]][j][1]
            firstremove = path[i]
            new = path[i]
            secondremove = path[i+1]
            break
        weight += graph[path[i]][j][1]

    if weight < target:
        new = N
        N += 1
        for i in range(len(graph[firstremove])):
            if graph[firstremove][i][0] == secondremove:
                graph[firstremove].pop(i)
                break
        graph[firstremove].append([new, target-weight])
        graph[new] = [[firstremove, target-weight]]
        for i in range(len(graph[secondremove])):
            if graph[secondremove][i][0] == firstremove:
                graph[secondremove].pop(i)
                break
        graph[secondremove].append([new, weight2-target])
        graph[new].append([secondremove, weight2-target])
    graph[new].append([n-1, distance])
    graph[n-1] = [[new, distance]]
    return N


AdditivePhylogeny(matrix, num, num)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(str(i) + '->' + str(graph[i][j][0]) + ':' + str(int(graph[i][j][1])))