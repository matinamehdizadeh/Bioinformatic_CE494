import collections

graph = {}

with open('rosalind_ba7a.txt', 'r') as f:
    n = int(f.readline())
    for line in f.readlines():
        string = line.replace('->', ' ').replace(':', ' ').split(' ')
        if int(string[0]) not in graph.keys():
            graph[int(string[0])] = [[int(string[1]), int(string[2])]]
        else:
            graph[int(string[0])].append([int(string[1]), int(string[2])])

for k in range(n):
    inf = 1000 * 1000
    BFS = [inf] * len(graph)
    stack = collections.deque([])
    stack.append(k)
    BFS[k] = 0

    while len(stack) > 0:
        u = stack.popleft()
        for i in graph[u]:
            if BFS[i[0]] == inf:
                BFS[i[0]] = i[1] + BFS[u]
                stack.append(i[0])

    final = BFS[:n]
    print(*final, sep=' ')