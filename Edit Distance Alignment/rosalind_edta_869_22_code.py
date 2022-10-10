from Bio import SeqIO
inputs = []
with open('rosalind_edta.fasta', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        inputs.append(str(record.seq))

s1 = inputs[0]
s2 = inputs[1]
n1 = len(s1)
n2 = len(s2)
s11 = ''
s21 = ''
dp = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]

for i in range(n1+1):
    dp[i][0] = i
for i in range(n2+1):
    dp[0][i] = i
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        val1 = 10000000
        val2 = 10000000
        if s1[i - 1] == s2[j - 1]:
            val1 = dp[i - 1][j - 1]
        elif (dp[i - 1][j] + 1) <= (dp[i][j - 1] + 1):
            if (dp[i - 1][j] + 1) <= (dp[i - 1][j - 1] + 1):
                val2 = dp[i - 1][j] + 1
            else:
                val2 = dp[i - 1][j - 1] + 1
        elif (dp[i][j - 1] + 1) <= (dp[i - 1][j - 1] + 1):
            val2 = dp[i][j - 1] + 1
        else:
            val2 = dp[i - 1][j - 1] + 1
        dp[i][j] = min(val1, val2)
i = n1
j = n2
counter = 0
while (i > 0) and (j > 0):
    if (dp[i-1][j-1] == dp[i][j]) and (s1[i-1] == s2[j-1]):
        s11 = str(s1[i-1]) + s11
        s21 = str(s2[j-1]) + s21
        i -= 1
        j -= 1
    elif dp[i][j - 1] + 1 == dp[i][j]:
        counter += 1
        s11 = '-' + s11
        s21 = str(s2[j-1]) + s21
        j -= 1
    elif dp[i - 1][j] + 1 == dp[i][j]:
        s11 = str(s1[i-1]) + s11
        s21 = '-' + s21
        i -= 1
        counter += 1
    elif dp[i - 1][j - 1] + 1 == dp[i][j]:
        s11 = str(s1[i-1]) + s11
        s21 = str(s2[j-1]) + s21
        i -= 1
        j -= 1
        counter += 1


while i > 0:
    s11 = str(s1[i - 1]) + s11
    s21 = '-' + s21
    i -= 1
    counter += 1
while j > 0:
    counter += 1
    s11 = '-' + s11
    s21 = str(s2[j - 1]) + s21
    j -= 1


print(counter)
print(s11)
print(s21)