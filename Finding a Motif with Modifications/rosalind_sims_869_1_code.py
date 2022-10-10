from Bio import SeqIO
inputs = []

with open('rosalind_sims.fasta', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        inputs.append(str(record.seq))
s1 = inputs[0]
t1 = inputs[1]
n1 = len(s1)
n2 = len(t1)

dp = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]

maximum = float('-inf')

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        val1 = float('-inf')
        val2 = float('-inf')
        if s1[i-1] == t1[j-1]:
            val1 = dp[i-1][j-1] + 1
        else:
            val2 = max(dp[i-1][j-1] - 1, dp[i][j-1] - 1, dp[i-1][j] - 1)
        dp[i][j] = max(val1, val2)
        if (dp[i][j] > maximum) and (j == len(t1)):
            maximum = dp[i][j]
            first_index = i
            second_index = j


i = first_index
j = second_index
s = ''
t = ''
while (i > 0) and (j > 0):
    if dp[i][j] == dp[i-1][j] - 1:
        s = s1[i - 1] + s
        t = '-' + t
        i -= 1
    elif dp[i][j] == dp[i][j-1] - 1:
        t = t1[j - 1] + t
        s = '-' + s
        j -= 1
    else:
        s = s1[i - 1] + s
        t = t1[j - 1] + t
        i -= 1
        j -= 1

print(maximum)
print(s)
print(t)