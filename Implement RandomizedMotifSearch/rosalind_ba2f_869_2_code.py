import random


def calculateDistance(temporary):
    maxProbString = ''
    for i2 in range(k):
        seq1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for m in temporary:
            seq1[m[i2]] += 1
        maximum = 0
        for key in seq1.keys():
            pT = seq1[key] / (len(temp) + 4)
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
with open('rosalind_ba2f.txt', 'r') as f:
    inp = f.readline().replace('\n', '').split()
    k = int(inp[0])
    t = int(inp[1])
    for line in f.readlines():
        dnas.append(line.replace('\n', ''))

seq2 = {'A':0, 'C':1, 'G':2, 'T':3}
best = []
for i in range(t):
    best.append(dnas[i][:k])
for i in range(300):
    localBest = []
    for dna in dnas:
        index = random.randint(k, len(dna))
        localBest.append(dna[index-k:index])
        while True:
            prob = []
            for i2 in range(k):
                seq1 = {'A': 1, 'C': 1, 'G': 1, 'T': 1}
                for m in localBest:
                    seq1[m[i2]] += 1
                pT = []
                for key in seq1.keys():
                    pT.append(seq1[key] / (len(localBest) + 4))
                prob.append(pT)
            temp = []
            for j in range(len(dnas)):
                probMax = 0
                for i2 in range(len(dnas[j]) + 1 - k):
                    stringT = dnas[j][i2:i2 + k]
                    probTemp = 1
                    for sub in range(len(stringT)):
                        probTemp *= prob[sub][seq2[stringT[sub]]]
                    if probMax < probTemp:
                        probMax = probTemp
                        newPattern = stringT
                temp.append(newPattern)
            if calculateDistance(localBest) > calculateDistance(temp):
                localBest = temp.copy()
            else:
                break
    if calculateDistance(best) > calculateDistance(localBest):
        best = localBest.copy()

for i in range(len(best)):
    print(best[i])