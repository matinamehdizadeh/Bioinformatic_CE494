kmers = []
with open('rosalind_dbru.txt', 'r') as f:
    for line in f.readlines():
        kmers.append(line.replace('\n',''))
len_kmer = len(kmers)
for i in range(len_kmer):
    string = ''
    i2 = kmers[i][::-1]
    for ii in i2:
        if ii == 'T':
            string += 'A'
        elif ii == 'A':
            string += 'T'
        elif ii == 'G':
            string += 'C'
        elif ii == 'C':
            string += 'G'
    kmers.append(string)

graph = {}
for kmer in kmers:
    if kmer[0:(len(kmer)-1)] not in graph:
        graph[kmer[0:(len(kmer)-1)]] = []
    if [kmer[1:len(kmer)]] not in graph[kmer[0:(len(kmer)-1)]]:
        graph[kmer[0:(len(kmer)-1)]].append([kmer[1:len(kmer)]])

for node in sorted(graph.keys()):
    for j in range(len(graph[node])):
        print("("+str(node)+", "+str(graph[node][j][0])+")")