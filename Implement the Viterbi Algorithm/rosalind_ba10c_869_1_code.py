import numpy as np
with open('rosalind_ba10c.txt', 'r') as f:
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

viterbi = np.zeros([len(states), len(string)])
viterbi2 = np.zeros([len(states), len(string)])
maximum = 0
for i in range(len(states)):
    viterbi[i][0] = emission[i][alphabet[string[0]]] / len(states)
for i in range(len(string)-1):
    for j in range(len(states)):
        maximum = 0
        for k in range(len(states)):
            if maximum < viterbi[k][i] * transition[k][j]:
                maximum = viterbi[k][i] * transition[k][j]
                index = k
        viterbi[j][i+1] = emission[j][alphabet[string[i+1]]] * maximum
        viterbi2[j][i+1] = index
final = ''
states2 = {}
for key in states.keys():
    states2[states[key]] = key
maximum = 0
for i in range(len(states2)):
    if viterbi[i][-1] > maximum:
        maximum = viterbi[i][-1]
        index = i
for i in range(len(string)-1, -1, -1):
    final = states2[index] + final
    index = int(viterbi2[index][i])

print(final)