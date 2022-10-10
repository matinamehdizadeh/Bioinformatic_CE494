import numpy as np

with open('rosalind_ba10k.txt', 'r') as f:
    n = int(f.readline().replace('\n', ''))
    f.readline()
    string = f.readline().replace('\n','')
    f.readline()
    alphabet1 = f.readline().split()
    alphabet = {}
    for i in range(len(alphabet1)):
        alphabet[alphabet1[i]] = i
    f.readline()
    states1 = f.readline().split()
    states = {}
    for i in range(len(states1)):
        states[states1[i]] = i
    f.readline()
    f.readline()
    transition = []
    emission = []

    for i in range(len(states)):
        temp = []
        x = f.readline().split()
        for i in range(1, len(states)+1):
            temp.append(float(x[i]))
        transition.append(temp)
    f.readline()
    f.readline()
    for i in range(len(states)):
        temp = []
        x = f.readline().split()
        for i in range(1, len(alphabet)+1):
            temp.append(float(x[i]))
        emission.append(temp)

for iteration in range(n):
    baum = np.zeros([len(states), len(string)])
    baum2 = np.zeros([len(states), len(string)])
    probTransition = np.zeros([len(states), len(states)])
    probEmission = np.zeros([len(states), len(alphabet)])

    for i in range(len(states)):
        baum[i][0] = emission[i][alphabet[string[0]]] / len(states)
        baum2[i][-1] = 1
    for i in range(len(string)-1):
        i2 = len(string)-1-i
        for j in range(len(states)):
            all1 = 0
            all2 = 0
            for k in range(len(states)):
                all1 += baum[k][i] * transition[k][j]
                all2 += emission[k][alphabet[string[i2]]] * transition[j][k] * baum2[k][i2]

            baum[j][i+1] = emission[j][alphabet[string[i+1]]] * all1
            baum2[j][i2-1] = all2
    sumProb = 0

    for i in range(len(states)):
        sumProb += baum[i][-1]

    for i in range(len(states)):
        for j in range(len(states)):
            all1 = 0
            for k in range(len(string)-1):
                all1 += (baum[i][k] * baum2[j][k+1] * emission[j][alphabet[string[k+1]]] * transition[i][j])
            probTransition[i][j] = all1 / sumProb

        for j in range(len(alphabet)):
            all2 = 0
            for k in range(len(string)):
                if j == alphabet[string[k]]:
                    all2 += (baum[i][k] * baum2[i][k])
            probEmission[i][j] = all2 / sumProb

    for i in range(len(states)):
        sumAll = sum(probTransition[i])
        for j in range(len(states)):
            transition[i][j] = probTransition[i][j]/sumAll
        sumAll = sum(probEmission[i])
        for j in range(len(alphabet)):
            emission[i][j] = probEmission[i][j]/sumAll

for key in states.keys():
    print(key, end='')
    if key != list(states.keys())[-1]:
        print('\t', end='')
print()

counter = 0
for key in states.keys():
    print(key, end='\t')
    for j in range(len(states)):
        print("%.3f" % transition[counter][j], end='')
        if j != len(states)-1:
            print('\t', end='')
    counter += 1
    print()
print('--------')
print('\t', end='')
for key in alphabet.keys():
    print(key, end='')
    if key != list(states.keys())[-1]:
        print('\t', end='')
print()
counter = 0
for key in states.keys():
    print(key, end='\t')
    for j in range(len(alphabet)):
        print("%.3f" % emission[counter][j], end='')
        if j != len(alphabet)-1:
            print('\t', end='')
    counter += 1
    print()