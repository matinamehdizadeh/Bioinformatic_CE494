import numpy as np
nodes = []

with open('rosalind_ba7e.txt', 'r') as f:
    n = int(f.readline())
    matrix = np.zeros(shape=(n, n))
    counter = 0
    for line in f.readlines():
        string = line.split()
        nodes.append(counter)
        for j in range(n):
            matrix[counter][j] = (int(string[j]))
        counter += 1
graph = {}
for k in range(n):
    R = matrix.sum(axis=0)
    temp = np.zeros(shape=matrix.shape)
    dist = np.zeros(shape=matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != j:
                temp[i][j] = (n-k-2) * matrix[i][j] - R[i] - R[j]
            if j > i:
                dist[i][j] = (R[i] - R[j])/(n-k-2)
                dist[j][i] = dist[i][j]
    minimum = np.argwhere(temp == np.min(temp))[0]
    weight1 = (dist[minimum[0]][minimum[1]] + matrix[minimum[0]][minimum[1]])/2
    weight2 = (-dist[minimum[1]][minimum[0]] + matrix[minimum[1]][minimum[0]])/2

    replace = [0.5 * (matrix[k2][minimum[0]] + matrix[k2][minimum[1]] - matrix[minimum[0]][minimum[1]]) for k2 in range(n-k)]
    replace = np.delete(replace, minimum)
    matrix = np.delete(np.delete(matrix, minimum, 0), minimum, 1)
    matrix = np.vstack([matrix, replace])
    replace = np.append(replace, [0]).reshape(n-k-1,1)
    matrix = np.hstack([matrix, replace])
    nodes.append(nodes[-1] + 1)

    if nodes[minimum[0]] not in graph.keys():
        graph[nodes[minimum[0]]] = []
    graph[nodes[minimum[0]]].append([nodes[-1], "{:.3f}".format(weight1)])
    if nodes[minimum[1]] not in graph.keys():
        graph[nodes[minimum[1]]] = []
    graph[nodes[minimum[1]]].append([nodes[-1], "{:.3f}".format(weight2)])
    graph[nodes[-1]] = []
    graph[nodes[-1]].append([nodes[minimum[0]], "{:.3f}".format(weight1)])
    graph[nodes[-1]].append([nodes[minimum[1]], "{:.3f}".format(weight2)])
    nodes = np.array(nodes)
    nodes = np.delete(nodes, minimum).tolist()
    if k == n-3:
        if nodes[0] not in graph.keys():
            graph[nodes[0]] = []
        if nodes[1] not in graph.keys():
            graph[nodes[1]] = []
        maximum = np.amax(matrix)
        graph[nodes[0]].append([nodes[1], "{:.3f}".format(maximum)])
        graph[nodes[1]].append([nodes[0], "{:.3f}".format(maximum)])
        break

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(str(i) + '->' + str(graph[i][j][0]) + ':' + str(graph[i][j][1]))