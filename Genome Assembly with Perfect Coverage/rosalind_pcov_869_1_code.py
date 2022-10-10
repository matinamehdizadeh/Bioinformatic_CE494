kmers = []
with open('rosalind_pcov.txt', 'r') as f:
    for line in f.readlines():
        kmers.append(line.replace('\n',''))

graph = {}
for kmer in kmers:
    if kmer[0:(len(kmer)-1)] not in graph:
        graph[kmer[0:(len(kmer)-1)]] = []
    if [kmer[1:len(kmer)]] not in graph[kmer[0:(len(kmer)-1)]]:
        graph[kmer[0:(len(kmer)-1)]].append([kmer[1:len(kmer)]])

key = list(graph.keys())[0]

string = key[-1]
for i in range(len(graph)-1):
    key = graph[key][0][0]
    string += key[-1]

print(string)