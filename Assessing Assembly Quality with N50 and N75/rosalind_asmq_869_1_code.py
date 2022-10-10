dnas = []
with open('rosalind_asmq.txt', 'r') as f:
    for line in f.readlines():
        dnas.append(line.replace('\n',''))
dnas = sorted(dnas, key=len)

total_len = 0
for dna in dnas:
	total_len += len(dna)

n50 = 0
n75 = 0
count = 0
flag50 = True
for i in range(len(dnas)-1, -1, -1):
	count += len(dnas[i])
	if flag50 and ((count/total_len) > 0.5):
		n50 = len(dnas[i])
		flag50 = False
	elif (count/total_len) > 0.75:
		n75 = len(dnas[i])
		break

print(n50, n75)