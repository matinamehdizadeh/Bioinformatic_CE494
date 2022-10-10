from Bio import SeqIO

score_matrix = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
                [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
                [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
                [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
                [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
                [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
                [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
                [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
                [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
                [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
                [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
                [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
                [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
                [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
                [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
                [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
                [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
                [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
                [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
                [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]
find_middle = [0, -1, 1, 2, 3, 4, 5, 6, 7, -1, 8, 9, 10, 11, -1, 12, 13, 14, 15, 16, -1, 17, 18, -1, 19, -1]


def middle_score(s1, s2, number):
    n1 = len(s1)
    n2 = len(s2)
    if n2 % 2 != 0:
        if number == 1:
            n2 -= 1
        else:
            n2 += 1
    dp1 = [0] * (len(s1) + 1)
    dp2 = [0] * (len(s1) + 1)
    pre = [0] * (len(s1) + 1)
    if number == 2:
        s1 = s1[::-1]
        s2 = s2[::-1]
    for i in range(n1 + 1):
        dp1[i] = -5 * i
    for i in range(1, int(n2 / 2) + 1):
        for j in range(n1 + 1):
            if j == 0:
                dp2[0] = i * (-5)
            else:
                a = ord(s1[j - 1]) - ord('A')
                b = ord(s2[i - 1]) - ord('A')
                z = dp1[j - 1] + score_matrix[find_middle[a]][find_middle[b]]
                dp2[j] = max(dp1[j] - 5, dp2[j - 1] - 5, z)
                if dp2[j] == z:
                    pre[j] = 0
                elif dp2[j] == dp1[j] - 5:
                    pre[j] = 1
                elif dp2[j] == dp2[j - 1] - 5:
                    pre[j] = 2
        dp1[:] = dp2[:]
    if number == 2:
        dp2.reverse()
        pre.reverse()
    return dp2, pre


def align(s1, t1):
    n1 = len(s1)
    n2 = len(t1)
    dp = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]

    for i in range(n1 + 1):
        dp[i][0] = -5 * i
    for i in range(n2 + 1):
        dp[0][i] = -5 * i

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            a = ord(s1[i - 1]) - ord('A')
            b = ord(t1[j - 1]) - ord('A')
            z = dp[i - 1][j - 1] + score_matrix[find_middle[a]][find_middle[b]]
            dp[i][j] = max((dp[i][j - 1] - 5), (dp[i - 1][j] - 5), z)

    i = n1
    j = n2
    s = ''
    t = ''
    while (i > 0) and (j > 0):
        a = ord(s1[i - 1]) - ord('A')
        b = ord(t1[j - 1]) - ord('A')
        if dp[i][j] == dp[i - 1][j - 1] + score_matrix[find_middle[a]][find_middle[b]]:
            s = s1[i - 1] + s
            t = t1[j - 1] + t
            i -= 1
            j -= 1
        elif dp[i - 1][j] - 5 == dp[i][j]:
            s = s1[i - 1] + s
            t = '-' + t
            i -= 1
        else:
            s = '-' + s
            t = t1[j - 1] + t
            j -= 1
    while i > 0:
        s = str(s1[i - 1]) + s
        t = '-' + t
        i -= 1
    while j > 0:
        s = '-' + s
        t = str(t1[j - 1]) + t
        j -= 1
    return s, t


def linear_space_align(top, bottom, left, right):
    if right == left:
        return [string1[top:bottom], '-' * (bottom - top)]
    elif top == bottom:
        return ['-' * (right - left), string2[left:right]]
    elif (bottom - top == 1) or (right - left == 1):
        return align(string1[top:bottom], string2[left:right])
    else:
        s1 = string1[top:bottom]
        s2 = string2[left:right]
        middle1, b1 = middle_score(s1, s2, 1)
        middle2, b2 = middle_score(s1, s2, 2)
        sumS = [middle2[i] + middle1[i] for i in range(len(middle2))]
        maximum = sumS.index(max(sumS))
        if len(s2) % 2 == 0:
            n22 = len(s2) // 2
        else:
            n22 = (len(s2) - 1) // 2
        first = [maximum + top, n22 + left]
        if maximum == len(sumS) - 1:
            second = [maximum + top, n22 + 1 + left]
        elif b2[maximum] == 1:
            second = [maximum + top, n22 + 1 + left]
        elif b2[maximum] == 2:
            second = [maximum + 1 + top, n22 + left]
        elif b2[maximum] == 0:
            second = [maximum + 1 + top, n22 + 1 + left]

        move = [''] * 2
        if (first[0] == second[0]) and (first[1] == second[1]):
            move = ['-', '-']
        elif first[0] == second[0]:
            move[0] = '-'
            move[1] = string2[first[1]]
        elif first[1] == second[1]:
            move[0] = string1[first[0]]
            move[1] = '-'
        else:
            move[0] = string1[first[0]]
            move[1] = string2[first[1]]

        mid1 = linear_space_align(top, first[0], left, first[1])
        mid2 = linear_space_align(second[0], bottom, second[1], right)
        newStrin1 = mid1[0] + move[0] + mid2[0]
        newStrin2 = mid1[1] + move[1] + mid2[1]
        return newStrin1, newStrin2


inputs = []
with open('rosalind_ba5l.txt') as input_data:
    string1, string2 = [line.strip() for line in input_data]

sFinal, tFinal = linear_space_align(0, len(string1), 0, len(string2))
counter = 0
for i in range(len(sFinal)):
    if (sFinal[i] == '-') or (tFinal[i] == '-'):
        counter -= 5
    else:
        a = ord(sFinal[i]) - ord('A')
        b = ord(tFinal[i]) - ord('A')
        counter += score_matrix[find_middle[a]][find_middle[b]]

print(counter)
print(sFinal)
print(tFinal)