dnas = []
with open('rosalind_ba2e.txt', 'r') as f:
    inp = f.readline().replace('\n', '').split()
    k = int(inp[0])
    t = int(inp[1])
    for line in f.readlines():
        dnas.append(line.replace('\n', ''))

seq2 = {'A':0, 'C':1, 'G':2, 'T':3}
best = []
for i in range(t):
    best.append(dnas[i][:k])
for i in range(len(dnas[0])+1-k):
    temp = [dnas[0][i:i+k]]
    for j in range(1, t):
        prob = []
        for i2 in range(k):
            seq1 = {'A': 1, 'C': 1, 'G': 1, 'T': 1}
            for m in temp:
                seq1[m[i2]] += 1
            pT = []
            for key in seq1.keys():
                pT.append(seq1[key]/(len(temp)+4))
            prob.append(pT)
        probMax = 0
        for i2 in range(len(dnas[j])+1-k):
            stringT = dnas[j][i2:i2+k]
            probTemp = 1
            for sub in range(len(stringT)):
                probTemp *= prob[sub][seq2[stringT[sub]]]
            if probMax < probTemp:
                probMax = probTemp
                newPattern = stringT
        temp.append(newPattern)
    maxProbString = ''
    for i2 in range(k):
        seq1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for m in temp:
            seq1[m[i2]] += 1
        maximum = 0
        for key in seq1.keys():
            pT = seq1[key] / (len(temp) + 4)
            if pT > maximum:
                maximum = pT
                newGene = key
        maxProbString = maxProbString + newGene
    distance1 = 0
    distance2 = 0
    for m in temp:
        for j in range(k):
            if m[j] != maxProbString[j]:
                distance1 += 1

    maxProbString = ''
    for i2 in range(k):
        seq1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for m in best:
            seq1[m[i2]] += 1
        maximum = 0
        for key in seq1.keys():
            pT = seq1[key] / (len(best) + 4)
            if pT > maximum:
                maximum = pT
                newGene = key
        maxProbString = maxProbString + newGene
    for m in best:
        for j in range(k):
            if m[j] != maxProbString[j]:
                distance2 += 1
    if distance1 < distance2:
        best = temp.copy()

for i in range(len(best)):
    print(best[i])