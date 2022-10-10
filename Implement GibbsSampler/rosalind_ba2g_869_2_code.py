import random


def calculateDistance(temporary):
    maxProbString = ''
    for i2 in range(k):
        seq1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for m in temporary:
            seq1[m[i2]] += 1
        maximum = 0
        for key in seq1.keys():
            pT = seq1[key] / (len(temporary) + 4)
            if pT > maximum:
                maximum = pT
                newGene = key
        maxProbString = maxProbString + newGene
    distance = 0
    for m in temporary:
        for j in range(k):
            if m[j] != maxProbString[j]:
                distance += 1
    return distance



dnas = []
with open('rosalind_ba2g.txt', 'r') as f:
    inp = f.readline().replace('\n', '').split()
    k = int(inp[0])
    t = int(inp[1])
    N = int(inp[2])
    for line in f.readlines():
        dnas.append(line.replace('\n', ''))
seq2 = {'A':0, 'C':1, 'G':2, 'T':3}
best = []
for i in range(t):
    best.append(dnas[i][:k])
for i in range(25):
    localBest = []
    for dna in dnas:
        index = random.randint(k, len(dna))
        localBest.append(dna[index-k:index])
    temp = localBest.copy()
    for j in range(N):
        index = random.randint(0, t-1)
        localBest.pop(index)
        prob = []
        for i2 in range(k):
            seq1 = {'A': 1, 'C': 1, 'G': 1, 'T': 1}
            for m in localBest:
                seq1[m[i2]] += 1
            pT = []
            for key in seq1.keys():
                pT.append(seq1[key] / (len(localBest) + 4))
            prob.append(pT)

        prob2 = []
        for i2 in range(len(dnas[index]) + 1 - k):
            stringT = dnas[index][i2:i2 + k]
            probTemp = 1
            for sub in range(len(stringT)):
                probTemp *= prob[sub][seq2[stringT[sub]]]
            prob2.append(probTemp)
        normalizer = sum(prob2)
        for i2 in range(len(prob2)):
            prob2[i2] = prob2[i2]/normalizer
        newRand = random.uniform(0, 1)
        sumAll = 0
        for i2 in range(len(prob2)):
            sumAll += prob2[i2]
            if newRand < sumAll:
                newindex = i2
                break
        localBest.insert(index, dnas[index][newindex:newindex+k])
        if calculateDistance(localBest) < calculateDistance(temp):
            temp = localBest.copy()

    if calculateDistance(best) > calculateDistance(temp):
        best = temp.copy()

for i in best:
    print(i)