from itertools import product
kmers = []
dnas = []


with open('rosalind_ba2b.txt', 'r') as f:
    n = int(f.readline())
    for line in f.readlines():
        dnas.append(line)

totalMin = n*len(dnas)
for roll in product(['A', 'C', 'G', 'T'], repeat = n):
    tempMinimum = 0
    for dna in dnas:
        minimum = n
        for k1 in range(len(dna)-n+1):
            distance = 0
            for k2 in range(n):
                if roll[k2] != dna[k1+k2]:
                    distance += 1
            if minimum > distance:
                minimum = distance
        tempMinimum += minimum
        if tempMinimum > totalMin:
            break

    if tempMinimum <= totalMin:
        totalMin = tempMinimum
        motif = roll


for i in range(n):
    print(motif[i], end='')