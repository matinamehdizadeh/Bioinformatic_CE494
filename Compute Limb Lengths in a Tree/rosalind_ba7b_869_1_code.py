import numpy as np

with open('rosalind_ba7b.txt', 'r') as f:
    n = int(f.readline())
    target = int(f.readline())
    matrix = np.zeros(shape=(n, n))
    counter = 0
    for line in f.readlines():
        string = line.split()
        for j in range(n):
            matrix[counter][j] = (int(string[j]))
        counter += 1

minimum = float("inf")
for i in range(n):
    for j in range(n):
        dist = (matrix[i][target] + matrix[target][j] - matrix[i][j])
        if minimum > dist > 0:
            minimum = dist
print(int(minimum/2))