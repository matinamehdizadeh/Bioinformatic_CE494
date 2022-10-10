from Bio import SeqIO
kmers = []
with open('rosalind_corr.fasta', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        kmers.append(str(record.seq))

len_kmers = len(kmers)
for i in range(len(kmers)):
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
wrongs = []
i = 0
while i < len_kmers:
    if kmers.count(kmers[i]) == 1:
        wrongs.append(kmers[i])
        kmers.remove(kmers[i])
        len_kmers -= 1
    else:
        i += 1
for wrong in wrongs:
    for kmer in kmers:
        counter = 0
        for k in range(len(kmer)):
            if kmer[k] != wrong[k]:
                counter += 1
        if counter == 1:
            print(str(wrong)+'->'+str(kmer))
            break